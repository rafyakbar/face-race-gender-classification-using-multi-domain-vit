## B. Vision Transformer

<a id="fig3"></a>
**Figure 3. Architecture of the ViT Backbone and Patch Projection.**

![Figure 3. Architecture of the ViT Backbone and Patch Projection.](images/vit.png)

Arsitektur ekstraksi representasi visual penelitian ini mengadopsi ViT-Base sebagaimana diilustrasikan pada [Figure 3](#fig3) [[26]](06_references.md#ref26). Citra wajah masukan berukuran 224 × 224 piksel dengan 3 saluran warna dibagi menjadi 196 patch spasial non-overlapping $\mathbf{x}_p^i$ berukuran 16 × 16 piksel [[27]](06_references.md#ref27). Setiap patch diproyeksikan secara linier melalui matriks $\mathbf{E}$ ke ruang laten berdimensi $D = 768$, lalu dirangkaikan dengan token kelas $\mathbf{x}_{\text{class}}$ dan embedding posisi $\mathbf{E}_{\text{pos}}$ sesuai [(1)](#eq1) [[27]](06_references.md#ref27). Vektor sekuens token awal $\mathbf{z}_0$ dialirkan ke tumpukan 12 layer transformer encoder identik. Setiap layer encoder $\ell$ memproses masukan $\mathbf{z}_{\ell-1}$ menjadi representasi antara $\mathbf{z}'_\ell$ melalui mekanisme MHSA setelah operasi Layer Normalization (LN) sesuai [(2)](#eq2), yang dilanjutkan menuju representasi luaran $\mathbf{z}_\ell$ melalui blok Multi-Layer Perceptron (MLP) dua lapis beraktivasi GeLU berdasarkan [(3)](#eq3) [[28]](06_references.md#ref28). Mekanisme self-attention memungkinkan pemodelan hubungan global antarpatch wajah tanpa ketergantungan pada receptive field lokal seperti pada operasi konvolusi [[29]](06_references.md#ref29).

<a id="eq1"></a>
$$
\mathbf{z}_0 = [\mathbf{x}_{\text{class}}; \, \mathbf{x}_p^1\mathbf{E}; \, \dots; \, \mathbf{x}_p^{196}\mathbf{E}] + \mathbf{E}_{\text{pos}} \tag{1}
$$

<a id="eq2"></a>
$$
\mathbf{z}'_\ell = \text{MHSA}(\text{LN}(\mathbf{z}_{\ell-1})) + \mathbf{z}_{\ell-1} \tag{2}
$$

<a id="eq3"></a>
$$
\mathbf{z}_\ell = \text{MLP}(\text{LN}(\mathbf{z}'_\ell)) + \mathbf{z}'_\ell \tag{3}
$$

<a id="tab2"></a>
**Table II. Multi-Domain Feature Fusion and Ablation Configurations.**

| # | Configuration | Domain Category | Dimension |
|:---:|---|:---:|:---:|
| 1 | `Face` | Single-Domain | 768 |
| 2 | `Emotion` | Single-Domain | 768 |
| 3 | `Age` | Single-Domain | 768 |
| 4 | `Emotion ⊕ Face` | Dual-Domain | 1,536 |
| 5 | `Face ⊕ Age` | Dual-Domain | 1,536 |
| 6 | `Emotion ⊕ Age` | Dual-Domain | 1,536 |
| 7 | `Face ⊕ Emotion ⊕ Age` | **Tri-Domain (Proposed)** | **2,304** |

Untuk mempertahankan efisiensi komputasi dan mencegah variabilitas pelatihan ulang, ketiga model backbone ViT dibekukan (frozen) sebagai penyedia task-associated representations secara offline. Model ViT-Face (`skutaada/VIT-VGGFace`) menangkap representasi terkait geometri biometrik wajah, ViT-Emotion (`dima806/facial_emotions_image_detection`) menghasilkan representasi terkait ekspresi wajah, dan ViT-Age (`dima806/facial_age_image_detection`) mengekstraksi representasi terkait estimasi usia wajah. Dari setiap model domain, vektor fitur $\mathbf{f}_{\text{domain}} \in \mathbb{R}^{768}$ diekstraksi dari representasi token $[\text{CLS}]$ pada layer encoder terakhir $L$ ($\mathbf{z}_L^0$) setelah operasi LN sesuai [(4)](#eq4). Ketiga representasi laten domain tunggal tersebut digabungkan menjadi vektor fusi tri-domain $\mathbf{z}_{\text{tri}} \in \mathbb{R}^{2304}$ melalui operasi konkatenasi fitur ($\oplus$) dari vektor $\mathbf{f}_{\text{face}}$, $\mathbf{f}_{\text{emotion}}$, dan $\mathbf{f}_{\text{age}}$ sebagaimana dirumuskan pada [(5)](#eq5). Eksplorasi sistematis mencakup tujuh skema ablasi fitur, yang meliputi tiga konfigurasi domain tunggal berdimensi 768, tiga konfigurasi domain ganda berdimensi 1,536, serta satu konfigurasi tri-domain berdimensi 2,304 seperti dirangkum pada [Table II](#tab2).

<a id="eq4"></a>
$$
\mathbf{f}_{\text{domain}} = \text{LN}(\mathbf{z}_L^0) \in \mathbb{R}^{768} \tag{4}
$$

<a id="eq5"></a>
$$
\mathbf{z}_{\text{tri}} = \mathbf{f}_{\text{face}} \oplus \mathbf{f}_{\text{emotion}} \oplus \mathbf{f}_{\text{age}} \in \mathbb{R}^{2304} \tag{5}
$$
