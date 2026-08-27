# [JUDUL PAPER]

## Informasi Umum
- Judul:
- Penulis: (nama + afiliasi)
- Tahun:
- Journal / Conference:
- Publisher:
- ISSN / ISBN:
- Volume / Nomor / Halaman:
- DOI:
- URL: (Scopus / DOI / IEEE / sumber resmi)
- Keywords:
- Riwayat Artikel:
  - Received:
  - Revised:
  - Accepted:
  - Published:
- Lisensi:
- Jenis Paper: (Eksperimen / Review / Benchmark / Dataset / dll.)

---

## Poin-Poin yang Dibahas dalam Introduction
1.
2.
3.
...

---

## Problem Statement (Apa masalah yang ingin diselesaikan?)

...

---

## Tujuan Penelitian

...

---

## Research Question

Catatan:
Jika paper tidak menuliskan research question secara eksplisit, nyatakan bahwa research question tidak tersedia, kemudian rumuskan sendiri berdasarkan problem statement dan tujuan penelitian.

1.
2.
...

---

## Kontribusi Utama

1.
2.
3.
... (biasanya ada di bagian akhir introduction)

---

## Dataset

### Dataset 1
- Nama dataset: (DemogPairs, FairFace, UTKFace, CelebA, VGGFace2, LFW, CASIA-WebFace, RAF-DB, dll.)
- Sumber dataset:
- URL: (jika ada)
- Jumlah data: (jumlah citra / jumlah subjek unik)
- Komposisi Demografis:
  - Ras / Etnis: (proporsi Asian, Black, White, Indian, dll.)
  - Gender: (proporsi Female / Male)
  - Usia / Kelompok Umur: (jika ada)
- Keseimbangan data: (Balanced / Imbalanced / Intersectional)
- Resolusi & Format Citra: (224 × 224, JPEG, RGB, dll.)
- Pembagian data: (Train / Validation / Test / K-Fold Stratified Split)
- Status akses: (Open Access / Non-Commercial / Private)
- Label / Anotasi Target: (Race, Gender, Age, Expression/Emotion, Identity, dll.)
- Tujuan penggunaan: (Training / Feature Extraction / Testing / Benchmark)

### Dataset n (jika ada)

---

## Metodologi Penelitian

### Gambaran Umum
...

### Arsitektur / Pendekatan
- Preprocessing & Face Cropping/Alignment: (MTCNN, RetinaFace, Dlib, AutoImageProcessor, Resizing 224 × 224, Normalisasi, dll.)
- Feature Extractor / Backbone Model: (Vision Transformer, ViT-Base, ResNet, EfficientNet, MobileNet, CNN, dll.)
- Domain Fitur yang Diekstrak: (Face Identity, Facial Emotion/Affect, Biological Age, Gender, Ethnicity, dll.)
- Representasi Output: (Token [CLS], Global Average Pooling, Feature Embedding, dll.)
- Dimensi Vektor Fitur: (768-d, 512-d, 1.536-d, 2.304-d, dll.)
- Mekanisme Penggabungan Fitur (*Feature Fusion*): (Concatenation, Cross-Attention, Gating, Multi-Head Fusion, Single-Domain, dll.)
- Penskalaan & Reduksi Dimensi: (MinMaxScaler, StandardScaler, PCA, None, dll.)
- Classifier / Prediction Head: (Support Vector Machine / SVC, Multi-Layer Perceptron / MLP, Softmax, Multi-task Head, dll.)
- Optimasi Hyperparameter: (GridSearchCV, RandomSearch, Manual Tuning, dll.)
- Loss Function: (Cross-Entropy, Focal Loss, Triplet Loss, ArcFace, Contrastive Loss, Fairness-regularized Loss, dll.)
- Pendekatan Keadilan & Mitigasi Bias (*Fairness Strategy*): (Demographic Parity, Equalized Odds, Data Resampling, Cost-sensitive Learning, Adversarial Debiasing, dll.)

### Tahapan Metodologi
1.
2.
3.
...

---

## Detail Implementasi

### Konfigurasi Pelatihan & Optimasi
- Image Size / Input Resolution:
- Batch Size:
- Epoch / Iterasi:
- Learning Rate & Optimizer:
- Hyperparameter Classifier: (C, Kernel, Gamma, Degree untuk SVM / Hidden Layers untuk MLP, dll.)
- Skema Validasi: (5-Fold Stratified Cross-Validation, Hold-out 80/20, dll.)
- Random Seed:

### Lingkungan Implementasi
- Hardware: (GPU / CPU / RAM)
- Framework / Library: (PyTorch, HuggingFace Transformers, Scikit-Learn, Imbalanced-Learn, Joblib, OpenCV, dll.)
- Sistem Operasi:
- Waktu Pelatihan / Ekstraksi:
- Detail implementasi lainnya:

---

## Evaluation Metrics

### Metrik Klasifikasi Global
- Accuracy
- Macro Precision
- Macro Recall
- Macro F1-Score
- ROC-AUC / AUC-OVR

### Metrik Per-Kelas & Keadilan Demografis (*Demographic Fairness*)
- One-vs-Rest (OvR) Accuracy / F1 per subkelompok demografis
- Confusion Matrix (Cross-demographic confusion)
- Disparate Impact (DI) / Demographic Parity Difference (DPD)
- Equalized Odds / Equal Opportunity Difference (EOD)
- Subgroup Disparity Gap (selisih performa kelompok terbaik vs terburuk)
- Verification Metrics (TAR @ FAR = 10⁻⁴, jika relevan)

---

## Hasil Penelitian

### Temuan Utama
...

### Analisis Penulis
...

### Perbandingan dengan Baseline / SOTA
...

---

## Score

### Metrik Global
| Metric | Nilai |
|--------|-------|
| Accuracy | |
| Macro Precision | |
| Macro Recall | |
| Macro F1-Score | |
| ROC-AUC | |

### Metrik Per-Kelompok Demografis (jika tersedia)
| Kelompok Demografis | Accuracy / TAR | Precision | Recall | F1-Score |
|---------------------|:--------------:|:---------:|:------:|:--------:|
| Asian Females | | | | |
| Asian Males | | | | |
| Black Females | | | | |
| Black Males | | | | |
| White Females | | | | |
| White Males | | | | |

---

## Kelebihan Penelitian

1.
2.
3.
...

---

## Keterbatasan Penelitian

1.
2.
3.
...

---

## Future Work (Saran Penelitian Selanjutnya)

1.
2.
3.
...

---

## Catatan Penting untuk Riset Kita

### Insight yang Dapat Diadopsi
...

### Relevansi dengan Kerangka Kerja Multi-Domain ViT (Identity + Emotion + Age) + SVM
...

### Hal yang Membedakan Paper Ini dari Penelitian Kita
...

### Catatan Tambahan
... (jika ada)
