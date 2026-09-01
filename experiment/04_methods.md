# Metode Klasifikasi - Empat Classifier dengan Grid Search with Cross-Validation

## Ringkasan

Penelitian menerapkan empat classifier dalam pipeline modular yang identik untuk memastikan perbandingan yang adil. Pipeline menggabungkan **Feature Scaler - Dimensionality Reducer (PCA) - Classifier** dengan optimasi hyperparameter melalui Grid Search with Cross-Validation (GridSearchCV).

| Classifier | Kombinasi | Fits (x5-Fold) | Parameter Kunci |
|---|:---:|:---:|---|
| Support Vector Classifier (SVM) | 288 | 1.440 | C, kernel, gamma, degree |
| Gaussian Naive Bayes (GNB) | 240 | 1.200 | var_smoothing |
| Random Forest (RF) | 288 | 1.440 | n_estimators, max_depth, max_features |
| Logistic Regression (LR) | 270 | 1.350 | C, solver, max_iter |
| **Gabungan** | **1.086** | **5.430** | per konfigurasi fitur |

Setiap dari 7 konfigurasi fitur dilatih independen untuk keempat classifier, dievaluasi pada 2.160 data uji (held-out, 360 per kelas). Total untuk 7 fitur adalah **38.010 fits** plus 28 model refit final.

---

## Arsitektur Pipeline

Pipeline dibangun agar seluruh transformasi dipelajari hanya dari fold latih dan diterapkan ke fold validasi atau uji tanpa kebocoran data.

```
Input Fitur (768 / 1.536 / 2.304 dimensi)
  -> Feature Scaler [None | MinMaxScaler]
  -> Dimensionality Reducer (PCA) [None | 0.5 | 0.75 varians]
  -> Classifier (SVM | GaussianNB | RandomForest | LogisticRegression)
  -> Prediksi Kelas 0-5
     0=Black_Males, 1=White_Females, 2=Asian_Males,
     3=White_Males, 4=Black_Females, 5=Asian_Females
```

Urutan Scaler - PCA - Classifier bersifat krusial karena PCA sensitif terhadap skala. Opsi None berarti tahap tersebut dilewati sebagai passthrough, sehingga GridSearchCV dapat menguji apakah penskalaan atau reduksi membantu.

---

## Ruang Hyperparameter

**SVM (288):** Scaler 2 x PCA 3 x C 4 x kernel 3 x gamma 2 x degree 2. Parameter menguji regularisasi, jenis kernel (rbf, poly, linear), dan kompleksitas batas keputusan.

**GNB (240):** Scaler 2 x PCA 3 x var_smoothing 40 (rentang logspace -9 sampai 2). Satu-satunya parameter GNB dieksplorasi secara logaritmik karena sensitivitas eksponensial.

**RF (288):** Scaler 2 x PCA 3 x n_estimators 2 x max_depth 3 x min_samples_split 2 x min_samples_leaf 2 x max_features 2. Menguji ukuran ensemble, kedalaman, dan regularisasi pohon.

**LR (270):** Scaler 2 x PCA 3 x C 5 x solver 3 x max_iter 3. Menguji regularisasi, algoritma optimasi (lbfgs, saga, newton-cg), dan batas iterasi hingga 2000.

---

## Protokol GridSearchCV

Validasi menggunakan **5-Fold Stratified Cross-Validation** dengan shuffle dan seed 42, sehingga setiap fold mempertahankan proporsi 6 kelas (16,67% per kelas) dan setiap sampel menjadi data validasi tepat satu kali.

Scoring memakai empat metrik paralel: accuracy, F1-macro, precision-macro, dan recall-macro, dengan **refit berdasarkan accuracy**. Dataset seimbang sempurna, sehingga accuracy tidak bias dan selaras dengan tujuan utama, sementara metrik macro tetap dilaporkan untuk audit fairness.

Alur per kombinasi: fit pipeline pada 4 fold latih, transform dan prediksi pada 1 fold validasi, hitung 4 metrik, lalu rata-rata ke-5 fold. Kombinasi terbaik di-refit pada seluruh 8.640 data latih dan disimpan sebagai best estimator.

Pencegahan kebocoran data dijamin karena scaler dan PCA di-fit di dalam loop Cross-Validation, bukan sebelumnya pada seluruh data latih.

---

## Metrik Evaluasi

**Metrik global (macro-averaged, N=2160):** Accuracy, Macro Precision, Macro Recall, dan Macro F1-Score, masing-masing memberi bobot identik kepada setiap kelompok demografis.

**Metrik per kelas (One-vs-Rest):** Dari confusion matrix 6x6 dihitung TP, FN, FP, TN per kelas, lalu One-vs-Rest Accuracy sebagai (TP+TN)/N, serta precision, recall, dan F1 per kelas untuk audit fairness interseksional.

Hasil disimpan sebagai model terkompresi, file JSON berisi best parameters dan metrik, heatmap confusion matrix, serta tabel peringkat Cross-Validation.

---

## Pengaturan Komputasi

| Aspek | Nilai |
|---|---|
| Backend paralel | threading |
| Alokasi core | 60% CPU logis |
| Reprodusibilitas | seed 42 |
| Error handling | raise (gagal cepat) |
| Persistensi | kompresi level 9 |

Durasi tipikal: SVM tri-domain belasan jam, GNB menit, RF dan LR jam-an tergantung hardware, untuk GridSearch 5-Fold penuh.

---

## Referensi File

- `code/utils/evaluation.py` - orkestrasi GridSearchCV dan metrik
- `code/utils/constants.py` - definisi 6 kelas
- `code/2.1.*`, `2.2.*`, `2.4.*`, `2.5.*` - notebook per classifier
