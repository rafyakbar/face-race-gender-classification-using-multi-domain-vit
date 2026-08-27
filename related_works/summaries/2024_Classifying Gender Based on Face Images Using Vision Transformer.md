# Classifying Gender Based on Face Images Using Vision Transformer

## Informasi Umum
- Judul: Classifying Gender Based on Face Images Using Vision Transformer
- Penulis: Ganjar Gingin Tahyudin (Telkom University, Indonesia), Mahmud Dwi Sulistiyo (Telkom University, Indonesia), Muhammad Arzaki (Telkom University, Indonesia), Ema Rachmawati (Telkom University, Indonesia)
- Tahun: 2024
- Journal / Conference: International Journal on Informatics Visualization (JOIV)
- Publisher: Politeknik Negeri Padang
- ISSN / ISBN: 2549-9904 (Online), 2549-9610 (Print)
- Volume / Nomor / Halaman: Volume 8, Number 1 (March 2024), hlm. 18–25
- DOI: 10.62527/joiv.8.1.1923
- URL: http://joiv.org/index.php/joiv/article/view/1923 (Scopus: https://www.scopus.com/pages/publications/85191010901)
- Keywords: Gender; classification; face image; vision transformer
- Riwayat Artikel:
  - Received: 21 June 2023
  - Revised: 3 October 2023
  - Accepted: 6 November 2023
  - Date of publication: 31 March 2024
- Lisensi: Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) — Open Access
- Jenis Paper: Eksperimen / Applied Research

---

## Poin-Poin yang Dibahas dalam Introduction
1. Dalam era visi komputer modern, klasifikasi otomatis gender dari citra wajah memainkan peran penting pada berbagai aplikasi cerdas seperti sistem keamanan, kontrol akses gedung, personalisasi antarmuka pengguna, dan pemasaran produk bertarget.
2. Meskipun secara komputasi gender merupakan tugas klasifikasi biner sederhana (*Male vs Female*), variabilitas visual wajah di dunia nyata sangat tinggi akibat perbedaan ras/etnis, kelompok usia, gaya rambut, ekspresi wajah, dan kondisi pencahayaan.
3. Sebagian besar penelitian terdahulu mengandalkan arsitektur *Convolutional Neural Networks* (CNN) atau fitur *handcrafted* (seperti MB-LBP, SIFT, HOG) yang dipadukan dengan SVM atau Naïve Bayes.
4. Model *Vision Transformer* (ViT) yang mengadopsi mekanisme *self-attention* untuk memodelkan hubungan spasial global antar-patch citra menawarkan paradigma baru yang potensial melampaui CNN.
5. Masih sangat sedikit penelitian yang mengeksplorasi secara empiris dampak variasi ukuran citra (*pixel resolution*), ukuran patch (*patch size*), serta keandalan generalisasi ViT lintas kelompok ras (*racial groups*) dan rentang usia (*age groups*).

---

## Problem Statement (Apa masalah yang ingin diselesaikan?)

Bagaimana efektivitas model *Vision Transformer* (ViT) dalam mengenali gender dari citra wajah pada variasi ukuran piksel masukan (160 × 160 vs 224 × 224) dan jumlah patch (8 hingga 32), serta bagaimana keandalan generalisasinya pada evaluasi dataset internal (*same-dataset*) dan evaluasi lintas-dataset (*cross-dataset*) dengan menganalisis pola kesalahan klasifikasi (*misclassification rate*) pada 4 kelompok ras (Asian, Black, Caucasian, Indian) dan 12 kelompok usia (0 hingga 116 tahun).

---

## Tujuan Penelitian

1. Menerapkan arsitektur *Vision Transformer* (ViT) dengan kedalaman 12 lapisan encoder untuk klasifikasi gender biner berbasis citra wajah.
2. Mengeksplorasi 10 skenario kombinasi resolusi citra (160 × 160 dan 224 × 224 piksel) dengan berbagai ukuran patch (8, 10, 14, 16, 20, 28, dan 32 patch).
3. Melatih model pada dataset skala besar AFAD (*Asian Face Age Dataset*) yang memuat 165.432 citra wajah Asia.
4. Mengevaluasi performa model pada pengujian *same-dataset* (AFAD test set) dan *cross-dataset* menggunakan benchmark independen UTKFace (26.132 citra).
5. Melakukan analisis misklasifikasi mendalam untuk memetakan disparitas performa lintas 4 kelompok rasial dan 12 kategori rentang usia.

---

## Research Question

1. Bagaimana pengaruh kombinasi resolusi citra dan ukuran patch terhadap akurasi pelatihan, validasi, dan pengujian model Vision Transformer pada klasifikasi gender?
2. Sejauh mana model ViT yang dilatih pada populasi wajah ras Asia (AFAD) mampu mempertahankan akurasinya ketika diuji secara lintas-dataset pada populasi multi-ras (UTKFace)?
3. Kelompok ras dan rentang usia mana yang mengalami tingkat kesalahan klasifikasi gender paling tinggi, serta faktor visual apa yang menyebabkannya?

---

## Kontribusi Utama

1. **Eksplorasi Sistematis Resolusi & Patch Size ViT:** Melakukan evaluasi komparatif 10 skenario kombinasi ukuran piksel (160×160 vs 224×224) dan patch size (8 s.d. 32) pada arsitektur Vision Transformer untuk klasifikasi gender wajah.
2. **Capaian Tinggi pada Evaluasi Same-Dataset (AFAD):** Meraih akurasi validasi terbaik **96,76%** (resolusi 160×160, patch 8) dan akurasi pengujian tertinggi **98,43%** (resolusi 224×224, patch 28).
3. **Evaluasi Lintas-Dataset Terstandarisasi (UTKFace):** Menemukan bahwa konfigurasi 224 × 224 piksel dengan 14 patch merupakan yang paling optimal pada pengujian *cross-dataset*, mencapai akurasi **81,74%**, Precision **81,88%**, Recall **81,89%**, dan F1-score **81,89%**.
4. **Analisis Disparitas Rasial dan Rentang Usia:**
   - Membuktikan bahwa model memiliki misklasifikasi terendah pada kelompok ras asalnya (Asian: 20,9%), diikuti African/Black (33,9%), Indian (44,2%), dan tertinggi pada Caucasian/White (50,4%).
   - Membuktikan bahwa model bekerja sangat optimal pada usia dewasa produktif 21–70 tahun (akurasi >80%, terbaik usia 41–50 tahun: 83,24%), namun mengalami penurunan performa drastis pada anak-anak (0–10 tahun: error 43,07%) dan usia lanjut ekstrem (>80 tahun).

---

## Dataset

### 1. Dataset Pelatihan Utama: AFAD (Asian Face Age Dataset)
- Nama dataset: AFAD Dataset (Niu et al., 2016)
- Jumlah data total: 165.432 citra wajah subjek ras Asia (berusia 15 hingga 40 tahun).
- Komposisi Gender: Male (101.752 citra) dan Female (63.680 citra).
- Pembagian data:
  - **Training Set (90%):** 149.000 citra (91.300 pria, 57.700 wanita).
  - **Validation Set (5%):** 8.276 citra (5.190 pria, 3.086 wanita).
  - **Testing Set (5%):** 8.275 citra (5.067 pria, 3.208 wanita).
- Format Citra: RGB, variasi pose dan pencahayaan terkontrol.
- Status akses: Terbuka untuk riset akademik non-komersial.

### 2. Dataset Evaluasi Lintas-Dataset: UTKFace
- Nama dataset: UTKFace (Zhang et al., 2017)
- URL: https://susanqq.github.io/UTKFace/
- Jumlah data total: 26.132 citra wajah (11.316 pria dan 12.392 wanita / 23.708 citra terpakai).
- Komposisi Ras: 4 kelompok ras (White/Caucasian, Black/African, Asian, Indian).
- Rentang Usia: 0 hingga 116 tahun (dianalisis ke dalam 12 kategori umur).
- Karakteristik Tantangan: Kondisi liar (*in-the-wild*) dengan rentang ekspresi, oklusi, dan iluminasi yang lebar.
- Tujuan penggunaan: Evaluasi ketahanan generalisasi model terhadap perbedaan domain, ras, dan usia.

---

## Metodologi Penelitian

### Gambaran Umum
Penelitian ini membangun sistem klasifikasi gender berbasis Vision Transformer yang dilatih pada dataset AFAD dan diuji secara ganda (*same-dataset* dan *cross-dataset*).

```
                      Citra Wajah Masukan (AFAD / UTKFace)
                                       │
                                       ▼
             ┌───────────────────────────────────────────────────┐
             │ 1. Pra-pemrosesan & Augmentasi Citra              │
             │    - Resizing: 160×160 piksel dan 224×224 piksel  │
             │    - Augmentasi: Random Rotation, Zoom, Horiz-Flip│
             └─────────────────────────┬─────────────────────────┘
                                       │
                                       ▼
             ┌───────────────────────────────────────────────────┐
             │ 2. Pemotongan Patch (Patch Partitioning)          │
             │    - Resolusi Patch (P, P): 8, 10, 14, 16, 20, 28 │
             │    - Proyeksi Linier ke 1D Patch Embeddings       │
             │    - Penambahan Positional Embedding & [CLS] Token│
             └─────────────────────────┬─────────────────────────┘
                                       │
                                       ▼
             ┌───────────────────────────────────────────────────┐
             │ 3. Vision Transformer Encoder (12 Layers)         │
             │    - Multi-Head Self-Attention (MHSA)             │
             │    - Multi-Layer Perceptron (MLP Blocks)          │
             │    - Layer Normalization & Residual Connections   │
             └─────────────────────────┬─────────────────────────┘
                                       │
                                       ▼
             ┌───────────────────────────────────────────────────┐
             │ 4. Klasifikasi Head & Evaluasi Performa           │
             │    - Dense Binary Classifier [Male / Female]      │
             │    - Same-Dataset Testing (AFAD)                  │
             │    - Cross-Dataset Testing & Error Analysis (UTK) │
             └───────────────────────────────────────────────────┘
```

### Arsitektur / Pendekatan
- **Vision Transformer (ViT):**
  - Mengubah citra masukan $x \in \mathbb{R}^{H \times W \times C}$ menjadi urutan patch terflaten $x_p \in \mathbb{R}^{N \times (P^2 C)}$, di mana $(P, P)$ adalah resolusi patch dan $N = (HW) / P^2$ adalah jumlah patch.
  - Setiap patch diproyeksikan secara linier ke dimensi embedding konstan, ditambah vektor posisi (*positional embeddings*) dan token klasifikasi `[CLS]`.
  - Terdiri dari 12 blok Transformer Encoder berstruktur *Multi-Head Self-Attention* (MHSA) dan MLP.
- **Konfigurasi Skenario yang Dieksplorasi (10 Skenario):**
  - Resolusi 160 × 160 piksel dengan patch size: 8, 10, 16, 20, dan 32.
  - Resolusi 224 × 224 piksel dengan patch size: 8, 14, 16, 28, dan 32.
- **Classifier:** Lapisan Dense linier biner di atas token representasi `[CLS]`.

---

## Detail Implementasi

### Konfigurasi Pelatihan & Optimasi
- **Arsitektur:** Vision Transformer (12 Transformer Encoder Layers)
- **Learning Rate:** 0,001 (konstan)
- **Epochs:** 100 epoch
- **Data Augmentation:** Random rotation, random zoom, dan random horizontal flip
- **Resolusi Uji:** 160 × 160 piksel dan 224 × 224 piksel
- **Evaluasi Cross-Dataset:** Confusion matrix biner teradaptasi (True Male, True Female, False Male, False Female)

---

## Evaluation Metrics

### Metrik Klasifikasi Biner
- **Accuracy:** $\frac{TM + TF}{TM + TF + FM + FF}$
- **Precision:** Rata-rata aritmatika dari $\text{Precision}_{\text{Male}} = \frac{TM}{TM + FM}$ dan $\text{Precision}_{\text{Female}} = \frac{TF}{TF + FF}$
- **Recall:** Rata-rata aritmatika dari $\text{Recall}_{\text{Male}} = \frac{TM}{TM + FF}$ dan $\text{Recall}_{\text{Female}} = \frac{TF}{TF + FM}$
- **F1-Score:** Rata-rata harmonik dari Precision dan Recall:
  $$\text{F1-Score} = \frac{2 \times \text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$
- **Misclassification Rate (%):** Persentase kesalahan prediksi gender pada masing-masing kelompok ras dan 12 kelompok umur.

---

## Hasil Penelitian

### Temuan Utama

#### 1. Hasil Evaluasi Same-Dataset (AFAD Dataset)
- Pada dataset AFAD (populasi Asia), model ViT meraih performa sangat tinggi pada seluruh skenario (akurasi selalu >91%):
  - **Akurasi Validasi Tertinggi:** **96,76%** pada ukuran citra 160 × 160 piksel dengan patch size 8.
  - **Akurasi Pengujian Tertinggi:** **98,43%** pada ukuran citra 224 × 224 piksel dengan patch size 28.
  - Menambah jumlah patch tidak selalu berbanding lurus dengan peningkatan akurasi (patch size 32 menghasilkan akurasi terendah: 91,54%).

#### 2. Hasil Evaluasi Cross-Dataset (UTKFace Dataset)
- Pengujian lintas-dataset menunjukkan penurunan performa akibat perbedaan distribusi domain (*domain shift*):
  - **Konfigurasi Terbaik:** Ukuran citra 224 × 224 piksel dengan 14 patch menghasilkan **Akurasi 81,74%**, **Precision 81,88%**, **Recall 81,89%**, dan **F1-score 81,89%**.
  - Konfigurasi terendah terjadi pada ukuran 160 × 160 dengan patch 32 (Akurasi 67,89%).

#### 3. Analisis Misklasifikasi Berdasarkan Kelompok Ras (UTKFace)
- Karena model dilatih khusus pada AFAD (wajah Asia), tingkat kesalahan klasifikasi gender paling rendah diperoleh pada kelompok **Asian** (**20,9%** error / 75,80% correct), diikuti **African/Black** (33,9% error), **Indian** (44,2% error), dan tertinggi pada **Caucasian/White** (50,4% error).
- Temuan ini membuktikan adanya bias representasi yang kuat ketika model dilatih pada populasi ras tunggal.

#### 4. Analisis Misklasifikasi Berdasarkan Rentang Usia (12 Kelompok)
- **Kelompok Usia Optimal:** Model bekerja sangat baik pada rentang usia 21 hingga 70 tahun dengan akurasi selalu di atas 80% (puncak akurasi pada usia 41–50 tahun sebesar **83,24%** dengan error terendah 16,76%).
- **Kelompok Usia Rentan Kesalahan:** 
  - Anak-anak (usia 0–10 tahun): Error mencapai **43,07%** karena fitur dimorfisme seksual sekunder pada wajah belum terbentuk.
  - Lansia sangat tua (usia 81–90 tahun error 42,16%, usia 91–100 tahun error 57,58%, dan usia 111–116 tahun error **87,50%**) akibat kerutan penuaan ekstrem yang mengaburkan ciri gender.

---

## Score

### 1. Evaluasi Same-Dataset pada AFAD Dataset (10 Skenario)

| Resolusi Citra (Piksel) | Patch Size | Validation Accuracy | Testing Accuracy |
|:-----------------------:|:----------:|:-------------------:|:----------------:|
| 160 × 160 | 8 | **0,9676** | 0,9661 |
| 160 × 160 | 10 | 0,9628 | 0,9598 |
| 160 × 160 | 16 | 0,9609 | 0,9610 |
| 160 × 160 | 20 | 0,9485 | 0,9460 |
| 160 × 160 | 32 | 0,9196 | 0,9154 |
| 224 × 224 | 8 | 0,9639 | 0,9631 |
| 224 × 224 | 14 | 0,9667 | 0,9644 |
| 224 × 224 | 16 | 0,9633 | 0,9622 |
| **224 × 224** | **28** | 0,9492 | **0,9843** |
| 224 × 224 | 32 | 0,9381 | 0,9362 |

---

### 2. Evaluasi Cross-Dataset pada UTKFace Dataset (10 Skenario)

| Resolusi Citra (Piksel) | Patch Size | Accuracy | Precision | Recall | F1-Score |
|:-----------------------:|:----------:|:--------:|:---------:|:------:|:--------:|
| 160 × 160 | 8 | 0,8061 | 0,8070 | 0,8074 | 0,8072 |
| 160 × 160 | 10 | 0,7820 | 0,8050 | 0,7999 | 0,8024 |
| 160 × 160 | 16 | 0,7810 | 0,7814 | 0,7819 | 0,7817 |
| 160 × 160 | 20 | 0,7915 | 0,7947 | 0,7938 | 0,7942 |
| 160 × 160 | 32 | 0,6789 | 0,6970 | 0,6857 | 0,6913 |
| 224 × 224 | 8 | 0,8096 | 0,8096 | 0,8085 | 0,8089 |
| **224 × 224** | **14** | **0,8174** | **0,8188** | **0,8189** | **0,8189** |
| 224 × 224 | 16 | 0,8032 | 0,8109 | 0,8066 | 0,7983 |
| 224 × 224 | 28 | 0,7854 | 0,7921 | 0,7886 | 0,7903 |
| 224 × 224 | 32 | 0,7734 | 0,7734 | 0,7740 | 0,7737 |

---

### 3. Akurasi Klasifikasi Gender Berdasarkan Kelompok Usia pada UTKFace

| Rentang Usia (Tahun) | Persentase Benar (Correct) (%) | Persentase Salah (Incorrect) (%) |
|:--------------------:|:------------------------------:|:--------------------------------:|
| **0–10** | 56,93 | 43,07 |
| **11–20** | 74,20 | 25,80 |
| **21–30** | 82,35 | 17,65 |
| **31–40** | 82,12 | 17,88 |
| **41–50 (Optimal)** | **83,24** | **16,76** |
| **51–60** | 81,46 | 18,54 |
| **61–70** | 81,06 | 18,94 |
| **71–80** | 73,14 | 26,86 |
| **81–90** | 57,84 | 42,16 |
| **91–100** | 42,42 | 57,58 |
| **101–110** | 76,92 | 23,08 |
| **111–116** | 12,50 | 87,50 |

---

## Kelebihan Penelitian

1. **Eksplorasi Empiris Patch Size ViT yang Sistematis:** Menunjukkan secara gamblang bagaimana interaksi antara ukuran piksel dan ukuran patch mempengaruhi proses pembelajaran atensi global pada citra wajah.
2. **Analisis Cross-Dataset yang Jujur:** Tidak hanya mengevaluasi model pada dataset pelatihan yang sama, tetapi juga menguji batas generalisasi model pada dataset eksternal (UTKFace).
3. **Pemetaan Kesalahan Demografis & Usia yang Rinci:** Menyajikan analisis kuantitatif kegagalan klasifikasi melintasi 4 ras dan 12 kelompok umur secara komprehensif.

---

## Keterbatasan Penelitian

1. **Pelatihan Terbatas pada Satu Ras (AFAD):** Karena hanya dilatih pada populasi Asia, model mengalami bias rasial yang parah dan penurunan akurasi yang signifikan pada pengujian lintas-ras (turun dari 98,43% ke 81,74%).
2. **Hanya Menggunakan Single-Task ViT Tunggal:** Model dilatih *from scratch* pada tugas biner gender tanpa memanfaatkan *pre-trained weights* skala besar atau integrasi fitur komplementer multi-domain.
3. **Kinerja Rendah pada Usia Ekstrem:** Model mengalami kegagalan deteksi gender pada anak-anak di bawah 10 tahun dan lansia di atas 80 tahun karena belum mengintegrasikan fitur penuaan khusus.

---

## Future Work (Saran Penelitian Selanjutnya)

1. Melatih model Vision Transformer pada dataset multi-ras yang berimbang untuk mengeliminasi bias kelompok etnis tertentu.
2. Menggabungkan model ViT dengan teknik lain (*hybrid / multi-domain feature fusion*) untuk memperkuat pembedaan fitur gender pada kelompok usia ekstrem.
3. Mengembangkan mekanisme transfer learning dari model representasi wajah berskala besar.

---

## Catatan Penting untuk Riset Kita

### Insight yang Dapat Diadopsi
- **Bahaya Pelatihan pada Dataset Monorasial:** Penelitian Tahyudin et al. menjadi bukti empiris yang sangat kuat bahwa melatih model pada satu ras tertentu (AFAD) akan menyebabkan kegagalan generalisasi (*drop* akurasi hingga ~17%) saat berhadapan dengan populasi multi-ras. Ini memperkuat justifikasi metodologis mengapa penelitian kita menggunakan **DemogPairs (10.800 citra seimbang sempurna 3 Ras × 2 Gender)**.
- **Kerentanan Fitur Wajah terhadap Usia:** Temuan bahwa penuaan ekstrem mendistorsi pengenalan gender memvalidasi keputusan riset kita untuk menyertakan **ViT-Age** (`dima806/facial_age`) bersama **ViT-Face** dan **ViT-Emotion**.

### Relevansi dengan Kerangka Kerja Multi-Domain ViT (Identity + Emotion + Age) + SVM
- Pada riset Tahyudin et al., model ViT tunggal dilatih *from scratch* hanya untuk gender biner dan terbukti rentan terhadap pergeseran ras dan usia (akurasi cross-dataset hanya 81,74%).
- Pada penelitian kita:
  1. Kita memanfaatkan **3 Pre-trained Vision Transformers** yang telah terlatih pada domain masing-masing: ViT-Face (VGGFace), ViT-Emotion (Ekspresi), dan ViT-Age (Usia).
  2. Vektor fusi laten 2.304 dimensi menangkap korelasi holistik antara bentuk identitas, dinamika otot wajah, dan proses penuaan biologis.
  3. Klasifikasi dilakukan menggunakan **Support Vector Classifier (SVC)** dengan optimasi *GridSearchCV* 288 parameter pada DemogPairs, menghasilkan **akurasi 93,70%** pada 6 kelas interseksional ras dan gender secara seimbang dan adil.

### Hal yang Membedakan Paper Ini dari Penelitian Kita
| Aspek | Tahyudin et al. (2024) | Penelitian Kita |
|-------|------------------------|-----------------|
| **Tugas Target** | Klasifikasi Gender Biner (Male vs Female) | Klasifikasi Interseksional Terpadu 6-Kelas (3 Ras × 2 Gender) |
| **Arsitektur Ekstraktor** | Single ViT (Train from scratch, 12 layers) | 3 Pre-trained Vision Transformers (ViT-Face, ViT-Emotion, ViT-Age) |
| **Representasi Fitur** | Single-domain token [CLS] biner | Multi-Domain Latent Feature Fusion (2.304-d) |
| **Classifier** | Dense Linear Head (SoftMax/Sigmoid) | Support Vector Classifier (SVC) dengan GridSearchCV (288 kombinasi) |
| **Dataset Pelatihan** | AFAD (165k citra — Hanya Ras Asia) | DemogPairs (10.800 citra — 3 Ras × 2 Gender seimbang sempurna) |
| **Akurasi Cross-Dataset / Uji** | 81,74% (Gender biner pada UTKFace) | **93,70%** (6-Kelas Interseksional pada DemogPairs) |
