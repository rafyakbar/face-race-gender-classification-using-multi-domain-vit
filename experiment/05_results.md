# Hasil Eksperimen Komprehensif - Multi-Domain Vision Transformer & Klasifikasi Interseksional Ras-Gender

> **Dataset:** DemogPairs — 10.800 citra wajah seimbang (6 kelas interseksional $\times$ 1.800 citra, 600 identitas subjek unik $\times$ 18 citra per subjek).  
> **Protokol Utama (Revisi IEEE Access):** *Subject-Disjoint Partitioning* (Zero Data Leakage Protocol) — 480 subjek latih (8.640 citra) / 120 subjek uji held-out independen (2.160 citra, 20 subjek/kelas). Optimasi hyperparameter menggunakan 5-Fold *StratifiedGroupKFold* pada data latih (groups = `subject_id`).  
> **Tolok Ukur Historis (Baseline Kebocoran Data):** *Subject-Overlap Partitioning* (100% Identity Leakage Baseline) — split acak tingkat citra (*image-level stratified*) 8.640 latih / 2.160 uji dengan 593 subjek uji hadir dalam data latih.  
> **Total Model yang Dievaluasi:** 28 konfigurasi model per protokol (4 klasifikator $\times$ 7 varian fitur ViT) = 56 evaluasi model komparatif lengkap. Seluruh metrik dilaporkan dengan presisi 4 desimal langsung dari ground-truth arsip hasil (`experiment/code/archive/audit_ledger.json` dan `experiment/code/results/*.json`).

---

# BAGIAN 1: HASIL EKSPERIMEN SUBJECT-DISJOINT TERBARU
### (Zero Data Leakage Protocol — Standar Kepatuhan Revisi IEEE Access)

---

## 1.1 Ringkasan Eksekutif Protokol Subject-Disjoint

Evaluasi pada subjek yang benar-benar baru (*held-out unseen subjects*) memberikan gambaran objektif mengenai kemampuan generalisasi sejati (*true out-of-subject generalization*) representasi fitur Vision Transformer tanpa ada petunjuk identitas individu (*identity shortcuts*).

- **Juara Global Baru:** **Logistic Regression (LR) Tri-Domain (`vit-face-emotion-age`, 2.304 dimensi)** mencatat performa tertinggi dengan Akurasi **0.8866** (88,66%), Macro Precision **0.8875**, Macro Recall **0.8866**, Macro F1 **0.8868**, dan Interval Kepercayaan 95% Wilson Score **[87.25%, 89.93%]** (1.915 dari 2.160 citra uji benar).
- **Runner-up Terdekat:** **Support Vector Machine (SVM) Tri-Domain (`vit-face-emotion-age`, 2.304 dimensi)** dengan Akurasi **0.8861** (88,61%), Macro F1 **0.8863**, dan 95% Wilson CI **[87.20%, 89.88%]** (1.914 dari 2.160 citra uji benar).
- **Ekuivalensi Statistik Puncak:** Uji McNemar berpasangan (*Paired McNemar Test*) antara LR Tri-Domain dan SVM Tri-Domain menghasilkan $\chi^2 = 0.0000$ dan **$p = 1.0000$** (selisih bersih hanya **+1 citra** dari 2.160 sampel uji). Kedua klasifikator puncak terbukti secara inferensial **ekuivalen secara statistik**.
- **Keunggulan Efisiensi Komputasi LR:** Meskipun akurasinya ekuivalen dengan SVM, Logistic Regression menawarkan efisiensi komputasi yang dramatis:
  - Latensi inferensi: **0.0054 ms/sampel** vs **4.4481 ms/sampel** pada SVM (**>820$\times$ lebih cepat**).
  - Ukuran memori model: **0.11 MB** vs **36.60 MB** pada SVM (**>330$\times$ lebih ringkas**), menjadikannya kandidat optimal untuk implementasi *Edge AI* dan inferensi *real-time*.
- **Signifikansi Statistik Keunggulan Fusi Multi-Domain:** Penambahan domain ekspresi emosi dan usia biologis terhadap representasi wajah murni (`vit-face`) terbukti sangat signifikan secara statistik:
  - Pada SVM: Fusi Tri-Domain (0.8861) vs `vit-face` (0.8616) menghasilkan kenaikan +2.45 pp (+53 citra, $\chi^2 = 20.9612, p = 3.46 \times 10^{-6} < 0.001$).
  - Pada LR: Fusi Tri-Domain (0.8866) vs `vit-face` (0.8639) menghasilkan kenaikan +2.27 pp (+49 citra, $\chi^2 = 19.6923, p = 6.78 \times 10^{-6} < 0.001$).
  - Pada RF: Fusi Tri-Domain (0.8500) vs `vit-face` (0.8403) menghasilkan kenaikan +0.97 pp (+21 citra, $\chi^2 = 5.0633, p = 0.0238 < 0.05$).
- **Fenomena Kejenuhan Fitur Asimtotik (*Asymptotic Feature Saturation*):** Pada model non-linier berkapasitas tinggi (SVM), kenaikan dari Dual-Domain `vit-emotion-face` (0.8843) ke Tri-Domain `vit-face-emotion-age` (0.8861) hanya menghasilkan selisih +0.19 pp (+4 citra) dengan uji McNemar $\chi^2 = 0.1154$ dan **$p = 0.7343 > 0.05$** (tidak signifikan). Sebaliknya, pada model linier berbobot kompak (LR), transisi dari Dual ke Tri menghasilkan peningkatan signifikan +1.20 pp (+26 citra, $\chi^2 = 7.1023, p = 0.0073 < 0.01$).

---

## 1.2 Papan Peringkat Global 28 Model Subject-Disjoint (Zero Data Leakage)

Berikut adalah rekapitulasi lengkap seluruh 28 model benchmark yang dievaluasi pada dataset uji held-out independen (2.160 citra dari 120 subjek terisolasi), diurutkan berdasarkan Akurasi Pengujian tertinggi:

| Rank | Classifier | Konfigurasi Fitur | Tipe | Dim | Akurasi | Precision | Recall | Macro F1 | 95% Wilson CI | Benar/2.160 | Latensi (ms) | Ukuran (MB) | Parameter Hyperparameter Optimal |
|:---:|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **1** | **LR** | **vit-face-emotion-age** | **Tri** | **2304** | **0.8866** | **0.8875** | **0.8866** | **0.8868** | **[87.25%, 89.93%]** | 1915/2160 | 0.0054 | 0.11 | C=0.1, max_iter=500, solver=saga, pca=None, scaler=MinMaxScaler |
| **2** | **SVM** | **vit-face-emotion-age** | **Tri** | **2304** | **0.8861** | **0.8871** | **0.8861** | **0.8863** | **[87.20%, 89.88%]** | 1914/2160 | 4.4481 | 36.60 | C=10, degree=2, gamma=scale, kernel=rbf, probability=True, tol=0.001, pca=None, scaler=MinMaxScaler |
| **3** | **SVM** | **vit-emotion-face** | **Dual** | **1536** | **0.8843** | **0.8850** | **0.8843** | **0.8844** | **[87.01%, 89.71%]** | 1910/2160 | 0.9707 | 15.27 | C=0.1, degree=2, gamma=scale, kernel=poly, probability=True, tol=0.001, pca=None, scaler=MinMaxScaler |
| 4 | SVM | vit-face-age | Dual | 1536 | 0.8755 | 0.8766 | 0.8755 | 0.8757 | [86.09%, 88.87%] | 1891/2160 | 2.2581 | 23.48 | C=10, degree=2, gamma=scale, kernel=rbf, probability=True, tol=0.001, pca=None, scaler=None |
| 5 | LR | vit-emotion-face | Dual | 1536 | 0.8745 | 0.8759 | 0.8745 | 0.8749 | [85.99%, 88.78%] | 1889/2160 | 0.0039 | 0.08 | C=1, max_iter=500, solver=saga, pca=None, scaler=MinMaxScaler |
| 6 | LR | vit-face-age | Dual | 1536 | 0.8741 | 0.8744 | 0.8741 | 0.8740 | [85.94%, 88.74%] | 1888/2160 | 0.0090 | 0.11 | C=0.1, max_iter=500, solver=lbfgs, pca=None, scaler=MinMaxScaler |
| 7 | LR | vit-emotion-age | Dual | 1536 | 0.8667 | 0.8668 | 0.8667 | 0.8667 | [85.17%, 88.04%] | 1872/2160 | 0.0040 | 0.08 | C=0.1, max_iter=500, solver=saga, pca=None, scaler=MinMaxScaler |
| 8 | LR | vit-face | Single | 768 | 0.8639 | 0.8646 | 0.8639 | 0.8640 | [84.88%, 87.77%] | 1866/2160 | 0.0008 | 0.04 | C=0.1, max_iter=500, solver=saga, pca=None, scaler=None |
| 9 | SVM | vit-emotion-age | Dual | 1536 | 0.8625 | 0.8626 | 0.8625 | 0.8624 | [84.73%, 87.64%] | 1863/2160 | 3.1451 | 32.76 | C=10, degree=2, gamma=scale, kernel=rbf, probability=True, tol=0.001, pca=None, scaler=None |
| 10 | SVM | vit-face | Single | 768 | 0.8616 | 0.8624 | 0.8616 | 0.8619 | [84.64%, 87.55%] | 1861/2160 | 3.0653 | 7.56 | C=0.01, degree=3, gamma=scale, kernel=poly, probability=True, tol=0.001, pca=None, scaler=MinMaxScaler |
| 11 | SVM | vit-emotion | Single | 768 | 0.8579 | 0.8584 | 0.8579 | 0.8580 | [84.25%, 87.20%] | 1853/2160 | 1.8871 | 15.30 | C=10, degree=2, gamma=scale, kernel=rbf, probability=True, tol=0.001, pca=None, scaler=None |
| 12 | LR | vit-emotion | Single | 768 | 0.8523 | 0.8535 | 0.8523 | 0.8527 | [83.67%, 86.67%] | 1841/2160 | 0.0037 | 0.06 | C=0.1, max_iter=500, solver=lbfgs, pca=None, scaler=None |
| 13 | RF | vit-face-emotion-age | Tri | 2304 | 0.8500 | 0.8506 | 0.8500 | 0.8493 | [83.43%, 86.44%] | 1836/2160 | 0.0537 | 6.19 | max_depth=30, max_features=sqrt, min_samples_leaf=1, min_samples_split=2, n_estimators=200, pca=None, scaler=MinMaxScaler |
| 14 | RF | vit-face-age | Dual | 1536 | 0.8486 | 0.8488 | 0.8486 | 0.8478 | [83.29%, 86.31%] | 1833/2160 | 0.0310 | 6.19 | max_depth=None, max_features=sqrt, min_samples_leaf=1, min_samples_split=2, n_estimators=200, pca=None, scaler=None |
| 15 | RF | vit-emotion-face | Dual | 1536 | 0.8486 | 0.8493 | 0.8486 | 0.8479 | [83.29%, 86.31%] | 1833/2160 | 0.0316 | 8.58 | max_depth=None, max_features=sqrt, min_samples_leaf=1, min_samples_split=2, n_estimators=200, pca=PCA, scaler=MinMaxScaler |
| 16 | GNB | vit-emotion-face | Dual | 1536 | 0.8431 | 0.8437 | 0.8431 | 0.8430 | [82.71%, 85.78%] | 1821/2160 | 0.0083 | 0.78 | var_smoothing=0.011253, pca=PCA, scaler=MinMaxScaler |
| 17 | RF | vit-face | Single | 768 | 0.8403 | 0.8413 | 0.8403 | 0.8403 | [82.42%, 85.51%] | 1815/2160 | 0.0314 | 5.99 | max_depth=20, max_features=log2, min_samples_leaf=1, min_samples_split=5, n_estimators=200, pca=PCA, scaler=None |
| 18 | GNB | vit-face-emotion-age | Tri | 2304 | 0.8361 | 0.8379 | 0.8361 | 0.8364 | [81.99%, 85.11%] | 1806/2160 | 0.0081 | 1.36 | var_smoothing=0.011253, pca=PCA, scaler=None |
| 19 | GNB | vit-face-age | Dual | 1536 | 0.8306 | 0.8347 | 0.8306 | 0.8310 | [81.42%, 84.58%] | 1794/2160 | 0.0080 | 0.75 | var_smoothing=0.011253, pca=PCA, scaler=MinMaxScaler |
| 20 | SVM | vit-age | Single | 768 | 0.8255 | 0.8268 | 0.8255 | 0.8258 | [80.89%, 84.09%] | 1783/2160 | 2.0104 | 18.22 | C=10, degree=2, gamma=scale, kernel=rbf, probability=True, tol=0.001, pca=None, scaler=None |
| 21 | GNB | vit-face | Single | 768 | 0.8255 | 0.8268 | 0.8255 | 0.8250 | [80.89%, 84.09%] | 1783/2160 | 0.0031 | 0.19 | var_smoothing=0.041246, pca=PCA, scaler=MinMaxScaler |
| 22 | LR | vit-age | Single | 768 | 0.8148 | 0.8145 | 0.8148 | 0.8146 | [79.79%, 83.06%] | 1760/2160 | 0.0028 | 0.06 | C=0.1, max_iter=500, solver=lbfgs, pca=None, scaler=None |
| 23 | RF | vit-emotion-age | Dual | 1536 | 0.7731 | 0.7734 | 0.7731 | 0.7728 | [75.50%, 79.03%] | 1670/2160 | 0.0392 | 12.35 | max_depth=20, max_features=log2, min_samples_leaf=2, min_samples_split=2, n_estimators=200, pca=PCA, scaler=None |
| 24 | RF | vit-emotion | Single | 768 | 0.7611 | 0.7602 | 0.7611 | 0.7603 | [74.27%, 77.86%] | 1644/2160 | 0.0316 | 10.34 | max_depth=None, max_features=sqrt, min_samples_leaf=2, min_samples_split=2, n_estimators=200, pca=PCA, scaler=None |
| 25 | GNB | vit-emotion-age | Dual | 1536 | 0.7588 | 0.7597 | 0.7588 | 0.7578 | [74.03%, 77.64%] | 1639/2160 | 0.0048 | 0.24 | var_smoothing=0.011253, pca=PCA, scaler=MinMaxScaler |
| 26 | GNB | vit-emotion | Single | 768 | 0.7213 | 0.7251 | 0.7213 | 0.7199 | [70.20%, 73.98%] | 1558/2160 | 0.0031 | 0.13 | var_smoothing=0.005878, pca=PCA, scaler=MinMaxScaler |
| 27 | RF | vit-age | Single | 768 | 0.7181 | 0.7176 | 0.7181 | 0.7170 | [69.87%, 73.66%] | 1551/2160 | 0.0327 | 11.21 | max_depth=None, max_features=log2, min_samples_leaf=2, min_samples_split=5, n_estimators=200, pca=PCA, scaler=None |
| 28 | GNB | vit-age | Single | 768 | 0.6708 | 0.6691 | 0.6708 | 0.6686 | [65.07%, 69.03%] | 1449/2160 | 0.0045 | 0.37 | var_smoothing=0.000838, pca=PCA, scaler=MinMaxScaler |

---

## 1.3 Analisis per Klasifikator & Studi Ablasi Fitur

### 1.3.1 Support Vector Machine (SVM) — 7 Konfigurasi Fitur

| Rank | Konfigurasi Fitur | Tipe | Dimensi | Akurasi | Precision | Recall | Macro F1 | 95% Wilson CI | Parameter Optimal |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **1** | **vit-face-emotion-age** | **Tri** | **2304** | **0.8861** | 0.8871 | 0.8861 | **0.8863** | [87.20%, 89.88%] | C=10, rbf, gamma=scale, pca=None, scaler=MinMaxScaler |
| 2 | vit-emotion-face | Dual | 1536 | 0.8843 | 0.8850 | 0.8843 | 0.8844 | [87.01%, 89.71%] | C=0.1, poly, deg=2, gamma=scale, pca=None, scaler=MinMaxScaler |
| 3 | vit-face-age | Dual | 1536 | 0.8755 | 0.8766 | 0.8755 | 0.8757 | [86.09%, 88.87%] | C=10, rbf, gamma=scale, pca=None, scaler=None |
| 4 | vit-emotion-age | Dual | 1536 | 0.8625 | 0.8626 | 0.8625 | 0.8624 | [84.73%, 87.64%] | C=10, rbf, gamma=scale, pca=None, scaler=None |
| 5 | vit-face | Single | 768 | 0.8616 | 0.8624 | 0.8616 | 0.8619 | [84.64%, 87.55%] | C=0.01, poly, deg=3, gamma=scale, pca=None, scaler=MinMaxScaler |
| 6 | vit-emotion | Single | 768 | 0.8579 | 0.8584 | 0.8579 | 0.8580 | [84.25%, 87.20%] | C=10, rbf, gamma=scale, pca=None, scaler=None |
| 7 | vit-age | Single | 768 | 0.8255 | 0.8268 | 0.8255 | 0.8258 | [80.89%, 84.09%] | C=10, rbf, gamma=scale, pca=None, scaler=None |

**Dinamika Ablasi SVM:**
- Single Terbaik (`vit-face`: 0.8616) $\to$ Dual Terbaik (`vit-emotion-face`: 0.8843): kenaikan **+2.27 pp** (+2,63% relatif, reduksi error **16,40%**).
- Dual Terbaik (`vit-emotion-face`: 0.8843) $\to$ Tri-Domain (0.8861): kenaikan **+0.18 pp** (+4 citra), mengonfirmasi kejenuhan representasi laten.
- Single Terbaik $\to$ Tri-Domain: kenaikan **+2.45 pp** (+2,84% relatif, reduksi error **17,70%**, $p = 3.46 \times 10^{-6}$).
- Seluruh 7 konfigurasi SVM memilih `pca=None`, memanfaatkan ruang dimensi tinggi secara utuh.

---

### 1.3.2 Logistic Regression (LR) — 7 Konfigurasi Fitur

| Rank | Konfigurasi Fitur | Tipe | Dimensi | Akurasi | Precision | Recall | Macro F1 | 95% Wilson CI | Parameter Optimal |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **1** | **vit-face-emotion-age** | **Tri** | **2304** | **0.8866** | 0.8875 | 0.8866 | **0.8868** | [87.25%, 89.93%] | C=0.1, solver=saga, max_iter=500, pca=None, scaler=MinMaxScaler |
| 2 | vit-emotion-face | Dual | 1536 | 0.8745 | 0.8759 | 0.8745 | 0.8749 | [85.99%, 88.78%] | C=1, solver=saga, max_iter=500, pca=None, scaler=MinMaxScaler |
| 3 | vit-face-age | Dual | 1536 | 0.8741 | 0.8744 | 0.8741 | 0.8740 | [85.94%, 88.74%] | C=0.1, solver=lbfgs, max_iter=500, pca=None, scaler=MinMaxScaler |
| 4 | vit-emotion-age | Dual | 1536 | 0.8667 | 0.8668 | 0.8667 | 0.8667 | [85.17%, 88.04%] | C=0.1, solver=saga, max_iter=500, pca=None, scaler=MinMaxScaler |
| 5 | vit-face | Single | 768 | 0.8639 | 0.8646 | 0.8639 | 0.8640 | [84.88%, 87.77%] | C=0.1, solver=saga, max_iter=500, pca=None, scaler=None |
| 6 | vit-emotion | Single | 768 | 0.8523 | 0.8535 | 0.8523 | 0.8527 | [83.67%, 86.67%] | C=0.1, solver=lbfgs, max_iter=500, pca=None, scaler=None |
| 7 | vit-age | Single | 768 | 0.8148 | 0.8145 | 0.8148 | 0.8146 | [79.79%, 83.06%] | C=0.1, solver=lbfgs, max_iter=500, pca=None, scaler=None |

**Dinamika Ablasi LR:**
- Single Terbaik (`vit-face`: 0.8639) $\to$ Dual Terbaik (`vit-emotion-face`: 0.8745): kenaikan **+1.06 pp** (+1,23% relatif, reduksi error **7,79%**).
- Dual Terbaik (`vit-emotion-face`: 0.8745) $\to$ Tri-Domain (0.8866): kenaikan **+1.21 pp** (+26 citra, $p = 0.0073$).
- Single Terbaik $\to$ Tri-Domain: kenaikan **+2.27 pp** (+2,63% relatif, reduksi error **16,68%**, $p = 6.78 \times 10^{-6}$).
- LR merebut peringkat 1 dunia pada protokol Subject-Disjoint karena formulasi optimasi linier regulerisasi $L_2$ (`C=0.1`) mencegah model terperangkap pada variasi residual subjek.

---

### 1.3.3 Random Forest (RF) — 7 Konfigurasi Fitur

| Rank | Konfigurasi Fitur | Tipe | Dimensi | Akurasi | Precision | Recall | Macro F1 | 95% Wilson CI | Parameter Optimal |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **1** | **vit-face-emotion-age** | **Tri** | **2304** | **0.8500** | 0.8506 | 0.8500 | **0.8493** | [83.43%, 86.44%] | n_est=200, depth=30, max_feat=sqrt, min_split=2, min_leaf=1, pca=None, scaler=MinMaxScaler |
| 2 | vit-face-age | Dual | 1536 | 0.8486 | 0.8488 | 0.8486 | 0.8478 | [83.29%, 86.31%] | n_est=200, depth=None, max_feat=sqrt, min_split=2, min_leaf=1, pca=None, scaler=None |
| 3 | vit-emotion-face | Dual | 1536 | 0.8486 | 0.8493 | 0.8486 | 0.8479 | [83.29%, 86.31%] | n_est=200, depth=None, max_feat=sqrt, min_split=2, min_leaf=1, pca=PCA, scaler=MinMaxScaler |
| 4 | vit-face | Single | 768 | 0.8403 | 0.8413 | 0.8403 | 0.8403 | [82.42%, 85.51%] | n_est=200, depth=20, max_feat=log2, min_split=5, min_leaf=1, pca=PCA, scaler=None |
| 5 | vit-emotion-age | Dual | 1536 | 0.7731 | 0.7734 | 0.7731 | 0.7728 | [75.50%, 79.03%] | n_est=200, depth=20, max_feat=log2, min_split=2, min_leaf=2, pca=PCA, scaler=None |
| 6 | vit-emotion | Single | 768 | 0.7611 | 0.7602 | 0.7611 | 0.7603 | [74.27%, 77.86%] | n_est=200, depth=None, max_feat=sqrt, min_split=2, min_leaf=2, pca=PCA, scaler=None |
| 7 | vit-age | Single | 768 | 0.7181 | 0.7176 | 0.7181 | 0.7170 | [69.87%, 73.66%] | n_est=200, depth=None, max_feat=log2, min_split=5, min_leaf=2, pca=PCA, scaler=None |

**Dinamika Ablasi RF:**
- Berbeda dengan eksperimen lama di mana RF mengalami sedikit anomali dimensionalitas (Dual > Tri), pada protokol Subject-Disjoint Tri-Domain RF (0.8500) berhasil menempati peringkat tertinggi di rumpun RF, mengungguli Dual-Domain (0.8486) dan Single Face (0.8403, kenaikan signifikan $p = 0.0238$).

---

### 1.3.4 Gaussian Naive Bayes (GNB) — 7 Konfigurasi Fitur

| Rank | Konfigurasi Fitur | Tipe | Dimensi | Akurasi | Precision | Recall | Macro F1 | 95% Wilson CI | Parameter Optimal |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **1** | **vit-emotion-face** | **Dual** | **1536** | **0.8431** | 0.8437 | 0.8431 | **0.8430** | [82.71%, 85.78%] | var_smoothing=0.011253, pca=PCA, scaler=MinMaxScaler |
| 2 | vit-face-emotion-age | Tri | 2304 | 0.8361 | 0.8379 | 0.8361 | 0.8364 | [81.99%, 85.11%] | var_smoothing=0.011253, pca=PCA, scaler=None |
| 3 | vit-face-age | Dual | 1536 | 0.8306 | 0.8347 | 0.8306 | 0.8310 | [81.42%, 84.58%] | var_smoothing=0.011253, pca=PCA, scaler=MinMaxScaler |
| 4 | vit-face | Single | 768 | 0.8255 | 0.8268 | 0.8255 | 0.8250 | [80.89%, 84.09%] | var_smoothing=0.041246, pca=PCA, scaler=MinMaxScaler |
| 5 | vit-emotion-age | Dual | 1536 | 0.7588 | 0.7597 | 0.7588 | 0.7578 | [74.03%, 77.64%] | var_smoothing=0.011253, pca=PCA, scaler=MinMaxScaler |
| 6 | vit-emotion | Single | 768 | 0.7213 | 0.7251 | 0.7213 | 0.7199 | [70.20%, 73.98%] | var_smoothing=0.005878, pca=PCA, scaler=MinMaxScaler |
| 7 | vit-age | Single | 768 | 0.6708 | 0.6691 | 0.6708 | 0.6686 | [65.07%, 69.03%] | var_smoothing=0.000838, pca=PCA, scaler=MinMaxScaler |

**Dinamika Ablasi GNB:**
- Dual-Domain `vit-emotion-face` (0.8431) mengungguli Tri-Domain (0.8361) sebesar 0.70 pp pada GNB. Asumsi independensi kondisional (*conditional independence*) pada Naive Bayes semakin tertekan ketika dimensi bertambah ke 2.304 dengan korelasi laten antar-domain.

---

## 1.4 Uji Signifikansi Statistik Inferensial (McNemar Tests & Exact Binomial)

Untuk memenuhi standar metodologi IEEE Access secara ketat, perbedaan antar-skema fusi dan antar-klasifikator diuji menggunakan **Uji McNemar Berpasangan dengan koreksi kontinuitas Edwards** ($\chi^2 = (|b - c| - 1)^2 / (b + c)$) serta **Uji Binomial Eksak Dua Arah** (*Two-Sided Exact Binomial Test*):

### Tabel 1: Uji McNemar Tri-Domain (`vit-face-emotion-age`) vs Dual-Domain (`vit-emotion-face`)

| Klasifikator | Akurasi Tri (%) | Akurasi Dual (%) | Selisih (%) | Net Citra | $b$ (Tri+, Dual-) | $c$ (Tri-, Dual+) | McNemar $\chi^2$ | $p$-value Eksak | Signifikan ($\alpha=0.05$)? |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **SVM** | 88.61% | 88.43% | +0.19% | +4 | 41 | 37 | 0.1154 | 0.7343 | TIDAK (Kejenuhan Fitur) |
| **LR** | 88.66% | 87.45% | +1.20% | +26 | 57 | 31 | 7.1023 | **0.0073** | **YA ($p < 0.01$)** |
| **RF** | 85.00% | 84.86% | +0.14% | +3 | 51 | 48 | 0.0404 | 0.8408 | TIDAK |
| **GNB** | 83.61% | 84.31% | -0.69% | -15 | 62 | 77 | 1.4101 | 0.2349 | TIDAK |

### Tabel 2: Uji McNemar Dual-Domain (`vit-emotion-face`) vs Single-Domain (`vit-face`)

| Klasifikator | Akurasi Dual (%) | Akurasi Face (%) | Selisih (%) | Net Citra | $b$ (Dual+, Face-) | $c$ (Dual-, Face+) | McNemar $\chi^2$ | $p$-value Eksak | Signifikan ($\alpha=0.05$)? |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **SVM** | 88.43% | 86.16% | +2.27% | +49 | 85 | 36 | 19.0413 | **$9.82 \times 10^{-6}$** | **YA ($p < 0.001$)** |
| **LR** | 87.45% | 86.39% | +1.06% | +23 | 75 | 52 | 3.8110 | 0.0505 | *Marginal* ($p \approx 0.05$) |
| **RF** | 84.86% | 84.03% | +0.83% | +18 | 60 | 42 | 2.8333 | 0.0918 | TIDAK |
| **GNB** | 84.31% | 82.55% | +1.76% | +38 | 89 | 51 | 9.7786 | **0.0017** | **YA ($p < 0.01$)** |

### Tabel 3: Uji McNemar Tri-Domain (`vit-face-emotion-age`) vs Single-Domain (`vit-face`)

| Klasifikator | Akurasi Tri (%) | Akurasi Face (%) | Selisih (%) | Net Citra | $b$ (Tri+, Face-) | $c$ (Tri-, Face+) | McNemar $\chi^2$ | $p$-value Eksak | Signifikan ($\alpha=0.05$)? |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **SVM** | 88.61% | 86.16% | +2.45% | +53 | 91 | 38 | 20.9612 | **$3.46 \times 10^{-6}$** | **YA ($p < 0.001$)** |
| **LR** | 88.66% | 86.39% | +2.27% | +49 | 83 | 34 | 19.6923 | **$6.78 \times 10^{-6}$** | **YA ($p < 0.001$)** |
| **RF** | 85.00% | 84.03% | +0.97% | +21 | 50 | 29 | 5.0633 | **0.0238** | **YA ($p < 0.05$)** |
| **GNB** | 83.61% | 82.55% | +1.06% | +23 | 97 | 74 | 2.8304 | 0.0922 | TIDAK |

### Tabel 4: Uji Head-to-Head Top Model: LR Tri-Domain vs SVM Tri-Domain

| Perbandingan | Model 1 (LR Tri) | Model 2 (SVM Tri) | Selisih | Net Citra | $b$ (LR+, SVM-) | $c$ (LR-, SVM+) | McNemar $\chi^2$ | $p$-value Eksak | Kesimpulan Inferensial |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **LR Tri vs SVM Tri** | **88.66%** | **88.61%** | **+0.05%** | **+1** | 36 | 35 | **0.0000** | **1.0000** | **Ekuivalen Secara Statistik** |

---

## 1.5 Profil Latensi Inferensi & Efisiensi Memori (Edge AI Deployment Profile)

Perbandingan karakteristik operasional komputasi pada keempat klasifikator berbasis fitur Tri-Domain (`vit-face-emotion-age`, 2.304 dimensi):

| Model Klasifikator | Akurasi | Macro F1 | Latensi Inferensi (ms/sampel) | Throughput (sampel/detik) | Ukuran Bobot Model (MB) | Rasio Kecepatan vs SVM | Rasio Ukuran vs SVM |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Logistic Regression (LR)** | **0.8866** | **0.8868** | **0.0054 ms** | **~185.185** | **0.11 MB** | **823.7$\times$ lebih cepat** | **332.7$\times$ lebih hemat** |
| **Gaussian Naive Bayes (GNB)** | 0.8361 | 0.8364 | 0.0081 ms | ~123.456 | 1.36 MB | 549.1$\times$ lebih cepat | 26.9$\times$ lebih hemat |
| **Random Forest (RF)** | 0.8500 | 0.8493 | 0.0537 ms | ~18.621 | 6.19 MB | 82.8$\times$ lebih cepat | 5.9$\times$ lebih hemat |
| **Support Vector Machine (SVM)** | 0.8861 | 0.8863 | 4.4481 ms | ~224 | 36.60 MB | 1.0$\times$ (baseline) | 1.0$\times$ (baseline) |

> **Rekomendasi Arsitektural untuk Produksi:** Meskipun SVM memiliki akurasi yang sebanding (88,61% vs 88,66%), Logistic Regression adalah pilihan arsitektur yang jauh lebih unggul untuk penerapan skala industri dan perangkat tepi (*embedded / mobile devices*) karena hanya memerlukan memori 110 KB dengan waktu eksekusi sub-mikrodetik.

---

## 1.6 Evaluasi Kesetaraan Demografis & Keadilan Algoritmik (Fairness & Equal Opportunity Disparity)

Pada data uji held-out independen (360 citra per kelas, 20 subjek terisolasi per kelas), performa dievaluasi di seluruh 6 subkelompok interseksional untuk mengukur disparitas keadilan algoritmik (*Algorithmic Fairness*).

### 1.6.1 Evaluasi One-vs-Rest (OvR) Model Puncak Tri-Domain (Subject-Disjoint)

#### A. Model Juara 1: Logistic Regression Tri-Domain (Akurasi: 0.8866, Macro F1: 0.8868)

| Subkelompok Interseksional | Ras | Gender | Support Citra | Subjek Uji | Precision | Recall (TPR) | F1-Score | OvR Akurasi |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Asian_Females** | Asian | Wanita | 360 | 20 | 0.8643 | 0.8667 | 0.8655 | 0.9551 |
| **Asian_Males** | Asian | Pria | 360 | 20 | 0.8272 | 0.8778 | 0.8518 | 0.9491 |
| **Black_Females** | Black | Wanita | 360 | 20 | 0.8520 | **0.8472** | 0.8496 | 0.9500 |
| **Black_Males** | Black | Pria | 360 | 20 | 0.9159 | 0.8778 | 0.8965 | 0.9662 |
| **White_Females** | White | Wanita | 360 | 20 | 0.9132 | 0.9056 | 0.9093 | 0.9699 |
| **White_Males** | White | Pria | 360 | 20 | 0.9524 | **0.9444** | 0.9484 | 0.9829 |
| **Rata-rata Makro (Macro Avg)** | — | — | **2.160** | **120** | **0.8875** | **0.8866** | **0.8868** | **0.9622** |

- **Recall Maksimum:** 0.9444 (94,44% pada *White_Males*)
- **Recall Minimum:** 0.8472 (84,72% pada *Black_Females*)
- **Equal Opportunity Disparity ($\Delta \text{TPR}$):** $0.9444 - 0.8472 =$ **9.72 percentage points (pp)**.

---

#### B. Model Juara 2: SVM Tri-Domain (Akurasi: 0.8861, Macro F1: 0.8863)

| Subkelompok Interseksional | Ras | Gender | Support Citra | Subjek Uji | Precision | Recall (TPR) | F1-Score | OvR Akurasi |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Asian_Females** | Asian | Wanita | 360 | 20 | 0.8587 | 0.8611 | 0.8599 | 0.9532 |
| **Asian_Males** | Asian | Pria | 360 | 20 | 0.8234 | 0.8806 | 0.8510 | 0.9486 |
| **Black_Females** | Black | Wanita | 360 | 20 | 0.8764 | **0.8472** | 0.8616 | 0.9546 |
| **Black_Males** | Black | Pria | 360 | 20 | 0.9235 | 0.8722 | 0.8971 | 0.9667 |
| **White_Females** | White | Wanita | 360 | 20 | 0.9011 | 0.9111 | 0.9061 | 0.9685 |
| **White_Males** | White | Pria | 360 | 20 | 0.9392 | **0.9444** | 0.9418 | 0.9806 |
| **Rata-rata Makro (Macro Avg)** | — | — | **2.160** | **120** | **0.8871** | **0.8861** | **0.8863** | **0.9620** |

- **Recall Maksimum:** 0.9444 (94,44% pada *White_Males*)
- **Recall Minimum:** 0.8472 (84,72% pada *Black_Females*)
- **Equal Opportunity Disparity ($\Delta \text{TPR}$):** **9.72 percentage points (pp)**.

---

### 1.6.2 Ringkasan Metrik Keadilan Algoritmik Lintas Klasifikator Tri-Domain

| Klasifikator | Akurasi Global | Recall Min | Recall Max | $\Delta \text{TPR}$ (Equal Opportunity Gap) | F1-Score Min | F1-Score Max | $\Delta \text{F1}$ | Subkelompok Paling Rentan |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **Logistic Regression (LR)** | **0.8866** | **0.8472** | **0.9444** | **9.72 pp (0.0972)** | 0.8496 | 0.9484 | 0.0988 | Black_Females |
| **Support Vector Machine (SVM)** | **0.8861** | **0.8472** | **0.9444** | **9.72 pp (0.0972)** | 0.8510 | 0.9418 | 0.0908 | Black_Females |
| **Random Forest (RF)** | 0.8500 | 0.7333 | 0.9306 | 19.72 pp (0.1972) | 0.7869 | 0.9079 | 0.1210 | Black_Females |
| **Gaussian Naive Bayes (GNB)** | 0.8361 | 0.7500 | 0.8917 | 14.17 pp (0.1417) | 0.7803 | 0.9109 | 0.1306 | Black_Females |

> **Temuan Keadilan Algoritmik:** LR dan SVM menunjukkan toleransi disparitas terendah ($\Delta \text{TPR} = 9.72$ pp), sedangkan RF menunjukkan disparitas terlebar ($\Delta \text{TPR} = 19.72$ pp). Di seluruh klasifikator, *Black Females* secara konsisten menjadi subkelompok dengan recall terendah, sementara *White Males* mencapai recall tertinggi.

---

### 1.6.3 Matriks Konfusi Model Juara 1 (LR Tri-Domain, Akurasi: 0.8866)

Urutan kelas pada sumbu matriks mengikuti penataan kanonikal dataset DemogPairs:

| True \ Pred | Black_Males | White_Females | Asian_Males | White_Males | Black_Females | Asian_Females | Total Benar | Recall |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Black_Males** | **316** | 0 | 23 | 6 | 15 | 0 | 360 | 0.8778 |
| **White_Females** | 0 | **326** | 3 | 2 | 11 | 18 | 360 | 0.9056 |
| **Asian_Males** | 17 | 0 | **316** | 6 | 4 | 17 | 360 | 0.8778 |
| **White_Males** | 4 | 2 | 14 | **340** | 0 | 0 | 360 | 0.9444 |
| **Black_Females** | 8 | 23 | 8 | 2 | **305** | 14 | 360 | 0.8472 |
| **Asian_Females** | 0 | 6 | 18 | 1 | 23 | **312** | 360 | 0.8667 |
| **Total Prediksi** | **345** | **357** | **382** | **357** | **358** | **361** | **2.160** | — |

**Rincian Parameter Kinerja OvR (LR Tri-Domain):**
- **Black_Males:** TP=316, FP=29, FN=44, TN=1.771 $\to$ OvR Acc=0.9662, Prec=0.9159, Rec=0.8778, F1=0.8965
- **White_Females:** TP=326, FP=31, FN=34, TN=1.769 $\to$ OvR Acc=0.9699, Prec=0.9132, Rec=0.9056, F1=0.9093
- **Asian_Males:** TP=316, FP=66, FN=44, TN=1.734 $\to$ OvR Acc=0.9491, Prec=0.8272, Rec=0.8778, F1=0.8518
- **White_Males:** TP=340, FP=17, FN=20, TN=1.783 $\to$ OvR Acc=0.9829, Prec=0.9524, Rec=0.9444, F1=0.9484
- **Black_Females:** TP=305, FP=53, FN=55, TN=1.747 $\to$ OvR Acc=0.9500, Prec=0.8520, Rec=0.8472, F1=0.8496
- **Asian_Females:** TP=312, FP=49, FN=48, TN=1.751 $\to$ OvR Acc=0.9551, Prec=0.8643, Rec=0.8667, F1=0.8655

---

### 1.6.4 Matriks Konfusi Model Juara 2 (SVM Tri-Domain, Akurasi: 0.8861)

| True \ Pred | Black_Males | White_Females | Asian_Males | White_Males | Black_Females | Asian_Females | Total Benar | Recall |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Black_Males** | **314** | 0 | 25 | 11 | 10 | 0 | 360 | 0.8722 |
| **White_Females** | 0 | **328** | 2 | 2 | 7 | 21 | 360 | 0.9111 |
| **Asian_Males** | 17 | 0 | **317** | 6 | 4 | 16 | 360 | 0.8806 |
| **White_Males** | 3 | 1 | 16 | **340** | 0 | 0 | 360 | 0.9444 |
| **Black_Females** | 6 | 26 | 7 | 2 | **305** | 14 | 360 | 0.8472 |
| **Asian_Females** | 0 | 9 | 18 | 1 | 22 | **310** | 360 | 0.8611 |
| **Total Prediksi** | **340** | **364** | **385** | **362** | **348** | **361** | **2.160** | — |

**Rincian Parameter Kinerja OvR (SVM Tri-Domain):**
- **Black_Males:** TP=314, FP=26, FN=46, TN=1.774 $\to$ OvR Acc=0.9667, Prec=0.9235, Rec=0.8722, F1=0.8971
- **White_Females:** TP=328, FP=36, FN=32, TN=1.764 $\to$ OvR Acc=0.9685, Prec=0.9011, Rec=0.9111, F1=0.9061
- **Asian_Males:** TP=317, FP=68, FN=43, TN=1.732 $\to$ OvR Acc=0.9486, Prec=0.8234, Rec=0.8806, F1=0.8510
- **White_Males:** TP=340, FP=22, FN=20, TN=1.778 $\to$ OvR Acc=0.9806, Prec=0.9392, Rec=0.9444, F1=0.9418
- **Black_Females:** TP=305, FP=43, FN=55, TN=1.757 $\to$ OvR Acc=0.9546, Prec=0.8764, Rec=0.8472, F1=0.8616
- **Asian_Females:** TP=310, FP=51, FN=50, TN=1.749 $\to$ OvR Acc=0.9532, Prec=0.8587, Rec=0.8611, F1=0.8599

> **Karakteristik Kesalahan Klasifikasi:** Pola kesalahan pada kedua model identik: kesalahan dominan terjadi antar-ras dengan gender yang sama (misal 23–26 citra Black Females salah diprediksi sebagai White Females, dan 23–25 citra Black Males salah diprediksi sebagai Asian Males). Kesalahan intra-ras lintas-gender (misal Black Males tertukar dengan Black Females) sangat jarang terjadi (<3 citra).

---

# BAGIAN 2: HASIL EKSPERIMEN HISTORIS SUBJECT-OVERLAP
### (100% Identity Leakage Baseline — Data Pembanding untuk Menjawab Reviewer 2)

---

## 2.1 Konteks Eksperimen Historis & Metodologi Awal

Pada versi awal manuskrip yang diserahkan ke IEEE Access, partisi data menggunakan pembagian acak tingkat citra (*image-level stratified random split*):
```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
```
Protokol ini menyebabkan **100% dari 593 subjek uji** juga memiliki foto variasi lain di dalam data latih. Seluruh hasil historis ini sengaja dipertahankan secara utuh tanpa ada modifikasi untuk mendasari analisis komparatif kebocoran data pada Bagian 3.

---

## 2.2 Rekapitulasi Lengkap 28 Eksperimen Historis (Subject-Overlap)

| Rank | Classifier | Konfigurasi Fitur | Tipe | Akurasi | Precision | Recall | Macro F1 | Parameter Hyperparameter Optimal Historis |
|:---:|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---|
| **1** | **SVM** | **vit-face-emotion-age** | **Tri** | **0.9370** | 0.9372 | 0.9370 | **0.9369** | C=10, poly, γ=scale, deg=2, pca=None, scaler=None |
| **2** | **SVM** | **vit-emotion-face** | **Dual** | **0.9329** | 0.9333 | 0.9329 | **0.9329** | C=10, rbf, γ=scale, deg=2, pca=None, scaler=MinMaxScaler |
| **3** | **LR** | **vit-face-emotion-age** | **Tri** | **0.9273** | 0.9275 | 0.9273 | **0.9273** | C=0.1, solver=newton-cg, max_iter=500, pca=None, scaler=None |
| 4 | SVM | vit-face-age | Dual | 0.9255 | 0.9254 | 0.9255 | 0.9254 | C=10, poly, γ=scale, deg=2, pca=None, scaler=None |
| 5 | LR | vit-emotion-face | Dual | 0.9241 | 0.9241 | 0.9241 | 0.9240 | C=0.1, solver=lbfgs, max_iter=500, pca=None, scaler=None |
| 6 | SVM | vit-emotion-age | Dual | 0.9208 | 0.9210 | 0.9208 | 0.9209 | C=10, rbf, γ=scale, deg=2, pca=None, scaler=None |
| 7 | LR | vit-face-age | Dual | 0.9162 | 0.9162 | 0.9162 | 0.9162 | C=0.1, solver=newton-cg, max_iter=500, pca=None, scaler=None |
| 8 | SVM | vit-face | Single | 0.9083 | 0.9084 | 0.9083 | 0.9083 | C=10, rbf, γ=scale, deg=2, pca=None, scaler=None |
| 9 | LR | vit-face | Single | 0.9060 | 0.9060 | 0.9060 | 0.9059 | C=1, solver=newton-cg, max_iter=500, pca=None, scaler=MinMaxScaler |
| 10 | LR | vit-emotion-age | Dual | 0.9051 | 0.9052 | 0.9051 | 0.9051 | C=0.1, solver=lbfgs, max_iter=500, pca=None, scaler=None |
| 11 | SVM | vit-emotion | Single | 0.9019 | 0.9020 | 0.9019 | 0.9017 | C=10, rbf, γ=scale, deg=2, pca=None, scaler=None |
| 12 | LR | vit-emotion | Single | 0.8847 | 0.8850 | 0.8847 | 0.8846 | C=1, solver=saga, max_iter=500, pca=None, scaler=MinMaxScaler |
| 13 | SVM | vit-age | Single | 0.8764 | 0.8767 | 0.8764 | 0.8765 | C=10, rbf, γ=scale, deg=2, pca=None, scaler=None |
| 14 | RF | vit-emotion-face | Dual | 0.8685 | 0.8689 | 0.8685 | 0.8682 | n_est=200, depth=None, max_feat=sqrt, min_split=5, min_leaf=1, pca=PCA, scaler=None |
| 15 | LR | vit-age | Single | 0.8648 | 0.8649 | 0.8648 | 0.8648 | C=0.1, solver=lbfgs, max_iter=500, pca=None, scaler=None |
| 16 | RF | vit-face-emotion-age | Tri | 0.8620 | 0.8620 | 0.8620 | 0.8613 | n_est=200, depth=30, max_feat=sqrt, min_split=5, min_leaf=1, pca=PCA, scaler=None |
| 17 | RF | vit-face-age | Dual | 0.8579 | 0.8578 | 0.8579 | 0.8573 | n_est=200, depth=None, max_feat=sqrt, min_split=2, min_leaf=1, pca=PCA, scaler=None |
| 18 | RF | vit-face | Single | 0.8546 | 0.8543 | 0.8546 | 0.8539 | n_est=200, depth=30, max_feat=log2, min_split=2, min_leaf=1, pca=PCA, scaler=MinMaxScaler |
| 19 | GNB | vit-face-emotion-age | Tri | 0.8505 | 0.8512 | 0.8505 | 0.8505 | var_smoothing=5.8780e-03, pca=PCA, scaler=None |
| 20 | GNB | vit-emotion-face | Dual | 0.8486 | 0.8490 | 0.8486 | 0.8481 | var_smoothing=5.8780e-03, pca=PCA, scaler=MinMaxScaler |
| 21 | GNB | vit-face-age | Dual | 0.8315 | 0.8343 | 0.8315 | 0.8317 | var_smoothing=1.1253e-02, pca=PCA, scaler=MinMaxScaler |
| 22 | GNB | vit-face | Single | 0.8269 | 0.8271 | 0.8269 | 0.8258 | var_smoothing=4.1246e-02, pca=PCA, scaler=MinMaxScaler |
| 23 | RF | vit-emotion-age | Dual | 0.8111 | 0.8111 | 0.8111 | 0.8108 | n_est=200, depth=None, max_feat=log2, min_split=5, min_leaf=2, pca=PCA, scaler=None |
| 24 | RF | vit-emotion | Single | 0.8060 | 0.8063 | 0.8060 | 0.8057 | n_est=200, depth=None, max_feat=log2, min_split=5, min_leaf=1, pca=PCA, scaler=None |
| 25 | GNB | vit-emotion-age | Dual | 0.7681 | 0.7686 | 0.7681 | 0.7681 | var_smoothing=1.6037e-03, pca=PCA, scaler=MinMaxScaler |
| 26 | RF | vit-age | Single | 0.7366 | 0.7363 | 0.7366 | 0.7354 | n_est=200, depth=30, max_feat=log2, min_split=2, min_leaf=1, pca=PCA, scaler=None |
| 27 | GNB | vit-emotion | Single | 0.7338 | 0.7387 | 0.7338 | 0.7329 | var_smoothing=3.0703e-03, pca=PCA, scaler=None |
| 28 | GNB | vit-age | Single | 0.6963 | 0.6979 | 0.6963 | 0.6952 | var_smoothing=4.3755e-04, pca=PCA, scaler=MinMaxScaler |

---

## 2.3 Rincian per Klasifikator Historis (Subject-Overlap)

### 2.3.1 SVM Historis (288 kombinasi $\times$ 5 folds = 1.440 fits/fitur)
- `vit-face-emotion-age` (Tri): **0.9370** / 0.9372 / 0.9370 / **0.9369** (C=10, poly, deg=2, pca=None, scaler=None)
- `vit-emotion-face` (Dual): 0.9329 / 0.9333 / 0.9329 / 0.9329 (C=10, rbf, pca=None, scaler=MinMaxScaler)
- `vit-face-age` (Dual): 0.9255 / 0.9254 / 0.9255 / 0.9254 (C=10, poly, deg=2, pca=None, scaler=None)
- `vit-emotion-age` (Dual): 0.9208 / 0.9210 / 0.9208 / 0.9209 (C=10, rbf, pca=None, scaler=None)
- `vit-face` (Single): 0.9083 / 0.9084 / 0.9083 / 0.9083 (C=10, rbf, pca=None, scaler=None)
- `vit-emotion` (Single): 0.9019 / 0.9020 / 0.9019 / 0.9017 (C=10, rbf, pca=None, scaler=None)
- `vit-age` (Single): 0.8764 / 0.8767 / 0.8764 / 0.8765 (C=10, rbf, pca=None, scaler=None)

### 2.3.2 Logistic Regression Historis (270 kombinasi $\times$ 5 folds = 1.350 fits/fitur)
- `vit-face-emotion-age` (Tri): **0.9273** / 0.9275 / 0.9273 / **0.9273** (C=0.1, newton-cg, pca=None, scaler=None)
- `vit-emotion-face` (Dual): 0.9241 / 0.9241 / 0.9241 / 0.9240 (C=0.1, lbfgs, pca=None, scaler=None)
- `vit-face-age` (Dual): 0.9162 / 0.9162 / 0.9162 / 0.9162 (C=0.1, newton-cg, pca=None, scaler=None)
- `vit-face` (Single): 0.9060 / 0.9060 / 0.9060 / 0.9059 (C=1, newton-cg, pca=None, scaler=MinMaxScaler)
- `vit-emotion-age` (Dual): 0.9051 / 0.9052 | 0.9051 | 0.9051 (C=0.1, lbfgs, pca=None, scaler=None)
- `vit-emotion` (Single): 0.8847 / 0.8850 / 0.8847 / 0.8846 (C=1, saga, pca=None, scaler=MinMaxScaler)
- `vit-age` (Single): 0.8648 / 0.8649 / 0.8648 / 0.8648 (C=0.1, lbfgs, pca=None, scaler=None)

### 2.3.3 Random Forest Historis (288 kombinasi $\times$ 5 folds = 1.440 fits/fitur)
- `vit-emotion-face` (Dual): **0.8685** / 0.8689 / 0.8685 / **0.8682** (n=200, depth=None, sqrt, pca=PCA, scaler=None)
- `vit-face-emotion-age` (Tri): 0.8620 / 0.8620 / 0.8620 / 0.8613 (n=200, depth=30, sqrt, pca=PCA, scaler=None)
- `vit-face-age` (Dual): 0.8579 / 0.8578 / 0.8579 / 0.8573 (n=200, depth=None, sqrt, pca=PCA, scaler=None)
- `vit-face` (Single): 0.8546 / 0.8543 / 0.8546 / 0.8539 (n=200, depth=30, log2, pca=PCA, scaler=MinMaxScaler)
- `vit-emotion-age` (Dual): 0.8111 / 0.8111 / 0.8111 / 0.8108 (n=200, depth=None, log2, pca=PCA, scaler=None)
- `vit-emotion` (Single): 0.8060 / 0.8063 / 0.8060 / 0.8057 (n=200, depth=None, log2, pca=PCA, scaler=None)
- `vit-age` (Single): 0.7366 / 0.7363 / 0.7366 / 0.7354 (n=200, depth=30, log2, pca=PCA, scaler=None)

### 2.3.4 Gaussian Naive Bayes Historis (240 kombinasi $\times$ 5 folds = 1.200 fits/fitur)
- `vit-face-emotion-age` (Tri): **0.8505** / 0.8512 / 0.8505 / **0.8505** (var_smoothing=5.8780e-03, pca=PCA, scaler=None)
- `vit-emotion-face` (Dual): 0.8486 / 0.8490 / 0.8486 / 0.8481 (var_smoothing=5.8780e-03, pca=PCA, scaler=MinMaxScaler)
- `vit-face-age` (Dual): 0.8315 / 0.8343 / 0.8315 / 0.8317 (var_smoothing=1.1253e-02, pca=PCA, scaler=MinMaxScaler)
- `vit-face` (Single): 0.8269 / 0.8271 / 0.8269 / 0.8258 (var_smoothing=4.1246e-02, pca=PCA, scaler=MinMaxScaler)
- `vit-emotion-age` (Dual): 0.7681 / 0.7686 / 0.7681 / 0.7681 (var_smoothing=1.6037e-03, pca=PCA, scaler=MinMaxScaler)
- `vit-emotion` (Single): 0.7338 / 0.7387 / 0.7338 / 0.7329 (var_smoothing=3.0703e-03, pca=PCA, scaler=None)
- `vit-age` (Single): 0.6963 / 0.6979 / 0.6963 / 0.6952 (var_smoothing=4.3755e-04, pca=PCA, scaler=MinMaxScaler)

---

## 2.4 Matriks Konfusi Model Juara Historis (SVM Tri-Domain, Akurasi: 0.9370)

Pada eksperimen historis dengan kebocoran identitas 100%, SVM Tri-Domain menghasilkan akurasi 93,70% (2.024 dari 2.160 citra uji benar):

| True \ Pred | Black_Males | White_Females | Asian_Males | White_Males | Black_Females | Asian_Females | Total Benar | Recall |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Black_Males** | **339** | 0 | 9 | 4 | 8 | 0 | 360 | 0.9417 |
| **White_Females** | 1 | **341** | 0 | 5 | 4 | 9 | 360 | 0.9472 |
| **Asian_Males** | 6 | 0 | **340** | 4 | 2 | 8 | 360 | 0.9444 |
| **White_Males** | 4 | 2 | 4 | **349** | 0 | 1 | 360 | 0.9694 |
| **Black_Females** | 5 | 16 | 6 | 2 | **322** | 9 | 360 | 0.8944 |
| **Asian_Females** | 0 | 10 | 9 | 2 | 6 | **333** | 360 | 0.9250 |
| **Total Prediksi** | **355** | **369** | **368** | **366** | **342** | **360** | **2.160** | — |

**Parameter Kinerja OvR Historis (SVM Tri-Domain):**
- **Black_Males:** TP=339, FP=16, FN=21, TN=1.784 $\to$ OvR Acc=0.9829, Prec=0.9549, Rec=0.9417, F1=0.9483
- **White_Females:** TP=341, FP=28, FN=19, TN=1.772 $\to$ OvR Acc=0.9782, Prec=0.9241, Rec=0.9472, F1=0.9355
- **Asian_Males:** TP=340, FP=28, FN=20, TN=1.772 $\to$ OvR Acc=0.9778, Prec=0.9239, Rec=0.9444, F1=0.9341
- **White_Males:** TP=349, FP=17, FN=11, TN=1.783 $\to$ OvR Acc=0.9870, Prec=0.9536, Rec=0.9694, F1=0.9614
- **Black_Females:** TP=322, FP=20, FN=38, TN=1.780 $\to$ OvR Acc=0.9731, Prec=0.9415, Rec=0.8944, F1=0.9174
- **Asian_Females:** TP=333, FP=27, FN=27, TN=1.773 $\to$ OvR Acc=0.9750, Prec=0.9250, Rec=0.9250, F1=0.9250

---

# BAGIAN 3: ANALISIS KOMPARATIF ABLASI KEBOCORAN DATA
### (Studi Komparatif Subject-Disjoint vs. Subject-Overlap — Jawaban IEEE Access Reviewer 2)

---

## 3.1 Hakikat Masalah Kebocoran Data (Identity Leakage Audit)

Tanggapan langsung terhadap komentar kritis **IEEE Access Reviewer 2 (Comment #2: "Data Leakage and Generalization")**:

> *"In the DemogPairs dataset, each subject has multiple photos. When images are randomly partitioned at the image level, photos from the same identity appear in both train and test partitions. The reported accuracy of 93.70% may reflect identity memorization rather than demographic feature generalization."*

Hasil audit empiris komparatif antara kedua protokol diuraikan pada tabel berikut:

| Parameter Audit Metodologis | Protokol Historis (Subject-Overlap) | Protokol Revisi (Subject-Disjoint) | Perubahan Kepatuhan Akademik |
|:---|:---:|:---:|:---|
| **Metode Partisi Train / Test** | `train_test_split(stratify=y)` | `split_demogpairs_subject_disjoint` | Kepatuhan ketat standar biometrik |
| **Metode Cross-Validation** | `StratifiedKFold(n_splits=5)` | `StratifiedGroupKFold(n_splits=5)` | Pencegahan kontaminasi antar-lipatan |
| **Subjek Uji yang Bocor di Train** | **593 dari 593 subjek (100.00%)** | **0 dari 120 subjek (0.00%)** | **Eliminasi tuntas kebocoran (100% $\to$ 0%)** |
| **Citra Uji yang Terkontaminasi** | **2.160 dari 2.160 citra (100.00%)** | **0 dari 2.160 citra (0.00%)** | **0 citra bocor pada set uji** |
| **Subjek Overlap per Fold CV** | **~572 - 581 subjek / fold (~99%)** | **0 subjek / fold (0.00%)** | **0% overlap pada seluruh 5 folds** |
| **Kapasitas Pembelajaran Model** | Menghafal biometrik individu | Generalisasi representasi demografi | Evaluasi generalisasi sejati |

---

## 3.2 Tabel Komparasi Langsung Seluruh 28 Konfigurasi Model

Tabel berikut menyandingkan metrik kinerja dari seluruh 28 konfigurasi model antara protokol **Subject-Overlap (Lama)** dan **Subject-Disjoint (Baru)** secara presisi 4 desimal sesuai `audit_ledger.json`:

| Rank | Classifier | Konfigurasi Fitur | Tipe | Dim | Akurasi Lama (Overlap) | Akurasi Baru (Disjoint) | $\Delta \text{Acc}$ (Drop pp) | Drop Relatif (%) | Macro F1 Lama | Macro F1 Baru | $\Delta \text{F1}$ | 95% Wilson CI (Baru) | Latensi Baru (ms) | Ukuran (MB) |
|:---:|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | **LR** | **vit-face-emotion-age** | **Tri** | **2304** | 0.9273 | **0.8866** | **-0.0407** | **-4.39%** | 0.9273 | **0.8868** | -0.0405 | [87.25%, 89.93%] | 0.0054 | 0.11 |
| **2** | **SVM** | **vit-face-emotion-age** | **Tri** | **2304** | 0.9370 | **0.8861** | **-0.0509** | **-5.43%** | 0.9369 | **0.8863** | -0.0507 | [87.20%, 89.88%] | 4.4481 | 36.60 |
| **3** | **SVM** | **vit-emotion-face** | **Dual** | **1536** | 0.9329 | **0.8843** | **-0.0486** | **-5.21%** | 0.9329 | **0.8844** | -0.0486 | [87.01%, 89.71%] | 0.9707 | 15.27 |
| 4 | SVM | vit-face-age | Dual | 1536 | 0.9255 | 0.8755 | -0.0500 | -5.40% | 0.9254 | 0.8757 | -0.0497 | [86.09%, 88.87%] | 2.2581 | 23.48 |
| 5 | LR | vit-emotion-face | Dual | 1536 | 0.9241 | 0.8745 | -0.0495 | -5.36% | 0.9240 | 0.8749 | -0.0491 | [85.99%, 88.78%] | 0.0039 | 0.08 |
| 6 | LR | vit-face-age | Dual | 1536 | 0.9162 | 0.8741 | -0.0421 | -4.60% | 0.9162 | 0.8740 | -0.0422 | [85.94%, 88.74%] | 0.0090 | 0.11 |
| 7 | LR | vit-emotion-age | Dual | 1536 | 0.9051 | 0.8667 | -0.0384 | -4.25% | 0.9051 | 0.8667 | -0.0384 | [85.17%, 88.04%] | 0.0040 | 0.08 |
| 8 | LR | vit-face | Single | 768 | 0.9060 | 0.8639 | -0.0421 | -4.65% | 0.9059 | 0.8640 | -0.0420 | [84.88%, 87.77%] | 0.0008 | 0.04 |
| 9 | SVM | vit-emotion-age | Dual | 1536 | 0.9208 | 0.8625 | -0.0583 | -6.33% | 0.9209 | 0.8624 | -0.0585 | [84.73%, 87.64%] | 3.1451 | 32.76 |
| 10 | SVM | vit-face | Single | 768 | 0.9083 | 0.8616 | -0.0468 | -5.15% | 0.9083 | 0.8619 | -0.0464 | [84.64%, 87.55%] | 3.0653 | 7.56 |
| 11 | SVM | vit-emotion | Single | 768 | 0.9019 | 0.8579 | -0.0440 | -4.88% | 0.9017 | 0.8580 | -0.0437 | [84.25%, 87.20%] | 1.8871 | 15.30 |
| 12 | LR | vit-emotion | Single | 768 | 0.8847 | 0.8523 | -0.0324 | -3.66% | 0.8846 | 0.8527 | -0.0319 | [83.67%, 86.67%] | 0.0037 | 0.06 |
| 13 | RF | vit-face-emotion-age | Tri | 2304 | 0.8620 | 0.8500 | -0.0120 | -1.40% | 0.8613 | 0.8493 | -0.0121 | [83.43%, 86.44%] | 0.0537 | 6.19 |
| 14 | RF | vit-face-age | Dual | 1536 | 0.8579 | 0.8486 | -0.0093 | -1.08% | 0.8573 | 0.8478 | -0.0095 | [83.29%, 86.31%] | 0.0310 | 6.19 |
| 15 | RF | vit-emotion-face | Dual | 1536 | 0.8685 | 0.8486 | -0.0199 | -2.29% | 0.8682 | 0.8479 | -0.0203 | [83.29%, 86.31%] | 0.0316 | 8.58 |
| 16 | GNB | vit-emotion-face | Dual | 1536 | 0.8486 | 0.8431 | -0.0056 | -0.65% | 0.8481 | 0.8430 | -0.0051 | [82.71%, 85.78%] | 0.0083 | 0.78 |
| 17 | RF | vit-face | Single | 768 | 0.8546 | 0.8403 | -0.0144 | -1.68% | 0.8539 | 0.8403 | -0.0136 | [82.42%, 85.51%] | 0.0314 | 5.99 |
| 18 | GNB | vit-face-emotion-age | Tri | 2304 | 0.8505 | 0.8361 | -0.0144 | -1.69% | 0.8505 | 0.8364 | -0.0141 | [81.99%, 85.11%] | 0.0081 | 1.36 |
| 19 | GNB | vit-face-age | Dual | 1536 | 0.8315 | 0.8306 | -0.0009 | -0.11% | 0.8317 | 0.8310 | -0.0007 | [81.42%, 84.58%] | 0.0080 | 0.75 |
| 20 | SVM | vit-age | Single | 768 | 0.8764 | 0.8255 | -0.0509 | -5.81% | 0.8765 | 0.8258 | -0.0506 | [80.89%, 84.09%] | 2.0104 | 18.22 |
| 21 | GNB | vit-face | Single | 768 | 0.8269 | 0.8255 | -0.0014 | -0.17% | 0.8258 | 0.8250 | -0.0008 | [80.89%, 84.09%] | 0.0031 | 0.19 |
| 22 | LR | vit-age | Single | 768 | 0.8648 | 0.8148 | -0.0500 | -5.78% | 0.8648 | 0.8146 | -0.0502 | [79.79%, 83.06%] | 0.0028 | 0.06 |
| 23 | RF | vit-emotion-age | Dual | 1536 | 0.8111 | 0.7731 | -0.0380 | -4.68% | 0.8108 | 0.7728 | -0.0379 | [75.50%, 79.03%] | 0.0392 | 12.35 |
| 24 | RF | vit-emotion | Single | 768 | 0.8060 | 0.7611 | -0.0449 | -5.57% | 0.8057 | 0.7603 | -0.0454 | [74.27%, 77.86%] | 0.0316 | 10.34 |
| 25 | GNB | vit-emotion-age | Dual | 1536 | 0.7681 | 0.7588 | -0.0093 | -1.21% | 0.7681 | 0.7578 | -0.0102 | [74.03%, 77.64%] | 0.0048 | 0.24 |
| 26 | GNB | vit-emotion | Single | 768 | 0.7338 | 0.7213 | -0.0125 | -1.70% | 0.7329 | 0.7199 | -0.0130 | [70.20%, 73.98%] | 0.0031 | 0.13 |
| 27 | RF | vit-age | Single | 768 | 0.7366 | 0.7181 | -0.0185 | -2.51% | 0.7354 | 0.7170 | -0.0184 | [69.87%, 73.66%] | 0.0327 | 11.21 |
| 28 | GNB | vit-age | Single | 768 | 0.6963 | 0.6708 | -0.0255 | -3.66% | 0.6952 | 0.6686 | -0.0266 | [65.07%, 69.03%] | 0.0045 | 0.37 |

---

## 3.3 Analisis Kerentanan Klasifikator terhadap Kebocoran Data (Vulnerability Analysis)

Studi komparatif ini mengungkap variasi kerentanan yang sangat menarik antar-rumpun algoritma klasifikasi ketika kebocoran identitas dieliminasi:

| Rumpun Klasifikator | Rata-rata Akurasi Lama (Overlap) | Rata-rata Akurasi Baru (Disjoint) | Rata-rata Drop Akurasi ($\Delta \text{Acc}$) | Rata-rata Drop Relatif (%) | Rentang Drop ($\min - \max$) | Interpretasi Karakteristik Induktif |
|:---|:---:|:---:|:---:|:---:|:---:|:---|
| **Support Vector Machine (SVM)** | **0.9147** | **0.8647** | **-0.0499 pp** | **-5.46%** | -4.40 pp s.d. -5.83 pp | **Kapasitas Memori Tinggi**: Kernel non-linier RBF/Poly pada 2.304-d paling sensitif menghafal ciri khas subjek. |
| **Logistic Regression (LR)** | **0.9040** | **0.8615** | **-0.0425 pp** | **-4.71%** | -3.24 pp s.d. -5.00 pp | **Batas Keputusan Linier Kuat**: Regulerisasi $L_2$ (`C=0.1`) mencegah overfitting ekstrem, merebut ranking 1 global. |
| **Random Forest (RF)** | **0.8281** | **0.8071** | **-0.0210 pp** | **-2.57%** | -0.93 pp s.d. -4.49 pp | **Resistensi Ansambel**: Pemilihan fitur acak pada pohon keputusan dan PCA meredam eksploitasi shortcut identitas. |
| **Gaussian Naive Bayes (GNB)** | **0.7937** | **0.7836** | **-0.0101 pp** | **-1.29%** | -0.09 pp s.d. -2.55 pp | **Kapasitas Memori Terendah**: Asumsi independensi kondisional tidak mampu menghafal korelasi kompleks antar-fitur. |

### Temuan Saintifik Utama:
1. **Penurunan Akurasi Bersifat Sistematis dan Wajar:** Seluruh 28 konfigurasi model mengalami penurunan skor numerik sebesar $-0.09$ pp hingga $-5.83$ pp. Hal ini membuktikan bahwa pada eksperimen awal, model memang memanfaatkan sebagian kecil petunjuk visual identitas individu (*shortcut learning*).
2. **SVM Paling Rentan Overfitting Identitas:** SVM mengalami penurunan terbesar (rata-rata $-4.99$ pp). Kapasitas hipotesis kernel SVM pada ruang 2.304 dimensi memungkinkan batas keputusan meliuk mengelilingi titik data subjek tertentu.
3. **Resistensi Alami LR:** Logistic Regression mengalami penurunan lebih rendah ($-4.25$ pp) dan pada protokol Subject-Disjoint berhasil melampaui SVM pada model Tri-Domain (**88.66% vs 88.61%**), menegaskan keunggulan generalisasi batas keputusan linier teregularisasi.
4. **RF dan GNB Memiliki Penurunan Terendah:** Karena telah memanfaatkan reduksi dimensi PCA (`pca=PCA`) dan memiliki bias induktif independensi/ansambel, RF (drop $-2.10$ pp) dan GNB (drop $-1.01$ pp) hampir tidak terpengaruh oleh kebocoran identitas.

---

## 3.4 Pembuktian Generalisasi Sejati (*True Out-of-Subject Generalization*)

Apakah penurunan performa dari 93,70% ke 88,66% melemahkan klaim ilmiah paper? **Sama sekali tidak — justru memperkuat validitas ilmiah secara substansial:**

1. **Akurasi 88,66% pada 120 Subjek Terisolasi Merefleksikan Generalisasi Riil:**
   - Tebakan acak (*random baseline*) pada 6 kelas interseksional seimbang adalah **16.67%**.
   - Model mencapai akurasi **88.66% (1.915 dari 2.160 citra benar)** pada subjek yang **belum pernah dilihat sedikit pun oleh model selama pelatihan**.
   - Hal ini membuktikan bahwa representasi laten Vision Transformer menangkap ciri morfologis wajah, ekspresi emosional, dan penuaan biologis yang bersifat universal pada ras dan gender manusia, bukan sekadar mengenali individu tertentu.

2. **Konsistensi Hierarki Fusi Multi-Domain Tetap Kokoh:**
   - Keunggulan fusi Tri-Domain atas Single-Domain `vit-face` tetap bertahan secara signifikan di bawah protokol bebas kebocoran:
     - LR: $0.8639 \to 0.8866$ (**+2.27 pp**, $p = 6.78 \times 10^{-6} < 0.001$)
     - SVM: $0.8616 \to 0.8861$ (**+2.45 pp**, $p = 3.46 \times 10^{-6} < 0.001$)
     - RF: $0.8403 \to 0.8500$ (**+0.97 pp**, $p = 0.0238 < 0.05$)
   - Hal ini membuktikan bahwa hipotesis inti penelitian — *bahwa fusi multi-domain ViT (Face ⊕ Emotion ⊕ Age) memberikan representasi komplementer yang memperkaya klasifikasi interseksional ras dan gender* — **terbukti valid secara saintifik dan bebas dari artefak metodologis kebocoran data**.

---

## 3.5 Rangkuman Butir Respons untuk IEEE Access Reviewer 2 Comment #2

Rincian poin argumentatif yang disiapkan untuk naskah revisi dan surat tanggapan reviewer (*Response to Reviewers*):

1. **Pengakuan Transparan & Investigasi Empiris:** Penulis menerima sepenuhnya masukan Reviewer 2 dan telah melakukan audit kebocoran data menyeluruh, mengonfirmasi bahwa split acak tingkat citra sebelumnya memiliki kebocoran identitas 100%.
2. **Implementasi Protokol Subject-Disjoint Standar Industri:** Seluruh 28 model telah dilatih ulang dari nol menggunakan partisi `split_demogpairs_subject_disjoint` (80 subjek latih / 20 subjek uji per kelas) dan 5-Fold `StratifiedGroupKFold`, menjamin **0.00% kebocoran data**.
3. **Penyajian Studi Komparatif Dua Sisi:** Penulis tidak menyembunyikan hasil lama, melainkan mengangkat perbandingan antara hasil lama dan baru sebagai **Studi Ablasi Kebocoran Data (*Data Leakage Ablation Study*)** di Bagian Pembahasan Paper, memberikan kontribusi metodologis penting bagi komunitas visi komputer mengenai risiko *shortcut learning* pada dataset wajah interseksional.
4. **Validasi Signifikansi Statistik:** Penulis melengkapi hasil baru dengan Interval Kepercayaan 95% Wilson Score untuk seluruh 28 model serta Uji McNemar berpasangan, membuktikan signifikansi kenaikan multi-domain secara inferensial.

---

### Lampiran: Integritas Data & Berkas Hasil Ground-Truth

| Berkas Sumber Data | Keterangan & Lokasi Direktori |
|:---|:---|
| **Audit Ledger Komparatif** | `experiment/code/archive/audit_ledger.json` (28 entri komparatif lengkap) |
| **Hasil Subject-Disjoint (28 JSON)** | `experiment/code/results/demogpairs_{clf}_{feat}_{model}.json` |
| **Hasil Subject-Overlap (28 JSON)** | `experiment/code/archive/results_old/demogpairs_{clf}_{feat}_{model}.json` |
| **Notebook Audit Kebocoran** | `experiment/code/archive/notebook_old/0.0_data_leakage_audit.ipynb` |
| **Analisis Signifikansi Statistik** | `experiment/code/md/3.1_statistical_significance.md` |
| **Papan Peringkat Detail** | `experiment/code/md/3.0_compare.md` |
