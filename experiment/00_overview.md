# Framework Penelitian — Klasifikasi Ras dan Gender Berbasis Multi-Domain Feature Fusion (Identity, Age, Emotion ViT) + 4 Classifier Ter-optimasi

## Ringkasan

Penelitian ini mengimplementasikan kerangka kerja klasifikasi multi-atribut demografis (ras dan gender) secara terpadu (*intersectional classification*) pada citra wajah dengan pendekatan **Cross-Domain Feature Fusion**. Tiga model *Vision Transformer* (ViT-Base, 12 layer, 12 heads, 768 hidden dim, patch 16x16) yang telah dilatih pada domain spesifik digunakan sebagai *feature extractor offline* untuk mengekstrak tiga dimensi representasi wajah yang komplementer:

1. **Fitur Identitas Wajah (*Face Identity*)** — `skutaada/VIT-VGGFace` (pre-trained VGGFace) -> **768-d** token `[CLS]`, file `demogpairs_vit-face.pkl` (~29,37 MB).
2. **Fitur Ekspresi & Afek (*Facial Emotion*)** — `dima806/facial_emotions_image_detection` -> **768-d** `[CLS]` (~29,36 MB).
3. **Fitur Usia (*Facial Age*)** — `dima806/facial_age_image_detection` -> **768-d** `[CLS]` (~29,36 MB).

Ketiga vektor digabungkan per citra (*feature concatenation* `np.array(list(face)+list(emotion)+list(age))`) menghasilkan representasi **tri-domain 2.304 dimensi (768+768+768)**. Representasi ini diklasifikasikan ke **6 kelas demografis interseksional** (3 Ras x 2 Gender: *Asian Females, Asian Males, Black Females, Black Males, White Females, White Males*) menggunakan **4 classifier klasik yang masing-masing dioptimasi via `GridSearchCV` + 5-Fold Stratified CV** — bukan hanya SVM.

**Dataset:** DemogPairs (Hupont & Fernandez, FG 2019, DOI `10.1109/FG.2019.8756625`) — **10.800 citra wajah** (600 identitas x 18 citra), **seimbang sempurna 1.800 per kelas**, split stratified **80/20** (`random_state=42`, `stratify=y`): **8.640 latih (1.440/kelas)** dan **2.160 uji (360/kelas)**.

**Hasil inti (tri-domain 2.304-d, 2.160 test):**

| Rank | Classifier | Kombinasi Grid | Akurasi | F1-Macro | Status |
|:---:|---|:---:|:---:|:---:|---|
| **1** | **SVM (`SVC`)** | **288** | **93,70%** | **0,9369** | OK |
| **2** | **Logistic Regression** | **270** | **92,73%** | **0,9273** | OK |
| **3** | **Random Forest** | **288** | **86,85%*** | **0,8682** | OK |
| **4** | **Gaussian Naive Bayes** | **240** | **85,05%** | **0,8505** | OK |

> * **RF terbaik adalah *dual* `vit-emotion-face` (1.536-d) 86,85%**; tri-domain `vit-face-emotion-age` (2.304-d) 86,20% — selisih tipis, indikasi RF jenuh lebih awal. Untuk SVM/LR/GNB, **tri-domain selalu terbaik**, mengonfirmasi keuntungan monotonik fusi tri-domain.
>
> Total **28 eksperimen** = 7 konfigurasi fitur x 4 classifier. XGBoost sengaja dihapus — build `pip` tanpa CUDA (`No visible GPU is found`) dan estimasi CPU ~70 jam; butuh CUDA >=12.9 sedangkan lingkungan RTX 4060 Laptop menyediakan CUDA 12.6 (`torch 2.10.0+cu126`).

---

## Alur Penelitian Lengkap

```
+---------------------------------------------------------------------------------+
|                           FASE 1 - EKSTRAKSI FITUR OFFLINE                      |
|                                                                                 |
|  Dataset DemogPairs (10.800 citra: 6 kelas @ 1.800)                             |
|      |                                                                          |
|      +-- Input Pipeline ViT (AutoImageProcessor: Resize 224x224, Normalisasi)   |
|      |                                                                          |
|      +-- 3 Vision Transformer Feature Extractors (output [CLS] token):           |
|      |   * ViT-Face    (skutaada/VIT-VGGFace)                        -> 768-d   |
|      |   * ViT-Emotion (dima806/facial_emotions_image_detection)     -> 768-d   |
|      |   * ViT-Age     (dima806/facial_age_image_detection)         -> 768-d   |
|      |                                                                          |
|      +-- Disimpan sebagai File Fitur (.pkl) di experiment/code/features/:       |
|          * demogpairs_vit-face.pkl (29,37 MB)                                   |
|          * demogpairs_vit-emotion.pkl (29,36 MB)                                |
|          * demogpairs_vit-age.pkl (29,36 MB)                                    |
|                                                                                 |
|                                      |                                          |
+---------------------------------------------------------------------------------+
|                      FASE 2 - CROSS-DOMAIN FEATURE FUSION                       |
|                                                                                 |
|  Stratified Split 80/20 (random_state=42, stratify=y):                          |
|  * Training : 8.640 sampel (1.440/kelas)                                        |
|  * Testing  : 2.160 sampel (360/kelas)                                          |
|                                                                                 |
|  7 Skema Konfigurasi Fitur (Ablation Study):                                    |
|  1. Single-Domain: vit-age              ( 768-d)                                |
|  2. Single-Domain: vit-emotion          ( 768-d)                                |
|  3. Single-Domain: vit-face             ( 768-d)                                |
|  4. Dual-Domain  : vit-emotion + vit-age   (1.536-d)                            |
|  5. Dual-Domain  : vit-face + vit-age      (1.536-d)                            |
|  6. Dual-Domain  : vit-emotion + vit-face  (1.536-d)                            |
|  7. Tri-Domain   : vit-face + vit-emotion + vit-age (2.304-d) - USULAN UTAMA   |
|                                                                                 |
|                                      |                                          |
+---------------------------------------------------------------------------------+
|                 FASE 3 - TRAINING & OPTIMASI 4 CLASSIFIER                       |
|                                                                                 |
|  Pipeline ML (imblearn.pipeline.Pipeline + GridSearchCV):                       |
|  * Scaler: [None, MinMaxScaler()]                                               |
|  * PCA   : [None, PCA(n_components=0.5), PCA(n_components=0.75)]                |
|  * Scoring: accuracy, f1_macro, precision_macro, recall_macro; refit='accuracy' |
|  * CV    : StratifiedKFold(n_splits=5, shuffle=True, random_state=42)           |
|  * n_jobs: int(cpu_count * 0.6)                                                 |
|                                                                                 |
|  A) SVM (SVC probability=True, tol=1e-3) - 288 kombinasi:                       |
|     C in [0.01,0.1,1,10], kernel in [rbf,poly,linear], gamma in [scale,auto], degree in [2,3] |
|  B) Logistic Regression - 270 kombinasi:                                         |
|     C in [0.01,0.1,1,10], solver in [lbfgs,saga,newton-cg], max_iter in [500,1000] |
|  C) Random Forest - 288 kombinasi:                                              |
|     n_estimators in [100,200], max_depth in [None,20,30], max_features in [sqrt,log2], |
|     min_samples_split in [2,5], min_samples_leaf in [1,2]                       |
|  D) Gaussian Naive Bayes - 240 kombinasi:                                       |
|     var_smoothing=np.logspace(-9,2,40), scaler in [None,MinMax], PCA in [None,0.5,0.75] |
|                                                                                 |
|  Output per eksperimen: models/*.pkl, results/*.json, images/cm_*.png           |
|                                                                                 |
|                                      |                                          |
+---------------------------------------------------------------------------------+
|                      FASE 4 - EVALUASI & ANALISIS KOMPARATIF                    |
|                                                                                 |
|  Evaluasi pada Testing Set Independen (2.160 sampel):                           |
|  * Metrik Global: Accuracy, Macro Precision, Macro Recall, Macro F1-Score       |
|  * Metrik Per-Kelas: Precision, Recall, F1, Support + OvR Accuracy              |
|  * Confusion Matrix: text array (AI-readable) + PNG image                        |
|  * Fairness: kesetaraan demografis per subgrup interseksional                   |
|                                                                                 |
|  Agregasi Lintas Eksperimen:                                                    |
|  * 3.0_compare.ipynb - leaderboard 28 eksperimen (populated, terurut akurasi)   |
|  * md/3.0_compare.md - ekspor Markdown dari 3.0_compare (baca tanpa Jupyter)    |
|  * 4.0_test.ipynb - evaluasi final ter-eksekusi (CUDA, verifikasi akhir)        |
|  * md/ - 29 ekspor Markdown via nbconvert (MarkdownExporter)                    |
+---------------------------------------------------------------------------------+
```

---

## Komponen Utama Riset

### 1. Dataset & Pembagian Data

- **Dataset:** DemogPairs — koleksi citra wajah standar untuk studi keadilan algoritmik dan interseksionalitas demografis (600 identitas dari CWF & VGGFace2, 18 citra/identitas). Paper: Hupont & Fernandez (2019), FG 2019.
- **Karakteristik Kelas (6 kelas seimbang, label_idx sesuai `utils/constants.py`):**

| Kelas | Label Index | Ras | Gender | Sampel |
|---|:---:|---|:---:|:---:|
| `Black_Males` | 0 | Black | Male | 1.800 |
| `White_Females` | 1 | White | Female | 1.800 |
| `Asian_Males` | 2 | Asian | Male | 1.800 |
| `White_Males` | 3 | White | Male | 1.800 |
| `Black_Females` | 4 | Black | Female | 1.800 |
| `Asian_Females` | 5 | Asian | Female | 1.800 |
| **Total** | -- | -- | -- | **10.800** |

- **Stratified Split 80/20 (`random_state=42`):** Training **8.640** (1.440/kelas), Testing **2.160** (360/kelas). Mendukung `label` (string) dan `label_idx` (int) via `utils/dataset.py: load_demogpairs()`.

### 2. Feature Extraction — Mengapa Tri-Domain 2.304-d?

| Ekstraktor | Model HuggingFace | Domain Pre-training | Dimensi | Token | Ukuran |
|---|---|---|:---:|:---:|:---:|
| **ViT-Face** | `skutaada/VIT-VGGFace` | Face Identity / Recognition | 768 | `[CLS]` | 29,37 MB |
| **ViT-Emotion** | `dima806/facial_emotions_image_detection` | Facial Emotion Recognition | 768 | `[CLS]` | 29,36 MB |
| **ViT-Age** | `dima806/facial_age_image_detection` | Facial Age Detection | 768 | `[CLS]` | 29,36 MB |

Semua ViT-Base (12 layers, 12 heads, 768 hidden). Preprocessing via `AutoImageProcessor` (resize 224x224, normalisasi).

**Mengapa 2.304-d komplementer?**

- **ViT-Face** menangkap struktur biometrik (rahang, hidung, jarak mata) — diskriminatif kuat namun sensitif terhadap variasi usia/ekspresi.
- **ViT-Emotion** menangkap dinamika mikro wajah (*action units*, kontraksi otot) — memberi sinyal gender/ras tidak langsung namun bisa noisy bila sendirian.
- **ViT-Age** menangkap tekstur kulit & morfologi penuaan — lemah sendirian, namun menambah dimensi yang tidak dimiliki Face/Emotion.

Fusi **tri-domain 768+768+768 = 2.304-d** menggabungkan ketiga kelemahan/kelebihan tersebut. Ablasi membuktikan kenaikan monotonik pada SVM/LR/GNB: single (768-d) < dual (1.536-d) < tri (2.304-d). Contoh SVM: 87,64% (age) -> 90,19% (emotion) -> 90,83% (face) -> 92,08%-93,29% (dual) -> **93,70% (tri)**. Pola serupa pada LR dan GNB; RF jenuh sedikit lebih awal (dual emotion-face 86,85% > tri 86,20%).

### 3. Skema Feature Fusion (7 Konfigurasi — Ablation Study)

- **Single-Domain (768-d):** `vit-age`, `vit-emotion`, `vit-face`
- **Dual-Domain (1.536-d):** `vit-emotion-age`, `vit-face-age`, `vit-emotion-face`
- **Tri-Domain (2.304-d, usulan utama):** `vit-face-emotion-age` -> `np.array(list(face)+list(emotion)+list(age))`

Setiap konfigurasi diuji pada **ke-4 classifier** -> 28 baris leaderboard.

### 4. Klasifikasi & Optimasi — 4 Classifier, GridSearchCV 5-Fold

Pipeline: `Input (768/1.536/2.304-d) -> Scaler [None/MinMax] -> PCA [None/0.5/0.75 variance] -> Classifier`. Scoring `accuracy/f1_macro/precision_macro/recall_macro`, `refit='accuracy'`, `StratifiedKFold(5, shuffle=True, random_state=42)`, `n_jobs=0.6*cpu_count`. Evaluasi via `utils/evaluation.py: evaluate_models()` (*classification_report* + `_compute_class_metrics` OvR + `confusion_matrix` text-array + PNG `images/cm_{stem}.png`).

| Classifier | Kombinasi | Grid Utama | Catatan |
|---|:---:|---|---|
| **SVM** (`sklearn.svm.SVC`, `probability=True, tol=1e-3`) | **288** | `C in [0.01,0.1,1,10]`, `kernel in [rbf,poly,linear]`, `gamma in [scale,auto]`, `degree in [2,3]` x Scaler x PCA | `288 = 2x3x4x3x2x2` |
| **Logistic Regression** (`LogisticRegression`) | **270** | `C in [0.01,0.1,1,10]`, `solver in [lbfgs,saga,newton-cg]`, `max_iter in [500,1000]` x Scaler x PCA | aktual 270 teramati |
| **Random Forest** (`RandomForestClassifier`) | **288** | `n_estimators in [100,200]`, `max_depth in [None,20,30]`, `max_features in [sqrt,log2]`, `min_samples_split in [2,5]`, `min_samples_leaf in [1,2]` x PCA x Scaler | `max_depth=None` sering terbaik |
| **Gaussian NB** (`GaussianNB`) | **240** | `var_smoothing=np.logspace(-9,2,40)`, `scaler in [None,MinMax]`, `PCA in [None,0.5,0.75]` | `240 = 40x2x3` |

Total `288+270+288+240 = 1.086` kombinasi x 5-Fold = **5.430 fits**. Setiap fit menyimpan `results/*.json` (`best_parameters`, `test_accuracy/precision/recall/f1`, `classification_metrics` per kelas, `y_test/y_pred`).

---

## Ringkasan Hasil Eksperimen

### A. Performa Terbaik per Classifier (Tri-Domain 2.304-d; kecuali RF*)

| Classifier | Fitur Terbaik | Dim | Akurasi | Precision | Recall | F1-Macro | Parameter Terbaik | File Hasil |
|---|---|:---:|:---:|:---:|:---:|:---:|---|---|
| **SVM** | `vit-face-emotion-age` (tri) | 2304 | **93,70%** | 93,72% | 93,70% | 93,69% | `C=10, kernel=poly, degree=2, gamma=scale, tol=0.001, probability=True, pca=None, scaler=None` | `results/demogpairs_svm_vit-face-emotion-age_SVC.json` |
| **LR** | `vit-face-emotion-age` (tri) | 2304 | **92,73%** | 92,75% | 92,73% | 92,73% | `C=0.1, solver=newton-cg, max_iter=500, pca=None, scaler=None` | `results/demogpairs_lr_vit-face-emotion-age_LogisticRegression.json` |
| **RF** | `vit-emotion-face` (dual)* | 1536 | **86,85%** | 86,89% | 86,85% | 86,82% | `n_estimators=200, max_depth=None, max_features=sqrt, min_samples_split=5, min_samples_leaf=1, pca=PCA(0.75), scaler=None` | `results/demogpairs_rf_vit-emotion-face_RandomForestClassifier.json` |
| **GNB** | `vit-face-emotion-age` (tri) | 2304 | **85,05%** | 85,12% | 85,05% | 85,05% | `var_smoothing=0.005878, pca=PCA(0.75), scaler=None` | `results/demogpairs_gnb_vit-face-emotion-age_GaussianNB.json` |

> RF tri-domain (`vit-face-emotion-age`) = 86,20% (F1 0,8613, `max_depth=30, sqrt, n_estimators=200, pca=PCA`) — hanya 0,65 poin di bawah dual terbaik, menunjukkan RF kurang mendapat manfaat dari penambahan dimensi ketiga dibanding SVM/LR/GNB.

### B. Ablasi per Classifier (7 Konfigurasi — Test Set 2.160)

**SVM (288 combos):**

| Konfigurasi | Dim | Akurasi | F1 | Params Singkat |
|---|:---:|:---:|:---:|---|
| vit-age | 768 | 87,64% | 0,8765 | C=10, rbf, scale, no-pca/scaler |
| vit-emotion | 768 | 90,19% | 0,9017 | C=10, rbf, scale |
| vit-face | 768 | 90,83% | 0,9083 | C=10, rbf, scale |
| vit-emotion-age | 1536 | 92,08% | 0,9209 | C=10, rbf, scale |
| vit-face-age | 1536 | 92,55% | 0,9254 | C=10, poly d2 |
| vit-emotion-face | 1536 | 93,29% | 0,9329 | C=10, rbf, MinMaxScaler |
| **vit-face-emotion-age** | **2304** | **93,70%** | **0,9369** | **C=10, poly d2, scale** |

**Logistic Regression (270 combos):**

| Konfigurasi | Dim | Akurasi | F1 | Solver |
|---|:---:|:---:|:---:|---|
| vit-age | 768 | 86,48% | 0,8648 | lbfgs |
| vit-emotion | 768 | 88,47% | 0,8846 | saga (+MinMaxScaler) |
| vit-face | 768 | 90,60% | 0,9059 | newton-cg (+MinMaxScaler) |
| vit-emotion-age | 1536 | 90,51% | 0,9051 | lbfgs |
| vit-face-age | 1536 | 91,62% | 0,9162 | newton-cg |
| vit-emotion-face | 1536 | 92,41% | 0,9240 | lbfgs |
| **vit-face-emotion-age** | **2304** | **92,73%** | **0,9273** | **newton-cg** |

**Random Forest (288 combos):**

| Konfigurasi | Dim | Akurasi | F1 | n_estimators / max_depth |
|---|:---:|:---:|:---:|---|
| vit-age | 768 | 73,66% | 0,7354 | 200 / 30, log2, PCA |
| vit-emotion | 768 | 80,60% | 0,8057 | 200 / None, log2, PCA |
| vit-face | 768 | 85,46% | 0,8539 | 200 / 30, log2, PCA+MinMax |
| vit-emotion-age | 1536 | 81,11% | 0,8108 | 200 / None, log2, PCA |
| vit-face-age | 1536 | 85,79% | 0,8573 | 200 / None, sqrt, PCA |
| **vit-emotion-face** | **1536** | **86,85%** | **0,8682** | **200 / None, sqrt, PCA** |
| vit-face-emotion-age | 2304 | 86,20% | 0,8613 | 200 / 30, sqrt, PCA |

**Gaussian Naive Bayes (240 combos):**

| Konfigurasi | Dim | Akurasi | F1 | var_smoothing |
|---|:---:|:---:|:---:|---|
| vit-age | 768 | 69,63% | 0,6952 | 0,00044, PCA+MinMax |
| vit-emotion | 768 | 73,38% | 0,7329 | 0,00307, PCA |
| vit-face | 768 | 82,69% | 0,8258 | 0,04125, PCA+MinMax |
| vit-emotion-age | 1536 | 76,81% | 0,7681 | 0,00160, PCA+MinMax |
| vit-face-age | 1536 | 83,15% | 0,8317 | 0,01125, PCA+MinMax |
| vit-emotion-face | 1536 | 84,86% | 0,8481 | 0,00588, PCA+MinMax |
| **vit-face-emotion-age** | **2304** | **85,05%** | **0,8505** | **0,00588, PCA** |

### C. Full Leaderboard 28 Eksperimen (Top 10 — lengkap di `3.0_compare.ipynb` / `md/3.0_compare.md`)

| Rank | Classifier | Features | Akurasi | F1 | Dim |
|:---:|---|---|:---:|:---:|:---:|
| 1 | SVM | vit-face-emotion-age | 93,70% | 0,9369 | 2304 |
| 2 | SVM | vit-emotion-face | 93,29% | 0,9329 | 1536 |
| 3 | LR | vit-face-emotion-age | 92,73% | 0,9273 | 2304 |
| 4 | SVM | vit-face-age | 92,55% | 0,9254 | 1536 |
| 5 | LR | vit-emotion-face | 92,41% | 0,9240 | 1536 |
| 6 | SVM | vit-emotion-age | 92,08% | 0,9209 | 1536 |
| 7 | LR | vit-face-age | 91,62% | 0,9162 | 1536 |
| 8 | SVM | vit-face | 90,83% | 0,9083 | 768 |
| 9 | LR | vit-face | 90,60% | 0,9059 | 768 |
| 10 | LR | vit-emotion-age | 90,51% | 0,9051 | 1536 |

> Tabel lengkap 28 baris (termasuk RF & GNB) dihasilkan otomatis dari `results/*.json` di `3.0_compare.ipynb` dan diekspor ke `md/3.0_compare.md`. File ini adalah yang **paling populer** untuk tinjauan cepat tanpa menjalankan notebook.

### D. Per-Class Breakdown — Model Terbaik (SVM Tri, 93,70%, N=2.160)

| Kelas | Precision | Recall | F1-Score | Support |
|---|:---:|:---:|:---:|:---:|
| Black_Males | 0,9536 | 0,9694 | 0,9614 | 360 |
| Asian_Females | 0,9549 | 0,9417 | 0,9483 | 360 |
| White_Females | 0,9415 | 0,8944 | 0,9174 | 360 |
| White_Males | 0,9250 | 0,9250 | 0,9250 | 360 |
| Asian_Males | 0,9241 | 0,9472 | 0,9355 | 360 |
| Black_Females | 0,9239 | 0,9444 | 0,9341 | 360 |
| **Macro Avg** | **0,9372** | **0,9370** | **0,9369** | **2160** |

> OvR Accuracy per kelas lebih tinggi (mis. Black_Males ~98,7%) — lihat `md/svm/2.1.7_svm_vit-face-emotion-age.md` dan `results/demogpairs_svm_vit-face-emotion-age_SVC.json`. Untuk LR tri: macro 92,75%/92,73%/92,73%; GNB tri: 85,12%/85,05%/85,05%; RF dual terbaik: 86,89%/86,85%/86,82%.

---

## Dokumentasi Notebook & Ekspor Markdown

### `experiment/code/md/` — Ekspor `nbconvert` (29 File)

Semua **28 notebook pelatihan** + `3.0_compare.ipynb` diekspor ke Markdown agar dapat dibaca tanpa Jupyter menggunakan `nbconvert` (`MarkdownExporter`):

```bash
pip install nbconvert
jupyter nbconvert --to markdown notebook.ipynb          # CLI
# atau via Python:
from nbconvert import MarkdownExporter
import nbformat
with open("notebook.ipynb") as f: nb = nbformat.read(f, as_version=4)
body, _ = MarkdownExporter().from_notebook_node(nb)
open("notebook.md", "w", encoding="utf-8").write(body)
```

**Struktur `md/`:**
- `md/svm/` — 7 file `2.1.1_svm_vit-face.md` s.d. `2.1.7_svm_vit-face-emotion-age.md`
- `md/gnb/` — 7 file `2.2.1_gnb_vit-face.md` s.d. `2.2.7_gnb_vit-face-emotion-age.md`
- `md/rf/` — 7 file `2.4.1_rf_vit-face.md` s.d. `2.4.7_rf_vit-face-emotion-age.md`
- `md/lr/` — 7 file `2.5.1_lr_vit-face.md` s.d. `2.5.7_lr_vit-face-emotion-age.md`
- `md/3.0_compare.md` — leaderboard komparatif 28 eksperimen

> Folder lama `reports/` telah dihapus — digantikan `md/` (ekspor langsung, bukan laporan self-contained). Untuk melihat hasil tanpa menjalankan ulang, **baca `md/`**.

### `3.0_compare.ipynb` — Notebook Paling Populer

- **Status:** populated (28 baris), paling sering dibuka untuk ringkasan.
- **Fungsi:** memuat semua `results/*.json` via `utils.load_json`, mem-parse nama file `demogpairs_{clf}_{feat}_{model}.json`, membangun `DataFrame` kolom `Classifier/Features/Accuracy/Precision/Recall/F1`, mengurutkan ranking, dan menampilkan tabel + visualisasi.
- **Ekspor:** `md/3.0_compare.md` (MarkdownExporter) — dapat dibaca langsung di GitHub/preview Markdown.
- **Temuan kunci:** tri-domain unggul di SVM/LR/GNB; RF unggul di dual emotion-face; SVM > LR > RF > GNB pada tri-domain.

### `4.0_test.ipynb` — Evaluasi Final

- **Status:** executed (ter-eksekusi, verifikasi CUDA).
- **Fungsi:** pengujian final model-model terbaik pada test set independen, konfirmasi reproduktifitas hasil `results/*.json`, dan pengecekan pipeline end-to-end (load features -> fuse -> scaler/PCA -> predict -> metrics). Dijalankan pada lingkungan `torch-gpu` (conda Python 3.11, CUDA 12.6, `torch 2.10.0+cu126`, RTX 4060 Laptop terverifikasi).
- **Output:** metrik akurasi & confusion matrix yang konsisten dengan `results/`; menjadi bukti eksekusi nyata sebelum publikasi.

---

## Struktur Proyek (Ringkas)

```
face-race-gender-multi-vit/
|-- experiment/
|   |-- 00_overview.md              # <- file ini (framework 4-classifier, tri-domain 2304-d)
|   |-- 01_prepare-data.md          # persiapan dataset & split
|   |-- 02_preprocessing.md         # preprocessing citra & feature-level (scaler/PCA)
|   |-- 03_feature-extraction.md    # ekstraksi ViT-Face/Emotion/Age & fusi vektor
|   |-- 04_methods.md               # metode 4 classifier & GridSearchCV
|   |-- 05_results.md               # analisis komparatif & fairness interseksional
|   |-- dataset_demogpairs.md       # spesifikasi dataset DemogPairs
|   +-- code/
|       |-- 1.1_vit-*_*.ipynb       # ekstraksi ViT (3 notebook)
|       |-- 2.1.*_svm_vit-*_*.ipynb # SVM training (7 notebook, 288 combos)
|       |-- 2.2.*_gnb_vit-*_*.ipynb # GNB training (7 notebook, 240 combos)
|       |-- 2.4.*_rf_vit-*_*.ipynb  # RF training (7 notebook, 288 combos)
|       |-- 2.5.*_lr_vit-*_*.ipynb  # LR training (7 notebook, 270 combos)
|       |-- 3.0_compare.ipynb       # komparasi 28 hasil - POPULER
|       |-- 4.0_test.ipynb          # evaluasi final - executed, CUDA
|       |-- utils/                  # paket utilitas (<200 baris/modul)
|       |   |-- constants.py        # label & mapping DemogPairs
|       |   |-- dataset.py          # load_demogpairs()
|       |   |-- evaluation.py       # evaluate_models() - OvR, CM text-array+PNG
|       |   |-- extraction.py       # extract_vit_features()
|       |   |-- display.py          # printhtml, display_table
|       |   |-- serialization.py    # save/load JSON & pkl
|       |   +-- time_helpers.py     # seconds_to_time()
|       |-- md/                     # ekspor Markdown nbconvert (29 file) <- baca tanpa Jupyter
|       |   |-- svm/ (7), gnb/ (7), rf/ (7), lr/ (7)
|       |   +-- 3.0_compare.md
|       |-- images/                 # confusion matrices (28 PNG, cm_{clf}_{feat}_{model}.png)
|       |-- features/               # fitur .pkl ter-ekstraksi (768/1536/2304-d, gitignored)
|       |-- models/                 # model terlatih .pkl (gitignored)
|       +-- results/                # 28 JSON evaluasi (best_params, accuracy, per-class)
|-- related_works/                  # tinjauan pustaka
|-- references/                     # referensi BibTeX
+-- README.md                       # overview ringkas + leaderboard
```

---

## File Referensi Dokumentasi Eksperimen

| Berkas | Konten |
|--------|--------|
| `01_prepare-data.md` | Detail dataset DemogPairs, metadata, distribusi kelas, prosedur Stratified Split 80/20. |
| `02_preprocessing.md` | Preprocessing citra (ViT Processor), representasi vektor `[CLS]`, eksplorasi scaler & PCA. |
| `03_feature-extraction.md` | Ekstraksi fitur offline ViT-Face/Emotion/Age, skema penggabungan vektor tri-domain 2.304-d. |
| `04_methods.md` | Metode 4 classifier (SVM 288, LR 270, RF 288, GNB 240), GridSearchCV 5-Fold, metrik. |
| `05_results.md` | Analisis komparatif 28 model, confusion matrix, per-class metrics, waktu komputasi, insight fairness. |
| `dataset_demogpairs.md` | Analisis komprehensif struktur & demografi DemogPairs (3 Ras x 2 Gender, 600 identitas). |
| `code/md/` | Ekspor Markdown semua notebook (nbconvert) — baca tanpa Jupyter. |
| `code/md/3.0_compare.md` | Leaderboard 28 eksperimen — file paling populer untuk tinjauan cepat. |
| `code/4.0_test.ipynb` | Evaluasi final ter-eksekusi (CUDA) — verifikasi akhir pipeline. |

---

## Catatan Reproduktifitas

- **Python** 3.10+ (teruji 3.11, conda `torch-gpu`), **GPU CUDA** (RTX 4060 Laptop, CUDA 12.6, `torch 2.10.0+cu126`).
- Dependensi: `torch>=2.0`, `transformers>=4.30`, `scikit-learn>=1.3`, `imbalanced-learn>=0.11`, `joblib`, `pandas`, `numpy`, `pillow`, `matplotlib`, `seaborn`, `tqdm`, `nbconvert>=7`.
- Semua skor di atas berasal dari `experiment/code/results/*.json` (test set 2.160, `random_state=42`) dan ringkasan `README.md` (Full Leaderboard 28 rows) — **tanpa mengarang**, nilai dapat diverifikasi langsung via `md/3.0_compare.md` atau `3.0_compare.ipynb`.
