## B. Vision Transformer

<a id="fig3"></a>
**Figure 3. Redesigned High-Resolution Architecture of the Parallel Multi-Domain ViT Feature Extraction Backbones, Layer-12 CLS Token Extraction, and Direct Sum Feature Concatenation Pipeline.**

![Figure 3. Redesigned High-Resolution Architecture of the Parallel Multi-Domain ViT Feature Extraction Backbones, Layer-12 CLS Token Extraction, and Direct Sum Feature Concatenation Pipeline.](images/vit_v2.2.png)

Arsitektur pengekstraksi representasi visual mengadopsi model Vision Transformer baku Dosovitskiy et al. [[26]](06_references.md#ref26) pada [Figure 3](#fig3). Setiap citra masukan beresolusi 224 × 224 piksel ($C = 3$) dibagi menjadi $N = 196$ patch spasial berukuran $P \times P$ ($P = 16$) [[27]](06_references.md#ref27). Setiap patch diratakan menjadi $\mathbf{x}_p$ lalu diproyeksikan secara linier melalui $\mathbf{E}$ ke ruang laten $D = 768$. Vektor patch dirangkai dengan token kelas $\mathbf{x}_{\text{class}}$ dan embedding posisi $\mathbf{E}_{\text{pos}}$ sesuai [(5)](#eq5) [[27]](06_references.md#ref27). Sekuens token awal $\mathbf{z}_0$ diumpankan ke $L = 12$ lapisan transformer encoder identik. Pada tiap lapisan $\ell$, fitur diproses melalui Multi-Head Self-Attention (MHSA) dan Multi-Layer Perceptron (MLP) beraktivasi Gaussian Error Linear Unit (GeLU) berdasarkan [(6)](#eq6) [[28]](06_references.md#ref28). Mekanisme ini memodelkan relasi spasial global antarpatch wajah tanpa batasan receptive field lokal [[29]](06_references.md#ref29).

<a id="eq5"></a>
$$
\mathbf{z}_0 = [\mathbf{x}_{\text{class}}; \, \mathbf{x}_p^1\mathbf{E}; \dots; \, \mathbf{x}_p^N\mathbf{E}] + \mathbf{E}_{\text{pos}} \tag{5}
$$

<a id="eq6"></a>
$$
\mathbf{z}'_\ell = \text{MHSA}(\text{LN}(\mathbf{z}_{\ell-1})) + \mathbf{z}_{\ell-1}, \quad \mathbf{z}_\ell = \text{MLP}(\text{LN}(\mathbf{z}'_\ell)) + \mathbf{z}'_\ell \tag{6}
$$

Untuk memperoleh representasi visual komplementer, kerangka kerja ini memanfaatkan tiga backbone ViT-Base pra-latih yang dibekukan (frozen weights) secara terpisah. Model pertama merupakan `ViT-Face` (`skutaada/VIT-VGGFace`) pemeta geometri kraniofasial statis berbasis korpus VGGFace2. Model kedua adalah `ViT-Emotion` (`dima806/facial_emotions_image_detection`) pengekstrak dinamika ekspresi afektif berbasis korpus FER-2013. Model ketiga yaitu `ViT-Age` (`dima806/facial_age_image_detection`) pemeta morfologi usia biologis berbasis dataset UTKFace dan IMDB-WIKI. Ketiga model berstruktur ViT-Base/16 dengan dimensi tersembunyi 768 dan 12 lapisan encoder. Citra masukan RGB beresolusi 224 × 224 piksel dinormalisasi secara seragam lewat parameter statistik $\mu = [0.5, 0.5, 0.5]$ dan $\sigma = [0.5, 0.5, 0.5]$. Ekstraksi fitur menerapkan in-memory processor caching tanpa pembaruan bobot (frozen weights) demi menjamin efisiensi komputasi serta reproduktibilitas.

Representasi fitur laten tingkat tinggi diekstraksi dari setiap domain melalui aktivasi token $[\text{CLS}]$ pada lapisan encoder terakhir ($\ell = 12$). Vektor token tersebut distandardisasi melalui operasi Layer Normalization akhir untuk menghasilkan representasi domain teranormalisasi $\mathbf{f}_{\text{domain}} \in \mathbb{R}^{768}$ sesuai perumusan [(7)](#eq7), di mana $\mathbf{z}_{12}^0$ melambangkan token pertama lapisan kedua belas yang diekstraksi tanpa perhitungan gradien. Ketiga representasi domain digabungkan lewat fusi konkatenasi langsung (direct sum) $\oplus$ menjadi representasi tri-domain $\mathbf{z}_{\text{tri}} \in \mathbb{R}^{2304}$ berdasarkan formulasi [(8)](#eq8). Ruang representasi ini memadukan biometrik kraniofasial $\mathbf{f}_{\text{face}}$, ekspresi afektif $\mathbf{f}_{\text{emotion}}$, serta usia biologis $\mathbf{f}_{\text{age}}$. Pengujian ablasi sistematis mencakup tujuh skema fitur: tiga konfigurasi domain tunggal (768 dimensi), tiga domain ganda (1.536 dimensi), dan satu tri-domain (2.304 dimensi) sesuai [Table II](#tab2).

<a id="eq7"></a>
$$
\mathbf{f}_{\text{domain}} = \text{LN}(\mathbf{z}_{12}^0) \in \mathbb{R}^{768} \tag{7}
$$

<a id="eq8"></a>
$$
\mathbf{z}_{\text{tri}} = \mathbf{f}_{\text{face}} \oplus \mathbf{f}_{\text{emotion}} \oplus \mathbf{f}_{\text{age}} \in \mathbb{R}^{2304} \tag{8}
$$

<a id="tab2"></a>
**Table II. Multi-Domain Feature Fusion and Systematic Ablation Configurations.**

| # | Feature Scheme | Category | Input Source Domains | Feature Dimension |
| :---: | :--- | :---: | :--- | :---: |
| 1 | `Face` | Single-Domain | Static Craniofacial Biometrics (`skutaada/VIT-VGGFace`) | 768 |
| 2 | `Emotion` | Single-Domain | Dynamic Affective Expressions (`dima806/facial_emotions_image_detection`) | 768 |
| 3 | `Age` | Single-Domain | Biological Aging Morphology (`dima806/facial_age_image_detection`) | 768 |
| 4 | `Emotion ⊕ Face` | Dual-Domain | Affective Dynamics + Craniofacial Biometrics | 1,536 |
| 5 | `Face ⊕ Age` | Dual-Domain | Craniofacial Biometrics + Aging Morphology | 1,536 |
| 6 | `Emotion ⊕ Age` | Dual-Domain | Affective Dynamics + Aging Morphology | 1,536 |
| 7 | `Face ⊕ Emotion ⊕ Age` | Tri-Domain (Proposed) | Biometrics + Affective Dynamics + Aging Morphology | 2,304 |
