# Automatic Ethnicity Classification from Middle Part of the Face Using Convolutional Neural Networks

## Informasi Umum
- Judul: Automatic Ethnicity Classification from Middle Part of the Face Using Convolutional Neural Networks
- Penulis: David Belcar (Evolva d.o.o., Varaždin, Croatia), Petra Grd (Faculty of Organization and Informatics, University of Zagreb, Croatia), Igor Tomičić (Faculty of Organization and Informatics, University of Zagreb, Croatia)
- Tahun: 2022
- Journal / Conference: Informatics (MDPI)
- Publisher: MDPI
- ISSN / ISBN: 2227-9709
- Volume / Nomor / Halaman: Volume 9, Issue 1, Article 18, hlm. 1–25
- DOI: 10.3390/informatics9010018
- URL: https://www.mdpi.com/2227-9709/9/1/18
- Keywords: ethnicity classification, race classification, CNN, face biometric, FairFace, UTKFace
- Riwayat Artikel:
  - Received: 22 January 2022
  - Revised: 22 February 2022
  - Accepted: 22 February 2022
  - Published: 25 February 2022
- Lisensi: Creative Commons Attribution (CC BY 4.0) — Open Access
- Jenis Paper: Eksperimen / Applied Research

---

## Poin-Poin yang Dibahas dalam Introduction
1. Pengenalan wajah otomatis (*face recognition*) semakin banyak diterapkan pada keamanan, biometrik, forensik, pemasaran, dan interaksi manusia-komputer, namun atribut biometrik lunak (*soft biometrics*) seperti ras, gender, usia, dan emosi juga memegang peranan krusial.
2. Dari seluruh atribut demografis wajah, etnisitas/ras merupakan atribut yang paling sedikit dipelajari (*least studied*) dan memiliki kompleksitas tinggi akibat ketiadaan konsensus terminologi, tumpang tindih fenotipe, dan bias pelabelan manusia (*Other-Race Effect / ORE*).
3. Mayoritas literatur menunjukkan bahwa informasi diskriminatif rasial paling padat terkonsentrasi pada bagian tengah wajah (*middle part of the face*), khususnya area mata dan hidung.
4. Pemrosesan citra seluruh wajah membutuhkan sumber daya komputasi dan memori yang besar serta rentan terhadap noise latar belakang, gaya rambut, dan aksesoris.

---

## Problem Statement (Apa masalah yang ingin diselesaikan?)

Bagaimana membangun metode klasifikasi etnisitas otomatis yang akurat sekaligus hemat sumber daya komputasi dan memori dengan hanya memanfaatkan area tengah wajah (*middle part of the face*), serta mengevaluasi secara empiris apakah penambahan anotasi titik landmark wajah (*facial landmarks*) dapat meningkatkan performa klasifikasi pada arsitektur *Convolutional Neural Networks* (CNN).

---

## Tujuan Penelitian

1. Menyajikan tinjauan komprehensif perkembangan terkini metode klasifikasi etnisitas berbasis CNN.
2. Mengembangkan arsitektur CNN kustom yang dioptimasi untuk memproses masukan citra bagian tengah wajah beresolusi kompak (146 × 86 piksel).
3. Menguji pengaruh penambahan anotasi 68 *facial landmarks* secara visual pada citra terhadap akurasi dan konvergensi CNN.
4. Mengevaluasi efektivitas pendekatan yang diusulkan pada skenario 5 kelas (UTKFace) dan 7 kelas (FairFace) serta membandingkannya dengan metode *state-of-the-art*.

---

## Research Question

1. Apakah pemangkasan citra hanya pada bagian tengah wajah (area mata dan hidung) mampu menghasilkan akurasi klasifikasi etnisitas yang setara atau lebih baik dibandingkan penggunaan seluruh area wajah?
2. Apakah penggambaran titik *facial landmarks* secara eksplisit pada citra masukan memberikan kontribusi positif terhadap akurasi model CNN?
3. Bagaimana dampak pertambahan jumlah kelas etnis (dari 5 kelas ke 7 kelas) terhadap performa klasifikasi dan stabilitas model CNN?

---

## Kontribusi Utama

1. **Arsitektur CNN Efisien:** Merancang model CNN kustom (Model_18) berbasis 4 blok VGG (8 convolutional layers, 2,05 juta parameter) yang beroperasi pada citra bagian tengah wajah (146 × 86 piksel).
2. **Efisiensi Komputasi & Memori Signifikan:** Mengurangi ukuran penyimpanan array dataset hingga lebih dari 69% (dari 4,36 GB menjadi 1,34 GB pada UTKFace) dan mempercepat waktu pelatihan per epoch hingga 10 kali lipat (dari 250 detik menjadi 24 detik).
3. **Analisis Empiris Facial Landmarks:** Membuktikan secara eksperimental bahwa penambahan visual *facial landmarks* tidak meningkatkan performa klasifikasi CNN, melainkan hanya menambah beban komputasi pra-pemrosesan.
4. **Validasi Multi-Dataset:** Mencapai akurasi 80,34% pada UTKFace (5 kelas) dan 61,74% pada FairFace (7 kelas) yang kompetitif terhadap metode *state-of-the-art* yang menggunakan citra wajah penuh.

---

## Dataset

### Dataset 1: UTKFace Filtered
- Nama dataset: UTKFace Filtered (turunan dari UTKFace)
- Sumber dataset: Zhang et al. (2017)
- URL: https://susanqq.github.io/UTKFace/
- Jumlah data: 18.246 citra wajah (disaring dari 23.807 citra asli, reduksi ~23% akibat eliminasi citra non-frontal/gagal deteksi landmark).
- Komposisi Demografis:
  - Ras / Etnis: White (41% / 7.513), Black (22% / 4.018), Asian (13% / 2.262), Indian (18% / 3.286), Other (6% / 1.167).
  - Gender: Male (53,7% / 9.793), Female (46,3% / 8.453).
  - Usia: Rentang 1 hingga 116 tahun.
- Keseimbangan data: Cukup bervariasi dengan dominasi White (41%).
- Resolusi & Format Citra: 146 × 86 piksel, Grayscale / RGB, cropped middle face.
- Pembagian data: Holdout method — 50% Train (9.123 citra), 25% Validation (4.559 citra), 25% Test (4.564 citra).
- Status akses: Open Access untuk riset non-komersial.
- Label Target: 5 kelas etnis (`White`, `Black`, `Asian`, `Indian`, `Other`).
- Tujuan penggunaan: Pelatihan, validasi, dan pengujian model klasifikasi 5-kelas.

### Dataset 2: FairFace Filtered
- Nama dataset: FairFace Filtered (turunan dari FairFace)
- Sumber dataset: Kärkkäinen & Joo (2021)
- URL: https://github.com/dchen236/FairFace
- Jumlah data: 55.384 citra wajah (disaring dari 97.698 citra asli, reduksi ~43,3% akibat eliminasi citra bersudut ekstrem, oklusi, dan non-frontal).
- Komposisi Demografis:
  - Ras / Etnis: White (19% / 10.692), Black (12% / 6.453), Latin (16% / 9.186), Indian (15% / 8.205), Middle Eastern (11% / 5.920), East Asian (14% / 7.770), Southeast Asian (13% / 7.159).
  - Gender: Male (49,4% / 27.353), Female (50,6% / 28.031) — seimbang sempurna.
  - Usia: Rentang 1 hingga 70 tahun.
- Keseimbangan data: Sangat seimbang antar-kelompok etnis dan gender.
- Resolusi & Format Citra: 146 × 86 piksel, Grayscale / RGB, cropped middle face.
- Pembagian data: Holdout method — 50% Train (27.692 citra), 25% Validation (13.846 citra), 25% Test (13.846 citra).
- Status akses: Open Access untuk riset non-komersial.
- Label Target: 7 kelas etnis (`White`, `Black`, `Latin`, `Indian`, `Middle Eastern`, `East Asian`, `Southeast Asian`).
- Tujuan penggunaan: Pelatihan, validasi, dan pengujian model klasifikasi 7-kelas.

---

## Metodologi Penelitian

### Gambaran Umum
Penelitian ini mengusulkan pipeline klasifikasi etnisitas otomatis berbasis CNN kustom yang memproses area tengah wajah. Pipeline terdiri dari tahapan pra-pemrosesan citra, ekstraksi landmark, pemangkasan area fokus, augmentasi data, pelatihan CNN berstruktur blok VGG dengan regularisasi Batch Normalization dan Dropout, serta evaluasi komparatif antara model dengan dan tanpa anotasi visual landmark.

### Arsitektur / Pendekatan
- Preprocessing & Face Cropping/Alignment:
  1. Deteksi posisi mata dan *face centering*.
  2. *Resizing* citra ke ukuran 200 × 200 piksel.
  3. Konversi ke *grayscale*.
  4. Deteksi 68 *facial landmarks* menggunakan Histogram of Oriented Gradients (HOG) dan Linear Support Vector Machine (SVM) melalui pustaka `dlib`.
  5. Pemangkasan citra (*image cropping*) hanya pada area mata dan hidung menghasilkan format 146 × 86 piksel.
  6. (Opsional untuk varian landmark) Menggambar titik-titik landmark (*plotting landmarks*) pada citra.
  7. Normalisasi piksel ke rentang [0, 1] dengan pembagian 255.
  8. Augmentasi data: peregangan horizontal/vertikal hingga 10% dan pencerminan horizontal (*horizontal flip*). Rotasi acak tidak digunakan karena menurunkan performa.
- Feature Extractor & Backbone Model: CNN kustom (Model_18) yang terdiri dari 4 VGG Blocks (total 8 Convolutional Layers dengan kernel 4×4 pada blok pertama, 3×3 pada blok kedua, dan 2×2 pada blok ketiga dan keempat).
- Domain Fitur yang Diekstrak: Fitur spasial lokal dan morfologi bagian tengah wajah (mata, pangkal hidung, cuping hidung).
- Representasi Output: Flattening layer $\rightarrow$ Fully Connected Layers (Dense 128 $\rightarrow$ Dense 64 $\rightarrow$ Output Head).
- Dimensi Vektor Fitur: 128-d pada FC1, 64-d pada FC2.
- Mekanisme Penggabungan Fitur (*Feature Fusion*): *Single-Domain spatial CNN representation* (tanpa fusi multi-modalitas).
- Regularisasi: Kombinasi *Batch Normalization* pada seluruh layer konvolusi/FC dan *Dropout* bertahap (0.4 pada blok VGG 1–3, 0.45 pada blok VGG 4, dan 0.5 pada layer FC).
- Classifier / Prediction Head: *Dense SoftMax Layer* (5 neuron untuk UTKFace, 7 neuron untuk FairFace).
- Optimasi Hyperparameter: Eksperimen manual terhadap 20 kandidat arsitektur CNN (membandingkan penempatan BatchNorm, Dropout, jumlah filter, dan ukuran kernel).
- Loss Function: *Categorical Cross-Entropy Loss*.
- Pendekatan Keadilan & Mitigasi Bias: Pemanfaatan dataset terfilter yang menjaga proporsi gender dan etnisitas serta evaluasi rinci per-kelompok etnis menggunakan *confusion matrix*.

### Tahapan Metodologi
1. **Pengumpulan & Audit Dataset:** Mengunduh dan menyeleksi dataset UTKFace dan FairFace.
2. **Pra-pemrosesan Citra:** Melakukan deteksi mata, *centering*, konversi *grayscale*, ekstraksi 68 landmark HOG+SVM, dan pemotongan area tengah wajah (146 × 86 piksel).
3. **Penyusunan Dataset Filtered:** Membentuk 4 sub-dataset: UTKFace Filtered (dengan & tanpa landmark) dan FairFace Filtered (dengan & tanpa landmark).
4. **Desain & Eksplorasi Arsitektur CNN:** Membangun dan menguji 20 variasi arsitektur CNN untuk memilih model dengan akurasi validasi terbaik (terpilih Model_18).
5. **Pelatihan Model (Training & Validation):** Melatih 4 konfigurasi model:
   - `Model_F1`: UTKFace tanpa landmark (5 kelas).
   - `Model_F2`: FairFace tanpa landmark (7 kelas).
   - `Model_F3`: UTKFace dengan landmark (5 kelas).
   - `Model_F4`: FairFace dengan landmark (7 kelas).
6. **Pengujian & Evaluasi (Testing):** Menguji model pada data uji independen (25% holdout) menggunakan metrik *Accuracy*, *Precision*, *Recall*, *Weighted F1-Score*, dan analisis *Confusion Matrix*.
7. **Analisis Efisiensi & Benchmarking:** Mengukur efisiensi memori RAM, ukuran file, waktu komputasi, dan membandingkan hasil dengan studi terdahulu.

---

## Detail Implementasi

### Konfigurasi Pelatihan & Optimasi
- Image Size / Input Resolution: 146 × 86 piksel
- Batch Size: 64
- Epoch / Iterasi: 150 epoch (UTKFace), ~120–130 epoch (FairFace)
- Learning Rate: 0,001 (konstan)
- Optimizer: Adam Optimizer
- Loss Function: SoftMax Categorical Cross-Entropy
- Total Layer: 31 layers
- Learnable Parameters: 2.050.000 parameter
- Skema Validasi: Holdout Validation (50% Train, 25% Validation, 25% Test)
- Random Seed: Default split

### Lingkungan Implementasi
- Hardware:
  - Processor: Intel Core i7-7700
  - GPU: NVIDIA GeForce GTX 1060 6 GB
  - RAM: 16 GB DDR4 2400 MHz
- Framework / Library: Python, Keras/TensorFlow, dlib, OpenCV, Scikit-Learn
- Sistem Operasi: Linux / Windows
- Waktu Pelatihan:
  - UTKFace Filtered: ~2 jam (24 detik per epoch)
  - FairFace Filtered: ~9 jam

---

## Evaluation Metrics

### Metrik Klasifikasi Global
- **Accuracy:** Proporsi total prediksi benar terhadap seluruh sampel uji.
- **Weighted F1-Score:** Rata-rata harmonik Precision dan Recall yang dibobotkan berdasarkan proporsi jumlah sampel (*support*) masing-masing kelas.

### Metrik Per-Kelas & Keadilan Demografis (*Demographic Fairness*)
- **Precision:** $TP / (TP + FP)$ untuk setiap kelas etnis.
- **Recall:** $TP / (TP + FN)$ untuk setiap kelas etnis.
- **Class F1-Score:** $2 \times (\text{Precision} \times \text{Recall}) / (\text{Precision} + \text{Recall})$.
- **Confusion Matrix:** Matriks konfusi multi-kelas (5×5 untuk UTKFace, 7×7 untuk FairFace) untuk mendeteksi pola kesalahan klasifikasi silang antar-etnis (*cross-ethnicity confusion*).

---

## Hasil Penelitian

### Temuan Utama
1. **Keunggulan Citra Bagian Tengah Wajah:** Menggunakan hanya area tengah wajah (146 × 86 piksel) menghasilkan akurasi **80,34%** pada UTKFace (5 kelas), mengungguli model terdahulu berbasis wajah penuh (Hamdi & Moussaoui, 2020: 78,88%), membuktikan bahwa mata dan hidung memuat representasi rasial paling esensial.
2. **Dampak Anotasi Facial Landmarks:** Penambahan visualisasi landmark pada citra **tidak memberikan peningkatan performa yang signifikan**, bahkan sedikit menurunkan akurasi (UTKFace: 80,34% tanpa landmark vs 79,97% dengan landmark; FairFace: 61,74% tanpa landmark vs 60,52% dengan landmark). Hal ini menunjukkan filter konvolusi CNN sudah mampu mengekstrak fitur spasial secara implisit tanpa memerlukan anotasi eksplisit.
3. **Kompleksitas Jumlah Kelas:** Menambah jumlah kelas dari 5 kelas (UTKFace) menjadi 7 kelas (FairFace) menurunkan akurasi dari 80,34% ke 61,74%, yang disebabkan oleh tingginya kesamaan visual dan tumpang tindih fenotipe antara kelompok etnis yang berdekatan geografis (misal: *East Asian* vs *Southeast Asian*, *Latin* vs *White* / *Middle Eastern*).
4. **Efisiensi Komputasi Ekstrem:** Memotong citra ke bagian tengah wajah memangkas memori RAM dataset dari 4,36 GB menjadi 1,34 GB, memungkinkan seluruh data latih dimuat langsung ke memori komputer dan mempercepat waktu latih per epoch dari 250 detik menjadi 24 detik (percepatan 10×).

### Analisis Penulis
- Penurunan performa pada kelas minoritas seperti *Other* (Recall 18,15%, F1 0,2494) pada UTKFace disebabkan oleh heterogenitas visual yang sangat tinggi di dalam kelas tersebut (mencakup individu Latin, Timur Tengah, dan campuran).
- Pada FairFace, kelas *Latin* dan *Middle Eastern* mengalami tingkat konfusi tertinggi terhadap kelas *White*, mengindikasikan bahwa fitur visual berbasis CNN konvensional kesulitan memisahkan sub-populasi dengan akar fenotipe Kaukasoid/Hispanik tanpa informasi kontekstual tambahan.

### Perbandingan dengan Baseline / SOTA
- Pada dataset UTKFace (5 kelas lengkap): Model usulan (80,34%) lebih unggul dibanding Hamdi & Moussaoui (2020) yang mencapai 78,88% menggunakan VGG-16 pada citra wajah penuh.
- Beberapa penelitian lain melaporkan akurasi >90% pada UTKFace (misal: Das et al., 2018: 90,1%), namun mereka mengeliminasi kelas *Other* (hanya 4 kelas) sehingga tidak dapat dibandingkan secara langsung (*apples-to-apples*).

---

## Score

### 1. Hasil Pengujian pada UTKFace Filtered (5 Kelas)

| Model | Anotasi Landmark | Accuracy | Weighted F1-Score | Waktu Training / Epoch |
|-------|:----------------:|:--------:|:-----------------:|:----------------------:|
| **Model_F1** | **Tanpa Landmark** | **80,34%** | **0,7940** | **24 s** |
| Model_F3 | Dengan Landmark | 79,97% | 0,7832 | 24 s |

#### Rincian Per-Kelas Model_F1 (Tanpa Landmark — 5 Kelas):
| Kelompok Etnis | Support (Data Uji) | Precision | Recall | F1-Score |
|----------------|:------------------:|:---------:|:------:|:--------:|
| **White** | 1.879 | 0,8349 | 0,8829 | 0,8583 |
| **Black** | 1.004 | 0,8333 | 0,8317 | 0,8325 |
| **Asian** | 566 | **0,9094** | 0,8693 | **0,8889** |
| **Indian** | 822 | 0,6967 | 0,7628 | 0,7282 |
| **Other** | 292 | 0,3985 | 0,1815 | 0,2494 |

---

### 2. Hasil Pengujian pada FairFace Filtered (7 Kelas)

| Model | Anotasi Landmark | Accuracy | Weighted F1-Score | Waktu Training Total |
|-------|:----------------:|:--------:|:-----------------:|:--------------------:|
| **Model_F2** | **Tanpa Landmark** | **61,74%** | **0,6177** | **~9 jam** |
| Model_F4 | Dengan Landmark | 60,52% | 0,6028 | ~9 jam |

#### Rincian Per-Kelas Model_F2 (Tanpa Landmark — 7 Kelas):
| Kelompok Etnis | Support (Data Uji) | Precision | Recall | F1-Score |
|----------------|:------------------:|:---------:|:------:|:--------:|
| **White** | 2.672 | 0,6877 | 0,6602 | 0,6737 |
| **Black** | 1.613 | **0,8122** | 0,6863 | **0,7440** |
| **Latin** | 2.297 | 0,4701 | 0,4436 | 0,4564 |
| **Indian** | 2.051 | 0,5556 | **0,7679** | 0,6447 |
| **Middle Eastern** | 1.480 | 0,4996 | 0,4811 | 0,4902 |
| **East Asian** | 1.943 | 0,7540 | 0,6752 | 0,7125 |
| **Southeast Asian** | 1.790 | 0,6057 | 0,5922 | 0,5989 |

---

## Kelebihan Penelitian

1. **Efisiensi Komputasi dan Memori:** Pemotongan ke area tengah wajah (146 × 86) mengurangi ukuran memori hingga 69% dan mempercepat proses training hingga 10× lipat tanpa menurunkan akurasi.
2. **Desain Eksperimen Sistematis:** Menguji 20 variasi arsitektur CNN untuk menemukan konfigurasi regularisasi optimal antara *Batch Normalization* dan *Dropout*.
3. **Eksplorasi Hipotesis Landmark:** Memberikan bukti empiris yang jelas mengenai inefisiensi penggambaran *facial landmarks* eksplisit pada CNN dalam tugas klasifikasi etnisitas.
4. **Transparansi Hasil:** Menyajikan matriks konfusi lengkap dan metrik per-kelas (*Precision*, *Recall*, *F1-score*) yang mendalam pada dua benchmark publik berskala besar.

---

## Keterbatasan Penelitian

1. **Tingkat Reduksi Data Tinggi pada Tahap Filtering:** Sebanyak 23% citra UTKFace dan 43,3% citra FairFace terbuang karena kegagalan deteksi wajah/landmark pada pose non-frontal atau beresolusi rendah.
2. **Akurasi 7 Kelas yang Masih Rendah:** Akurasi pada FairFace hanya mencapai 61,74%, menunjukkan keterbatasan arsitektur CNN konvensional dari goresan (*from scratch*) dalam memisahkan kelas-kelas etnis yang berdekatan fenotipenya.
3. **Tidak Menggunakan Arsitektur Pre-trained Modern:** Model dilatih *from scratch* dan tidak memanfaatkan *transfer learning* dari model representasi mutakhir seperti Vision Transformer (ViT) atau model biometrik skala besar.
4. **Performa Sangat Rendah pada Kelas Campuran/Minoritas:** Kelas *Other* pada UTKFace dan *Latin* / *Middle Eastern* pada FairFace memiliki nilai F1 < 0,50 akibat tingginya tingkat konfusi dengan kelas *White*.

---

## Future Work (Saran Penelitian Selanjutnya)

1. Menerapkan *Transfer Learning* dari model-model *pre-trained* pengenalan wajah terbukti tangguh (seperti VGGFace2 atau Vision Transformers) sebagai dasar ekstraksi fitur.
2. Menggabungkan beberapa model neural network (*multi-network / feature fusion*) untuk menangkap atribut pelengkap di luar area tengah wajah.
3. Membangun dataset latih yang lebih seimbang yang merepresentasikan populasi dunia secara proporsional.
4. Mengembangkan strategi penanganan citra non-frontal agar tidak perlu membuang banyak citra pada tahap pra-pemrosesan.

---

## Catatan Penting untuk Riset Kita

### Insight yang Dapat Diadopsi
- **Area Mata & Hidung sebagai Wilayah Kunci:** Penelitian ini membuktikan bahwa region tengah wajah (*ocular and nasal regions*) merupakan kontributor informasi rasial terbesar. Hal ini sejalan dengan representasi lokal yang ditangkap oleh lapisan atensi pada Vision Transformer.
- **Inefisiensi Landmark Manual pada CNN:** Menambahkan titik landmark visual pada piksel citra terbukti sia-sia karena membebani pra-pemrosesan tanpa menambah akurasi. Ini memperkuat keputusan riset kita untuk menggunakan representasi embedding laten berdimensi tinggi dari ViT daripada anotasi landmark piksel.

### Relevansi dengan Kerangka Kerja Multi-Domain ViT (Identity + Emotion + Age) + SVM
- **Kelemahan CNN Single-Domain vs Keunggulan Multi-Domain ViT:** Model CNN tunggal pada paper ini hanya meraih akurasi 80,34% (5 kelas) dan 61,74% (7 kelas). Sebaliknya, pada penelitian kita, penggabungan representasi laten multi-domain (**ViT-Face + ViT-Emotion + ViT-Age** sebesar 2.304 dimensi) dipadukan dengan optimasi SVM berhasil meraih **93,70% akurasi** pada 6 kelas interseksional ras dan gender DemogPairs.
- **Penanganan Bias Demografis:** Pada penelitian Belcar et al., disparitas antar-kelas sangat timpang (F1 kelas Asian 0,88 vs Other 0,24). Pada riset kita, fusi multi-domain ViT menghasilkan performa yang sangat adil dan konsisten lintas kelompok demografis (F1 seluruh kelas berada di rentang 0,9174 hingga 0,9614).

### Hal yang Membedakan Paper Ini dari Penelitian Kita
| Aspek | Belcar et al. (2022) | Penelitian Kita |
|-------|----------------------|-----------------|
| **Fokus Tugas** | Klasifikasi etnisitas tunggal (5 & 7 kelas) | Klasifikasi interseksional terpadu (3 Ras × 2 Gender = 6 kelas) |
| **Masukan Citra** | Cropped middle face (146 × 86 piksel) | Full facial image terstandarisasi (224 × 224 piksel) |
| **Arsitektur Ekstraktor** | CNN 8-layer kustom (*train from scratch*) | 3 Pre-trained Vision Transformers (ViT-Face, ViT-Emotion, ViT-Age) |
| **Representasi Fitur** | Single-domain spatial features (128-d) | Multi-Domain Latent Feature Fusion (2.304-d) |
| **Classifier** | SoftMax categorical head (end-to-end) | Support Vector Classifier (SVC) dengan GridSearchCV (288 kombinasi) |
| **Dataset** | UTKFace & FairFace | DemogPairs (10.800 citra seimbang sempurna) |
| **Akurasi Terbaik** | 80,34% (5 kelas) / 61,74% (7 kelas) | **93,70%** (6 kelas interseksional) |

### Catatan Tambahan
Paper ini dapat dijadikan referensi kuat dalam bab *Related Works* dan *Background* untuk menjustifikasi:
1. Mengapa fitur wajah berbasis CNN konvensional belum memadai untuk klasifikasi multi-ras yang kompleks (>5 kelas).
2. Mengapa pendekatan representasi multi-domain *Vision Transformer* (menyatukan identitas, emosi, dan usia) menjadi solusi yang jauh lebih unggul dan komprehensif.
