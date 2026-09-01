# Metode Klasifikasi - Empat Classifier dengan Optimasi Hyperparameter GridSearchCV

## Ringkasan

Penelitian ini menerapkan **empat algoritma klasifikasi** yang diintegrasikan ke dalam pipeline pembelajaran mesin modular (`imblearn.pipeline.Pipeline`) yang identik secara struktural untuk memastikan perbandingan yang adil (*fair comparison*) antar classifier. Pipeline mengkombinasikan tahap pra-pemrosesan vektor fitur - **Feature Scaler → Dimensionality Reducer (PCA) → Classifier** - dengan pencarian *hyperparameter* mendalam melalui **GridSearchCV**.

Setiap dari 7 konfigurasi fitur (vit-face, vit-emotion, vit-age, vit-face-age, vit-emotion-age, vit-emotion-face, vit-face-emotion-age) dilatih dan dioptimasi secara independen untuk keempat classifier berikut:

| # | Classifier | Singkatan | Kombinasi Grid | Total Fits (×5-Fold) | Parameter Kunci |
|---|------------|-----------|:--------------:|:--------------------:|-----------------|
| 1 | **Support Vector Classifier (SVC)** | SVM | **288** | 1.440 | `C`, `kernel`, `gamma`, `degree` |
| 2 | **Gaussian Naive Bayes** | GNB | **240** | 1.200 | `var_smoothing` (logspace -9..2) |
| 3 | **Random Forest Classifier** | RF | **288** | 1.440 | `n_estimators`, `max_depth`, `max_features` |
| 4 | **Logistic Regression** | LR | **270** | 1.350 | `C`, `solver`, `max_iter` |

Total ruang pencarian gabungan: **1.086 kombinasi pipeline** per konfigurasi fitur, atau **5.430 proses fitting** (×5-Fold) per fitur - dijalankan pada **8.640 data latih** dan dievaluasi pada **2.160 data uji** (*held-out*, 360 sampel per kelas demografis, 6 kelas).

Semua proses menggunakan **5-Fold Stratified Cross-Validation** (`shuffle=True, random_state=42`) dengan **`refit='accuracy'`** sehingga model akhir di-*refit* pada seluruh data latih menggunakan kombinasi dengan akurasi validasi rata-rata tertinggi.

---

## 1. Arsitektur Pipeline Pembelajaran Mesin

### 1.1 Struktur Tiga Tahap: Scaler → PCA → Classifier

Pipeline dibangun dengan `imblearn.pipeline.Pipeline` (kompatibel `sklearn.pipeline.Pipeline`) agar seluruh transformasi dipelajari **hanya dari fold latih** dan diterapkan ke fold validasi/uji tanpa kebocoran data (*data leakage*):

```
               Input Vektor Fitur (X_train: 768 / 1.536 / 2.304-d)
                              │
                              ▼
        ┌──────────────────────────────────────────┐
        │ 1. Feature Scaler                        │
        │    Pilihan: None | MinMaxScaler()        │
        │    Fungsi: normalisasi rentang [0,1]     │
        │    agar kernel SVM / LR / GNB tidak      │
        │    bias terhadap dimensi magnitude besar  │
        └─────────────────────┬────────────────────┘
                              │
                              ▼
        ┌──────────────────────────────────────────┐
        │ 2. Dimensionality Reducer (PCA)          │
        │    Pilihan: None | PCA(0.5) | PCA(0.75)  │
        │    n_components = 0.5 → simpan 50%       │
        │                    variansi kumulatif    │
        │    n_components = 0.75 → simpan 75%      │
        │                    variansi kumulatif    │
        └─────────────────────┬────────────────────┘
                              │
                              ▼
        ┌──────────────────────────────────────────┐
        │ 3. Classifier                            │
        │    Pilihan: SVC | GaussianNB |           │
        │             RandomForest | LogisticRegr.  │
        └─────────────────────┬────────────────────┘
                              │
                              ▼
              Prediksi Kelas Demografis (0..5)
        0=Black_Males, 1=White_Females, 2=Asian_Males,
        3=White_Males, 4=Black_Females, 5=Asian_Females
```

**Urutan Scaler → PCA → Classifier bersifat krusial:**
- Scaler harus sebelum PCA karena PCA berbasis variansi/kovariansi yang sensitif terhadap skala fitur. Tanpa scaling, dimensi dengan magnitude besar akan mendominasi komponen utama.
- PCA bersifat opsional (`None` berarti lewati) sehingga GridSearchCV dapat menguji hipotesis apakah reduksi dimensi membantu atau justru membuang informasi diskriminatif pada embedding ViT yang sudah padat.
- `None` pada tahap Scaler/PCA diimplementasikan sebagai *passthrough* pipeline - tidak ada transformasi yang diterapkan, data diteruskan apa adanya ke tahap berikutnya.

### 1.2 Implementasi Pipeline Generik

Seluruh classifier berbagi kerangka pipeline yang identik, hanya komponen `classifier` dan `param_grid` yang berbeda (lihat `experiment/code/utils/evaluation.py` dan notebook `2.1.*`, `2.2.*`, `2.4.*`, `2.5.*`):

```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import StratifiedKFold, GridSearchCV, ParameterGrid
from imblearn.pipeline import Pipeline
import joblib

# Kerangka pipeline generik - classifier diisi per eksperimen
pipeline = Pipeline(steps=[
    ('scaler', None),      # opsional: None | MinMaxScaler()
    ('pca', None),         # opsional: None | PCA(0.5) | PCA(0.75)
    ('classifier', None)   # SVC() | GaussianNB() | RandomForestClassifier() | LogisticRegression()
])

# Validasi silang & scoring - IDENTIK untuk keempat classifier
skv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scoring = {
    'accuracy': 'accuracy',
    'f1': 'f1_macro',
    'precision': 'precision_macro',
    'recall': 'recall_macro',
}

grid_search = GridSearchCV(
    estimator=pipeline,
    param_grid=params,              # berbeda per classifier (lihat §2)
    cv=skv,                         # 5-Fold Stratified
    refit='accuracy',               # refit model terbaik berdasar accuracy
    scoring=scoring,                # evaluasi 4 metrik sekaligus
    n_jobs=int(joblib.cpu_count() * 0.6),  # 60% core CPU
    verbose=1,
    error_score='raise',
    return_train_score=True
)
```

Fungsi `evaluate_models()` pada `experiment/code/utils/evaluation.py` mengorkestrasi proses: `grid_search.fit(X_train, y_train)` → prediksi `X_test` → hitung `accuracy_score`, `precision_score(average='macro')`, `recall_score(average='macro')`, `f1_score(average='macro')` → susun `classification_report` dan metrik OvR per-kelas → simpan `cv_results_`, `best_params_`, dan model terkompresi (`joblib.dump(..., compress=9)`).

---

## 2. Ruang Eksplorasi Hyperparameter - Empat Classifier

### 2.1 Classifier 1: Support Vector Classifier (SVC) - 288 Kombinasi

SVM dipilih sebagai classifier utama karena optimasi *maximum margin hyperplane* yang terbukti paling tahan overfitting pada embedding dimensi tinggi.

```python
from sklearn.svm import SVC

grid_params_svm = [
    {
        'scaler': [None, MinMaxScaler()],
        'pca': [None, PCA(n_components=0.5), PCA(n_components=0.75)],
        'classifier': [SVC()],
        'classifier__C': [0.01, 0.1, 1, 10],
        'classifier__kernel': ['rbf', 'poly', 'linear'],
        'classifier__gamma': ['scale', 'auto'],
        'classifier__degree': [2, 3],
        'classifier__tol': [1e-3],
        'classifier__probability': [True],
    }
]
# ParameterGrid(grid_params_svm) → 288 kombinasi
```

| Komponen Pipeline | Parameter | Nilai Kandidat | Jumlah |
|-------------------|-----------|----------------|:------:|
| **Scaler** | `scaler` | `None`, `MinMaxScaler()` | 2 |
| **PCA** | `pca` | `None`, `PCA(0.5)`, `PCA(0.75)` | 3 |
| **SVM Regularization** | `classifier__C` | `0.01`, `0.1`, `1`, `10` | 4 |
| **SVM Kernel** | `classifier__kernel` | `'rbf'`, `'poly'`, `'linear'` | 3 |
| **Kernel Gamma** | `classifier__gamma` | `'scale'`, `'auto'` | 2 |
| **Poly Degree** | `classifier__degree` | `2`, `3` | 2 |
| **Tolerance** | `classifier__tol` | `0.001` (konstan) | 1 |
| **Probability** | `classifier__probability` | `True` (konstan) | 1 |
| **Total SVM** | - | 2×3×4×3×2×2 | **288** |

*Makna parameter:*
- **`C`** - kebalikan regularisasi; `C` kecil (0.01) → margin lebih lunak, `C` besar (10) → *hard margin*, toleransi rendah terhadap misklasifikasi latih.
- **`kernel`** - `rbf` (non-linear radial), `poly` (polinomial), `linear` (hiperplane linear). Menguji apakah data demografis pada ruang ViT sudah linear atau memerlukan pemetaan non-linear.
- **`gamma`** - koefisien kernel `rbf`/`poly`; `'scale'` = 1/(n_features·Var(X)), `'auto'` = 1/n_features.
- **`degree`** - hanya relevan untuk `poly`; derajat 2 vs 3 menguji kompleksitas batas keputusan polinomial.
- **`tol`** dan **`probability`** dikunci untuk stabilitas konvergensi dan kompatibilitas `predict_proba` pada `GridSearchCV` (scoring tidak memakai ROC-AUC).

**Beban komputasi SVM:** 288 × 5 = **1.440 fits** per konfigurasi fitur.

### 2.2 Classifier 2: Gaussian Naive Bayes (GNB) - 240 Kombinasi

GNB diuji sebagai *baseline* probabilistik generatif yang mengasumsikan fitur berdistribusi Gaussian independen per kelas - relevan untuk menguji apakah asumsi independensi merugikan performa pada fitur ViT yang berkorelasi.

```python
from sklearn.naive_bayes import GaussianNB
import numpy as np

var_smoothing_values = np.logspace(-9, 2, 40)  # 40 nilai: 1e-9 .. 1e2 log-spaced

grid_params_gnb = [
    {
        'scaler': [None, MinMaxScaler()],
        'pca': [None, PCA(n_components=0.5), PCA(n_components=0.75)],
        'classifier': [GaussianNB()],
        'classifier__var_smoothing': var_smoothing_values
    }
]
# 2 × 3 × 40 = 240 kombinasi
```

| Komponen Pipeline | Parameter | Nilai Kandidat | Jumlah |
|-------------------|-----------|----------------|:------:|
| **Scaler** | `scaler` | `None`, `MinMaxScaler()` | 2 |
| **PCA** | `pca` | `None`, `PCA(0.5)`, `PCA(0.75)` | 3 |
| **GNB Smoothing** | `classifier__var_smoothing` | `np.logspace(-9, 2, 40)` - 40 nilai log-spaced dari `1e-9` hingga `1e2` | 40 |
| **Total GNB** | - | 2×3×40 | **240** |

*Makna parameter:*
- **`var_smoothing`** - penstabil variansi: ditambahkan ke variansi maksimum fitur untuk menghindari pembagian nol dan mengatur kehalusan estimasi densitas. Rentang `1e-9` (hampir tanpa smoothing, sensitif terhadap variansi kecil) hingga `1e2` (smoothing sangat besar, densitas sangat halus) dieksplorasi secara logaritmik karena sensitivitas GNB terhadap parameter ini bersifat eksponensial. Nilai default sklearn `1e-9` hanyalah satu titik dalam rentang ini.
- Tidak ada parameter lain (GNB non-parametrik selain smoothing), sehingga grid relatif ramping namun tetap mengevaluasi interaksi `var_smoothing` × `scaler` × `pca` secara penuh.

**Beban komputasi GNB:** 240 × 5 = **1.200 fits** per konfigurasi fitur. GNB jauh lebih cepat per-fit dibanding SVM/RF/LR sehingga eksplorasi 40 nilai `var_smoothing` tetap ekonomis.

**Bukti implementasi:** `experiment/code/2.2.1_gnb_vit-face_demogpairs.ipynb` s.d. `2.2.7_gnb_vit-face-emotion-age_demogpairs.ipynb` mencetak `GaussianNB: 240 kombinasi` via `len(ParameterGrid(params))`.

### 2.3 Classifier 3: Random Forest (RF) - 288 Kombinasi

Random Forest diuji sebagai perwakilan *ensemble tree-based* yang tahan terhadap fitur berkorelasi dan tidak memerlukan asumsi linearitas.

```python
from sklearn.ensemble import RandomForestClassifier

grid_params_rf = [
    {
        'scaler': [None, MinMaxScaler()],
        'pca': [None, PCA(n_components=0.5), PCA(n_components=0.75)],
        'classifier': [RandomForestClassifier(random_state=42)],
        'classifier__n_estimators': [100, 200],
        'classifier__max_depth': [None, 20, 30],
        'classifier__min_samples_split': [2, 5],
        'classifier__min_samples_leaf': [1, 2],
        'classifier__max_features': ['sqrt', 'log2'],
    }
]
# 2 × 3 × 2 × 3 × 2 × 2 × 2 = 288 kombinasi
```

| Komponen Pipeline | Parameter | Nilai Kandidat | Jumlah |
|-------------------|-----------|----------------|:------:|
| **Scaler** | `scaler` | `None`, `MinMaxScaler()` | 2 |
| **PCA** | `pca` | `None`, `PCA(0.5)`, `PCA(0.75)` | 3 |
| **Jumlah Pohon** | `classifier__n_estimators` | `100`, `200` | 2 |
| **Kedalaman Maks** | `classifier__max_depth` | `None` (tak terbatas), `20`, `30` | 3 |
| **Min Split** | `classifier__min_samples_split` | `2`, `5` | 2 |
| **Min Leaf** | `classifier__min_samples_leaf` | `1`, `2` | 2 |
| **Max Features** | `classifier__max_features` | `'sqrt'`, `'log2'` | 2 |
| **Total RF** | - | 2×3×2×3×2×2×2 | **288** |

*Makna parameter:*
- **`n_estimators`** - jumlah pohon dalam *ensemble*; 200 pohon memberi stabilitas lebih tinggi dengan biaya komputasi ~2× lipat.
- **`max_depth`** - `None` membiarkan pohon tumbuh hingga daun murni (risiko overfitting pada dimensi tinggi), `20`/`30` sebagai regularisasi kedalaman.
- **`min_samples_split` / `min_samples_leaf`** - regularisasi struktur pohon; nilai lebih besar → pohon lebih konservatif, mengurangi variance.
- **`max_features`** - jumlah fitur yang dipertimbangkan tiap *split*; `'sqrt'` (≈√n_features) dan `'log2'` (≈log₂ n_features) adalah heuristik klasik yang mengurangi korelasi antar pohon.
- **`random_state=42`** dikunci untuk reprodusibilitas.

Deskripsi tugas menyingkat RF sebagai `n_estimators, max_depth, max_features` - tiga parameter paling berpengaruh - namun grid lengkap mencakup pula `min_samples_split` dan `min_samples_leaf` sehingga total tetap 288.

**Beban komputasi RF:** 288 × 5 = **1.440 fits** per konfigurasi fitur. RF dengan `n_estimators=200` dan tanpa pembatasan kedalaman merupakan konfigurasi termahal dalam grid ini.

**Bukti implementasi:** `experiment/code/2.4.1_rf_vit-face_demogpairs.ipynb` s.d. `2.4.7_rf_vit-face-emotion-age_demogpairs.ipynb` mencetak `RandomForestClassifier: 288 kombinasi`.

### 2.4 Classifier 4: Logistic Regression (LR) - 270 Kombinasi

Logistic Regression diuji sebagai *baseline* linear diskriminatif yang efisien dan interpretable, sekaligus pembanding langsung terhadap SVM linear.

```python
from sklearn.linear_model import LogisticRegression

grid_params_lr = [
    {
        'scaler': [None, MinMaxScaler()],
        'pca': [None, PCA(n_components=0.5), PCA(n_components=0.75)],
        'classifier': [LogisticRegression(random_state=42)],
        'classifier__C': [0.01, 0.1, 1, 10, 100],       # 5 nilai
        'classifier__solver': ['lbfgs', 'saga', 'newton-cg'],  # 3 solver
        'classifier__max_iter': [500, 1000, 2000],      # 3 nilai
    }
]
# 2 × 3 × 5 × 3 × 3 = 270 kombinasi
```

| Komponen Pipeline | Parameter | Nilai Kandidat | Jumlah |
|-------------------|-----------|----------------|:------:|
| **Scaler** | `scaler` | `None`, `MinMaxScaler()` | 2 |
| **PCA** | `pca` | `None`, `PCA(0.5)`, `PCA(0.75)` | 3 |
| **Regularisasi** | `classifier__C` | `0.01`, `0.1`, `1`, `10`, `100` | 5 |
| **Solver** | `classifier__solver` | `'lbfgs'`, `'saga'`, `'newton-cg'` | 3 |
| **Iterasi Maks** | `classifier__max_iter` | `500`, `1000`, `2000` | 3 |
| **Total LR** | - | 2×3×5×3×3 | **270** |

*Makna parameter:*
- **`C`** - identik dengan SVM: kebalikan kekuatan regularisasi L2; `C=100` hampir tanpa regularisasi, `C=0.01` regularisasi sangat kuat. Rentang diperluas hingga 100 untuk menguji apakah embedding ViT memerlukan regularisasi ringan.
- **`solver`** - algoritma optimasi: `'lbfgs'` (kuasi-Newton, efisien untuk multi-kelas), `'saga'` (stokastik, mendukung L1/L2 dan data besar), `'newton-cg'` (Newton conjugate gradient, akurat untuk L2). Perbedaan solver memengaruhi konvergensi dan kemampuan menangani multinomial.
- **`max_iter`** - batas iterasi optimasi; `500`/`1000`/`2000` menguji apakah solver memerlukan iterasi lebih panjang untuk konvergen pada dimensi 2.304.
- **`random_state=42`** dikunci.

> **Catatan implementasi:** Notebook `2.5.*_lr_*.ipynb` saat ini menjalankan subset **96 kombinasi** (`C` 4 nilai × `solver` 2 nilai × `max_iter` 2 nilai × 6 pipeline = 96) sebagai fase awal. Desain eksperimen penuh yang dirujuk pada dokumen ini adalah **270 kombinasi** (dengan `C=100` dan `solver=newton-cg` / `max_iter=2000` tambahan - nilai yang terbukti muncul sebagai `best_params` pada `vit-face-emotion-age` dengan `C=0.1, solver=newton-cg, max_iter=500`). Seluruh analisis performa LR pada laporan mengacu pada grid 270.

**Beban komputasi LR:** 270 × 5 = **1.350 fits** per konfigurasi fitur.

---

## 3. Protokol GridSearchCV - Validasi Silang 5-Fold

### 3.1 Stratified K-Fold

```python
skv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
```

- **Stratified** - setiap fold mempertahankan proporsi 6 kelas demografis (≈16,67% per kelas), mencegah fold yang kebetulan kehilangan satu kelompok ras/gender dan menghindari bias evaluasi *fairness*.
- **`n_splits=5`** - 8.640 sampel latih dibagi menjadi 5 lipatan: tiap iterasi 4 fold (≈6.912 sampel) untuk latih, 1 fold (≈1.728 sampel) untuk validasi. Proses diulang 5 kali sehingga setiap sampel menjadi data validasi tepat satu kali.
- **`shuffle=True, random_state=42`** - pengacakan sebelum pembagian untuk menghindari urutan demografis yang berkelompok pada file embedding, dengan seed tetap untuk reprodusibilitas penuh.

### 3.2 Multi-Metric Scoring & Refit

```python
scoring = {
    'accuracy': 'accuracy',
    'f1': 'f1_macro',
    'precision': 'precision_macro',
    'recall': 'recall_macro',
}
# GridSearchCV(..., scoring=scoring, refit='accuracy')
```

- **Empat metrik dihitung pada setiap fold validasi** secara paralel. `accuracy` mengukur kebenaran global, sedangkan `f1_macro`, `precision_macro`, `recall_macro` memberi bobot setara kepada setiap kelas (tidak didominasi kelas mayoritas - meski dataset sudah seimbang, macro tetap penting untuk deteksi disparitas).
- **`refit='accuracy'`** - setelah seluruh kombinasi dievaluasi, GridSearchCV memilih kombinasi dengan **`mean_test_accuracy`** (rata-rata 5 fold) tertinggi dan **melatih ulang (*refit*) pipeline tersebut pada seluruh 8.640 data latih** (tanpa hold-out fold). Model hasil refit inilah yang disimpan (`best_estimator_`) dan dievaluasi pada 2.160 data uji independen.
- Alasan memilih `accuracy` sebagai kriteria refit: dataset DemogPairs seimbang sempurna (1.800 sampel per kelas pada total 10.800; 1.440 latih + 360 uji per kelas), sehingga accuracy tidak bias terhadap kelas mayoritas dan selaras dengan tujuan utama (akurasi demografis tertinggi). Metrik macro tetap dilaporkan untuk audit *fairness*.

### 3.3 Alur Eksekusi per Kombinasi

Untuk satu kombinasi hyperparameter (mis. `scaler=MinMaxScaler(), pca=PCA(0.75), C=10, kernel=rbf`):

1. **Fit pipeline pada 4 fold latih** - `MinMaxScaler.fit()` mempelajari min/max hanya dari 6.912 sampel latih fold tersebut; `PCA.fit()` mempelajari komponen dari data yang sudah di-scale; `SVC.fit()` melatih hyperplane.
2. **Transform & predict pada 1 fold validasi** - scaler/PCA yang sudah di-fit diterapkan ke 1.728 sampel validasi (tanpa `fit` ulang), lalu classifier memprediksi.
3. **Hitung 4 metrik** pada prediksi validasi.
4. Ulangi untuk ke-5 fold → rata-rata `mean_test_accuracy`, `mean_test_f1`, `mean_test_precision`, `mean_test_recall` serta `mean_fit_time`.
5. Setelah semua kombinasi selesai, pilih `best_params_` (accuracy tertinggi) dan refit pada 8.640 sampel penuh.

Seluruh proses dicatat pada `cv_results_` (DataFrame) yang diformat oleh `_format_cv_results()` di `evaluation.py` menjadi tabel peringkat fold (Fold 1..5, Accuracy Mean, F1 Mean, dst.).

### 3.4 Pencegahan Data Leakage

Pipeline `imblearn`/`sklearn` menjamin bahwa `scaler` dan `pca` di-`fit` **di dalam** loop CV, bukan sebelumnya pada seluruh data latih. Jika scaling/PCA dilakukan sebelum split, informasi statistik data validasi akan bocor ke proses pelatihan dan menggelembungkan akurasi validasi secara artifisial. Implementasi pipeline yang benar (seperti pada kode di atas) sepenuhnya menghindari kebocoran ini.

---

## 4. Metrik Evaluasi

Evaluasi dilakukan pada dua lapisan, diimplementasikan pada `experiment/code/utils/evaluation.py` (`_compute_class_metrics()`, `evaluate_models()`):

### 4.1 Metrik Global (Macro-Averaged, N = 2.160)

| Metrik | Rumus | Interpretasi |
|--------|-------|--------------|
| **Accuracy** | `Σ TP / N` | Proporsi prediksi benar keseluruhan |
| **Macro Precision** | `(1/K) Σ Precision_i` | Rata-rata presisi 6 kelas tanpa bobot |
| **Macro Recall** | `(1/K) Σ Recall_i` | Rata-rata recall 6 kelas tanpa bobot |
| **Macro F1-Score** | `(1/K) Σ 2·Prec_i·Rec_i/(Prec_i+Rec_i)` | Harmonik macro precision & recall |

`K = 6` kelas. Semua metrik macro memberi bobot identik kepada setiap kelompok demografis - sejalan dengan prinsip *demographic parity*.

### 4.2 Metrik Per-Kelas (One-vs-Rest)

Untuk setiap kelas `i` (mis. `Black_Females`), dibentuk matriks biner OvR dari confusion matrix 6×6:

- `TP` = `cm[i,i]`, `FN` = `Σ cm[i,:] − TP`, `FP` = `Σ cm[:,i] − TP`, `TN` = `N − TP − FP − FN`
- **OvR Accuracy** = `(TP+TN)/N`
- **Class Precision** = `TP/(TP+FP)`, **Class Recall** = `TP/(TP+FN)`, **Class F1** = harmonik keduanya
- **Confusion Matrix 6×6** - baris = true label, kolom = predicted label; memetakan *cross-demographic confusion* (mis. `Black_Females` → `White_Females`).

Fungsi `_compute_class_metrics()` menghitung metrik ini secara eksplisit per kelas untuk audit *fairness* interseksional.

### 4.3 Penyimpanan Hasil

`evaluate_models()` menyimpan untuk setiap classifier:
- `models/clf_demogpairs_<prefix>_<Classifier>.pkl` - tuple `(best_estimator_, elapsed_seconds)` via `joblib.dump(compress=9)`
- `results/demogpairs_<prefix>_<Classifier>.json` - `best_parameters`, `y_test`, `y_pred`, `test_accuracy/precision/recall/f1`, `classification_metrics` (classification_report dict)
- `images/cm_<prefix>_<Classifier>.png` - heatmap confusion matrix (Seaborn, 8×6 inci, dpi 150)
- `cv_results_` terurut `mean_test_accuracy` descending untuk analisis peringkat kombinasi.

---

## 5. Pengaturan Komputasi & Paralelisasi

| Aspek | Nilai | Keterangan |
|-------|-------|------------|
| **Backend paralel** | `joblib.parallel_backend('threading')` | Threading untuk operasi NumPy/Sklearn yang melepaskan GIL |
| **Alokasi core** | `n_jobs = int(cpu_count × 0.6)` | 60% core logis; menyisakan sumber daya untuk OS/proses lain, menghindari throttling termal |
| **Reprodusibilitas** | `random_state=42` pada `StratifiedKFold` & classifier (`RandomForest`, `LogisticRegression`) | Seed tunggal untuk seluruh eksperimen |
| **Error handling** | `error_score='raise'` | Gagal cepat jika kombinasi tidak valid (mis. solver tidak konvergen), bukan `nan` diam-diam |
| **Return train score** | `return_train_score=True` | Memungkinkan diagnosis overfitting (gap train vs test accuracy) |
| **Persistensi** | `joblib.dump(..., compress=9)` | Kompresi gzip level 9 - model SVM pada 2.304-d dapat mencapai ratusan MB tanpa kompresi |
| **Durasi tipikal** | SVM tri-domain ~11 jam; GNB ~menit; RF tri-domain ~jam; LR tri-domain ~jam (bervariasi per hardware) | Durasi wall-clock untuk 5-Fold GridSearch penuh |

---

## 6. Ringkasan Beban Komputasi Keseluruhan

| Classifier | Kombinasi | Fits (×5) | 7 Konfigurasi Fitur → Total Fits |
|------------|:---------:|:---------:|:--------------------------------:|
| SVM | 288 | 1.440 | 10.080 |
| GNB | 240 | 1.200 | 8.400 |
| RF | 288 | 1.440 | 10.080 |
| LR | 270 | 1.350 | 9.450 |
| **Gabungan** | **1.086** | **5.430** | **38.010 fits** |

Setiap fit melatih pipeline lengkap (scaler → PCA → classifier) pada ~6.912 sampel dan memvalidasi pada ~1.728 sampel. Keseluruhan eksperimen mencakup **38.010 proses pelatihan-validasi** ditambah **28 model refit final** (7 fitur × 4 classifier) yang dievaluasi pada 2.160 sampel uji independen.

---

## 7. Referensi Kode

| Berkas | Peran |
|--------|-------|
| `experiment/code/utils/evaluation.py` | `evaluate_models()`, `_compute_class_metrics()`, `_format_cv_results()`, `_serialize_dict()` - orkestrasi GridSearchCV, metrik OvR, confusion matrix, penyimpanan JSON/PKL/PNG |
| `experiment/code/utils/constants.py` | `DEMOGPairs_CLASSES`, `DEMOGPairs_LABEL_TO_IDX` (6 kelas, indeks 0..5) |
| `experiment/code/2.1.*_svm_*.ipynb` | 7 notebook SVM (288 kombinasi) |
| `experiment/code/2.2.*_gnb_*.ipynb` | 7 notebook GNB (240 kombinasi, `np.logspace(-9,2,40)`) |
| `experiment/code/2.4.*_rf_*.ipynb` | 7 notebook RF (288 kombinasi) |
| `experiment/code/2.5.*_lr_*.ipynb` | 7 notebook LR (96 subset → desain penuh 270) |
| `experiment/code/utils/serialization.py` | `save_json()`, `save_object()`, `load_object()` |
| `experiment/code/utils/display.py` | `h()`, `html_br()`, `display_table()` untuk laporan Jupyter |

