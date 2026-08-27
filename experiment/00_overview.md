# Framework Penelitian — Klasifikasi Ras dan Gender Berbasis Multi-Domain Feature Fusion (Identity, Age, Emotion ViT) + SVM

## Ringkasan

Penelitian ini mengimplementasikan kerangka kerja klasifikasi multi-atribut demografis (ras dan gender) secara terpadu (*intersectional classification*) pada citra wajah dengan pendekatan **Cross-Domain Feature Fusion**. Tiga model *Vision Transformer* (ViT-Base) yang telah dilatih pada domain spesifik digunakan sebagai *feature extractor offline* untuk mengekstrak tiga dimensi representasi wajah:
1. **Fitur Identitas Wajah (*Face Identity*)** menggunakan ViT-VGGFace (`skutaada/VIT-VGGFace`, 768-d).
2. **Fitur Ekspresi & Afek (*Facial Emotion*)** menggunakan ViT-Emotion (`dima806/facial_emotions_image_detection`, 768-d).
3. **Fitur Usia (*Facial Age*)** menggunakan ViT-Age (`dima806/facial_age_image_detection`, 768-d).

Vektor fitur dari ketiga domain tersebut digabungkan (*feature concatenation*) menghasilkan representasi multimodal berdimensi tinggi (2.304-d untuk gabungan 3 fitur), yang kemudian diklasifikasikan ke dalam **6 kelas demografis interseksional** (3 Ras × 2 Gender: *Asian Females*, *Asian Males*, *Black Females*, *Black Males*, *White Females*, *White Males*) menggunakan *Support Vector Classifier* (SVC) yang dioptimasi secara otomatis menggunakan *Grid Search* (288 kombinasi hyperparameter) dan *5-Fold Stratified Cross-Validation*.

**Dataset:** DemogPairs (10.800 citra wajah, seimbang sempurna 1.800 citra per kelas).

---

## Alur Penelitian

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        FASE EKSTRAKSI FITUR OFFLINE                         │
│                                                                             │
│  Dataset DemogPairs (10.800 Citra: 6 Kelas @ 1.800 Citra)                    │
│      │                                                                      │
│      ├── Input Pipeline ViT (AutoImageProcessor: Resize 224×224, Norm)       │
│      │                                                                      │
│      ├── 3 Vision Transformer Feature Extractors (Output [CLS] Token):       │
│      │   • ViT-Face    (skutaada/VIT-VGGFace)                    → 768-d    │
│      │   • ViT-Emotion (dima806/facial_emotions_image_detection) → 768-d    │
│      │   • ViT-Age     (dima806/facial_age_image_detection)     → 768-d    │
│      │                                                                      │
│      └── Disimpan sebagai File Fitur (.pkl):                                │
│          • demogpairs_vit-face.pkl (29,37 MB)                               │
│          • demogpairs_vit-emotion.pkl (29,36 MB)                            │
│          • demogpairs_vit-age.pkl (29,36 MB)                                │
│                                                                             │
│                                      ▼                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                        FASE CROSS-DOMAIN FEATURE FUSION                     │
│                                                                             │
│  Stratified Split 80/20 (Random State 42):                                  │
│  • Training Set : 8.640 sampel (1.440 per kelas)                            │
│  • Testing Set  : 2.160 sampel (360 per kelas)                              │
│                                                                             │
│  7 Skema Konfigurasi Fitur (Ablation Study):                                │
│  1. Single-Domain: vit-age (768-d)                                          │
│  2. Single-Domain: vit-emotion (768-d)                                      │
│  3. Single-Domain: vit-face (768-d)                                         │
│  4. Dual-Domain  : vit-emotion + vit-age (1.536-d)                          │
│  5. Dual-Domain  : vit-face + vit-age (1.536-d)                             │
│  6. Dual-Domain  : vit-emotion + vit-face (1.536-d)                         │
│  7. Tri-Domain   : vit-face + vit-emotion + vit-age (2.304-d) — USULAN      │
│                                                                             │
│                                      ▼                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                    FASE TRAINING & OPTIMASI CLASSIFIER (SVM)                │
│                                                                             │
│  Pipeline Machine Learning (Imbalanced-Learn / Scikit-Learn Pipeline):      │
│  • Scaler: [None, MinMaxScaler()]                                           │
│  • PCA: [None, PCA(n_components=0.5), PCA(n_components=0.75)]               │
│  • Classifier: SVC(probability=True, tol=1e-3)                              │
│    - C: [0.01, 0.1, 1, 10]                                                  │
│    - Kernel: ['rbf', 'poly', 'linear']                                      │
│    - Gamma: ['scale', 'auto']                                               │
│    - Degree: [2, 3]                                                         │
│                                                                             │
│  Grid Search: 288 kombinasi hyperparameter × 5-Fold CV = 1.440 fits / model │
│                                                                             │
│                                      ▼                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                           FASE EVALUASI & ANALISIS                          │
│                                                                             │
│  Evaluasi pada Testing Set Independen (2.160 sampel):                       │
│  • Metrik Global: Accuracy, Macro Precision, Macro Recall, Macro F1-Score   │
│  • Metrik Per-Kelas: One-vs-Rest Accuracy, Precision, Recall, F1, Support   │
│  • Analisis Confusion Matrix & Kesetaraan Demografis (*Demographic Parity*) │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Komponen Utama Riset

### 1. Dataset & Pembagian Data
- **Dataset:** DemogPairs — kumpulan data citra wajah standar untuk studi keadilan algoritmik (*fairness*) dan interseksionalitas demografis yang dikumpulkan dari CWF (*Celebrities in the Wild Faces*) dan VGGFace2.
- **Karakteristik Kelas:** 6 kelas teranotasi seimbang:
  - `Asian_Females` (Label Index: 5) — 1.800 citra
  - `Asian_Males` (Label Index: 2) — 1.800 citra
  - `Black_Females` (Label Index: 4) — 1.800 citra
  - `Black_Males` (Label Index: 0) — 1.800 citra
  - `White_Females` (Label Index: 1) — 1.800 citra
  - `White_Males` (Label Index: 3) — 1.800 citra
  - **Total:** 10.800 citra.
- **Stratified Split (80/20):**
  - **Training:** 8.640 sampel (1.440 per kelas).
  - **Testing:** 2.160 sampel (360 per kelas).

### 2. Feature Extraction (Vision Transformers)
| Ekstraktor | Model HuggingFace | Domain Pre-training | Dimensi Fitur | Output Token | Ukuran File |
|------------|-------------------|---------------------|:-------------:|:------------:|:-----------:|
| **ViT-Face** | `skutaada/VIT-VGGFace` | Face Identity / Recognition (VGGFace) | 768 | `[CLS]` | 29,37 MB |
| **ViT-Emotion** | `dima806/facial_emotions_image_detection` | Facial Emotion Recognition | 768 | `[CLS]` | 29,36 MB |
| **ViT-Age** | `dima806/facial_age_image_detection` | Facial Age Detection | 768 | `[CLS]` | 29,36 MB |

### 3. Skema Feature Fusion
- **Single-Domain:** Menggunakan satu fitur independen (768 dimensi).
- **Dual-Domain:** Menggabungkan 2 fitur (768 + 768 = 1.536 dimensi).
- **Tri-Domain (Usulan Utama):** Menggabungkan 3 fitur (768 + 768 + 768 = 2.304 dimensi).

### 4. Klasifikasi & Optimasi (Support Vector Machine)
- **Model:** `sklearn.svm.SVC` dalam `imblearn.pipeline.Pipeline`.
- **Ruang Pencarian Hyperparameter (288 kombinasi):**
  - Normalisasi: `Scaler` (None, MinMaxScaler())
  - Reduksi Dimensi: `PCA` (None, PCA 50%, PCA 75%)
  - Regularisasi: `C` (0.01, 0.1, 1, 10)
  - Fungsi Kernel: `kernel` ('rbf', 'poly', 'linear')
  - Koefisien Kernel: `gamma` ('scale', 'auto')
  - Derajat Polinomial: `degree` (2, 3)
- **Validasi Silang:** 5-Fold Stratified K-Fold (`refit='accuracy'`).

---

## Ringkasan Hasil Eksperimen (Ablation Study)

Tabel berikut menyajikan perbandingan performa 7 model eksperimen pada data uji independen (2.160 sampel):

| No | Konfigurasi Fitur | Domain | Dimensi | Classifier | Parameter Terbaik | Akurasi | Precision | Recall | F1-Score |
|:--:|-------------------|--------|:-------:|:----------:|-------------------|:-------:|:---------:|:------:|:--------:|
| 1 | `vit-age` | Single | 768 | SVM | C=10, rbf, scale, deg=2, no-pca, no-scaler | 0,8764 | 0,8767 | 0,8764 | 0,8765 |
| 2 | `vit-emotion` | Single | 768 | SVM | C=10, rbf, scale, deg=2, no-pca, no-scaler | 0,9019 | 0,9020 | 0,9019 | 0,9017 |
| 3 | `vit-face` | Single | 768 | SVM | C=10, rbf, scale, deg=2, no-pca, no-scaler | 0,9083 | 0,9084 | 0,9083 | 0,9083 |
| 4 | `vit-emotion-age` | Dual | 1.536 | SVM | C=10, rbf, scale, deg=2, no-pca, no-scaler | 0,9208 | 0,9210 | 0,9208 | 0,9209 |
| 5 | `vit-face-age` | Dual | 1.536 | SVM | C=10, poly, scale, deg=2, no-pca, no-scaler | 0,9255 | 0,9254 | 0,9255 | 0,9254 |
| 6 | `vit-emotion-face` | Dual | 1.536 | SVM | C=10, rbf, scale, deg=2, no-pca, MinMaxScaler | 0,9329 | 0,9333 | 0,9329 | 0,9329 |
| 7 | **`vit-face-emotion-age`** | **Tri-Domain** | **2.304** | **SVM** | **C=10, poly, scale, deg=2, no-pca, no-scaler** | **0,9370** | **0,9372** | **0,9370** | **0,9369** |

### Konfigurasi Terbaik (Model Usulan)
* **Fitur:** `vit-face-emotion-age` (Tri-Domain Fusion: 2.304 dimensi)
* **Classifier:** `SVC`
* **Hyperparameter:** Kernel Polinomial (`poly`), Derajat 2, C=10, Gamma `scale`, tanpa PCA, tanpa Scaler.
* **Skor Evaluasi:**
  * **Test Accuracy:** **93,70%** (2.024 dari 2.160 prediksi benar).
  * **Macro Precision:** **93,72%**.
  * **Macro Recall:** **93,70%**.
  * **Macro F1-Score:** **93,69%**.
  * **5-Fold CV Accuracy:** **92,65%** (± 0,83%) | **CV ROC-AUC:** **0,9948**.

---

## File Referensi Dokumentasi Eksperimen

| Berkas | Konten |
|--------|--------|
| [`01_prepare-data.md`](file:///G:/My%20Drive/Research/BIMA/Face%20Race%20Gender%203%20Fitur/research/experiment/01_prepare-data.md) | Detail dataset DemogPairs, metadata, distribusi kelas, dan prosedur Stratified Split 80/20. |
| [`02_preprocessing.md`](file:///G:/My%20Drive/Research/BIMA/Face%20Race%20Gender%203%20Fitur/research/experiment/02_preprocessing.md) | Preprocessing citra (ViT Processor), representasi vektor `[CLS]`, eksplorasi scaler dan PCA. |
| [`03_feature-extraction.md`](file:///G:/My%20Drive/Research/BIMA/Face%20Race%20Gender%203%20Fitur/research/experiment/03_feature-extraction.md) | Ekstraksi fitur offline ViT-Face, ViT-Emotion, ViT-Age, dan skema penggabungan vektor. |
| [`04_methods.md`](file:///G:/My%20Drive/Research/BIMA/Face%20Race%20Gender%203%20Fitur/research/experiment/04_methods.md) | Metode klasifikasi SVM, konfigurasi Grid Search 288 parameter, 5-fold CV, dan metrik. |
| [`05_results.md`](file:///G:/My%20Drive/Research/BIMA/Face%20Race%20Gender%203%20Fitur/research/experiment/05_results.md) | Analisis hasil komparatif 7 model, confusion matrix, per-class metrics, waktu komputasi, dan insight. |
| [`dataset_demogpairs.md`](file:///G:/My%20Drive/Research/BIMA/Face%20Race%20Gender%203%20Fitur/research/experiment/dataset_demogpairs.md) | Analisis komprehensif struktur dan demografi dataset DemogPairs (3 Ras × 2 Gender). |
