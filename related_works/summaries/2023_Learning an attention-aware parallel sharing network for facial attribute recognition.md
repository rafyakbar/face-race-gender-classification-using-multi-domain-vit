# Learning an Attention-Aware Parallel Sharing Network for Facial Attribute Recognition

## Informasi Umum
- Judul: Learning an attention-aware parallel sharing network for facial attribute recognition
- Penulis: Si Chen (Fujian Key Laboratory of Pattern Recognition and Image Understanding, Xiamen University of Technology, China), Xinyu Lai (Xiamen University of Technology, China), Yan Yan (Fujian Key Laboratory of Sensing and Computing for Smart City, Xiamen University, China), Da-Han Wang (Xiamen University of Technology, China), Shunzhi Zhu (Xiamen University of Technology, China)
- Tahun: 2023
- Journal / Conference: Journal of Visual Communication and Image Representation (Elsevier)
- Publisher: Elsevier Inc.
- ISSN / ISBN: 1047-3203
- Volume / Nomor / Halaman: Volume 90, Article 103745, hlm. 1–11
- DOI: 10.1016/j.jvcir.2022.103745
- URL: https://www.sciencedirect.com/science/article/pii/S1047320322002656
- Keywords: Facial attribute recognition, Multi-task learning, Attention mechanism, Parallel sharing network, Class imbalance
- Riwayat Artikel:
  - Received: 7 April 2022
  - Revised: 29 October 2022
  - Accepted: 28 December 2022
  - Available online: 3 January 2023
- Lisensi: Elsevier ScienceDirect Article
- Jenis Paper: Eksperimen / Applied Research

---

## Poin-Poin yang Dibahas dalam Introduction
1. Atribut wajah (*facial attributes*) seperti usia, gender, ras, ekspresi, dan aksesoris mendeskripsikan karakteristik spesifik wajah manusia dan memiliki aplikasi luas dalam pencarian citra, verifikasi biometrik wajah, pengawasan cerdas, dan media sosial.
2. Metode *Facial Attribute Recognition* (FAR) berbasis deep learning terbagi menjadi: metode berbasis bagian (*part-based*) yang memerlukan lokalisasi bagian wajah secara eksplisit, dan metode holistik (*holistic methods*) yang mengekstrak fitur dari seluruh citra wajah tanpa deteksi bagian terpisah.
3. Metode *Multi-Task Learning* (MTL) holistik konvensional umumnya menerapkan jaringan berbagi serial (*serial sharing network / SSN*), di mana fitur tingkat rendah dibagi bersama dan cabang multi-task hanya memprediksi atribut pada lapisan akhir. Akibatnya, fitur spasial tingkat rendah yang kaya detail tidak dieksplorasi secara optimal dan sulit menentukan titik pemisahan (*split point*) jaringan.
4. Dataset FAR dunia nyata sering kali mengalami ketidakseimbangan kelas (*class imbalance*) yang parah antar-atribut (misalnya sampel positif untuk atribut *Bald*, *Mustache*, dan *Gray Hair* sangat langka), serta terganggu oleh wilayah wajah yang tidak informatif (*distractive background/regions*).

---

## Problem Statement (Apa masalah yang ingin diselesaikan?)

Bagaimana mengatasi kelemahan jaringan berbagi serial (SSN) pada multi-task FAR yang mengabaikan kekayaan fitur spasial tingkat rendah, merancang mekanisme atensi yang mampu mengukur kompatibilitas fitur lokal dan global multi-level secara fleksibel, serta memitigasi masalah ketidakseimbangan kelas (*class imbalance*) dan penambangan sampel sulit (*hard example mining*) pada pengenalan multi-atribut wajah.

---

## Tujuan Penelitian

1. Merancang arsitektur **Attention-aware Parallel Sharing (APS)** network untuk pengenalan multi-atribut wajah secara holistik dan terpadu.
2. Mengembangkan sub-jaringan berbagi paralel (*Parallel Sharing Network / PSN*) yang memungkinkan sub-jaringan spesifik tugas secara adaptif mengekstrak fitur dari setiap blok konvolusi sub-jaringan bersama (VGG-16).
3. Mengintegrasikan mekanisme atensi berbasis *multi-feature soft-alignment modules* untuk mengevaluasi kompatibilitas semantik antara fitur lokal multi-level dan deskriptor global tingkat akhir.
4. Mengembangkan skema penalti *Adaptive Focal Loss* (AFL) yang bobotnya otomatis menyesuaikan rasio sampel positif per batch guna menyeimbangkan pembelajaran pada atribut yang mengalami ketidakseimbangan kelas ekstrem.
5. Mengevaluasi performa pengenalan 40 atribut wajah pada benchmark skala besar CelebA dan LFWA serta membandingkannya dengan metode *state-of-the-art*.

---

## Research Question

1. Bagaimana merancang interaksi paralel antara sub-jaringan bersama (*shared sub-network*) dan sub-jaringan spesifik tugas (*task-specific sub-networks*) agar fitur spasial tingkat rendah tidak hilang seiring bertambahnya kedalaman jaringan?
2. Apakah penyelarasan lunak (*soft-alignment*) antara fitur lokal tingkat menengah/dalam dan fitur global lapisan akhir mampu memandu atensi jaringan pada wilayah wajah yang paling diskriminatif?
3. Sejauh mana skema *Adaptive Focal Loss* (AFL) mampu mengatasi bias ketidakseimbangan kelas pada atribut minoritas tanpa menurunkan akurasi atribut mayoritas?

---

## Kontribusi Utama

1. **Arsitektur Parallel Sharing Network (PSN):** Menggantikan struktur serial konvensional dengan jaringan paralel modular yang menghubungkan sub-jaringan bersama (VGG-16) ke sub-jaringan atribut parsial (*partial attributes*) dan atribut umum (*general attributes*) pada setiap blok konvolusi.
2. **Modul Multi-Feature Soft-Alignment:** Mekanisme atensi inovatif yang menghitung skor kompatibilitas antara fitur lokal multi-level dan fitur global FC1, memungkinkan representasi multi-kedalaman berpartisipasi langsung dalam keputusan klasifikasi akhir.
3. **Skema Penalti Adaptive Focal Loss (AFL):** Memformulasikan fungsi loss adaptif yang menggabungkan loss MSE dengan suku penalti Focal Loss yang bobotnya disesuaikan secara dinamis berdasarkan proporsi positif batch latih ($q_j$) dan parameter pemfokus ($\gamma=2$).
4. **Performa State-of-the-Art pada Benchmark FAR:** Meraih rata-rata akurasi **92,12%** pada CelebA (mengungguli 7 metode SOTA dan meraih akurasi terbaik pada 16 atribut) serta **86,74%** pada LFWA (terbaik pada 19 atribut).

---

## Dataset

### 1. Dataset CelebA (CelebFaces Attributes Dataset)
- Nama dataset: CelebA (Liu et al., ICCV 2015)
- URL: http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html
- Jumlah data: 202.599 citra wajah dari 10.177 identitas selebriti.
- Anotasi: 40 atribut biner wajah (termasuk *Male, Young, Pale Skin, Black Hair, Attractive, Chubby, Eyeglasses, Smiling, Pointy Nose*, dll.) dan 5 koordinat landmark wajah.
- Pembagian data:
  - **Training Set:** 162.770 citra
  - **Validation Set:** 19.962 citra
  - **Testing Set:** 19.962 citra
- Resolusi & Format: 224 × 224 piksel, RGB terstandarisasi.
- Karakteristik Tantangan: Variasi pose liar, oklusi, pencahayaan kompleks, dan ketidakseimbangan kelas yang parah antar-atribut.

### 2. Dataset LFWA (Labeled Faces in the Wild with Attributes)
- Nama dataset: LFWA (turunan dari benchmark LFW)
- URL: https://talhassner.github.io/home/projects/lfwa/
- Jumlah data: 13.232 citra wajah dari 5.749 identitas unik.
- Anotasi: 40 atribut biner identik dengan CelebA.
- Pembagian data: 50% Training Set (~6.616 citra) dan 50% Testing Set (~6.616 citra).
- Resolusi & Format: 64 × 64 piksel, RGB.

---

## Metodologi Penelitian

### Gambaran Umum
Sistem APS membagi 40 atribut wajah ke dalam dua kelompok fungsional:
1. **Atribut Parsial (*Partial Attributes*):** Atribut yang terkonsentrasi pada wilayah wajah lokal tertentu (seperti *Eyeglasses, Bags Under Eyes, Big Nose, Pointy Nose, Mustache, Arched Eyebrows*, dll.).
2. **Atribut Umum (*General Attributes*):** Atribut yang mencakup keseluruhan tampilan wajah holistik (seperti *Male, Young, Attractive, Oval Face, Pale Skin, Chubby, Smiling*, dll.).

Arsitektur terdiri dari satu sub-jaringan bersama (VGG-16) dan dua sub-jaringan spesifik tugas yang terhubung secara paralel pada setiap blok konvolusi.

```
                          Citra Masukan (224×224 / 64×64)
                                         │
                                         ▼
         ┌──────────────────────────────────────────────────────────────┐
         │ 1. Sub-jaringan Bersama (Shared Sub-network: VGG-16)         │
         │    - Blok Konvolusi S^1, S^2, S^3, S^4, S^5                  │
         └───────┬──────────────────────┬──────────────────────┬────────┘
                 │                      │                      │
                 ▼ Koneksi Paralel      │                      ▼ Koneksi Paralel
       ┌────────────────────────┐       │            ┌────────────────────────┐
       │ 2. Task-Specific Sub-1 │       │            │ 3. Task-Specific Sub-2 │
       │    (Partial Attributes)│       │            │    (General Attributes)│
       │    - Blok Atensi Tugas │       │            │    - Blok Atensi Tugas │
       └─────────┬──────────────┘       │            └─────────┬──────────────┘
                 │                      │                      │
                 ▼                      ▼                      ▼
       ┌──────────────────────────────────────────────────────────────┐
       │ 4. Multi-Feature Soft-Alignment Modules (Atensi Multi-Level) │
       │    - Kompatibilitas Fitur Lokal (Blok 4 & 5) + Global (FC1)  │
       │    - Bobot Atensi a_ti^b → Global Descriptor G_t             │
       └────────────────────────┬─────────────────────────────────────┘
                                │
                                ▼
       ┌──────────────────────────────────────────────────────────────┐
       │ 5. Prediksi Atribut & Optimasi Adaptive Focal Loss (AFL)     │
       │    - Klasifikasi Linear Head per Atribut                     │
       │    - AFL = L_MSE + β * L_AF (Menyeimbangkan Imbalance Batch) │
       └────────────────────────┬─────────────────────────────────────┘
                                │
                                ▼
                   Output: 40 Prediksi Biner Atribut
```

### Formulasi Matematika

#### 1. Mekanisme Parallel Sharing Network (PSN)
Fitur masukan $F_t^b$ untuk blok ke-$b$ pada sub-jaringan tugas ke-$t$ dirumuskan sebagai:
$$F_t^b = \begin{cases} S^{b1} \otimes S^{b2}, & b = 1 \\ [p(F_t^{b-1}), S^{b1}] \otimes S^{b2}, & b = 2 \\ [p(F_t^{b-1}), S^{b1}] \otimes S^{b3}, & b = 3, 4, 5 \end{cases}$$
di mana $\otimes$ adalah perkalian *element-wise*, $[\cdot, \cdot]$ adalah konkatenasi fitur, dan $p(\cdot)$ adalah operasi Conv-BN-ReLU-Pool pada blok atensi tugas.

#### 2. Multi-Feature Soft-Alignment Module
- Skor kompatibilitas lokal tugas: $c_{ti}^b = \langle u, h_{ti}^b + g_t \rangle$
- Skor kompatibilitas lokal bersama: $r_i^b = \langle w, l_i^b + g_t \rangle$
- Skor kompatibilitas terpadu terbobot ($\tau = 0,1$):
  $$\hat{c}_{ti}^b = \tau c_{ti}^b + (1 - \tau) r_i^b$$
- Normalisasi SoftMax dan pembentukan deskriptor atensi global ($b = 4, 5$):
  $$G_t^b = \sum_{i=1}^n a_{ti}^b \cdot h_{ti}^b$$
  $$G_t = [\eta G_t^4, (1 - \eta) G_t^5], \quad \eta = 0,1$$

#### 3. Fungsi Loss Adaptive Focal Loss (AFL)
$$AFL = L_{MSE} + \beta \frac{1}{N} \sum_{i=1}^N \sum_{j=1}^M L_{AF}, \quad \beta = 0,25$$
di mana suku penalti $L_{AF}$ dirumuskan sebagai:
$$L_{AF} = \begin{cases} (1 - q_j) \cdot (1 - \hat{y}_{ij})^\gamma \hat{y}_{ij}, & y_{ij} = 1 \\ q_j \cdot \hat{y}_{ij}^\gamma (1 - \hat{y}_{ij}), & y_{ij} = 0 \end{cases}$$
di mana $q_j$ adalah rasio sampel positif untuk atribut ke-$j$ dalam batch latih dan $\gamma = 2$.

---

## Detail Implementasi

### Konfigurasi Pelatihan & Optimasi
- **Platform:** PyTorch
- **Hardware:** NVIDIA Titan X GPU
- **Input Size:** 224 × 224 piksel (CelebA), 64 × 64 piksel (LFWA)
- **Epochs:** 15 epoch
- **Batch Size:** 16
- **Optimizer:** Stochastic Gradient Descent (SGD)
- **Learning Rate:** 0,001 dengan linear decay rate 10
- **Hyperparameter:** $\tau = 0,1$, $\eta = 0,1$, $\gamma = 2$, $\beta = 0,25$

---

## Evaluation Metrics

### Metrik Klasifikasi
- **Attribute Classification Accuracy (%):** Persentase prediksi biner yang benar untuk masing-masing dari 40 atribut wajah.
- **Mean Classification Accuracy (%):** Rata-rata akurasi di seluruh 40 atribut wajah pada himpunan data uji independen.

---

## Hasil Penelitian

### Temuan Utama

#### 1. Keunggulan Arsitektur Parallel Sharing (PSN)
- VGG16-PSN (91,45% pada CelebA) secara konsisten mengungguli jaringan serial VGG16-SSN (91,29%), terutama pada atribut yang membutuhkan detail bentuk seperti *Pointy Nose*, *Oval Face*, dan *Young*.
- PSN membuktikan bahwa memfasilitasi aliran informasi dari setiap blok konvolusi bersama ke sub-jaringan tugas mencegah hilangnya informasi spasial tingkat rendah.

#### 2. Kontribusi Modul Soft-Alignment (AM) dan Loss AFL
- Menambahkan modul atensi *multi-feature soft-alignment* mendongkrak akurasi rata-rata sebesar +0,14% pada CelebA dan +0,61% pada LFWA.
- Skema *Adaptive Focal Loss* (AFL) berhasil meningkatkan pengenalan pada atribut minoritas langka (seperti *Bald* 98,92%, *Gray Hair* 97,91%, *Mustache* 96,04%).

#### 3. Performa State-of-the-Art pada 40 Atribut Wajah
- Model APS mencapai rata-rata akurasi **92,12%** pada CelebA dan **86,74%** pada LFWA, mengungguli seluruh 7 metode SOTA pembanding tanpa memerlukan tugas tambahan seperti deteksi landmark atau pelacakan identitas.

---

## Score

### 1. Hasil Ablation Study pada CelebA dan LFWA

| Varian Model | Parallel Sharing (PSN) | Attention Alignment (AM) | Adaptive Focal Loss (AFL) | CelebA Mean Acc (%) | LFWA Mean Acc (%) |
|--------------|:----------------------:|:------------------------:|:-------------------------:|:-------------------:|:-----------------:|
| VGG16-SSN (Serial) | — | — | — | 91,29 | 86,31 |
| VGG16-PSN | ✓ | — | — | 91,45 | 86,13 |
| APS without AM | ✓ | — | ✓ | 91,98 | 86,13 |
| APS without AFL | ✓ | ✓ | — | 92,00 | 86,20 |
| **APS (Full Model)** | **✓** | **✓** | **✓** | **92,12** | **86,74** |

---

### 2. Perbandingan Akurasi Atribut Demografis Kunci dengan SOTA (CelebA Dataset)

| Atribut Demografis | LNets+ANet [6] | MCNN-AUX [23] | MCFA [48] | DMM-CNN [19] | SSPL [36] | APS (Metode Usulan) |
|---------------------|:--------------:|:-------------:|:---------:|:------------:|:---------:|:-------------------:|
| **Male (Gender)** | 98,00% | 98,17% | 98,00% | 98,29% | **98,86%** | **98,86%** |
| **Young (Usia)** | 87,00% | 88,48% | 88,00% | 88,98% | 88,82% | **88,42%** |
| **Pale Skin (Warna Kulit)** | 91,00% | 97,05% | 97,00% | 97,00% | **97,14%** | **96,91%** |
| **Black Hair** | 88,00% | 89,78% | 89,00% | 90,50% | 89,10% | **91,92%** |
| **Narrow Eyes** | 81,00% | 87,23% | 87,00% | 87,73% | 87,57% | **93,92%** |
| **Rata-rata 40 Atribut** | **87,33%** | **91,29%** | **91,23%** | **91,70%** | **91,68%** | **92,12%** |

---

### 3. Perbandingan Akurasi Rata-rata pada LFWA Dataset

| Metode | Tipe Model | Rata-rata Akurasi (%) |
|--------|:----------:|:---------------------:|
| LNets+ANet [6] | Part-based Cascade CNN | 83,85 |
| MCFA [48] | Multi-Task Cascaded CNN | 83,63 |
| SPLITFACE [49] | Segment-based Occlusion FAR | 85,82 |
| MCNN-AUX [23] | Multi-Task CNN with Auxiliary Layer | 86,31 |
| AFFAIR [47] | End-to-End Landmark-Free CNN | 86,13 |
| SSPL [36] | Spatial-Semantic Patch Learning | 86,34 |
| DMM-CNN [19] | Multi-Task Multi-Label CNN | 86,56 |
| **APS (Metode Usulan)** | **Attention-aware Parallel Sharing** | **86,74** |

---

## Kelebihan Penelitian

1. **Pemanfaatan Fitur Multi-Level Efektif:** Berhasil mengatasi hilangnya fitur spasial tingkat rendah pada arsitektur CNN dalam melalui koneksi paralel dan atensi *soft-alignment*.
2. **Penanganan Dinamis Class Imbalance:** Skema *Adaptive Focal Loss* yang menyesuaikan rasio positif per batch terbukti efektif menaikkan akurasi pada atribut minoritas tanpa merusak stabilitas konvergensi.
3. **Interpretabilitas Tinggi via CAM:** Visualisasi *Class Activation Maps* membuktikan bahwa jaringan secara tepat memusatkan atensi pada area spesifik untuk atribut parsial (mata untuk *Narrow Eyes*, hidung untuk *Big Nose*) dan area luas untuk atribut umum (*Male*, *Chubby*).
4. **Desain End-to-End Ringan:** Tidak memerlukan modul deteksi landmark wajah terpisah atau data anotasi identitas tambahan selama inferensi.

---

## Keterbatasan Penelitian

1. **Backbone Masih Berbasis CNN Konvensional (VGG-16):** Meskipun arsitektur koneksinya paralel, backbone yang digunakan adalah VGG-16 yang memiliki parameter besar dan belum memanfaatkan mekanisme *self-attention global* seperti Vision Transformers (ViT).
2. **Keterbatasan Format Multitask Biner:** Model dirancang untuk memprediksi 40 atribut biner independen secara multi-label, belum memodelkan struktur interseksionalitas multi-arah secara langsung (misalnya pasangan Ras × Gender).
3. **Pengujian Terbatas pada Citra Resolusi Rendah:** Resolusi masukan pada LFWA dibatasi pada 64 × 64 piksel yang mengakibatkan penurunan akurasi pada atribut berdetail halus.

---

## Future Work (Saran Penelitian Selanjutnya)

1. Mengadopsi arsitektur transformer visual mutakhir (*Vision Transformers / Swin Transformer*) sebagai backbone paralel untuk menangkap dependensi jarak jauh antar-atribut.
2. Mengintegrasikan pemodelan relasi graf antar-atribut (*graph convolutional networks*) pada modul penyelarasan atensi.
3. Mengeksplorasi penerapan skema APS pada klasifikasi interseksional demografis wajah skala besar dengan keberagaman etnis yang lebih tinggi.

---

## Catatan Penting untuk Riset Kita

### Insight yang Dapat Diadopsi
- **Pemisahan Karakteristik Atribut Parsial vs Global:** Pembuktian Chen et al. bahwa atribut lokal (mata, hidung) dan atribut global (gender, usia, morfologi wajah) memerlukan representasi yang berbeda memvalidasi konsep **Multi-Domain Feature Fusion** pada riset kita:
  - **ViT-Face** menangkap representasi biometrik & konfigurasi identitas global.
  - **ViT-Emotion** menangkap dinamika mikro-otot wajah lokal (*action units*).
  - **ViT-Age** menangkap tekstur biologis dan kerutan penuaan.
- **Pentingnya Keseimbangan Data Demografis:** Chen et al. harus merancang *Adaptive Focal Loss* yang rumit karena CelebA sangat timpang. Sebaliknya, penelitian kita menggunakan **DemogPairs (10.800 citra seimbang sempurna)** yang secara inheren mengeliminasi bias distribusi kelas dari awal.

### Relevansi dengan Kerangka Kerja Multi-Domain ViT (Identity + Emotion + Age) + SVM
- Pada riset Chen et al., multi-tasking dilakukan pada level CNN konvensional (VGG-16) dengan layer klasifikasi linear.
- Pada penelitian kita, kita memanfaatkan representasi laten transfer dari **3 Vision Transformers (ViT-Base)** terpisah (`VIT-VGGFace`, `facial_emotions`, `facial_age`), menghasilkan vektor fusi 2.304 dimensi.
- Vektor representasi multi-domain tersebut diklasifikasikan menggunakan **Support Vector Machine (SVM)** dengan optimasi *GridSearchCV* 288 parameter, menghasilkan akurasi **93,70%** pada 6 kelas interseksional ras dan gender secara terpadu.

### Hal yang Membedakan Paper Ini dari Penelitian Kita
| Aspek | Chen et al. (2023) | Penelitian Kita |
|-------|--------------------|-----------------|
| **Tugas Target** | Multi-Label Facial Attribute Recognition (40 Atribut Biner) | Klasifikasi Interseksional Terpadu 6-Kelas (3 Ras × 2 Gender) |
| **Arsitektur Ekstraktor** | VGG-16 dengan Parallel Sharing & Attention Blocks | 3 Pre-trained Vision Transformers (ViT-Face, ViT-Emotion, ViT-Age) |
| **Domain Representasi** | Fitur Spasial Parsial vs Umum dalam Satu CNN | Multi-Domain Latent Embeddings (Identitas, Emosi, Usia: 2.304-d) |
| **Classifier** | Multi-Task Linear Layer Head dengan Adaptive Focal Loss | Support Vector Classifier (SVC) dengan GridSearchCV (288 kombinasi) |
| **Dataset** | CelebA (200k) & LFWA (13k) — Imbalanced Multi-label | DemogPairs (10.800 citra seimbang sempurna 6 kelas) |
| **Akurasi Gender / Ras** | Male: 98,86%, Young: 88,42% (Multi-label) | **Akurasi 6-Kelas Interseksional: 93,70%**, Macro F1: **0,9369** |
