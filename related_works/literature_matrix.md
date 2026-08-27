# Literature Matrix: Face Race & Gender Demographic Recognition and Vision Transformer Fusion

**Tanggal Disusun**: 2026-08-21  
**Total Sumber Aktif**: 10 Paper (2022–2025, Scopus-indexed / WoS / IEEE / Elsevier / MDPI)  
**Tema Utama**: Klasifikasi Ras & Gender Wajah, Mitigasi Bias Demografis, dan Fusi Fitur Multi-Domain Vision Transformer  
**Catatan**: Seluruh tabel menggunakan format terstruktur agar mudah digabungkan dan dirujuk dalam manuskrip publikasi.

---

## Tabel 1a — Informasi Umum

| No | Judul Paper | Tahun | Penulis | Journal / Conference | Publisher | Jenis Paper |
|:--:|-------------|:-----:|---------|----------------------|:---------:|:-----------:|
| 1 | Automatic Ethnicity Classification from Middle Part of the Face Using Convolutional Neural Networks | 2022 | Belcar, Ribarić, & Vrbanovský | Sensors, Vol. 22, Art. 5940 | MDPI | Eksperimen |
| 2 | Face Gender and Age Classification Based on Multi-Task, Multi-Instance and Multi-Scale Learning | 2022 | Liao, Yuan, Wu, Zhong, Jin, & Xiong | Applied Sciences, Vol. 12, Art. 12432 | MDPI | Eksperimen |
| 3 | Intelligent deep learning based ethnicity recognition and classification using facial images | 2022 | Sunitha, Geetha, Neelakandan, Pundir, Hemalatha, & Kumar | Image and Vision Computing, Vol. 121, Art. 104404 | Elsevier | Eksperimen |
| 4 | A Multidimensional Analysis of Social Biases in Vision Transformers | 2023 | Brinkmann, Swoboda, & Bartelt | IEEE/CVF International Conference on Computer Vision (ICCV 2023) | IEEE / CVF | Eksperimen & Analisis Bias |
| 5 | Deep Generative Views to Mitigate Gender Classification Bias Across Gender-Race Groups | 2023 | Ramachandran & Rattani | ICPR 2022 International Workshops and Challenges | Springer Nature | Eksperimen & Mitigasi Bias |
| 6 | Learning an attention-aware parallel sharing network for facial attribute recognition | 2023 | Chen, Lai, Yan, Wang, & Zhu | Journal of Visual Communication and Image Representation, Vol. 90, Art. 103745 | Elsevier | Eksperimen |
| 7 | Classifying Gender Based on Face Images Using Vision Transformer | 2024 | Tahyudin, Sulistiyo, Arzaki, & Rachmawati | International Journal on Informatics Visualization, Vol. 8(1), hlm. 18–25 | Politeknik Negeri Padang | Eksperimen |
| 8 | Ethnicity Classification Based on Facial Images using Deep Learning Approach | 2024 | Kalkatawi & Saeed | International Journal of Advanced Computer Science and Applications, Vol. 15(2), hlm. 217–226 | SAI Organization | Eksperimen |
| 9 | Dual Vision Transformer Integration for Race and Gender Recognition Based on Facial Images | 2025 | Putri, Anifah, Putra, Yamasari, & Akbar | 8th International Conference on Vocational Education and Electrical Engineering (ICVEE 2025) | IEEE | Eksperimen (Prekursor 1) |
| 10 | MD-ViT: Multidomain Vision Transformer Fusion for Fair Demographic Attribute Recognition | 2025 | Putri, Putra, & Yamasari | Journal of Information Engineering and Educational Technology (JIEET), Vol. 9(2), hlm. 64–79 | UNESA | Eksperimen (Prekursor 2) |

---

## Tabel 1b — Dataset yang Digunakan

| No | Judul Paper | Dataset | Status Akses | Jumlah Total Sampel | Partisi Split (Train / Val / Test) | Komposisi Demografis (Ras / Gender / Usia) | Format & Resolusi |
|:--:|-------------|---------|:------------:|:-------------------:|:----------------------------------:|:------------------------------------------:|:-----------------:|
| 1 | Belcar et al. (2022) | UTKFace & FairFace | Public | UTKFace (23.708) & FairFace (86.744) | 80% Train, 20% Test (FairFace: 86.744 train, 10.954 val) | 4 Ras UTKFace (White, Black, Asian, Indian) & 7 Ras FairFace | Cropped Middle Face (Mata-Hidung) vs Full Face |
| 2 | Liao et al. (2022) | MORPH-II & Adience | Academic / Public | MORPH-II (55.132) & Adience (17.603) | 5-Fold Subject-Exclusive CV (Adience) & Standard Split (MORPH) | MORPH: 84,6% Male / 15,4% Female (3 Kelompok Usia); Adience: 8.192 Male / 9.411 Female (8 Kelompok Usia) | 9 Face Patches RGB (Full, Dahi, Mata, Pipi, Hidung, Mulut) |
| 3 | Sunitha et al. (2022) | BUPT-GLOBALFACE | Public | 440.000 citra (subset) | 400.000 Train / 32.000 Val / 8.000 Test (Exam) | 4 Ras Seimbang (Caucasian, African, Asian, Indian — 25% per kelas) | 40 × 40 piksel, Grayscale, Dlib 68 Aligned |
| 4 | Brinkmann et al. (2023) | ImageNet-1K / 21k, iEAT, CIFAR-10 | Public | ImageNet-1K (1,28M + 159k CDA), ImageNet-21k (14,2M), iEAT (15 Tes) | Standard Pre-training & Zero-shot/Linear Probe on CIFAR-10 | 15 Uji Asosiasi Sosial (Ras, Gender, Usia, Skin Tone, Disabilitas, Agama) | 224 × 224, 384 × 384, 512 × 512 RGB |
| 5 | Ramachandran & Rattani (2023) | FairFace, DiveFace, UTKFace, Morph-II, VISOB, UFPR | Public / Academic | FairFace (~100k), DiveFace (150k), UTKFace (20k), Morph (55k) | Train: FairFace 86.744, Val: 10.954, Cross-dataset: DiveFace/UTK/Morph | FairFace: 7 Ras Seimbang, Gender Male/Female; Cross-dataset: Multi-ras | 256 × 256 piksel RGB + Generative Views GAN |
| 6 | Chen et al. (2023) | CelebA & LFWA | Public | CelebA (202.599) & LFWA (13.232) | CelebA: 162.770 Train / 19.962 Val / 19.962 Test; LFWA: 50% Train / 50% Test | 40 Atribut Biner (Male, Young, Pale Skin, Black Hair, Chubby, dll.) | CelebA: 224 × 224 RGB; LFWA: 64 × 64 RGB |
| 7 | Tahyudin et al. (2024) | AFAD & UTKFace | Public | AFAD (165.432) & UTKFace (26.132) | AFAD: 149.000 Train (90%) / 8.276 Val (5%) / 8.275 Test (5%); UTKFace: Full Cross-test | AFAD: Ras Asia Tunggal (15–40 th); UTKFace: 4 Ras, 12 Kelompok Usia (0–116 th) | 160 × 160 & 224 × 224 RGB |
| 8 | Kalkatawi & Saeed (2024) | Merged Dataset (FairFace + UTKFace + Arab Face) | Public | 111.421 citra wajah | 101.474 Train (~91,1%) / 9.947 Test (~8,9%) | 6 Ras: Asian (15,9k), Black (18,6k), Indian (18,1k), Latino (15,0k), Middle Eastern (15,2k), White (28,6k) | 224 × 224 RGB, Center Cropped |
| 9 | Putri et al. (2025 - ICVEE) | DemogPairs | Public (Benchmark) | 10.800 citra wajah | 5-Fold Stratified CV (80% Train: 8.640 / 20% Test: 2.160) | 6 Kelas Interseksional Seimbang Sempurna (1.800 per kelas: Asian/Black/White × Female/Male) | 224 × 224 RGB |
| 10 | Putri et al. (2025 - JIEET) | DemogPairs | Public (Benchmark) | 10.800 citra wajah | 80% Train (8.640 citra untuk 5-Fold CV) / 20% Held-Out Test (2.160 citra) | 6 Kelas Interseksional Seimbang Sempurna (1.800 per kelas: Asian/Black/White × Female/Male) | 224 × 224 RGB (ViT-Age: Grayscale) |

---

## Tabel 2 — Metodologi, Arsitektur, & Classifier

| No | Judul Paper | Ekstraktor Fitur / Backbone | Mekanisme Atensi / Fusi Fitur | Dimensi Representasi | Classifier | Formulasi Tugas |
|:--:|-------------|-----------------------------|-------------------------------|:--------------------:|:----------:|:---------------:|
| 1 | Belcar et al. (2022) | ResNet-50, Inception-v3, VGG-16 | Region Cropping (Mata-Hidung) vs Full Face | Vektor GAP (2.048-d / 512-d) | SoftMax / Dense Layer | Klasifikasi Ras Multi-Kelas (4 Ras UTK / 7 Ras FairFace) |
| 2 | Liao et al. (2022) | MobileNetV3 + CPR (Multi-Scale) | Multi-Instance Fusion (MIF) Atensi Berbobot pada 9 Patches | Concat Instance Features | Gender-Conditional Deep Random Forest (DRF) | Multi-Task Terkondisi (Gender Biner $\rightarrow$ 8 Grup Usia Bersyarat) |
| 3 | Sunitha et al. (2022) | Xception Network (Depthwise Separable) | Global Average Pooling + PCA Feature Reduction | 2.048-d $\rightarrow$ PCA Reduced | Kernel Extreme Learning Machine (KELM) + GSO | Klasifikasi Ras Multi-Kelas (4 Ras Makro) |
| 4 | Brinkmann et al. (2023) | ViT-DINO, ViT-MoCo, ViT-MSN, ViT-MAE, BEiT, iGPT | Multi-Head Self-Attention (MHSA) + Layer-wise Analysis | 768-d (Base), 1024-d (Large), 1280-d (Huge) | Linear Evaluation Probe (Cosine Sim iEAT) | Pengukuran Bias Sosial Representasi Laten (15 Dimensi iEAT) |
| 5 | Ramachandran & Rattani (2023) | EfficientNetV2-L / CLIP ViT-L/14 Vision Tower | StyleGAN2 Deep Generative Views (NL) + JS Divergence Loss | 1.280-d (EfficientNet) / 768-d (CLIP ViT) | SoftMax + Evidential Dirichlet Head (EDL) | Klasifikasi Gender Biner dengan Mitigasi Bias Rasial |
| 6 | Chen et al. (2023) | VGG-16 Shared Backbone (5 Blok Konvolusi) | Parallel Sharing Network (PSN) + Multi-Feature Soft-Alignment (AM) | Multi-Level Concatenation | Multi-Task Linear Layer Head + Adaptive Focal Loss (AFL) | Multi-Label Facial Attribute Recognition (40 Atribut) |
| 7 | Tahyudin et al. (2024) | Vision Transformer (ViT-Base 12 Layers) | Multi-Head Self-Attention (MHSA) pada Patch Embeddings | 768-d Token `[CLS]` | Dense Binary SoftMax Layer | Klasifikasi Gender Biner (Male vs Female) |
| 8 | Kalkatawi & Saeed (2024) | Multi-Axis Vision Transformer (MaxViT) | Max-SA (Window Attention 7×7 + Grid Attention 7×7) + MBConv-SE | 512-d (Hierarchical Output) | Adaptive AvgPool $\rightarrow$ Dense Layer (Tanh) | Klasifikasi Etnisitas Multi-Kelas (6 Kelompok Etnis) |
| 9 | Putri et al. (2025 - ICVEE) | Dual-ViT: ViT-Face (`skutaada/VIT-VGGFace`) + ViT-Emotion (`dima806/facial_emotions`) | Concatenation Laten Multi-Domain (Struktur Statis + Ekspresi Dinamis) | 1.536-d (768 + 768) | Support Vector Machine (SVC) + Grid Search (48 kombinasi) | Klasifikasi Interseksional Terpadu 6-Kelas (3 Ras × 2 Gender) |
| 10 | Putri et al. (2025 - JIEET) | Dual-ViT: ViT-VGGFace (`skutaada/VIT-VGGFace`) + ViT-Age (`dima806/facial_age`) | Concatenation Laten Multi-Domain (Identitas Biometrik + Penuaan Morfologis) | 1.536-d (768 + 768) | eXtreme Gradient Boosting (XGBoost) + 5-Fold Grid Search | Klasifikasi Interseksional Terpadu 6-Kelas (3 Ras × 2 Gender) |

---

## Tabel 3 — Konfigurasi Pelatihan & Komputasi

| No | Judul Paper | Input Resolution | Optimizer | Learning Rate | Batch Size | Epochs / Iterasi | Regularisasi / Parameter Kunci | Hardware / Platform |
|:--:|-------------|:----------------:|:---------:|:-------------:|:----------:|:----------------:|:------------------------------:|:-------------------:|
| 1 | Belcar et al. (2022) | 224 × 224 | Adam | $10^{-4}$ (decay) | 32 / 64 | 50 epoch (Early Stop) | Dropout (0.5), Data Augmentasi (Flip, Zoom) | NVIDIA Titan RTX GPU / TensorFlow |
| 2 | Liao et al. (2022) | 9 Patches (Multiscale) | SGD / Adam | 0,001 | 64 | 6.000 iterasi | DRF Tree Depth=20, Split Interactive=1.500 | Multi-GPU Workstation / PyTorch |
| 3 | Sunitha et al. (2022) | 40 × 40 (Grayscale) | Metaheuristik GSO | N/A (KELM least sq) | N/A | 10-Fold CV Fitness | Metaheuristik Glowworm Swarm Optimization | Python 3.6.5 / TensorFlow / Scikit-learn |
| 4 | Brinkmann et al. (2023) | 224, 384, 512 | Adam | $1,5 \times 10^{-4}$ | 128 | 1 epoch (1-sided CDA) | Stable Diffusion + CLIPSeg Inpainting Masking | Multi-GPU Cluster / PyTorch & Timm |
| 5 | Ramachandran & Rattani (2023) | 256 × 256 | RMSProp | $4 \times 10^{-4}$ (Cosine) | 128 | TD | $\alpha=2$ (JS Div), $m=7$ tetangga, Lazy Reg $n=2$, EDL Threshold=0.2 | 2× NVIDIA RTX 8000 GPU / PyTorch |
| 6 | Chen et al. (2023) | 224 × 224 / 64 × 64 | SGD | 0,001 (Decay 10) | 16 | 15 epoch | $\tau=0,1, \eta=0,1, \gamma=2, \beta=0,25$ (Adaptive Focal Loss) | NVIDIA Titan X GPU / PyTorch |
| 7 | Tahyudin et al. (2024) | 160 × 160 & 224 × 224 | SGD / Adam | 0,001 | 16 / 32 | 100 epoch | 10 Skenario Patch (8 s.d. 32 patch), 12 Layers ViT | Google Colab / PyTorch |
| 8 | Kalkatawi & Saeed (2024) | 224 × 224 | Adadelta | 0,1 (Adaptif) | 20 | 15 epoch | Partition Size $7 \times 7$ (Window & Grid Attention) | Intel i7-6700, 16GB RAM, RTX 3080 (10GB) |
| 9 | Putri et al. (2025 - ICVEE) | 224 × 224 | Grid Search SVM | N/A (Convex Opt) | N/A | 5-Fold CV | $C=2.0$, kernel=`'poly'`, degree=2, $\gamma$=`'scale'`, tol=$10^{-3}$ | NVIDIA GPU / PyTorch & Scikit-Learn |
| 10 | Putri et al. (2025 - JIEET) | 224 × 224 | Grid Search XGBoost | Shrinkage $\eta$ | N/A | 5-Fold CV | `tree_method='hist'`, `max_depth=3`, `min_child_weight=3`, $\gamma=0.0$ | Python 3.10 / XGBoost & Scikit-Learn |

---

## Tabel 4 — Hasil Kuantitatif Benchmark & Fairness

| No | Judul Paper | Dataset Pengujian | Akurasi Global (%) | Precision (%) | Recall (%) | F1-Score (%) | ROC-AUC | Metrik Keadilan / Analisis Bias |
|:--:|-------------|-------------------|:------------------:|:-------------:|:----------:|:------------:|:-------:|:--------------------------------:|
| 1 | Belcar et al. (2022) | UTKFace / FairFace | 80,34% (UTK) / 61,74% (FairFace) | TD | TD | TD | TD | Area mata-hidung mempertahankan ~94% akurasi wajah penuh |
| 2 | Liao et al. (2022) | MORPH-II / Adience | MORPH: Gender 99,6%, Usia 96,1% / Adience: Gender 93,5%, Usia 63,7% | TD | TD | TD | TD | Pengkondisian gender meningkatkan akurasi usia sebesar +8% pada Adience |
| 3 | Sunitha et al. (2022) | BUPT-GLOBALFACE (Exam 8k) | **98,97%** (Rata-rata 5 Runs) | 97,95% | 97,94% | 97,94% | **0,9986** | F1-Score stabil di atas 96,7% pada 4 ras (Asian 98,87%, African 97,28%, Caucasian 97,37%, Indian 98,42%) |
| 4 | Brinkmann et al. (2023) | iEAT 15 Tests (ImageNet-21k) | Linear CIFAR10: 84,8%–95,1% | TD | TD | TD | TD | ViT Diskriminatif (DINO, MoCo) hanya 2–4 bias signifikan vs Generatif (MAE, BEiT) 6–8 bias signifikan |
| 5 | Ramachandran & Rattani (2023) | FairFace Val (7 Ras) | **95,06%** (EffNet) / **96,70%** (CLIP ViT) | TD | TD | TD | TD | DoB turun dari 2,01 ke **1,67** (EffNet) dan **0,99** (CLIP ViT); SeR naik ke **95,87%**; Reject option memangkas DoB ke **1,25** |
| 6 | Chen et al. (2023) | CelebA / LFWA (40 Atribut) | **92,12%** (CelebA) / **86,74%** (LFWA) | TD | TD | TD | TD | Akurasi Male 98,86%, Young 88,42%, Pale Skin 96,91%, Black Hair 91,92%; CAM fokus pada area spesifik |
| 7 | Tahyudin et al. (2024) | AFAD (Same) / UTKFace (Cross) | 98,43% (AFAD) / **81,74%** (UTKFace) | 81,88% | 81,89% | 81,89% | TD | Misklasifikasi ras asal terendah (Asian 20,9%), tertinggi Caucasian (50,4%); Usia produktif 41–50 th optimal (83,24%), anak-anak/lansia error tinggi |
| 8 | Kalkatawi & Saeed (2024) | Merged Dataset (9.947 Test) | **77,20%** (Top-2: **91,30%**) | TD | TD | TD | TD | Black (89,6%), Asian (87,2%), Indian (79,7%), White (71,9%), Latino (60,9%), Middle Eastern (38,5% — overlap tinggi) |
| 9 | Putri et al. (2025 - ICVEE) | DemogPairs (5-Fold CV) | **92,41%** (Test: 92,18%) | 92,00% | 92,00% | 92,00% | **0,9948** | Akurasi subkelompok stabil **0,97–0,98**; F1-score seimbang **0,90–0,95** di seluruh 6 kelas |
| 10 | Putri et al. (2025 - JIEET) | DemogPairs (Held-Out Test 2.160) | **89,07%** (5-Fold CV: 89,81%) | 89,09% | 89,07% | 89,06% | TD | Disparitas F1 sangat rendah (**87,38% s.d. 91,03%**, $\sigma = 1,33\%$, gap 3,65%) |

---

## Tabel 5 — Kelebihan, Keterbatasan, & Future Work

| No | Judul Paper | Kelebihan Utama | Keterbatasan Utama | Saran Penelitian Selanjutnya (Future Work) |
|:--:|-------------|-----------------|--------------------|--------------------------------------------|
| 1 | Belcar et al. (2022) | Membuktikan area mata-hidung sangat diskriminatif untuk ras; menyederhanakan preprocessing tanpa landmark 68 titik. | Akurasi masih tertinggal dibanding citra utuh; performa drop signifikan pada FairFace (61,74%). | Menggabungkan model transformer visual dan memperluas variasi sudut pose wajah. |
| 2 | Liao et al. (2022) | Pemanfaatan dependensi gender-usia via Deep Random Forest; 10× lebih cepat dilatih dibanding RoR; tahan distorsi lokal via 9 patches. | Ketergantungan pada akurasi deteksi ujung hidung; belum melibatkan atribut ras; klasifikasi usia diskret. | Mengintegrasikan atribut ras/etnis dan emosi ke dalam skema multi-task terpadu. |
| 3 | Sunitha et al. (2022) | Pipeline modular terintegrasi (Xception + PCA + KELM); tuning parameter otomatis via GSO; konvergensi sangat cepat tanpa backprop. | Citra diperkecil ke 40×40 grayscale (kehilangan tekstur mikro kulit); terbatas pada 4 ras makro. | Memanfaatkan citra RGB beresolusi tinggi dan memperluas taksonomi etnisitas. |
| 4 | Brinkmann et al. (2023) | Analisis bias multi-dimensi pertama pada ViT; evaluasi empiris 15 tes iEAT; membuktikan ViT diskriminatif lebih adil dari generatif. | CDA via difusi tidak menghilangkan bias secara tuntas dan sedikit menurunkan kualitas representasi hilir. | Mengembangkan teknik post-hoc debiasing pada ruang embedding laten transformer. |
| 5 | Ramachandran & Rattani (2023) | Mengeliminasi trade-off akurasi vs fairness; eksplorasi ruang laten StyleGAN2 (SeFA); kuantifikasi ketidakpastian teoritis via Dirichlet EDL. | Biaya komputasi inversi GAN tinggi; evaluasi difokuskan pada gender biner yang diuji lintas ras. | Menerapkan pembangkitan tetangga generatif on-the-fly dan memperluas ke klasifikasi multi-atribut simultan. |
| 6 | Chen et al. (2023) | Menghubungkan fitur spasial multi-level via Parallel Sharing (PSN); modul atensi soft-alignment; penanganan dinamis class imbalance via AFL. | Backbone masih VGG-16 konvensional; formulasi multi-label biner belum memodelkan interseksionalitas terpadu. | Mengadopsi Vision Transformer sebagai backbone paralel dan pemodelan relasi graf atribut. |
| 7 | Tahyudin et al. (2024) | Evaluasi sistematis 10 skenario resolusi & patch size ViT; analisis cross-dataset mendalam melintasi 4 ras dan 12 kelompok umur. | Melatih model pada ras tunggal (AFAD) memicu penurunan performa tajam lintas ras (~17%) dan rentan pada usia ekstrem. | Melatih model pada dataset multi-ras yang berimbang sempurna dan fusi fitur multi-domain. |
| 8 | Kalkatawi & Saeed (2024) | Penerapan pertama MaxViT (Window + Grid Attention) untuk 6 etnis; database gabungan 111k citra; efisiensi parameter tinggi (30,4M). | Akurasi end-to-end tertahan di 77,2% akibat tumpang tindih visual parah pada kelompok multirasial (Middle Eastern 38,5%). | Mengembangkan fusi fitur multi-domain (emosi/usia) dan klasifikasi berhierarki. |
| 9 | Putri et al. (2025 - ICVEE) | Integrasi 2 domain komplementer (ViT-Face + ViT-Emotion); akurasi 92,41% pada DemogPairs 6-kelas; keadilan subkelompok sangat tinggi. | Belum melibatkan domain penuaan biologis (ViT-Age); ruang pencarian SVM masih terbatas pada 48 kombinasi tanpa scaler/PCA. | Mengintegrasikan domain ketiga (ViT-Age) dan memperluas grid search pipeline. |
| 10 | Putri et al. (2025 - JIEET) | Integrasi 2 domain (ViT-VGGFace + ViT-Age); membuktikan kontribusi positif penuaan; efisiensi pelatihan XGBoost hist-tree (239 s). | Akurasi XGBoost (89,07%) masih di bawah SVM; belum mengikutsertakan domain dinamika emosi wajah. | Mengintegrasikan ketiga domain secara simultan (Face + Emotion + Age) dipadukan dengan SVM optimal. |
