## B. Vision Transformer

<a id="fig3"></a>
![Figure 3. Architecture of Multi-Domain ViT Feature Extraction and Fusion.](images/vit_v2.2.png)
<p align="center"><strong>Figure 3. Architecture of Multi-Domain ViT Feature Extraction and Fusion.</strong></p>

Arsitektur ekstraksi fitur visual mengadopsi model ViT standar yang dipetakan ke dalam alur komputasi pada [Figure 3](#fig3) [[26]](06_references.md#ref26). Pada Tahap (1), citra masukan 224 × 224 piksel ($C = 3$ kanal) diproses, lalu pada Tahap (2) dipartisi menjadi $N = 196$ patch non-overlapping berukuran $P \times P$ ($P = 16$). Patch diratakan menjadi $\mathbf{x}_p \in \mathbb{R}^{P^2 \cdot C}$ dan pada Tahap (3) diproyeksikan via matriks linier $\mathbf{E} \in \mathbb{R}^{(P^2 \cdot C) \times D}$ ke ruang laten $D = 768$. Pada Tahap (4), vektor patch digabungkan dengan token kelas $\mathbf{x}_{\text{class}} \in \mathbb{R}^D$ dan penyandian posisi $\mathbf{E}_{\text{pos}} \in \mathbb{R}^{(N+1) \times D}$ sesuai [(5)](#eq5) [[27]](06_references.md#ref27). Sekuens $\mathbf{z}_0$ dialirkan ke $L = 12$ lapisan transformer encoder, di mana fitur diproses melalui MHSA dan MLP beraktivasi GeLU menurut [(6)](#eq6) [[28]](06_references.md#ref28). Tahap (1) hingga (4) digambarkan satu kali demi efisiensi visual, namun berlangsung secara independen di setiap backbone pada Tahap (5) [[29]](06_references.md#ref29).

<a id="eq5"></a>
$$
\mathbf{z}_0 = [\mathbf{x}_{\text{class}}; \, \mathbf{x}_p^1\mathbf{E}; \dots; \, \mathbf{x}_p^N\mathbf{E}] + \mathbf{E}_{\text{pos}} \tag{5}
$$

<a id="eq6"></a>
$$
\mathbf{z}'_\ell = \text{MHSA}(\text{LN}(\mathbf{z}_{\ell-1})) + \mathbf{z}_{\ell-1}, \quad \mathbf{z}_\ell = \text{MLP}(\text{LN}(\mathbf{z}'_\ell)) + \mathbf{z}'_\ell \tag{6}
$$

Untuk memperoleh representasi visual komplementer, kerangka kerja ini memanfaatkan tiga model backbone ViT-Base pra-latih yang dibekukan (frozen weights), seluruhnya di-fine-tune dari `google/vit-base-patch16-224-in21k`. Model pertama merupakan `ViT-Face` (`skutaada/VIT-VGGFace`, versi `e85f0c9`) hasil fine-tuning korpus VGGFace2 untuk memetakan geometri kraniofasial biometrik statis. Model kedua adalah `ViT-Emotion` (`dima806/facial_emotions_image_detection`, versi `747cf16`) berbasis korpus FER-2013 untuk mengekstraksi ekspresi afektif dinamis. Model ketiga adalah `ViT-Age` (`dima806/facial_age_image_detection`, versi `ad35933`) berbasis korpus gabungan UTKFace dan IMDB-WIKI untuk estimasi penuaan biologis. Seluruh model berstruktur ViT-Base/16 dengan dimensi laten 768 dan 12 lapisan encoder. Citra masukan RGB 224 × 224 piksel diproses melalui `AutoImageProcessor` dengan normalisasi seragam $\mu = \sigma = [0.5, 0.5, 0.5]$ per kanal serta diakselerasi via in-memory processor caching demi efisiensi komputasi dan reproduktibilitas.

<a id="tab2"></a>
**Table II. Multi-Domain Feature Fusion and Systematic Ablation Configurations.**

| # | Feature Scheme | Category | Feature Dimension |
| :---: | :--- | :---: | :---: |
| 1 | `Face` | Single-Domain | 768 |
| 2 | `Emotion` | Single-Domain | 768 |
| 3 | `Age` | Single-Domain | 768 |
| 4 | `Emotion ⊕ Face` | Dual-Domain | 1,536 |
| 5 | `Face ⊕ Age` | Dual-Domain | 1,536 |
| 6 | `Emotion ⊕ Age` | Dual-Domain | 1,536 |
| 7 | `Face ⊕ Emotion ⊕ Age` | Tri-Domain (Proposed) | 2,304 |

Pada Tahap (5), representasi fitur laten tingkat tinggi diekstraksi secara paralel dari ketiga backbone ViT yang dibekukan melalui aktivasi token kelas $[\text{CLS}]$ pada lapisan encoder terakhir ($\ell = 12$). Vektor keluaran distandardisasi via Layer Normalization akhir untuk menghasilkan representasi $\mathbf{f}_{\text{domain}} \in \mathbb{R}^{768}$ sesuai [(7)](#eq7), dengan $\mathbf{z}_{12}^0$ menyatakan token pertama lapisan ke-12 tanpa pembaruan gradien. Selanjutnya, pada Tahap (6), ketiga representasi digabungkan melalui fusi konkatenasi langsung $\oplus$ menjadi vektor tri-domain $\mathbf{z}_{\text{tri}} \in \mathbb{R}^{2304}$ berdasarkan [(8)](#eq8) yang memadukan informasi kraniofasial $\mathbf{f}_{\text{face}}$, afektif $\mathbf{f}_{\text{emotion}}$, dan usia biologis $\mathbf{f}_{\text{age}}$. Representasi ini diteruskan ke Tahap (7) untuk klasifikasi hilir enam kelas interseksional. Kebaruan metodologis difokuskan pada kerangka evaluasi fusi multi-domain komplementer yang efisien tanpa komputasi fine-tuning ulang, yang diuji secara sistematis melintasi tujuh konfigurasi fitur pada [Table II](#tab2).

<a id="eq7"></a>
$$
\mathbf{f}_{\text{domain}} = \text{LN}(\mathbf{z}_{12}^0) \in \mathbb{R}^{768} \tag{7}
$$

<a id="eq8"></a>
$$
\mathbf{z}_{\text{tri}} = \mathbf{f}_{\text{face}} \oplus \mathbf{f}_{\text{emotion}} \oplus \mathbf{f}_{\text{age}} \in \mathbb{R}^{2304} \tag{8}
$$
