# II. RELATED WORKS

## A. Demographic Face Recognition

Perkembangan analisis atribut demografis wajah beralih dari deskriptor geometri lokal seperti Local Binary Patterns dan filter Gabor menuju representasi Convolutional Neural Networks (CNN). Pendekatan berbasis region lokal memanfaatkan geometri area wajah bagian tengah untuk mengenali etnisitas sekaligus menekan interferensi latar belakang citra [[11]](06_references.md#ref11). Namun, arsitektur konvolusi klasik rentan terhadap fluktuasi pencahayaan dan disparitas Other-Race Effect. Peningkatan kedalaman arsitektur konvolusi terbukti mampu memperluas daya diskriminasi fitur visual dalam membedakan karakteristik populasi yang heterogen [[13]](06_references.md#ref13). Selain pendalaman lapisan, mekanisme berbagi fitur paralel yang diintegrasikan dengan modul atensi visual dikembangkan untuk menangkap korelasi antaratribut wajah [[16]](06_references.md#ref16). Pendekatan ini memperkuat transisi menuju ekstraksi representasi yang adaptif terhadap morfologi wajah.

Setelah ekstraksi fitur selesai, penentuan pengklasifikasi hilir memegang peranan krusial dalam memetakan representasi laten ke ruang keputusan demografis. Model konvensional umumnya mengandalkan lapisan SoftMax secara end-to-end untuk menghasilkan probabilitas kelas secara langsung [[11]](06_references.md#ref11), [[18]](06_references.md#ref18). Namun, pendekatan pemetaan ruang fitur nonlinier seperti Kernel Extreme Learning Machine (KELM) dan Support Vector Machine (SVM) pada representasi beku menawarkan batas pemisahan kelas yang kokoh tanpa pembaruan bobot backbone [[13]](06_references.md#ref13), [[12]](06_references.md#ref12). Formulasi matematis fungsi keputusan KELM dimodelkan pada [(1)](#eq1):

<a id="eq1"></a>
$$
f(\mathbf{x}) = \mathbf{h}(\mathbf{x})\boldsymbol{\beta} = \sum_{i=1}^M \beta_i K(\mathbf{x}, \mathbf{x}_i) \tag{1}
$$

di mana $\mathbf{h}(\mathbf{x})$ menyatakan pemetaan laten, $\boldsymbol{\beta} = [\beta_1, \dots, \beta_M]^T$ bobot teroptimasi, $K(\mathbf{x}, \mathbf{x}_i)$ fungsi kernel kedekatan nonlinier sampel $\mathbf{x}$ terhadap pendukung $\mathbf{x}_i$, dan $M$ jumlah basis. Pemetaan kernel ini memisahkan batas keputusan nonlinier berdimensi tinggi tanpa optimasi gradien berulang.

## B. Vision Transformers in Face Analysis

Penerapan Vision Transformer (ViT) dalam analisis biometrik wajah menghadirkan pemodelan visual global yang mengatasi bias induktif lokal CNN [[14]](06_references.md#ref14). Citra masukan dipartisi menjadi $N$ patch visual dan diproyeksikan secara linier ke dimensi laten via formulasi [(2)](#eq2):

<a id="eq2"></a>
$$
\mathbf{x}_p \in \mathbb{R}^{N \times (P^2 \cdot C)}, \quad \mathbf{z}_0 = [\mathbf{x}_{\text{class}}; \, \mathbf{x}_p^1\mathbf{E}; \dots; \, \mathbf{x}_p^N\mathbf{E}] + \mathbf{E}_{\text{pos}} \tag{2}
$$

di mana $N = HW/P^2$ menyatakan jumlah patch $P \times P$ pada $C$ kanal, $\mathbf{E} \in \mathbb{R}^{(P^2 \cdot C) \times D}$ matriks proyeksi, $\mathbf{x}_{\text{class}}$ token kelas, dan $\mathbf{E}_{\text{pos}}$ posisi spasial. Interaksi antarpatch dimodelkan via mekanisme Scaled Dot-Product Multi-Head Self-Attention (MHSA) sesuai [(3)](#eq3):

<a id="eq3"></a>
$$
\text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^T}{\sqrt{d_k}}\right)\mathbf{V} \tag{3}
$$

dengan $\mathbf{Q}$, $\mathbf{K}$, dan $\mathbf{V}$ menyatakan matriks Query, Key, dan Value berskala $\sqrt{d_k}$. Mekanisme atensi ini efektif diterapkan pada klasifikasi gender wajah [[17]](06_references.md#ref17), sementara arsitektur multi-aksis seperti MaxViT memperkaya hierarki representasi lewat atensi blok dan kisi [[18]](06_references.md#ref18).

Karakteristik representasi global yang dihasilkan oleh arsitektur transformer mendorong telaah mendalam terkait propagasi bias demografis dalam sistem visi komputer. Pengujian pada korpus data yang seimbang menyediakan kondisi eksperimental terkontrol untuk membandingkan disparitas performa antarsubkelompok tanpa distorsi ketimpangan jumlah sampel kelas. Walaupun distribusi data disetarakan, keseimbangan tersebut tidak secara otomatis meniadakan bias sosial yang melekat pada model. Investigasi representasi laten membuktikan bahwa arsitektur transformer dapat mereproduksi serta melipatgandakan bias sosial yang bersumber dari korpus pra-latih berskala masif [[14]](06_references.md#ref14). Sebagai langkah penanganan ketimpangan tersebut, pendekatan pandangan generatif berbasis StyleGAN2 dimanfaatkan untuk memperkaya keragaman fenotipik antarkelompok demografis [[15]](06_references.md#ref15). Integrasi metode ini membuktikan bahwa pengujian keadilan representasi dan penyelarasan distribusi data sangat krusial dalam perancangan model biometrik wajah modern.

## C. Multi-Domain Feature Fusion

Keterbatasan representasi domain tunggal mendorong perkembangan multi-tugas dan fusi lintas representasi visual. Pembelajaran multi-tugas terbukti efektif dalam memetakan korelasi antara estimasi usia dan klasifikasi gender secara terpadu [[12]](06_references.md#ref12), sedangkan skema berbagi representasi paralel memfasilitasi ekstraksi simultan berbagai atribut afektif wajah [[16]](06_references.md#ref16). Lebih lanjut, eksplorasi penggabungan fitur laten berbasis Vision Transformer memperlihatkan keunggulan integrasi ganda domain biometrik wajah dan ekspresi emosi [[19]](06_references.md#ref19), serta perpaduan fitur biometrik dengan estimasi usia biologis [[20]](06_references.md#ref20). Fusi representasi multi-domain diformulasikan via operasi Direct Sum pada [(4)](#eq4):

<a id="eq4"></a>
$$
\mathbf{z}_{\text{fused}} = \mathbf{z}_{\text{face}} \oplus \mathbf{z}_{\text{emotion}} \oplus \mathbf{z}_{\text{age}} \in \mathbb{R}^{D_{\text{total}}} \tag{4}
$$

di mana $\oplus$ menyatakan konkatenasi langsung representasi biometrik $\mathbf{z}_{\text{face}}$, ekspresi afektif $\mathbf{z}_{\text{emotion}}$, dan usia $\mathbf{z}_{\text{age}}$, berdimensi terakumulasi $D_{\text{total}} = 2.304$. Integrasi ini memadukan identitas statis, ekspresi dinamis, dan penuaan alami.

Mempertimbangkan batasan metodologis pada studi terdahulu, penelitian ini menegaskan posisi kebaruan melalui fusi tri-domain terpadu yang memadukan representasi biometrik wajah, ekspresi emosi afektif, dan usia biologis dari model Vision Transformer pra-latih dengan bobot backbone beku. Berbeda dari literatur sebelumnya yang mengevaluasi performa pada skema pembagian citra acak berisiko kebocoran identitas, kerangka kerja ini dievaluasi secara ketat di bawah protokol Strict Subject-Disjoint Partitioning untuk menjamin keabsahan generalisasi pada subjek yang belum pernah dilihat sebelumnya. Selain itu, kontribusi penelitian ini mencakup eksplorasi sistematis tujuh skema ablasi representasi fitur lintas empat famili pengklasifikasi pembelajaran mesin klasik, optimasi prapemrosesan terisolasi tingkat lipatan bebas kebocoran, serta karakterisasi inferensial formal mengenai fenomena saturasi representasi nonlinier versus komplementaritas linier.
