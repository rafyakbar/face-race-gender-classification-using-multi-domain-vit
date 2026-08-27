# Dual Vision Transformer Integration for Race and Gender Recognition Based on Facial Images

## Informasi Umum
- Judul: Dual Vision Transformer Integration for Race and Gender Recognition Based on Facial Images
- Penulis: Rezky Arisanti Putri (Universitas Negeri Surabaya), Lilik Anifah (Universitas Negeri Surabaya), Ricky Eka Putra (Universitas Negeri Surabaya), Yuni Yamasari (Universitas Negeri Surabaya), Rafy Aulia Akbar (Universitas Negeri Surabaya)
- Tahun: 2025
- Journal / Conference: 2025 8th International Conference on Vocational Education and Electrical Engineering (ICVEE)
- Publisher: IEEE
- ISSN / ISBN: 979-8-3315-8552-5
- Volume / Nomor / Halaman: hlm. 258–264
- DOI: 10.1109/ICVEE66651.2025.11281432
- URL: https://doi.org/10.1109/ICVEE66651.2025.11281432
- Keywords: Vision Transformer, soft biometrics, race recognition, gender recognition, SVM, deep learning, multi-domain feature integration, DemogPairs
- Riwayat Artikel:
  - Published in IEEE Xplore: September 2025
- Lisensi: IEEE Conference Publication
- Jenis Paper: Eksperimen / Applied Research (Studi Prekursor / Dual-Domain Baseline)

---

## Poin-Poin yang Dibahas dalam Introduction
1. Klasifikasi ras dan gender dari citra wajah merupakan biometrik lunak (*soft biometrics*) fundamental yang memiliki peran esensial dalam forensik digital, keamanan publik, pengawasan cerdas, serta personalisasi layanan dan sistem rekomendasi berbasis demografis.
2. Pengenalan demografis otomatis menghadapi tantangan berat akibat definisi ras yang abstrak dan inkonsisten, variasi ekspresi wajah liar, sudut pose, pencahayaan, serta bias bawaan dataset publik yang sering kali timpang dan menguntungkan kelompok tertentu (seperti Kaukasia).
3. Jaringan Konvolusional (CNN) konvensional memiliki keterbatasan struktural dalam memodelkan hubungan spasial global jarak jauh antar-wilayah wajah yang terpisah (*long-range spatial dependencies*).
4. Model *Vision Transformer* (ViT) dengan mekanisme *self-attention* menawarkan representasi spasial global yang superior, namun sebagian besar penelitian yang ada hanya mengandalkan fitur dari domain tunggal (*single-domain features*), sehingga rentan mengalami keterbatasan generalisasi pada populasi heterogen.
5. Fusi fitur multi-domain yang mengintegrasikan struktur anatomi biometrik wajah statis (*facial structure*) dan dinamika ekspresi wajah (*facial expression*) berpotensi meningkatkan akurasi sekaligus memastikan keadilan (*fairness*) antar-subkelompok demografis.

---

## Problem Statement (Apa masalah yang ingin diselesaikan?)

Bagaimana mengatasi keterbatasan model domain tunggal dalam mengenali ras dan gender wajah secara simultan dengan mengintegrasikan representasi fitur statis (struktur biometrik wajah) dan dinamis (ekspresi emosi wajah) dari dua model *Vision Transformer* (*Dual-Domain ViT*) yang dipadukan dengan pengklasifikasi *Support Vector Machine* (SVM) optimal pada dataset berimbang sempurna DemogPairs.

---

## Tujuan Penelitian

1. Mengembangkan arsitektur integrasi dua model Vision Transformer (*Dual-Domain ViT*):
   - **ViT-Face:** Model ViT pre-trained pada VGGFace2 untuk mengekstrak fitur struktur wajah statis (768 dimensi).
   - **ViT-Emotion:** Model ViT pre-trained pada FER-2013 untuk mengekstrak fitur ekspresi emosi dinamis (768 dimensi).
2. Menggabungkan kedua vektor embedding laten menjadi representasi gabungan 1.536 dimensi via konkatenasi langsung.
3. Melakukan klasifikasi 6 kelas interseksional demografis (*Asian_Females, Asian_Males, Black_Females, Black_Males, White_Females, White_Males*) menggunakan *Support Vector Machine* (SVM).
4. Melakukan optimasi hyperparameter SVM secara sistematis (*Grid Search*) dengan skema 5-Fold Cross-Validation.
5. Mengevaluasi performa akurasi, waktu komputasi, dan keadilan demografis (*fairness evaluation*) di seluruh subkelompok pada dataset DemogPairs (10.800 citra).

---

## Research Question

1. Apakah fusi fitur multi-domain dari ViT-Face dan ViT-Emotion mampu menghasilkan peningkatan akurasi dan metrik klasifikasi yang signifikan dibandingkan model fitur tunggal (ViT-Face saja atau ViT-Emotion saja)?
2. Kombinasi hyperparameter SVM (nilai $C$, tipe kernel, derajat polinomial, nilai gamma, dan batas toleransi) mana yang menghasilkan bidang keputusan (*decision hyperplane*) paling optimal untuk vektor fusi 1.536 dimensi?
3. Sejauh mana integrasi Dual-ViT mampu mempertahankan stabilitas performa dan keadilan (*fairness*) di seluruh 6 subkelompok demografis interseksional?

---

## Kontribusi Utama

1. **Framework Integrasi Dual-ViT Multi-Domain:** Merancang pendekatan baru yang memadukan representasi biometrik statis (ViT-Face) dan mikro-ekspresi wajah dinamis (ViT-Emotion) untuk klasifikasi ras dan gender secara terpadu.
2. **Peningkatan Performa di Atas Model Tunggal:** Membuktikan secara empiris bahwa fusi Dual-ViT (1.536-d) menghasilkan akurasi **92,41%**, Precision **0,92**, Recall **0,92**, F1-Score **0,92**, dan ROC-AUC **0,9948**, melampaui ViT-Face tunggal (90,37%) dan ViT-Emotion tunggal (90,19%).
3. **Optimasi Parameter SVM Sistematis:** Menemukan konfigurasi kernel polinomial non-linear optimal ($C = 2,0$, kernel `'poly'`, degree = 2, gamma = `'scale'`, tol = 0,001) yang mampu memetakan hubungan kompleks antar-fitur laten multi-domain.
4. **Analisis Keadilan Demografis Subkelompok (*Demographic Fairness*):** Menunjukkan akurasi stabil antara **97% hingga 98%** dan nilai F1-Score yang seimbang (0,90–0,95) di seluruh 6 subkelompok demografis pada dataset DemogPairs tanpa bias yang merugikan salah satu kelas.

---

## Dataset

### Dataset DemogPairs (10.800 Citra Wajah)
- Nama dataset: DemogPairs (Fernández & Hupont, IEEE FG 2019)
- Jumlah data total: 10.800 citra wajah dari 6 subkelompok demografis yang berimbang sempurna (1.800 citra per kelas).
- Komposisi 6 Kelas Interseksional (3 Ras × 2 Gender):
  1. `Asian_Females` (1.800 citra)
  2. `Asian_Males` (1.800 citra)
  3. `Black_Females` (1.800 citra)
  4. `Black_Males` (1.800 citra)
  5. `White_Females` (1.800 citra)
  6. `White_Males` (1.800 citra)
- Karakteristik Citra: Citra wajah terpotong dan terpusat (*face-centered*), resolusi masukan diubah ke 224 × 224 piksel RGB.
- Skema Pembagian: 5-Fold Stratified Cross-Validation (80% Training / 20% Testing per fold).

---

## Metodologi Penelitian

### Gambaran Umum
Sistem memproses citra wajah DemogPairs melalui dua model Vision Transformer pre-trained secara paralel, mengekstrak embedding token `[CLS]` 768-d dari masing-masing model, menggabungkannya menjadi vektor fusi 1.536-d, dan mengklasifikasikannya menggunakan Support Vector Machine (SVM).

```
                      Citra Wajah Masukan (DemogPairs 224×224×3)
                                          │
                      ┌───────────────────┴───────────────────┐
                      │                                       │
                      ▼                                       ▼
       ┌──────────────────────────────┐        ┌──────────────────────────────┐
       │ 1. ViT-Face                  │        │ 2. ViT-Emotion               │
       │    (skutaada/VIT-VGGFace)    │        │    (FER-2013 Fine-tuned)     │
       │    - Pre-trained VGGFace2    │        │    - Pre-trained FER-2013    │
       │    - Fitur Struktur Statis   │        │    - Fitur Ekspresi Dinamis  │
       │    - Output: Vektor 768-d    │        │    - Output: Vektor 768-d    │
       └──────────────┬───────────────┘        └──────────────┬───────────────┘
                      │                                       │
                      └───────────────────┬───────────────────┘
                                          │
                                          ▼ Konkatenasi Fitur
       ┌──────────────────────────────────────────────────────────────────────┐
       │ 3. Vektor Fitur Gabungan Dual-Domain (1.536 Dimensi)                 │
       │    v_dual = [v_face (768-d), v_emotion (768-d)]                      │
       └──────────────────────────────────┬───────────────────────────────────┘
                                          │
                                          ▼
       ┌──────────────────────────────────────────────────────────────────────┐
       │ 4. Support Vector Machine (SVM) Classification                       │
       │    - Optimasi Hyperparameter via GridSearchCV (48 kombinasi)         │
       │    - Konfigurasi Optimal: C=2.0, Kernel='poly', Degree=2, Gamma='scale'│
       │    - Evaluasi 5-Fold Stratified Cross-Validation                     │
       └──────────────────────────────────┬───────────────────────────────────┘
                                          │
                                          ▼
                Prediksi 6-Kelas Interseksional Ras-Gender
```

### Detail Komponen

#### 1. ViT-Face
- Arsitektur: Vision Transformer Base (`google/vit-base-patch16-224`) yang di-finetune pada dataset VGGFace2 (3,31 juta citra, 9.131 identitas).
- Menghasilkan representasi wajah global invarian terhadap variasi pencahayaan dan pose (vektor embedding 768 dimensi).

#### 2. ViT-Emotion
- Arsitektur: Vision Transformer Base yang di-finetune pada dataset ekspresi FER-2013 (35.887 citra, 7 kategori emosi).
- Menangkap pola deformasi dinamis pada alis, mata, dan mulut (vektor embedding 768 dimensi).

#### 3. Support Vector Machine (SVM)
- Memetakan vektor fusi ke ruang berdimensi tinggi menggunakan fungsi kernel polinomial:
  $$K(x_i, x_j) = (\langle x_i, x_j \rangle + 1)^d$$
- Mengoptimasi margin pemisah antar 6 kelas demografis dengan parameter regularisasi $C$.

---

## Detail Implementasi

### Konfigurasi Pelatihan & Optimasi
- Framework: Python, PyTorch, Scikit-Learn, HuggingFace Transformers
- Input Resolution: 224 × 224 piksel (Patch size 16 × 16 $\rightarrow$ 196 patch)
- Skema Validasi: 5-Fold Stratified Cross-Validation
- Ruang Pencarian Grid Search SVM (48 kombinasi):
  - $C \in [0.1, 1.0, 2.0]$
  - Kernel: `['rbf', 'poly']`
  - Gamma: `['scale', 'auto']`
  - Degree: `[2, 3]`
  - Tolerance (`tol`): `[1e-3, 1e-4]`
  - Max Iterations: 1.000, Probability: True, Random State: 42

---

## Evaluation Metrics

### Metrik Klasifikasi Multi-Kelas
- **Accuracy:** Proporsi total prediksi benar terhadap seluruh sampel uji.
- **Precision:** $\frac{TP}{TP + FP}$ rata-rata makro.
- **Recall:** $\frac{TP}{TP + FN}$ rata-rata makro.
- **F1-Score:** Rata-rata harmonik Precision dan Recall: $\frac{2 \times P \times R}{P + R}$.
- **ROC-AUC:** *Receiver Operating Characteristic — Area Under Curve* (evaluasi probabilitas multi-kelas).
- **Execution Time:** Waktu total ekstraksi fitur dan pelatihan.

---

## Hasil Penelitian

### Temuan Utama

#### 1. Keunggulan Fusi Dual-ViT Dibanding Fitur Tunggal
- **ViT-Face Tunggal:** Akurasi **90,37%** | Precision 0,90 | Recall 0,90 | F1 0,90 | ROC-AUC 0,9920 | Durasi: 8.661 detik (~2,4 jam).
- **ViT-Emotion Tunggal:** Akurasi **90,19%** | Precision 0,90 | Recall 0,90 | F1 0,90 | ROC-AUC 0,9916 | Durasi: 17.653 detik (~4,9 jam).
- **ViT-Face + ViT-Emotion (Dual Fusi):** Akurasi **92,41%** | Precision **0,92** | Recall **0,92** | F1 **0,92** | ROC-AUC **0,9948** | Durasi: 20.428 detik (~5,7 jam).
- Peningkatan akurasi sebesar **+2,04%** membuktikan sifat saling melengkapi (*complementary*) antara fitur identitas statis dan fitur ekspresi dinamis.

#### 2. Konfigurasi Optimal Hyperparameter SVM
- Konfigurasi terbaik: $C = 2,0$, kernel `'poly'`, degree = 2, gamma = `'scale'`, tol = 0,001 (Akurasi rata-rata 5-fold: **92%**).
- Kernel RBF dan kernel polinomial derajat 3 dengan gamma `'auto'` menghasilkan performa lebih rendah (akurasi turun hingga 78%–81%).

#### 3. Evaluasi Keadilan Subkelompok Demografis (*Subgroup Fairness*)
- Performa sangat stabil dan berimbang di seluruh 6 subkelompok:
  - Akurasi berkisar antara **0,97 hingga 0,98** pada seluruh kelas.
  - Nilai F1-Score berkisar antara **0,90 hingga 0,95**:
    - Black Males: F1 **0,95**
    - White Males: F1 **0,95**
    - Asian Males: F1 **0,92**
    - White Females: F1 **0,91**
    - Black Females: F1 **0,91**
    - Asian Females: F1 **0,90**
- Membuktikan bahwa dataset seimbang DemogPairs dan representasi Dual-ViT berhasil memitigasi bias demografis.

---

## Score

### 1. Perbandingan Kinerja Model Tunggal vs Dual-Domain ViT (5-Fold CV)

| Model Ekstraktor | Dimensi Fitur | Accuracy (%) | Precision | Recall | F1-Score | ROC-AUC | Waktu Eksekusi |
|------------------|:-------------:|:------------:|:---------:|:------:|:--------:|:-------:|:--------------:|
| ViT-Face | 768 | 90,37 | 0,90 | 0,90 | 0,90 | 0,9920 | 8.661 s (~2,4 jam) |
| ViT-Emotion | 768 | 90,19 | 0,90 | 0,90 | 0,90 | 0,9916 | 17.653 s (~4,9 jam) |
| **ViT-Face + ViT-Emotion** | **1.536** | **92,41** | **0,92** | **0,92** | **0,92** | **0,9948** | **20.428 s (~5,7 jam)** |

---

### 2. Evaluasi Keadilan Klasifikasi per Subkelompok Demografis (Dual-ViT + SVM)

| Subkelompok Demografis | Accuracy | Precision | Recall | F1-Score |
|------------------------|:--------:|:---------:|:------:|:--------:|
| **Black Males** | 0,98 | 0,97 | 0,94 | 0,95 |
| **White Males** | 0,98 | 0,95 | 0,96 | 0,95 |
| **Asian Males** | 0,97 | 0,90 | 0,93 | 0,92 |
| **White Females** | 0,97 | 0,91 | 0,91 | 0,91 |
| **Black Females** | 0,97 | 0,92 | 0,91 | 0,91 |
| **Asian Females** | 0,97 | 0,90 | 0,90 | 0,90 |

---

### 3. Hasil Hyperparameter Tuning SVM (Top vs Bottom Candidate)

| Peringkat | Parameter Hyperparameter | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Fold 5 | Mean Acc | Mean F1 | Waktu Training (s) |
|:---------:|--------------------------|:------:|:------:|:------:|:------:|:------:|:--------:|:-------:|:------------------:|
| **1 (Best)** | C=2.0, poly, deg=2, gamma='scale', tol=1e-4 | 0,93 | 0,93 | 0,91 | 0,92 | 0,92 | **0,92** | **0,92** | 247,7 s |
| **2** | C=2.0, poly, deg=2, gamma='scale', tol=1e-3 | 0,93 | 0,93 | 0,91 | 0,92 | 0,92 | **0,92** | **0,92** | 238,4 s |
| 47 | C=2.0, poly, deg=3, gamma='auto', tol=1e-3 | 0,81 | 0,78 | 0,78 | 0,77 | 0,78 | 0,78 | 0,79 | 1.331,7 s |
| 48 | C=2.0, poly, deg=3, gamma='auto', tol=1e-4 | 0,81 | 0,78 | 0,78 | 0,77 | 0,78 | 0,78 | 0,79 | 1.172,6 s |

---

## Kelebihan Penelitian

1. **Konsep Fusi Multi-Domain yang Efektif:** Menggabungkan representasi laten struktur biometrik (ViT-Face) dan ekspresi wajah (ViT-Emotion) terbukti saling melengkapi dan mendongkrak akurasi hingga 92,41%.
2. **Keadilan Subkelompok Demografis Terjaga:** Menggunakan dataset DemogPairs berimbang sempurna menghasilkan variasi F1 yang sangat kecil (0,90–0,95) antar-kelompok ras dan gender.
3. **Pemanfaatan Classifier SVM yang Efisien:** Menggunakan SVM non-linear dengan optimasi parameter grid search menghasilkan waktu latih yang cepat (238 detik) dan performa generalisasi tinggi tanpa risiko overfitting lapisan dense dalam.

---

## Keterbatasan Penelitian

1. **Belum Mengintegrasikan Domain Penuaan Biologis (Usia):** Model baru menggabungkan 2 fitur (Identitas + Emosi) dan belum menyertakan domain usia yang memiliki variabilitas morfologi wajah signifikan seiring penuaan.
2. **Ruang Pencarian Hyperparameter Masih Terbatas:** Eksplorasi SVM baru mencakup 48 kombinasi (C = 0.1, 1, 2) tanpa melibatkan pra-pemrosesan scaler (seperti StandardScaler, RobustScaler) dan reduksi PCA.
3. **Biaya Komputasi Ekstraksi Fitur:** Membutuhkan waktu total ekstraksi ~5,7 jam untuk memproses 10.800 citra melalui dua model ViT.

---

## Future Work (Saran Penelitian Selanjutnya)

1. Memperluas kerangka fusi multi-domain dengan menyertakan domain representasi wajah lainnya, khususnya model Vision Transformer spesifik domain penuaan wajah (*ViT-Age*).
2. Memperluas eksplorasi hyperparameter pipeline (mencakup teknik standarisasi data, reduksi dimensi PCA, dan variasi regularisasi $C$ yang lebih luas).
3. Mengembangkan arsitektur end-to-end terpadu yang lebih ringan untuk kebutuhan inferensi waktu nyata (*real-time applications*).

---

## Catatan Penting untuk Riset Kita

### Hubungan Langsung sebagai Studi Prekursor (Dual-Domain $\rightarrow$ Tri-Domain)
- Paper ICVEE 2025 ini merupakan **fondasi awal (studi prekursor)** dari penelitian lanjutan yang sedang kita kerjakan.
- Pada paper ICVEE 2025 ini, tim meneliti integrasi **2 fitur (Dual-Domain)**: ViT-Face + ViT-Emotion (1.536-d), mencapai akurasi **92,41%** pada 5-Fold CV (dan akurasi test split 92,18%).
- Pada penelitian lanjutan kita (**3 Fitur / Tri-Domain: Face + Emotion + Age**):
  1. Kita menambahkan domain ketiga: **ViT-Age (`dima806/facial_age_image_detection`)** untuk menangkap varians morfologi penuaan biologis.
  2. Dimensi fitur diperluas dari 1.536-d menjadi **2.304-d** (768 + 768 + 768).
  3. Ruang pencarian GridSearchCV diperluas menjadi **288 kandidat** (mencakup Scaler: none/Standard/Robust/MinMax, PCA: none/50/100/200, C: 0.1/1/10, kernel: linear/poly/rbf, gamma: scale/auto, degree: 2/3/4).
  4. Performa meningkat signifikan dari **92,18% (Dual)** menjadi **93,70% (Tri-Domain)** pada test set dengan Macro F1 **0,9369** dan CV ROC-AUC **0,9948**, dengan konfigurasi optimal `SVC(C=10, kernel='poly', degree=2, gamma='scale', no-pca, no-scaler)`.

### Perbandingan Evolusi Metodologi: ICVEE 2025 (Dual) vs Riset Kita (Tri-Domain)
| Aspek | Putri et al. (ICVEE 2025 - Dual) | Riset Lanjutan Kita (Tri-Domain) |
|-------|----------------------------------|----------------------------------|
| **Domain Fitur** | 2 Domain: Identitas (ViT-Face) + Emosi (ViT-Emotion) | **3 Domain: Identitas + Emosi + Usia (ViT-Age)** |
| **Dimensi Embedding** | 1.536 Dimensi (768 + 768) | **2.304 Dimensi (768 + 768 + 768)** |
| **Pencarian GridSearch** | 48 Kombinasi Parameter (C: 0.1, 1, 2) | **288 Kombinasi (Scaler, PCA, C: 0.1, 1, 10, Kernel, Degree, Gamma)** |
| **Konfigurasi Terbaik** | SVC(C=2.0, poly, degree=2, gamma='scale') | **SVC(C=10, poly, degree=2, gamma='scale', no-pca, no-scaler)** |
| **Akurasi Test Set** | 92,18% (5-Fold CV Acc: 92,41%) | **93,70% (5-Fold CV Acc: 92,65% $\pm$ 0,83%)** |
| **Macro F1 Test Set** | 0,9217 | **0,9369** |
| **CV ROC-AUC** | 0,9948 | **0,9948** |
| **Jumlah Total Sampel** | DemogPairs (10.800 citra seimbang sempurna) | DemogPairs (10.800 citra seimbang sempurna) |
