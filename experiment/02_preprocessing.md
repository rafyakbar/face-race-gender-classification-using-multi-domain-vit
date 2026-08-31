# Preprocessing Pipeline — Normalisasi Citra, Ekstraksi Vektor [CLS], dan Transformasi Fitur

## Ringkasan

Pipeline *preprocessing* pada penelitian ini dirancang secara **dua tingkat (*two-level*)** yang saling terpisah namun berurutan, untuk menjamin bahwa setiap citra maupun vektor fitur yang dihasilkan berada pada skala dan distribusi yang konsisten sebelum masuk ke model:

| Tingkat | Tahap | Komponen Utama | Lokasi Kode |
|---------|-------|----------------|-------------|
| **Tingkat 1 — *Image-Level*** | Normalisasi dan standardisasi citra mentah | `AutoImageProcessor` (224 × 224, normalisasi mean/std spesifik model) | `code/utils/extraction.py` → `extract_vit_features()` |
| **Tingkat 2 — *Feature-Level*** | Transformasi dan standardisasi vektor fitur numerik | `MinMaxScaler` (penskalian) dan `PCA` (reduksi dimensi 50% / 75% varians) di dalam `imblearn.pipeline.Pipeline` | `code/2.1.*_svm_*.ipynb` (`grid_params`), `code/utils/evaluation.py` |

Kedua tingkat dieksekusi pada fase yang berbeda: tingkat citra dijalankan **sekali (*offline*)** saat ekstraksi fitur ViT (10.800 citra DemogPairs), sedangkan tingkat fitur dijalankan **di dalam *cross-validation*** (`GridSearchCV`) sehingga setiap *fold* melakukan *fitting* scaler/PCA hanya pada data latih — mencegah *data leakage*.

---

## 1. Preprocessing Tingkat Citra (*Image-Level Preprocessing*)

### 1.1 Tujuan dan Prinsip

`AutoImageProcessor` dari HuggingFace Transformers (dipanggil via `AutoImageProcessor.from_pretrained(model_path)`) adalah *preprocessor* resmi yang menyertai setiap *checkpoint* ViT. Setiap model (Face / Emotion / Age) memiliki nilai `image_mean` dan `image_std` yang berbeda sesuai statistik dataset pra-latihnya, sehingga processor **tidak menggunakan nilai hard-coded** melainkan memuat konfigurasi spesifik model secara otomatis. Seluruh citra DemogPairs distandardisasi ke format identik **224 × 224 piksel, 3 *channel* RGB, tensor float32** agar sesuai dengan ekspektasi *patch embedding* ViT-Base (`vit-base-patch16-224` → 196 patch 16×16 + 1 token [CLS] = 197 token).

### 1.2 Diagram Alir

```
Citra Mentah (JPEG, variasi ukuran / mode warna)
        │
        ▼
┌──────────────────────────────────────────────────┐
│ 1. Pemuatan Citra                                │
│    - Input: path file (str) atau np.ndarray      │
│    - Image.open(path) / Image.fromarray(arr)     │
└──────────────────────────────────────────────────┘
        │
        ▼
┌──────────────────────────────────────────────────┐
│ 2. Verifikasi & Konversi Format Warna            │
│    - if image.mode != 'RGB':                     │
│        image = image.convert('RGB')              │
│    - Menjamin 3 channel (R,G,B), membuang alpha  │
│      / grayscale / CMYK                          │
└──────────────────────────────────────────────────┘
        │
        ▼
┌──────────────────────────────────────────────────┐
│ 3. Spatial Resizing (AutoImageProcessor)         │
│    - Interpolasi bicubic ke 224 × 224 piksel     │
│    - Konfigurasi size diambil dari processor     │
│      config (height=224, width=224)              │
│    - Menjaga aspect ratio via resize + center    │
│      crop sesuai implementasi processor ViT      │
└──────────────────────────────────────────────────┘
        │
        ▼
┌──────────────────────────────────────────────────┐
│ 4. Tensor Normalization (AutoImageProcessor)     │
│    - Rescale: piksel uint8 [0,255] → float [0,1] │
│      (x / 255.0)                                 │
│    - Standardisasi channel-wise:                 │
│      x_norm = (x - mean) / std                   │
│      mean/std = nilai spesifik checkpoint        │
│      (contoh VGGFace ≠ Emotion)                  │
└──────────────────────────────────────────────────┘
        │
        ▼
┌──────────────────────────────────────────────────┐
│ 5. Batch Formatting & Device Allocation          │
│    - return_tensors="pt" → Tensor [1, 3, 224, 224] │
│    - .to(device): cuda jika tersedia, else cpu   │
│    - torch.no_grad() saat inferensi              │
└──────────────────────────────────────────────────┘
        │
        ▼
Input ke Vision Transformer Encoder (model.vit)
        │
        ▼
last_hidden_state [1, 197, 768] → [CLS] token [1, 768]
```

### 1.3 Implementasi Lengkap (`code/utils/extraction.py`)

Fungsi inti `extract_vit_features()` menangani seluruh tingkat citra:

**Catatan penting:**
- `processor(images=image, return_tensors="pt")` secara atomik melakukan resize, rescale, dan normalisasi — tidak ada langkah manual `transforms.Resize`/`Normalize` terpisah.
- `model.vit(**inputs)` mengakses *backbone* ViT tanpa *classification head*, sehingga `last_hidden_state` berisi *hidden state* murni encoder, bukan logit.
- Pemanggilan di notebook ekstraksi selalu dengan `feature_type='cls'` (default) dan `model` yang sudah di-*preload* untuk efisiensi *batch loop*:

### 1.4 Tiga Checkpoint yang Digunakan

| Model | Checkpoint | Domain Pra-latih | Processor Mean/Std |
|-------|------------|------------------|---------------------|
| ViT-Face | `skutaada/VIT-VGGFace` | Identitas wajah (VGGFace) | Sesuai config VGGFace |
| ViT-Emotion | `dima806/facial_emotions_image_detection` | Emosi wajah | Sesuai config Emotion |
| ViT-Age | `dima806/facial_age_image_detection` | Estimasi usia wajah | Sesuai config Age |

Masing-masing processor di-*instantiate* dari `model_path` yang sama dengan model klasifikasi — menjamin konsistensi normalisasi antara fase ekstraksi dan inferensi.

---

## 2. Representasi Token `[CLS]` — Output Tingkat Citra

Arsitektur ViT-Base membagi citra 224 × 224 menjadi **196 patch** berukuran 16 × 16, ditambah **1 token khusus `[CLS]`** di posisi awal urutan (total 197 token sekuens).

```
Citra 224×224
    → 14 × 14 grid patch (16×16) = 196 patch
    → Linear Patch Embedding (768-d) + Positional Embedding
    → Sequence: [CLS] + 196 patch embeddings = [197, 768]
    → 12× Transformer Encoder (Multi-Head Self-Attention, 12 heads)
    → last_hidden_state [1, 197, 768]
    → Ambil indeks 0 → vektor [CLS] [768]
```

Melalui mekanisme *multi-head self-attention* berlapis, token `[CLS]` mengagregasi informasi global seluruh patch wajah menjadi satu deskriptor padat 768-dimensi. Vektor inilah yang disimpan sebagai fitur dan menjadi input bagi tingkat preprocessing selanjutnya.

---

## 3. Preprocessing Tingkat Vektor Fitur (*Feature-Level Preprocessing*)

Setelah ekstraksi offline, setiap citra direpresentasikan sebagai vektor numerik (768-d untuk *single-domain*, 1.536-d untuk *dual-domain*, 2.304-d untuk *tri-domain*). Sebelum masuk ke klasifikasi SVM, vektor-vektor ini melalui transformasi opsional yang **dioptimasi secara sistematis** melalui `GridSearchCV` di dalam `imblearn.pipeline.Pipeline`.

### 3.1 Posisi dalam Pipeline Pembelajaran

```
Input Vektor Fitur (X_train, shape [8640, D])
              │
              ▼
┌──────────────────────────────────────────┐
│ 1. Feature Scaler                        │
│    Pilihan: None | MinMaxScaler()        │
│    (dopelajari hanya pada X_train fold)  │
└─────────────────────┬────────────────────┘
              │
              ▼
┌──────────────────────────────────────────┐
│ 2. Dimensionality Reducer (PCA)          │
│    Pilihan: None | PCA(50%) | PCA(75%)   │
│    (fit pada X_train fold, transform     │
│     X_train & X_val)                     │
└─────────────────────┬────────────────────┘
              │
              ▼
┌──────────────────────────────────────────┐
│ 3. Classifier (SVC)                      │
│    Kernel, C, gamma, degree ...          │
└─────────────────────┬────────────────────┘
              │
              ▼
   Prediksi Kelas Demografis (0..5) — sesuai DEMOGPairs_LABEL_TO_IDX
   0=Black_Males, 1=White_Females, 2=Asian_Males,
   3=White_Males, 4=Black_Females, 5=Asian_Females
```

Implementasi pipeline (identik di seluruh notebook `2.1.*`, `2.2.*`, `2.4.*`, `2.5.*`):

### 3.2 A. Penskalaan Fitur (*Feature Scaling*)

Eksperimen membandingkan **dua opsi** yang dieksplorasi sebagai *hyperparameter* `scaler` dalam *grid*:

| Opsi | Nilai Grid | Perilaku | Formula |
|------|------------|----------|---------|
| **Tanpa penskalaan** | `None` | Mempertahankan distribusi nilai *embedding* asli ViT (`float32`, rentang kontinu hasil LayerNorm transformer) — tidak ada transformasi | — |
| **MinMaxScaler** | `MinMaxScaler()` | Mentransformasi setiap dimensi fitur secara independen ke rentang [0, 1] berdasarkan min–max **data latih pada fold tersebut** | `x_scaled = (x - x_min) / (x_max - x_min)` |

> **Catatan *fitting* yang benar:** Karena scaler berada di dalam `Pipeline`, `fit()` hanya dipanggil pada `X_train` di setiap *fold* CV, lalu `transform()` diterapkan pada `X_val`/`X_test`. Hal ini mencegah *data leakage* — statistik penskalaan tidak pernah melihat data uji.

### 3.3 B. Reduksi Dimensi (*Principal Component Analysis — PCA*)

Eksperimen membandingkan **tiga opsi** berbasis rasio varians kumulatif (`n_components` sebagai *float* 0–1):

| Opsi | Nilai Grid | Makna | Dimensi Keluaran (contoh tri-domain 2.304-d) |
|------|------------|-------|----------------------------------------------|
| **Tanpa PCA** | `None` | Menggunakan seluruh dimensi fitur asli | 768 / 1.536 / 2.304 (utuh) |
| **PCA 50%** | `PCA(n_components=0.5)` | Mempertahankan komponen utama hingga mencakup **50% total varians** data latih | Dinamis — ditentukan oleh *explained variance ratio* |
| **PCA 75%** | `PCA(n_components=0.75)` | Mempertahankan komponen utama hingga **75% total varians** | Dinamis — lebih banyak komponen daripada 50% |

Parameter `n_components=0.5` / `0.75` adalah **rasio varians**, bukan jumlah komponen tetap — `sklearn.decomposition.PCA` secara otomatis memilih `k` terkecil sehingga `Σ explained_variance_ratio_[:k] ≥ threshold`.

### 3.4 Temuan Preprocessing pada Tahap Optimasi (SVM)

Dari **288 kombinasi** yang dievaluasi per model (× 5 *fold* = 1.440 *fits*):

1. **PCA tidak terpilih pada seluruh model terbaik (`pca: None`).** Reduksi dimensi linear menghilangkan detail non-linear halus yang telah diekstrak oleh ViT (terutama informasi tekstur mikro yang relevan untuk membedakan ras/gender), sehingga menurunkan akurasi lintas *fold*.
2. **Penskalaan `scaler: None` optimal pada 6 dari 7 konfigurasi model.** *Embedding* ViT telah memiliki skala yang teratur secara intrinsik berkat *Layer Normalization* di setiap *transformer block*, sehingga penskalaan tambahan tidak memberi keuntungan dan bahkan dapat mengaburkan magnitudo relatif antar dimensi. Hanya konfigurasi gabungan `vit-emotion-face` yang menunjukkan sedikit peningkatan dengan `MinMaxScaler` (kemungkinan karena rentang dinamis kedua domain tersebut paling heterogen).

---

## 4. Konfigurasi Scoring, Paralelisasi, dan Evaluasi

### 4.1 Scoring GridSearchCV — Tanpa `roc_auc_ovr`

Seluruh eksperimen (SVM, GNB, RF, LR — total 28 notebook `2.*`) menggunakan **skor yang identik dan sengaja tanpa `roc_auc_ovr`**:

**Alasan tidak memakai `roc_auc_ovr`:**
- Metrik ROC-AUC *one-vs-rest* memerlukan `predict_proba` / `decision_function` yang tidak konsisten lintas *classifier* (mis. SVM memerlukan `probability=True` yang mahal; GNB/RF/LR memiliki kalibrasi probabilitas berbeda), sehingga perbandingan antar-algoritma menjadi tidak adil.
- Fokus penelitian adalah **klasifikasi 6 kelas demografis** dengan evaluasi berbasis *hard prediction* (akurasi dan F1 makro) serta analisis *fairness* per-kelas via OvR Accuracy dan *confusion matrix*, bukan peringkat probabilitas.
- Menghindari *scoring* ganda yang memperlambat *grid search* (ROC-AUC menambah komputasi `predict_proba` di setiap *fold*).

> **Koreksi terhadap dokumen sebelumnya:** Jika dokumen `04_methods.md` atau `05_results.md` masih menyebut `roc_auc_ovr` / `ROC-AUC OvR` sebagai bagian dari `scoring` GridSearchCV, hal tersebut **tidak sesuai dengan implementasi aktual** di notebook dan `code/utils/evaluation.py`. Scoring aktual hanya 4 metrik di atas.

### 4.2 Paralelisasi — `n_jobs = 60%` CPU Logis

- Nilai dihitung dinamis dari `joblib.cpu_count()` (jumlah *logical cores*), dikali 0,6 dan di-*cast* ke `int`.
- Backend `threading` dipilih agar kompatibel dengan *thread-safety* scikit-learn dan menghindari *overhead fork* pada Windows.
- Estimasi total *fits* per eksperimen: 288 kombinasi × 5 *fold* = **1.440 *fits*** yang didistribusikan ke `n_jobs` *workers*.

### 4.3 Evaluasi — OvR Accuracy & Confusion Matrix Text Array

Evaluasi akhir dilakukan di `code/utils/evaluation.py` oleh fungsi `evaluate_models()` dan `_compute_class_metrics()`, dengan tampilan dibantu `code/utils/display.py`.

#### a) Metrik Global (Makro)

#### b) Metrik Per-Kelas — OvR Accuracy (`_compute_class_metrics`)

Untuk setiap kelas demografis, dihitung metrik *One-vs-Rest* secara eksplisit dari *confusion matrix* 6×6:

Kolom **`OvR Accuracy`** yang tampil di tabel evaluasi (via `display_table()` dari `code/utils/display.py`) adalah `(TP + TN) / Total` — mengukur seberapa baik model membedakan **satu kelas vs. lima kelas lainnya** secara biner. Nilai ini sangat informatif untuk mendeteksi *disparitas demografis* (mis. apakah kelas tertentu lebih sering salah diklasifikasikan).

#### c) Confusion Matrix — Heatmap + Text Array

`evaluate_models()` menghasilkan **dua representasi** *confusion matrix*:

1. **Heatmap PNG** (`seaborn.heatmap`, `annot=True`, `fmt="d"`, `cmap="Blues"`) yang disimpan ke `images/cm_<model>.png` dan ditampilkan *inline* di Jupyter via `printhtml('<img ...>')`:

   
2. **Text array berlabel** yang dicetak ke *stdout* (berguna saat notebook dijalankan sebagai skrip / di terminal tanpa *display* grafis) — diimplementasikan sebagai *loop* manual yang mencetak header kolom dan setiap baris dengan *padding* rata kanan:

   
   Contoh keluaran (6×6, nilai integer cacah prediksi):

   ```
   Confusion Matrix:
                           Asian_Females       Asian_Males     Black_Females       Black_Males     White_Females       White_Males
         Asian_Females               340                 5                 2                 1                 8                 4
           Asian_Males                 6               338                 1                 3                 2                 10
         Black_Females                 2                 1               345                 4                 3                 5
           Black_Males                 1                 4                 3               350                 1                 1
         White_Females                 7                 2                 4                 1               335                11
           White_Males                 5                 9                 2                 1                12               331
   ```

   Format ini dipertahankan **apa adanya** (integer `d`, bukan proporsi) agar pembaca dapat menghitung *support* dan *error rate* per sel tanpa ambiguitas pembulatan.

#### d) Helper Tampilan (`code/utils/display.py`)

- `h(level, text)` — menampilkan *heading* HTML di Jupyter atau `#"*level` di terminal.
- `display_table(data, ...)` — merender `list[dict]` (seperti `class_metrics` atau `fold_results`) sebagai tabel HTML di Jupyter dan teks di terminal; mendukung *pagination* (`n_items`), *column hiding*, dan ekspor Excel.
- `printhtml(html)` / `html_br()` — abstraksi *display* yang otomatis beralih antara `IPython.display.HTML` (notebook) dan `print()` biasa (terminal), dideteksi via `_is_notebook()` / `IS_NOTEBOOK`.

---

## 5. Ringkasan Alur End-to-End

```
Dataset DemogPairs (10.800 citra, 6 kelas, 1.800/kelas)
        │
        ▼ (Tingkat 1: Image-Level, offline)
AutoImageProcessor — resize 224×224, rescale [0,1], (x-mean)/std, to tensor [1,3,224,224]
        │
        ▼
ViT Encoder (12 layer, 768-d) → last_hidden_state [1,197,768] → [CLS] [768]
        │
        ▼
Penyimpanan .pkl (29 MB per domain) — 3 file: vit-face / vit-emotion / vit-age
        │
        ▼ (Feature Fusion — concatenation)
Vektor gabungan: 768 (single) / 1.536 (dual) / 2.304 (tri)
        │
        ▼ (Split: 8.640 train / 2.160 test, stratified)
        │
        ▼ (Tingkat 2: Feature-Level, di dalam CV)
Pipeline(scaler → PCA → SVC)  —  scaler ∈ {None, MinMaxScaler}, pca ∈ {None, 0.5, 0.75}
        │
        ▼
GridSearchCV — 288 kombinasi × 5-fold = 1.440 fits
  scoring={accuracy, f1_macro, precision_macro, recall_macro}  (tanpa roc_auc_ovr)
  refit='accuracy', n_jobs=int(cpu_count*0.6), backend threading
        │
        ▼
Model terbaik (best_params_) → evaluasi pada test set
  → metrik makro (accuracy, precision, recall, F1)
  → metrik per-kelas OvR Accuracy + Precision/Recall/F1
  → confusion matrix: heatmap PNG + text array berlabel
```

---

## 6. Referensi File

| File | Peran |
|------|-------|
| `code/utils/extraction.py` | Definisi `extract_vit_features()` — seluruh logika tingkat citra |
| `code/utils/evaluation.py` | `evaluate_models()`, `_compute_class_metrics()` (OvR Accuracy), `_format_cv_results()`, pencetakan CM text array, penyimpanan heatmap |
| `code/utils/display.py` | `display_table()`, `h()`, `printhtml()`, `html_br()`, deteksi `IS_NOTEBOOK` |
| `code/1.1_vit-*_demogpairs.ipynb` | Eksekusi ekstraksi offline per domain (memanggil `extract_vit_features`) |
| `code/2.1.*_svm_*.ipynb` (7 file) | Definisi `grid_params` (scaler/PCA), `Pipeline`, `GridSearchCV` dengan scoring 4 metrik & `n_jobs=0.6` |
| `code/2.2.*`, `2.4.*`, `2.5.*` | Varian GNB/RF/LR — struktur pipeline & scoring identik |
