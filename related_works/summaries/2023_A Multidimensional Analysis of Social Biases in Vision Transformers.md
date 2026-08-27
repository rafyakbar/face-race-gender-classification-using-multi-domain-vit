# A Multidimensional Analysis of Social Biases in Vision Transformers

## Informasi Umum
- Judul: A Multidimensional Analysis of Social Biases in Vision Transformers
- Penulis: Jannik Brinkmann (University of Mannheim, Germany), Paul Swoboda (University of Mannheim, Germany), Christian Bartelt (University of Mannheim, Germany)
- Tahun: 2023
- Journal / Conference: 2023 IEEE/CVF International Conference on Computer Vision (ICCV 2023)
- Publisher: IEEE / Computer Vision Foundation (CVF)
- ISSN / ISBN: 2380-7504
- Volume / Nomor / Halaman: hlm. 4891–4900
- DOI: 10.1109/ICCV51070.2023.00453
- URL: https://openaccess.thecvf.com/content/ICCV2023/html/Brinkmann_A_Multidimensional_Analysis_of_Social_Biases_in_Vision_Transformers_ICCV_2023_paper.html
- Keywords: Vision Transformers, Social Biases, Fairness, Self-Supervised Learning, Image Embedding Association Test (iEAT), Counterfactual Augmentation
- Riwayat Artikel:
  - Published: October 2023 (ICCV 2023)
- Lisensi: CC BY (CVF Open Access)
- Jenis Paper: Eksperimen & Analisis Empiris / Algorithmic Fairness & Bias Benchmark

---

## Poin-Poin yang Dibahas dalam Introduction
1. Model representasi citra swa-bimbingan (*self-supervised learning / SSL*) seperti SimCLR dan iGPT terbukti menyandikan berbagai bias sosial manusia (seperti rasisme, seksisme, bias usia, dan stereotipe kelompok) di dalam ruang *embedding*-nya.
2. Meskipun bias representasi dalam ruang *embedding* tidak terlihat secara langsung oleh pengguna akhir, bias ini berisiko besar merambat (*propagate*) ke tugas-tugas hilir (*downstream tasks*) selama proses *fine-tuning* atau *feature extraction*.
3. Sebagian besar literatur mengasumsikan bias sosial semata-mata muncul dari ko-okurensi objek dalam data latih (misalnya wanita lebih sering ditampilkan di dapur/rumah, pria di lingkungan industri/konstruksi), namun belum meneliti faktor arsitektur, skala model, dan fungsi objektif pelatihan secara mendalam pada Vision Transformer (ViT).
4. Vision Transformer (ViT) telah menjadi arsitektur standar utama untuk *transfer learning* dalam visi komputer, sehingga sangat penting untuk memahami secara komprehensif faktor-faktor yang memicu atau memitigasi bias sosial dalam representasi laten ViT.

---

## Problem Statement (Apa masalah yang ingin diselesaikan?)

Bagaimana faktor-faktor multi-dimensi—mencakup manipulasi data latih melalui *Counterfactual Data Augmentation* (CDA) berbasis difusi, pemilihan fungsi objektif pelatihan *self-supervised* (diskriminatif vs generatif), skala ukuran model (Base, Large, Huge), resolusi citra masukan, serta lapisan representasi internal (*embedding layer*)—mempengaruhi kemunculan, besaran (*magnitude*), dan arah (*direction*) bias sosial di dalam ruang representasi *Vision Transformers* (ViT)?

---

## Tujuan Penelitian

1. Mengukur dan menguantifikasi bias sosial pada ruang *embedding* berbagai varian ViT menggunakan kerangka kerja *Image Embedding Association Test* (iEAT) yang mencakup 15 uji asosiasi sosial standar.
2. Mengevaluasi efektivitas teknik *Counterfactual Data Augmentation* (CDA) berbasis model difusi teks-ke-citra (*Stable Diffusion* + *CLIPSeg*) dalam memitigasi bias sosial pada tahap pra-pelatihan dan *fine-tuning*.
3. Menganalisis perbedaan manifestasi bias sosial antara model ViT yang dilatih menggunakan objektif diskriminatif (*joint-embedding*: DINO, MoCo-v3, MSN) dibandingkan objektif generatif (*reconstruction-based*: MAE, BEiT, iGPT).
4. Menyelidiki pengaruh skala kapasitas parameter model, resolusi spasial citra masukan, ukuran patch, dan kedalaman lapisan terhadap intensitas bias sosial yang disandikan.

---

## Research Question

1. Sejauh mana augmentasi data kontrafaktual berbasis penyuntingan semantik model difusi mampu mengurangi atau mengeliminasi bias sosial pada model ViT tanpa merusak kualitas representasi untuk tugas hilir?
2. Mengapa model ViT dengan fungsi objektif diskriminatif menyandikan bias sosial yang jauh lebih rendah dibandingkan model dengan fungsi objektif rekonstruksi generatif?
3. Bagaimana pengaruh penskalaan ukuran model (*scaling model size*) dan peningkatan resolusi citra terhadap besaran efek bias sosial (*bias effect size*)?
4. Apakah model yang dilatih pada dataset yang sama selalu mewarisi bias yang searah, ataukah fungsi objektif pelatihan dapat memicu arah bias yang berkebalikan (*opposite biases*)?

---

## Kontribusi Utama

1. **Analisis Multi-Dimensi Pertama pada ViT:** Menyajikan investigasi sistematis pertama mengenai bias sosial pada representasi laten Vision Transformers melintasi 15 dimensi pengujian iEAT (mencakup ras, gender, warna kulit, disabilitas, usia, agama, dan orientasi seksual).
2. **CDA Berbasis Generatif Difusi Semantik:** Mengembangkan pipeline augmentasi data kontrafaktual menggunakan BLIP, CLIPSeg, dan Stable Diffusion (menghasilkan 159.393 citra kontrafaktual dari ImageNet-1K), membuktikan bahwa CDA dapat mereduksi bias tetapi tidak mampu menghilangkannya secara tuntas serta membawa konsekuensi sedikit penurunan performa representasi hilir.
3. **Bukti Keunggulan Objektif Diskriminatif:** Menunjukkan secara empiris bahwa ViT yang dilatih dengan objektif diskriminatif (seperti DINO dan MoCo) secara konsisten memiliki jumlah bias signifikan yang jauh lebih sedikit dibandingkan model generatif berbasis rekonstruksi piksel/token (seperti MAE dan BEiT).
4. **Skalabilitas Model Mereduksi Bias:** Membuktikan bahwa memperbesar kapasitas model (Base $\rightarrow$ Large $\rightarrow$ Huge) dan meningkatkan resolusi citra masukan (224 $\rightarrow$ 384 $\rightarrow$ 512) secara sistematis menurunkan rata-rata magnitudo bias sosial.
5. **Penemuan Fenomena Bias Berlawanan (*Opposite Biases*):** Mengungkapkan bahwa model ViT yang dilatih pada dataset yang persis sama (ImageNet-21k) dapat menunjukkan arah bias yang berkebalikan tergantung objektif pelatihannya, membuktikan bahwa bias bukan sekadar cerminan statistik ko-okurensi data mentah semata.

---

## Dataset

### 1. Dataset Benchmark Bias: Image Embedding Association Test (iEAT)
- Nama dataset: iEAT Dataset
- Sumber: Steed & Caliskan (FAccT 2021)
- Struktur Uji: 15 uji asosiasi konsep target ($X, Y$) terhadap pasangan atribut stereotipikal ($A, B$):
  - **T1:** Young vs Old (Pleasant vs Unpleasant)
  - **T2:** Other vs Arab-Muslim (Pleasant vs Unpleasant)
  - **T3:** European American vs Asian American (American vs Foreign)
  - **T4:** Disabled vs Not-Disabled (Pleasant vs Unpleasant)
  - **T5:** Male vs Female (Career vs Family) — *Gender-Career Bias*
  - **T6:** Male vs Female (Science vs Liberal Arts) — *Gender-Science Bias*
  - **T7:** Flower vs Insect (Pleasant vs Unpleasant) — *Baseline Valence Test*
  - **T8:** European American vs Native American (Pleasant vs Unpleasant)
  - **T9:** European American vs African American (Pleasant vs Unpleasant) — *Racial Bias*
  - **T10:** Christianity vs Judaism (Pleasant vs Unpleasant)
  - **T11:** Gay vs Straight (Pleasant vs Unpleasant)
  - **T12:** Light Skin vs Dark Skin (Pleasant vs Unpleasant) — *Skin Tone Bias*
  - **T13:** White vs Black (Tool vs Weapon) — *Weapon Bias*
  - **T14:** White vs Black (Tool vs Weapon Modern) — *Modern Weapon Bias*
  - **T15:** Thin vs Fat (Pleasant vs Unpleasant) — *Body Weight Bias*
- Format data: Citra stimulus beresolusi terstandarisasi untuk evaluasi ruang embedding.

### 2. Dataset Pelatihan & Pre-training Model ViT
- **ImageNet ILSVRC 2012 (ImageNet-1K):** 1,28 juta citra yang digunakan untuk melatih dan mengevaluasi CDA (ditambah 159.393 citra kontrafaktual yang disintesis).
- **ImageNet-21k:** 14,2 juta citra untuk pra-pelatihan model skala besar skala penuh.
- **CIFAR-10:** Digunakan untuk *linear evaluation protocol* (linear probe) guna mengukur kualitas representasi hilir setelah debiasing.

---

## Metodologi Penelitian

### Gambaran Umum
Penelitian ini mengukur representasi bias sosial pada ruang *embedding* laten ViT menggunakan metrik kesamaan kosinus terbobot iEAT. Evaluasi dilakukan secara multidimensi dengan memvariasikan data latih (asli vs kontrafaktual), objektif *self-supervised* (diskriminatif vs generatif), ukuran model (S, M, L, B, H), resolusi masukan, serta kedalaman lapisan transformer (Layer 1 hingga Layer 12).

```
                 Citra Masukan / Stimulus Uji iEAT
                                │
                                ▼
       ┌───────────────────────────────────────────────────────────┐
       │ 1. Arsitektur Vision Transformer (ViT-Base/Large/Huge)    │
       │    - Discriminative SSL: DINO, MoCo-v3, MSN               │
       │    - Generative SSL    : MAE, BEiT, iGPT                  │
       └────────────────────────┬──────────────────────────────────┘
                                │
                                ▼ Ekstraksi Embedding Vektor
       ┌───────────────────────────────────────────────────────────┐
       │ 2. Kerangka Pengukuran Bias: iEAT Formalism               │
       │    - Perhitungan Cosine Similarity s(w, A, B)             │
       │    - Statistik Uji s(X, Y, A, B) & Permutation Test (p_t) │
       │    - Effect Size d (Magnitudo & Arah Bias)                │
       └────────────────────────┬──────────────────────────────────┘
                                │
                                ▼ Analisis Multidimensi
       ┌───────────────────────────────────────────────────────────┐
       │ 3. Investigasi Multi-Faktor:                              │
       │    • Data Augmentation : Stable Diffusion CDA (159k imgs) │
       │    • Training Objective: Discriminative vs Generative     │
       │    • Model Scaling     : Base → Large → Huge              │
       │    • Input Resolution  : 224 → 384 → 512 piksel           │
       │    • Layer Depth       : Layer 1 s.d. Layer 12            │
       └───────────────────────────────────────────────────────────┘
```

### Formulasi Matematika iEAT
1. **Asosiasi Diferensial Target dengan Atribut:**
   $$s(w, A, B) = \mu(\cos(w, a)_{a \in A}) - \mu(\cos(w, b)_{b \in B})$$
2. **Statistik Uji Asosiasi Konsep Target:**
   $$s(X, Y, A, B) = \sum_{x \in X} s(x, A, B) - \sum_{y \in Y} s(y, A, B)$$
3. **Signifikansi Statistik (Permutation Test):**
   $$p_t = \Pr[s(X_i, Y_i, A, B) > s(X, Y, A, B)]$$
   di mana $X_i, Y_i$ adalah partisi acak berukuran sama dari $X \cup Y$. Ambang signifikansi ditetapkan pada $p_t < 0,05$.
4. **Effect Size $d$ (Ukuran Magnitudo & Arah Bias):**
   $$d = \frac{\mu(s(x, A, B)_{x \in X}) - \mu(s(y, A, B)_{y \in Y})}{\sigma(s(t, A, B)_{t \in X \cup Y})}$$
   - $d = 0$ mengindikasikan ketiadaan bias.
   - Nilai absolut $|d|$ mengukur kekuatan bias, sedangkan tanda (+/-) menunjukkan arah asosiasi bias.

### Pipeline Counterfactual Data Augmentation (CDA)
- Menggunakan BLIP dan CLIP untuk menghasilkan deskripsi teks dari citra ImageNet.
- Mengganti istilah gender target (misal: "man" $\rightarrow$ "woman") pada teks.
- Menggunakan CLIPSeg untuk menghasilkan mask area target pada citra.
- Menggunakan Stable Diffusion *inpainting* untuk menggambar ulang area bermasker sesuai teks kontrafaktual.

---

## Detail Implementasi

### Konfigurasi Model & Pelatihan
- **Model ViT yang Diuji:**
  - ViT-DINO-B (12 layer, 12 heads, hidden size 768)
  - ViT-MoCo-B (12 layer, 12 heads, hidden size 768)
  - ViT-MSN-B (Masked Siamese Networks)
  - BEiT-B (BERT pre-training of image transformers, mask ratio 40%)
  - ViT-MAE-B, ViT-MAE-L, ViT-MAE-H (Masked Autoencoder, mask ratio 75%)
  - iGPT-S, iGPT-M, iGPT-L (Image Generative Pre-training)
- **Implementasi:** PyTorch, HuggingFace Transformers, Timm library.
- **Pelatihan Kontrafaktual:** Adam Optimizer, batch size 128, learning rate $1,5 \times 10^{-4}$ selama 1 epoch (untuk mencegah *over-correction*).

---

## Evaluation Metrics

### Metrik Evaluasi Bias & Kualitas
- **iEAT Effect Size ($d$):** Mengukur deviasi baku kekuatan asosiasi bias sosial.
- **Jumlah Bias Signifikan ($N_{\text{bias}}$):** Jumlah uji dari 15 tes iEAT yang memiliki nilai signifikansi statistik $p_t < 0,05$.
- **Linear Probe Classification Accuracy (CIFAR-10):** Mengukur apakah mitigasi bias menurunkan kualitas representasi generalisasi fitur visual.

---

## Hasil Penelitian

### Temuan Utama

#### 1. Dampak Counterfactual Data Augmentation (CDA)
- CDA berhasil menurunkan bias gender pada BEiT (dari $d = 0,65$ ke $0,45$) dan ViT-MoCo (dari $d = 1,41$ ke $1,39$ pada 1-sided CDA, dan dari $1,25$ ke $1,04$ pada 2-sided CDA dari awal).
- Namun pada ViT-MAE, CDA justru sedikit meningkatkan bias ($0,59 \rightarrow 0,64$), membuktikan bahwa efektivitas manipulasi data latih sangat bergantung pada fungsi objektif arsitektur.
- CDA membawa trade-off sedikit penurunan akurasi representasi hilir pada CIFAR-10 (misal: BEiT turun dari 87,5% ke 84,8%).

#### 2. Objektif Diskriminatif vs Generatif
- **Model Diskriminatif Lebih Bersih dari Bias:** ViT-DINO, ViT-MoCo, dan ViT-MSN rata-rata hanya memiliki **2 hingga 4 bias signifikan** pada ambang $p_t < 0,05$.
- **Model Generatif Sangat Rentan Bias:** ViT-MAE, BEiT, dan iGPT rata-rata menyandikan **6 hingga 8 bias signifikan**.
- **Penyebab:** Objektif generatif memaksa model merekonstruksi pola statistik piksel data latih secara utuh, sehingga secara pasif menyerap dan memperkuat bias stereotipikal. Sebaliknya, objektif diskriminatif mendorong model mempelajari invariansi representasi yang berfokus pada fitur visual esensial yang kurang terpengaruh bias kontekstual.

#### 3. Fenomena Arah Bias Berlawanan (*Opposite Biases*)
- Pada dataset yang persis sama (ImageNet-21k), model dapat menghasilkan arah bias yang bertolak belakang:
  - ViT-MAE mengasosiasikan *Native Americans* lebih negatif dibandingkan *European Americans* ($d = -1,15$).
  - Sebaliknya, ViT-MoCo menunjukkan asosiasi sebaliknya ($d = +1,10$).
- Hal ini membuktikan bahwa fungsi objektif pembelajaran memiliki peran deterministik yang sama besarnya dengan data latih dalam membentuk ruang embedding.

#### 4. Penskalaan Ukuran Model (*Model Scaling*) & Resolusi
- **Ukuran Model:** Semakin besar ukuran ViT, rata-rata magnitudo bias absolut $|d|$ menurun secara signifikan:
  - iGPT: Small ($|d| \approx 0,84$) $\rightarrow$ Medium ($|d| \approx 0,61$) $\rightarrow$ Large ($|d| \approx 0,41$).
  - ViT-MAE: Base $\rightarrow$ Large $\rightarrow$ Huge menunjukkan tren penurunan serupa.
- **Resolusi Masukan:** Pada model BEiT, menaikkan resolusi masukan dari 224 × 224 ke 384 × 384 dan 512 × 512 secara konsisten memperkecil efek bias sosial.

#### 5. Analisis Per-Lapisan (*Layer-wise Analysis*)
- Pada lapisan awal (Layer 1–4), seluruh model menunjukkan jumlah bias yang mirip karena mendeteksi fitur tingkat rendah (seperti kecerahan piksel yang berkorelasi dengan warna kulit).
- Pada lapisan akhir (Layer 8–12), model diskriminatif berhasil mendispersikan dan membuang bias sosial, sedangkan model generatif mempertahankan bias tersebut hingga ke lapisan keluaran.

---

## Score

### 1. Effect Size iEAT pada Berbagai Model Self-Supervised (ImageNet-21k)

| Model ViT | Tipe Objektif | T1 (Age) | T5 (Gender-Career) | T6 (Gender-Science) | T9 (Race) | T12 (Skin Tone) | T13 (Weapon Bias) | Rata-rata $|d|$ |
|-----------|:-------------:|:--------:|:------------------:|:-------------------:|:---------:|:---------------:|:-----------------:|:---------------:|
| **ViT-DINO-B** | Diskriminatif | -0,99 | **-0,38** | -0,01 | -0,49 | -0,13 | -0,88 | **0,57** |
| **ViT-MoCo-B** | Diskriminatif | -0,15 | **-1,41** | -0,13 | **-1,10** | -0,11 | -0,77 | **0,61** |
| **ViT-MSN-B** | Diskriminatif | -0,93 | **-0,14** | -0,31 | -0,78 | **-1,09** | -0,18 | **0,59** |
| **BEiT-B** | Generatif | -0,18 | **-0,65** | -0,09 | **-1,28** | **-1,14** | **-1,58** | **0,81** |
| **iGPT-S** | Generatif | -0,66 | **-0,22** | -0,16 | -0,54 | **-1,31** | **-1,11** | **0,84** |
| **ViT-MAE-B** | Generatif | -0,11 | **-0,59** | -0,08 | -0,81 | **-0,96** | **-1,30** | **0,82** |

*(Catatan: Angka tebal menunjukkan bias signifikan secara statistik pada $p_t < 0,05$)*

---

### 2. Pengaruh Penskalaan Model terhadap Rata-rata Effect Size $|d|$

| Model | Ukuran (Size) | Parameter (M) | Rata-rata Nilai Absolut Bias $|d|$ |
|-------|:-------------:|:-------------:|:---------------------------------:|
| iGPT-S | Small | ~85M | 0,84 |
| iGPT-M | Medium | ~300M | 0,61 |
| iGPT-L | Large | ~1,4B | **0,41** |
| ViT-MAE-B | Base | 86M | 0,82 |
| ViT-MAE-L | Large | 307M | 0,71 |
| ViT-MAE-H | Huge | 632M | **0,58** |

---

## Kelebihan Penelitian

1. **Investigasi Menyeluruh dan Multi-Faset:** Mengeksplorasi hubungan antara data latih, arsitektur, ukuran model, resolusi, fungsi objektif, dan kedalaman lapisan terhadap bias sosial secara empiris.
2. **Penggunaan Model Generatif Difusi Mutakhir untuk CDA:** Memanfaatkan Stable Diffusion dan CLIPSeg untuk mensintesis data kontrafaktual berkualitas tinggi pada skala ratusan ribu citra.
3. **Analisis Layer-wise yang Mendalam:** Memberikan penjelasan intuitif mengenai bagaimana representasi fitur tingkat rendah bertransformasi menjadi bias semantik tingkat tinggi pada lapisan transformer.
4. **Wawasan Desain Model yang Dapat Ditindaklanjuti:** Memberikan panduan praktis bagi praktisi AI dalam memilih arsitektur dan fungsi objektif yang lebih adil (*fair by design*).

---

## Keterbatasan Penelitian

1. **CDA Tidak Mengeliminasi Bias Secara Tuntas:** Augmentasi kontrafaktual hanya mampu menekan sebagian bias dan berpotensi menurunkan akurasi generalisasi tugas hilir.
2. **Sampel Pengujian Patch Size Terbatas:** Variasi eksplorasi ukuran patch masih terbatas pada sedikit model yang tersedia secara publik.
3. **Fokus pada Model Self-Supervised Vision:** Belum mengeksplorasi secara mendalam model *supervised pre-trained* khusus domain wajah biometrik (seperti VGGFace).

---

## Future Work (Saran Penelitian Selanjutnya)

1. Mengembangkan metode intervensi pasca-pelatihan (*post-hoc debiasing interventions*) pada ruang embedding tanpa memerlukan augmentasi data yang mahal.
2. Mengkaji perambatan bias representasi ViT ke tugas-tugas hilir klasifikasi multi-atribut dan deteksi wajah secara kuantitatif.
3. Menyelidiki arsitektur fusi multi-modalitas dan multi-domain untuk membatalkan bias antar-domain yang saling bertentangan.

---

## Catatan Penting untuk Riset Kita

### Insight yang Dapat Diadopsi
- **Kekayaan Representasi Demografis pada ViT:** Paper ini membuktikan secara teoritis dan empiris bahwa Vision Transformer menyandikan fitur-fitur sosial dan demografis (seperti ras, warna kulit, gender, dan usia) secara sangat kuat dan terstruktur pada representasi embedding latennya.
- **Pemanfaatan ViT Layer Representasi Tinggi:** Karena representasi laten ViT mampu menangkap perbedaan atribut manusia yang sangat halus, vektor embedding dari token `[CLS]` lapisan akhir menjadi representasi yang sangat ideal untuk klasifikasi demografis.

### Relevansi dengan Kerangka Kerja Multi-Domain ViT (Identity + Emotion + Age) + SVM
- **Mengapa Multi-Domain Feature Fusion Kita Bekerja Sangat Baik:**
  - Brinkmann et al. menemukan bahwa model ViT tunggal dapat memiliki ketimpangan bias representasi jika berdiri sendiri.
  - Pada penelitian kita, kita mengintegrasikan **tiga domain representasi independen**: ViT-Face (Identitas/Biometrik), ViT-Emotion (Ekspresi/Dinamika Otot), dan ViT-Age (Usia/Morfologi Penuaan) menghasilkan vektor gabungan 2.304 dimensi.
  - Penggabungan multi-domain ini saling melengkapi (*complementary representations*) dan menyeimbangkan ruang fitur.
- **Keadilan Demografis pada Model Kita:**
  - Ketika vektor multi-domain 2.304-d diklasifikasikan menggunakan **Support Vector Machine (SVM)** dengan regularisasi optimal ($C=10$, kernel polinomial) pada dataset DemogPairs (10.800 citra seimbang sempurna), model usulan kita mencapai **Akurasi 93,70%** dan **Macro F1 0,9369**.
  - Analisis per-kelas pada riset kita menunjukkan disparitas yang sangat rendah (F1 seluruh kelas berada di rentang 0,9174 hingga 0,9614), membuktikan bahwa fusi multi-domain ViT + SVM berhasil memitigasi disparitas representasi antar-subkelompok demografis.

### Hal yang Membedakan Paper Ini dari Penelitian Kita
| Aspek | Brinkmann et al. (ICCV 2023) | Penelitian Kita |
|-------|------------------------------|-----------------|
| **Fokus Utama** | Audit & Kuantifikasi Bias Sosial pada Ruang Embedding ViT (iEAT Benchmark) | Klasifikasi Interseksional Ras & Gender Terpadu (6-Kelas) Berbasis Multi-Domain ViT + SVM |
| **Metode Evaluasi** | Image Embedding Association Test (iEAT 15 Tests, Effect Size $d$) | Multiclass Test Accuracy, Macro Precision/Recall/F1, 5-Fold CV, Confusion Matrix |
| **Model ViT** | Model Self-Supervised Umum (DINO, MoCo, MAE, BEiT, iGPT) | 3 Model Pre-trained Spesifik Domain Wajah (ViT-VGGFace, ViT-Emotion, ViT-Age) |
| **Pendekatan Fitur** | Analisis representasi single model | Cross-Domain Feature Fusion (Concatenation 768-d $\rightarrow$ 1.536-d $\rightarrow$ 2.304-d) |
| **Classifier** | Linear evaluation probe pada CIFAR-10 | Support Vector Classifier (SVC) dengan GridSearchCV 288 parameter |
| **Dataset** | ImageNet-1K / ImageNet-21k | DemogPairs (10.800 citra seimbang: 3 Ras × 2 Gender) |
| **Capaian Akhir** | Panduan desain arsitektur ViT yang lebih adil | **Sistem Klasifikasi Ras-Gender Akurasi 93,70% yang Adil & Seimbang** |
