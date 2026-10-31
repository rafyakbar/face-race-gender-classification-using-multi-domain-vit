# Panduan Referensi Utama AI Agent: Klasifikasi Interseksional Ras & Gender Wajah Berbasis Multi-Domain Vision Transformer Feature Fusion

> **Pemberitahuan Penting untuk AI Agent:** Berkas ini (`README.ai.md`) merupakan *single source of truth* otoritatif yang mandiri (*self-contained*) dan manual operasional komprehensif untuk repositori penelitian ini. Setiap AI agent yang berinteraksi dengan proyek ini diwajibkan membaca dokumen ini guna memahami konteks menyeluruh, latar belakang riset, arsitektur model, spesifikasi dataset, protokol ekstraksi fitur, *dual 28-model experimental benchmark* (*Subject-Disjoint Primary Benchmark* vs. *Subject-Overlap Historical Baseline*), *dossier* resmi peer review IEEE Access, artefak kepatuhan *submission*, utilitas basis kode, alur kerja reproduksi, serta aturan penulisan ilmiah tanpa perlu mengeksplorasi atau merekonstruksi konteks dari berkas-berkas terpisah.

---

## 📑 Daftar Isi

1. [Ringkasan Eksekutif & Identitas Manuskrip](#1-ringkasan-eksekutif--identitas-manuskrip)
2. [Perjalanan Publikasi Terkini & Dossier Peer Review (`paper_reviews_ieee/`)](#2-perjalanan-publikasi-terkini--dossier-peer-review-paper_reviews_ieee)
3. [Arsitektur Penelitian & Pipeline Metodologi](#3-arsitektur-penelitian--pipeline-metodologi)
4. [Spesifikasi Dataset, Encoding Label & Protokol Dual Partitioning](#4-spesifikasi-dataset-encoding-label--protokol-dual-partitioning)
5. [Ekstraksi Fitur & 7 Skema Ablasi](#5-ekstraksi-fitur--7-skema-ablasi)
6. [Pipeline Classifier Klasik & Optimasi GridSearchCV Lengkap](#6-pipeline-classifier-klasik--optimasi-gridsearchcv-lengkap)
7. [Benchmark Eksperimental Ganda Komprehensif](#7-benchmark-eksperimental-ganda-komprehensif)
   - 7.1 [Leaderboard Utama: Subject-Disjoint Leaderboard (28 Model)](#71-leaderboard-utama-subject-disjoint-leaderboard-28-model)
   - 7.2 [Leaderboard Historis: Subject-Overlap Leaderboard (28 Model)](#72-leaderboard-historis-subject-overlap-leaderboard-28-model)
   - 7.3 [Ablasi Komparatif Data Leakage & Analisis Generalisasi](#73-ablasi-komparatif-data-leakage--analisis-generalisasi)
   - 7.4 [Pengujian Hipotesis Inferensial & Signifikansi Statistik (Paired McNemar Tests)](#74-pengujian-hipotesis-inferensial--signifikansi-statistik-paired-mcnemar-tests)
8. [Performa Subkelompok Interseksional, Confusion Matrix & Profil Fairness](#8-performa-subkelompok-interseksional-confusion-matrix--profil-fairness)
9. [Perbandingan dengan Studi Terdahulu pada DemogPairs & Literatur](#9-perbandingan-dengan-studi-terdahulu-pada-demogpairs--literatur)
10. [Arsitektur Repositori & Inventaris Berkas](#10-arsitektur-repositori--inventaris-berkas)
11. [Kepatuhan Submission & Paket Unggahan (`paper_submission/` & `upload/`)](#11-kepatuhan-submission--paket-unggahan-paper_submission--upload)
12. [Suite Mock Peer Review Internal (`paper_reviews/`) & Agent Skills (`.agents/skills/`)](#12-suite-mock-peer-review-internal-paper_reviews--agent-skills-agentsskills)
13. [Referensi Pustaka Utilitas Python (`experiment/code/utils/`)](#13-referensi-pustaka-utilitas-python-experimentcodeutils)
14. [Alur Kerja Eksekusi, Reproduksi & Kompilasi Manuskrip](#14-alur-kerja-eksekusi-reproduksi--kompilasi-manuskrip)
15. [Batasan Klaim Ilmiah & Direktif Penulisan Akademik (28 Aturan/Direktif)](#15-batasan-klaim-ilmiah--direktif-penulisan-akademik-28-aturandirektif)
16. [Profil Penulis Utama, Provenance Akademik & Metadata Sitasi](#16-profil-penulis-utama-provenance-akademik--metadata-sitasi)
17. [Riwayat Sesi Kerja AI Agent & Log Kronologis (`docs/sessions/`)](#17-riwayat-sesi-kerja-ai-agent--log-kronologis-docssessions)

---

## 1. Ringkasan Eksekutif & Identitas Manuskrip

### 1.1 Metadata Inti
- **Judul Repositori / Direktori Kerja:** `face-race-gender-multi-vit` (`D:\Research\face-race-gender-multi-vit`)
- **Penulis Utama Korpus:** Dr. Ir. Ricky Eka Putra, S.Kom., M.Kom. (Corresponding Author, `rickyeka@unesa.ac.id`), Rezky Arisanti Putri, S.Kom., M.Kom., Dr. Yuni Yamasari, S.Kom., M.Kom., Rafy Aulia Akbar, S.Kom., M.Kom.
- **Afiliasi:** Departemen Informatika, Fakultas Informatika, Universitas Negeri Surabaya (UNESA), Surabaya, Jawa Timur, Indonesia.
- **Jurnal Target:** **IEEE Access** (Open Access, Q1, Impact Factor: 3.4).
- **ID Pelacakan Resmi Manuskrip:** **`Access-2026-50857`**.
- **Judul Manuskrip:** *Multi-Domain Vision Transformer Fusion for Intersectional Demographic Classification from Facial Images*.
- **Milestone Terkini:** Keputusan Editorial Diterima pada **20 Oktober 2026** (Hasil Review Biner: *Reject & Resubmit* dengan tepat 1 kesempatan *resubmission* yang diberikan).
- **Tujuan Milestone Utama:** Resolusi tuntas terhadap Komentar #2 Reviewer 2 mengenai *identity overlap* dan generalisasi lintas-subjek melalui arsitektur *dual-benchmark*.

### 1.2 Paradigma Penelitian Inti
Penelitian ini mengusulkan sebuah kerangka kerja *offline feature fusion* untuk klasifikasi atribut demografis interseksional 6 kelas (3 Ras × 2 Gender: Asian/Black/White × Female/Male) dari citra wajah. Sistem mengekstraksi representasi laten terasosiasi tugas (*task-associated latent representations*) dari tiga *backbone* Vision Transformer (ViT-Base) terspesialisasi yang telah dilatih sebelumnya (*pre-trained*) dan dibekukan (*frozen*):
1. **ViT-Face** (`skutaada/VIT-VGGFace`): Menangkap biometrik kraniofasial statis dan geometri spasial yang berkaitan dengan identitas.
2. **ViT-Emotion** (`dima806/facial_emotions_image_detection`): Menangkap ekspresi afektif dinamis dan *facial action units* terdelokalisasi.
3. **ViT-Age** (`dima806/facial_age_image_detection`): Menangkap morfologi penuaan biologis dan pola tekstur epidermal.

Vektor token `[CLS]` tingkat tinggi (768-d per domain) digabungkan (*concatenated*) menjadi **representasi Tri-Domain** ($\mathbf{z}_{\text{tri}} \in \mathbb{R}^{2304}$) dan diumpankan ke *classifier* klasik hilir yang dioptimasi secara menyeluruh melalui 5-Fold Stratified GridSearchCV (mengevaluasi 1.086 kombinasi *hyperparameter* dan total 38.010 *cross-validation fits* pada 4 famili *classifier*: SVM, Logistic Regression, Random Forest, dan Gaussian Naive Bayes).

### 1.3 Arsitektur Dual Benchmark & Pencapaian Utama

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                   DEMOGPAIRS DATASET                                   │
│                 10.800 Citra Wajah │ 600 Subjek Unik (18 citra/subjek)                 │
│                 6 Kelas Interseksional (1.800 citra per kelas demografi)               │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │
                    ┌───────────────────────┴───────────────────────┐
                    ▼                                               ▼
┌───────────────────────────────────────┐       ┌───────────────────────────────────────┐
│       PRIMARY BENCHMARK REVISION      │       │     HISTORICAL BASELINE ARCHIVE       │
│      (Subject-Disjoint Partition)     │       │       (Subject-Overlap Split)         │
│ ───────────────────────────────────── │       │ ───────────────────────────────────── │
│ • 480 Subjek Latih (8.640 citra)      │       │ • Partisi acak 80/20 level citra      │
│ • 120 Subjek Uji Held-Out (2.160 ctra)│       │ • 593/593 subjek tumpang-tindih di uji│
│ • Identity Leakage: 0.00% (Nol)       │       │ • Identity Leakage: 100.00%           │
│ • Terbaik: LR Tri (88.66%)/SVM(88.61%)│       │ • Terbaik: SVM Tri (93.70%)           │
│ • Lokasi: experiment/code/results/    │       │ • Lokasi: experiment/code/archive/    │
└───────────────────────────────────────┘       └───────────────────────────────────────┘
```

1. **Primary Benchmark: Subject-Disjoint Partitioning (Zero Identity Leakage — Tonggak Revisi IEEE Access):**
   - **Model Performa Puncak:** **Logistic Regression (LR) + Tri-Domain ViT Fusion** (`vit-face-emotion-age`, 2.304-d)
     - **Test Accuracy:** **88.66%** (1.915 prediksi benar dari 2.160 sampel uji *held-out* dari 120 subjek tak terlihat).
     - **Macro Precision:** **0.8875** | **Macro Recall:** **0.8866** | **Macro F1-Score:** **0.8868**
     - **95% Wilson Score CI:** **[87.25%, 89.93%]**
     - **Inference Latency:** **0.0054 ms/sampel** (>800x lebih cepat dibanding SVM)
     - **Penyimpanan Model:** **0.11 MB** (>330x lebih ringkas dibanding SVM)
     - **Hyperparameter Terbaik:** $C = 0.1$, solver = `'saga'`, max_iter = 500, Scaler = `'MinMaxScaler'`, PCA = `None`.
   - **Model Runner-Up:** **Support Vector Machine (SVM) + Tri-Domain ViT Fusion** (`vit-face-emotion-age`, 2.304-d)
     - **Test Accuracy:** **88.61%** (1.914 prediksi benar dari 2.160 sampel uji).
     - **Macro Precision:** **0.8871** | **Macro Recall:** **0.8861** | **Macro F1-Score:** **0.8863**
     - **95% Wilson Score CI:** **[87.20%, 89.88%]**
     - **Hyperparameter Terbaik:** $C = 10$, kernel = `'rbf'`, gamma = `'scale'`, Scaler = `'MinMaxScaler'`, PCA = `None`.
   - **Ekuivalensi Statistik (LR vs. SVM):** Paired McNemar test mengonfirmasi $p = 1.0000$ (keuntungan bersih +1 citra), membuktikan paritas performa prediktif yang setara secara statistik sementara LR memberikan keunggulan komputasi tepi (*edge computing*) yang sangat dominan.
   - **Dominasi Tri-Domain:** Fusi tri-domain meraih performa puncak pada **3 dari 4 classifier** di bawah kondisi *subject-disjoint* (LR: 88.66%, SVM: 88.61%, RF: 85.00%). GNB mencapai puncak pada dual-domain `Emotion ⊕ Face` (84.31%).

2. **Historical Benchmark: Subject-Overlap Baseline (Baseline 100% Identity Leakage):**
   - **Konfigurasi Performa Puncak:** **Support Vector Machine (SVM) + Tri-Domain ViT Fusion**
     - **Test Accuracy:** **93.70%** (2.024 prediksi benar dari 2.160 sampel uji *held-out*).
     - **Macro Precision:** **0.9372** | **Macro Recall:** **0.9370** | **Macro F1-Score:** **0.9369**
     - **Hyperparameter Terbaik:** $C = 10$, kernel = `'poly'`, degree = 2, gamma = `'scale'`, Scaler = `None`, PCA = `None`.
   - **Peran dalam Revisi:** Dipertahankan secara utuh untuk memberikan landasan empiris bagi **Seksi IV Manuskrip: Analisis Komparatif Data Leakage & Generalisasi**, yang secara langsung menuntaskan Komentar #2 Reviewer 2 IEEE Access.

3. **Temuan Komparatif Inti:**
   Penurunan akurasi nominal sebesar ~4.0% hingga 5.1% pada subjek tak terlihat (93.70% $\to$ 88.61% pada SVM; 92.73% $\to$ 88.66% pada LR) secara empiris menguantifikasi besaran biaya memorisasi identitas (*identity memorization*). Yang terpenting, **pengujian hipotesis Paired McNemar membuktikan bahwa fusi multi-domain ViT tetap unggul secara signifikan secara statistik dibandingkan biometrik wajah domain tunggal ($p = 3.46 \times 10^{-6} < 0.001$ pada SVM; $p = 6.78 \times 10^{-6} < 0.001$ pada LR)**, mengonfirmasi bahwa peningkatan dari fusi multi-domain bersifat riil dan dapat digeneralisasikan lintas identitas baru yang belum pernah dilihat model sebelumnya.

---

## 2. Perjalanan Publikasi Terkini & Dossier Peer Review (`paper_reviews_ieee/`)

Manuskrip ini diajukan secara resmi ke IEEE Access dan memperoleh surat keputusan editorial resmi pada 20 Oktober 2026. Seluruh berkas *dossier* proses peer review dikurasi secara terstruktur di dalam direktori [`paper_reviews_ieee/`](paper_reviews_ieee/).

### 2.1 Ringkasan Keputusan Editorial
- **Associate Editor:** Dr. Vincenzo Conti (`vincenzo.conti@unikore.it`, `vinc.conti@gmail.com`).
- **Article Administrator:** Mr. Adesh Choudhary (`adesh.choudhary@ieee.org`).
- **Tanggal Keputusan:** 20-10-2026.
- **Tipe Keputusan:** Ditolak di bawah model peer review biner IEEE Access (*Reject & Resubmit*), disertai undangan eksplisit untuk mengajukan kembali manuskrip yang telah direvisi.
- **Kesempatan Pengajuan Ulang:** Tepat **SATU** kesempatan *resubmission* yang diperbolehkan.
- **URL Portal Resubmission:** [IEEE Author Portal Resubmission Board](https://ieee.atyponrex.com/journal/ieee-access).

### 2.2 Berkas Terkurasi di `paper_reviews_ieee/`
| Berkas | Path | Peran & Konten |
|---|---|---|
| **Editorial Decision & Reviews** | [`IEEE-Access_Decision-on-Manuscript-ID-Access-2026-50857.md`](paper_reviews_ieee/IEEE-Access_Decision-on-Manuscript-ID-Access-2026-50857.md) | Surat keputusan resmi, tautan pengajuan, 3 berkas wajib, komentar Reviewer 1 (7 poin) & Reviewer 2 (10 poin) beserta kuesioner evaluasi. |
| **Response to Reviewers Template** | [`IEEE-Access_Response-to-Reviewers-template.md`](paper_reviews_ieee/IEEE-Access_Response-to-Reviewers-template.md) | Struktur standar respons IEEE Access: tanggapan poin-demi-poin terhadap komentar reviewer, respons penulis, dan tindakan perbaikan yang diambil. |
| **Request for Byline Change** | [`Request-for-Byline-Change.md`](paper_reviews_ieee/Request-for-Byline-Change.md) | Formulir resmi dan justifikasi rinci yang diwajibkan apabila terjadi perubahan daftar/urutan penulis antara pengajuan awal dan revisi. |
| **Resubmission Checklist** | [`Resubmission-Checklist.md`](paper_reviews_ieee/Resubmission-Checklist.md) | Daftar periksa kepatuhan 10 poin: respons reviewer, alat bantu tata bahasa, formula matematika, referensi, PDF tersorot (*highlighted PDF*), dan berkas utama. |

### 2.3 Dekonstruksi Rinci Komentar Reviewer

#### Reviewer 1 (Acceptable with Revisions; 7 Komentar Inti)
1. **Panjang Bab Pendahuluan:** Perketat Seksi I agar alur fokus tulisan lebih terarah.
2. **Kajian Literatur & Formulasi Matematika:** Susun Seksi II dengan struktur yang lebih baik dan integrasikan formulasi matematika formal.
3. **Perancangan Ulang Gambar 3:** Rancang ulang diagram arsitektur ViT pada Gambar 3 agar visualisasi proyeksi *patch* dan ekstraksi fitur terartikulasi secara lebih jelas.
4. **Pendalaman Diskusi Gambar 4:** Perdalam diskusi empiris seputar interpretasi representasi visual fitur.
5. **Detail Eksperimen & Biaya Komputasi:** Laporkan waktu komputasi/eksekusi, spesifikasi dataset mendalam, dan kontribusi konkret penelitian.
6. **Perbandingan Metode Lebih Luas:** Bingkai perbandingan terhadap baseline literatur secara metodologis dan kontekstual yang ketat.
7. **Bab Kesimpulan:** Revisi Seksi V untuk merefleksikan kontribusi nyata penelitian secara padat dan akurat.

#### Reviewer 2 (Substantial Methodological & Statistical Scrutiny; 10 Komentar Inti)
1. **Kebaruan & Kontribusi Metodologi:** Perjelas kontribusi metodologis fusi fitur tri-domain dibandingkan sekadar konkatenasi vektor sederhana.
2. **Data Leakage & Generalisasi Subject-Disjoint:** **(PERHATIAN KRITIS / CRITICAL CONCERN)** Mempertanyakan apakah citra dari identitas yang sama muncul di kedua partisi latih dan uji akibat pembagian acak (*random splitting*); meminta evaluasi di bawah kondisi *subject-disjoint* yang ketat.
3. **Pra-pemrosesan & Reproduksibilitas:** Sebutkan *checkpoint identifier* resmi HuggingFace, parameter *image processor*, dan prosedur normalisasi secara presisi.
4. **Konsistensi Ruang Pencarian Hyperparameter:** Rekonsiliasikan metrik ruang pencarian yang dilaporkan (1.086 kombinasi, 38.010 *cross-validation fits*, 28 *final refits*).
5. **Signifikansi Statistik & Uji McNemar:** Laporkan pengujian hipotesis statistik inferensial (uji McNemar) untuk memvalidasi perbedaan performa dan menguji klaim keunggulan tri-domain secara sahih.
6. **Cakupan Analisis Keadilan (Fairness):** Perbaiki cakupan klaim keadilan; tegaskan bahwa EOD memberikan wawasan disparitas subkelompok namun bukan audit keadilan algoritmik yang komprehensif/lengkap.
7. **Kondisi Benchmark Baseline Literatur:** Perjelas apakah metode-metode terdahulu yang dievaluasi pada DemogPairs menggunakan partisi identik; perlakukan perbandingan tersebut secara kontekstual.
8. **Profil Efisiensi Komputasi:** Laporkan latensi ekstraksi fitur, waktu pelatihan classifier, latensi inferensi per sampel, konsumsi memori, dan ukuran berkas model pada disk penyimpanan.
9. **Interpretasi Tumpang Tindih Fenotipik & Visual:** Kualifikasi pernyataan terkait *overlap* fenotipik dan pola penuaan biologis secara hati-hati.
10. **Batasan & Cakupan Kesimpulan:** Batasi kesimpulan secara eksplisit hanya pada kategori demografi yang tersedia di dalam DemogPairs.

---

## 3. Arsitektur Penelitian & Pipeline Metodologi

```
                             [ Citra Masukan Wajah: 224x224 RGB ]
                                               │
             ┌─────────────────────────────────┼─────────────────────────────────┐
             ▼                                 ▼                                 ▼
       [ ViT-Face ]                     [ ViT-Emotion ]                    [ ViT-Age ]
    (skutaada/VIT-VGGFace)        (dima806/facial_emotions...)        (dima806/facial_age...)
       Token [CLS] 768-d                 Token [CLS] 768-d                 Token [CLS] 768-d
             │                                 │                                 │
             └─────────────────────────────────┼─────────────────────────────────┘
                                               ▼
                        [ Konkatenasi Fitur: z_tri in R^2304 ]
                                               │
                                               ▼
                      [ Pipeline Preprocessing: Scaler + PCA (Fold-level) ]
                                               │
                                               ▼
                     [ 5-Fold Stratified Subject-Disjoint GridSearchCV ]
                       (Logistic Regression / SVM / Random Forest / GNB)
                                               │
                                               ▼
                      [ Klasifikasi Interseksional 6-Kelas pada DemogPairs ]
                (Asian_Females, Asian_Males, Black_Females, Black_Males, White_Females, White_Males)
```

### 3.1 Mekanisme Ekstraksi Fitur Vision Transformer
Ketiga model dibangun berdasarkan arsitektur **ViT-Base (`vit-base-patch16-224`)**:
- **Pemrosesan Masukan:** Citra RGB berukuran $224 \times 224 \times 3$ dipartisi menjadi $N = 196$ *patch* non-tumpang tindih ($P = 16 \times 16$).
- **Proyeksi Patch Linear:** Masing-masing *patch* diratakan ($\mathbf{x}_p^i \in \mathbb{R}^{768}$) dan diproyeksikan secara linear melalui matriks $\mathbf{E} \in \mathbb{R}^{(P^2C) \times D}$ ke dimensi tersembunyi $D = 768$.
- **Penambahan Token CLS & Position Embedding:**
  $$\mathbf{z}_0 = [\mathbf{x}_{\text{class}}; \, \mathbf{x}_p^1\mathbf{E}; \, \mathbf{x}_p^2\mathbf{E}; \, \dots; \, \mathbf{x}_p^{196}\mathbf{E}] + \mathbf{E}_{\text{pos}}, \quad \mathbf{E}_{\text{pos}} \in \mathbb{R}^{(N+1) \times D}$$
- **Blok Encoder (12 Lapisan):** Setiap lapisan terdiri atas Multi-Head Self-Attention (MHSA, 12 *heads*) dan Multi-Layer Perceptron (MLP) dengan Layer Normalization (LN):
  $$\mathbf{z}'_\ell = \text{MHSA}(\text{LN}(\mathbf{z}_{\ell-1})) + \mathbf{z}_{\ell-1}$$
  $$\mathbf{z}_\ell = \text{MLP}(\text{LN}(\mathbf{z}'_\ell)) + \mathbf{z}'_\ell, \quad \ell = 1, \dots, 12$$
- **Ekstraksi Fitur Akhir:** Parameter *backbone* dibekukan (*frozen*); vektor fitur diekstraksi dari representasi token `[CLS]` ternormalisasi ($\mathbf{z}_L^0$) dari lapisan *encoder* terakhir $L = 12$:
  $$\mathbf{f}_{\text{domain}} = \text{LayerNorm}(\mathbf{z}_L^0) \in \mathbb{R}^{768}$$

### 3.2 Spesifikasi Backbone ViT
| Backbone | Identifier HuggingFace | Tugas & Domain Pre-training | Isyarat Visual Representasi |
|---|---|---|---|
| **ViT-Face** | `skutaada/VIT-VGGFace` | Rekognisi Biometrik Wajah (VGGFace) | Struktur tulang kraniofasial, jarak antar-okular, proporsi statis wajah |
| **ViT-Emotion** | `dima806/facial_emotions_image_detection` | Deteksi Keadaan Afektif & Ekspresi Wajah | Mikroekspresi dinamis, aktivasi otot di sekitar mulut, alis, dan mata |
| **ViT-Age** | `dima806/facial_age_image_detection` | Estimasi Usia Biologis Wajah | Elastisitas epidermal, lipatan nasolabial, kerutan periokular, morfologi penuaan |

---

## 4. Spesifikasi Dataset, Encoding Label & Protokol Dual Partitioning

### 4.1 Dataset Benchmark: DemogPairs
- **Sitasi Primer:** I. Hupont and C. Fernández, "DemogPairs: Quantifying the Impact of Demographic Imbalance in Deep Face Recognition," *IEEE FG 2019*, DOI: `10.1109/FG.2019.8756625`.
- **Komposisi Dataset:** 10.800 citra wajah dari 600 subjek/identitas unik (100 subjek per kelompok demografi, 18 citra beresolusi tinggi per subjek).
- **Keseimbangan Kelas:** Terdistribusi seimbang sempurna (*perfectly balanced*) di seluruh 6 subkelompok demografi interseksional (masing-masing 1.800 citra).

### 4.2 Encoding Label
- **`DEMOGPairs_LABEL_TO_IDX` (pada [`experiment/code/utils/constants.py`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/utils/constants.py)):**
  - `Black_Males`: `0` | `White_Females`: `1` | `Asian_Males`: `2` | `White_Males`: `3` | `Black_Females`: `4` | `Asian_Females`: `5`
- **Urutan Kelas Menurut Abjad (`DEMOGPairs_CLASSES`):**
  `['Asian_Females', 'Asian_Males', 'Black_Females', 'Black_Males', 'White_Females', 'White_Males']`
- **Penyelarasan Evaluasi:** Pada modul `utils/evaluation.py`, matriks konfusi (*confusion matrix*) dan *classification report* secara eksplisit memetakan indeks kelas menggunakan argumen `labels=[DEMOGPairs_LABEL_TO_IDX[n] for n in target_names]` guna mencegah inversi sumbu metrik.

### 4.3 Spesifikasi Protokol Dual Partitioning

#### Protokol A: Strict Subject-Disjoint Partitioning (Primary Benchmark — Tonggak Revisi)
- **Implementasi:** Fungsi `split_demogpairs_subject_disjoint` pada modul `utils/dataset.py`.
- **Pembagian Subjek:** 600 subjek unik dipartisi secara ketat berdasarkan identitas individu:
  - **Data Latih (Training Set):** 80 subjek per kelas $\times$ 6 kelas = **480 subjek unik** ($N = 8.640$ citra; 1.440 citra per kelas).
  - **Data Uji Held-Out (Test Set):** 20 subjek per kelas $\times$ 6 kelas = **120 subjek unik** ($N = 2.160$ citra; 360 citra per kelas).
- **Identity Overlap:** **0.00% (Nol / Zero Leakage)**. Tidak ada satu pun identitas subjek pada partisi uji yang pernah muncul pada data latih.
- **Cross-Validation:** 5-Fold Stratified Group K-Fold dieksekusi secara ketat hanya di dalam batasan 480 subjek latih.
- **Lokasi Artefak Aktif:** Jupyter Notebook di `experiment/code/`, model tersimpan di `experiment/code/models/`, berkas hasil evaluasi di `experiment/code/results/`.

#### Protokol B: Subject-Overlap Partitioning (Historical Baseline — Data Leakage Ablation)
- **Implementasi:** Pembagian acak bertingkat pada level citra (`train_test_split(..., test_size=0.2, random_state=42, stratify=y)`).
- **Identity Overlap:** **100.00%**. Seluruh 593 identitas subjek pada data uji turut muncul pada data latih dalam variasi pose/pencahayaan yang berbeda.
- **Lokasi Artefak Arsip:** Seluruh suite historis dipreservasi secara utuh di dalam `experiment/code/archive/` (`notebook_old/`, `models_old/`, `results_old/`, `md_old/`, `audit_ledger.json`).

---

## 5. Ekstraksi Fitur & 7 Skema Ablasi

### 5.1 Taksonomi Ablasi
| Indeks Skema | Nama Skema Fitur | Kategori | Dimensionalitas | Formulasi Konkatenasi |
|:---:|---|:---:|:---:|---|
| 1 | `vit-age` | Single-Domain | 768 | $\mathbf{z} = \mathbf{f}_{\text{age}} \in \mathbb{R}^{768}$ |
| 2 | `vit-emotion` | Single-Domain | 768 | $\mathbf{z} = \mathbf{f}_{\text{emotion}} \in \mathbb{R}^{768}$ |
| 3 | `vit-face` | Single-Domain | 768 | $\mathbf{z} = \mathbf{f}_{\text{face}} \in \mathbb{R}^{768}$ |
| 4 | `vit-emotion-age` | Dual-Domain | 1.536 | $\mathbf{z} = [\mathbf{f}_{\text{emotion}} \,\|\, \mathbf{f}_{\text{age}}] \in \mathbb{R}^{1536}$ |
| 5 | `vit-face-age` | Dual-Domain | 1.536 | $\mathbf{z} = [\mathbf{f}_{\text{face}} \,\|\, \mathbf{f}_{\text{age}}] \in \mathbb{R}^{1536}$ |
| 6 | `vit-emotion-face` | Dual-Domain | 1.536 | $\mathbf{z} = [\mathbf{f}_{\text{emotion}} \,\|\, \mathbf{f}_{\text{face}}] \in \mathbb{R}^{1536}$ |
| 7 | **`vit-face-emotion-age`** | **Tri-Domain (Diusulkan)** | **2.304** | $\mathbf{z} = [\mathbf{f}_{\text{face}} \,\|\, \mathbf{f}_{\text{emotion}} \,\|\, \mathbf{f}_{\text{age}}] \in \mathbb{R}^{2304}$ |

### 5.2 Berkas Cache Fitur Offline
*Dictionary* fitur hasil serialisasi yang memetakan path relatif citra ke larik NumPy 768-d (`float32`) tersimpan pada direktori `experiment/code/features/`:
- `demogpairs_vit-face.pkl` (30.8 MB)
- `demogpairs_vit-emotion.pkl` (30.8 MB)
- `demogpairs_vit-age.pkl` (30.8 MB)

### 5.3 Metrik Waktu Ekstraksi Fitur & Direktori `experiment/code/times/`
Pencatatan waktu ekstraksi fitur tingkat citra dan ringkasan performa agregat tersimpan pada direktori `experiment/code/times/` dalam format JSON terstandarisasi:
- `features_vit-face.json` (skutaada/VIT-VGGFace: total 5.044,0 s / 467,04 ms per citra pada CPU; ~42 ms pada GPU RTX 4060)
- `features_vit-emotion.json` (dima806/facial_emotions_...: total 5.148,0 s / 476,67 ms per citra pada CPU)
- `features_vit-age.json` (dima806/facial_age_...: total 5.865,0 s / 543,06 ms per citra pada CPU)

Setiap berkas JSON memuat `model_name`, `feature_name`, `device`, `total_images`, `total_time_seconds`, `total_time_formatted`, `avg_time_per_image_seconds`, `avg_time_per_image_ms`, serta kamus lengkap `times_per_image` yang memetakan seluruh 10.800 path citra ke durasi ekstraksinya masing-masing.

> [!TIP]
> **In-Memory Caching Processor & Resolusi Bottleneck:** Modul `utils/extraction.py` telah dilengkapi *global in-memory caching* (`_PROCESSOR_CACHE`) dan helper `get_image_processor()` untuk mengeliminasi pemanggilan `AutoImageProcessor.from_pretrained` berulang sebanyak 10.800 kali dari disk. Optimasi ini memangkas latensi GPU per citra dari ~1.280 ms menjadi ~42 ms (peningkatan kecepatan ~30×), sehingga total waktu ekstraksi 10.800 citra pada CUDA GPU tuntas hanya dalam ~7,6 menit (bukan >3,8 jam).

---

## 6. Pipeline Classifier Klasik & Optimasi GridSearchCV Lengkap

### 6.1 Formulasi Pipeline End-to-End
$$\mathbf{x} \xrightarrow{\text{Scaler}} \tilde{\mathbf{x}} \xrightarrow{\text{PCA}} \hat{\mathbf{x}} \xrightarrow{\text{Classifier}} \hat{y} \in \{0, 1, 2, 3, 4, 5\}$$

### 6.2 Ruang Pencarian Hyperparameter per Classifier
- **Support Vector Machine (SVM) – 288 konfigurasi per skema:**
  - `scaler`: `[None, MinMaxScaler()]`
  - `pca`: `[None, PCA(n_components=0.50), PCA(n_components=0.75)]`
  - `classifier__C`: `[0.1, 1, 10, 100]`
  - `classifier__kernel`: `['linear', 'rbf', 'poly']`
  - `classifier__degree`: `[2, 3]`
  - `classifier__gamma`: `['scale', 'auto']`
- **Logistic Regression (LR) – 270 konfigurasi per skema:**
  - `scaler`: `[None, MinMaxScaler()]`
  - `pca`: `[None, PCA(n_components=0.50), PCA(n_components=0.75)]`
  - `classifier__C`: `[0.01, 0.1, 1, 10, 100]`
  - `classifier__solver`: `['lbfgs', 'saga', 'newton-cg']`
  - `classifier__max_iter`: `[200, 500, 2000]`
- **Random Forest (RF) – 288 konfigurasi per skema:**
  - `scaler`: `[None, MinMaxScaler()]`
  - `pca`: `[None, PCA(n_components=0.50), PCA(n_components=0.75)]`
  - `classifier__n_estimators`: `[100, 200]`
  - `classifier__max_depth`: `[None, 10, 30]`
  - `classifier__max_features`: `['sqrt', 'log2']`
  - `classifier__min_samples_split`: `[2, 5]`
  - `classifier__min_samples_leaf`: `[1, 2]`
- **Gaussian Naive Bayes (GNB) – 240 konfigurasi per skema:**
  - `scaler`: `[None, MinMaxScaler()]`
  - `pca`: `[None, PCA(n_components=0.50), PCA(n_components=0.75)]`
  - `classifier__var_smoothing`: 40 nilai logaritmik dari $10^{-9}$ hingga $10^{2}$ (`np.logspace(-9, 2, 40)`)

### 6.3 Ringkasan Skala Optimasi
- Total kombinasi per skema fitur: $288 + 270 + 288 + 240 = \mathbf{1.086}$ kombinasi.
- Total *cross-validation fits* (5-Fold) per skema: $1.086 \times 5 = \mathbf{5.430}$ *fits*.
- Total keseluruhan untuk 7 skema fitur: $5.430 \times 7 = \mathbf{38.010}$ *cross-validation fits* + 28 model *final refit*.

---

## 7. Benchmark Eksperimental Ganda Komprehensif

### 7.1 Leaderboard Utama: Subject-Disjoint Leaderboard (28 Model)
Dievaluasi pada partisi uji independen *subject-disjoint* ($N = 2.160$ sampel dari 120 subjek baru). Data diekstraksi secara presisi dari berkas JSON aktif di `experiment/code/results/*.json`:

| Rank | Classifier | Skema Fitur | Kategori | Dimensi | Test Accuracy | Precision | Recall | F1-Score | 95% CI (Wilson) | Latency (ms) | Size (MB) | Hyperparameter Terbaik |
|:---:|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 🥇 **1** | **LR** | **`vit-face-emotion-age`** | **Tri** | **2.304** | **88.66%** | **0.8875** | **0.8866** | **0.8868** | **[87.25%, 89.93%]** | **0.0054** | **0.11** | `C=0.1, solver='saga', max_iter=500, scaler=MinMaxScaler, pca=None` |
| 🥈 **2** | **SVM** | **`vit-face-emotion-age`** | **Tri** | **2.304** | **88.61%** | **0.8871** | **0.8861** | **0.8863** | **[87.20%, 89.88%]** | 4.4481 | 36.60 | `C=10, kernel='rbf', gamma='scale', scaler=MinMaxScaler, pca=None` |
| 🥉 **3** | SVM | `vit-emotion-face` | Dual | 1.536 | **88.43%** | 0.8850 | 0.8843 | 0.8844 | [87.01%, 89.71%] | 0.9707 | 15.27 | `C=10, kernel='rbf', gamma='scale', scaler=MinMaxScaler, pca=None` |
| 4 | SVM | `vit-face-age` | Dual | 1.536 | 87.55% | 0.8766 | 0.8755 | 0.8757 | [86.09%, 88.87%] | 2.2581 | 23.48 | `C=10, kernel='rbf', gamma='scale', scaler=MinMaxScaler, pca=None` |
| 5 | LR | `vit-emotion-face` | Dual | 1.536 | 87.45% | 0.8759 | 0.8745 | 0.8749 | [85.99%, 88.78%] | 0.0039 | 0.08 | `C=0.1, solver='saga', max_iter=500, scaler=MinMaxScaler, pca=None` |
| 6 | LR | `vit-face-age` | Dual | 1.536 | 87.41% | 0.8744 | 0.8741 | 0.8740 | [85.94%, 88.74%] | 0.0090 | 0.11 | `C=0.1, solver='saga', max_iter=500, scaler=MinMaxScaler, pca=None` |
| 7 | LR | `vit-emotion-age` | Dual | 1.536 | 86.67% | 0.8668 | 0.8667 | 0.8667 | [85.17%, 88.04%] | 0.0040 | 0.08 | `C=0.1, solver='saga', max_iter=500, scaler=MinMaxScaler, pca=None` |
| 8 | LR | `vit-face` | Single | 768 | 86.39% | 0.8646 | 0.8639 | 0.8640 | [84.88%, 87.77%] | 0.0008 | 0.04 | `C=1, solver='saga', max_iter=500, scaler=MinMaxScaler, pca=None` |
| 9 | SVM | `vit-emotion-age` | Dual | 1.536 | 86.25% | 0.8626 | 0.8625 | 0.8624 | [84.73%, 87.64%] | 3.1451 | 32.76 | `C=10, kernel='rbf', gamma='scale', scaler=MinMaxScaler, pca=None` |
| 10 | SVM | `vit-face` | Single | 768 | 86.16% | 0.8624 | 0.8616 | 0.8619 | [84.64%, 87.55%] | 3.0653 | 7.56 | `C=10, kernel='rbf', gamma='scale', scaler=MinMaxScaler, pca=None` |
| 11 | SVM | `vit-emotion` | Single | 768 | 85.79% | 0.8584 | 0.8579 | 0.8580 | [84.25%, 87.20%] | 1.8871 | 15.30 | `C=10, kernel='rbf', gamma='scale', scaler=MinMaxScaler, pca=None` |
| 12 | LR | `vit-emotion` | Single | 768 | 85.23% | 0.8535 | 0.8523 | 0.8527 | [83.67%, 86.67%] | 0.0037 | 0.06 | `C=0.1, solver='saga', max_iter=500, scaler=MinMaxScaler, pca=None` |
| 13 | RF | `vit-face-emotion-age` | Tri | 2.304 | 85.00% | 0.8506 | 0.8500 | 0.8493 | [83.43%, 86.44%] | 0.0537 | 6.19 | `n_estimators=200, max_depth=None, max_features='sqrt', min_samples_split=2, min_samples_leaf=1, pca=PCA(0.75), scaler=None` |
| 14 | RF | `vit-emotion-face` | Dual | 1.536 | 84.86% | 0.8493 | 0.8486 | 0.8479 | [83.29%, 86.31%] | 0.0316 | 8.58 | `n_estimators=200, max_depth=None, max_features='sqrt', min_samples_split=2, min_samples_leaf=1, pca=PCA(0.75), scaler=None` |
| 15 | RF | `vit-face-age` | Dual | 1.536 | 84.86% | 0.8488 | 0.8486 | 0.8478 | [83.29%, 86.31%] | 0.0310 | 6.19 | `n_estimators=200, max_depth=None, max_features='sqrt', min_samples_split=2, min_samples_leaf=1, pca=PCA(0.75), scaler=None` |
| 16 | GNB | `vit-emotion-face` | Dual | 1.536 | 84.31% | 0.8437 | 0.8431 | 0.8430 | [82.71%, 85.78%] | 0.0083 | 0.78 | `var_smoothing=0.005878, pca=PCA(0.75), scaler=MinMaxScaler` |
| 17 | RF | `vit-face` | Single | 768 | 84.03% | 0.8413 | 0.8403 | 0.8403 | [82.42%, 85.51%] | 0.0314 | 5.99 | `n_estimators=200, max_depth=None, max_features='sqrt', min_samples_split=2, min_samples_leaf=1, pca=PCA(0.75), scaler=None` |
| 18 | GNB | `vit-face-emotion-age` | Tri | 2.304 | 83.61% | 0.8379 | 0.8361 | 0.8364 | [81.99%, 85.11%] | 0.0081 | 1.36 | `var_smoothing=0.005878, pca=PCA(0.75), scaler=None` |
| 19 | GNB | `vit-face-age` | Dual | 1.536 | 83.06% | 0.8347 | 0.8306 | 0.8310 | [81.42%, 84.58%] | 0.0080 | 0.75 | `var_smoothing=0.011253, pca=PCA(0.75), scaler=MinMaxScaler` |
| 20 | SVM | `vit-age` | Single | 768 | 82.55% | 0.8268 | 0.8255 | 0.8258 | [80.89%, 84.09%] | 2.0104 | 18.22 | `C=10, kernel='rbf', gamma='scale', scaler=MinMaxScaler, pca=None` |
| 21 | GNB | `vit-face` | Single | 768 | 82.55% | 0.8268 | 0.8255 | 0.8250 | [80.89%, 84.09%] | 0.0031 | 0.19 | `var_smoothing=0.041246, pca=PCA(0.75), scaler=MinMaxScaler` |
| 22 | LR | `vit-age` | Single | 768 | 81.48% | 0.8145 | 0.8148 | 0.8146 | [79.79%, 83.06%] | 0.0028 | 0.06 | `C=0.1, solver='saga', max_iter=500, scaler=MinMaxScaler, pca=None` |
| 23 | RF | `vit-emotion-age` | Dual | 1.536 | 77.31% | 0.7734 | 0.7731 | 0.7728 | [75.50%, 79.03%] | 0.0392 | 12.35 | `n_estimators=200, max_depth=None, max_features='log2', min_samples_split=5, min_samples_leaf=2, pca=PCA(0.75), scaler=None` |
| 24 | RF | `vit-emotion` | Single | 768 | 76.11% | 0.7602 | 0.7611 | 0.7603 | [74.27%, 77.86%] | 0.0316 | 10.34 | `n_estimators=200, max_depth=None, max_features='log2', min_samples_split=5, min_samples_leaf=1, pca=PCA(0.75), scaler=None` |
| 25 | GNB | `vit-emotion-age` | Dual | 1.536 | 75.88% | 0.7597 | 0.7588 | 0.7578 | [74.03%, 77.64%] | 0.0048 | 0.24 | `var_smoothing=0.001604, pca=PCA(0.75), scaler=MinMaxScaler` |
| 26 | GNB | `vit-emotion` | Single | 768 | 72.13% | 0.7251 | 0.7213 | 0.7199 | [70.20%, 73.98%] | 0.0031 | 0.13 | `var_smoothing=0.003070, pca=PCA(0.75), scaler=None` |
| 27 | RF | `vit-age` | Single | 768 | 71.81% | 0.7176 | 0.7181 | 0.7170 | [69.87%, 73.66%] | 0.0327 | 11.21 | `n_estimators=200, max_depth=30, max_features='log2', min_samples_split=2, min_samples_leaf=1, pca=PCA(0.75), scaler=None` |
| 28 | GNB | `vit-age` | Single | 768 | 67.08% | 0.6691 | 0.6708 | 0.6686 | [65.07%, 69.03%] | 0.0045 | 0.37 | `var_smoothing=0.000438, pca=PCA(0.75), scaler=MinMaxScaler` |

### 7.2 Leaderboard Historis: Subject-Overlap Leaderboard (28 Model)
Dipreservasi di dalam `experiment/code/archive/results_old/*.json` dan `audit_ledger.json` sebagai baseline komparatif:

| Rank | Classifier | Skema Fitur | Kategori | Dimensi | Test Accuracy | Precision | Recall | F1-Score | Hyperparameter Terbaik |
|:---:|---|---|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 🥇 **1** | **SVM** | **`vit-face-emotion-age`** | **Tri** | **2.304** | **0.9370** | **0.9372** | **0.9370** | **0.9369** | `C=10, kernel='poly', degree=2, gamma='scale', scaler=None, pca=None` |
| 🥈 **2** | **SVM** | `vit-emotion-face` | Dual | 1.536 | **0.9329** | 0.9333 | 0.9329 | 0.9329 | `C=10, kernel='rbf', degree=2, gamma='scale', scaler=MinMaxScaler, pca=None` |
| 🥉 **3** | **LR** | **`vit-face-emotion-age`** | **Tri** | **2.304** | **0.9273** | 0.9275 | 0.9273 | 0.9273 | `C=0.1, solver='newton-cg', max_iter=500, scaler=None, pca=None` |
| 4 | SVM | `vit-face-age` | Dual | 1.536 | 0.9255 | 0.9254 | 0.9255 | 0.9254 | `C=10, kernel='poly', degree=2, gamma='scale', scaler=None, pca=None` |
| 5 | LR | `vit-emotion-face` | Dual | 1.536 | 0.9241 | 0.9241 | 0.9241 | 0.9240 | `C=0.1, solver='lbfgs', max_iter=500, scaler=None, pca=None` |
| 6 | SVM | `vit-emotion-age` | Dual | 1.536 | 0.9208 | 0.9210 | 0.9208 | 0.9209 | `C=10, kernel='rbf', degree=2, gamma='scale', scaler=None, pca=None` |
| 7 | LR | `vit-face-age` | Dual | 1.536 | 0.9162 | 0.9162 | 0.9162 | 0.9162 | `C=0.1, solver='newton-cg', max_iter=500, scaler=None, pca=None` |
| 8 | SVM | `vit-face` | Single | 768 | 0.9083 | 0.9084 | 0.9083 | 0.9083 | `C=10, kernel='rbf', degree=2, gamma='scale', scaler=None, pca=None` |
| 9 | LR | `vit-face` | Single | 768 | 0.9060 | 0.9060 | 0.9060 | 0.9059 | `C=1, solver='newton-cg', max_iter=500, scaler=MinMaxScaler, pca=None` |
| 10 | LR | `vit-emotion-age` | Dual | 1.536 | 0.9051 | 0.9052 | 0.9051 | 0.9051 | `C=0.1, solver='lbfgs', max_iter=500, scaler=None, pca=None` |
| 11 | SVM | `vit-emotion` | Single | 768 | 0.9019 | 0.9020 | 0.9019 | 0.9017 | `C=10, kernel='rbf', degree=2, gamma='scale', scaler=None, pca=None` |
| 12 | LR | `vit-emotion` | Single | 768 | 0.8847 | 0.8850 | 0.8847 | 0.8846 | `C=1, solver='saga', max_iter=500, scaler=MinMaxScaler, pca=None` |
| 13 | SVM | `vit-age` | Single | 768 | 0.8764 | 0.8767 | 0.8764 | 0.8765 | `C=10, kernel='rbf', degree=2, gamma='scale', scaler=None, pca=None` |
| 14 | RF | `vit-emotion-face` | Dual | 1.536 | 0.8685 | 0.8689 | 0.8685 | 0.8682 | `n_estimators=200, max_depth=None, max_features='sqrt', min_samples_split=5, min_samples_leaf=1, pca=PCA(0.75), scaler=None` |
| 15 | LR | `vit-age` | Single | 768 | 0.8648 | 0.8649 | 0.8648 | 0.8648 | `C=0.1, solver='lbfgs', max_iter=500, scaler=None, pca=None` |
| 16 | RF | `vit-face-emotion-age` | Tri | 2.304 | 0.8620 | 0.8620 | 0.8620 | 0.8613 | `n_estimators=200, max_depth=30, max_features='sqrt', min_samples_split=5, min_samples_leaf=1, pca=PCA(0.75), scaler=None` |
| 17 | RF | `vit-face-age` | Dual | 1.536 | 0.8579 | 0.8578 | 0.8579 | 0.8573 | `n_estimators=200, max_depth=None, max_features='sqrt', min_samples_split=2, min_samples_leaf=1, pca=PCA(0.75), scaler=None` |
| 18 | RF | `vit-face` | Single | 768 | 0.8546 | 0.8543 | 0.8546 | 0.8539 | `n_estimators=200, max_depth=30, max_features='log2', min_samples_split=2, min_samples_leaf=1, pca=PCA(0.75), scaler=MinMaxScaler` |
| 19 | GNB | `vit-face-emotion-age` | Tri | 2.304 | 0.8505 | 0.8512 | 0.8505 | 0.8505 | `var_smoothing=0.005878, pca=PCA(0.75), scaler=None` |
| 20 | GNB | `vit-emotion-face` | Dual | 1.536 | 0.8486 | 0.8490 | 0.8486 | 0.8481 | `var_smoothing=0.005878, pca=PCA(0.75), scaler=MinMaxScaler` |
| 21 | GNB | `vit-face-age` | Dual | 1.536 | 0.8315 | 0.8343 | 0.8315 | 0.8317 | `var_smoothing=0.011253, pca=PCA(0.75), scaler=MinMaxScaler` |
| 22 | GNB | `vit-face` | Single | 768 | 0.8269 | 0.8271 | 0.8269 | 0.8258 | `var_smoothing=0.041246, pca=PCA(0.75), scaler=MinMaxScaler` |
| 23 | RF | `vit-emotion-age` | Dual | 1.536 | 0.8111 | 0.8111 | 0.8111 | 0.8108 | `n_estimators=200, max_depth=None, max_features='log2', min_samples_split=5, min_samples_leaf=2, pca=PCA(0.75), scaler=None` |
| 24 | RF | `vit-emotion` | Single | 768 | 0.8060 | 0.8063 | 0.8060 | 0.8057 | `n_estimators=200, max_depth=None, max_features='log2', min_samples_split=5, min_samples_leaf=1, pca=PCA(0.75), scaler=None` |
| 25 | GNB | `vit-emotion-age` | Dual | 1.536 | 0.7681 | 0.7686 | 0.7681 | 0.7681 | `var_smoothing=0.001604, pca=PCA(0.75), scaler=MinMaxScaler` |
| 26 | RF | `vit-age` | Single | 768 | 0.7366 | 0.7363 | 0.7366 | 0.7354 | `n_estimators=200, max_depth=30, max_features='log2', min_samples_split=2, min_samples_leaf=1, pca=PCA(0.75), scaler=None` |
| 27 | GNB | `vit-emotion` | Single | 768 | 0.7338 | 0.7387 | 0.7338 | 0.7329 | `var_smoothing=0.003070, pca=PCA(0.75), scaler=None` |
| 28 | GNB | `vit-age` | Single | 768 | 0.6963 | 0.6979 | 0.6963 | 0.6952 | `var_smoothing=0.000438, pca=PCA(0.75), scaler=MinMaxScaler` |

### 7.3 Ablasi Komparatif Data Leakage & Analisis Generalisasi
Secara langsung menjawab Komentar #2 Reviewer 2, perbandingan kedua benchmark ini menguantifikasi secara eksak dampak dari memorisasi identitas (*identity memorization*):

| Classifier | Skema Fitur | Akurasi Subject-Overlap | Akurasi Subject-Disjoint | $\Delta\text{Acc}$ (Penurunan) | 95% Wilson Score CI |
|---|---|:---:|:---:|:---:|:---:|
| **SVM** | `vit-face-emotion-age` | 93.70% | 88.61% | -5.09 pp | [87.20%, 89.88%] |
| **SVM** | `vit-emotion-face` | 93.29% | 88.43% | -4.86 pp | [87.01%, 89.71%] |
| **SVM** | `vit-face` | 90.83% | 86.16% | -4.68 pp | [84.64%, 87.55%] |
| **LR** | `vit-face-emotion-age` | 92.73% | 88.66% | -4.07 pp | [87.25%, 89.93%] |
| **LR** | `vit-emotion-face` | 92.41% | 87.45% | -4.95 pp | [85.99%, 88.78%] |
| **LR** | `vit-face` | 90.60% | 86.39% | -4.21 pp | [84.88%, 87.77%] |
| **RF** | `vit-face-emotion-age` | 86.20% | 85.00% | -1.20 pp | [83.43%, 86.44%] |
| **GNB** | `vit-face-emotion-age` | 85.05% | 83.61% | -1.44 pp | [81.99%, 85.11%] |

### 7.4 Pengujian Hipotesis Inferensial & Signifikansi Statistik (Paired McNemar Tests)
Dihitung dari tabel kontingensi pasangan diskordan (*discordant pairs contingency tables*, $N = 2.160$) dengan koreksi kontinuitas Edwards:

1. **Tri-Domain vs. Single-Domain (`vit-face`):**
   - **SVM:** Tri-Domain (88.61%) vs. Face (86.16%) $\implies \Delta = +2.45\%$, Keuntungan Bersih = $+53$ citra ($b=91, c=38$), $\chi^2 = 20.9612$, **$p = 3.46 \times 10^{-6} < 0.001$ (Sangat Signifikan secara Statistik)**.
   - **Logistic Regression:** Tri-Domain (88.66%) vs. Face (86.39%) $\implies \Delta = +2.27\%$, Keuntungan Bersih = $+49$ citra ($b=83, c=34$), $\chi^2 = 19.6923$, **$p = 6.78 \times 10^{-6} < 0.001$ (Sangat Signifikan secara Statistik)**.
   - **Random Forest:** Tri-Domain (85.00%) vs. Face (84.03%) $\implies \Delta = +0.97\%$, Keuntungan Bersih = $+21$ citra ($b=50, c=29$), $\chi^2 = 5.0633$, **$p = 0.0238 < 0.05$ (Signifikan secara Statistik)**.
   - **Gaussian Naive Bayes:** Tri-Domain (83.61%) vs. Face (82.55%) $\implies \Delta = +1.06\%$, Keuntungan Bersih = $+23$ citra ($b=97, c=74$), $\chi^2 = 2.8304$, $p = 0.0922$ (Tidak signifikan).
2. **Tri-Domain vs. Dual-Domain (`vit-emotion-face`):**
   - **Logistic Regression:** Tri-Domain (88.66%) vs. Dual-Domain (87.45%) $\implies \Delta = +1.20\%$, Keuntungan Bersih = $+26$ citra ($b=57, c=31$), $\chi^2 = 7.1023$, **$p = 0.0073 < 0.01$ (Signifikan secara Statistik)**.
   - **SVM:** Tri-Domain (88.61%) vs. Dual-Domain (88.43%) $\implies \Delta = +0.19\%$, Keuntungan Bersih = $+4$ citra ($b=41, c=37$), $\chi^2 = 0.1154$, $p = 0.7343$ (Tidak signifikan; membuktikan terjadinya saturasi fitur asimtotik pada kernel non-linear RBF).
3. **Komparasi Arsitektur Puncak (LR Tri vs. SVM Tri):**
   - LR Tri (88.66%) vs. SVM Tri (88.61%) $\implies \Delta = +0.05\%$, Keuntungan Bersih = $+1$ citra ($b=36, c=35$), $\chi^2 = 0.0000$, **$p = 1.0000$ (Ekuivalen secara Statistik)**.
   - *Trade-off* Efisiensi Komputasi: LR terbukti **>800x lebih cepat dalam latensi inferensi** (0.0054 ms vs 4.4481 ms) dan **>330x lebih ringkas dalam ukuran model** (0.11 MB vs 36.60 MB).

---

## 8. Performa Subkelompok Interseksional, Confusion Matrix & Profil Fairness

### 8.1 Performa Subkelompok pada Subject-Disjoint Benchmark ($N = 2.160$)

#### (a) Logistic Regression Tri-Domain (Model Puncak Benchmark: 88.66%)
| Subkelompok Demografi | Ras Makro | Gender | Support | Recall / TPR | Precision | F1-Score |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **White_Males** | White | Male | 360 | **94.44%** | **95.24%** | **94.84%** |
| **White_Females** | White | Female | 360 | 90.56% | 91.32% | 90.93% |
| **Black_Males** | Black | Male | 360 | 87.78% | 91.59% | 89.65% |
| **Asian_Males** | Asian | Male | 360 | 87.78% | 82.72% | 85.18% |
| **Asian_Females** | Asian | Female | 360 | 86.67% | 86.43% | 86.55% |
| **Black_Females** | Black | Female | 360 | 84.72% | 85.20% | 84.96% |
| **Macro Average** | **Semua** | **Semua** | **2.160** | **88.66%** | **0.8875** | **0.8868** |

*Equal Opportunity Difference (Max - Min Recall): **9.72 percentage points** (94.44% - 84.72%).*

#### (b) Support Vector Machine Tri-Domain (88.61%)
| Subkelompok Demografi | Ras Makro | Gender | Support | Recall / TPR | Precision | F1-Score |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **White_Males** | White | Male | 360 | **94.44%** | 93.92% | **94.18%** |
| **White_Females** | White | Female | 360 | 91.11% | 90.11% | 90.61% |
| **Asian_Males** | Asian | Male | 360 | 88.06% | 82.34% | 85.10% |
| **Black_Males** | Black | Male | 360 | 87.22% | 92.35% | 89.71% |
| **Asian_Females** | Asian | Female | 360 | 86.11% | 85.87% | 85.99% |
| **Black_Females** | Black | Female | 360 | 84.72% | 87.64% | 86.16% |
| **Macro Average** | **Semua** | **Semua** | **2.160** | **88.61%** | **0.8871** | **0.8863** |

*Equal Opportunity Difference (Max - Min Recall): **9.72 percentage points**.*

### 8.2 Metrik Subkelompok Subject-Overlap Historis (SVM Tri-Domain: 93.70%)
Dipreservasi untuk referensi komparatif:
- `White_Males`: Recall 96.94%, Precision 95.36%, F1 96.14%
- `Black_Males`: Recall 94.17%, Precision 95.49%, F1 94.83%
- `White_Females`: Recall 94.72%, Precision 92.41%, F1 93.55%
- `Asian_Males`: Recall 94.44%, Precision 92.39%, F1 93.41%
- `Asian_Females`: Recall 92.50%, Precision 92.50%, F1 92.50%
- `Black_Females`: Recall 89.44%, Precision 94.15%, F1 91.74%
- Disparitas: $\Delta\text{F1} = 0.0440$, $\Delta\text{Recall} = 0.0750$.

---

## 9. Perbandingan dengan Studi Terdahulu pada DemogPairs & Literatur

### 9.1 Performa Komparatif pada Benchmark DemogPairs
| Referensi | Protokol Partisi | Arsitektur | Accuracy | Precision | Recall | F1-Score |
|---|---|---|:---:|:---:|:---:|:---:|
| Putri et al. (*JIEET 2025*) | Random Stratified (Subject-Overlap) | MD-ViT (Face + Age) + XGBoost | 89.07% | 0.8912 | 0.8907 | 0.8901 |
| Putri et al. (*IEEE ICVEE 2025*) | Random Stratified (Subject-Overlap) | Dual-ViT (Face + Emotion) + SVM | 92.41% | 0.9248 | 0.9241 | 0.9238 |
| **Diusulkan (Baseline Historis)** | **Random Stratified (Subject-Overlap)** | **Tri-Domain ViT + SVM** | **93.70%** | **0.9372** | **0.9370** | **0.9369** |
| **Diusulkan (Tonggak Revisi)** | **Subject-Disjoint (Zero Leakage)** | **Tri-Domain ViT + LR** | **88.66%** | **0.8875** | **0.8866** | **0.8868** |
| **Diusulkan (Tonggak Revisi)** | **Subject-Disjoint (Zero Leakage)** | **Tri-Domain ViT + SVM** | **88.61%** | **0.8871** | **0.8861** | **0.8863** |

*Pembedaan Kontekstual Penting:* Karya terdahulu (Putri et al. 2025) dievaluasi di bawah pembagian acak bertingkat pada level citra yang mengandung tumpang tindih identitas subjek (*subject overlap*). Pada partisi independen *subject-disjoint* yang ketat tanpa kebocoran identitas, kerangka kerja tri-domain yang kami usulkan mencapai akurasi 88.66% (LR) / 88.61% (SVM).

---

## 10. Arsitektur Repositori & Inventaris Berkas

```
D:\Research\face-race-gender-multi-vit\
├── README.md                              # Dokumentasi ringkas & publikasi penelitian
├── README.ai.md                           # Panduan manual referensi utama AI agent (BERKAS INI)
├── WORKFLOW.md                            # Standar Operasional Prosedur (SOP) alur penulisan manuskrip
├── paper_outline_v1.0.md                  # Kerangka master naskah v1.0 (Arsip historis pra-revisi / Subject-Overlap)
├── paper_outline_v1.1.md                  # Kerangka master naskah v1.1 (Definitif revisi IEEE Access / Subject-Disjoint)
├── folder_structure.txt                   # Pohon direktori lengkap dan glosarium berkas mendalam
├── authors.txt                            # Profil akademik penulis, afiliasi & ID ORCID
├── prompts.txt                            # Log pencatatan kronologis riwayat instruksi prompt
├── scopus_query.txt                       # Kueri penelusuran literatur Scopus
│
├── .agents/skills/                        # Kerangka kerja peer review & skill AI agent otonom
│   ├── ar-paper-reviewer/                 # Skill simulasi peer review akademik independen
│   ├── ar-paper-revision/                 # Skill eksekusi revisi teks presisi tingkat byte & patching
│   └── ar-paper-revision-coach/           # Skill dekonstruksi komentar reviewer, roadmap & rebuttal ledger
│
├── docs/                                  # Dokumentasi tata kelola riset dan log sesi kerja
│   └── sessions/                          # Log sesi kerja otonom AI agent kronologis (2026-10-27 s.d. terkini)
├── experiment/                            # Dokumentasi eksperimen, dataset & kode sumber
│   ├── 00_overview.md - 05_results.md     # Log eksperimental terstruktur & audit
│   ├── dataset_demogpairs.md              # Spesifikasi dataset dan ringkasan partisi
│   └── code/
│       ├── 1.1_vit-*_demogpairs.ipynb     # Notebook ekstraksi fitur (Face, Emotion, Age)
│       ├── 2.1.* - 2.5.*.ipynb            # Notebook classifier aktif Subject-Disjoint (SVM, GNB, RF, LR)
│       ├── 3.0_compare.ipynb              # Notebook komparasi global 28 model & benchmark (Subject-Disjoint)
│       ├── 3.1_statistical_significance.ipynb # Paired McNemar tests, Wilson Score CIs & analisis EOD
│       ├── 4.0_test.ipynb                 # Rutinitas pengujian dan evaluasi data held-out
│       ├── app.py                         # Aplikasi web demo inferensi interaktif berbasis Gradio
│       ├── archive/                       # Arsip Baseline Subject-Overlap Historis (Ablasi Data Leakage)
│       │   ├── audit_ledger.json          # Buku besar audit konsolidasi komparasi 28 Model Lama vs 28 Baru
│       │   ├── md_old/                    # Log Markdown (35 berkas) & confusion matrix eksperimen terdahulu
│       │   ├── models_old/                # Bobot model terlatih (.pkl) dari 28 model historis
│       │   ├── notebook_old/              # 35 notebook Jupyter eksperimen terdahulu
│       │   ├── results_old/               # 28 berkas hasil evaluasi mentah JSON model historis subject-overlap
│       │   └── README.md                  # Dokumentasi mendalam tujuan arsip dan protokol audit
│       ├── scripts/                       # Runner eksekusi otonom & skrip antrean otomatis
│       │   ├── auto_run_experiments.py    # Batch runner utama untuk otomatisasi pipeline 28 eksperimen
│       │   ├── run_gnb_queue.py           # Queue runner khusus untuk famili model Gaussian Naive Bayes
│       │   ├── run_remaining_queue.py     # Queue runner tangguh untuk beban kerja model yang tersisa
│       │   ├── run_experiments.bat        # Skrip batch Windows untuk peluncuran auto_run_experiments.py
│       │   ├── run_gnb.bat                # Skrip batch Windows untuk antrean GNB
│       │   └── README.md                  # Dokumentasi operasional runner dan perintah eksekusi
│       ├── utils/                         # Paket utilitas Python modular (constants, dataset, evaluation, dll.)
│       ├── dataset/demogpairs/metadata/   # 6 berkas metadata .txt (masing-masing 1.800 baris)
│       ├── features/                      # Vektor embedding fitur 768-d hasil serialisasi (.pkl)
│       ├── times/                         # Berkas metrik JSON waktu ekstraksi fitur (Face, Emotion, Age)
│       ├── md/                            # Ekspor Markdown seluruh notebook & laporan statistik
│       ├── models/                        # Bobot model terlatih (.pkl) dari 28 model aktif
│       ├── results/                       # 28 berkas hasil mentah JSON dari model aktif Subject-Disjoint
│       └── images/                        # Matriks konfusi dan grafik plot Wilson Score 95% CI
│
├── images/                                # Diagram arsitektur resolusi tinggi dan figur ilustrasi
├── paper/                                 # Draf manuskrip modular dalam format Markdown (gaya IEEE)
│   ├── 00_abstract.md - 05_conclusion.md  # Seksi-seksi inti draf manuskrip
│   ├── 06_references.md                   # Repositori daftar pustaka IEEE terstandarisasi (entri [1]-[51])
│   ├── 07_biographies.md                  # Seksi VII: Biografi penulis & aset foto potret
│   ├── acronyms.txt                       # Glosarium akronim terpusat
│   ├── ref_part_*.md                      # 10 log audit bibliografi modular (entri [1]-[51])
│   ├── references.txt                     # Registri penelusuran sitasi tingkat kalimat & verifikasi
│   └── references/                        # 51 berkas sumber bibliografi (.bib, .ris, .nbib, .bibtex)
│
├── paper_latex_en/                        # Paket LaTeX IEEE Access Bahasa Inggris siap-submit
│   ├── access.tex / access.pdf            # Master entrypoint LaTeX & hasil kompilasi PDF
│   ├── ieeeaccess.cls / IEEEtran.bst      # Berkas kelas dan gaya resmi IEEE Access
│   ├── references.bib                     # Basis data pustaka BibTeX terkonsolidasi
│   ├── sections/                          # 21 seksi modular LaTeX
│   └── images/                            # Aset figur grafis untuk kompilasi
│
├── paper_latex_id/                        # Paket referensi LaTeX IEEE Access Bahasa Indonesia
├── paper_reviews/                         # Sistem audit simulasi mock peer review multi-agent (Round 1 & 2)
├── paper_reviews_ieee/                    # Dossier keputusan editorial & review resmi IEEE Access
├── paper_submission/                      # Paket formal submission & laporan kepatuhan IEEE Access
├── sessions/                              # Cermin direktori sesi kerja kronologis
├── template/                              # Distribusi paket template LaTeX mentah resmi IEEE Access
└── upload/                                # Artefak berkas akhir siap unggah (PDF dan ZIP kode sumber)
```

---

## 11. Kepatuhan Submission & Paket Unggahan (`paper_submission/` & `upload/`)

### 11.1 Direktori `paper_submission/`
- `checklist_report.md`: Laporan sistematis yang mengaudit kepatuhan terhadap seluruh persyaratan pengajuan IEEE Access.
- `IEEE Reference Preparation Assistant Report.txt`: Luaran dari *IEEE Reference Preparation Assistant* yang memverifikasi konsistensi format metadata pustaka.
- `ieee_taxonomy.txt`: Daftar kata kunci kosakata terkendali yang selaras dengan kategori taksonomi resmi IEEE.
- `IEEE-Access-Submission-Checklist.pdf` / `.txt` / `.ID.txt`: Daftar periksa (*checklist*) resmi pengajuan manuskrip IEEE Access.

### 11.2 Direktori `upload/`
- `Multi-Domain Vision Transformer Fusion for Intersectional Demographic Classification from Facial Images.pdf`: Dokumen PDF hasil kompilasi format dua kolom IEEE Access.
- `Multi-Domain Vision Transformer Fusion for Intersectional Demographic Classification from Facial Images.zip`: Paket arsip berkas sumber terkompresi yang memuat `access.tex`, `sections/*.tex`, `images/*`, `ieeeaccess.cls`, dan `references.bib`.

---

## 12. Suite Mock Peer Review Internal (`paper_reviews/`) & Agent Skills (`.agents/skills/`)

### 12.1 Sistem Mock Peer Review Internal (`paper_reviews/`)
- **`round-1/`**: *Desk screening* awal (`00_desk_screening.md`), 5 ulasan penilai independen (EIC, Methodology Reviewer, Domain Expert, Cross-Perspective Analyst, Devil's Advocate), matriks temuan ulasan, surat keputusan editorial, dan *revision roadmap*.
- **`round-2/`**: Verifikasi eksekusi revisi, pelacakan residu isu, validasi draf surat tanggapan (*response letter*), audit surat sanggahan (*rebuttal audit*), matriks keterlacakan evaluasi ulang (*re-review traceability matrix*), dan persetujuan akhir (*sign-off*) Editor-in-Chief.
- **`REVIEW_LOG.md`**: Jejak audit komprehensif yang memantau tonggak perkembangan seluruh siklus telaah.

### 12.2 Keterampilan Agen Otonom Khusus (`.agents/skills/`)
- `ar-paper-reviewer`: Mengeksekusi simulasi telaah sejawat (*mock peer review*) akademik independen di 5 peran terspesialisasi berdasarkan Kontrak Sprint Schema 13.
- `ar-paper-revision`: Menerapkan *patch* revisi presisi tingkat byte (`<!--block:BNNNN-->`), validasi *fail-closed* dua fase, serta penyusunan formal *Response to Reviewers* (Schema 8).
- `ar-paper-revision-coach`: Mengurai komentar penelaah, menyusun taksonomi masalah 4-tingkat, menetapkan prioritas perbaikan (P1/P2/P3), dan menghasilkan *R&R Traceability Matrix* (Schema 11).

---

## 13. Referensi Pustaka Utilitas Python (`experiment/code/utils/`)

Berlokasi pada direktori `experiment/code/utils/`, modul ini menyediakan logika bersama (*shared logic*) terpadu yang digunakan oleh seluruh alur eksperimen:

- **`constants.py`**: Mendefinisikan kelas demografi (`DEMOGPairs_CLASSES`), pemetaan indeks label (`DEMOGPairs_LABEL_TO_IDX`, `DEMOGPairs_IDX_TO_LABEL`), nilai benih acak (*random seeds*), serta palet visualisasi grafik.
- **`dataset.py`**:
  - `load_demogpairs(metadata_path, images_path) -> list[dict]`: Membaca dan mem-parsing berkas metadata teks.
  - `split_demogpairs_subject_disjoint(...)`: Mengimplementasikan pembagian partisi *subject-disjoint* yang ketat (480 subjek latih / 120 subjek uji; kebocoran data identitas 0.00%).
- **`extraction.py`**: Rutinitas ekstraksi fitur ViT HuggingFace melalui representasi vektor token `[CLS]` ternormalisasi berdimensi `(768,)`. Dilengkapi *global in-memory caching* (`_PROCESSOR_CACHE`) dan helper `get_image_processor()` untuk mengeliminasi pemuatan ulang pra-pemroses per citra dari disk.
- **`evaluation.py`**: Rutinitas evaluasi terpadu, pelatihan pipeline *GridSearchCV*, pembangkitan metrik One-vs-Rest (OvR), serta penulisan serialisasi ke format JSON.
- **`serialization.py`**: Serialisasi model berkinerja tinggi menggunakan Joblib (`save_object`, `load_object`) serta utilitas penyimpanan format JSON terstruktur.
- **`display.py` & `time_helpers.py`**: Utilitas visualisasi tabel terformat dan pelacakan pewaktu durasi eksekusi program.

---

## 14. Alur Kerja Eksekusi, Reproduksi & Kompilasi Manuskrip

### 14.1 Penyiapan Lingkungan Python
```bash
conda create -n torch-gpu python=3.11 -y
conda activate torch-gpu
pip install torch torchvision transformers scikit-learn imbalanced-learn joblib pandas numpy pillow matplotlib seaborn tqdm gradio nbconvert
```

### 14.2 Menjalankan Pipeline Aktif (Subject-Disjoint)

#### Eksekusi Batch melalui Skrip Antrean Otomatis:
```bash
cd experiment/code
python scripts/auto_run_experiments.py
```

#### Eksekusi Interaktif Langkah Demi Langkah:
1. **Ekstraksi Fitur:** Jalankan notebook `1.1_vit-face_demogpairs.ipynb`, `1.1_vit-emotion_demogpairs.ipynb`, dan `1.1_vit-age_demogpairs.ipynb` secara berurutan. Di bawah akselerasi CUDA GPU dengan in-memory processor caching, ekstraksi 10.800 citra selesai dalam ~7,6 menit per domain (~42 ms/citra). Waktu ekstraksi otomatis dicatat ke `times/features_vit-*.json`.
2. **Pelatihan & Optimasi Model:** Eksekusi notebook classifier aktif:
   - Logistic Regression: `2.5.1` sampai `2.5.7`
   - Support Vector Machine: `2.1.1` sampai `2.1.7`
   - Random Forest: `2.4.1` sampai `2.4.7`
   - Gaussian Naive Bayes: `2.2.1` sampai `2.2.7`
3. **Komparasi Lintas Model:** Jalankan `3.0_compare.ipynb` untuk mengonsolidasikan seluruh 28 berkas hasil JSON ke dalam papan peringkat (*leaderboard*) benchmark komparatif.
4. **Pengujian Signifikansi Statistik:** Jalankan `3.1_statistical_significance.ipynb` untuk menghasilkan matriks uji McNemar berpasangan, Wilson Score 95% CI, serta evaluasi keadilan EOD.
5. **Aplikasi Inferensi Web Interaktif:**
   ```bash
   python experiment/code/app.py
   # Meluncurkan antarmuka visual Gradio pada http://127.0.0.1:7860
   ```

### 14.3 Kompilasi Manuskrip LaTeX
```bash
# Kompilasi Manuskrip LaTeX Bahasa Inggris Siap-Submit
cd paper_latex_en
pdflatex access.tex
bibtex access
pdflatex access.tex
pdflatex access.tex
```

---

## 15. Batasan Klaim Ilmiah & Direktif Penulisan Akademik (28 Aturan/Direktif)

Saat menyusun, merevisi, atau mengaudit draf manuskrip, menyusun outline makalah, maupun merancang naskah tanggapan komentar penelaah (*Response to Reviewers*), seluruh AI agent **WAJIB** mematuhi secara ketat 28 direktif berikut:

1. **Kejelasan Partisi Ganda (Dual Partitioning Clarity):** Bedakan secara eksplisit antara *Subject-Disjoint Partitioning* (Benchmark Utama / Primary Benchmark, 0.00% kebocoran, 88.66% LR / 88.61% SVM) dan *Subject-Overlap Partitioning* (Baseline Historis, 100% kebocoran, 93.70% SVM). Bingkai hasil historis secara murni sebagai studi ablasi komparatif kebocoran data (*data leakage ablation study*).
2. **Formulasi Hati-Hati terhadap Kebocoran Data (Cautious Data Leakage Formulation):** Nyatakan secara presisi bahwa "protokol partisi *subject-disjoint* mengisolasi seluruh 120 identitas subjek uji dari data latih, mengeliminasi kebocoran akibat memorisasi identitas (*identity memorization leakage*)."
3. **Pengaturan Evaluasi Seimbang (Balanced Evaluation Setting):** Dataset yang seimbang tidak serta-merta menunjukkan bahwa bias demografis telah tereliminasi sepenuhnya; rujuklah kondisi ini sebagai "kondisi evaluasi seimbang (*balanced evaluation setting*)" atau "distribusi kelas yang seimbang antar-subkelompok."
4. **Validasi Signifikansi Statistik (Statistical Significance Validation):** Klaim bahwa representasi multi-domain ViT melampaui performa domain tunggal biometrik wajah divalidasi secara formal melalui pengujian hipotesis Paired McNemar ($p = 3.46 \times 10^{-6} < 0.001$ untuk SVM; $p = 6.78 \times 10^{-6} < 0.001$ untuk LR). Selalu sebutkan nilai *p-value* eksak dan statistik uji saat menggunakan frasa "signifikan secara statistik."
5. **Cakupan Akurat Tri-Domain (Accurate Tri-Domain Scope):** Fusi tri-domain meraih akurasi puncak pada 3 dari 4 classifier di bawah partisi *subject-disjoint* (LR: 88.66%, SVM: 88.61%, RF: 85.00%). Gaussian Naive Bayes mencapai performa puncak pada konfigurasi dual-domain `Emotion ⊕ Face` (84.31%).
6. **Kontribusi Komplementer Fitur Usia (Complementary Age Features):** Posisikan fitur usia (*Age*) sebagai penyedia "kontribusi informasi komplementer" atau "informasi diskriminatif tambahan", yang sangat bermanfaat bagi classifier linear ($p = 0.0073$ pada LR), sementara pada SVM non-linear terjadi kejenuhan fitur asimtotik ($p = 0.7343$).
7. **Pertukaran Komparatif LR vs. SVM (LR vs. SVM Trade-off):** Tekankan bahwa LR Tri-Domain dan SVM Tri-Domain setara secara statistik dalam hal akurasi prediktif ($p = 1.0000$), namun LR menawarkan keunggulan komputasi yang substansial (>800x lebih cepat dalam inferensi, >330x lebih ringkas dalam ukuran model).
8. **Pemisahan Temuan Empiris vs Teoretis (Empirical vs Theoretical Separation):** Pisahkan secara tegas antara temuan empiris (angka metrik eksperimental aktual) dari interpretasi atau hipotesis konseptual.
9. **Hindari Hiperbola State-of-the-Art (No State-of-the-Art Hyperbole):** Gunakan rumusan kalimat "performa tertinggi di antara konfigurasi yang dievaluasi pada DemogPairs" — jangan pernah mengklaim "state-of-the-art" tanpa bukti perbandingan global yang menyeluruh.
10. **Batasan Generalisasi Demografi (Demographic Generalization Scope):** Batasi klaim generalisasi secara eksplisit hanya pada 3 kelompok ras makro yang terwakili di dalam DemogPairs (Asian, Black, White).
11. **Pernyataan Etika AI (AI Ethics Statement):** Rumuskan bahwa penelitian ini ditujukan untuk tolok ukur akademik (*academic benchmarking*) dan riset keadilan algoritmik (*algorithmic fairness*); implementasi pengawasan ruang publik memerlukan mekanisme *human-in-the-loop* dan tata kelola etika yang ketat.
12. **Definisi Token CLS pada Persamaan (4):** Simbol $\mathbf{z}_L^0$ pada formulasi $\mathbf{f}_{\text{domain}} = \text{LayerNorm}(\mathbf{z}_L^0)$ merujuk secara spesifik pada representasi vektor token `[CLS]` dari **lapisan encoder terakhir L** pada arsitektur ViT backbone.
13. **Penyebutan Embedding ViT sebagai Representasi Terasosiasi Tugas:** Gunakan frasa "representasi terasosiasi tugas (*task-associated representations*)" sebagai pembingkaian terminologi utama.
14. **Penyebutan Angka Disparitas Eksak:**
    - Subject-Disjoint LR: *Equal Opportunity Difference* $\Delta\text{TPR} = \mathbf{9.72\text{ pp}}$ (White_Males 94.44% vs. Black_Females 84.72%).
    - Subject-Disjoint SVM: *Equal Opportunity Difference* $\Delta\text{TPR} = \mathbf{9.72\text{ pp}}$ (White_Males 94.44% vs. Black_Females 84.72%).
    - Subject-Overlap SVM: $\Delta\text{F1} = \mathbf{0.0440}$, $\Delta\text{Recall} = \mathbf{0.0750}$, $\Delta\text{Precision} = \mathbf{0.0310}$.
15. **Cakupan Analisis Performa Subkelompok (Subgroup Performance Scope):** Evaluasi performa subkelompok mencerminkan performa klasifikasi per-kelas pada demografi interseksional dan tidak dapat diklaim sebagai audit komprehensif keadilan algoritmik secara utuh.
16. **Konteks Akurasi One-vs-Rest (OvR Accuracy Context):** Ingat rasio kelas negatif 5:1 dalam evaluasi OvR 6-kelas; dilarang menyajikan akurasi OvR sebagai indikator keadilan utama.
17. **Pemeriksaan Konsistensi Numerik Lengkap (Full Numerical Consistency Check):** Seluruh tabel, matriks konfusi, metrik per-subkelompok, dan teks naratif harus 100% konsisten secara numerik dengan berkas `experiment/code/results/*.json` dan `experiment/code/archive/audit_ledger.json`.
18. **Pernyataan Kebaruan (Novelty Statement):** Kebaruan penelitian terletak pada integrasi: (a) fusi fitur ViT tri-domain, (b) evaluasi komparatif 4 famili classifier di bawah GridSearchCV terpadu, (c) ablasi empiris kebocoran data (*subject-disjoint* vs *subject-overlap*), dan (d) validasi statistik inferensial menggunakan Paired McNemar Test.
19. **Keselarasan Pertanyaan Riset (RQ Alignment):** Setiap kesimpulan ilmiah harus didukung oleh bukti empiris yang terverifikasi (*evidential anchor*).
20. **Konsistensi Terminologi, Notasi & Angka Akhir:** Verifikasi konsistensi notasi (simbol $\oplus$, rumus matematika, dan nilai metrik) di seluruh naskah.
21. **Hupont & Fernández (IEEE FG 2019):** Merupakan makalah perintis pembuat dataset DemogPairs; disitir saat memperkenalkan spesifikasi dataset, bukan sebagai pesaing langsung perbandingan performa.
22. **SOP Universal Pipeline Manuskrip (`WORKFLOW.md`):** Seluruh proses penulisan, penerjemahan, dan persiapan publikasi harus mengikuti pedoman operasional pada `WORKFLOW.md`.
23. **Protokol Audit Sitasi Tingkat Kalimat (`paper/references.txt`):** Klaim faktual harus dapat dilacak langsung ke entri referensi yang terdaftar.
24. **Standar Sitasi Teks Interaktif (`paper/*.md`):** Sitasi dalam teks draf Markdown wajib menggunakan format interaktif `[[N]](06_references.md#refN)`.
25. **Preservasi Direktori Arsip:** Dilarang keras menghapus atau mengubah berkas apa pun di dalam `experiment/code/archive/` atau `audit_ledger.json`.
26. **Pemeliharaan Direktori Skrip:** Pertahankan seluruh skrip otomatisasi runner tetap rapi dan terisolasi di dalam `experiment/code/scripts/`.
27. **Standar Penempatan Notebook:** Seluruh 33 notebook Jupyter aktif wajib dipertahankan posisinya langsung pada akar direktori `experiment/code/`.
28. **Penyelarasan Respons Reviewer:** Saat merancang draf surat tanggapan untuk Komentar #2 Reviewer 2, manfaatkan tabel komparasi kebocoran data dan nilai *p-value* McNemar langsung dari Seksi 7 panduan manual ini.

---

## 16. Profil Penulis Utama, Provenance Akademik & Metadata Sitasi

### 16.1 Tim Peneliti
Seluruh penulis beridentitas resmi di bawah naungan **Departemen Informatika, Fakultas Informatika, Universitas Negeri Surabaya (UNESA), Surabaya, Jawa Timur, Indonesia**:
1. **Dr. Ir. Ricky Eka Putra, S.Kom., M.Kom.** ([ORCID: 0000-0002-5515-7967](https://orcid.org/0000-0002-5515-7967)) - Corresponding Author (`rickyeka@unesa.ac.id`)
2. **Rezky Arisanti Putri, S.Kom., M.Kom.** ([ORCID: 0009-0000-8021-1833](https://orcid.org/0009-0000-8021-1833))
3. **Dr. Yuni Yamasari, S.Kom., M.Kom.** ([ORCID: 0000-0001-9719-3491](https://orcid.org/0000-0001-9719-3491))
4. **Rafy Aulia Akbar, S.Kom., M.Kom.** ([ORCID: 0009-0003-6991-0694](https://orcid.org/0009-0003-6991-0694))
5. **Assoc. Prof. Dr. Shukor Sanim Mohd Fauzi** ([ORCID: 0000-0003-4333-7853](https://orcid.org/0000-0003-4333-7853)) - School of Computing Sciences, College of Computing, Informatics and Mathematics, Universiti Teknologi MARA, Cawangan Perlis, Kampus Arau, 02600 Arau, Perlis, Malaysia (`shukorsanim@uitm.edu.my`)

### 16.2 Entri Metadata Sitasi
```bibtex
@article{putra2026multidomain,
  title={Multi-Domain Vision Transformer Fusion for Intersectional Demographic Classification from Facial Images},
  author={Putra, Ricky Eka and Putri, Rezky Arisanti and Yamasari, Yuni and Akbar, Rafy Aulia and Mohd Fauzi, Shukor Sanim},
  journal={IEEE Access},
  year={2026}
}

@inproceedings{putri2025dual,
  title={Dual Vision Transformer Integration for Race and Gender Recognition Based on Facial Images},
  author={Putri, Rezky Arisanti and Anifah, Lilik and Putra, Ricky Eka and Yamasari, Yuni and Akbar, Rafy Aulia},
  booktitle={2025 8th International Conference on Vocational Education and Electrical Engineering (ICVEE)},
  pages={1--6},
  year={2025},
  organization={IEEE}
}

@article{putri2025mdvit,
  title={MD-ViT: Multidomain Vision Transformer Fusion for Fair Demographic Attribute Recognition},
  author={Putri, Rezky Arisanti and Putra, Ricky Eka and Yamasari, Yuni},
  journal={Journal of Information Engineering and Educational Technology (JIEET)},
  volume={9},
  number={2},
  pages={64--79},
  year={2025}
}

@inproceedings{hupont2019demogpairs,
  title={DemogPairs: Quantifying the Impact of Demographic Imbalance in Deep Face Recognition},
  author={Hupont, Isabelle and Fernandez, Carles},
  booktitle={2019 14th IEEE International Conference on Automatic Face & Gesture Recognition (FG 2019)},
  pages={1--7},
  year={2019},
  doi={10.1109/FG.2019.8756625}
}
```

---

## 17. Riwayat Sesi Kerja AI Agent & Log Kronologis (`docs/sessions/` & `sessions/`)

Seluruh sesi kerja terpadu otonom dicatat secara teliti ke dalam direktori `docs/sessions/` dan dicerminkan pada `sessions/` untuk transparansi dan auditabilitas riset:

1. **`2026-09-06`**: Audit Paper dan Sinkronisasi LaTeX ID (`session_2026-09-06_agy_audit-paper-dan-sinkronisasi-latex-id.md`).
2. **`2026-09-07`**: Audit Sitasi dan Pembaruan Dokumentasi Sistem (`session_2026-09-07_agy_audit-sitasi-dan-pembaruan-dokumentasi-sistem.md`).
3. **`2026-09-08`**: Standardisasi IEEE dan Sitasi Interaktif Manuskrip (`session_2026-09-08_agy_standardisasi-ieee-dan-sitasi-interaktif-manuskrip.md`).
4. **`2026-10-27`**: Standardisasi Arsip Historis, Re-eksekusi 33 Notebook Aktif berbasis *instant cached weights*, Cermin Markdown `md/`, dan Formalisasi Paradigma Dual-Benchmark (`2026-10-27_standardisasi-arsip-re-eksekusi-notebook-dan-dokumentasi-dual-benchmark.md`).
5. **`2026-10-28`**: Dekonstruksi Review Resmi IEEE Access via Skill `ar-paper-revision-coach`, Penyusunan Roadmap Schema 7 (`08_revision_roadmap.md`), Nested Commitment Ledger Schema 11 (`09_revision_tracking.md`), Rangka Surat Sanggahan (`10_response_letter_skeleton.md`), dan Audit 856 Angka Numerik di `05_results.md` (`2026-10-28_dekonstruksi-review-ieee-roadmap-revisi-dan-audit-numerik-hasil.md`).
6. **`2026-10-29`**: Penyempurnaan Master Outline Manuskrip v1.1 (`paper_outline_v1.1.md`), Standardisasi Persamaan Eq. (1) s.d. (23), Evaluasi Figure 3 ViT v2.0 (`2026-10-29_penyempurnaan-paper-outline-v1.1-evaluasi-figure3-vit-dan-sinkronisasi-prompts.md`).
7. **`2026-10-31 (Sesi 1)`**: Audit Latensi Ekstraksi CPU Empiris (~1.487 ms Tri-Domain), Redesain Figure 3 ViT ke Format Vektor 300 DPI (`images/vit_v2.2.png`), Regenerasi Matriks Konfusi 6×6 Figure 4 v1.1, dan Penyelarasan Tabel Efisiensi Komputasi XIV & Komparasi Literatur XVI (`2026-10-31_audit-latensi-ekstraksi-cpu-redesign-figure3-v2.2-dan-sinkronisasi-outline.md`).
8. **`2026-10-31 (Sesi 2)`**: Instrumentasi Waktu Ekstraksi pada `1.1_vit-*.ipynb`, Pembangkitan Berkas JSON Metrik Waktu `experiment/code/times/`, Investigasi Bottleneck CUDA via `systematic-debugging` (In-Memory Processor Caching di `extraction.py`, speedup 30× ke ~42 ms/citra pada GPU RTX 4060), dan Verifikasi Native PyTorch (`2026-10-31_instrumentasi-waktu-ekstraksi-caching-processor-dan-debugging-cuda.md`).
