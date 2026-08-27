# MD-ViT: Multidomain Vision Transformer Fusion for Fair Demographic Attribute Recognition

## Informasi Umum
- Judul: MD-ViT: Multidomain Vision Transformer Fusion for Fair Demographic Attribute Recognition
- Penulis: Rezky Arisanti Putri (Universitas Negeri Surabaya), Ricky Eka Putra (Corresponding author, Universitas Negeri Surabaya), Yuni Yamasari (Universitas Negeri Surabaya)
- Tahun: 2025
- Journal / Conference: JIEET (Journal of Information Engineering and Educational Technology)
- Publisher: Department of Informatics, Universitas Negeri Surabaya
- ISSN / ISBN: E-ISSN: 2549-869X
- Volume / Nomor / Halaman: Volume 9, Number 2, 2025, hlm. 64–79
- DOI: 10.26740/jieet.v9n2.p64-79
- URL: https://journal.unesa.ac.id/index.php/jieet/article/view/p64-79
- Keywords: Vision Transformer, demographic classification, fairness, feature fusion, XGBoost, DemogPairs, soft biometrics
- Riwayat Artikel:
  - Submitted: 24 November 2025
  - Accepted: 5 December 2025
  - Available online: 6 December 2025
- Lisensi: Creative Commons Attribution Non-Commercial-Share Alike 4.0 International (CC BY-NC-SA 4.0) — Open Access
- Jenis Paper: Eksperimen / Applied Research (Studi Prekursor / Dual-Domain: Face + Age via XGBoost)

---

## Poin-Poin yang Dibahas dalam Introduction
1. Pengenalan atribut demografis (khususnya klasifikasi ras dan gender) dari citra wajah memegang peranan krusial pada berbagai aplikasi modern, mulai dari kesehatan presisi (*precision healthcare*), forensik digital, kontrol akses aman, hingga analisis sosio-demografis.
2. Model pembelajaran mendalam konvensional sering kali mengalami bias algoritmik dan keterbatasan ketangguhan ketika dihadapkan pada variasi pose, pencahayaan, ekspresi, serta dataset yang tidak seimbang antar-kelompok populasi.
3. Jaringan Konvolusional (CNN, seperti ResNet-50) terbatas oleh operasi konvolusi lokal yang kurang optimal dalam menangkap korelasi spasial global antar-fitur wajah. Sebaliknya, Vision Transformer (ViT) dengan mekanisme *self-attention* mampu memodelkan relasi fitur jarak jauh secara holistik.
4. Sebagian besar penelitian yang ada hanya mengandalkan fitur domain tunggal. Padahal, citra wajah manusia secara alami menyandikan informasi multidimensi yang saling melengkapi (*complementary*), seperti struktur identitas wajah dan pola penuaan biologis (*age-related morphological cues*).
5. Algoritma *eXtreme Gradient Boosting* (XGBoost) menawarkan keunggulan dalam memodelkan interaksi non-linear fitur tingkat tinggi secara efisien dengan regularisasi eksplisit ($L_2$ leaf penalty, gain-based pruning) guna memitigasi *overfitting*.

---

## Problem Statement (Apa masalah yang ingin diselesaikan?)

Bagaimana memitigasi bias algoritmik dan meningkatkan akurasi serta keadilan (*fairness*) klasifikasi interseksional ras dan gender dari citra wajah dengan mengintegrasikan representasi fitur laten biometrik struktural (ViT-VGGFace) dan morfologi penuaan biologis (ViT-Age) yang dipadukan dengan pengklasifikasi *tree-based ensemble* XGBoost pada dataset berimbang DemogPairs.

---

## Tujuan Penelitian

1. Merancang dan mengembangkan kerangka kerja **MD-ViT** (*Multidomain Vision Transformer Fusion*) untuk klasifikasi interseksional ras dan gender secara terpadu.
2. Mengintegrasikan dua model Vision Transformer pre-trained spesifik tugas:
   - **ViT-VGGFace:** Pre-trained pada VGGFace2 untuk mengekstrak fitur struktur identitas statis (768 dimensi).
   - **ViT-Face Age:** Dilatih pada UTKFace dan IMDB-WIKI untuk mengekstrak fitur morfologi penuaan biologis (768 dimensi).
3. Menggabungkan kedua representasi embedding laten menjadi vektor fusi 1.536 dimensi via konkatenasi.
4. Mengklasifikasikan 6 subkelompok demografis interseksional (*Asian Females, Asian Males, Black Females, Black Males, White Females, White Males*) menggunakan algoritma XGBoost.
5. Melakukan optimasi hyperparameter XGBoost secara sistematis melalui 5-Fold Cross-Validation Grid Search pada training set (8.640 citra) dan menguji model pada held-out test set independen (2.160 citra).
6. Mengevaluasi keadilan demografis (*fairness analysis*) di seluruh 6 subkelompok demografis guna memastikan tidak ada kelompok yang dirugikan secara diskriminatif.

---

## Research Question

1. Apakah integrasi fitur lintas-tugas (*cross-task feature fusion*) antara representasi identitas struktural (ViT-VGGFace) dan penuaan biologis (ViT-Age) mampu memberikan peningkatan akurasi prediktif dibandingkan model domain tunggal?
2. Bagaimana konfigurasi hyperparameter XGBoost (metode pohon, kedalaman pohon, bobot daun minimum, parameter regularisasi gamma) mempengaruhi stabilitas validasi silang dan pencegahan *overfitting*?
3. Sejauh mana kerangka kerja MD-ViT mampu menekan disparitas performa (*intersectional bias gap*) lintas 6 subkelompok demografis?

---

## Kontribusi Utama

1. **Framework MD-ViT (Dual-Domain Face + Age):** Mengusulkan kerangka kerja fusi lintas-domain yang memadukan informasi struktural wajah jangka panjang (ViT-VGGFace) dan dinamika penuaan morfologis (ViT-Age) untuk klasifikasi demografis.
2. **Peningkatan Performa atas Baseline Tunggal:** Fusi MD-ViT (1.536-d) dipadukan dengan XGBoost meraih akurasi **89,07%**, Precision **89,09%**, Recall **89,07%**, dan F1-Score **89,06%** pada held-out test set DemogPairs (2.160 citra), mengungguli ViT-VGGFace tunggal (88,61%) dan ViT-Age tunggal (78,94%).
3. **Optimasi Hyperparameter XGBoost Berbasis Hist-Tree:** Menemukan konfigurasi optimal (`tree_method = 'hist'`, `max_depth = 3`, `min_child_weight = 3`, `gamma = 0.0`) yang menghasilkan akurasi 5-Fold CV **89,81%** dengan waktu pelatihan yang sangat efisien (239,16 detik, 16× lebih cepat dibanding metode `'approx'`).
4. **Keadilan Subkelompok Demografis Terbukti:** Analisis keadilan menunjukkan disparitas performa yang sangat minim antar-subkelompok (rentang F1-Score: **87,38% hingga 91,03%** dengan standar deviasi $\sigma = 1,33\%$, selisih gap hanya 3,65%), membuktikan mitigasi bias interseksional yang sangat efektif.

---

## Dataset

### Dataset DemogPairs (10.800 Citra Wajah)
- Nama dataset: DemogPairs (Hupont & Fernández, IEEE FG 2019)
- Total Sampel: **10.800 citra wajah** terkurasi dan terstandarisasi.
- Komposisi 6 Kelas Interseksional (Seimbang Sempurna 1.800 citra per kelas):
  1. `Asian_Females` (1.800 citra)
  2. `Asian_Males` (1.800 citra)
  3. `Black_Females` (1.800 citra)
  4. `Black_Males` (1.800 citra)
  5. `White_Females` (1.800 citra)
  6. `White_Males` (1.800 citra)
- Pembagian Data:
  - **Training Set (80%):** 8.640 citra (1.440 citra per kelas) untuk pelatihan dan 5-Fold CV Grid Search.
  - **Held-Out Testing Set (20%):** 2.160 citra (360 citra per kelas) yang dievaluasi secara independen.
- Resolusi & Format: 224 × 224 piksel RGB.

---

## Metodologi Penelitian

### Gambaran Umum
Pipeline MD-ViT terdiri dari 7 tahapan terstruktur:
1. *Image Input:* Memuat citra wajah teranotasi dari DemogPairs.
2. *Preprocessing:* Resizing ke 224 × 224 piksel, normalisasi ImageNet. ViT-Age menggunakan masukan grayscale untuk mereduksi bias pigmen kulit dan fokus pada tekstur kerutan/pori.
3. *Dataset Splitting:* Pembagian terstratifikasi 80/20.
4. *ViT-Based Feature Extraction:* Ekstraksi paralel token `[CLS]` dari ViT-VGGFace (768-d) dan ViT-Age (768-d).
5. *Feature Fusion:* Penggabungan via konkatenasi menjadi vektor fusi 1.536-d.
6. *Classification via XGBoost:* Pelatihan ensemble pohon keputusan dengan optimasi hyperparameter 5-Fold CV.
7. *Model Evaluation:* Evaluasi metrik makro dan disaggregasi keadilan per subkelompok.

```
                     Citra Wajah Masukan (DemogPairs 224×224)
                                        │
                    ┌───────────────────┴───────────────────┐
                    │                                       │
                    ▼ (RGB Input)                           ▼ (Grayscale Input)
     ┌──────────────────────────────┐        ┌──────────────────────────────┐
     │ 1. ViT-VGGFace               │        │ 2. ViT-Face Age              │
     │    (skutaada/VIT-VGGFace)    │        │    (dima806/facial_age)      │
     │    - Pretrained VGGFace2     │        │    - Pretrained UTK & IMDB   │
     │    - Fitur Identitas/Struktur│        │    - Fitur Penuaan Morfologis│
     │    - Output: Vektor 768-d    │        │    - Output: Vektor 768-d    │
     └──────────────┬───────────────┘        └──────────────┬───────────────┘
                    │                                       │
                    └───────────────────┬───────────────────┘
                                        │
                                        ▼ Konkatenasi Fitur
     ┌──────────────────────────────────────────────────────────────────────┐
     │ 3. Vektor Fitur Gabungan Multidomain (1.536 Dimensi)                 │
     │    v_fused = [v_VGGFace (768-d), v_Age (768-d)]                      │
     └──────────────────────────────────┬───────────────────────────────────┘
                                        │
                                        ▼
     ┌──────────────────────────────────────────────────────────────────────┐
     │ 4. eXtreme Gradient Boosting (XGBoost) Classifier                    │
     │    - Optimasi 5-Fold CV Grid Search pada Training Set                │
     │    - Konfigurasi Optimal: tree_method='hist', max_depth=3, gamma=0.0 │
     │    - Evaluasi Final pada Held-Out Test Set (2.160 Citra)             │
     └──────────────────────────────────┬───────────────────────────────────┘
                                        │
                                        ▼
               Prediksi 6-Kelas Interseksional Ras-Gender
```

### Formulasi Matematika XGBoost
- Prediksi inisial: $f_0(x) = \frac{1}{n} \sum_{i=1}^n y_i$
- Vektor residual: $\hat{Y} = y - f_0(X)$
- Skor Similaritas Node:
  $$\text{Similarity} = \frac{(\sum \hat{y})^2}{\sum [p_1(x_i)(1 - p_1(x_i))] + \lambda}$$
- Gain Pemisahan Node:
  $$\text{Gain} = (\text{Left Similarity} + \text{Right Similarity}) - \text{Root Similarity}$$
- Nilai Bobot Daun (Output Value):
  $$\text{Output Value} = \frac{\sum \hat{y}_i}{\sum [F_{i-1}(x_i)(1 - F_{i-1}(x_i))] + \lambda}$$

---

## Detail Implementasi

### Konfigurasi Model & Pelatihan
- **Feature Extractors:** ViT-Base (`google/vit-base-patch16-224`) fine-tuned pada VGGFace2 dan Facial Age Detection.
- **Classifier:** XGBoost Multiclass Classifier.
- **Ruang Pencarian Grid Search XGBoost:**
  - `tree_method`: `['approx', 'hist']`
  - `max_depth`: `[3, 6, 8]`
  - `gamma`: `[0.0, 0.1, 0.3]`
  - `min_child_weight`: `[1, 3, 5]`
  - `random_state`: 42, `n_jobs`: 1

---

## Evaluation Metrics

### Metrik Klasifikasi Multi-Kelas & Fairness
- **Accuracy (%):** $\frac{TP + TN}{TP + TN + FP + FN}$
- **Precision (%):** $\frac{TP}{TP + FP}$ rata-rata makro.
- **Recall (%):** $\frac{TP}{TP + FN}$ rata-rata makro.
- **F1-Score (%):** $\frac{2 \times P \times R}{P + R}$ rata-rata makro.
- **Disparitas F1 Subkelompok ($\sigma$ dan Gap):** Standar deviasi dan selisih rentang $(\max - \min)$ F1 antar-subkelompok demografis.

---

## Hasil Penelitian

### Temuan Utama

#### 1. Keunggulan Fusi Lintas-Domain (MD-ViT)
- **ViT-Face Age Tunggal:** Akurasi **78,94%** | Precision 78,95% | Recall 78,94% | F1 **78,90%**
- **ViT-VGGFace Tunggal:** Akurasi **88,61%** | Precision 88,63% | Recall 88,61% | F1 **88,59%**
- **ViT-VGGFace-Age (MD-ViT Fusi):** Akurasi **89,07%** | Precision **89,09%** | Recall **89,07%** | F1 **89,06%**
- Mengonfirmasi bahwa penambahan fitur penuaan memberikan perbaikan konsisten (+0,46% akurasi) atas fitur identitas biometrik murni.

#### 2. Dampak Hyperparameter Tuning XGBoost
- Konfigurasi `tree_method = 'hist'` dengan `max_depth = 3`, `min_child_weight = 3`, dan `gamma = 0.0` mencapai akurasi validasi silang tertinggi (**89,81%**) dengan waktu latih tercepat (**239,16 detik**).
- Meningkatkan kedalaman pohon `max_depth` ke 8 menurunkan performa (F1 turun 1,6%) karena memicu *overfitting*.

#### 3. Analisis Keadilan Subkelompok Demografis (*Demographic Fairness*)
- Performa di seluruh 6 subkelompok demografis sangat merata:
  - Akurasi berada pada rentang **95,79% hingga 96,94%** (gap hanya 1,15%).
  - F1-Score berada pada rentang **87,38% hingga 91,03%** dengan standar deviasi hanya $\sigma = 1,33\%$:
    - White Males: F1 **91,03%**
    - Black Males: F1 **90,73%**
    - White Females: F1 **89,99%**
    - Asian Females: F1 **87,71%**
    - Black Females: F1 **87,54%**
    - Asian Males: F1 **87,38%**
- Tidak ditemukan pola bias sistematis yang merugikan kelompok ras atau gender tertentu secara sepihak.

---

## Score

### 1. Evaluasi Komparasi Model Tunggal vs MD-ViT Fusi (Held-Out Test Set: 2.160 Citra)

| Fitur yang Digunakan | Classifier | Accuracy (%) | Precision (%) | Recall (%) | F1-Score (%) |
|----------------------|:----------:|:------------:|:-------------:|:----------:|:------------:|
| ViT-Face Age | XGBoost | 78,94 | 78,95 | 78,94 | 78,90 |
| ViT-VGGFace | XGBoost | 88,61 | 88,63 | 88,61 | 88,59 |
| **ViT-VGGFace-Age (MD-ViT)** | **XGBoost** | **89,07** | **89,09** | **89,07** | **89,06** |

---

### 2. Evaluasi Keadilan per Subkelompok Demografis (MD-ViT + XGBoost pada Test Set)

| Subkelompok Demografis | Accuracy (%) | Precision (%) | Recall (%) | F1-Score (%) |
|------------------------|:------------:|:-------------:|:----------:|:------------:|
| **White Males** | 96,94 | 89,10 | 93,06 | **91,03** |
| **Black Males** | 96,94 | 91,76 | 89,72 | **90,73** |
| **White Females** | 96,62 | 88,89 | 91,11 | **89,99** |
| **Asian Females** | 95,93 | 88,20 | 87,22 | **87,71** |
| **Black Females** | 95,93 | 89,31 | 85,83 | **87,54** |
| **Asian Males** | 95,79 | 87,26 | 87,50 | **87,38** |
| **Rata-rata Makro** | **96,35** | **89,09** | **89,07** | **89,06** |

---

### 3. Perbandingan Konfigurasi Hyperparameter XGBoost (5-Fold CV)

| tree_method | max_depth | min_child_weight | gamma | Mean Accuracy (%) | Mean F1-Score (%) | Waktu Latih (detik) |
|:-----------:|:---------:|:----------------:|:-----:|:-----------------:|:-----------------:|:-------------------:|
| **hist (Best)** | **3** | **3** | **0.0** | **89,81** | **89,81** | **239,16** |
| approx | 3 | 3 | 0.0 | 89,76 | 89,74 | 3.981,62 |
| hist | 3 | 1 | 0.3 | 89,63 | 89,62 | 237,69 |
| approx | 3 | 5 | 0.1 | 89,70 | 89,69 | 2.353,18 |
| hist | 8 | 1 | 0.3 | 88,23 | 88,19 | 365,99 |
| approx | 8 | 1 | 0.3 | 87,94 | 87,91 | 2.678,01 |

---

## Kelebihan Penelitian

1. **Sinergi Lintas-Domain yang Jelas:** Memadukan fitur spasial identitas global dengan morfologi penuaan biologis terbukti memberikan informasi komplementer yang memperkaya representasi.
2. **Efisiensi Komputasi XGBoost:** Algoritma XGBoost dengan metode `hist` mampu memproses vektor 1.536 dimensi dalam 239 detik dengan regularisasi eksplisit yang mencegah overfitting.
3. **Keadilan Subkelompok yang Teruji:** Menunjukkan bahwa fusi fitur pada dataset seimbang berhasil menekan disparitas interseksional hingga rentang F1 hanya 3,65%.
4. **Metodologi Partisi Ketat:** Menggunakan pemisahan data 80% train (untuk 5-Fold CV Grid Search) dan 20% test held-out independen yang dievaluasi satu kali untuk menjamin objektivitas.

---

## Keterbatasan Penelitian

1. **Performa XGBoost Masih di Bawah SVM:** Klasifikasi XGBoost menghasilkan akurasi 89,07%, masih lebih rendah dibandingkan Support Vector Machine (SVM) pada konfigurasi fusi serupa.
2. **Belum Melibatkan Domain Emosi / Ekspresi Wajah:** Model baru menggabungkan 2 domain (Identitas + Usia) dan belum mengikutsertakan domain dinamika ekspresi mikro wajah.
3. **Ekstraksi Fitur Terpisah (Modular):** Proses ekstraksi fitur dilakukan secara terpisah (dua inferensi ViT mandiri) sebelum digabungkan ke classifier tabular, belum beroperasi secara end-to-end.

---

## Future Work (Saran Penelitian Selanjutnya)

1. Mengintegrasikan ketiga domain wajah (Identitas + Usia + Emosi) dalam satu kerangka kerja fusi komprehensif.
2. Membandingkan kinerja XGBoost terhadap algoritma margin optimal seperti Support Vector Machine (SVM) dengan eksplorasi kernel non-linear.
3. Mengembangkan arsitektur end-to-end terpadu yang mampu mempelajari bobot atensi dinamis antar-domain secara simultan.

---

## Catatan Penting untuk Riset Kita

### Hubungan Langsung sebagai Studi Prekursor (Evolusi 2 Fitur ke 3 Fitur)
- Paper JIEET 2025 ini merupakan **studi pendahulu kedua** dari tim riset kita yang mengevaluasi kombinasi **Dual-Domain (Identitas ViT-Face + Usia ViT-Age)** dengan pengklasifikasi **XGBoost** (akurasi 89,07%).
- Studi pendahulu pertama (Putri et al., ICVEE 2025) mengevaluasi **Dual-Domain (Identitas ViT-Face + Emosi ViT-Emotion)** dengan pengklasifikasi **SVM** (akurasi 92,18%–92,41%).
- **Penelitian Lanjutan Kita (Tri-Domain: Face + Emotion + Age + SVM):**
  1. Menyatukan **ketiga domain sekaligus** (*Identitas + Emosi + Usia*), menghasilkan representasi **2.304 dimensi**.
  2. Menggunakan pengklasifikasi **Support Vector Machine (SVC)** dengan pencarian **288 kombinasi parameter** (menguji scaler, PCA, $C=10$, kernel polinomial derajat 2).
  3. Menghasilkan lonjakan performa tertinggi:
     - Dari **89,07%** (MD-ViT XGBoost: Face + Age)
     - Dari **92,18%** (Dual-ViT SVM: Face + Emotion)
     - Menjadi **93,70%** (Tri-Domain ViT + SVM: Face + Emotion + Age) pada test set dengan Macro F1 **0,9369** dan CV ROC-AUC **0,9948**!

### Perbandingan Evolusi Tiga Studi:
| Aspek | MD-ViT (JIEET 2025) | Dual-ViT (ICVEE 2025) | Riset Lanjutan Kita (Tri-Domain) |
|-------|---------------------|----------------------|----------------------------------|
| **Kombinasi Domain** | 2 Domain: Face + Age | 2 Domain: Face + Emotion | **3 Domain: Face + Emotion + Age** |
| **Dimensi Fitur** | 1.536 Dimensi | 1.536 Dimensi | **2.304 Dimensi (768 × 3)** |
| **Classifier** | XGBoost (GridSearch 36 komb) | SVM (GridSearch 48 komb) | **SVM (GridSearchCV 288 komb)** |
| **Konfigurasi Terbaik** | hist, max_depth=3, gamma=0.0 | C=2.0, poly, deg=2, scale | **SVC(C=10, poly, deg=2, scale, no-pca, no-scaler)** |
| **Akurasi Test Set** | 89,07% | 92,18% | **93,70%** |
| **Macro F1 Test Set** | 0,8906 | 0,9217 | **0,9369** |
| **CV Accuracy / ROC** | CV Acc: 89,81% | CV Acc: 92,41% / ROC: 0,9948 | **CV Acc: 92,65% ($\pm$ 0,83%) / ROC: 0,9948** |
| **Dataset** | DemogPairs (10.800 citra) | DemogPairs (10.800 citra) | **DemogPairs (10.800 citra)** |
