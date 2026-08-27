# Ethnicity Classification Based on Facial Images Using Deep Learning Approach

## Informasi Umum
- Judul: Ethnicity Classification Based on Facial Images using Deep Learning Approach
- Penulis: Abdul-aziz Kalkatawi (University of Jeddah, Saudi Arabia), Usman Saeed (University of Jeddah, Saudi Arabia)
- Tahun: 2024
- Journal / Conference: International Journal of Advanced Computer Science and Applications (IJACSA)
- Publisher: The Science and Information (SAI) Organization
- ISSN / ISBN: 2156-5570 (Online), 2158-107X (Print)
- Volume / Nomor / Halaman: Volume 15, No. 2, 2024, hlm. 217–226
- DOI: 10.14569/IJACSA.2024.0150223
- URL: https://doi.org/10.14569/IJACSA.2024.0150223
- Keywords: Vision transformer, deep learning, ethnicity, race, classification, recognition, Multi-Axis Vision Transformer (MaxViT)
- Riwayat Artikel:
  - Published: February 2024
- Lisensi: Creative Commons Attribution 4.0 International (CC BY 4.0) — Open Access
- Jenis Paper: Eksperimen / Applied Research

---

## Poin-Poin yang Dibahas dalam Introduction
1. Ras dan etnisitas merupakan konsep pengelompokan manusia berdasarkan kriteria biologis dan sosio-geografis yang tercermin nyata pada struktur morfologi wajah (wilayah superior: dahi/mata, tengah: hidung/pipi, dan inferior: bibir/dagu/rahang).
2. Pengenalan etnisitas otomatis melalui teknik visi komputer memiliki signifikansi besar dalam interaksi manusia-komputer (HCI), sistem pengawasan video (*surveillance*), biometrik cerdas, dan analisis demografis.
3. Sebagian besar penelitian terdahulu memiliki dua batasan utama: (a) hanya terbatas pada klasifikasi 3 hingga 4 kelompok etnis makro, dan (b) didominasi oleh arsitektur Convolutional Neural Networks (CNN) atau deskriptor *handcrafted*.
4. Model *Multi-Axis Vision Transformer* (MaxViT) yang menggabungkan *local window attention* dan *global grid attention* dengan blok *Inverted Residual* (MBConv) menawarkan potensi superior dalam memodelkan hubungan spasial lokal dan semantik global untuk pengenalan etnisitas pada citra wajah liar.

---

## Problem Statement (Apa masalah yang ingin diselesaikan?)

Bagaimana meningkatkan akurasi dan kemampuan generalisasi sistem pengenalan etnisitas otomatis dari citra wajah liar untuk mengklasifikasikan 6 kelompok etnis sekaligus (*Asian, Black, Indian, Latino Hispanic, Middle Eastern, White*), serta mengatasi tantangan tumpang tindih visual (*overlapping facial traits*) yang parah pada kelompok etnis multirasial menggunakan arsitektur hybrid *Multi-Axis Vision Transformer* (MaxViT).

---

## Tujuan Penelitian

1. Mengimplementasikan model *Multi-Axis Vision Transformer* (MaxViT) untuk klasifikasi 6 kelompok etnis dari citra wajah secara *end-to-end*.
2. Membangun dataset gabungan skala besar (111.421 citra wajah) dengan mengintegrasikan tiga repositori benchmark etnis: FairFace, UTKFace, dan Arab face dataset.
3. Membandingkan performa akurasi klasifikasi dan efisiensi parameter MaxViT terhadap empat arsitektur CNN terkemuka (VGG-16 / VGG-Face, ResNet-50 / VGG-Face2, EfficientNet-V2, dan AlexNet).
4. Menganalisis akurasi *Top-2* dan matriks konfusi guna memetakan pola kesalahan klasifikasi dan tumpang tindih fenotipe antar-kelompok etnis.
5. Menguji skalabilitas model MaxViT pada skenario 3 kelas (Black, White, Others) vs 6 kelas penuh.

---

## Research Question

1. Bagaimana efektivitas mekanisme *Multi-Axis Self-Attention* (Max-SA: Window Attention + Grid Attention) pada MaxViT dalam menangkap fitur fenotipe etnis lokal dan global secara simultan?
2. Apakah model MaxViT mampu mengungguli arsitektur CNN mapan (VGG-Face, ResNet-50, EfficientNet-V2) dalam akurasi klasifikasi 6 etnis sekaligus mempertahankan efisiensi ukuran parameter?
3. Kelompok etnis mana yang memiliki tingkat tumpang tindih morfologi visual (*visual overlap*) tertinggi dan bagaimana dampaknya terhadap performa model?

---

## Kontribusi Utama

1. **Penerapan Pertama MaxViT untuk Klasifikasi 6 Etnis:** Menjadi studi perintis yang memanfaatkan arsitektur hybrid *Multi-Axis Vision Transformer* (MaxViT) untuk pengenalan 6 kelompok etnis (*Asian, Black, Indian, Latino Hispanic, Middle Eastern, White*).
2. **Pembangunan Database Multi-Etnis Skala Besar:** Menggabungkan dataset FairFace, UTKFace, dan Arab face dataset menjadi database terpadu berisi **111.421 citra wajah** (101.474 sampel latih dan 9.947 sampel uji terstandarisasi).
3. **Capaian Akurasi Unggul & Top-2 Accuracy:** Meraih akurasi pengujian 6-kelas sebesar **77,2%** dan **Top-2 Accuracy 91,3%** pada data uji 9.947 citra, melampaui VGG-16 (74,7%), ResNet-50 (74,7%), dan EfficientNet-V2 (75,2%).
4. **Efisiensi Parameter Model Tertinggi:** MaxViT hanya memiliki **~30,4 juta parameter**, jauh lebih ringkas dibandingkan VGG-16 (134,2 juta), ResNet-50 (41,1 juta), dan EfficientNet-V2 (52,8 juta).
5. **Skalabilitas 3-Kelas:** Meraih akurasi **83,5%** pada skenario 3 kelas (Black, White, Others), mengungguli AlexNet (78,2%).

---

## Dataset

### Database Gabungan (Merged Dataset: 111.421 Citra Wajah)
- Sumber Integrasi:
  1. **FairFace Dataset:** 97.698 citra wajah 7 kelompok etnis (Kärkkäinen & Joo, 2021).
  2. **UTKFace Dataset:** 20.000 citra wajah 5 kelompok etnis (Zhang et al., 2017).
  3. **Arab Face Dataset:** 8.818 citra wajah sub-etnis Arab (Al-Humaidan et al., 2021).
- Total Sampel: **111.421 citra** (101.474 Training / 9.947 Testing).
- Komposisi 6 Kelompok Etnis Target:
  - **Asian:** 15.937 citra (14.350 train, 1.587 test) — 14,3%
  - **Black:** 18.589 citra (16.759 train, 1.830 test) — 16,7%
  - **Indian:** 18.074 citra (16.294 train, 1.780 test) — 16,2%
  - **Latino Hispanic:** 14.988 citra (13.490 train, 1.498 test) — 13,5%
  - **Middle Eastern:** 15.188 citra (13.979 train, 1.209 test) — 13,6%
  - **White:** 28.645 citra (26.602 train, 2.043 test) — 25,7%
- Rasio Pembagian: ~91,1% Training dan ~8,9% Testing per kelas.
- Format & Resolusi: 224 × 224 piksel RGB, Center Cropped, Normalisasi ImageNet.

---

## Metodologi Penelitian

### Gambaran Umum
Sistem memanfaatkan arsitektur hybrid MaxViT yang diawali dengan lapisan konvolusional (*Stem*) untuk mereduksi dimensi spasial awal, diikuti oleh 4 blok MaxViT berjenjang yang memadukan *MBConv* (dengan Squeeze-and-Excitation), *Window Attention*, dan *Grid Attention*, sebelum diakhiri dengan *classification head* 6 kelas.

```
                      Citra Wajah Masukan (224×224×3 RGB)
                                       │
                                       ▼
             ┌───────────────────────────────────────────────────┐
             │ 1. Pra-pemrosesan & Augmentasi                    │
             │    - Center Crop 224×224                          │
             │    - Random Horizontal Flip (Probabilitas 80%)    │
             │    - Normalisasi ImageNet (Mean & Std)            │
             └─────────────────────────┬─────────────────────────┘
                                       │
                                       ▼
             ┌───────────────────────────────────────────────────┐
             │ 2. Stem Convolutional Layer                       │
             │    - Reduksi Spasial: 3×224×224 ──> 64×112×112    │
             │    - Conv (K=3, S=2) → BN → GELU → Conv (K=3, S=1)│
             └─────────────────────────┬─────────────────────────┘
                                       │
                                       ▼
             ┌───────────────────────────────────────────────────┐
             │ 3. Empat Blok MaxViT Berjenjang (Hierarchical)    │
             │    ├─ Block 1 (×2 Module): 64×56×56               │
             │    ├─ Block 2 (×2 Module): 128×28×28              │
             │    ├─ Block 3 (×5 Module): 256×14×14              │
             │    └─ Block 4 (×2 Module): 512×7×7                │
             │    [Tiap Modul: MBConv-SE + Window-Attn + Grid-Attn]
             └─────────────────────────┬─────────────────────────┘
                                       │
                                       ▼
             ┌───────────────────────────────────────────────────┐
             │ 4. Classifier Head & Prediksi                     │
             │    - Adaptive AvgPool → Flatten → LayerNorm       │
             │    - Linear → Tanh → Linear (Output 6 Kelas)      │
             └─────────────────────────┬─────────────────────────┘
                                       │
                                       ▼
                 Prediksi Etnisitas [6 Kelas Output]
```

### Arsitektur / Pendekatan
- **Multi-Axis Self-Attention (Max-SA):**
  - **Window Attention (Block Attention):** Membagi peta fitur menjadi jendela lokal non-overlapping berukuran $P \times P = 7 \times 7$ untuk memodelkan korelasi fitur wajah jarak dekat (seperti bentuk mata, kontur bibir).
  - **Grid Attention (Sparse Global Attention):** Mengambil sampel titik-titik fitur secara seragam pada grid berukuran $G \times G = 7 \times 7$ untuk memodelkan interaksi spasial global lintas wajah secara efisien dengan kompleksitas linear.
  - **Relative Positional Bias:** Menambahkan bias posisi relatif pada operasi multi-head attention untuk mempertahankan topologi struktur wajah.
- **MBConv Block dengan Squeeze-and-Excitation (SE):**
  - Memanfaatkan konvolusi *depthwise separable* dengan pemetaan saluran adaptif via blok SE untuk memperkuat generalisasi fitur lokal.
- **Transfer Learning:** Memanfaatkan bobot pre-trained ImageNet-1K dan melakukan fine-tuning penuh pada seluruh lapisan dengan classifier head 6-kelas.

---

## Detail Implementasi

### Konfigurasi Pelatihan & Optimasi
- **Framework:** PyTorch (2.0.0+cu118) / Python 3.10.5
- **Hardware:** Intel Core i7-6700, 16 GB RAM, GPU NVIDIA RTX 3080 (10 GB VRAM)
- **Input Resolution:** 224 × 224 piksel (3 channel RGB)
- **Optimizer:** Adadelta Optimizer (Learning Rate: 0,1, adaptif otomatis per parameter)
- **Loss Function:** Categorical Cross-Entropy Loss
- **Batch Size:** 20 citra
- **Epochs:** 15 epoch
- **Attention Partition Size:** $7 \times 7$ untuk window attention dan grid attention

---

## Evaluation Metrics

### Metrik Klasifikasi Multi-Kelas
- **Overall Classification Accuracy (%):** Persentase total prediksi benar terhadap 9.947 sampel data uji.
- **Per-Class Accuracy (%):** Akurasi klasifikasi untuk masing-masing dari 6 kelompok etnis.
- **Top-2 Predicted Accuracy (%):** Persentase di mana label sebenarnya berada dalam dua probabilitas prediksi teratas.
- **Model Parameter Count (M):** Jumlah parameter terbobot untuk mengukur efisiensi komputasi dan memori.
- **Confusion Matrix:** Matriks konfusi 6×6 untuk menganalisis tumpang tindih prediksi antar-etnis.

---

## Hasil Penelitian

### Temuan Utama

#### 1. Keunggulan MaxViT terhadap Baseline CNN
- MaxViT meraih akurasi 6-kelas tertinggi (**77,2%**), melampaui seluruh model CNN: EfficientNet-V2 (75,2%), ResNet-50 / VGG-Face2 (74,7%), dan VGG-16 / VGG-Face (74,7%).
- Pada metrik **Top-2 Accuracy**, MaxViT meraih skor **91,3%**, membuktikan bahwa untuk sebagian besar kesalahan, etnisitas sebenarnya berada pada peringkat prediksi kedua.

#### 2. Efisiensi Parameter yang Luar Biasa
- MaxViT hanya berukuran **30,41 juta parameter**, jauh lebih ringan dibanding VGG-16 (134,29 juta parameter), ResNet-50 (41,19 juta parameter), dan EfficientNet-V2 (52,86 juta parameter).

#### 3. Analisis Per-Kelas Etnisitas
- Kelompok etnis dengan akurasi tertinggi:
  - **Black:** **89,6%** (1.639 dari 1.830 citra terprediksi benar).
  - **Asian:** **87,2%** (1.384 dari 1.587 citra terprediksi benar).
  - **Indian:** **79,7%** (1.418 dari 1.780 citra terprediksi benar).
  - **White:** **71,9%** (1.469 dari 2.043 citra terprediksi benar).
- Kelompok etnis dengan akurasi terendah (Tumpang Tindih Tinggi):
  - **Latino Hispanic:** **60,9%** (912 benar; 165 salah ke Indian, 149 ke White, 89 ke Asian).
  - **Middle Eastern:** **38,5%** (466 benar; 218 salah ke White, 134 ke Latino Hispanic, 52 ke Indian).

#### 4. Fenomena Tumpang Tindih Fenotipe Multirasial
- Analisis matriks konfusi membuktikan bahwa kelompok etnis *Middle Eastern*, *Latino Hispanic*, dan *White* memiliki tumpang tindih fenotipe visual yang sangat tinggi karena secara antropologis merupakan populasi multirasial dengan ciri morfologi wajah yang beririsan dekat.

---

## Score

### 1. Perbandingan Akurasi Klasifikasi 6 Etnis dan Ukuran Parameter

| Model | Tipe Arsitektur | 6-Class Accuracy (%) | Top-2 Accuracy (%) | Parameter Count (M) |
|-------|:---------------:|:--------------------:|:------------------:|:-------------------:|
| VGG-16 (VGG-Face) [41] | CNN Monolitik | 74,7 | 85,2 | 134,29 M |
| ResNet-50 (VGG-Face2) [17] | Residual CNN | 74,7 | 88,8 | 41,19 M |
| EfficientNet-V2 [42] | MBConv CNN | 75,2 | 88,9 | 52,86 M |
| **MaxViT (Metode Usulan)** | **Hybrid Vision Transformer** | **77,2** | **91,3** | **30,41 M** |

---

### 2. Akurasi Per-Kelas Etnisitas Model MaxViT pada Test Set (9.947 Citra)

| Kelompok Etnis | Jumlah Sampel Uji | Prediksi Benar | Akurasi Per-Kelas (%) |
|----------------|:-----------------:|:--------------:|:---------------------:|
| **Black** | 1.830 | 1.639 | **89,6%** |
| **Asian** | 1.587 | 1.384 | **87,2%** |
| **Indian** | 1.780 | 1.418 | **79,7%** |
| **White** | 2.043 | 1.469 | **71,9%** |
| **Latino Hispanic** | 1.498 | 912 | **60,9%** |
| **Middle Eastern** | 1.209 | 466 | **38,5%** |
| **Total / Rata-rata** | **9.947** | **7.288** | **77,2%** |

---

### 3. Matriks Konfusi MaxViT (9.947 Sampel Uji 6 Kelas)

| True \ Pred | Black | Asian | Indian | Latino Hispanic | Middle Eastern | White |
|-------------|:-----:|:-----:|:------:|:---------------:|:--------------:|:-----:|
| **Black** | **1.639** | 19 | 73 | 72 | 14 | 13 |
| **Asian** | 30 | **1.384** | 34 | 100 | 12 | 27 |
| **Indian** | 84 | 38 | **1.418** | 154 | 73 | 13 |
| **Latino Hispanic** | 68 | 89 | 165 | **912** | 115 | 149 |
| **Middle Eastern** | 6 | 10 | 52 | 134 | **466** | 147 |
| **White** | 15 | 42 | 27 | 308 | 182 | **1.469** |

---

## Kelebihan Penelitian

1. **Penerapan Arsitektur Vision Transformer Mutakhir:** Mengadopsi MaxViT yang memadukan keunggulan konvolusi lokal (MBConv), atensi lokal (Window Attention), dan atensi global (Grid Attention).
2. **Efisiensi Komputasi Tinggi:** Memiliki jumlah parameter paling kecil (30,4M) namun menghasilkan akurasi tertinggi di antara seluruh baseline CNN.
3. **Database Skala Besar dan Beragam:** Menggabungkan 3 dataset independen (FairFace, UTKFace, Arab Face) untuk membangun basis data 111.421 citra yang mencakup 6 etnis.
4. **Analisis Tumpang Tindih yang Transparan:** Menyajikan evaluasi Top-2 Accuracy (91,3%) dan matriks konfusi rinci yang menjelaskan batas kemampuan klasifikasi etnisitas pada kelompok multirasial.

---

## Keterbatasan Penelitian

1. **Akurasi Masih Terbatas pada 77,2%:** Akurasi klasifikasi 6 etnis secara end-to-end masih tertahan di 77,2% karena ambiguitas visual pada etnis Middle Eastern (38,5%) dan Latino Hispanic (60,9%).
2. **Ketidakseimbangan Jumlah Sampel per Etnis:** Dataset gabungan masih memiliki ketimpangan distribusi (kelas White mencapai 25,7% sedangkan Latino Hispanic hanya 13,5%).
3. **Tidak Melibatkan Atribut Gender atau Usia:** Model dilatih murni untuk etnisitas tunggal tanpa mempertimbangkan interaksi interseksional gender atau penuaan wajah.

---

## Future Work (Saran Penelitian Selanjutnya)

1. Mengembangkan dataset yang lebih representatif untuk kelompok etnis multirasial guna mereduksi ambiguitas klasifikasi.
2. Mengintegrasikan fusi multi-modalitas atau multi-domain fitur (seperti emosi dan usia) untuk memperkuat pemisahan batas keputusan (*decision boundary*).
3. Mengembangkan mekanisme klasifikasi berhierarki (*hierarchical classification*) untuk memisahkan ras makro terlebih dahulu sebelum mengklasifikasi sub-etnis yang beririsan dekat.

---

## Catatan Penting untuk Riset Kita

### Insight yang Dapat Diadopsi
- **Tantangan Klasifikasi End-to-End Monolitik:** Temuan Kalkatawi & Saeed membuktikan bahwa melatih satu model Vision Transformer secara *end-to-end* untuk klasifikasi multi-etnis rentan terhambat di akurasi ~77% akibat tumpang tindih fenotipe visual.
- **Pentingnya Keseimbangan Data Demografis:** Ketimpangan kelas pada dataset gabungan Kalkatawi et al. terbukti memperburuk akurasi kelas minoritas (Middle Eastern jatuh ke 38,5%). Hal ini memperkuat keputusan metodologis riset kita untuk menggunakan **DemogPairs (10.800 citra dengan 1.800 sampel per kelas seimbang sempurna)**.

### Relevansi dengan Kerangka Kerja Multi-Domain ViT (Identity + Emotion + Age) + SVM
- Pada paper Kalkatawi & Saeed, ekstraksi fitur dan klasifikasi dilakukan oleh satu model MaxViT tunggal untuk 6 etnis saja.
- Pada penelitian kita:
  1. Kita mengadopsi **tiga Vision Transformers (ViT-Base)** terpisah yang mencakup tiga pilar komplementer: **Identitas Biometrik** (`skutaada/VIT-VGGFace`), **Dinamika Afektif / Emosi** (`dima806/facial_emotions`), dan **Penuaan Wajah** (`dima806/facial_age`).
  2. Vektor fusi laten 2.304 dimensi menyediakan representasi multi-aspek yang jauh lebih kaya untuk membedakan fitur interseksional.
  3. Klasifikasi dilakukan menggunakan **Support Vector Machine (SVC)** dengan optimasi *GridSearchCV* 288 parameter, menghasilkan **Akurasi 93,70%** dan **Macro F1 0,9369** pada 6 kelas interseksional 3 Ras × 2 Gender secara terpadu.

### Hal yang Membedakan Paper Ini dari Penelitian Kita
| Aspek | Kalkatawi & Saeed (2024) | Penelitian Kita |
|-------|--------------------------|-----------------|
| **Tugas Target** | Klasifikasi Etnisitas Tunggal 6-Kelas | Klasifikasi Interseksional Terpadu 6-Kelas (3 Ras × 2 Gender) |
| **Arsitektur Ekstraktor** | Single-backbone Hybrid MaxViT (30,4M params) | 3 Pre-trained Vision Transformers (ViT-Face, ViT-Emotion, ViT-Age) |
| **Domain Fitur** | Fitur Spasial Tunggal (Max-SA: Window + Grid) | Multi-Domain Latent Embeddings (Identitas, Emosi, Usia: 2.304-d) |
| **Classifier** | Dense Linear Head dengan Tanh | Support Vector Classifier (SVC) dengan GridSearchCV (288 kombinasi) |
| **Dataset** | Merged Dataset (111k citra — Tidak Seimbang) | DemogPairs (10.800 citra — 6 Kelas Seimbang Sempurna 100%) |
| **Akurasi Pengujian** | 77,20% (Top-2: 91,30%) | **93,70%**, Macro F1: **0,9369** |
