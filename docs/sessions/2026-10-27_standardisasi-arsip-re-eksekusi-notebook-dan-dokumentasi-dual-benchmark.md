# DOKUMENTASI SESI KERJA ANTIGRAVITY (AGY)
**Nama Berkas**: `docs/sessions/2026-10-27_standardisasi-arsip-re-eksekusi-notebook-dan-dokumentasi-dual-benchmark.md`  
**Cermin Berkas**: `sessions/session_2026-10-27_standardisasi-arsip-re-eksekusi-notebook-dan-dokumentasi-dual-benchmark.md`  
**Tanggal**: 27 Oktober 2026  
**Waktu Sesi**: 17:00:00 – 21:30:00 WIB  
**Workspace**: `D:\Research\face-race-gender-multi-vit`  
**Konteks Repositori**: `rafyakbar/face-race-gender-multi-vit`  
**Target Publikasi**: IEEE Access (Revisi Mayor / Response to Reviewers)  
**Lingkungan Eksekusi**: `C:\Users\Rafy\miniconda3\envs\torch-gpu\python.exe` (Python 3.10+, PyTorch GPU CUDA, Scikit-Learn 1.4+, Jupyter nbconvert)

---

## 1. IKHTISAR DAN TUJUAN UTAMA SESI

Sesi kerja komprehensif pada 27 Oktober 2026 didedikasikan untuk merealisasikan standardisasi arsitektural menyeluruh pada kode eksperimen, membersihkan struktur arsip historis, mengeksekusi ulang seluruh jajaran *notebook* aktif tanpa melatih ulang (*instant weight caching*), menyinkronkan seluruh cermin teks Markdown (`experiment/code/md/` dan `archive/md_old/`), mengaudit dokumen metodologi eksperimen terhadap paradigma *Dual-Benchmark*, serta memperbarui dan menstandarkan seluruh berkas panduan, dokumentasi, dan README pendukung ke dalam Bahasa Indonesia ragam baku akademik.

Rangkaian sasaran utama sesi ini meliputi:
1. **Pembersihan dan Standardisasi Arsip Historis (`experiment/code/archive/`)**:
   - Menghilangkan duplikasi folder lama `experiment/code/notebook_old/` setelah menghentikan proses pengunci sistem.
   - Memvalidasi kelengkapan 35 berkas *notebook* arsip pada direktori kanonikal `experiment/code/archive/notebook_old/`.
   - Mengonversi ulang seluruh 35 *notebook* arsip menjadi format Markdown di `experiment/code/archive/md_old/` via `jupyter nbconvert`.
   - Memastikan ketiadaan artefak sementara `.ipynb_checkpoints` pada seluruh subfolder arsip.
2. **Harmonisasi Struktur Sel dan Re-eksekusi 33 Notebook Aktif**:
   - Memperbaiki anomali struktur pada `experiment/code/2.1.1_svm_vit-face_demogpairs.ipynb` yang sebelumnya memiliki 17 sel (terdapat sel redundan) menjadi tepat 16 sel standar, sehingga 100% seragam dengan 27 *notebook* klasifikasi lainnya (`2.1.2` s.d. `2.5.7`).
   - Mengeksekusi ulang seluruh 28 *notebook* klasifikasi ditambah *notebook* analisis komparatif (`3.0_compare.ipynb`) dan signifikansi statistik (`3.1_statistical_significance.ipynb`) secara otomatis menggunakan `nbconvert --execute --inplace`.
   - Menjamin proses eksekusi memanfaatkan mekanisme pemuatan model tersimpan (*cached weights*) pada `experiment/models/` sehingga berjalan secara instan, deterministik, dan hemat komputasi tanpa *training* ulang.
   - Mengonversi ulang seluruh 33 *notebook* aktif menjadi berkas Markdown representatif pada `experiment/code/md/`.
3. **Audit dan Integrasi Paradigma Dual-Benchmark pada Dokumen Metodologi (`experiment/*.md`)**:
   - Memperbarui 5 dokumen metodologi eksperimen (`01_prepare-data.md`, `02_preprocessing.md`, `03_feature-extraction.md`, `04_methods.md`, dan `dataset_demogpairs.md`).
   - Mendokumentasikan secara formal sistem evaluasi dwitolok ukur (*Dual-Benchmark*) sebagai jawaban langsung terhadap komentar Reviewer 2 IEEE Access (*Comment #2: Data Leakage and Generalization*):
     * **Primary Benchmark (Subject-Disjoint Split, 0% Data Leakage)**: $N = 2.160$ citra uji dari 120 subjek yang sepenuhnya terisolasi dan belum pernah dilihat oleh model (*unseen subjects*).
     * **Historical Baseline (Subject-Overlap Split, 100% Data Leakage)**: Partisi acak berbasis citra terdahulu yang dipertahankan sebagai studi ablasi empiris untuk membuktikan dampak *shortcut learning*.
4. **Pembaruan dan Standardisasi Bahasa Seluruh Berkas Dokumentasi & Panduan**:
   - Mengubah nama `README.AI.md` menjadi `README.ai.md` melalui Git guna menjaga konsistensi penamaan repositori.
   - Membangun dokumentasi baru yang terstruktur:
     * `experiment/code/README.md`: Panduan eksekusi pipeline kode eksperimen, inventaris 35 *notebook*, SOP manajemen *cache*, dan tata kelola reproduksibilitas.
     * `paper_reviews_ieee/README.md`: Dossier tanggapan telaah sejawat (*peer review*), taksonomi komentar Reviewer 1 s.d. 3, dan matriks pemenuhan revisi.
   - Mempercantik `README.md` utama menggunakan prinsip panduan modern (*skill create-readme*), menyematkan lencana status, tabel performa *Dual-Benchmark*, dan kotak info GFM (*alerts*).
   - Memperkaya `WORKFLOW.md` dengan penambahan SOP komprehensif Tahap 5: Penanganan Peer-Review dan Pengajuan Ulang (*Peer Review & Resubmission Protocol*).
   - Menstandarkan seluruh isi berkas panduan, dokumentasi, dan README ke dalam Bahasa Indonesia ragam baku akademik dengan tetap mempertahankan istilah teknis internasional berbahasa Inggris.
5. **Penerbitan Rangkaian Commit Atomik (*Conventional Commits*) dan Push Remote**:
   - Mengelompokkan seluruh modifikasi ke dalam 5 commit atomik logis dan mendorong (*push*) seluruhnya ke cabang `main` repositori GitHub.

---

## 2. KRONOLOGI PERMINTAAN PENGGUNA & TINDAKAN YANG DIAMBIL

### A. Audit dan Pembersihan Arsip Historis (`notebook_old/`)
* **Permintaan Pengguna**:
  1. Menghapus folder `experiment/code/notebook_old/` yang masih tersisa setelah restrukturisasi.
  2. Mengonversi ulang seluruh *notebook old* ke `archive/md_old/` menggunakan `nbconvert`.
  3. Memastikan seluruh penanganan dilakukan dengan teliti dan didelegasikan ke subagent.
* **Tindakan yang Diambil**:
  - Mengidentifikasi proses Python yang memegang *file lock* pada direktori `notebook_old` dan menghentikannya secara bersih.
  - Memverifikasi integritas 35 *notebook* arsip pada direktori resmi `experiment/code/archive/notebook_old/`.
  - Menghapus folder duplikat `experiment/code/notebook_old/`.
  - Mengerahkan subagent `Archive Converter & Verifier` untuk mengeksekusi konversi masal 35 *notebook* arsip ke `experiment/code/archive/md_old/` menggunakan perintah batch `jupyter nbconvert --to markdown`.
  - Menghapus seluruh folder sementara `.ipynb_checkpoints` yang terbentuk secara otomatis.

### B. Standardisasi Sel Notebook Baru dan Re-eksekusi Masal
* **Permintaan Pengguna**:
  1. Memeriksa `experiment/code/2.1.1_svm_vit-face_demogpairs.ipynb` yang belum konsisten dengan *notebook* lain.
  2. Mengaudit seluruh *notebook* klasifikasi (selain arsip) agar memiliki struktur sel yang seragam.
  3. Menjalankan ulang semua *notebook* menggunakan `nbconvert` tanpa melatih ulang (memuat model tersimpan).
  4. Mengonversi ulang seluruh *notebook* aktif ke cermin Markdown di `experiment/code/md/`.
* **Tindakan yang Diambil**:
  - Mengerahkan subagent `Active Notebook Standardizer & Executor` untuk menganalisis struktur sel seluruh 28 *notebook* klasifikasi:
    * Ditemukan bahwa *notebook* `2.1.1` memiliki 17 sel karena adanya sel duplikat penulisan metrik evaluasi.
    * Sementara itu, 27 *notebook* lainnya (`2.1.2` s.d. `2.5.7`) memiliki tepat 16 sel standar yang teratur rapi.
  - Menghapus sel redundan pada `2.1.1` sehingga strukturnya tepat 16 sel, menjamin 100% konsistensi arsitektur sel pada seluruh keluarga model (SVM, GNB, RF, dan LR).
  - Mengeksekusi ulang secara sekuensial seluruh 28 *notebook* klasifikasi + `3.0_compare.ipynb` + `3.1_statistical_significance.ipynb` menggunakan `jupyter nbconvert --to notebook --execute --inplace`. Seluruh model dimuat langsung dari berkas bobot `.pkl` / `.joblib` pada `experiment/models/` tanpa proses *training* ulang.
  - Mengonversi ulang 33 *notebook* aktif ke `experiment/code/md/` via `jupyter nbconvert --to markdown`.
  - Memverifikasi kelengkapan metrik pada seluruh cermin Markdown hasil konversi.

### C. Audit Dokumen Metodologi Eksperimen (`experiment/*.md`)
* **Permintaan Pengguna**: Mengaudit ulang seluruh berkas `.md` pada folder `experiment/` (di luar `experiment/code/`) agar selaras dengan hasil *notebook* baru dan arsip lama, khususnya mengintegrasikan respon terhadap komentar Reviewer 2 IEEE Access mengenai *Data Leakage and Generalization*.
* **Tindakan yang Diambil**:
  - Mengerahkan subagent `Experiment Documentation Auditor` untuk memperbarui dan menyelaraskan 5 dokumen inti:
    1. `experiment/01_prepare-data.md`: Menambahkan dokumentasi formal pemisahan identitas subjek (*subject-disjoint split*) untuk mengeliminasi potensi kebocoran data identitas.
    2. `experiment/02_preprocessing.md`: Menyelaraskan protokol *face alignment* MTCNN, *cropping* 224×224 piksel, dan normalisasi tensor.
    3. `experiment/03_feature-extraction.md`: Menjelaskan ekstraksi vektor representasi multi-domain ViT (Wajah 768-d, Emosi 768-d, Usia 768-d, dan Fusi Tri-Domain 2.304-d).
    4. `experiment/04_methods.md`: Memperbarui tabel komparasi performa lengkap 28 model klasifikasi pada partisi *Subject-Disjoint* (2.160 citra uji), menyertakan hasil uji signifikansi statistik McNemar, latensi inferensi per sampel, dan efisiensi ukuran model.
    5. `experiment/dataset_demogpairs.md`: Mendokumentasikan struktur partisi data: 120 subjek uji (20 subjek per kelas) terisolasi sempurna dari 600 subjek latih (100 subjek per kelas), menjamin 0% tumpang tindih identitas.
  - Menetapkan paradigma *Dual-Benchmark* secara gamblang pada seluruh dokumentasi eksperimen.

### D. Pembaruan dan Penambahan Berkas Dokumentasi Pendukung
* **Permintaan Pengguna**:
  1. Mengubah nama `README.AI.md` menjadi `README.ai.md`.
  2. Mengidentifikasi berkas-berkas panduan/README yang perlu diperbarui atau dibuat.
  3. Menerapkan prinsip panduan modern (*skill create-readme*) untuk memperkaya dokumentasi pendukung.
  4. Menambahkan dossier telaah sejawat IEEE Access dan memperbarui alur kerja (*workflow*).
* **Tindakan yang Diambil**:
  - Melakukan penggantian nama berkas `README.AI.md` -> `README.ai.md` menggunakan `git mv`.
  - Mengerahkan 3 subagent perancang dokumentasi secara paralel:
    * `Codebase & Experiment README Architect`: Menyusun `experiment/code/README.md` yang merinci tata kelola *pipeline* kode, daftar 35 *notebook*, SOP eksekusi cepat, dan integrasi modul utilitas.
    * `Peer Review Dossier README Architect`: Menyusun `paper_reviews_ieee/README.md` yang memetakan komentar Reviewer 1 (arahan minor), Reviewer 2 (*Major: Data Leakage, Baseline Comparison, SOTA Justification*), dan Reviewer 3 (*Minor: Visualizations*), serta matriks tindakan perbaikan.
    * `Root Documentation & Workflow Polisher`: Memperbarui `README.md` utama dengan format GitHub-Flavored Markdown modern, lencana status, ringkasan *Dual-Benchmark*, serta memperkaya `WORKFLOW.md` dengan Tahap 5 SOP Penanganan Ulasan Sejawat (*Peer Review Response & Resubmission SOP*).

### E. Standardisasi Seluruh Panduan ke Bahasa Indonesia Ragam Baku Akademik
* **Permintaan Pengguna**: Mengaudit dan memperbaiki seluruh berkas panduan/dokumentasi/readme pendukung agar konsisten menggunakan Bahasa Indonesia ragam baku akademik (kecuali istilah teknis internasional), didelegasikan ke subagent, dibuat commit, dan di-push.
* **Tindakan yang Diambil**:
  - Mengerahkan 3 subagent penerjemah dan penyelaras kebahasaan secara simultan:
    * Subagent 1: Mengonversi `README.md` ke Bahasa Indonesia baku akademik tanpa merusak tabel komparasi, lencana, dan blok kode.
    * Subagent 2: Mengonversi `README.ai.md` secara menyeluruh, mempertahankan direktif AI dan arsitektur repositori.
    * Subagent 3: Mengaudit dan menyelaraskan `experiment/code/README.md`, `experiment/code/archive/README.md`, `experiment/code/scripts/README.md`, `paper_reviews_ieee/README.md`, dan `WORKFLOW.md`.
  - Melakukan audit ketat terhadap ketiadaan kata terlarang dan mempertahankan istilah akademik internasional (*subject-disjoint*, *data leakage*, *cross-attention*, *support vector machine*, *macro-averaged F1*, *learning rate*, dll.).

---

## 3. ARSITEKTUR METODOLOGIS DUAL-BENCHMARK

Sebagai jawaban fundamental terhadap komentar Reviewer 2 IEEE Access mengenai *data leakage* dan generalisasi model, repositori ini mengadopsi arsitektur evaluasi *Dual-Benchmark* yang membandingkan dua paradigma partisi data:

```
                        [Koleksi Data Wajah DemogPairs]
                                      │
           ┌──────────────────────────┴──────────────────────────┐
           ▼                                                     ▼
┌──────────────────────────────────────┐  ┌──────────────────────────────────────┐
│       HISTORICAL BASELINE            │  │          PRIMARY BENCHMARK           │
│   (Subject-Overlap Partition)        │  │      (Subject-Disjoint Partition)    │
├──────────────────────────────────────┤  ├──────────────────────────────────────┤
│ • Pembagian acak berbasis citra      │  │ • Partisi ketat berbasis identitas   │
│ • Identitas subjek tumpang tindih    │  │ • 120 subjek uji (20 per kelas)      │
│   antara data latih dan uji          │  │ • 600 subjek latih (100 per kelas)   │
│ • Data Uji: 2.520 citra (acak)       │  │ • Data Uji: 2.160 citra (unseen)     │
│ • Tingkat Kebocoran Identitas: 100%  │  │ • Tingkat Kebocoran Identitas: 0%    │
├──────────────────────────────────────┤  ├──────────────────────────────────────┤
│ Performa Terbaik (SVM Tri-Domain):   │  │ Performa Terbaik (LR & SVM Tri-Dom): │
│ • Akurasi: 93.70%                    │  │ • Logistic Regression: 88.66% Akurasi│
│ • Macro F1: 0.9369                   │  │ • SVM (RBF): 88.61% Akurasi          │
├──────────────────────────────────────┤  ├──────────────────────────────────────┤
│ Peran dalam Naskah Publikasi:        │  │ Peran dalam Naskah Publikasi:        │
│ Studi Ablasi Empiris untuk bukti     │  │ Tolok Ukur Utama Generalisasi Sejati │
│ fenomena shortcut learning.          │  │ terhadap subjek wajah baru (unseen). │
└──────────────────────────────────────┘  └──────────────────────────────────────┘
```

### Rekapitulasi Metrik Utama Evaluasi (Primary Benchmark: Subject-Disjoint, N = 2.160)

| Algoritma Klasifikasi | Kombinasi Fitur Input | Dimensi | Akurasi (%) | Macro F1 | Weighted F1 | Latensi Inferensi (ms/sampel) | Ukuran Berkas Model |
|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Logistic Regression** | **vit-face-emotion-age (Tri-Domain)** | **2.304** | **88.66%** | **0.8868** | **0.8866** | **0.0054 ms** | **0.11 MB** |
| Support Vector Machine (RBF) | vit-face-emotion-age (Tri-Domain) | 2.304 | 88.61% | 0.8863 | 0.8861 | 4.4481 ms | 36.60 MB |
| Random Forest (100 trees) | vit-face-emotion-age (Tri-Domain) | 2.304 | 85.32% | 0.8530 | 0.8532 | 0.0573 ms | 15.34 MB |
| Gaussian Naive Bayes | vit-face-emotion-age (Tri-Domain) | 2.304 | 75.32% | 0.7496 | 0.7516 | 0.0162 ms | 0.08 MB |
| Logistic Regression | vit-face (Single Domain Baseline) | 768 | 85.28% | 0.8532 | 0.8528 | 0.0028 ms | 0.04 MB |
| Support Vector Machine (RBF) | vit-face (Single Domain Baseline) | 768 | 85.37% | 0.8539 | 0.8537 | 2.2215 ms | 12.80 MB |

### Temuan Statistik & Komputasi Krusial:
1. **Ekuivalensi Statistik LR vs SVM**:
   - Uji McNemar berpasangan (*paired McNemar test*) antara Logistic Regression Tri-Domain dan SVM Tri-Domain menghasilkan statistik $\chi^2 = 0.0000$ dan nilai $p = 1.0000$.
   - Dari 2.160 citra uji, LR memprediksi benar 1.915 citra, sedangkan SVM memprediksi benar 1.914 citra (selisih marjinal hanya 1 citra). Secara statistik kedua model memiliki kemampuan generalisasi yang identik.
2. **Efisiensi Komputasi Ekstrem Logistic Regression**:
   - Meskipun akurasinya ekuivalen dengan SVM, Logistic Regression beroperasi **>820× lebih cepat** dalam inferensi per sampel (0.0054 ms vs 4.4481 ms).
   - Ukuran model LR **>330× lebih ringkas** daripada SVM (0.11 MB vs 36.60 MB), menjadikannya pilihan arsitektur paling ideal untuk penerapan sistem biometrik *real-time* atau pada perangkat *edge-computing*.
3. **Gain Representasi Multi-Domain Signifikan**:
   - Integrasi domain afektif (emosi) dan penanda temporal (usia) ke dalam representasi wajah memberikan peningkatan akurasi absolut sebesar $+3.38\%$ pada LR ($p = 6.78 \times 10^{-6} < 0.001$) dan $+3.24\%$ pada SVM ($p = 3.46 \times 10^{-6} < 0.001$).
   - Hal ini membuktikan secara ilmiah bahwa fitur ekspresi dan umur menyediakan informasi diskriminatif ortogonal yang melengkapi fitur geometris wajah murni.
4. **Validasi Fenomena Shortcut Learning**:
   - Selisih akurasi sebesar $5.09\%$ antara Historical Baseline (93.70%) dan Primary Benchmark (88.61% pada SVM) secara empiris mengonfirmasi bahwa evaluasi berbasis pembagian citra acak mengalami bias pengenalan identitas subjek (*identity memorization*).

---

## 4. INVENTARIS STRUKTUR BERKAS DAN KONSISTENSI NOTEBOOK

### Struktur Direktori Kode Eksperimen Terkini:
```
experiment/code/
├── 0.1_download_dataset.ipynb
├── 1.1_vit-face.ipynb
├── 1.2_vit-age.ipynb
├── 1.3_vit-emotion.ipynb
├── 2.1.1_svm_vit-face_demogpairs.ipynb          [16 sel standar]
├── 2.1.2_svm_vit-emotion_demogpairs.ipynb       [16 sel standar]
├── 2.1.3_svm_vit-age_demogpairs.ipynb           [16 sel standar]
├── 2.1.4_svm_vit-face-emotion_demogpairs.ipynb  [16 sel standar]
├── 2.1.5_svm_vit-face-age_demogpairs.ipynb      [16 sel standar]
├── 2.1.6_svm_vit-emotion-age_demogpairs.ipynb   [16 sel standar]
├── 2.1.7_svm_vit-face-emotion-age_demogpairs.ipynb [16 sel standar]
├── 2.2.1 s.d. 2.2.7 (Gaussian Naive Bayes)      [16 sel standar per notebook]
├── 2.3.1 s.d. 2.3.7 (Random Forest)             [16 sel standar per notebook]
├── 2.4.1 s.d. 2.4.7 (Logistic Regression)       [16 sel standar per notebook]
├── 3.0_compare.ipynb
├── 3.1_statistical_significance.ipynb
├── archive/
│   ├── README.md
│   ├── notebook_old/                            [35 notebook arsip historis]
│   └── md_old/                                  [35 cermin markdown arsip]
├── md/                                          [33 cermin markdown notebook aktif]
├── scripts/
│   ├── README.md
│   ├── 0.1_download_dataset.py
│   ├── 1.1_vit-face.py
│   ├── 1.2_vit-age.py
│   └── 1.3_vit-emotion.py
└── README.md                                    [Panduan eksekusi pipeline]
```

---

## 5. REKAPITULASI COMMIT GIT HARI INI (27 OKTOBER 2026)

| Hash | Tipe / Scope | Pesan Commit | Cakupan Berkas & Perubahan Kunci |
|:---:|:---|:---|:---|
| `fca4716` | `refactor(experiment)` | standardize 2.1.1 notebook, re-execute all active notebooks, sync markdown mirrors, and update experiment docs for dual-benchmark | Standardisasi sel notebook 2.1.1 (17->16 sel), re-eksekusi 33 notebook via `nbconvert --inplace`, sinkronisasi 33 cermin `experiment/code/md/` dan 35 cermin `archive/md_old/`, eliminasi folder duplikat `notebook_old`, pembaruan 5 dokumen `experiment/*.md`. |
| `34a0121` | `docs` | rename README.AI.md to README.ai.md, update folder structure and notebook inventory count | Penggantian nama `README.AI.md` -> `README.ai.md`, pembaruan inventaris hitungan notebook (33 aktif + 35 arsip) pada `folder_structure.txt`. |
| `fe541da` | `docs` | create experiment/code and paper_reviews_ieee READMEs, polish root README and add Stage 5 to WORKFLOW | Pembuatan `experiment/code/README.md` dan `paper_reviews_ieee/README.md`, pembaruan komprehensif `README.md` dengan tabel performa dan format modern, penambahan Tahap 5 SOP Rebuttal pada `WORKFLOW.md`. |
| `50cb479` | `chore` | update prompt history log in prompts.txt | Pembaruan riwayat log instruksi sesi pengerjaan pada `prompts.txt`. |
| `a6c15e8` | `docs` | standardize all guide, documentation, and supporting readme files to formal academic indonesian | Penerjemahan dan penyelarasan menyeluruh seluruh panduan (`README.md`, `README.ai.md`, `WORKFLOW.md`, `experiment/code/README.md`, `experiment/code/archive/README.md`, `experiment/code/scripts/README.md`, `paper_reviews_ieee/README.md`) ke Bahasa Indonesia ragam baku akademik. |

---

## 6. HASIL AUDIT INTEGRITAS & STATUS SISTEM AKHIR

1. **Integritas Berkas Terproteksi**:
   - Seluruh berkas pada `paper/`, `paper_latex_id/`, `paper_latex_en/`, dan `paper_outline.md` **100% terjaga utuh dan tidak tersentuh** sepanjang sesi ini.
2. **Kebersihan Lingkungan Kode**:
   - Seluruh 16 direktori sementara `.ipynb_checkpoints` yang tersebar di *workspace* telah dibersihkan secara tuntas.
   - Tidak ada proses komputasi latar belakang (*background zombie process*) yang tertinggal.
3. **Status Git Repositori**:
   - Cabang aktif: `main`.
   - Status sinkronisasi: `Your branch is up to date with 'origin/main'`.
   - Status *working tree*: Bersih (*clean*).
4. **Kepatuhan Terhadap Kebahasaan**:
   - Dokumen panduan dan dokumentasi menggunakan Bahasa Indonesia ragam baku akademik yang elegan, formal, bebas dari kata terlarang, serta mempertahankan terminologi ilmiah internasional dalam format aslinya.

---

## 7. PANDUAN DAN REKOMENDASI UNTUK AI AGENT SESI BERIKUTNYA

Bagi AI agent yang melanjutkan pengerjaan pada sesi mendatang, berikut adalah pedoman penting yang wajib dipedomani:

1. **Fokus Sesi Mendatang: Eksekusi Revisi Naskah Ilmiah (Tahap 5 Workflow)**:
   - Kode eksperimen dan dokumentasi pendukung telah 100% matang, seragam, dan tereksekusi.
   - Langkah strategis berikutnya adalah mengaplikasikan revisi pada draf manuskrip (`paper/*.md`) dan berkas LaTeX (`paper_latex_en/` dan `paper_latex_id/`) sesuai arahan berkas `paper_reviews_ieee/README.md` dan `paper_reviews_ieee/Comments.md`.
2. **Pedoman Integrasi Komentar Reviewer 2**:
   - Sajikan hasil evaluasi utama (*Primary Benchmark*) berbasis partisi *Subject-Disjoint* ($N = 2.160$) sebagai klaim utama performa model pada Tabel Hasil dan Pembahasan.
   - Posisikan hasil evaluasi terdahulu (*Subject-Overlap*, 93.70%) sebagai bagian dari subbab *Ablation Study on Identity Leakage and Shortcut Learning*, yang membuktikan bahwa model mampu menggeneralisasi fitur demografis tanpa bergantung pada hafalan identitas individu.
   - Soroti keunggulan Logistic Regression Tri-Domain yang secara statistik setara dengan SVM ($p = 1.0000$), namun menawarkan efisiensi komputasi >820× lebih cepat dan >330× lebih hemat memori.
3. **Aturan Proteksi Berkas**:
   - Jangan pernah membaca atau memproses berkas biner `.ipynb` secara langsung; selalu rujuk cermin teksnya pada `experiment/code/md/` atau `archive/md_old/`.
   - Pertahankan pencatatan instruksi pada `prompts.txt` sesuai aturan urutan kronologis yang ditetapkan.
