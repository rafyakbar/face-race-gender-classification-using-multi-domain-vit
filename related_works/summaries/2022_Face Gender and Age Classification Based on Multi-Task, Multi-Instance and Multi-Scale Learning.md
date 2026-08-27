# Face Gender and Age Classification Based on Multi-Task, Multi-Instance and Multi-Scale Learning

## Informasi Umum
- Judul: Face Gender and Age Classification Based on Multi-Task, Multi-Instance and Multi-Scale Learning
- Penulis: Haibin Liao (Wuhan Textile University & Jiangxi Smart City Industrial Technology Research Institute), Li Yuan (Wuhan Textile University), Mou Wu (Hubei University of Science and Technology), Liangji Zhong (Hubei University of Science and Technology), Guonian Jin (Hubei University of Science and Technology), Neal Xiong (Sul Ross State University, USA)
- Tahun: 2022
- Journal / Conference: Applied Sciences (MDPI)
- Publisher: MDPI
- ISSN / ISBN: 2076-3417
- Volume / Nomor / Halaman: Volume 12, Issue 23, Article 12432, hlm. 1–14
- DOI: 10.3390/app122312432
- URL: https://www.mdpi.com/2076-3417/12/23/12432
- Keywords: facial attribute recognition, feature extraction, deep learning, random forest
- Riwayat Artikel:
  - Received: 28 October 2022
  - Revised: 29 November 2022
  - Accepted: 29 November 2022
  - Published: 5 December 2022
- Lisensi: Creative Commons Attribution (CC BY 4.0) — Open Access
- Jenis Paper: Eksperimen / Applied Research

---

## Poin-Poin yang Dibahas dalam Introduction
1. Estimasi gender dan kelompok usia dari citra wajah merupakan atribut biometrik lunak (*soft biometrics*) fundamental yang esensial dalam berbagai aplikasi nyata (keamanan, interaksi manusia-komputer, periklanan cerdas, dan verifikasi usia).
2. Klasifikasi otomatis gender dan usia pada citra *in-the-wild* menghadapi tantangan berat akibat variasi intra-subjek (resolusi rendah, perubahan pencahayaan, variasi pose, oklusi) serta variasi inter-subjek antar-individu.
3. Metode pembelajaran mendalam konvensional umumnya memprediksi gender dan usia secara terisolasi (*single-task*) serta mengandalkan lapisan *Fully Connected* (FC) berbasis *back-propagation* yang rentan terjebak pada *local minima* dan mengalami *overfitting*.
4. Pria dan wanita memiliki pola morfologi penuaan biologis yang berbeda (*gender-dependent aging models*), namun ketergantungan intrinsik antara gender dan usia ini jarang dimanfaatkan secara efektif dalam kerangka kerja terpadu.

---

## Problem Statement (Apa masalah yang ingin diselesaikan?)

Bagaimana mengatasi variasi intra-subjek yang parah (iluminasi, oklusi, resolusi rendah) dan variasi inter-subjek pada citra wajah *in-the-wild*, serta memanfaatkan ketergantungan saling mempengaruhi antara gender dan penuaan wajah dalam arsitektur pembelajaran multi-task yang efisien dan tangguh terhadap *overfitting*.

---

## Tujuan Penelitian

1. Merancang kerangka kerja hibrida pembelajaran multi-task berbasis *Multi-Instance Multi-Scale Learning* (MML) yang dipadukan dengan *Deep Random Forest* (DRF).
2. Mengekstrak representasi fitur wajah yang tangguh terhadap distorsi lokal dengan memilih 9 *facial instances* berbasis struktur anatomi wajah dan menggabungkannya melalui *Multi-Instance Fusion* (MIF) serta *Compact Pyramid Refinement* (CPR).
3. Mengembangkan model *Gender-Conditional Random Forest* yang memanfaatkan hasil estimasi gender sebagai probabilitas bersyarat untuk memandu pengelompokan usia wajah secara akurat.
4. Mengevaluasi performa model pada dataset benchmark MORPH-II dan Adience serta membandingkannya dengan metode *state-of-the-art*.

---

## Research Question

1. Bagaimana merancang mekanisme ekstraksi fitur spasial multi-instance dan multi-skala agar mampu mereduksi dampak distorsi lokal (oklusi, pencahayaan, pose) pada citra wajah?
2. Apakah perumusan estimasi usia berbasis probabilitas bersyarat keselarasan gender (*gender-aligned conditional probability*) mampu meningkatkan akurasi pengelompokan usia wajah?
3. Sejauh mana integrasi *Deep Random Forest* (DRF) mampu memberikan keunggulan generalisasi dan efisiensi waktu komputasi dibandingkan lapisan *Fully Connected* / *SoftMax* standar?

---

## Kontribusi Utama

1. **Arsitektur Hibrida MML-DRF:** Menggabungkan keunggulan ekstraksi fitur representasi *deep learning* (CNN) dengan ketahanan generalisasi pohon keputusan (*Random Forest*) dalam skema multi-task.
2. **Ekstraksi Fitur Multi-Instance Berbasis Struktur Wajah:** Memilih 9 patch wajah anatomis (*three eyes and five chambers*) menggunakan MobileNetV3 yang diperkuat modul *Multi-Instance Fusion* (MIF) berbobot atensi.
3. **Modul Multi-Scale CPR:** Menerapkan *Compact Pyramid Refinement* dengan *depth-wise separable convolutions* (dilation rate 1, 2, 3) untuk memadukan fitur semantik tingkat tinggi dengan detail spasial tingkat rendah.
4. **Gender-Conditional Random Forest:** Merumuskan model *probabilistic learning* bersyarat gender dengan fungsi pemisah *Neurally Connected Split Function* (NCSF) yang terbukti meningkatkan akurasi pengelompokan usia hingga ~8% pada dataset Adience.
5. **Efisiensi Komputasi Tinggi:** Memangkas durasi pelatihan hingga kurang dari 1/10 waktu komputasi model *Residual Networks of Residual Networks* (RoR).

---

## Dataset

### Dataset 1: MORPH-II
- Nama dataset: MORPH Album 2 (MORPH-II)
- Sumber dataset: Ricanek & Tesafaye (2006)
- Jumlah data: 55.132 citra wajah (46.645 pria dan 8.487 wanita) dari populasi non-selebriti.
- Komposisi Demografis:
  - Gender: 84,6% Male, 15,4% Female.
  - Usia: Rentang 16 hingga 77 tahun.
  - Kelompok Usia Target (3 Grup): Grup 1 (16–30 tahun), Grup 2 (31–45 tahun), Grup 3 (46–60+ tahun).
- Keseimbangan data: Imbalanced gender (dominasi pria), terkontrol secara pencahayaan dan pose (*semi-constrained*).
- Resolusi & Format Citra: Citra wajah terpusat (frontal/semi-frontal), format RGB.
- Status akses: Akademik / Berlisensi.
- Label Target: Gender (Male / Female) dan Kelompok Usia (3 kelas).
- Tujuan penggunaan: Evaluasi performa pada dataset semi-terkontrol skala besar.

### Dataset 2: Adience Benchmark
- Nama dataset: Adience Faces Benchmark
- Sumber dataset: Eidinger, Enbar, & Hassner (2014)
- URL: https://talhassner.github.io/home/projects/Adience/
- Jumlah data: ~26.000 citra (17.603 citra teranotasi lengkap) dari 2.284 subjek unik yang diunggah ke Flickr melalui ponsel pintar.
- Komposisi Demografis:
  - Gender: 8.192 Male, 9.411 Female (cukup seimbang).
  - Kelompok Usia Target (8 Grup): 0–2 (1.427), 4–6 (2.162), 8–13 (2.294), 15–20 (1.653), 25–32 (4.897), 38–43 (2.350), 48–53 (825), 60+ (869).
- Keseimbangan data: Sangat menantang (*in-the-wild*) dengan variasi ekstrem pada pencahayaan, pose, resolusi rendah, ekspresi, dan oklusi.
- Pembagian data: Standard 5-Fold Subject-Exclusive Cross-Validation.
- Status akses: Open Access untuk riset non-komersial.
- Label Target: Gender (Male / Female) dan Kelompok Usia (8 kelas).
- Tujuan penggunaan: Evaluasi ketangguhan model pada kondisi *unconstrained in-the-wild*.

---

## Metodologi Penelitian

### Gambaran Umum
Metodologi penelitian terdiri dari dua tahapan besar: (1) Ekstraksi fitur representasi mendalam multi-instance dan multi-skala (MML) menggunakan backbone MobileNetV3 terpadu, dan (2) Klasifikasi multi-task hierarkis berbasis *Deep Random Forest* (DRF), di mana gender diprediksi terlebih dahulu dan kemudian digunakan sebagai kondisi probabilitas untuk pengelompokan usia.

```
                          Citra Masukan
                                │
                                ▼
         ┌──────────────────────────────────────────────┐
         │ 1. Deteksi Wajah & Landmark (YOLOX)          │
         │    - Ekstraksi 9 Facial Instances            │
         └──────────────────────┬───────────────────────┘
                                │
                                ▼
         ┌──────────────────────────────────────────────┐
         │ 2. Multi-Instance Multi-Scale Learning (MML) │
         │    - Backbone: MobileNetV3                   │
         │    - Modul Multi-Instance Fusion (MIF)       │
         │    - Decoder: Compact Pyramid Refinement     │
         └──────────────────────┬───────────────────────┘
                                │
                                ▼ Vektor Fitur y
         ┌──────────────────────────────────────────────┐
         │ 3. Deep Random Forest (DRF) Multi-Task       │
         ├──────────────────────────────────────────────┤
         │ a. Random Forest Gender T^G                  │
         │    → Prediksi Probabilitas Gender p(g|y)     │
         │                                              │
         │ b. Gender-Conditional Random Forest T^A      │
         │    → Pemisahan Node NCSF                     │
         │    → Prediksi Usia Bersyarat p(a|g, y)       │
         └──────────────────────┬───────────────────────┘
                                │
                                ▼
                Output: [Gender, Age Group]
```

### Arsitektur / Pendekatan
- **Deteksi Wajah & Seleksi 9 Instances:**
  - Menggunakan algoritma deteksi YOLOX untuk memotong wajah murni (*Instance 1: full face*).
  - Menemukan posisi ujung hidung (*nose tip*) melalui lokalisasi landmark.
  - Berdasarkan aturan proporsi klasik wajah "tiga bagian dan lima mata" (*three eyes and five chambers*), 8 patch wajah lainnya dipotong: dahi (Inst 2), mata kanan (Inst 3), mata kiri (Inst 4), tengah wajah (Inst 5), hidung (Inst 6), pipi kanan (Inst 7), pipi kiri (Inst 8), dan mulut/dagu (Inst 9).
- **Backbone & Multi-Instance Fusion (MIF):**
  - Menggunakan MobileNetV3 sebagai arsitektur dasar ekstraksi instance.
  - Setiap skala fitur ($S_1, S_2, S_3, S_4, S_5$) diproses melalui Global Average Pooling (GAP), 2 lapisan FC, ReLU, dan Sigmoid untuk menghasilkan vektor atensi $v^i$.
  - Vektor atensi dikalikan dengan fitur Inverted Residual Blocks (IRBs) untuk merekalibrasi fitur instance: $C^i = \text{IRB}(v^i \otimes N^i)$, kemudian digabungkan secara konkatenasi: $C = [C^1, C^2, \dots, C^M]$.
- **Multi-Scale Integration Learning (CPR):**
  - Menggunakan modul *Compact Pyramid Refinement* (CPR) pada decoder.
  - Saluran diperluas dengan konvolusi 1×1, diproses melalui tiga *depth-wise separable convolutions* dengan rasio dilatasi 1, 2, dan 3, distandarisasi dengan Batch Normalization, dan dikompresi kembali ke dimensi asal.
- **Gender-Conditional Random Forest (DRF):**
  - **Gender RF ($T^G$):** Dilatih menggunakan ukuran ketidakpastian (*entropy uncertainty*) untuk membagi node dan menyimpan distribusi Gaussian $N(g; \bar{g}_l, \sigma_l)$ pada leaf node.
  - **Age Conditional RF ($T^A$):** Pohon keputusan dilatih secara independen pada subset data gender. Menggunakan *Neurally Connected Split Function* (NCSF) yang menggabungkan *Information Gain* pohon dengan fungsi koneksi layer tersembunyi MMFL.
  - **Inferensi Probabilitas Usia:**
    $$p(a|y) = \sum_{n} p(a|\Omega_n, y) \int_{g \in \Omega_n} p(g|y) \, dg$$

### Tahapan Metodologi
1. Pra-pemrosesan citra, augmentasi data (translasi acak dan *mirroring*), dan ekstraksi 9 patch wajah.
2. Pelatihan jaringan MML berbasis PyTorch untuk meminimalkan loss representasi fitur.
3. Pelatihan Random Forest Gender $T^G$ pada seluruh data latih.
4. Pembagian data latih berdasarkan gender dan pelatihan Gender-Conditional Random Forest $T^A$ menggunakan pemisah NCSF.
5. Evaluasi pengujian menggunakan skema 5-Fold Subject-Exclusive Cross-Validation pada Adience dan split standar pada MORPH-II.

---

## Detail Implementasi

### Konfigurasi Pelatihan & Optimasi
- Framework Ekstraksi Fitur: PyTorch
- Learning Rate: 0,001
- Epochs: 6.000 iterasi
- Splitting Interactive Times (DRF): 1.500
- Kedalaman Pohon (Tree Depth): 20
- Augmentasi Data: Random translation dan horizontal mirroring
- Skema Validasi: 5-Fold Subject-Exclusive Cross-Validation (Adience)

### Lingkungan Implementasi
- Hardware: Multi-GPU / Multi-core CPU Workstation
- Framework / Library: PyTorch, OpenCV, Scikit-Learn, NumPy
- Komparator Model: Plain CNN (AlexNet), ResNet50, RoR (Residual Networks of Residual Networks), CNN-ELM

---

## Evaluation Metrics

### Metrik Klasifikasi
- **Classification Accuracy (%):** Persentase prediksi gender dan kelompok usia yang tepat terhadap total sampel data uji.
- **Confusion Matrix:** Matriks konfusi multi-kelas (3×3 pada MORPH-II dan 8×8 pada Adience) untuk mengevaluasi akurasi spesifik per kelompok umur dan pola kesalahan adjacent-class.
- **Ablation Comparison Metric:** Perbandingan akurasi pengelompokan usia dengan vs tanpa *gender-aligned conditional probability*.

---

## Hasil Penelitian

### Temuan Utama
1. **Performa State-of-the-Art:** Model usulan MML-DRF meraih akurasi gender **99,60%** dan usia **96,14%** pada MORPH-II, serta akurasi gender **93,48%** dan usia **63,72%** pada Adience benchmark (*in-the-wild*).
2. **Efektivitas Gender-Aligned Conditioning:** Menjadikan gender sebagai kondisi probabilitas bersyarat terbukti meningkatkan akurasi pengelompokan usia sebesar **~8%** pada dataset Adience yang menantang.
3. **Keunggulan Ekstraksi Fitur MML:** Fitur MML mengungguli fitur konvensional (Gabor, LBP, BIF) maupun fitur deep learning standar (Plain CNN, ResNet50) dengan peningkatan margin akurasi hingga +4%–8%.
4. **Efisiensi Pelatihan DRF:** Dibandingkan dengan arsitektur dalam yang sangat kompleks seperti RoR, waktu pelatihan DRF **kurang dari 1/10 waktu pelatihan RoR**, dan waktu inferensinya jauh lebih cepat.

### Analisis Penulis
- Pada dataset Adience, kelompok usia ekstrem (0–2 tahun dengan akurasi 66,90%, 25–32 tahun dengan 65,35%, dan 60+ tahun dengan 65,24%) memiliki akurasi tertinggi karena fitur morfologi visualnya sangat khas. Sebaliknya, kelompok usia transisi (48–53 tahun dengan 60,29%) memiliki tingkat kesalahan tertinggi akibat kemiripan visual dengan kelompok usia 38–43 dan 60+.
- Analisis matriks konfusi membuktikan bahwa mayoritas kesalahan prediksi usia hanya bergeser ke kelompok usia yang bersebelahan (*adjacent age group*), yang secara praktis masih sangat dapat ditoleransi.

---

## Score

### 1. Perbandingan Akurasi Ekstraksi Fitur pada Dataset Adience

| Fitur yang Digunakan | Classifier SVM (Gender / Usia) | Classifier DRF Usulan (Gender / Usia) |
|----------------------|:------------------------------:|:-------------------------------------:|
| Gabor | 82,61% / 42,72% | 82,45% / 48,62% |
| LBP | 84,52% / 41,47% | 85,06% / 47,67% |
| BIF | 83,48% / 44,06% | 83,67% / 50,61% |
| Plain CNN (AlexNet) | 86,83% / 50,75% | 87,14% / 55,32% |
| ResNet50 | 88,21% / 51,58% | 89,84% / 58,05% |
| **MMFL (Usulan)** | **92,35% / 55,24%** | **93,48% / 63,72%** |

---

### 2. Perbandingan Performa dengan Metode State-of-the-Art

| Metode | MORPH-II Gender Acc | MORPH-II Age Acc | Adience Gender Acc | Adience Age Acc |
|--------|:-------------------:|:----------------:|:------------------:|:---------------:|
| Plain CNN | 98,70% | 89,15% | 86,80% | 50,70% |
| RoR (ResNet of ResNet) | 99,50% | 94,86% | 92,43% | 62,34% |
| CNN-ELM | 98,50% | 92,58% | 88,20% | 52,30% |
| **MML-DRF (Metode Usulan)** | **99,60%** | **96,14%** | **93,48%** | **63,72%** |

---

### 3. Matriks Konfusi Pengelompokan Usia MORPH-II (3 Grup)

| True \ Pred | Grup 1 (16–30) | Grup 2 (31–45) | Grup 3 (46–60+) |
|-------------|:--------------:|:--------------:|:---------------:|
| **Grup 1 (16–30)** | **97,80%** | 1,40% | 0,80% |
| **Grup 2 (31–45)** | 1,80% | **96,60%** | 1,60% |
| **Grup 3 (46–60+)** | 3,20% | 2,78% | **94,02%** |

---

## Kelebihan Penelitian

1. **Pemanfaatan Dependensi Gender-Usia:** Menggunakan gender sebagai kondisi probabilitas bersyarat secara cerdas mengatasi disparitas pola penuaan pria vs wanita.
2. **Ketahanan Multi-Instance:** Pembagian 9 patch anatomis wajah berhasil memitigasi distorsi lokal seperti oklusi kacamata, bayangan pencahayaan, dan variasi pose.
3. **Efisiensi Waktu & Generalisasi:** Penggunaan DRF terbukti lebih cepat dilatih (10× lebih cepat dari RoR) serta menghindari kelemahan *overfitting* lapisan FC konvensional.
4. **Evaluasi Ketat:** Menggunakan protokol validasi silang 5-fold *subject-exclusive* pada benchmark Adience yang tidak terkontrol.

---

## Keterbatasan Penelitian

1. **Ketergantungan pada Akurasi Deteksi Hidung:** Pemotongan 8 patch anatomis bergantung pada keberhasilan deteksi ujung hidung (*nose tip landmark*), yang rentan gagal pada pose wajah profil ekstrem (>45°).
2. **Tidak Melibatkan Atribut Ras / Etnis:** Model hanya membatasi multi-task pada gender dan usia, belum mengintegrasikan atribut ras/etnis yang juga mempengaruhi morfologi wajah secara signifikan.
3. **Klasifikasi Usia Diskret (Grouping):** Model memperlakukan usia sebagai klasifikasi kelompok diskret (*grouping*), bukan estimasi regresi kontinu nilai usia eksak (*exact chronological age*).

---

## Future Work (Saran Penelitian Selanjutnya)

1. Mengintegrasikan atribut wajah lainnya (seperti ras/etnisitas, ekspresi emosi, dan pose) ke dalam kerangka kerja multi-task terpadu.
2. Memanfaatkan ketergantungan silang antara ras, gender, dan usia untuk meningkatkan ketepatan identifikasi simultan.
3. Mengembangkan mekanisme regresi usia kontinu yang diselaraskan dengan representasi fitur multi-skala.

---

## Catatan Penting untuk Riset Kita

### Insight yang Dapat Diadopsi
- **Sinergi Kuat Antara Fitur Usia dan Gender:** Temuan bahwa penuaan wajah memiliki dependensi erat terhadap gender memvalidasi keputusan riset kita untuk menyertakan **ViT-Age** bersama **ViT-Face** dan **ViT-Emotion** dalam mengekstrak fitur demografis wajah.
- **Kelemahan Fully Connected End-to-End:** Paper ini mengonfirmasi bahwa *classifier* non-backpropagation (seperti Random Forest atau SVM) memiliki generalisasi yang lebih baik dan lebih tahan *overfitting* dibanding lapisan Dense/Softmax standar.

### Relevansi dengan Kerangka Kerja Multi-Domain ViT (Identity + Emotion + Age) + SVM
- Pada paper Liao et al., fusi multi-skala dilakukan pada level konvolusi CNN (MobileNetV3) dan diprediksi bersyarat via Random Forest.
- Pada penelitian kita, kita membawa konsep ini ke tingkat yang lebih tinggi: memanfaatkan **Vision Transformer (ViT)** *pre-trained* pada domain Identitas (`skutaada/VIT-VGGFace`), Emosi (`dima806/facial_emotions`), dan Usia (`dima806/facial_age`).
- Vektor fitur embedding tingkat tinggi (2.304 dimensi) kemudian diklasifikasikan menggunakan **Support Vector Machine (SVM)** dengan optimasi *GridSearchCV* 288 parameter pada dataset DemogPairs (10.800 citra seimbang sempurna), mencapai akurasi **93,70%** pada 6 kelas interseksional ras dan gender.

### Hal yang Membedakan Paper Ini dari Penelitian Kita
| Aspek | Liao et al. (2022) | Penelitian Kita |
|-------|--------------------|-----------------|
| **Tugas Target** | Klasifikasi Multi-Task (Gender biner + 8 Kelompok Usia) | Klasifikasi Interseksional Terpadu (3 Ras × 2 Gender = 6 kelas) |
| **Ekstraktor Fitur** | MobileNetV3 + 9 Instance Patches + CPR | 3 Multi-Domain Vision Transformers (ViT-Face, ViT-Emotion, ViT-Age) |
| **Dimensi Fitur** | Multi-instance multi-scale tensor | Concatenated Latent Embeddings (2.304-d) |
| **Classifier** | Multi-Task Deep Random Forest (DRF) | Support Vector Classifier (SVC) dengan GridSearchCV & 5-Fold CV |
| **Dataset** | MORPH-II & Adience | DemogPairs (10.800 citra berimbang sempurna) |
| **Performa Utama** | Gender: 93,48%, Usia: 63,72% (Adience) | **Akurasi 6-Kelas: 93,70%**, Macro F1: **0,9369** |
