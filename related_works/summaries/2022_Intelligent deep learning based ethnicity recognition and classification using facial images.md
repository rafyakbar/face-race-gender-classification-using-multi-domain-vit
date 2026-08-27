# Intelligent Deep Learning Based Ethnicity Recognition and Classification Using Facial Images

## Informasi Umum
- Judul: Intelligent deep learning based ethnicity recognition and classification using facial images
- Penulis: Gurram Sunitha (Sree Vidyanikethan Engineering College, India), K. Geetha (SRM Institute of Science and Technology, India), S. Neelakandan (R.M.K Engineering College, India), Aditya Kumar Singh Pundir (Arya College of Engineering and Information Technology, India), S. Hemalatha (Kongu Engineering College, India), Vinay Kumar (GLA University, India)
- Tahun: 2022
- Journal / Conference: Image and Vision Computing (Elsevier)
- Publisher: Elsevier B.V.
- ISSN / ISBN: 0262-8856
- Volume / Nomor / Halaman: Volume 121, Article 104404, hlm. 1–12
- DOI: 10.1016/j.imavis.2022.104404
- URL: https://www.sciencedirect.com/science/article/pii/S0262885622000336
- Keywords: Ethnicity recognition, Facial analysis, Deep learning, Facial landmarks, Image classification, Parameter tuning
- Riwayat Artikel:
  - Received: 16 August 2021
  - Revised: 17 January 2022
  - Accepted: 10 February 2022
  - Available online: 15 February 2022
- Lisensi: Elsevier ScienceDirect Article
- Jenis Paper: Eksperimen / Applied Research

---

## Poin-Poin yang Dibahas dalam Introduction
1. Analisis citra wajah dalam visi komputer telah berkembang pesat untuk mengekstrak biometrik lunak (*soft biometrics*) seperti identitas, gender, usia, etnisitas, dan ekspresi emosi.
2. Otomasi pengenalan etnis dan ras memiliki implikasi penting dalam bidang kedokteran/farmakogenomik terarah ras, interaksi manusia-komputer (*HCI*), pengawasan video cerdas (*surveillance*), forensik, dan periklanan bertarget.
3. Etnisitas merupakan atribut wajah yang paling sedikit dieksplorasi secara mendalam karena subjektivitas persepsi manusia, kurangnya konsensus taksonomi ras, dan adanya fenomena bias kognitif *Other-Race Effect* (ORE) dalam pelabelan dataset.
4. Metode tradisional berbasis fitur buatan tangan (*handcrafted features*) gagal mempertahankan akurasi pada citra liar (*in-the-wild*) akibat variasi ekstrem pada pencahayaan, sudut pose, dan oklusi.
5. Pemanfaatan jaringan konvolusional dalam (*Deep CNN*) yang dikombinasikan dengan pengklasifikasi cepat berbasis kernel dan optimasi metaheuristik menawarkan solusi superior untuk klasifikasi etnisitas skala besar.

---

## Problem Statement (Apa masalah yang ingin diselesaikan?)

Bagaimana merancang pipeline pengenalan etnisitas otomatis (*IDL-ERCFI*) yang mampu menstandarkan citra wajah liar melalui penyelarasan *facial landmarks*, mengekstrak representasi fitur mendalam menggunakan model *Xception*, mereduksi *curse of dimensionality* via *Principal Component Analysis* (PCA), serta mengklasifikasikan etnis secara akurat dan efisien menggunakan *Kernel Extreme Learning Machine* (KELM) yang parameternya dioptimasi secara otomatis menggunakan algoritma metaheuristik *Glowworm Swarm Optimization* (GSO).

---

## Tujuan Penelitian

1. Mengembangkan arsitektur terintegrasi **IDL-ERCFI** (*Intelligent Deep Learning-based Ethnicity Recognition and Classification using Facial Images*) untuk klasifikasi etnisitas dari citra wajah.
2. Mengintegrasikan pra-pemrosesan 2D berbasis *landmark alignment* untuk menstabilkan variasi pose dan rotasi kepala.
3. Memanfaatkan jaringan *Xception* sebagai ekstraktor fitur representasi spasial dan *cross-channel* yang mendalam.
4. Menerapkan PCA untuk mereduksi dimensi vektor fitur Xception tanpa menghilangkan varians diskriminatif esensial.
5. Mengimplementasikan pengklasifikasi KELM yang dioptimasi menggunakan algoritma metaheuristik GSO guna mencapai konvergensi cepat dan akurasi klasifikasi multi-ras yang superior pada dataset BUPT-GLOBALFACE.

---

## Research Question

1. Bagaimana efektivitas penyelarasan wajah 2D berbasis landmark dalam menormalisasi orientasi wajah sebelum diekstraksi oleh jaringan deep learning?
2. Sejauh mana reduksi dimensi linear PCA mampu mengatasi *curse of dimensionality* dari vektor fitur Xception (2.048 dimensi) tanpa menurunkan ketepatan klasifikasi etnis?
3. Apakah optimasi parameter KELM berbasis *Glowworm Swarm Optimization* (GSO) mampu mengungguli pengklasifikasi standar seperti SVM, MLP, dan SoftMax dalam hal akurasi dan stabilitas lintas pengujian?

---

## Kontribusi Utama

1. **Kerangka Kerja IDL-ERCFI Terpadu:** Menggabungkan 5 tahapan modular: *Pre-processing* $\rightarrow$ Ekstraksi Fitur *Xception* $\rightarrow$ Reduksi Fitur *PCA* $\rightarrow$ Klasifikasi *KELM* $\rightarrow$ *Tuning* Parameter *GSO*.
2. **Pemanfaatan Arsitektur Xception:** Mengadopsi *depthwise separable convolutions* untuk mengekstraksi representasi fitur laten 2.048 dimensi yang kaya informasi fenotipe rasial.
3. **Kombinasi PCA dan KELM:** Mengatasi *curse of dimensionality* sekaligus memanfaatkan kecepatan komputasi KELM yang tidak memerlukan pembaruan gradien iteratif (*non-backpropagation*).
4. **Optimasi Hyperparameter Berbasis GSO:** Menggunakan algoritma perilaku kunang-kunang (*glowworm*) untuk menemukan pasangan parameter regulasi $C$ dan parameter kernel KELM yang optimal berdasarkan fungsi fitness 10-fold cross-validation.
5. **Performa Luar Biasa pada Skala Besar:** Mencapai akurasi rata-rata **98,97%–99,05%** dan ROC-AUC **99,86%** pada benchmark BUPT-GLOBALFACE (4 kelas ras), melampaui berbagai metode *state-of-the-art* (seperti VGGFace-SVM, R-Net, dan Inception-ResNet-v2).

---

## Dataset

### Dataset: BUPT-GLOBALFACE (BUPT Equalized Face Dataset)
- Nama dataset: BUPT-GLOBALFACE (bagian dari inisiatif BUPT Equalized Face)
- Sumber dataset: Beijing University of Posts and Telecommunications (BUPT), dirilis Agustus 2019
- Jumlah data total: 1,3 juta citra dari 29.000 selebriti (didistribusikan merata ~320.000 citra per ras).
- Subset Eksperimen yang Digunakan: Total **440.000 citra wajah**:
  - **Training Set:** 400.000 citra (100.000 citra per ras).
  - **Validation Set:** 32.000 citra (8.000 citra per ras).
  - **Testing Set (Exam Set):** 8.000 citra (2.000 citra per ras).
- Komposisi Demografis:
  - 4 Kelompok Ras Utama: **Caucasian**, **African**, **Asian**, **Indian** (seimbang sempurna 25% per kelas).
- Karakteristik Citra: Kondisi liar (*in-the-wild*) dengan rentang variasi sudut *yaw* dan *roll* yang lebar, variasi ekspresi, usia, dan pencahayaan.
- Resolusi & Format Citra: 40 × 40 piksel, Grayscale, *tightly cropped and aligned*.
- Status akses: Terbuka untuk riset akademik.
- Label Target: 4 kelas ras (`Caucasian`, `African`, `Asian`, `Indian`).
- Tujuan penggunaan: Pelatihan, validasi, dan pengujian model IDL-ERCFI.

---

## Metodologi Penelitian

### Gambaran Umum
Sistem IDL-ERCFI memproses citra wajah melalui lima tahapan berurutan:
1. Pra-pemrosesan citra (penyelarasan berbasis landmark 2D).
2. Ekstraksi representasi fitur menggunakan model *Xception*.
3. Reduksi dimensi fitur menggunakan *Principal Component Analysis* (PCA).
4. Klasifikasi multi-ras menggunakan *Kernel Extreme Learning Machine* (KELM).
5. Penyesuaian hyperparameter optimal KELM menggunakan *Glowworm Swarm Optimization* (GSO).

```
                  Citra Wajah Masukan (BUPT-GLOBALFACE)
                                    │
                                    ▼
       ┌───────────────────────────────────────────────────────────┐
       │ 1. Pra-pemrosesan & Penyelarasan Landmark 2D              │
       │    - Deteksi 68/67 landmark dlib                          │
       │    - Rotasi berbasis kemiringan mata, cropping (40×40)    │
       │    - Konversi Grayscale, Mean Centering, Normalisasi [0,1]│
       └────────────────────────────┬──────────────────────────────┘
                                    │
                                    ▼
       ┌───────────────────────────────────────────────────────────┐
       │ 2. Ekstraksi Fitur Mendalam: Jaringan Xception            │
       │    - Entry Flow → Middle Flow (×8) → Exit Flow            │
       │    - Global Average Pooling (GAP) → Vektor 2.048-d        │
       └────────────────────────────┬──────────────────────────────┘
                                    │
                                    ▼
       ┌───────────────────────────────────────────────────────────┐
       │ 3. Reduksi Dimensi Fitur: PCA                             │
       │    - Perhitungan Mean, Varians, dan Matriks Kovariansi    │
       │    - Mengatasi Curse of Dimensionality                    │
       └────────────────────────────┬──────────────────────────────┘
                                    │
                                    ▼
       ┌───────────────────────────────────────────────────────────┐
       │ 4. Klasifikasi: Kernel Extreme Learning Machine (KELM)    │
       │    - Pemetaan Kernel Non-Linear Mercer Ω_ELM = H * H^T    │
       │    - Solusi Analitik Least Squares Tanpa Backpropagation  │
       └────────────────────────────┬──────────────────────────────┘
                                    ▲
                                    │ Parameter Optimal (C, γ)
       ┌────────────────────────────┴──────────────────────────────┐
       │ 5. Optimasi Hyperparameter: Algoritma GSO                 │
       │    - Pembaruan Luciferin berbasis 10-Fold CV Fitness      │
       │    - Pergerakan Kunang-Kunang & Radius Keputusan Dinamis  │
       └────────────────────────────┬──────────────────────────────┘
                                    │
                                    ▼
            Prediksi Ras: [Caucasian / African / Asian / Indian]
```

### Arsitektur / Pendekatan
- **Penyelarasan Wajah (*Landmark Alignment*):**
  - Menggunakan pustaka `dlib` untuk mengekstrak 68 titik landmark wajah.
  - Menghitung sudut kemiringan garis horizontal antar-mata dan melakukan rotasi 2D terhadap titik tengah mata.
  - Memotong wajah dengan proporsi: posisi mata berada pada 32% lebar dan 38% tinggi dari batas atas, serta menyertakan area dagu untuk mengkompensasi rotasi *yaw* tinggi.
  - Citra diubah ke ukuran 40 × 40 piksel, diubah ke *grayscale*, dan dinormalisasi ke rentang [0, 1].
- **Ekstraktor Fitur Xception:**
  - Terdiri dari 3 bagian utama: *Entry Flow* (konvolusi standar + konvolusi separabel), *Middle Flow* (8 kali pengulangan blok konvolusi separabel 728 filter), dan *Exit Flow* (konvolusi separabel 1.536 dan 2.048 filter).
  - Menggunakan *Global Average Pooling* (GAP) pada lapisan akhir untuk menghasilkan vektor deskriptor kompak 2.048 dimensi per citra.
- **Reduksi Fitur PCA:**
  - Menghitung nilai mean $Q$, deviasi standar $SD$, dan matriks kovariansi $\text{Cov}(Q, R)$ untuk memproyeksikan fitur ke sub-ruang ortogonal berdimensi lebih rendah.
- **Kernel Extreme Learning Machine (KELM):**
  - Menggunakan formulasi kernel Mercer $\Omega_{\text{ELM}} = H H^T$ di mana $\Omega_{\text{ELM}(i, r)} = K(x_i, x_r)$.
  - Fungsi keputusan keluaran:
    $$f(x) = h(x) H^T \left( \frac{I}{C} + \Omega_{\text{ELM}} \right)^{-1} Y$$
  - Memungkinkan pemisahan kelas non-linear dengan kecepatan inferensi sangat tinggi tanpa proses *gradient descent*.
- **Optimasi Hyperparameter GSO:**
  - Mengoptimasi parameter KELM ($C$ dan parameter kernel) melalui populasi agen kunang-kunang (*glowworms*).
  - Setiap agen membawa kadar luciferin $l_i(t)$ yang diperbarui berdasarkan nilai *fitness*:
    $$\text{Fitness} = 1 - \text{CA}_{\text{validation}}$$
    $$\text{CA}_{\text{validation}} = 1 - \frac{1}{10} \sum_{i=1}^{10} \left( \frac{y_c}{y_c + y_f} \right) \times 100$$
  - Agen bergerak menuju tetangga dengan intensitas luciferin yang lebih tinggi dengan aturan probabilitas transisi $P_{ij}(t)$ dan radius keputusan adaptif $r_d^i(t)$.

---

## Detail Implementasi

### Konfigurasi Pelatihan & Optimasi
- Image Size / Input Resolution: 40 × 40 piksel (Grayscale)
- Feature Backbone: Xception Pretrained Model
- Dimensi Vektor Ekstraksi: 2.048 dimensi (sebelum PCA)
- Classifier: KELM dengan Kernel RBF/Non-linear
- Optimasi Parameter: Glowworm Swarm Optimization (GSO)
- Skema Validasi: 10-Fold Cross-Validation untuk evaluasi fitness GSO
- Total Sampel Latih: 400.000 citra | Validasi: 32.000 citra | Uji: 8.000 citra

### Lingkungan Implementasi
- Bahasa Pemrograman: Python 3.6.5
- Library: TensorFlow, Keras, dlib, OpenCV, Scikit-Learn, NumPy
- Eksperimen Pengujian: 5 kali pengujian independen (*Run-1 s.d. Run-5*) pada data uji (8.000 citra).

---

## Evaluation Metrics

### Metrik Klasifikasi Global & Per-Kelas
- **Accuracy (%):** Persentase prediksi benar terhadap seluruh sampel uji.
- **Precision (%):** $TP / (TP + FP)$ per kelas ras.
- **Recall (%):** $TP / (TP + FN)$ per kelas ras.
- **F1-Score (%):** Rata-rata harmonik Precision dan Recall.
- **ROC-AUC (%):** *Receiver Operating Characteristic — Area Under Curve* untuk mengevaluasi kemampuan diskriminasi model.
- **Confusion Matrix:** Matriks konfusi 4×4 pada data uji untuk mendeteksi kesalahan klasifikasi silang antar-ras.

---

## Hasil Penelitian

### Temuan Utama
1. **Performa Sangat Tinggi:** Model IDL-ERCFI menghasilkan performa konsisten pada seluruh 5 pengujian independen dengan rata-rata akurasi **98,97%**, Precision **97,95%**, Recall **97,94%**, dan F1-Score **97,94%** pada data uji BUPT-GLOBALFACE (8.000 citra).
2. **Nilai ROC-AUC Mendekati Sempurna:** Nilai ROC-AUC mencapai **99,84% (Run-1)**, **99,80% (Run-2)**, **99,90% (Run-3)**, **99,77% (Run-4)**, dan **99,86% (Run-5)**.
3. **Stabilitas Antar-Kelas:** Keempat kelas ras mencapai nilai F1-Score di atas 96,7%:
   - Kelas **Asian** meraih skor tertinggi (Akurasi ~99,35%–99,44%, Precision ~98,51%–98,90%, Recall ~98,60%–98,90%, F1 ~98,55%–98,87%).
   - Kelas **African** dan **Indian** meraih F1 rata-rata ~97,5%–98,5%.
   - Kelas **Caucasian** meraih F1 rata-rata ~96,8%–97,5%.
4. **Keunggulan Dibandingkan SOTA:** IDL-ERCFI mengungguli seluruh model pembanding, termasuk VGGFace-SVM (98,00%), R-Net (97,00%), MobileNet (96,64%), Inception-ResNet-v2 (96,36%), VGG-19 (96,06%), SeNet (95,89%), dan SGD-Softmax (95,00%).

---

## Score

### 1. Evaluasi Rinci IDL-ERCFI pada 5 Pengujian Independen (Exam Set: 8.000 Citra)

| Pengujian | Kelas Ras | Accuracy (%) | Precision (%) | Recall (%) | F1-Score (%) |
|:---------:|-----------|:------------:|:-------------:|:----------:|:------------:|
| **Run-1** | Caucasian | 98,41 | 97,85 | 95,75 | 96,79 |
| | African | 98,56 | 96,18 | 98,15 | 97,15 |
| | Asian | 99,28 | 98,50 | 98,60 | 98,55 |
| | Indian | 99,08 | 98,15 | 98,15 | 98,15 |
| | **Rata-rata Run-1** | **98,83** | **97,67** | **97,66** | **97,66** |
| **Run-2** | Caucasian | 98,70 | 98,37 | 96,40 | 97,37 |
| | African | 98,62 | 96,23 | 98,35 | 97,28 |
| | Asian | 99,44 | 98,90 | 98,85 | 98,87 |
| | Indian | 99,21 | 98,50 | 98,35 | 98,42 |
| | **Rata-rata Run-2** | **98,99** | **98,00** | **97,99** | **97,99** |
| **Run-3** | **Rata-rata Run-3** | **98,98** | **97,98** | **97,96** | **97,96** |
| **Run-4** | **Rata-rata Run-4** | **98,99** | **97,98** | **97,98** | **97,97** |
| **Run-5** | **Rata-rata Run-5** | **99,05** | **98,11** | **98,10** | **98,10** |

---

### 2. Perbandingan Performa dengan Metode State-of-the-Art

| Metode | Accuracy (%) | Precision (%) | Recall (%) | F1-Score (%) |
|--------|:------------:|:-------------:|:----------:|:------------:|
| EOR-Adam | 76,00 | 76,00 | 76,00 | 76,00 |
| Adam-Softmax | 93,00 | 93,00 | 93,00 | 93,00 |
| SGD-Softmax | 95,00 | 95,00 | 95,00 | 95,00 |
| SeNet | 95,89 | 95,90 | 95,89 | 95,89 |
| VGG-19 | 96,06 | 96,06 | 96,06 | 96,06 |
| Inception-ResNet-v2 | 96,36 | 96,36 | 96,36 | 96,36 |
| MobileNet | 96,64 | 96,64 | 96,64 | 96,64 |
| R-Net | 97,00 | 97,00 | 97,00 | 97,00 |
| VGGFace-SVM | 98,00 | 98,00 | 97,00 | 98,00 |
| **IDL-ERCFI (Usulan)** | **98,97** | **97,95** | **97,94** | **97,94** |

---

## Kelebihan Penelitian

1. **Pipeline Modular yang Komprehensif:** Mengintegrasikan normalisasi geometri (landmark alignment), ekstraksi fitur mendalam (Xception), reduksi dimensi (PCA), dan pengklasifikasi cepat non-iteratif (KELM).
2. **Kecepatan Inferensi dan Pelatihan KELM:** Penggunaan KELM menghindari proses *backpropagation* yang lambat dan rentan *local minima*, menghasilkan proses pembelajaran analitik yang sangat efisien pada dataset berskala ratusan ribu citra.
3. **Optimasi Hyperparameter Otomatis:** Algoritma GSO mengotomatisasi pencarian parameter KELM secara cerdas sehingga terbebas dari *trial-and-error* manual.
4. **Pengujian Skala Besar:** Menggunakan subset 440.000 citra dari dataset BUPT-GLOBALFACE yang berimbang dan teruji secara statistik melalui 5 *runs* pengujian mandiri.

---

## Keterbatasan Penelitian

1. **Resolusi Masukan Sangat Kecil (40 × 40 piksel):** Penurunan resolusi ke 40 × 40 piksel dan konversi ke *grayscale* menghilangkan informasi tekstur mikro kulit dan spektrum warna wajah yang krusial untuk membedakan etnisitas yang lebih spesifik (*fine-grained*).
2. **Keterbatasan Kategori Etnis (Hanya 4 Ras Makro):** Model hanya mengevaluasi 4 ras makro (*Caucasian, African, Asian, Indian*) dan tidak mencakup kelompok interseksional gender atau etnis minoritas (seperti Latin, Timur Tengah, Asia Tenggara).
3. **Kompleksitas Komputasi GSO:** Meskipun KELM sangat cepat, proses iterasi agen GSO dengan evaluasi fitness berbasis 10-fold CV membutuhkan waktu komputasi metaheuristik yang cukup intensif selama fase optimasi.

---

## Future Work (Saran Penelitian Selanjutnya)

1. Mengembangkan arsitektur deep learning yang lebih kompleks dengan pengoptimal hyperparameter terintegrasi secara end-to-end.
2. Memperluas klasifikasi ke kelompok etnis yang lebih halus (*fine-grained ethnicities*) dan skenario multi-atribut demografis (gender dan usia).
3. Mengevaluasi ketahanan model terhadap citra beresolusi tinggi dengan informasi warna penuh (RGB) untuk menangkap perbedaan pigmen kulit alami.

---

## Catatan Penting untuk Riset Kita

### Insight yang Dapat Diadopsi
- **Pemisahan Ekstraktor Fitur dan Classifier Optimal:** Paper ini membuktikan bahwa mengekstraksi fitur embedding laten dari model pre-trained yang kuat lalu mengklasifikasikannya menggunakan *classifier* berbasis optimasi ruang margin/kernel (seperti KELM/SVM) menghasilkan akurasi yang jauh lebih tinggi (98,97%) dibandingkan melatih classifier *SoftMax end-to-end* (93%–95%).
- **Pentingnya Optimasi Hyperparameter Sistematis:** Penyetelan parameter kernel dan regularisasi yang tepat merupakan faktor kunci dalam memaksimalkan bidang pisah (*decision hyperplane*).

### Relevansi dengan Kerangka Kerja Multi-Domain ViT (Identity + Emotion + Age) + SVM
- Pada riset Sunitha et al., mereka hanya menggunakan satu arsitektur CNN tunggal (*Xception*) untuk fitur spasial monolitik ras.
- Pada penelitian kita, kita mengembangkan pendekatan yang jauh lebih holistik: memanfaatkan **3 Vision Transformers (ViT-Base)** terpisah yang mencakup tiga pilar representasi wajah: **Identitas Biometrik** (`skutaada/VIT-VGGFace`), **Dinamika Afek/Emosi** (`dima806/facial_emotions`), dan **Penuaan Biologis/Usia** (`dima806/facial_age`).
- Vektor gabungan 2.304 dimensi tersebut kemudian dioptimasi menggunakan **Support Vector Classifier (SVC)** melalui *GridSearchCV* 288 kombinasi parameter pada dataset DemogPairs (10.800 citra seimbang sempurna), mencapai akurasi **93,70%** pada 6 kelas interseksional 3 Ras × 2 Gender.

### Hal yang Membedakan Paper Ini dari Penelitian Kita
| Aspek | Sunitha et al. (2022) | Penelitian Kita |
|-------|-----------------------|-----------------|
| **Tugas Target** | Klasifikasi Ras Makro 4-Kelas | Klasifikasi Interseksional Terpadu 6-Kelas (3 Ras × 2 Gender) |
| **Ekstraktor Fitur** | Single-backbone CNN (Xception) | 3 Pre-trained Vision Transformers (ViT-Face, ViT-Emotion, ViT-Age) |
| **Domain Representasi** | Fitur Spasial Tunggal Wajah (40×40 Grayscale) | Multi-Domain Latent Embeddings (224×224 RGB: Identitas, Emosi, Usia) |
| **Dimensi Fitur** | Vektor Xception (2.048-d) direduksi PCA | Fusi Vektor Concatenation (2.304-d murni tanpa PCA) |
| **Classifier & Optimasi** | KELM + Glowworm Swarm Optimization (GSO) | Support Vector Classifier (SVC) + GridSearchCV (288 kombinasi) |
| **Dataset** | BUPT-GLOBALFACE (400k train, 8k test) | DemogPairs (8.640 train, 2.160 test seimbang sempurna) |
| **Target Evaluasi** | Ras Tunggal (Caucasian, African, Asian, Indian) | Pasangan Demografis Interseksional (Asian/Black/White × Female/Male) |
