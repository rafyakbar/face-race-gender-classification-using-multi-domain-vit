# Metode Klasifikasi - Empat Classifier dengan Grid Search with Cross-Validation

## Ringkasan

Penelitian menerapkan empat keluarga algoritma klasifikasi dalam pipeline terenkapsulasi yang modular dan identik untuk memastikan perbandingan yang objektif dan adil. Pipeline menggabungkan tahapan: **Feature Scaler $\to$ Dimensionality Reducer (PCA) $\to$ Classifier** dengan optimasi hyperparameter menyeluruh melalui Grid Search with Cross-Validation (GridSearchCV).

Sebagai tanggapan langsung terhadap telaah kritis **IEEE Access Reviewer 2 (Comment #2: Data Leakage, Comment #4: Search Consistency, & Comment #8: Computational Efficiency)** serta **Reviewer 1 (Comment #5: Time Cost)**:
- Protokol GridSearchCV diperbarui dengan pemisahan subjek identitas menggunakan `StratifiedGroupKFold(n_splits=5, shuffle=True, random_state=42)` dengan `groups=groups_train` untuk protokol utama **Subject-Disjoint** (mencegah kebocoran data identitas antar-lipatan).
- Protokol historis **Subject-Overlap** menggunakan `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)` dipertahankan sebagai baseline pembanding.
- Ruang pencarian hyperparameter direkonsiliasi secara presisi: **1.086 konfigurasi per skema fitur**, menghasilkan **38.010 penyesuaian (*fits*) validasi silang**, dan **28 model refit final**.
- Metrik efisiensi komputasi (latensi inferensi per sampel dalam milidetik dan ukuran penyimpanan model dalam megabyte) dicatat dan dilaporkan secara komprehensif.

| Klasifikator | Ruang Kombinasi | Fits per Fitur (5-Fold) | Total Fits (7 Fitur) | Parameter Kunci yang Dioptimasi |
|---|:---:|:---:|:---:|---|
| **Support Vector Classifier (SVM)** | **288** | 1.440 | 10.080 | $C$, kernel (`linear`, `rbf`, `poly`), gamma, degree |
| **Logistic Regression (LR)** | **270** | 1.350 | 9.450 | $C$, solver (`lbfgs`, `saga`, `newton-cg`), max_iter |
| **Random Forest (RF)** | **288** | 1.440 | 10.080 | n_estimators, max_depth, max_features, min_samples_split, min_samples_leaf |
| **Gaussian Naive Bayes (GNB)** | **240** | 1.200 | 8.400 | var_smoothing (rentang logaritmik 40 nilai) |
| **Total Gabungan** | **1.086** | **5.430** | **38.010** | **+ 28 Refit Model Akhir** |

---

## Arsitektur Pipeline Terenkapsulasi

Pipeline klasifikasi dibangun dengan prinsip enkapsulasi ketat (*strict encapsulation*) melalui `sklearn.pipeline.Pipeline` agar seluruh parameter transformasi dipelajari secara eksklusif dari fold pelatihan dan diterapkan pada fold validasi atau uji tanpa ada kebocoran informasi (*data leakage*):

```
Vektor Fitur Input (768 / 1.536 / 2.304-D)
  │
  ├── Tahap 1: Feature Scaler [None | MinMaxScaler]
  │     └── Menstandarkan fitur ke rentang [0, 1] jika diaktifkan
  │
  ├── Tahap 2: Dimensionality Reducer (PCA) [None | n_components=0.5 | n_components=0.75]
  │     └── Reduksi dimensi berbasis varians kumulatif jika diaktifkan
  │
  ├── Tahap 3: Klasifikator [SVM | Logistic Regression | Random Forest | Gaussian Naive Bayes]
  │     └── Estimator utama yang memetakan fitur ke probabilitas kelas
  │
  └── Output: Prediksi Kelas Interseksional (0–5)
        0 = Black_Males      1 = White_Females    2 = Asian_Males
        3 = White_Males      4 = Black_Females    5 = Asian_Females
```

Urutan `Scaler` $\to$ `PCA` $\to$ `Classifier` sangat fundamental karena algoritma Principal Component Analysis (PCA) sangat sensitif terhadap skala varians fitur. Opsi `None` memungkinkan GridSearchCV mengevaluasi secara mandiri apakah penskalaan atau reduksi dimensi memberikan keuntungan generalisasi nyata atau justru menghilangkan informasi diskriminatif halus.

---

## Rincian Rekonsiliasi Ruang Hyperparameter (1.086 Konfigurasi)

Untuk menjawab **Reviewer 2 Comment #4**, rincian matematis ruang pencarian hyperparameter untuk masing-masing klasifikator dijabarkan sebagai berikut:

### 1. Support Vector Classifier (SVM) — 288 Kombinasi
- **Scaler (2):** `[None, MinMaxScaler()]`
- **PCA (3):** `[None, PCA(0.50), PCA(0.75)]`
- **C (4):** `[0.01, 0.1, 1.0, 10.0]`
- **Kernel (3):** `['linear', 'rbf', 'poly']`
- **Gamma (2):** `['scale', 'auto']` (hanya aktif untuk rbf dan poly)
- **Degree (2):** `[2, 3]` (hanya aktif untuk poly)
- **Kombinasi:** $2 \times 3 \times 4 \times [1 (\text{linear}) + 2 (\text{rbf}) + 4 (\text{poly})] = 24 \times 12 = 288$ kombinasi.

### 2. Logistic Regression (LR) — 270 Kombinasi
- **Scaler (2):** `[None, MinMaxScaler()]`
- **PCA (3):** `[None, PCA(0.50), PCA(0.75)]`
- **C (5):** `[0.001, 0.01, 0.1, 1.0, 10.0]`
- **Solver (3):** `['lbfgs', 'saga', 'newton-cg']`
- **Max Iterations (3):** `[500, 1000, 2000]`
- **Kombinasi:** $2 \times 3 \times 5 \times 3 \times 3 = 270$ kombinasi.

### 3. Random Forest (RF) — 288 Kombinasi
- **Scaler (2):** `[None, MinMaxScaler()]`
- **PCA (3):** `[None, PCA(0.50), PCA(0.75)]`
- **n_estimators (2):** `[100, 200]`
- **max_depth (3):** `[None, 20, 30]`
- **max_features (2):** `['sqrt', 'log2']`
- **min_samples_split (2):** `[2, 5]`
- **min_samples_leaf (2):** `[1, 2]`
- **Kombinasi:** $2 \times 3 \times 2 \times 3 \times 2 \times 2 \times 2 = 288$ kombinasi.

### 4. Gaussian Naive Bayes (GNB) — 240 Kombinasi
- **Scaler (2):** `[None, MinMaxScaler()]`
- **PCA (3):** `[None, PCA(0.50), PCA(0.75)]`
- **var_smoothing (40):** 40 nilai terdistribusi logaritmik merata pada rentang $\log_{10} \in [-9, 2]$ (`np.logspace(-9, 2, 40)`).
- **Kombinasi:** $2 \times 3 \times 40 = 240$ kombinasi.

### Total Eksekusi:
$$\text{Total per skema fitur} = 288 + 270 + 288 + 240 = 1.086 \text{ konfigurasi}$$
$$\text{Total validasi silang (5-Fold)} = 1.086 \times 5 = 5.430 \text{ fits per skema fitur}$$
$$\text{Total keseluruhan 7 skema fitur} = 5.430 \times 7 = \mathbf{38.010} \text{ fits}$$
$$\text{Model refit final pada data latih penuh} = 4 \times 7 = \mathbf{28} \text{ model refit}$$

---

## Protokol GridSearchCV: Subject-Disjoint vs. Subject-Overlap

Pencegahan kebocoran data (*data leakage*) pada fase tuning hyperparameter diterapkan secara ketat dengan membedakan kedua protokol:

### 1. Protokol Utama Revisi IEEE Access (Subject-Disjoint Cross-Validation)
- Menggunakan **`StratifiedGroupKFold(n_splits=5, shuffle=True, random_state=42)`**.
- Pengelompokan dilakukan berdasarkan identitas subjek: `groups = groups_train` (di mana `groups_train` berisi `subject_id` dari 480 subjek latih).
- Setiap fold validasi memuat tepat **16 subjek per kelas (total 96 subjek = 1.728 citra)**, sedangkan 4 fold latih memuat **64 subjek per kelas (total 384 subjek = 6.912 citra)**.
- **Tingkat kebocoran identitas antar-lipatan = 0,00%**. Tidak ada subjek yang muncul bersamaan di subset latih dan validasi dalam satu iterasi fold. Hal ini menjawab secara komprehensif kekhawatiran Reviewer 2 Comment #2 mengenai validasi generalisasi sejati.

### 2. Protokol Historis Baseline (Subject-Overlap Cross-Validation)
- Menggunakan **`StratifiedKFold(n_splits=5, shuffle=True, random_state=42)`**.
- Pembagian dilakukan secara terstratifikasi pada tingkat citra tanpa memperhitungkan batas identitas subjek.
- Hasil audit membuktikan bahwa ~572 hingga 581 subjek (~99% identitas) tumpang tindih antara data latih dan validasi pada setiap fold.
- Dipertahankan sebagai baseline historis untuk membedah dampak inflasi akurasi akibat kebocoran informasi identitas.

### Refit dan Kriteria Seleksi Model
- Penilaian (*scoring*) menghitung 4 metrik paralel: `accuracy`, `f1_macro`, `precision_macro`, dan `recall_macro`.
- Kriteria seleksi estimator terbaik menggunakan **`refit='accuracy'`**. Karena dataset seimbang sempurna (1.440 citra per kelas di set latih), akurasi memberikan estimasi performa global yang objektif dan tidak bias.
- Konfigurasi parameter dengan rerata akurasi cross-validation tertinggi di-refit pada seluruh 8.640 data latih, kemudian disimpan sebagai *best estimator*.

---

## Metrik Evaluasi Komprehensif & Profil Efisiensi Komputasi

Seluruh model yang telah dioptimasi dievaluasi secara independen pada dataset uji held-out (2.160 citra):

### 1. Metrik Kinerja Klasifikasi Global & Lokal
- **Metrik Global (Macro-averaged, $N=2.160$):**
  - Akurasi Pengujian (*Test Accuracy*)
  - Macro Precision, Macro Recall, dan Macro F1-Score
  - Interval Kepercayaan 95% Wilson Score (*95% Wilson Confidence Interval*):
    $$\text{CI}_{95\%} = \frac{\hat{p} + \frac{z^2}{2N} \pm z \sqrt{\frac{\hat{p}(1-\hat{p})}{N} + \frac{z^2}{4N^2}}}{1 + \frac{z^2}{N}}, \quad z = 1.95996$$
- **Evaluasi Matriks Konfusi 6×6 & Analisis Keadilan (Fairness OvR):**
  - Perhitungan True Positive (TP), False Negative (FN), False Positive (FP), dan True Negative (TN) untuk setiap kelas demografis.
  - *One-vs-Rest (OvR) Accuracy*: $(TP + TN) / N$.
  - *Equal Opportunity Disparity* (EOD): Disparitas True Positive Rate antar-subkelompok demografis ($\Delta \text{Recall} = \max(\text{Recall}) - \min(\text{Recall})$), merespons catatan Reviewer 2 Comment #6.

### 2. Pengujian Signifikansi Statistik Inferensial (Reviewer 2 #5)
- **Uji McNemar Berpasangan (*Paired McNemar's Test*) dengan Koreksi Kontinuitas Edwards (1948):**
  $$\chi^2 = \frac{(|b - c| - 1)^2}{b + c}$$
  di mana $b$ adalah sampel yang benar pada Model A namun salah pada Model B, dan $c$ adalah sebaliknya.
- **Uji Eksak Binomial (*Exact Binomial Test*):** Diterapkan saat $b + c < 25$.
- Menguji signifikansi perbandingan: Tri-Domain vs Single-Domain (`vit-face`), Tri-Domain vs Dual-Domain (`vit-emotion-face`), dan antar-klasifikator puncak (LR vs SVM).

### 3. Profil Efisiensi Komputasi (Reviewer 1 #5 & Reviewer 2 #8)
Untuk membuktikan klaim kepraktisan dan kelayakan komputasi, penelitian mencatat metrik efisiensi berikut:
- **Latensi Inferensi per Sampel (*Inference Latency*):** Diukur dalam milidetik (ms) per sampel citra pada set uji ($N=2.160$) di bawah kondisi pengujian terstandarisasi.
- **Ukuran Penyimpanan Model (*Model Storage Footprint*):** Diukur dalam megabyte (MB) dari berkas model serial (`joblib` level 9).
- **Temuan Kunci Efisiensi:** Pada protokol Subject-Disjoint, **Logistic Regression Tri-Domain** mencatat performa ekuivalen secara statistik dengan SVM Tri-Domain (Akurasi 88,66% vs 88,61%, McNemar $p = 1,0000$), namun menawarkan keunggulan latensi **>820× lebih cepat** (0,0054 ms vs 4,4481 ms) dan ukuran memori **>330× lebih hemat** (0,11 MB vs 36,60 MB).

---

## Konfigurasi Lingkungan Komputasi

| Parameter Lingkungan | Konfigurasi | Keterangan |
|---|---|---|
| **Pustaka Utama** | `scikit-learn` 1.3+, `joblib`, `numpy`, `scipy` | Algoritma klasifikasi & evaluasi |
| **Backend Paralel** | `threading` (lokal multi-core) | Menghindari overhead duplikasi memori |
| **Alokasi CPU** | 60% logical cores | Menjaga stabilitas sistem |
| **Tingkat Kompresi Model** | `joblib.dump(..., compress=9)` | Efisiensi penyimpanan disk maksimum |
| **Deterministik Seed** | `random_state = 42` | Menjamin replikasi eksperimen 100% |

---

## Referensi File & Implementasi

- `experiment/code/utils/evaluation.py` — Implementasi fungsi orkestrasi GridSearchCV, perhitungan metrik, McNemar test, dan pencatatan latensi/ukuran memori.
- `experiment/code/utils/constants.py` — Pemetaan kanonik 6 kelas interseksional.
- `experiment/01_prepare-data.md` — Spesifikasi partisi Subject-Disjoint vs Subject-Overlap.
- `experiment/05_results.md` — Rekapitulasi lengkap metrik 28 model Subject-Disjoint dan 28 model Subject-Overlap.
- `experiment/code/archive/audit_ledger.json` — Berkas arsip ground-truth metrik efisiensi dan akurasi seluruh 56 model.
