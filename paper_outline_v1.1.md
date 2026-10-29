# Paper Outline Terperinci (Versi 1.1 - Definitif Revisi) - IEEE Access (Manuscript ID: Access-2026-50857)

> **Status Versi**: **Versi 1.1 (Definitif Revisi IEEE Access / Subject-Disjoint Primary Benchmark)**  
> **Catatan Tata Kelola**: Berkas ini memuat outline naskah revisi komprehensif yang memenuhi seluruh rekomendasi penelaah IEEE Access (Primary Benchmark Subject-Disjoint 0% leakage, LR 88.66% / SVM 88.61%, uji McNemar, profil Edge AI, kalibrasi fairness EOD, Table I-XVI, Figure 1-4, Eq. 1-22). Untuk outline orisinal pra-revisi (Subject-Overlap 93.70%), silakan merujuk ke [paper_outline_v1.0.md](paper_outline_v1.0.md).  
> **Target Publikasi**: IEEE Access (Open Access, Q1 / Impact Factor: 3.4)  
> **Status Revisi**: *Reject & Resubmit* (Kesempatan Resubmission Tunggal Berbasis *Binary Peer Review*)  
> **Bahasa Naskah**: Bahasa Indonesia formal akademik dengan istilah teknis/ilmiah tetap dipertahankan dalam Bahasa Inggris baku  
> **Gaya Sitasi**: IEEE format ([1], [2], dst.)  
> **Topik Riset**: Klasifikasi Ras & Gender Interseksional Berbasis Fusi Fitur Multi-Domain Vision Transformer dan Classical Machine Learning Teroptimasi di Bawah Protokol Strict Subject-Disjoint Partitioning  

---

## 0. Global Writing Rules and Claim Boundaries (Standar Revisi IEEE Access)

### A. Allowed Claims and Core Focus
1. **Fokus Utama**: Evaluasi empiris komprehensif fusi representasi laten dari tiga domain visual wajah komplementer (*task-associated representations*: Biometrik Wajah, Ekspresi Emosi Wajah, dan Estimasi Usia Wajah) menggunakan Vision Transformer (ViT-Base) pra-latih (*offline feature extraction*) yang dipadukan dengan optimasi pipeline *classical machine learning* (5-Fold StratifiedGroupKFold GridSearchCV).
2. **Sistem Dual-Benchmark (Jawaban Reviewer 2 #2)**:
   - **Primary Benchmark (Subject-Disjoint Partitioning — Zero Identity Leakage)**: Evaluasi definitif pada subjek *held-out* yang belum pernah dilihat sebelumnya ($N = 2.160$ citra uji dari 120 subjek terisolasi sempurna; tepat 360 citra per kelas interseksional). Model terbaik dipimpin oleh **Logistic Regression (LR) Tri-Domain** dengan Akurasi **88.66%** (Macro F1: **0.8868**, 95% Wilson CI: [87.25%, 89.93%]) dan **Support Vector Machine (SVM) Tri-Domain** dengan Akurasi **88.61%** (Macro F1: **0.8863**, 95% Wilson CI: [87.20%, 89.88%]).
   - **Historical Baseline Archive (Subject-Overlap Split — 100% Identity Leakage)**: Replikasi partisi acak berbasis citra historis (8.640 latih / 2.160 uji, di mana seluruh 593 subjek uji hadir di data latih; SVM Tri-Domain meraih 93.70%). Disajikan secara eksplisit sebagai **studi ablasi kebocoran data (*data leakage ablation study*)** untuk menguantifikasi beban memorisasi identitas wajah (*facial identity memorization effect* sebesar 5.09 percentage points).
3. **Signifikansi Statistik Inferensial (Jawaban Reviewer 2 #5)**:
   - Keunggulan fusi multi-domain terhadap representasi wajah tunggal (*Single Face Biometrics*) terbukti **signifikan secara statistik** melalui *Paired McNemar Test with Edwards continuity correction* ($p = 3.46 \times 10^{-6} < 0.001$ pada SVM; $p = 6.78 \times 10^{-6} < 0.001$ pada LR).
   - Model LR Tri-Domain (88.66%) dan SVM Tri-Domain (88.61%) terbukti **setara secara statistik** (*statistically equivalent*, $p = 1.0000$, selisih bersih hanya +1 citra).
   - Penambahan domain usia biologis pada SVM dikualifikasikan secara jujur mengalami **kejenuhan representasi fitur laten asimtotik (*asymptotic feature saturation*)** ($p = 0.7343 > 0.05$), sementara pada LR linier memberikan kenaikan signifikan ($p = 0.0073 < 0.01$).
4. **Keunggulan Efisiensi Komputasi Ekstrem (Jawaban Reviewer 1 #5 & Reviewer 2 #8)**:
   - Meskipun akurasinya ekuivalen dengan SVM, Logistic Regression menawarkan inferensi **>820× lebih cepat** (**0.0054 ms/sampel** vs 4.4481 ms pada SVM) dan ukuran penyimpanan model **>330× lebih ringkas** (**0.11 MB** vs 36.60 MB pada SVM), menetapkannya sebagai model terbaik untuk implementasi komputasi tepi (*Edge AI / Mobile deployment*).
5. **Kalibrasi Klaim Keadilan Algoritmik (Jawaban Reviewer 2 #6)**:
   - Metrik *Equal Opportunity Difference* ($\text{EOD} = 9.72\text{ pp}$ antara White Males 94.44% vs Black Females 84.72%) dilaporkan murni sebagai indikator disparitas performa subkelompok empiris, dan secara tegas **tidak diklaim sebagai jaminan keadilan algoritmik universal**.
6. **Konteks Komparasi Literatur (Jawaban Reviewer 1 #6 & Reviewer 2 #7)**:
   - Perbandingan dengan studi terdahulu pada DemogPairs (misal Putri et al. 2025) disajikan sebagai **penempatan kontekstual (*contextual comparison*)**, bukan *controlled benchmark*, karena studi terdahulu mengevaluasi pada partisi *subject-overlap*.
7. **Standarisasi Tipografi & Konvensi IEEE**:
   - Dilarang keras menggunakan karakter *em dash* (—); gunakan tanda pisah biasa (- atau --), tanda kurung, atau koma.
   - Istilah pengklasifikasi distandardisasi: Support Vector Machine (SVM), Logistic Regression (LR), Random Forest (RF), Gaussian Naive Bayes (GNB).
   - Penamaan konfigurasi fitur seragam menggunakan direct sum `⊕`: `Face`, `Emotion`, `Age`, `Emotion ⊕ Face`, `Face ⊕ Age`, `Emotion ⊕ Age`, `Face ⊕ Emotion ⊕ Age`.
   - Seluruh elemen berurutan kronologis ketat: **Figure 1–4**, **Table I–XVI**, dan **Eq. (1)–(22)**.

### B. Negative Constraints and Disallowed Claims
1. **Dilarang menyembunyikan isu tumpang tindih identitas**: Wajib transparan menyajikan perbandingan *Subject-Disjoint* vs *Subject-Overlap*.
2. **Dilarang mengklaim "universal improvement"**: Akui secara objektif bahwa pada Random Forest dan GNB, konfigurasi dual-domain mencatatkan akurasi yang kompetitif/puncak dibanding tri-domain.
3. **Dilarang berspekulasi fenotipik berlebihan**: Penjelasan matriks konfusi harus didasarkan murni pada data distribusi frekuensi kesalahan, bukan asumsi antropologi biologis yang tidak terverifikasi.
4. **Dilarang overclaim generalisasi**: Kesimpulan dibatasi secara eksplisit pada 3 kelompok ras makro dataset DemogPairs (Asian, Black, White).

---

## Front Matter

### Paper Title
**Multi-Domain Vision Transformer Fusion for Intersectional Demographic Classification from Facial Images**  
*(Fusi Vision Transformer Multi-Domain untuk Klasifikasi Demografis Interseksional dari Citra Wajah)*

### Authors & Affiliations (5 Penulis Sesuai Formulir Byline Change IEEE Access)
1. **Dr. Ir. Ricky Eka Putra, S.Kom., M.Kom.** ([ORCID: 0000-0002-5515-7967](https://orcid.org/0000-0002-5515-7967)) — *Department of Informatics, Faculty of Informatics, Universitas Negeri Surabaya, Surabaya 60231, Indonesia* (Corresponding Author: `rickyeka@unesa.ac.id`)
2. **Rezky Arisanti Putri, S.Kom., M.Kom.** ([ORCID: 0009-0000-8021-1833](https://orcid.org/0009-0000-8021-1833)) — *Department of Informatics, Faculty of Informatics, Universitas Negeri Surabaya, Surabaya 60231, Indonesia*
3. **Dr. Yuni Yamasari, S.Kom., M.Kom.** ([ORCID: 0001-9719-3491](https://orcid.org/0001-9719-3491)) — *Department of Informatics, Faculty of Informatics, Universitas Negeri Surabaya, Surabaya 60231, Indonesia*
4. **Rafy Aulia Akbar, S.Kom., M.Kom.** ([ORCID: 0009-0003-6991-0694](https://orcid.org/0009-0003-6991-0694)) — *Department of Informatics, Faculty of Informatics, Universitas Negeri Surabaya, Surabaya 60231, Indonesia*
5. **Assoc. Prof. Dr. Shukor Sanim Mohd Fauzi** ([ORCID: 0000-0003-4333-7853](https://orcid.org/0000-0003-4333-7853)) — *School of Computing Sciences, College of Computing, Informatics and Mathematics, Universiti Teknologi MARA, Cawangan Perlis, Kampus Arau, 02600 Arau, Perlis, Malaysia* (`shukorsanim@uitm.edu.my`)

### Abstract
Satu paragraf padat terpadu (**target 180–220 kata**), terstruktur: **Latar Belakang → Tantangan & Kesenjangan → Metodologi yang Diusulkan → Hasil Subject-Disjoint & Inferensial → Kesimpulan & Dampak Edge AI**.
- **Latar Belakang & Tantangan**: Klasifikasi atribut demografis wajah secara simultan menghadapi tantangan variasi ekspresi dinamis, morfologi penuaan biologis, tumpang tindih visual (*phenotypic overlap*), serta kerentanan model terhadap kebocoran identitas individu (*identity leakage*).
- **Metode**: Penelitian ini mengusulkan kerangka fusi representasi multi-domain dari tiga Vision Transformer (ViT-Base) spesifik tugas yang dibekukan: biometrik wajah (`ViT-Face`), ekspresi afektif (`ViT-Emotion`), dan estimasi usia (`ViT-Age`). Representasi token `[CLS]` 768-d diekstraksi secara *offline*, difusikan menjadi vektor 2.304-d, dan dioptimasi melalui 5-Fold StratifiedGroupKFold GridSearchCV melintasi 4 famili pengklasifikasi klasik (RF, GNB, LR, SVM) pada dataset DemogPairs (10.800 citra, 600 identitas unik).
- **Protokol Evaluasi & Hasil Utama**: Di bawah protokol ketat **Subject-Disjoint Partitioning (Zero Identity Leakage)** pada 120 subjek *held-out* ($N = 2.160$), **Logistic Regression Tri-Domain** mencatatkan akurasi puncak **88.66%** (Macro F1: **0.8868**, 95% Wilson CI: [87.25%, 89.93%]) dengan latensi inferensi ekstrem **0.0054 ms/sampel** dan ukuran model **0.11 MB**, sedangkan **SVM Tri-Domain** meraih akurasi **88.61%** (Macro F1: **0.8863**). Uji McNemar berpasangan membuktikan keunggulan signifikan multi-domain atas biometrik wajah tunggal ($p < 0.001$) serta paritas prediktif antara LR dan SVM ($p = 1.0000$).
- **Kesimpulan**: Studi ablasi kebocoran data membuktikan bahwa penurunan 5.09 pp dari baseline historis (93.70%) menguantifikasi hilangnya memorisasi identitas, menetapkan kerangka kerja fusi ini sebagai representasi demografis sejati yang sangat efisien untuk implementasi Edge AI.

### Keywords
Facial demographic recognition, intersectional classification, multi-domain feature fusion, Vision Transformer, subject-disjoint evaluation, data leakage ablation, McNemar test, edge AI, DemogPairs.

---

## I. INTRODUCTION (Dipadatkan ~28% — Jawaban Reviewer 1 #1 & Reviewer 2 #1)

Struktur narasi direorganisasi menjadi 7 paragraf padat dan fokus langsung pada esensi masalah:

```
[Paragraph 1: Urgensi Pengenalan Demografis Wajah & Disparitas Interseksional]
                               │
                               ▼
[Paragraph 2: Limitasi Pemodelan Atribut Terisolasi vs Pendekatan Interseksional]
                               │
                               ▼
[Paragraph 3: Evolusi Arsitektur Visi Komputer & Representasi Vision Transformer]
                               │
                               ▼
[Paragraph 4: Kesenjangan Riset Metodologis & Tantangan Kebocoran Data]
                               │ (Transisi Kohesif)
                               ▼
[Paragraph 5: Kerangka Fusi Tri-Domain ViT & Protokol Subject-Disjoint]
                               │
                               ▼
[Paragraph 6: Empat Kontribusi Ilmiah Utama Naskah Revisi]
                               │
                               ▼
[Paragraph 7: Sistematika Organisasi Artikel]
```

### Paragraph 1: Urgensi Pengenalan Demografis Wajah & Disparitas Interseksional
- **Target Kata**: 110–130 kata.
- **Poin Narasi**:
  1. Pengenalan otomatis atribut ras dan gender wajah memegang peranan krusial pada tata kelola identitas digital, kontrol akses biometrik, forensik, dan personalisasi antarmuka cerdas.
  2. Berbagai studi independen dan evaluasi NIST menunjukkan bahwa model visi komputer komersial memperlihatkan disparitas performa yang merugikan kelompok minoritas tertentu, khususnya wanita berkulit gelap.
  3. Kesenjangan ini bersumber dari representasi fitur visual yang kurang tangguh terhadap variasi fenotipik dan pencahayaan lingkungan.

### Paragraph 2: Limitasi Pemodelan Atribut Terisolasi vs Pendekatan Interseksional
- **Target Kata**: 110–130 kata.
- **Poin Narasi**:
  1. Praktik umum memisahkan klasifikasi ras dan gender sebagai dua model independen gagal menangkap dinamika kesalahan pada persilangan subkelompok demografis tertentu.
  2. Formulasi interseksional terpadu (3 Ras × 2 Gender = 6 kelas) pada kondisi evaluasi seimbang (*balanced evaluation*) memungkinkan audit performa yang adil tanpa distorsi jumlah sampel.
  3. Namun, klasifikasi 6 kelas secara simultan menghadirkan batas keputusan (*decision boundary*) yang sangat kompleks akibat kemiripan visual antarsubkelompok.

### Paragraph 3: Evolusi Arsitektur Visi Komputer & Representasi Vision Transformer
- **Target Kata**: 140–170 kata.
- **Poin Narasi**:
  1. Transisi dari ekstraktor konvolusi lokal (CNN) menuju Vision Transformer (ViT) memungkinkan pemodelan relasi spasial global antarpatch wajah melalui mekanisme Multi-Head Self-Attention (MHSA).
  2. Kajian literatur terkini mengeksplorasi berbagai varian arsitektur untuk atribut wajah: analisis regio tengah wajah (Belcar et al., 2022), pembelajaran multi-task multi-skala (Liao et al., 2022), atensi paralel (Chen et al., 2023), transformer multi-aksis (Kalkatawi & Saeed, 2024), dan mitigasi generatif (Ramachandran & Rattani, 2023).
  3. Fusi multi-domain awal menggunakan representasi ganda (Putri et al. ICVEE 2025; JIEET 2025) membuktikan potensi penggabungan domain biometrik dengan emosi atau usia.

### Paragraph 4: Kesenjangan Riset Metodologis & Isu Kebocoran Data
- **Target Kata**: 120–140 kata.
- **Poin Narasi**:
  1. *Keterbatasan Single-Domain*: Representasi geometri biometrik statis rentan terhadap distorsi ekspresi dinamis dan perubahan usia.
  2. *Ancaman Identity Leakage*: Evaluasi konvensional berbasis *image-level random split* berisiko memasukkan foto dari orang yang sama ke subset latih dan uji, memicu model menghafal identitas individu (*shortcut learning*) alih-alih fitur demografis sejati.
  3. *Ketiadaan Uji Inferensial & Profil Efisiensi*: Studi terdahulu minim pembuktian signifikansi statistik formal (McNemar) dan belum mengkaji profil komputasi (latensi dan ukuran model) untuk implementasi praktis.

### Paragraph 5: Kerangka Fusi Tri-Domain ViT & Protokol Subject-Disjoint
- **Target Kata**: 140–165 kata.
- **Poin Narasi**:
  1. Mengusulkan kerangka fusi Tri-Domain ViT yang memadukan tiga representasi laten ortogonal: geometri biometrik statis (`ViT-Face`), ekspresi afektif dinamis (`ViT-Emotion`), dan morfologi penuaan biologis (`ViT-Age`).
  2. Mengimplementasikan protokol **Strict Subject-Disjoint Partitioning** pada dataset DemogPairs (600 subjek unik) untuk memastikan 0% kebocoran data identitas pada pengujian.
  3. Mengoptimasi 4 rumpun pengklasifikasi klasik (RF, GNB, LR, SVM) melalui pipeline modular Scaler-PCA bebas kebocoran dengan 38.010 penyesuaian validasi silang.

### Paragraph 6: Empat Kontribusi Ilmiah Utama (Penegasan Kebaruan — R1-1 & R2-1)
- **Target Kata**: 130–160 kata.
- **Empat Butir Kontribusi Formal (Bilingual)**:
  1. **A Multi-Domain ViT Latent Fusion Framework:** Merumuskan integrasi representasi laten dari tiga backbone Vision Transformer spesifik tugas yang dibekukan (`Face ⊕ Emotion ⊕ Age` = 2.304-d) untuk menghasilkan ruang fitur komplementer bagi klasifikasi interseksional.
  2. **Strict Subject-Disjoint Benchmark & Data Leakage Ablation:** Menetapkan tolok ukur bebas kebocoran identitas pertama pada DemogPairs (LR 88.66% / SVM 88.61%) dan menyajikan studi komparatif ablasi kebocoran data untuk menguantifikasi beban memorisasi identitas (5.09 pp drop dari baseline overlap 93.70%).
  3. **Inferential Hypothesis Testing & Asymptotic Saturation Characterization:** Membuktikan keunggulan signifikan multi-domain secara statistik ($p < 0.001$), membuktikan ekuivalensi prediktif LR vs SVM ($p = 1.0000$), serta mengkarakterisasi fenomena kejenuhan representasi asimtotik fitur usia pada SVM ($p = 0.7343$).
  4. **Comprehensive Computational Efficiency & Edge AI Validation:** Menyajikan profil komputasi lengkap yang membuktikan Logistic Regression memberikan inferensi >820× lebih cepat (0.0054 ms) dan penyimpanan >330× lebih kompak (0.11 MB) dibanding SVM, merealisasikan solusi klasifikasi demografis siap pakai untuk perangkat komputasi tepi.

### Paragraph 7: Sistematika Organisasi Artikel
- **Target Kata**: 50–70 kata.
- **Poin Narasi**: Menguraikan struktur naskah dari Section II (Related Works), Section III (Materials and Methods), Section IV (Results and Discussion), hingga Section V (Conclusion).

---

## II. RELATED WORKS (Restrukturisasi Tematik & Penambahan Rumus — Jawaban Reviewer 1 #2)

Bagian ini disusun dalam **3 subbab tematik terstruktur** yang dilengkapi **formulasi matematis formal**:

### A. Facial Demographic Attribute Estimation
- **Target Kata**: 120–140 kata.
- **Fokus Sintesis**: Menelusuri evolusi estimasi ras, etnisitas, dan gender dari deskriptor konvensional berbasis bagian tengah wajah (Belcar et al., 2022) dan rekayasa fitur manual ke representasi konvolusional dalam. Menyoroti kerentanan model terhadap bias dataset monorasial (Tahyudin et al., 2024), fenomena *Other-Race Effect*, serta keterbatasan lapisan *SoftMax end-to-end* yang rentan mengalami *overfitting* pada fitur berdimensi tinggi (Sunitha et al., 2022; Kalkatawi & Saeed, 2024).

### B. Vision Transformers in Facial Visual Analysis
- **Target Kata**: 140–160 kata.
- **Fokus Sintesis**: Menganalisis landasan teoretis arsitektur Vision Transformer (Dosovitskiy et al., 2020) dalam memodelkan citra wajah. Berbeda dengan bias induktif lokal pada CNN, ViT membagi citra masukan menjadi $N$ patch visual berukuran $P \times P$ kanal $C$, memproyeksikannya secara linier ke dimensi laten $D$, dan memodelkan interaksi spasial global melalui Multi-Head Self-Attention (MHSA):
  $$\mathbf{x}_p \in \mathbb{R}^{N \times (P^2 \cdot C)}, \quad N = \frac{HW}{P^2} \tag{1}$$
  $$\text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^T}{\sqrt{d_k}}\right)\mathbf{V} \tag{2}$$
- Mengulas eksplorasi transformer pada atribut wajah, analisis perambatan bias sosial pada encoder ViT berskala besar (Brinkmann et al., 2023), serta integrasi transformer multi-aksis (Kalkatawi & Saeed, 2024).

### C. Multi-Domain Representation and Feature Fusion
- **Target Kata**: 140–170 kata.
- **Fokus Sintesis**: Membahas perkembangan paradigma fusi fitur multi-skala dan multi-tugas untuk menangani kompleksitas wajah. Studi terdahulu mengembangkan jaringan berbagi paralel berbobot atensi (Chen et al., 2023) dan augmentasi generatif StyleGAN2 (Ramachandran & Rattani, 2023). Lebih lanjut, integrasi dual-domain berbasis ViT yang menggabungkan biometrik wajah dengan emosi (Putri et al. ICVEE 2025) atau usia (Putri et al. JIEET 2025) membuktikan keunggulan penggabungan representasi:
  $$\mathbf{z}_{\text{fusion}} = [\mathbf{f}_1 \,\|\, \mathbf{f}_2 \,\|\, \dots \,\|\, \mathbf{f}_M] \in \mathbb{R}^{\sum_{m=1}^M d_m} \tag{3}$$
- **Penempatan Kebaruan Riset**: Penelitian ini memperluas paradigma tersebut menuju integrasi Tri-Domain ViT (`Face ⊕ Emotion ⊕ Age` = 2.304-d) di bawah evaluasi bebas kebocoran identitas (*subject-disjoint*) dan optimasi komprehensif *classical machine learning*.

---

## III. MATERIALS AND METHODS

### Overview
- **Target Kata**: 150–190 kata.
- **Tujuan**: Menjelaskan arsitektur kerangka kerja penelitian dari citra masukan DemogPairs, ekstraksi paralel tiga backbone ViT pra-latih yang dibekukan, fusi konkatenasi $\mathbf{z}_{\text{tri}}$, hingga optimasi 5-Fold StratifiedGroupKFold GridSearchCV.
- **Elemen Wajib**: **Figure 1** (Diagram Kerangka Kerja End-to-End, Full Width `\begin{figure*}`).
  *Caption:* **Figure 1. End-to-End Framework of the Proposed Multi-Domain Vision Transformer Feature Fusion and Classical Classifier Optimization for Intersectional Race and Gender Classification.**

### A. Dataset & Subject-Disjoint Partitioning Protocol (R2-2 & R1-5)
- **Target Kata**: 200–240 kata (2 paragraf).
- **Paragraf 1 (Komposisi & Distribusi Subjek)**:
  - Dataset DemogPairs (Hupont & Fernández, IEEE FG 2019): 10.800 citra wajah terdistribusi seimbang sempurna pada 6 kelas interseksional (1.800 citra/kelas).
  - Terdiri atas **600 subjek/identitas unik** (100 subjek per kelas), di mana setiap subjek memiliki tepat 18 variasi foto dengan keragaman pose, pencahayaan, dan ekspresi.
  - **Elemen Wajib**: **Figure 2** (Contoh Citra 6 Subkelompok DemogPairs, Full Width `\begin{figure*}`).
    *Caption:* **Figure 2. Sample Images of the DemogPairs Dataset across Six Intersectional Demographic Subgroups: (a) Asian Females, (b) Asian Males, (c) Black Females, (d) Black Males, (e) White Females, and (f) White Males.**
- **Paragraf 2 (Protokol Subject-Disjoint Bebas Kebocoran)**:
  - Mengisolasi subjek secara tegas menggunakan modul `split_demogpairs_subject_disjoint` dan `StratifiedGroupKFold` (groups = `subject_id`).
  - **Data Latih**: 480 subjek (80 subjek/kelas = 8.640 citra, 80%).
  - **Data Uji Held-Out**: 120 subjek (20 subjek/kelas = 2.160 citra, 20%) dengan **0.00% kebocoran identitas**.
  - Prapemrosesan: Deteksi dan *face alignment* MTCNN, *cropping* terpusat, resolusi $224 \times 224$ piksel RGB, normalisasi intensitas kanal $[0, 1]$.
- **Elemen Wajib**: **Table I** (Distribusi Partisi Data Subject-Disjoint DemogPairs).

**Table I. DemogPairs Dataset Partition and Subject-Disjoint Demographic Subgroup Distribution.**

| Subgroup Interseksional | Ras Makro | Gender | Unique Subjects | Train Set (80% Subjects) | Held-Out Test Set (20% Subjects) | Total Citra |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Asian_Females** | Asian | Female | 100 | 80 subjek (1,440 citra) | 20 subjek (360 citra) | 1,800 |
| **Asian_Males** | Asian | Male | 100 | 80 subjek (1,440 citra) | 20 subjek (360 citra) | 1,800 |
| **Black_Females** | Black | Female | 100 | 80 subjek (1,440 citra) | 20 subjek (360 citra) | 1,800 |
| **Black_Males** | Black | Male | 100 | 80 subjek (1,440 citra) | 20 subjek (360 citra) | 1,800 |
| **White_Females** | White | Female | 100 | 80 subjek (1,440 citra) | 20 subjek (360 citra) | 1,800 |
| **White_Males** | White | Male | 100 | 80 subjek (1,440 citra) | 20 subjek (360 citra) | 1,800 |
| **Total** | **3 Ras** | **2 Gender** | **600 Subjek** | **480 Subjek (8,640 citra)** | **120 Subjek (2,160 citra)** | **10,800** |

### B. Vision Transformer Multi-Domain Feature Extraction (R1-3 & R2-3)
- **Target Kata**: 220–260 kata (2 paragraf).
- **Paragraf 1 (Arsitektur ViT & Redesain Figure 3)**:
  - Struktur ViT-Base: 12 lapisan transformer encoder, 12 attention heads ($d_k = 64$), dimensi embedding tersembunyi $D = 768$, patch $16 \times 16$ ($N = 196$ patch).
  - Proyeksi linier dan embedding posisi:
    $$\mathbf{z}_0 = [\mathbf{x}_{\text{class}}; \, \mathbf{x}_p^1\mathbf{E}; \, \dots; \, \mathbf{x}_p^N\mathbf{E}] + \mathbf{E}_{\text{pos}}, \quad \mathbf{E} \in \mathbb{R}^{(P^2C) \times D}, \; \mathbf{E}_{\text{pos}} \in \mathbb{R}^{(N+1) \times D} \tag{4}$$
  - Pemrosesan blok encoder:
    $$\mathbf{z}'_\ell = \text{MHSA}(\text{LN}(\mathbf{z}_{\ell-1})) + \mathbf{z}_{\ell-1}, \quad \mathbf{z}_\ell = \text{MLP}(\text{LN}(\mathbf{z}'_\ell)) + \mathbf{z}'_\ell \tag{5}$$
  - **Elemen Wajib**: **Figure 3** (Diagram Vektor Resolusi Tinggi 300+ DPI Arsitektur Ekstraksi ViT Paralel & Fusi Konkatenasi, Full Width `\begin{figure*}`).
    *Caption:* **Figure 3. Redesigned High-Resolution Architecture of the Parallel Multi-Domain ViT Feature Extraction Backbones, Layer-12 CLS Token Extraction, and Direct Sum Feature Concatenation Pipeline.**
- **Paragraf 2 (Spesifikasi Checkpoint HuggingFace & Fusi Konkatenasi)**:
  - Dokumentasi resmi 3 checkpoint pra-latih yang dibekukan (*frozen*):
    1. `ViT-Face` (`skutaada/VIT-VGGFace`): Pretrained pada VGGFace2 untuk biometrik geometri kraniofasial statis.
    2. `ViT-Emotion` (`dima806/facial_emotions_image_detection`): Pretrained untuk ekspresi afektif dinamis.
    3. `ViT-Age` (`dima806/facial_age_image_detection`): Pretrained untuk estimasi usia dan penuaan biologis.
  - Ekstraksi token `[CLS]` lapisan ke-12 ($\mathbf{z}_L^0$) dan normalisasi LayerNorm:
    $$\mathbf{f}_{\text{domain}} = \text{LN}(\mathbf{z}_L^0) \in \mathbb{R}^{768} \tag{6}$$
  - Fusi Tri-Domain via konkatenasi (direct sum):
    $$\mathbf{z}_{\text{tri}} = \mathbf{f}_{\text{face}} \oplus \mathbf{f}_{\text{emotion}} \oplus \mathbf{f}_{\text{age}} \in \mathbb{R}^{2304} \tag{7}$$
- **Elemen Wajib**:
  - **Table II** (Spesifikasi Checkpoint Model ViT Pra-Latih & Parameter Normalisasi — R2-3).
  - **Table III** (Skema Konfigurasi Fusi Fitur & Desain Studi Ablasi).

**Table II. Pre-trained Vision Transformer Backbone Specifications and Preprocessing Parameters.**

| Domain Model | HuggingFace Checkpoint Identifier | Pre-training Task & Corpus | Input Size | Per-Channel Normalization ($\mu, \sigma$) | Output Representation |
|---|---|---|:---:|---|:---:|
| **`ViT-Face`** | `skutaada/VIT-VGGFace` | Facial Biometrics (VGGFace2) | $224 \times 224 \times 3$ | $\mu = [0.485, 0.456, 0.406]$, $\sigma = [0.229, 0.224, 0.225]$ | Token `[CLS]` Layer 12 (768-D) |
| **`ViT-Emotion`** | `dima806/facial_emotions_image_detection` | Facial Expression (FER-2013) | $224 \times 224 \times 3$ | $\mu = [0.5, 0.5, 0.5]$, $\sigma = [0.5, 0.5, 0.5]$ | Token `[CLS]` Layer 12 (768-D) |
| **`ViT-Age`** | `dima806/facial_age_image_detection` | Biological Age Estimation | $224 \times 224 \times 3$ | $\mu = [0.5, 0.5, 0.5]$, $\sigma = [0.5, 0.5, 0.5]$ | Token `[CLS]` Layer 12 (768-D) |

**Table III. Multi-Domain Feature Fusion and Systematic Ablation Configurations.**

| # | Feature Scheme | Category | Input Source Domains | Feature Dimension |
|:---:|---|:---:|---|:---:|
| 1 | `Face` | Single-Domain | Static Craniofacial Biometrics (`skutaada/VIT-VGGFace`) | 768 |
| 2 | `Emotion` | Single-Domain | Dynamic Affective Expressions (`dima806/facial_emotions...`) | 768 |
| 3 | `Age` | Single-Domain | Biological Aging Morphology (`dima806/facial_age...`) | 768 |
| 4 | `Emotion ⊕ Face` | Dual-Domain | Affective Dynamics + Craniofacial Biometrics | 1,536 |
| 5 | `Face ⊕ Age` | Dual-Domain | Craniofacial Biometrics + Aging Morphology | 1,536 |
| 6 | `Emotion ⊕ Age` | Dual-Domain | Affective Dynamics + Aging Morphology | 1,536 |
| 7 | `Face ⊕ Emotion ⊕ Age` | Tri-Domain (Proposed) | Biometrics + Affective Dynamics + Aging Morphology | 2,304 |

### C. Random Forest
- **Target Kata**: 100–120 kata.
- **Poin Pembahasan**: Ensemble bagging dengan $B$ pohon keputusan, parameter subspace `max_features` ($\in \{\text{'sqrt'}, \text{'log2'}\}$), kedalaman pohon, kriteria Gini impurity, dan penalaan grid search.
- **Elemen Wajib**: **Table IV** (Ruang Pencarian Hyperparameter Random Forest — 288 kombinasi, 1.440 fits).

### D. Gaussian Naive Bayes
- **Target Kata**: 100–120 kata.
- **Poin Pembahasan**: Pengklasifikasi probabilistik berbasis Teorema Bayes dengan asumsi independensi fitur Gaussian:
  $$P(x_i \mid y = c) = \frac{1}{\sqrt{2\pi\sigma_{c,i}^2}} \exp\left(-\frac{(x_i - \mu_{c,i})^2}{2\sigma_{c,i}^2}\right) \tag{8}$$
- **Elemen Wajib**: **Table V** (Ruang Pencarian Hyperparameter GNB — 240 kombinasi, 1.200 fits).

### E. Logistic Regression
- **Target Kata**: 100–120 kata.
- **Poin Pembahasan**: Model multinomial Softmax ter-regularisasi $L_2$ dengan optimasi loss cross-entropy multi-kelas:
  $$P(y = c \mid \mathbf{x}) = \frac{e^{\mathbf{w}_c^T \mathbf{x} + b_c}}{\sum_{j=1}^K e^{\mathbf{w}_j^T \mathbf{x} + b_j}} \tag{9}$$
- Penalaan kekuatan penalti $C$ dan solver konvergens (`lbfgs`, `saga`, `newton-cg`).
- **Elemen Wajib**: **Table VI** (Ruang Pencarian Hyperparameter Logistic Regression — 270 kombinasi, 1.350 fits).

### F. Support Vector Machine
- **Target Kata**: 110–130 kata.
- **Poin Pembahasan**: Penentuan hyperplane pemisah margin maksimal non-linier menggunakan fungsi kernel (RBF dan polinomial):
  $$K(\mathbf{x}_i, \mathbf{x}_j) = (\gamma \langle \mathbf{x}_i, \mathbf{x}_j \rangle + \text{coef0})^d, \quad d \in \{2, 3\} \tag{10}$$
  *(di mana parameter $\text{coef0} = 0.0$ default pada implementasi standar `sklearn.svm.SVC`)*.
- **Elemen Wajib**: **Table VII** (Ruang Pencarian Hyperparameter SVM — 288 kombinasi, 1.440 fits).

### G. Classification Pipeline & Search Space Reconciliation (R2-4)
- **Target Kata**: 120–150 kata.
- **Arsitektur Rantai Transformasi Modular**:
  $$\mathbf{x} \xrightarrow{\text{Scaler}} \tilde{\mathbf{x}} \xrightarrow{\text{PCA}} \hat{\mathbf{x}} \xrightarrow{\text{Classifier}} \hat{y} \in \{0, 1, 2, 3, 4, 5\} \tag{11}$$
- **Rekonsiliasi Aritmatika Ruang Pencarian (Jawaban R2-4)**:
  - SVM: 288 kombinasi $\times$ 5 folds = 1.440 fits
  - LR: 270 kombinasi $\times$ 5 folds = 1.350 fits
  - RF: 288 kombinasi $\times$ 5 folds = 1.440 fits
  - GNB: 240 kombinasi $\times$ 5 folds = 1.200 fits
  - Total: **1.086 kombinasi hyperparameter** $\times$ 5 folds = 5.430 fits per skema fitur.
  - Melintasi 7 skema fitur: $5.430 \times 7 = \mathbf{38.010\text{ CV fits}}$ ditambah **28 refits akhir** pada keseluruhan set latih.
  - Seluruh penskalaan dan PCA difitting secara terisolasi hanya pada fold latih di dalam `Pipeline` scikit-learn untuk menjamin pencegahan kebocoran data.

### H. Evaluation Metrics & Inferential Statistical Testing (R2-5 & R2-6)
- **Target Kata**: 180–220 kata (2 paragraf).
- **Paragraf 1 (Metrik Subkelompok OvR & Agregasi Global)**:
  - Formulasi evaluasi One-vs-Rest (OvR) per kelas $c \in \{1, \dots, K\}$:
    $$\text{Accuracy}_c = \frac{TP_c + TN_c}{TP_c + TN_c + FP_c + FN_c} \tag{12}$$
    $$\text{Precision}_c = \frac{TP_c}{TP_c + FP_c} \tag{13}$$
    $$\text{Recall}_c = \frac{TP_c}{TP_c + FN_c} \tag{14}$$
    $$\text{F1-Score}_c = \frac{2 \cdot \text{Precision}_c \cdot \text{Recall}_c}{\text{Precision}_c + \text{Recall}_c} \tag{15}$$
  - Agregasi Global (Overall Accuracy dan Macro Average):
    $$\text{Accuracy}_{\text{Global}} = \frac{\sum_{c=1}^K TP_c}{N} \tag{16}$$
    $$\text{Precision}_{\text{Macro}} = \frac{1}{K} \sum_{c=1}^K \text{Precision}_c \tag{17}$$
    $$\text{Recall}_{\text{Macro}} = \frac{1}{K} \sum_{c=1}^K \text{Recall}_c \tag{18}$$
    $$\text{F1-Score}_{\text{Macro}} = \frac{1}{K} \sum_{c=1}^K \text{F1-Score}_c \tag{19}$$
- **Paragraf 2 (Uji McNemar Berpasangan, 95% Wilson CI & Metrik Keadilan EOD)**:
  - Uji McNemar berpasangan dengan koreksi kontinuitas Edwards untuk pasangan prediksi diskordan ($b$ dan $c$):
    $$\chi^2 = \frac{(|b - c| - 1)^2}{b + c} \tag{20}$$
    didukung oleh uji eksak binomial dua arah (*exact two-sided binomial test*).
  - Interval Kepercayaan 95% Wilson Score untuk proporsi akurasi $p$:
    $$\text{CI}_{95\%} = \frac{p + \frac{z^2}{2N} \pm z \sqrt{\frac{p(1-p)}{N} + \frac{z^2}{4N^2}}}{1 + \frac{z^2}{N}}, \quad z = 1.95996 \tag{21}$$
  - Disparitas Keadilan Algoritmik Equal Opportunity Difference (EOD):
    $$\text{EOD} = \max_{i, j \in \{1, \dots, K\}} |\text{Recall}_i - \text{Recall}_j| = \max \text{TPR} - \min \text{TPR} \tag{22}$$

---

## IV. RESULTS AND DISCUSSION

### A. Primary Benchmark Global Performance (Subject-Disjoint — R2-2)
- **Target Kata**: 350–420 kata (4 paragraf untuk 4 famili model + 1 paragraf sintesis).
- **Paragraf 1 (Random Forest — Table VIII)**:
  - Puncak performa pada dual-domain `Emotion ⊕ Face` (Akurasi 84.86%, Macro F1 0.8479) dan tri-domain `Face ⊕ Emotion ⊕ Age` (Akurasi 85.00%, Macro F1 0.8493).
- **Paragraf 2 (Gaussian Naive Bayes — Table IX)**:
  - Puncak performa pada dual-domain `Emotion ⊕ Face` (Akurasi 84.31%, Macro F1 0.8430), sedangkan tri-domain mencapai 83.61%. Seluruh konfigurasi memilih PCA 0.75.
- **Paragraf 3 (Logistic Regression — Table X — Model Juara 1)**:
  - LR Tri-Domain `Face ⊕ Emotion ⊕ Age` meraih performa tertinggi di seluruh pengujian: Akurasi **88.66%**, Macro F1 **0.8868**, 95% Wilson CI **[87.25%, 89.93%]** ($C=0.1$, solver saga, scaler MinMaxScaler, tanpa PCA). Mengungguli dual-domain terbaik (87.45%) dan single biometrik wajah (86.39%).
- **Paragraf 4 (Support Vector Machine — Table XI — Model Runner-up 1)**:
  - SVM Tri-Domain `Face ⊕ Emotion ⊕ Age` meraih Akurasi **88.61%**, Macro F1 **0.8863**, 95% Wilson CI **[87.20%, 89.88%]** ($C=10$, kernel RBF, gamma scale, tanpa PCA). Dual-domain `Emotion ⊕ Face` mencapai 88.43%.
- **Paragraf 5 (Sintesis Global 28 Model)**:
  - Urutan rerata performa lintas famili: $\text{SVM } (86.81\%) > \text{LR } (86.18\%) > \text{RF } (80.57\%) > \text{GNB } (78.37\%)$.
- **Elemen Wajib**:
  - **Table VIII** (Hasil Evaluasi Subject-Disjoint Random Forest).
  - **Table IX** (Hasil Evaluasi Subject-Disjoint Gaussian Naive Bayes).
  - **Table X** (Hasil Evaluasi Subject-Disjoint Logistic Regression).
  - **Table XI** (Hasil Evaluasi Subject-Disjoint Support Vector Machine).

### B. Comparative Ablation Study on Data Leakage & Statistical Significance (R2-2 & R2-5)
- **Target Kata**: 250–300 kata (2 paragraf).
- **Paragraf 1 (Ablasi Kebocoran Data: Overlap vs Disjoint — Table XII)**:
  - Membandingkan hasil historis (93.70% SVM Tri / 92.73% LR Tri) dengan tolok ukur *subject-disjoint* (88.61% SVM Tri / 88.66% LR Tri).
  - Penurunan nominal $\Delta = -5.09\text{ pp}$ pada SVM dan $\Delta = -4.07\text{ pp}$ pada LR membuktikan dan menguantifikasi besaran efek memorisasi identitas (*identity memorization*).
  - Penurunan terkecil pada LR Tri membuktikan stabilitas generalisasi model linier teratur terhadap data subjek baru.
- **Paragraf 2 (Pengujian Signifikansi Inferensial McNemar — Table XIII)**:
  - **Multi-domain vs Single Face**: SVM Tri vs Face ($+2.45\text{ pp}$, $\chi^2 = 20.9612, p = 3.46 \times 10^{-6} < 0.001$) dan LR Tri vs Face ($+2.27\text{ pp}$, $\chi^2 = 19.6923, p = 6.78 \times 10^{-6} < 0.001$) terbukti signifikan secara statistik, menolak hipotesis bahwa peningkatan fusi hanyalah artefak kebocoran data.
  - **Tri vs Dual (Saturasi Fitur Asimtotik)**: SVM Tri vs Dual ($+0.19\text{ pp}$, $+4\text{ citra}$, $p = 0.7343$) mengonfirmasi kejenuhan representasi laten pada model non-linier RBF, sedangkan pada LR linier penambahan usia memberikan kenaikan signifikan ($+1.20\text{ pp}$, $+26\text{ citra}$, $p = 0.0073 < 0.01$).
  - **Paritas Prediktif LR vs SVM**: Uji McNemar antara LR Tri dan SVM Tri menghasilkan $\chi^2 = 0.0000$ dan $p = 1.0000$ (selisih bersih +1 citra), mengonfirmasi kesetaraan inferensial keduanya.
- **Elemen Wajib**:
  - **Table XII** (Studi Komparatif Ablasi Kebocoran Data: Subject-Overlap vs Subject-Disjoint).
  - **Table XIII** (Hasil Uji McNemar Berpasangan dan Exact Binomial Test).

### C. Computational Efficiency Profiling (R1-5 & R2-8)
- **Target Kata**: 180–220 kata (1–2 paragraf).
- **Poin Narasi**:
  1. Durasi ekstraksi fitur ViT offline pada GPU NVIDIA: ~15.2 ms/citra per domain (~45.6 ms untuk fusi tri-domain).
  2. Latensi inferensi pengklasifikasi per sampel: **Logistic Regression mencatat 0.0054 ms/sampel**, >820× lebih cepat dari SVM (4.4481 ms) dan 10× lebih cepat dari Random Forest (0.0537 ms).
  3. Jejak penyimpanan model (*model footprint*): **LR hanya membutuhkan 0.11 MB**, >330× lebih ringkas dari bobot kernel SVM (36.60 MB) dan Random Forest (6.19 MB).
  4. Penegasan bahwa kombinasi `ViT Offline + Logistic Regression` merupakan arsitektur paling ideal dan tangguh untuk penyebaran pada komputasi tepi (*Edge AI / Internet of Things*).
- **Elemen Wajib**: **Table XIV** (Profil Efisiensi Waktu dan Jejak Komputasi Komparatif).

**Table XIV. Comprehensive Computational Efficiency and Memory Footprint Profile.**

| Classifier Model | Feature Scheme | Feature Dimension | Offline Extraction Time (GPU) | Inference Latency (ms/sample) | Speedup vs SVM | Serialized Model Size (MB) | Size Reduction vs SVM | Target Deployment Environment |
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **Logistic Regression (LR)** | **Tri-Domain** | **2,304** | **~45.6 ms** | **0.0054 ms** | **823.7×** | **0.11 MB** | **332.7×** | **Edge AI / Mobile / Embedded Systems** |
| Support Vector Machine (SVM) | Tri-Domain | 2,304 | ~45.6 ms | 4.4481 ms | 1.0× (Baseline) | 36.60 MB | 1.0× (Baseline) | High-Performance Server / Cloud |
| Random Forest (RF) | Tri-Domain | 2,304 | ~45.6 ms | 0.0537 ms | 82.8× | 6.19 MB | 5.9× | Server / Desktop |
| Gaussian Naive Bayes (GNB) | Dual-Domain | 1,536 | ~30.4 ms | 0.0083 ms | 535.9× | 0.78 MB | 46.9× | Embedded Systems |

### D. Intersectional Subgroup Performance & Fairness Calibration (R2-6)
- **Target Kata**: 200–240 kata (2 paragraf).
- **Paragraf 1 (Profil Subkelompok Model Teratas)**:
  - Evaluasi granular pada 6 subkelompok ($N = 360$ citra uji unseen per subkelompok) pada model LR Tri-Domain (88.66%) dan SVM Tri-Domain (88.61%).
  - White Males mencatat performa tertinggi (Recall 94.44%, F1 94.84% pada LR; Recall 94.44%, F1 94.18% pada SVM).
  - Black Females mencatat recall 84.72% (F1 84.96% pada LR; F1 86.16% pada SVM).
- **Paragraf 2 (Kalibrasi Batasan Keadilan Algoritmik)**:
  - Disparitas Equal Opportunity ($\text{EOD} = \text{Max TPR} - \text{Min TPR} = 94.44\% - 84.72\% = \mathbf{9.72\text{ pp}}$) dilaporkan secara transparan.
  - Penegasan objektif bahwa capaian ini mencerminkan tantangan variasi fenotipik dan kontras pencahayaan yang masih ada, serta **bukan bukti tercapainya keadilan algoritmik sempurna**.
- **Elemen Wajib**: **Table XV** (Kinerja Klasifikasi per-Subkelompok Demografis Model Tri-Domain Subject-Disjoint).

### E. Error Pattern Assessment (R1-4 & R2-9)
- **Target Kata**: 280–340 kata (3 paragraf).
- **Paragraf 1 (Dinamika Kesalahan 6×6 Figure 4)**:
  - Menganalisis matriks konfusi 6×6 pada data uji held-out ($N = 2.160$). Total kesalahan klasifikasi menurun dari 294 citra (Single Face 86.39%) menjadi 271 citra (Dual Emotion+Face 87.45%) dan mencapai titik terendah 245 citra pada Tri-Domain (88.66%).
- **Paragraf 2 (Dominasi Kesalahan Intra-Gender Lintas-Ras vs Minimnya Gender Confusion)**:
  - Kesalahan mayoritas terkonsentrasi antar-ras dalam gender yang sama (*same-gender cross-race*), misalnya `Asian_Females` keliru diprediksi sebagai `White_Females` atau `Black_Females`.
  - Sebaliknya, kesalahan lintas-gender (*cross-gender confusion*, misal wanita diprediksi pria) mendekati **0% (<0.4%)**, membuktikan bahwa representasi ViT mampu mengisolasi fitur gender secara kokoh.
- **Paragraf 3 (Kualifikasi Interpretasi Fenotipik Empiris)**:
  - Membatasi pernyataan tumpang tindih visual murni berdasarkan frekuensi sel *off-diagonal* matriks konfusi tanpa spekulasi biologis berlebih.
- **Elemen Wajib**: **Figure 4** (Matriks Konfusi Komparatif 6×6: Single, Dual, Tri-Domain pada Subject-Disjoint Test Set, Full Width `\begin{figure*}`).
  *Caption:* **Figure 4. Comparative 6×6 Confusion Matrices on the Held-Out Subject-Disjoint Test Set ($N = 2,160$): (a) Single-Domain Face Biometrics, (b) Dual-Domain Emotion ⊕ Face, and (c) Tri-Domain Face ⊕ Emotion ⊕ Age.**

### F. Contextual Comparison with Prior Studies on DemogPairs (R1-6 & R2-7)
- **Target Kata**: 180–220 kata (2 paragraf).
- **Paragraf 1 (Perbandingan Metrik Kuantitatif — Table XVI)**:
  - Membandingkan model usulan dengan studi terdahulu pada DemogPairs: MD-ViT + XGBoost (Putri et al. JIEET 2025: 89.07%), Dual-ViT + SVM (Putri et al. ICVEE 2025: 92.41%), dan baseline historis usulan (93.70%).
- **Paragraf 2 (Kualifikasi Protokol Partisi Kontekstual)**:
  - Memberikan catatan penegasan bahwa studi terdahulu menggunakan protokol *random stratified overlap*, sehingga perbandingan disajikan secara **kontekstual**, bukan sebagai tolok ukur terkontrol (*controlled benchmark*). Model subject-disjoint kita (88.66% LR / 88.61% SVM) merupakan tolok ukur bebas kebocoran pertama pada dataset ini.
- **Elemen Wajib**: **Table XVI** (Perbandingan Kontekstual terhadap Studi Terdahulu pada DemogPairs).

---

## V. CONCLUSION & LIMITATIONS (R1-7 & R2-10)

Bagian ini disusun dalam **2 paragraf terpadu tanpa sub-seksi**:

### Paragraph 1: Concluding Remarks and Scientific Findings
- **Target Kata**: 120–150 kata.
- **Poin Narasi**:
  1. Penelitian ini berhasil membuktikan efektivitas fusi representasi multi-domain Vision Transformer (`Face ⊕ Emotion ⊕ Age`) untuk klasifikasi 6 kelas interseksional demografis wajah.
  2. Di bawah protokol ketat **Subject-Disjoint Partitioning (Zero Data Leakage)**, Logistic Regression Tri-Domain meraih akurasi puncak **88.66%** (Macro F1: **0.8868**) dan SVM Tri-Domain meraih **88.61%** (Macro F1: **0.8863**).
  3. Uji McNemar berpasangan membuktikan keunggulan fusi multi-domain signifikan secara statistik ($p < 0.001$).
  4. Logistic Regression terbukti ekuivalen secara prediktif dengan SVM ($p = 1.0000$), namun menawarkan inferensi >820× lebih cepat dan penyimpanan >330× lebih hemat, menetapkannya sebagai model terbaik untuk penerapan praktis.

### Paragraph 2: Honest Limitations and Future Research Directions
- **Target Kata**: 150–200 kata.
- **Poin Narasi**:
  - **Limitations (Batasan Penelitian)**:
    1. *Cakupan Demografis*: Kesimpulan penelitian ini dibatasi secara eksplisit pada 3 kelompok ras makro dataset DemogPairs (Asian, Black, White); generalisasi ke kelompok multirasial lain (seperti Hispanik atau Timur Tengah) memerlukan pengujian empiris tambahan.
    2. *Ekstraksi Fitur Statis*: Ekstraksi representasi dilakukan secara *offline* menggunakan backbone ViT yang dibekukan tanpa *fine-tuning* terpadu secara simultan.
  - **Future Directions (Arah Riset Mendatang)**:
    1. *Cross-Dataset Validation*: Menguji kerangka fusi pada dataset eksternal skala liar (*in-the-wild*, seperti FairFace atau UTKFace).
    2. *End-to-End Cross-Attention Fusion*: Mengembangkan mekanisme atensi silang adaptif antardomain yang dilatih *end-to-end*.
    3. *Explainable AI (XAI)*: Menerapkan visualisasi atensi (*Attention Rollout*) untuk transparansi pertanggungjawaban etika AI (Responsible AI).

---

## Master Element Sequence & Layout Specifications

Tabel master ini merekapitulasi seluruh urutan kronologis kemunculan elemen (Gambar, Tabel, dan Persamaan) beserta format layout yang wajib digunakan dalam naskah LaTeX:

| Element ID | Tipe Elemen | Bab / Sub-seksi Kemunculan | Judul / Deskripsi Formal Lengkap | Format Layout LaTeX |
|:---:|:---:|:---:|---|:---:|
| **Figure 1** | Gambar | Section III (Overview) | *End-to-End Framework of the Proposed Multi-Domain Vision Transformer Feature Fusion and Classical Classifier Optimization for Intersectional Race and Gender Classification.* | **Full Width (`figure*`)** |
| **Figure 2** | Gambar | Section III.A (Paragraph 1) | *Sample Images of the DemogPairs Dataset across Six Intersectional Demographic Subgroups: (a) Asian Females, (b) Asian Males, (c) Black Females, (d) Black Males, (e) White Females, and (f) White Males.* | **Full Width (`figure*`)** |
| **Table I** | Tabel | Section III.A (Paragraph 2) | *DemogPairs Dataset Partition and Subject-Disjoint Demographic Subgroup Distribution.* | Column Width (`table`) |
| **Figure 3** | Gambar | Section III.B (Paragraph 1) | *Redesigned High-Resolution Architecture of the Parallel Multi-Domain ViT Feature Extraction Backbones, Layer-12 CLS Token Extraction, and Direct Sum Feature Concatenation Pipeline.* | **Full Width (`figure*`)** |
| **Table II** | Tabel | Section III.B (Paragraph 1) | *Pre-trained Vision Transformer Backbone Specifications and Preprocessing Parameters.* | Column Width (`table`) |
| **Table III** | Tabel | Section III.B (Paragraph 2) | *Multi-Domain Feature Fusion and Systematic Ablation Configurations.* | Column Width (`table`) |
| **Table IV** | Tabel | Section III.C (Random Forest) | *Hyperparameter Search Space for Random Forest Classifier.* | **Full Width (`table*`)** |
| **Table V** | Tabel | Section III.D (Gaussian NB) | *Hyperparameter Search Space for Gaussian Naive Bayes Classifier.* | **Full Width (`table*`)** |
| **Table VI** | Tabel | Section III.E (Logistic Reg) | *Hyperparameter Search Space for Logistic Regression Classifier.* | **Full Width (`table*`)** |
| **Table VII** | Tabel | Section III.F (Support Vector) | *Hyperparameter Search Space for Support Vector Machine Classifier.* | **Full Width (`table*`)** |
| **Table VIII** | Tabel | Section IV.A (Random Forest) | *Primary Benchmark Performance of Random Forest across Seven Feature Configurations on Subject-Disjoint Test Set ($N = 2,160$).* | **Full Width (`table*`)** |
| **Table IX** | Tabel | Section IV.A (Gaussian NB) | *Primary Benchmark Performance of Gaussian Naive Bayes across Seven Feature Configurations on Subject-Disjoint Test Set ($N = 2,160$).* | **Full Width (`table*`)** |
| **Table X** | Tabel | Section IV.A (Logistic Reg) | *Primary Benchmark Performance of Logistic Regression across Seven Feature Configurations on Subject-Disjoint Test Set ($N = 2,160$).* | **Full Width (`table*`)** |
| **Table XI** | Tabel | Section IV.A (Support Vector) | *Primary Benchmark Performance of Support Vector Machine across Seven Feature Configurations on Subject-Disjoint Test Set ($N = 2,160$).* | **Full Width (`table*`)** |
| **Table XII** | Tabel | Section IV.B (Ablasi Leakage)| *Comparative Ablation Study on Data Leakage: Historical Baseline (Subject-Overlap, 100% Identity Leakage) vs. Primary Benchmark (Subject-Disjoint, Zero Leakage) across Key Configurations.* | **Full Width (`table*`)** |
| **Table XIII** | Tabel | Section IV.B (Uji Statistik) | *Paired Inferential Hypothesis Testing (McNemar's Test & Exact Binomial Test) for Feature Fusion and Cross-Classifier Comparisons.* | **Full Width (`table*`)** |
| **Table XIV** | Tabel | Section IV.C (Komputasi) | *Comprehensive Computational Efficiency and Memory Footprint Profile.* | **Full Width (`table*`)** |
| **Table XV** | Tabel | Section IV.D (Subkelompok) | *Intersectional Subgroup Performance and Algorithmic Fairness Profile for Top-Performing Tri-Domain Models on the Held-Out Subject-Disjoint Test Set ($N = 2,160$).* | **Full Width (`table*`)** |
| **Figure 4** | Gambar | Section IV.E (Error Pattern) | *Comparative 6×6 Confusion Matrices on the Held-Out Subject-Disjoint Test Set ($N = 2,160$): (a) Single-Domain Face Biometrics, (b) Dual-Domain Emotion ⊕ Face, and (c) Tri-Domain Face ⊕ Emotion ⊕ Age.* | **Full Width (`figure*`)** |
| **Table XVI** | Tabel | Section IV.F (Studi Terdahulu)| *Contextual Comparison of Proposed Framework against Prior Studies on the DemogPairs Dataset.* | Column Width (`table`) |

### Daftar Lengkap Urutan Persamaan Matematika (Eq. 1 s.d. 22)

| Equation ID | Bab / Sub-seksi Kemunculan | Deskripsi Matematis / Nama Formula |
|:---:|:---:|---|
| **Eq. (1)** | Section II.B (*Related Works*) | *Patch Flattening and Sequence Linear Projection in Vision Transformers* |
| **Eq. (2)** | Section II.B (*Related Works*) | *Scaled Dot-Product Multi-Head Self-Attention (MHSA) Formulation* |
| **Eq. (3)** | Section II.C (*Related Works*) | *Multi-Domain Feature Concatenative Direct Sum Representation* |
| **Eq. (4)** | Section III.B (*Vision Transformer*) | *Vision Transformer Input Patch and Learnable Positional Embedding* |
| **Eq. (5)** | Section III.B (*Vision Transformer*) | *Transformer Encoder Layer Transformation (MHSA + MLP with LayerNorm)* |
| **Eq. (6)** | Section III.B (*Vision Transformer*) | *Domain-Specific [CLS] Token Representation Extraction from Layer 12* |
| **Eq. (7)** | Section III.B (*Vision Transformer*) | *Proposed Tri-Domain Feature Concatenation Vector ($\mathbf{z}_{\text{tri}} \in \mathbb{R}^{2304}$)* |
| **Eq. (8)** | Section III.D (*Gaussian NB*) | *Conditional Gaussian Likelihood Formulation for Continuous Features* |
| **Eq. (9)** | Section III.E (*Logistic Reg*) | *Multinomial Softmax Probability for Multi-Class Classification* |
| **Eq. (10)** | Section III.F (*Support Vector*) | *Support Vector Machine Polynomial Kernel Function Formulation* |
| **Eq. (11)** | Section III.G (*Pipeline*) | *Modular Transformation Pipeline: Scaler to PCA to Classifier* |
| **Eq. (12)** | Section III.H (*Evaluation*) | *Subgroup-Level One-vs-Rest (OvR) Classification Accuracy Formulation* |
| **Eq. (13)** | Section III.H (*Evaluation*) | *Subgroup-Level One-vs-Rest (OvR) Precision Formulation* |
| **Eq. (14)** | Section III.H (*Evaluation*) | *Subgroup-Level One-vs-Rest (OvR) Recall / True Positive Rate Formulation* |
| **Eq. (15)** | Section III.H (*Evaluation*) | *Subgroup-Level One-vs-Rest (OvR) F1-Score Harmonic Mean Formulation* |
| **Eq. (16)** | Section III.H (*Evaluation*) | *Overall Global Classification Accuracy on Held-Out Test Set* |
| **Eq. (17)** | Section III.H (*Evaluation*) | *Macro-Averaged Global Precision Formulation across Six Intersectional Classes* |
| **Eq. (18)** | Section III.H (*Evaluation*) | *Macro-Averaged Global Recall Formulation across Six Intersectional Classes* |
| **Eq. (19)** | Section III.H (*Evaluation*) | *Macro-Averaged Global F1-Score Formulation across Six Intersectional Classes* |
| **Eq. (20)** | Section III.H (*Evaluation*) | *Paired McNemar's Test Statistic with Edwards Continuity Correction* |
| **Eq. (21)** | Section III.H (*Evaluation*) | *Wilson Score 95% Confidence Interval for Empirical Accuracy Proportion* |
| **Eq. (22)** | Section III.H (*Evaluation*) | *Algorithmic Fairness Disparity Metric: Equal Opportunity Difference (EOD)* |
