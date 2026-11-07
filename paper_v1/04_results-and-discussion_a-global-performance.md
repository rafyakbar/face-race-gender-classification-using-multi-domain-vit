# IV. RESULTS AND DISCUSSION

## A. Global Performance

<a id="tab7"></a>
**Table VII. Performance Benchmark of Random Forest across Seven Feature Configurations.**

| Configuration | Accuracy | 95% CI | CV Score | Precision | Recall | F1-Score | Best Parameters |
|---|:---:|:---:|:---:|:---:|:---:|:---:|---|
| Face | 85.46% | [83.91%, 86.89%] | 87.07% ± 0.68% | 85.43% | 85.46% | 85.39% | n_est=200, depth=30, max_feat=log2,<br>min_split=2, min_leaf=1, pca=PCA(0.75), scaler=MinMaxScaler |
| Emotion | 80.60% | [78.88%, 82.21%] | 79.65% ± 1.01% | 80.63% | 80.60% | 80.57% | n_est=200, depth=None, max_feat=log2,<br>min_split=5, min_leaf=1, pca=PCA(0.75), scaler=None |
| Age | 73.66% | [71.76%, 75.47%] | 72.93% ± 0.85% | 73.63% | 73.66% | 73.54% | n_est=200, depth=30, max_feat=log2,<br>min_split=2, min_leaf=1, pca=PCA(0.75), scaler=None |
| **Emotion ⊕ Face** | **86.85%** | **[85.36%, 88.21%]** | **87.72% ± 0.69%** | **86.89%** | **86.85%** | **86.82%** | n_est=200, depth=None, max_feat=sqrt,<br>min_split=5, min_leaf=1, pca=PCA(0.75), scaler=None |
| Face ⊕ Age | 85.79% | [84.25%, 87.20%] | 87.20% ± 0.84% | 85.78% | 85.79% | 85.73% | n_est=200, depth=None, max_feat=sqrt,<br>min_split=2, min_leaf=1, pca=PCA(0.75), scaler=None |
| Emotion ⊕ Age | 81.11% | [79.41%, 82.71%] | 80.07% ± 0.87% | 81.11% | 81.11% | 81.08% | n_est=200, depth=None, max_feat=log2,<br>min_split=5, min_leaf=2, pca=PCA(0.75), scaler=None |
| Face ⊕ Emotion ⊕ Age | 86.20% | [84.68%, 87.59%] | 87.48% ± 0.86% | 86.20% | 86.20% | 86.13% | n_est=200, depth=30, max_feat=sqrt,<br>min_split=5, min_leaf=1, pca=PCA(0.75), scaler=None |

Evaluasi performa RF melintasi tujuh konfigurasi fitur pada data uji DemogPairs disajikan pada [Table VII](#tab7). Hasil eksperimen empiris menunjukkan bahwa skema dual-domain Emotion ⊕ Face mencapai capaian tertinggi dengan Akurasi 86.85% dan F1-Score 86.82%. Sebaliknya, penggabungan tri-domain Face ⊕ Emotion ⊕ Age mengalami sedikit penurunan performa menjadi Akurasi 86.20% dan F1-Score 86.13%. Penurunan ini diinterpretasikan sebagai kemungkinan tantangan partisi ruang fitur berdimensi 2,304 melalui pemotongan pohon acak (random splits) [[48]](06_references.md#ref48). Seluruh konfigurasi GridSearchCV secara konsisten memilih reduksi dimensionalitas PCA 0.75 untuk menyeimbangkan varians data. Pada kategori domain tunggal, fitur Face mencatatkan performa terbaik dengan Akurasi 85.46%, melampaui fitur domain Emotion sebesar 80.60% serta domain Age sebesar 73.66%.

<a id="tab8"></a>
**Table VIII. Performance Benchmark of Gaussian Naive Bayes across Seven Feature Configurations.**

| Configuration | Accuracy | 95% CI | CV Score | Precision | Recall | F1-Score | Best Parameters |
|---|:---:|:---:|:---:|:---:|:---:|:---:|---|
| Face | 82.69% | [81.03%, 84.22%] | 84.04% ± 0.74% | 82.71% | 82.69% | 82.58% | var_smoothing=4.1246e-02,<br>pca=PCA(0.75), scaler=MinMaxScaler |
| Emotion | 73.38% | [71.48%, 75.20%] | 73.11% ± 1.09% | 73.87% | 73.38% | 73.29% | var_smoothing=3.0703e-03,<br>pca=PCA(0.75), scaler=None |
| Age | 69.63% | [67.66%, 71.53%] | 69.19% ± 0.75% | 69.79% | 69.63% | 69.52% | var_smoothing=4.3755e-04,<br>pca=PCA(0.75), scaler=MinMaxScaler |
| Emotion ⊕ Face | 84.86% | [83.29%, 86.31%] | 85.65% ± 0.73% | 84.90% | 84.86% | 84.81% | var_smoothing=5.8780e-03,<br>pca=PCA(0.75), scaler=MinMaxScaler |
| Face ⊕ Age | 83.15% | [81.51%, 84.67%] | 84.34% ± 0.72% | 83.43% | 83.15% | 83.17% | var_smoothing=1.1253e-02,<br>pca=PCA(0.75), scaler=MinMaxScaler |
| Emotion ⊕ Age | 76.81% | [74.98%, 78.54%] | 75.54% ± 1.13% | 76.86% | 76.81% | 76.81% | var_smoothing=1.6037e-03,<br>pca=PCA(0.75), scaler=MinMaxScaler |
| **Face ⊕ Emotion ⊕ Age** | **85.05%** | **[83.48%, 86.49%]** | **85.53% ± 0.57%** | **85.12%** | **85.05%** | **85.05%** | var_smoothing=5.8780e-03,<br>pca=PCA(0.75), scaler=None |

Evaluasi performa klasifikasi probabilistik GNB pada tujuh variasi konfigurasi fitur dirangkum pada [Table VIII](#tab8). Meskipun model ini mengasumsikan independensi kondisional antarfitur, GNB menunjukkan tren peningkatan performa yang konsisten dari kategori domain tunggal ke multi-domain. Pada domain tunggal, konfigurasi Age menghasilkan capaian terendah dengan Akurasi 69.63% dan F1-Score 69.52%, sedangkan fitur Face mencapai Akurasi 82.69%. Integrasi representasi pada kategori dual-domain meningkatkan akurasi secara bertahap, dipimpin oleh kombinasi Emotion ⊕ Face sebesar 84.86%. Puncak performa klasifikasi GNB tercapai pada konfigurasi tri-domain Face ⊕ Emotion ⊕ Age dengan Akurasi 85.05% dan F1-Score 85.05%. Seluruh konfigurasi fitur GNB secara seragam memilih reduksi dimensionalitas PCA 0.75 berdasarkan hasil penalaan GridSearchCV.

<a id="tab9"></a>
**Table IX. Performance Benchmark of Logistic Regression across Seven Feature Configurations.**

| Configuration | Accuracy | 95% CI | CV Score | Precision | Recall | F1-Score | Best Parameters |
|---|:---:|:---:|:---:|:---:|:---:|:---:|---|
| Face | 90.60% | [89.30%, 91.76%] | 90.52% ± 0.59% | 90.60% | 90.60% | 90.59% | C=1, solver=newton-cg, max_iter=500,<br>pca=None, scaler=MinMaxScaler |
| Emotion | 88.47% | [87.06%, 89.75%] | 87.18% ± 0.76% | 88.50% | 88.47% | 88.46% | C=1, solver=saga, max_iter=500,<br>pca=None, scaler=MinMaxScaler |
| Age | 86.48% | [84.97%, 87.86%] | 84.91% ± 0.58% | 86.49% | 86.48% | 86.48% | C=0.1, solver=lbfgs, max_iter=500,<br>pca=None, scaler=None |
| Emotion ⊕ Face | 92.41% | [91.21%, 93.45%] | 91.89% ± 0.54% | 92.41% | 92.41% | 92.40% | C=0.1, solver=lbfgs, max_iter=500,<br>pca=None, scaler=None |
| Face ⊕ Age | 91.62% | [90.38%, 92.72%] | 91.53% ± 0.47% | 91.62% | 91.62% | 91.62% | C=0.1, solver=newton-cg, max_iter=500,<br>pca=None, scaler=None |
| Emotion ⊕ Age | 90.51% | [89.20%, 91.67%] | 89.26% ± 0.69% | 90.52% | 90.51% | 90.51% | C=0.1, solver=lbfgs, max_iter=500,<br>pca=None, scaler=None |
| **Face ⊕ Emotion ⊕ Age** | **92.73%** | **[91.56%, 93.75%]** | **92.19% ± 0.45%** | **92.75%** | **92.73%** | **92.73%** | C=0.1, solver=newton-cg, max_iter=500,<br>pca=None, scaler=None |

Hasil benchmark performa multinomial LR pada seluruh konfigurasi fitur dipaparkan pada [Table IX](#tab9). Karakteristik utama dari model LR adalah retensi representasi fitur penuh, di mana seluruh skema (tujuh dari tujuh konfigurasi) memilih tanpa reduksi PCA (pca=None) [[49]](06_references.md#ref49). Evaluasi empiris menunjukkan bahwa konfigurasi tri-domain Face ⊕ Emotion ⊕ Age mencatatkan performa tertinggi dengan Akurasi 92.73% dan F1-Score 92.73% melalui parameter penalti C=0.1 serta solver newton-cg. Capaian tri-domain ini melampaui konfigurasi dual-domain terbaik Emotion ⊕ Face yang meraih Akurasi 92.41% dan F1-Score 92.40%, serta mengungguli konfigurasi single-domain terbaik Face dengan Akurasi 90.60%. Temuan ini mengindikasikan efektivitas regularisasi L2 dalam menangani ruang fitur berdimensi tinggi tanpa kompresi komponen utama [[50]](06_references.md#ref50).

<a id="tab10"></a>
**Table X. Performance Benchmark of Support Vector Machine across Seven Feature Configurations.**

| Configuration | Accuracy | 95% CI | CV Score | Precision | Recall | F1-Score | Best Parameters |
|---|:---:|:---:|:---:|:---:|:---:|:---:|---|
| Face | 90.83% | [89.54%, 91.98%] | 91.41% ± 0.85% | 90.84% | 90.83% | 90.83% | C=10, rbf, γ=scale,<br>pca=None, scaler=None |
| Emotion | 90.19% | [88.86%, 91.37%] | 88.38% ± 0.54% | 90.20% | 90.19% | 90.17% | C=10, rbf, γ=scale,<br>pca=None, scaler=None |
| Age | 87.64% | [86.18%, 88.96%] | 86.78% ± 0.70% | 87.67% | 87.64% | 87.65% | C=10, rbf, γ=scale,<br>pca=None, scaler=None |
| Emotion ⊕ Face | 93.29% | [92.15%, 94.27%] | 92.31% ± 0.80% | 93.33% | 93.29% | 93.29% | C=10, rbf, γ=scale,<br>pca=None, scaler=MinMaxScaler |
| Face ⊕ Age | 92.55% | [91.36%, 93.58%] | 92.30% ± 0.57% | 92.54% | 92.55% | 92.54% | C=10, poly, γ=scale, deg=2,<br>pca=None, scaler=None |
| Emotion ⊕ Age | 92.08% | [90.87%, 93.15%] | 90.17% ± 0.65% | 92.10% | 92.08% | 92.09% | C=10, rbf, γ=scale,<br>pca=None, scaler=None |
| **Face ⊕ Emotion ⊕ Age** | **93.70%** | **[92.60%, 94.65%]** | **92.65% ± 0.93%** | **93.72%** | **93.70%** | **93.69%** | C=10, poly, γ=scale, deg=2,<br>pca=None, scaler=None |

Perkembangan performa SVM melintasi seluruh tahapan ablasi fitur dirangkum pada [Table X](#tab10). Serupa dengan model linier, seluruh konfigurasi SVM secara konsisten mempertahankan ruang representasi penuh tanpa reduksi PCA (pca=None). Evaluasi empiris memperlihatkan peningkatan performa berjenjang, dimulai dari konfigurasi domain tunggal terbaik Face dengan Akurasi 90.83% dan F1-Score 90.83%. Integrasi representasi pada skema dual-domain Emotion ⊕ Face meningkatkan performa dengan Akurasi 93.29% dan F1-Score 93.29%, sebelum akhirnya mencapai titik tertinggi pada konfigurasi tri-domain Face ⊕ Emotion ⊕ Age dengan Akurasi 93.70% dan F1-Score 93.69%. Pada hyperparameter, parameter degree bernilai 2 hanya aktif pada fungsi kernel poly, sedangkan model berbasis kernel RBF tidak mengaktifkan parameter tersebut [[51]](06_references.md#ref51).

Sintesis dari 28 eksperimen pada [Table VII](#tab7), [Table VIII](#tab8), [Table IX](#tab9), dan [Table X](#tab10) menetapkan SVM tri-domain Face ⊕ Emotion ⊕ Age sebagai model terbaik dengan Akurasi 93.70% dan F1-Score 93.69%. Rata-rata akurasi melintasi seluruh konfigurasi mencatat keunggulan SVM (91.47%), diikuti LR (90.40%), RF (82.81%), dan GNB (79.37%). Hasil Uji McNemar berpasangan antara Tri-Domain vs Dual-Domain pada SVM mencatat selisih +9 citra (+0.41%, chi2 = 1.0492, p = 0.3057, p > 0.05), serta pada RF diperoleh selisih -14 citra (-0.65%, chi2 = 1.4825, p = 0.2232, p > 0.05). Ketiadaan signifikansi statistik tersebut mengindikasikan fenomena asymptotic feature saturation (kejenuhan representasi fitur), di mana fusi Dual-Domain Emotion ⊕ Face telah menyerap mayoritas varians diskriminatif utama.
