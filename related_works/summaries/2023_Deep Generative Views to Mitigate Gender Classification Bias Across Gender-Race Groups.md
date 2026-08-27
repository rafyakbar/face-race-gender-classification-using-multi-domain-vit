# Deep Generative Views to Mitigate Gender Classification Bias Across Gender-Race Groups

## Informasi Umum
- Judul: Deep Generative Views to Mitigate Gender Classification Bias Across Gender-Race Groups
- Penulis: Sreeraj Ramachandran (School of Computing, Wichita State University, USA), Ajita Rattani (School of Computing, Wichita State University, USA)
- Tahun: 2023 (ICPR 2022 Workshops)
- Journal / Conference: Pattern Recognition, Computer Vision, and Image Processing. ICPR 2022 International Workshops and Challenges (Springer Nature Switzerland)
- Publisher: Springer Nature Switzerland, Cham
- ISSN / ISBN: 978-3-031-37731-0
- Volume / Nomor / Halaman: hlm. 551–569
- DOI: 10.1007/978-3-031-37731-0_40
- URL: https://link.springer.com/chapter/10.1007/978-3-031-37731-0_40 (Preprint: https://arxiv.org/abs/2208.08382)
- Keywords: Fairness and Bias in AI, Deep Generative Views, Generative Adversarial Networks, Evidential Deep Learning, Gender Classification, Face Biometrics
- Riwayat Artikel:
  - Submitted on arXiv: 17 August 2022
  - Published in Book: 2023 (ICPR 2022 Workshop Proceedings)
- Lisensi: Springer Nature / Open Access on arXiv
- Jenis Paper: Eksperimen / Algorithmic Fairness & Bias Mitigation

---

## Poin-Poin yang Dibahas dalam Introduction
1. Klasifikasi gender otomatis dari citra wajah merupakan atribut biometrik penting yang diterapkan luas dalam pengawasan, interaksi manusia-komputer, periklanan cerdas, dan pencarian citra.
2. Studi-studi terdahulu (termasuk *Gender Shades*) membuktikan adanya bias performa yang parah pada sistem klasifikasi gender komersial maupun akademis, di mana wanita dan individu berkulit gelap (*African-Americans*) secara konsisten mengalami tingkat kesalahan tertinggi.
3. Sebagian besar strategi mitigasi bias yang ada hanya diuji pada kelompok ras yang sangat terbatas (terutama ras biner: *Caucasian* vs *African-American*) dan sering kali menimbulkan kompromi (*trade-off*) yang tidak diinginkan: menurunkan akurasi klasifikasi keseluruhan demi mengejar keadilan (*fairness*).
4. Pemanfaatan ruang laten model generatif mutakhir (*StyleGAN2*) yang memiliki sifat kelancaran lokal (*locally smooth*) membuka peluang besar untuk menghasilkan variasi tampilan wajah sintetik yang realistis (*deep generative views*) guna mengajarkan invariansi representasi pada pengklasifikasi.
5. Kuantifikasi ketidakpastian prediksi (*uncertainty quantification*) berbasis *Evidential Deep Learning* dapat digunakan sebagai opsi penolakan (*reject option*) untuk menyaring sampel-sampel yang berada di daerah ambigu/kritis pada saat inferensi.

---

## Problem Statement (Apa masalah yang ingin diselesaikan?)

Bagaimana memitigasi bias klasifikasi gender lintas kelompok interseksional ras-gender secara simultan tanpa mengorbankan akurasi klasifikasi (*eliminating fairness-accuracy trade-off*), memperluas evaluasi keadilan ke berbagai kelompok etnis non-biner pada citra wajah dan biometrik okular, serta mengkuantifikasi ketidakpastian prediksi model guna menyaring sampel berisiko bias tinggi pada saat pengujian.

---

## Tujuan Penelitian

1. Mengembangkan strategi mitigasi bias gender terpadu yang menggabungkan *Deep Generative Views* berbasis StyleGAN2 (*Neighbor Learning / NL*), *Multi-Task Learning* (MT), dan *Evidential Deep Learning* (EDL).
2. Memanfaatkan ruang laten $W$ dari StyleGAN2 melalui inversi *e4e* dan faktorisasi semantik *SeFA* untuk menghasilkan variasi tetangga lokal yang mereplikasi variasi pose, pencahayaan, dan ekspresi.
3. Menerapkan regularisasi konsistensi berbasis *Jensen-Shannon (JS) Divergence* pada representasi embedding antara citra asli dan citra tetangga generatif.
4. Menerapkan teori logika subjektif (*Dirichlet evidential learning*) untuk mengukur ketidakpastian epistemik ($u$) sebagai mekanisme *reject option* pada saat pengujian.
5. Mengevaluasi performa akurasi dan metrik keadilan (*Degree of Bias / DoB* dan *Selection Rate / SeR*) pada benchmark wajah multi-ras (FairFace, DiveFace, UTKFace, Morph) dan modalitas okular (VISOB, UFPR).

---

## Research Question

1. Bagaimana memanfaatkan geometri lokal dari ruang laten GAN untuk menghasilkan variasi tampilan generatif (*generative views*) yang mampu memperkuat ketahanan representasi fitur terhadap distorsi visual intra-subjek?
2. Apakah penerapan *Neighbor Learning* (NL) mampu meningkatkan akurasi klasifikasi gender sekaligus mereduksi disparitas performa lintas kelompok ras tanpa menimbulkan *trade-off*?
3. Sejauh mana mekanisme *reject option* berbasis *Evidential Deep Learning* mampu mendeteksi dan menyaring prediksi berketidakpastian tinggi guna mendongkrak keadilan algoritmik pada tahap inferensi?

---

## Kontribusi Utama

1. **Strategi Mitigasi Bias Terpadu (NL + MT + EDL):** Menggabungkan pembelajaran terstruktur berbasis tampilan generatif GAN, pembelajaran multi-task berbobot atribut sensitif, dan kuantifikasi ketidakpastian bukti (*evidential learning*).
2. **Eliminasi Trade-off Akurasi vs Keadilan:** Berhasil membuktikan peningkatan ganda (*dual advantage*): meningkatkan akurasi klasifikasi gender sekaligus menekan disparitas performa lintas subkelompok rasial.
3. **Penerapan pada Arsitektur Vision Transformer (CLIP ViT-L/14):** Menunjukkan generalisasi metode pada model *foundation vision-language* CLIP (ViT-L/14), berhasil menurunkan *Degree of Bias* (DoB) dari 1,10 menjadi **0,99** dengan akurasi 96,70%.
4. **Evaluasi Interseksional 7 Kelompok Ras:** Menguji keadilan model melintasi 7 kelompok ras FairFace (*White, Black, Indian, Latino Hispanic, Middle Eastern, East Asian, Southeast Asian*) serta evaluasi lintas-dataset (*cross-dataset*) pada DiveFace, UTKFace, dan Morph.
5. **Mekanisme Reject Option Berbasis Ketidakpastian:** Menunjukkan bahwa menolak 4% sampel dengan ketidakpastian tertinggi (threshold 0,2) mampu meningkatkan akurasi sebesar **+2%** dan menurunkan DoB dari 1,62 menjadi **1,25**.
6. **Generalisasi ke Modalitas Okular:** Membuktikan efektivitas mitigasi bias pada citra biometrik mata dan periokular (VISOB dan UFPR).

---

## Dataset

### 1. Dataset Pelatihan Utama: FairFace (100k Images)
- Nama dataset: FairFace Dataset (Kärkkäinen & Joo, 2021)
- Jumlah data: ~100.000 citra wajah (86.744 train, 10.954 val/test).
- Komposisi Ras: 7 Kelompok Ras (*White, Black, Indian, East Asian, Southeast Asian, Middle Eastern, Latino Hispanic*) yang berimbang.
- Komposisi Gender: Male (53%) dan Female (47%).
- Resolusi & Format: 256 × 256 piksel, RGB.
- Tujuan penggunaan: Pelatihan StyleGAN2, pelatihan encoder *e4e*, dan pelatihan classifier gender utama.

### 2. Dataset Pengujian Lintas-Dataset (Cross-Dataset Evaluation)
- **DiveFace (150k citra):** 4 Kelompok Ras (*East Asian, Sub-Saharan African, South Indian, Caucasian*) berimbang gender 50/50.
- **UTKFace (20k citra):** 4 Kelompok Ras (*White, Black, Indian, Asian*) dengan variasi usia lebar.
- **Morph-II (55k citra):** 2 Kelompok Ras (*Caucasian, African-American*).

### 3. Dataset Modalitas Okular
- **VISOB 2.0:** Citra mata dari perangkat ponsel pintar (evaluasi bias gender pada biometrik okular).
- **UFPR Periocular:** Citra periokular tanpa kendala (*unconstrained mobile scenarios*).

---

## Metodologi Penelitian

### Gambaran Umum
Kerangka kerja yang diusulkan terdiri dari 4 tahapan utama:
1. Pelatihan generator StyleGAN2-ADA pada dataset FairFace (resolusi 256 × 256, FID = 4,29).
2. Pelatihan encoder *e4e* (*encoder4editing*) untuk memproyeksikan citra nyata ke ruang laten $W$.
3. Pembangkitan *Deep Generative Views* menggunakan *SeFA* (Closed-form Factorization) untuk menghasilkan 56 variasi tetangga per citra, disaring dengan detektor wajah MTCNN.
4. Pelatihan pengklasifikasi gender menggunakan *Neighbor Learning* (NL) berbasis loss *Jensen-Shannon Divergence* yang dipadukan dengan *Evidential Deep Learning* (EDL).

```
                 Citra Latih Wajah Asli x_i (FairFace)
                                  │
                                  ▼
       ┌───────────────────────────────────────────────────────────┐
       │ 1. Proyeksi ke Ruang Laten GAN (Encoder e4e)              │
       │    x_i ──> Style Vector w_i ∈ W                           │
       └──────────────────────────┬────────────────────────────────┘
                                  │
                                  ▼
       ┌───────────────────────────────────────────────────────────┐
       │ 2. Pembangkitan Generative Views (SeFA + StyleGAN2)       │
       │    - Perturbasi k-arah semantik: N(w_i)                   │
       │    - Generator G menghasilkan tetangga: N(x_i) = G(N(w_i))│
       │    - Penyaringan Non-Face via MTCNN                       │
       └──────────────────────────┬────────────────────────────────┘
                                  │
                                  ▼ Pasangan [x_i, N(x_i)]
       ┌───────────────────────────────────────────────────────────┐
       │ 3. Structured Neighbor Learning (NL)                      │
       │    - Backbone Classifier: EfficientNetV2-L / CLIP ViT-L/14│
       │    - Forward Pass pada x_i dan N(x_i)                     │
       │    - Backpropagation & Batch Stats HANYA pada x_i         │
       │    - Loss Regularisasi JS Divergence L_N(h(x_i), h(x_j))  │
       └──────────────────────────┬────────────────────────────────┘
                                  │
                                  ▼
       ┌───────────────────────────────────────────────────────────┐
       │ 4. Evidential Deep Learning (EDL) Head                    │
       │    - Parameter Distribusi Dirichlet α = [α_1, ..., α_K]   │
       │    - Kuantifikasi Ketidakpastian Epistemik u = K / S_i    │
       │    - Reject Option pada Sampel Uji dengan u > Threshold   │
       └──────────────────────────┬────────────────────────────────┘
                                  │
                                  ▼
            Prediksi Gender Terkalibrasi [Male / Female]
```

### Formulasi Matematika

#### 1. Fungsi Loss Structured Neighbor Learning
$$L_{\text{total}} = L_{\text{cls}}(y_i, y'_i) + \alpha \sum_{x_j \in N(x_i)} L_N(h_\theta(x_i), h_\theta(x_j))$$
- $L_{\text{cls}}$: Loss klasifikasi (Cross-Entropy atau Evidential Loss).
- $L_N$: Fungsi jarak representasi embedding menggunakan *Jensen-Shannon (JS) Divergence*.
- $\alpha$: Bobot regularisasi ($\alpha = 2$).
- $m$: Jumlah tetangga generatif ($m = 7$ pada konfigurasi optimal).
- *Lazy Regularization:* Regularisasi $L_N$ diaplikasikan setiap $n = 2$ batch untuk mempercepat komputasi.

#### 2. Evidential Deep Learning & Kuantifikasi Ketidakpastian
- Bukti kelas: $e_j = \alpha_{ij} - 1$ di mana $S_i = \sum_{j=1}^K (\alpha_{ij})$ adalah kekuatan Dirichlet.
- Ketidakpastian epistemik:
  $$u = \frac{K}{S_i} = \frac{K}{\sum_{j=1}^K (e_j + 1)}$$
- Fungsi Loss Dirichlet:
  $$L_i = \sum_{j=1}^K (y_{ij} - \hat{p}_{ij})^2 + \frac{\hat{p}_{ij}(1 - \hat{p}_{ij})}{S_i + 1}$$
  $$L_{\text{edl}} = \sum_{i=1}^N L_i + \lambda_t \sum_{i=1}^N \text{KL}[D(p_i|\tilde{\alpha}_i) \,\|\, D(p_i|\langle 1, \dots, 1 \rangle)]$$

---

## Detail Implementasi

### Konfigurasi Pelatihan & Optimasi
- **Backbone Classifier:**
  - EfficientNetV2-L (Pre-trained ImageNet)
  - CLIP ViT-L/14 Vision Tower (Pre-trained OpenAI 400M pairs)
- **Optimizer:** RMSProp dengan Cosine Annealing Schedule
- **Learning Rate Awal:** $4 \times 10^{-4}$
- **Weight Decay:** $1 \times 10^{-5}$
- **Batch Size:** 128 (didistribusikan pada 2 GPU NVIDIA RTX 8000)
- **Label Smoothing:** 0.1
- **Data Augmentation:** AutoAugment policy

---

## Evaluation Metrics

### Metrik Keadilan & Akurasi
- **Average Accuracy (%):** Rata-rata akurasi klasifikasi gender pada seluruh subkelompok demografis.
- **Degree of Bias (DoB $\downarrow$):** Standar deviasi akurasi klasifikasi antar-subkelompok demografis. Nilai lebih rendah menunjukkan model lebih adil.
  $$\text{DoB} = \sqrt{\frac{1}{G} \sum_{g=1}^G (\text{Acc}_g - \overline{\text{Acc}})^2}$$
- **Selection Rate (SeR $\uparrow$):** Rasio antara akurasi subkelompok terburuk terhadap akurasi subkelompok terbaik. Nilai mendekati 100% menunjukkan keadilan sempurna.
  $$\text{SeR} = \frac{\min_g(\text{Acc}_g)}{\max_g(\text{Acc}_g)} \times 100\%$$

---

## Hasil Penelitian

### Temuan Utama

#### 1. Performa pada FairFace (7 Kelompok Ras × 2 Gender)
- Metode usulan **NL (Neighbor Learning)** secara konsisten meningkatkan akurasi sekaligus menurunkan bias:
  - Baseline EfficientNetV2-L: Akurasi 94,27% | DoB 2.01 | SeR 91.96%
  - **+ NL (Neighbor Learning):** Akurasi **95,06%** | DoB **1.67** | SeR **93.68%**
  - **+ MT + NL + EDL:** Akurasi **94,70%** | DoB **1.62** | SeR **93.62%**
- Mengungguli model skala besar Instagram (Mahajan et al., dilatih pada 3,5 miliar citra: Akurasi 93,77%, DoB 1.73).

#### 2. Peningkatan pada CLIP ViT-L/14
- Penerapan metode usulan pada model Vision Transformer CLIP (ViT-L/14) menghasilkan keadilan tertinggi:
  - CLIP Baseline: Akurasi 96,76% | DoB 1.10 | SeR 95.36%
  - **CLIP + NL:** Akurasi **96,70%** | DoB **0.99** | SeR **95.87%** (DoB berhasil ditekan di bawah 1,0).

#### 3. Evaluasi Lintas-Dataset (Cross-Dataset)
- **DiveFace:** Akurasi mencapai **98,60%** dengan DoB sangat rendah (**0.51**) dan SeR **98.39%**.
- **Morph-II:** Akurasi mencapai **96,41%** dengan perbaikan DoB dibanding baseline.
- **UTKFace:** Akurasi mencapai **94,76%**.

#### 4. Dampak Mekanisme Reject Option
- Pada ambang batas ketidakpastian 0,2, model hanya menolak 4% citra masukan yang paling ambigu, namun menghasilkan lonjakan akurasi sebesar **+2%** dan memangkas DoB dari 1.62 menjadi **1.25**.

---

## Score

### 1. Hasil Klasifikasi Gender Lintas 7 Ras pada FairFace Validation Set

| Konfigurasi Model | Arsitektur | Rata-rata Akurasi (%) ↑ | Degree of Bias (DoB) ↓ | Selection Rate (SeR) (%) ↑ |
|-------------------|:----------:|:-----------------------:|:----------------------:|:--------------------------:|
| Baseline | EfficientNetV2-L | 94,27 | 2,01 | 91,96 |
| + NL (LR=2) | EfficientNetV2-L | 94,67 | 1,67 | 93,78 |
| **+ NL (No LR)** | EfficientNetV2-L | **95,06** | **1,67** | **93,68** |
| + MT (Multi-Task) | EfficientNetV2-L | 94,58 | 1,73 | 92,83 |
| + MT + NL | EfficientNetV2-L | 94,59 | 1,66 | 93,48 |
| **+ MT + NL + EDL** | EfficientNetV2-L | **94,70** | **1,62** | **93,62** |
| Instagram SOTA [34] | ResNeXt-101 (3.5B imgs) | 93,77 | 1,73 | 93,66 |
| CLIP + Linear Probe [45] | ViT-L/14 (400M pairs) | 96,76 | 1,10 | 95,36 |
| **CLIP + NL (Usulan)** | **ViT-L/14** | **96,70** | **0,99** | **95,87** |
| **CLIP + MT + NL + EDL** | **ViT-L/14** | **96,70** | **1,00** | **95,38** |

---

### 2. Rincian Akurasi Gender per-Subkelompok Rasial (Model F: MT + NL + EDL)

| Ras / Etnis | Akurasi Male (%) | Akurasi Female (%) | Rata-rata Ras (%) |
|-------------|:----------------:|:------------------:|:-----------------:|
| **Black** | 91,86 | 91,55 | 91,71 |
| **East Asian** | 94,85 | 95,73 | 95,29 |
| **Indian** | 95,35 | 95,41 | 95,38 |
| **Latino Hispanic** | 94,58 | 96,02 | 95,30 |
| **Middle Eastern** | 97,79 | 95,71 | 96,75 |
| **Southeast Asian** | 92,65 | 94,41 | 93,53 |
| **White** | 94,83 | 95,02 | 94,93 |

---

### 3. Hasil Evaluasi Lintas-Dataset (Cross-Dataset Evaluation)

| Konfigurasi Model | UTKFace Acc / DoB | DiveFace Acc / DoB | Morph-II Acc / DoB |
|-------------------|:-----------------:|:------------------:|:------------------:|
| Baseline | 94,67% / 1,96 | 98,45% / 0,74 | 96,26% / 7,67 |
| **NL (Usulan)** | **94,76% / 2,26** | **98,60% / 0,51** | **96,41% / 7,72** |
| **CLIP + NL (Usulan)** | **96,47% / 1,60** | **99,02% / 0,62** | **99,19% / 1,39** |

---

## Kelebihan Penelitian

1. **Mengeliminasi Trade-off Akurasi vs Fairness:** Salah satu dari sedikit metode mitigasi bias yang terbukti mampu meningkatkan akurasi keseluruhan sekaligus menurunkan bias disparitas.
2. **Eksplorasi Ruang Laten GAN Cerdas:** Memanfaatkan kelancaran lokal StyleGAN2 dan faktorisasi SeFA untuk menghasilkan variasi semantik tanpa memerlukan pelabelan manual.
3. **Kuantifikasi Ketidakpastian Teoretis:** Penggunaan Evidential Deep Learning (EDL) memberikan estimasi ketidakpastian yang dapat diandalkan untuk menyaring sampel kritis (*reject option*).
4. **Validasi Skala Luas & Multi-Modalitas:** Diuji pada berbagai arsitektur (EfficientNetV2, CLIP ViT-L/14), 4 dataset wajah, dan 2 dataset biometrik okular.

---

## Keterbatasan Penelitian

1. **Beban Komputasi Pembangkitan GAN:** Mengharuskan proses inversi laten *e4e* dan pembangkitan puluhan variasi gambar via StyleGAN2 yang membutuhkan sumber daya GPU intensif pada tahap pra-pelatihan.
2. **Ketergantungan pada Domain Wajah StyleGAN2:** Kualitas tampilan generatif sangat bergantung pada keberhasilan StyleGAN2 dalam merekonstruksi wajah tanpa distorsi artifaktual.
3. **Fokus pada Tugas Klasifikasi Gender Biner:** Evaluasi difokuskan pada klasifikasi gender biner yang diuji lintas ras, belum memformulasikan klasifikasi interseksional ras dan gender secara bersamaan dalam ruang multi-kelas terpadu.

---

## Future Work (Saran Penelitian Selanjutnya)

1. Mengintegrasikan pembangkitan tampilan tetangga generatif secara *on-the-fly* selama proses pelatihan end-to-end.
2. Menerapkan kerangka kerja mitigasi bias berbasis tampilan generatif pada tugas visi komputer lainnya seperti deteksi *deepfake* dan serangan *biometric spoofing*.
3. Memperluas formulasi ke klasifikasi multi-atribut interseksional simultan (ras, gender, dan usia).

---

## Catatan Penting untuk Riset Kita

### Insight yang Dapat Diadopsi
- **Keunggulan Arsitektur Vision Transformer dalam Fairness:** Eksperimen Ramachandran & Rattani membuktikan bahwa model berbasis Vision Transformer (**CLIP ViT-L/14**) secara inheren memiliki *Degree of Bias* (DoB) yang jauh lebih rendah (0,99–1,10) dibandingkan arsitektur CNN seperti EfficientNetV2 (DoB 1,62–2,01) dan ResNeXt (DoB 1,73). Hal ini menjadi landasan ilmiah yang sangat kuat mengapa penelitian kita memilih **Vision Transformer (ViT)** sebagai fondasi ekstraksi fitur.
- **Kekuatan Fitur Laten Invarian:** Pembelajaran yang mempertahankan konsistensi representasi laten terhadap variasi lokal menghasilkan generalisasi yang superior lintas domain dan dataset.

### Relevansi dengan Kerangka Kerja Multi-Domain ViT (Identity + Emotion + Age) + SVM
- Pada paper Ramachandran & Rattani, tugas dibatasi pada klasifikasi biner gender yang dievaluasi keadilannya lintas 7 ras FairFace.
- Pada penelitian kita, kita melangkah lebih jauh dengan memformulasikan tugas sebagai **klasifikasi interseksional 6-arah langsung (3 Ras × 2 Gender: Asian Females, Asian Males, Black Females, Black Males, White Females, White Males)** pada dataset DemogPairs (10.800 citra seimbang sempurna).
- Pendekatan kita menggabungkan **3 Vision Transformers (ViT-Base)** terpisah (*Identitas/Biometrik via ViT-VGGFace*, *Dinamika Emosi via ViT-Emotion*, dan *Usia Biologis via ViT-Age*) menghasilkan vektor multi-domain 2.304-d.
- Melalui klasifikasi **Support Vector Machine (SVM)** yang dioptimasi via *GridSearchCV* 288 parameter, model kita mencapai akurasi **93,70%** dan F1 **0,9369**, dengan performa yang sangat adil dan konsisten di seluruh kelompok (F1 berkisar 0,9174 hingga 0,9614).

### Hal yang Membedakan Paper Ini dari Penelitian Kita
| Aspek | Ramachandran & Rattani (2023) | Penelitian Kita |
|-------|-------------------------------|-----------------|
| **Tugas Target** | Klasifikasi Gender Biner (Dievaluasi Keadilannya Lintas Ras) | Klasifikasi Interseksional Terpadu 6-Kelas (3 Ras × 2 Gender) |
| **Strategi Fairness** | StyleGAN2 Deep Generative Views (NL) + Evidential Deep Learning (EDL) | Multi-Domain Feature Fusion (3 ViT) + Balanced Intersectional Dataset (DemogPairs) |
| **Ekstraktor Fitur** | Single-backbone (EfficientNetV2-L / CLIP ViT-L/14) | 3 Pre-trained Vision Transformers (ViT-Face, ViT-Emotion, ViT-Age) |
| **Dimensi Fitur** | Feature embedding tunggal per backbone | Concatenated Multi-Domain Latent Embeddings (2.304-d) |
| **Classifier** | SoftMax / Evidential Dirichlet Head | Support Vector Classifier (SVC) dengan GridSearchCV (288 kombinasi) |
| **Dataset** | FairFace (100k) & Cross-dataset (DiveFace, UTKFace, Morph) | DemogPairs (10.800 citra seimbang sempurna 6 kelas) |
| **Hasil Utama** | Akurasi Gender: 95,06%–96,70%, DoB: 0,99–1,62 | **Akurasi 6-Kelas Interseksional: 93,70%**, Macro F1: **0,9369** |
