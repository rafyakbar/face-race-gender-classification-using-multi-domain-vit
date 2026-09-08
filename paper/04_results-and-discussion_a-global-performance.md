# IV. RESULTS AND DISCUSSION

## A. Global Performance

<a id="tab7"></a>
**Table VII. Performance Benchmark of Random Forest across Seven Feature Configurations.**

| Configuration | Accuracy | Precision | Recall | F1-Score | Best Parameters |
|---|:---:|:---:|:---:|:---:|---|
| Face | 85.46% | 85.43% | 85.46% | 85.39% | n_est=200, depth=30, max_feat=log2,<br>min_split=2, min_leaf=1, pca=PCA(0.75), scaler=MinMaxScaler |
| Emotion | 80.60% | 80.63% | 80.60% | 80.57% | n_est=200, depth=None, max_feat=log2,<br>min_split=5, min_leaf=1, pca=PCA(0.75), scaler=None |
| Age | 73.66% | 73.63% | 73.66% | 73.54% | n_est=200, depth=30, max_feat=log2,<br>min_split=2, min_leaf=1, pca=PCA(0.75), scaler=None |
| **Emotion ⊕ Face** | **86.85%** | **86.89%** | **86.85%** | **86.82%** | n_est=200, depth=None, max_feat=sqrt,<br>min_split=5, min_leaf=1, pca=PCA(0.75), scaler=None |
| Face ⊕ Age | 85.79% | 85.78% | 85.79% | 85.73% | n_est=200, depth=None, max_feat=sqrt,<br>min_split=2, min_leaf=1, pca=PCA(0.75), scaler=None |
| Emotion ⊕ Age | 81.11% | 81.11% | 81.11% | 81.08% | n_est=200, depth=None, max_feat=log2,<br>min_split=5, min_leaf=2, pca=PCA(0.75), scaler=None |
| Face ⊕ Emotion ⊕ Age | 86.20% | 86.20% | 86.20% | 86.13% | n_est=200, depth=30, max_feat=sqrt,<br>min_split=5, min_leaf=1, pca=PCA(0.75), scaler=None |

Evaluasi performa RF melintasi tujuh konfigurasi fitur pada data uji DemogPairs disajikan pada [Table VII](#tab7). Hasil eksperimen empiris menunjukkan bahwa skema dual-domain Emotion ⊕ Face mencapai capaian tertinggi dengan Akurasi 86.85% dan F1-Score 86.82%. Sebaliknya, penggabungan tri-domain Face ⊕ Emotion ⊕ Age mengalami sedikit penurunan performa menjadi Akurasi 86.20% dan F1-Score 86.13%. Penurunan ini diinterpretasikan sebagai kemungkinan tantangan partisi ruang fitur berdimensi 2,304 melalui pemotongan pohon acak (random splits) [[48]](06_references.md#ref48). Seluruh konfigurasi GridSearchCV secara konsisten memilih reduksi dimensionalitas PCA 0.75 untuk menyeimbangkan varians data. Pada kategori domain tunggal, fitur Face mencatatkan performa terbaik dengan Akurasi 85.46%, melampaui fitur domain Emotion sebesar 80.60% serta domain Age sebesar 73.66%.

<a id="tab8"></a>
**Table VIII. Performance Benchmark of Gaussian Naive Bayes across Seven Feature Configurations.**

| Configuration | Accuracy | Precision | Recall | F1-Score | Best Parameters |
|---|:---:|:---:|:---:|:---:|---|
| Face | 82.69% | 82.71% | 82.69% | 82.58% | var_smoothing=4.1246e-02,<br>pca=PCA(0.75), scaler=MinMaxScaler |
| Emotion | 73.38% | 73.87% | 73.38% | 73.29% | var_smoothing=3.0703e-03,<br>pca=PCA(0.75), scaler=None |
| Age | 69.63% | 69.79% | 69.63% | 69.52% | var_smoothing=4.3755e-04,<br>pca=PCA(0.75), scaler=MinMaxScaler |
| Emotion ⊕ Face | 84.86% | 84.90% | 84.86% | 84.81% | var_smoothing=5.8780e-03,<br>pca=PCA(0.75), scaler=MinMaxScaler |
| Face ⊕ Age | 83.15% | 83.43% | 83.15% | 83.17% | var_smoothing=1.1253e-02,<br>pca=PCA(0.75), scaler=MinMaxScaler |
| Emotion ⊕ Age | 76.81% | 76.86% | 76.81% | 76.81% | var_smoothing=1.6037e-03,<br>pca=PCA(0.75), scaler=MinMaxScaler |
| **Face ⊕ Emotion ⊕ Age** | **85.05%** | **85.12%** | **85.05%** | **85.05%** | var_smoothing=5.8780e-03,<br>pca=PCA(0.75), scaler=None |

Evaluasi performa klasifikasi probabilistik GNB pada tujuh variasi konfigurasi fitur dirangkum pada [Table VIII](#tab8). Model GNB menunjukkan tren peningkatan performa yang konsisten dari kategori domain tunggal ke multi-domain. Pada domain tunggal, konfigurasi Age menghasilkan capaian terendah dengan Akurasi 69.63% dan F1-Score 69.52%, sedangkan fitur Face mencapai Akurasi 82.69%. Integrasi fitur pada kategori dual-domain meningkatkan akurasi secara konsisten, dipimpin oleh kombinasi Emotion ⊕ Face sebesar 84.86%. Puncak performa klasifikasi GNB tercapai pada konfigurasi tri-domain Face ⊕ Emotion ⊕ Age dengan Akurasi 85.05% dan F1-Score 85.05%. Seluruh konfigurasi fitur GNB secara seragam memilih reduksi dimensionalitas PCA 0.75 berdasarkan hasil GridSearchCV.

<a id="tab9"></a>
**Table IX. Performance Benchmark of Logistic Regression across Seven Feature Configurations.**

| Configuration | Accuracy | Precision | Recall | F1-Score | Best Parameters |
|---|:---:|:---:|:---:|:---:|---|
| Face | 90.60% | 90.60% | 90.60% | 90.59% | C=1, solver=newton-cg, max_iter=500,<br>pca=None, scaler=MinMaxScaler |
| Emotion | 88.47% | 88.50% | 88.47% | 88.46% | C=1, solver=saga, max_iter=500,<br>pca=None, scaler=MinMaxScaler |
| Age | 86.48% | 86.49% | 86.48% | 86.48% | C=0.1, solver=lbfgs, max_iter=500,<br>pca=None, scaler=None |
| Emotion ⊕ Face | 92.41% | 92.41% | 92.41% | 92.40% | C=0.1, solver=lbfgs, max_iter=500,<br>pca=None, scaler=None |
| Face ⊕ Age | 91.62% | 91.62% | 91.62% | 91.62% | C=0.1, solver=newton-cg, max_iter=500,<br>pca=None, scaler=None |
| Emotion ⊕ Age | 90.51% | 90.52% | 90.51% | 90.51% | C=0.1, solver=lbfgs, max_iter=500,<br>pca=None, scaler=None |
| **Face ⊕ Emotion ⊕ Age** | **92.73%** | **92.75%** | **92.73%** | **92.73%** | C=0.1, solver=newton-cg, max_iter=500,<br>pca=None, scaler=None |

Hasil benchmark performa multinomial LR pada seluruh konfigurasi fitur dipaparkan pada [Table IX](#tab9). Karakteristik utama dari model LR adalah retensi representasi fitur penuh, di mana seluruh skema (tujuh dari tujuh konfigurasi) memilih tanpa reduksi PCA (pca=None) [[49]](06_references.md#ref49). Evaluasi empiris menunjukkan bahwa konfigurasi tri-domain Face ⊕ Emotion ⊕ Age mencatatkan performa tertinggi dengan Akurasi 92.73% dan F1-Score 92.73% melalui parameter penalti C=0.1 serta solver newton-cg. Capaian tri-domain ini melampaui konfigurasi dual-domain terbaik Emotion ⊕ Face yang meraih Akurasi 92.41% dan F1-Score 92.40%, serta mengungguli konfigurasi single-domain terbaik Face dengan Akurasi 90.60%. Temuan ini mengindikasikan efektivitas regularisasi L2 dalam menangani ruang fitur berdimensi tinggi tanpa kompresi komponen utama [[50]](06_references.md#ref50).

<a id="tab10"></a>
**Table X. Performance Benchmark of Support Vector Machine across Seven Feature Configurations.**

| Configuration | Accuracy | Precision | Recall | F1-Score | Best Parameters |
|---|:---:|:---:|:---:|:---:|---|
| Face | 90.83% | 90.84% | 90.83% | 90.83% | C=10, rbf, γ=scale,<br>pca=None, scaler=None |
| Emotion | 90.19% | 90.20% | 90.19% | 90.17% | C=10, rbf, γ=scale,<br>pca=None, scaler=None |
| Age | 87.64% | 87.67% | 87.64% | 87.65% | C=10, rbf, γ=scale,<br>pca=None, scaler=None |
| Emotion ⊕ Face | 93.29% | 93.33% | 93.29% | 93.29% | C=10, rbf, γ=scale,<br>pca=None, scaler=MinMaxScaler |
| Face ⊕ Age | 92.55% | 92.54% | 92.55% | 92.54% | C=10, poly, γ=scale, deg=2,<br>pca=None, scaler=None |
| Emotion ⊕ Age | 92.08% | 92.10% | 92.08% | 92.09% | C=10, rbf, γ=scale,<br>pca=None, scaler=None |
| **Face ⊕ Emotion ⊕ Age** | **93.70%** | **93.72%** | **93.70%** | **93.69%** | C=10, poly, γ=scale, deg=2,<br>pca=None, scaler=None |

(Catatan: Parameter degree hanya aktif dan dilaporkan pada kernel poly; pada kernel rbf, parameter degree tidak aktif dan tidak dicantumkan pada naskah publikasi).

Perkembangan performa SVM melintasi seluruh tahapan ablasi fitur dirangkum pada [Table X](#tab10). Serupa dengan model linier, seluruh konfigurasi SVM secara konsisten mempertahankan ruang representasi penuh tanpa reduksi PCA (pca=None). Evaluasi empiris memperlihatkan peningkatan performa berjenjang, dimulai dari konfigurasi domain tunggal terbaik Face dengan Akurasi 90.83% dan F1-Score 90.83%. Integrasi representasi pada skema dual-domain Emotion ⊕ Face meningkatkan performa dengan Akurasi 93.29% dan F1-Score 93.29%, sebelum akhirnya mencapai titik tertinggi pada konfigurasi tri-domain Face ⊕ Emotion ⊕ Age dengan Akurasi 93.70% dan F1-Score 93.69%. Pada hyperparameter, parameter degree bernilai 2 hanya aktif pada fungsi kernel poly, sedangkan model berbasis kernel RBF tidak mengaktifkan parameter tersebut [[51]](06_references.md#ref51).

Hasil 28 eksperimen pada [Table VII](#tab7), [Table VIII](#tab8), [Table IX](#tab9), dan [Table X](#tab10) menunjukkan bahwa SVM dengan fusi tri-domain Face ⊕ Emotion ⊕ Age memberikan performa tertinggi dalam seluruh konfigurasi yang diuji. Model tersebut mencapai Akurasi 93.70% dan F1-Score 93.69%. Jika dirata-ratakan pada tujuh konfigurasi fitur, SVM memperoleh Akurasi 91.47%, diikuti oleh LR 90.40%, RF 82.81%, dan GNB 79.37%. Pada konfigurasi SVM tri-domain, GridSearchCV memilih kernel polinomial derajat 2 sebagai konfigurasi terbaik. Temuan ini berlaku pada data dan ruang pencarian yang digunakan, sehingga tidak dapat diartikan sebagai keunggulan universal kernel polinomial. Perbandingan tersebut bersifat deskriptif dan tidak membuktikan superioritas statistik suatu classifier karena penelitian ini tidak melakukan pengujian hipotesis formal.
