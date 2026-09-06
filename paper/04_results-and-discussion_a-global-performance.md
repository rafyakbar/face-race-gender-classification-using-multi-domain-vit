# IV. RESULTS AND DISCUSSION

## A. Global Performance

Evaluasi performa RF melintasi tujuh konfigurasi fitur pada data uji DemogPairs disajikan pada [Table VII](#tab7). Hasil eksperimen empiris menunjukkan bahwa skema dual-domain Emotion ⊕ Face mencapai capaian tertinggi dengan Akurasi 86.85% dan F1-Score 86.82%. Sebaliknya, penggabungan tri-domain Face ⊕ Emotion ⊕ Age mengalami sedikit penurunan performa menjadi Akurasi 86.20% dan F1-Score 86.13%. Penurunan ini diinterpretasikan sebagai kemungkinan tantangan partisi ruang fitur berdimensi 2.304 melalui pemotongan pohon acak (random splits). Seluruh konfigurasi RF secara konsisten memilih reduksi dimensionalitas PCA 0.75 untuk menyeimbangkan varians data. Pada kategori domain tunggal, fitur Face mencatatkan performa terbaik dengan Akurasi 85.46%, melampaui fitur domain Emotion sebesar 80.60% serta domain Age sebesar 73.66%.

<a id="tab7"></a>
**Table VII. Performance Benchmark of Random Forest across Seven Feature Configurations.**

| Configuration | Domain Category | Accuracy | Precision | Recall | F1-Score | Best Parameters |
|---|:---:|:---:|:---:|:---:|:---:|---|
| Face | Single | 0.8546 | 0.8543 | 0.8546 | 0.8539 | n_est=200, depth=30, max_feat=log2, min_split=2, min_leaf=1, pca=PCA(0.75), scaler=MinMaxScaler |
| Emotion | Single | 0.8060 | 0.8063 | 0.8060 | 0.8057 | n_est=200, depth=None, max_feat=log2, min_split=5, min_leaf=1, pca=PCA(0.75), scaler=None |
| Age | Single | 0.7366 | 0.7363 | 0.7366 | 0.7354 | n_est=200, depth=30, max_feat=log2, min_split=2, min_leaf=1, pca=PCA(0.75), scaler=None |
| **Emotion ⊕ Face** | **Dual** | **0.8685** | **0.8689** | **0.8685** | **0.8682** | n_est=200, depth=None, max_feat=sqrt, min_split=5, min_leaf=1, pca=PCA(0.75), scaler=None |
| Face ⊕ Age | Dual | 0.8579 | 0.8578 | 0.8579 | 0.8573 | n_est=200, depth=None, max_feat=sqrt, min_split=2, min_leaf=1, pca=PCA(0.75), scaler=None |
| Emotion ⊕ Age | Dual | 0.8111 | 0.8111 | 0.8111 | 0.8108 | n_est=200, depth=None, max_feat=log2, min_split=5, min_leaf=2, pca=PCA(0.75), scaler=None |
| Face ⊕ Emotion ⊕ Age | Tri | 0.8620 | 0.8620 | 0.8620 | 0.8613 | n_est=200, depth=30, max_feat=sqrt, min_split=5, min_leaf=1, pca=PCA(0.75), scaler=None |

Evaluasi performa klasifikasi probabilistik GNB pada tujuh variasi konfigurasi fitur dirangkum pada [Table VIII](#tab8). Meskipun dibatasi oleh asumsi dasar independensi fitur kontinu, model GNB menunjukkan tren peningkatan performa yang konsisten dari kategori domain tunggal ke multi-domain. Pada domain tunggal, konfigurasi Age menghasilkan capaian terendah dengan Akurasi 69.63% dan F1-Score 69.52%, sedangkan fitur Face mencapai Akurasi 82.69%. Integrasi fitur pada kategori dual-domain meningkatkan akurasi secara konsisten, dipimpin oleh kombinasi Emotion ⊕ Face sebesar 84.86%. Puncak performa klasifikasi GNB tercapai pada konfigurasi tri-domain Face ⊕ Emotion ⊕ Age dengan Akurasi 85.05% dan F1-Score 85.05%. Seluruh konfigurasi fitur GNB secara seragam memilih reduksi dimensionalitas PCA 0.75 untuk meminimalkan korelasi antarfitur laten.

<a id="tab8"></a>
**Table VIII. Performance Benchmark of Gaussian Naive Bayes across Seven Feature Configurations.**

| Configuration | Domain Category | Accuracy | Precision | Recall | F1-Score | Best Parameters |
|---|:---:|:---:|:---:|:---:|:---:|---|
| Face | Single | 0.8269 | 0.8271 | 0.8269 | 0.8258 | var_smoothing=4.1246e-02, pca=PCA(0.75), scaler=MinMaxScaler |
| Emotion | Single | 0.7338 | 0.7387 | 0.7338 | 0.7329 | var_smoothing=3.0703e-03, pca=PCA(0.75), scaler=None |
| Age | Single | 0.6963 | 0.6979 | 0.6963 | 0.6952 | var_smoothing=4.3755e-04, pca=PCA(0.75), scaler=MinMaxScaler |
| Emotion ⊕ Face | Dual | 0.8486 | 0.8490 | 0.8486 | 0.8481 | var_smoothing=5.8780e-03, pca=PCA(0.75), scaler=MinMaxScaler |
| Face ⊕ Age | Dual | 0.8315 | 0.8343 | 0.8315 | 0.8317 | var_smoothing=1.1253e-02, pca=PCA(0.75), scaler=MinMaxScaler |
| Emotion ⊕ Age | Dual | 0.7681 | 0.7686 | 0.7681 | 0.7681 | var_smoothing=1.6037e-03, pca=PCA(0.75), scaler=MinMaxScaler |
| **Face ⊕ Emotion ⊕ Age** | **Tri** | **0.8505** | **0.8512** | **0.8505** | **0.8505** | var_smoothing=5.8780e-03, pca=PCA(0.75), scaler=None |

Hasil benchmark performa multinomial LR pada seluruh konfigurasi fitur dipaparkan pada [Table IX](#tab9). Karakteristik utama dari model LR adalah retensi representasi fitur penuh, di mana seluruh skema (tujuh dari tujuh konfigurasi) memilih tanpa reduksi PCA (pca=None). Evaluasi empiris menunjukkan bahwa konfigurasi tri-domain Face ⊕ Emotion ⊕ Age mencatatkan performa tertinggi dengan Akurasi 92.73% dan F1-Score 92.73% melalui parameter penalti C=0.1 serta solver newton-cg. Capaian tri-domain ini melampaui konfigurasi dual-domain terbaik Emotion ⊕ Face yang meraih Akurasi 92.41% dan F1-Score 92.40%, serta mengungguli konfigurasi single-domain terbaik Face dengan Akurasi 90.60%. Temuan ini mengindikasikan efektivitas regularisasi L2 dalam menangani ruang fitur berdimensi tinggi tanpa kompresi komponen utama.

<a id="tab9"></a>
**Table IX. Performance Benchmark of Logistic Regression across Seven Feature Configurations.**

| Configuration | Domain Category | Accuracy | Precision | Recall | F1-Score | Best Parameters |
|---|:---:|:---:|:---:|:---:|:---:|---|
| Face | Single | 0.9060 | 0.9060 | 0.9060 | 0.9059 | C=1, solver=newton-cg, max_iter=500, pca=None, scaler=MinMaxScaler |
| Emotion | Single | 0.8847 | 0.8850 | 0.8847 | 0.8846 | C=1, solver=saga, max_iter=500, pca=None, scaler=MinMaxScaler |
| Age | Single | 0.8648 | 0.8649 | 0.8648 | 0.8648 | C=0.1, solver=lbfgs, max_iter=500, pca=None, scaler=None |
| Emotion ⊕ Face | Dual | 0.9241 | 0.9241 | 0.9241 | 0.9240 | C=0.1, solver=lbfgs, max_iter=500, pca=None, scaler=None |
| Face ⊕ Age | Dual | 0.9162 | 0.9162 | 0.9162 | 0.9162 | C=0.1, solver=newton-cg, max_iter=500, pca=None, scaler=None |
| Emotion ⊕ Age | Dual | 0.9051 | 0.9052 | 0.9051 | 0.9051 | C=0.1, solver=lbfgs, max_iter=500, pca=None, scaler=None |
| **Face ⊕ Emotion ⊕ Age** | **Tri** | **0.9273** | **0.9275** | **0.9273** | **0.9273** | C=0.1, solver=newton-cg, max_iter=500, pca=None, scaler=None |

Perkembangan performa SVM melintasi seluruh tahapan ablasi fitur dirangkum pada [Table X](#tab10). Serupa dengan model linier, seluruh konfigurasi SVM secara konsisten mempertahankan ruang representasi penuh tanpa reduksi PCA (pca=None). Evaluasi empiris memperlihatkan peningkatan performa berjenjang, dimulai dari konfigurasi domain tunggal terbaik Face dengan Akurasi 90.83% dan F1-Score 90.83%. Integrasi representasi pada skema dual-domain Emotion ⊕ Face meningkatkan performa dengan Akurasi 93.29% dan F1-Score 93.29%, sebelum akhirnya mencapai titik tertinggi pada konfigurasi tri-domain Face ⊕ Emotion ⊕ Age dengan Akurasi 93.70% dan F1-Score 93.69%. Pada penalaan hyperparameter, parameter degree bernilai 2 hanya aktif pada fungsi kernel poly, sedangkan model berbasis kernel RBF tidak mengaktifkan parameter tersebut.

<a id="tab10"></a>
**Table X. Performance Benchmark of Support Vector Machine across Seven Feature Configurations.**

| Configuration | Domain Category | Accuracy | Precision | Recall | F1-Score | Best Parameters |
|---|:---:|:---:|:---:|:---:|:---:|---|
| Face | Single | 0.9083 | 0.9084 | 0.9083 | 0.9083 | C=10, rbf, γ=scale, pca=None, scaler=None |
| Emotion | Single | 0.9019 | 0.9020 | 0.9019 | 0.9017 | C=10, rbf, γ=scale, pca=None, scaler=None |
| Age | Single | 0.8764 | 0.8767 | 0.8764 | 0.8765 | C=10, rbf, γ=scale, pca=None, scaler=None |
| Emotion ⊕ Face | Dual | 0.9329 | 0.9333 | 0.9329 | 0.9329 | C=10, rbf, γ=scale, pca=None, scaler=MinMaxScaler |
| Face ⊕ Age | Dual | 0.9255 | 0.9254 | 0.9255 | 0.9254 | C=10, poly, γ=scale, deg=2, pca=None, scaler=None |
| Emotion ⊕ Age | Dual | 0.9208 | 0.9210 | 0.9208 | 0.9209 | C=10, rbf, γ=scale, pca=None, scaler=None |
| **Face ⊕ Emotion ⊕ Age** | **Tri** | **0.9370** | **0.9372** | **0.9370** | **0.9369** | C=10, poly, γ=scale, deg=2, pca=None, scaler=None |

(Catatan: Parameter degree hanya aktif dan dilaporkan pada kernel poly; pada kernel rbf, parameter degree tidak aktif dan tidak dicantumkan pada naskah publikasi).

Sintesis komparatif deskriptif melintasi 28 kombinasi eksperimen menunjukkan bahwa model SVM berbasis fusi tri-domain Face ⊕ Emotion ⊕ Age menempati capaian performa tertinggi dalam ruang pencarian yang dievaluasi, dengan raihan Akurasi 93.70% dan F1-Score 93.69%. Berdasarkan nilai rata-rata performa pengklasifikasi di seluruh konfigurasi fitur, urutan hierarki deskriptif efektivitas algoritma dipimpin oleh SVM (91.47%), diikuti oleh LR (90.40%), RF (82.81%), dan GNB (79.37%). Karakteristik non-linier kernel polinomial pada SVM terbukti efektif dalam memetakan batas keputusan antarsubkelompok demografis berdimensi tinggi. Akan tetapi, perbandingan urutan performa ini sepenuhnya bersifat deskriptif empiris pada pengaturan eksperimen terkontrol dan tidak mencerminkan superioritas statistik mutlak antarfamili algoritma tanpa pengujian hipotesis formal.
