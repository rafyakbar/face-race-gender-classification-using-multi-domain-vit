# Standard Operating Procedure: Research Manuscript Pipeline (WORKFLOW.md)

Dokumen ini merupakan **panduan standar operasional universal (*Universal Research Manuscript Pipeline SOP*)** untuk mentransformasikan ide, metodologi, dan hasil eksperimen penelitian menjadi manuskrip publikasi jurnal internasional bereputasi tinggi (misal: IEEE, Elsevier, Springer, Nature, dsb.).

Pedoman ini bersifat **agnostik terhadap topik penelitian** (*project-independent*) dan dirancang untuk dapat direplikasi pada berbagai repositori riset berbasis kecerdasan buatan (*AI*), visi komputer (*Computer Vision*), pemrosesan bahasa alami (*NLP*), maupun komputasi biomedis.

---

## 🗺️ Kerangka Kerja Alur 5 Tahap (The 5-Stage Manuscript Lifecycle)

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                             TAHAP 1: OUTLINE MASTER                              │
│                                (paper_outline.md)                                │
│   - Cetak biru arsitektural (The Blueprint & Single Source of Truth)             │
│   - Memuat struktur bab, target jumlah kata per paragraf, dan alur narasi        │
│   - Master formulasi matematis kanonikal, skema penomoran tabel & gambar         │
│   - Wajib diaudit dan diverifikasi 100% sebelum masuk tahap penulisan draf       │
└────────────────────────────────────────┬─────────────────────────────────────────┘
                                         │
                                         ▼
┌──────────────────────────────────────────────────────────────────────────────────┐
│                       TAHAP 2: MODULAR MARKDOWN DRAFTS                           │
│                                   (paper/)                                       │
│   - Penulisan naskah narasi lengkap per sub-bagian dalam format Markdown (.md)   │
│   - Struktur modular: 1 file untuk 1 sub-seksi spesifik                          │
│   - Audit sitasi tingkat kalimat via paper/references.txt & paper/references/    │
│   - Kepatuhan ketat terhadap target kata per paragraf & registri acronyms.txt    │
│   - Integrasi tabel dan visualisasi data hasil eksperimen                        │
└────────────────────────────────────────┬─────────────────────────────────────────┘
                                         │
                    ┌────────────────────┴────────────────────┐
                    ▼                                         ▼
┌───────────────────────────────────────┐ ┌───────────────────────────────────────┐
│     TAHAP 3: LATEX BAHASA INDONESIA   │ │      TAHAP 4: LATEX BAHASA INGGRIS    │
│           (paper_latex_id/)           │ │           (paper_latex_en/)           │
│ - Implementasi template IEEE Access   │ │ - Implementasi template IEEE Access   │
│   (ieeeaccess.cls & IEEEtran.bst)     │ │   (ieeeaccess.cls & IEEEtran.bst)     │
│ - Modularisasi naskah (sections/*.tex)│ │ - Naskah final submission (Camera-    │
│ - Kompilasi master: access.tex ->     │ │   Ready / Submission Package)         │
│   access.pdf                          │ │ - Kompilasi master: access.tex ->     │
│ - Validasi struktur & tinjauan tim    │ │   access.pdf                          │
│                                       │ │ - Sinkronisasi 1-ke-1 label, rumus,   │
│                                       │ │   tabel, gambar, dan references.bib   │
└───────────────────────────────────────┘ └───────────────────┬───────────────────┘
                                                              │
                                    Keputusan Editorial /     │
                                    Peer Review Feedback      │
                                                              ▼
┌──────────────────────────────────────────────────────────────────────────────────┐
│     TAHAP 5: SIKLUS HIDUP REVISI PEER REVIEW & RESUBMISSION IEEE ACCESS          │
│                              (paper_reviews_ieee/)                               │
│   - Langkah 5.1: Dekonstruksi Komentar & Pembuatan Matriks Tanggapan             │
│   - Langkah 5.2: Eksekusi Eksperimen Komparatif & Validasi Bebas Kebocoran Data │
│   - Langkah 5.3: Pembaruan Naskah Modular Markdown (paper/*.md) & Traceability   │
│   - Langkah 5.4: Sinkronisasi LaTeX & Pembangkitan Dua Berkas PDF (Clean/Yellow) │
│   - Langkah 5.5: Finalisasi Point-by-Point Response Letter & Byline Change Form │
└──────────────────────────────────────────────────────────────────────────────────┘
```

---

## 📑 Rincian Struktur & Konvensi Penamaan Modul

### 1. Tahap 1: Outline Master (`paper_outline.md`)
Dokumen outline master berfungsi sebagai **kontrak ilmiah** yang mengunci:
- **Spesifikasi Dokumen:** Judul, profil penulis, afiliasi, abstrak terpadu, dan kata kunci.
- **Batasan Kata Paragraf:** Rentang kata minimum dan maksimum per paragraf (contoh: 100-150 kata untuk paragraf umum, 150-275 kata untuk tinjauan literatur).
- **Master Notasi Matematika:** Penomoran kanonikal persamaan $\text{Eq. } (1), (2), \dots, (N)$ beserta definisi simbol variabel.
- **Master Tabel & Gambar:** Penomoran resmi Tabel I..N dan Gambar 1..N, lengkap dengan petunjuk layout (*column width* vs *full width span* `table*`/`figure*`).
- **Matriks Sitasi:** Daftar artikel ilmiah pendukung yang wajib disitir per sub-bagian.

---

### 2. Tahap 2: Draf Modular Markdown (`paper/`)
Semua draf naskah ditulis dalam folder `paper/` secara terpisah per sub-bagian agar memudahkan fokus penulisan, audit berkas, dan pelacakan versi (*version control*).

#### Struktur Direktori Draf Modular Markdown:
```
paper/
├── 00_abstract.md                                      # Metadata, Judul, Abstrak, Kata Kunci
├── 01_introduction.md                                  # Section I: Latar belakang, urgensi, gap, kontribusi, organisasi
├── 02_related-works.md                                 # Section II: Tinjauan literatur tematik & posisi riset
├── 03_materials-and-methods_0-overview.md              # Section III: Teks pengantar metodologi & Figure 1 (Framework)
├── 03_materials-and-methods_a-dataset.md               # Section III-A: Deskripsi dataset DemogPairs & Figure 2 / Table I
├── 03_materials-and-methods_b-vision-transformer.md    # Section III-B: ViT feature extractor & Eq. (1)-(5) / Figure 3
├── 03_materials-and-methods_c-random-forest.md         # Section III-C: Random Forest formulation & Eq. (6)
├── 03_materials-and-methods_d-gaussian-naive-bayes.md  # Section III-D: Gaussian Naive Bayes formulation & Eq. (7)
├── 03_materials-and-methods_e-logistic-regression.md   # Section III-E: Logistic Regression formulation & Eq. (8)
├── 03_materials-and-methods_f-support-vector-machine.md# Section III-F: Support Vector Machine formulation & Eq. (9)
├── 03_materials-and-methods_g-classification-pipeline.md # Section III-G: Pipeline modular & 5-Fold Stratified GridSearchCV
├── 03_materials-and-methods_h-evaluation-metrics.md    # Section III-H: Metrik evaluasi OvR & Global (Eq. 10-17)
├── 04_results-and-discussion_a-global-performance.md   # Section IV-A: Benchmark performa global 28 model (Table VII-X)
├── 04_results-and-discussion_b-feature-ablation-study.md # Section IV-B: Analisis ablasi fitur & kontribusi domain
├── 04_results-and-discussion_c-intersectional-subgroup-performance.md # Section IV-C: Evaluasi performa subkelompok & disparitas (Table XI)
├── 04_results-and-discussion_d-error-pattern-assessment.md # Section IV-D: Analisis pola kesalahan & confusion matrix (Figure 4)
├── 04_results-and-discussion_e-comparison-with-prior-studies.md # Section IV-E: Perbandingan komparatif studi terdahulu (Table XII)
├── 05_conclusion.md                                    # Section V: Kesimpulan, limitasi riset, dan rencana masa depan
├── 06_references.md                                    # Section VI: Daftar pustaka format IEEE (entri [1]-[51])
├── 07_biographies.md                                   # Section VII: Biografi akademik seluruh penulis
├── acronyms.txt                                        # Registri pelacakan singkatan & akronim pertama kali (Rule 1.3)
├── ref_part_*.md                                       # 10 berkas log audit bibliografi modular (entri [1]-[51])
├── references.txt                                      # Registri audit sitasi tingkat kalimat (Sentence-Level Citation)
├── references/                                         # Direktori 51 berkas sumber bibliografi (.bib, .ris, .nbib, .bibtex)
└── images/                                             # Berkas aset visual gambar beresolusi tinggi untuk naskah
```

---

### 3. Tahap 3 & 4: Modular LaTeX (`paper_latex_id/` & `paper_latex_en/`)
Folder LaTeX mengimplementasikan template resmi penerbit IEEE Access (`ieeeaccess.cls` dan `IEEEtran.bst`).

#### Struktur Direktori LaTeX:
```
paper_latex_[id|en]/
├── access.tex                        # File induk LaTeX (memuat preamble, paket, dan perintah \input{})
├── access.pdf                        # Berkas PDF hasil kompilasi dua kolom standar IEEE Access
├── ieeeaccess.cls                    # Official IEEE Access document class
├── IEEEtran.bst                      # IEEE Access BibTeX bibliography style
├── references.bib                    # Basis data BibTeX terpadu dari seluruh sitasi naskah
├── images/                           # Aset visual diagram dan plot beresolusi tinggi
└── sections/                         # 21 berkas naskah LaTeX modular
    ├── 00_title.tex                  # \title{}, \author{}, \affil{}, \corresp{}
    ├── 00_abstract.tex               # \begin{abstract} ... \end{abstract} & \begin{keywords}
    ├── 01_introduction.tex           # \section{Introduction}
    ├── 02_related-works.tex          # \section{Related Works}
    ├── 03_materials-and-methods_*.tex# \section{Materials and Methods} & 9 sub-bagian modular
    ├── 04_results-and-discussion_*.tex# \section{Results and Discussion} & 5 sub-bagian modular
    ├── 05_conclusion.tex             # \section{Conclusion}
    └── 07_biographies.tex            # Biografi & foto seluruh penulis (\begin{IEEEbiography})
```

#### Alur Kompilasi Naskah LaTeX:
Untuk mengompilasi naskah LaTeX dari baris perintah (*terminal*):
```bash
pdflatex access.tex
bibtex access
pdflatex access.tex
pdflatex access.tex
```

---

### 4. Tahap 5: Siklus Hidup Revisi Peer Review & Resubmission IEEE Access (The 5th Stage: Peer Review & Resubmission SOP)

Tahap 5 diaktifkan ketika keputusan editorial dari jurnal telah diterima (misal: keputusan biner *Reject & Resubmit* IEEE Access dengan tepat **satu kesempatan** perbaikan). Tahap ini menjamin seluruh poin masukan ditangani secara komprehensif, terstruktur, berbasis bukti empiris, dan dapat dilacak dengan presisi tinggi.

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│             LANGKAH 5.1: DEKONSTRUKSI KOMENTAR & MATRIKS TANGGAPAN                      │
│             - Parsing surat keputusan Associate Editor & Reviewer                       │
│             - Pemetaan komentar ke Comments.md (Teks asli, terjemahan, aksi)            │
│             - Klasifikasi prioritas isu (P1: Fatal/Metodologi, P2: Komparasi, P3: Teks) │
└───────────────────────────────────────────┬─────────────────────────────────────────────┘
                                            │
                                            ▼
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│             LANGKAH 5.2: EKSEKUSI EKSPERIMEN & VALIDASI DUAL-BENCHMARK                  │
│             - Rekonstruksi partisi Subject-Disjoint (Zero Leakage, N=2,160 unseen)      │
│             - Pelaksanaan 28 model klasifikasi baru (5-Fold Stratified GridSearchCV)    │
│             - Preservasi Historical Baseline (Subject-Overlap, 93.70%) di archive/     │
│             - Uji hipotesis statistik inferensial (Paired McNemar Test & 95% Wilson CI) │
│             - Evaluasi disparitas interseksional (EOD 9.72 pp) & profil komputasi       │
└───────────────────────────────────────────┬─────────────────────────────────────────────┘
                                            │
                                            ▼
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│             LANGKAH 5.3: PEMBARUAN NASKAH MODULAR MARKDOWN (paper/*.md)                 │
│             - Penyusutan Section I: Introduction (merespons R1 Komentar #1)             │
│             - Restrukturisasi Section II & penambahan Eq. (1)-(3) (merespons R1 #2)     │
│             - Redesain Figure 3 arsitektur ViT & presisi notasi (R1 #3 & #4)            │
│             - Pembaruan hasil empiris Section IV & tabel studi terdahulu (R2 #1 & #2)   │
│             - Penyelarasan kepatuhan sitasi IEEE pada Bagian VI & references.txt (R1 #7)│
└───────────────────────────────────────────┬─────────────────────────────────────────────┘
                                            │
                                            ▼
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│             LANGKAH 5.4: SINKRONISASI LATEX & PEMBANGKITAN DUA BERKAS PDF               │
│             - Sinkronisasi teks, tabel, rumus, dan referensi ke paper_latex_en/         │
│             - Pembangkitan Clean PDF (access.pdf) tanpa penanda visual                  │
│             - Pembangkitan Highlighted PDF (access_highlighted.pdf) dengan tanda kuning │
│             - Verifikasi konsistensi nomor halaman, nomor kolom, dan nomor baris        │
└───────────────────────────────────────────┬─────────────────────────────────────────────┘
                                            │
                                            ▼
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│             LANGKAH 5.5: FINALISASI RESPONSE LETTER & BYLINE CHANGE FORM                │
│             - Penyusunan Point-by-Point Author Response Letter berstruktur tripartit    │
│               (Reviewer's Concern, Author's Response, Action to Remedy)                 │
│             - Pengisian formulir resmi Request for Byline Change (ko-penulis baru UiTM) │
│             - Verifikasi akhir menggunakan Resubmission Checklist (10 butir kepatuhan)  │
│             - Pengemasan paket pengunggahan portal (upload/ & paper_submission/)        │
└─────────────────────────────────────────────────────────────────────────────────────────┘
```

#### Langkah 5.1: Dekonstruksi Komentar & Pembuatan Matriks Tanggapan (`paper_reviews_ieee/Comments.md`)
1. **Analisis Surat Keputusan Editorial:**
   - Telaah surat dari Associate Editor untuk memahami konteks umum, tenggat waktu resubmission, dan regulasi khusus penerbit (kebijakan *binary peer review* IEEE Access).
   - Ekstrak seluruh butir komentar dari seluruh penelaah tanpa ada yang terlewat.
2. **Strukturasi Dokumen `Comments.md`:**
   - Simpan kompilasi pada [`paper_reviews_ieee/Comments.md`](paper_reviews_ieee/Comments.md).
   - Sajikan dalam format bilingual: teks asli bahasa Inggris verbatim diikuti terjemahan dan elaborasi Bahasa Indonesia formal.
   - Kategorisasikan setiap komentar penelaah:
     - **Reviewer 1 (R1 — 7 Komentar):**
       1. *Introduction Length:* Pendahuluan terlalu panjang dan wajib diringkas/dipadatkan.
       2. *Related Works Structure:* Penataan ulang tematik studi terdahulu dan penambahan formulasi matematis literatur.
       3. *Figure 3 Redesign:* Desain ulang diagram arsitektur ViT agar resolusi tajam, representatif, dan menjelaskan kebaruan (*novelty*).
       4. *Mathematical Formulations:* Perbaikan dan konsistensi penulisan notasi matematika serta persamaan encoder/klasifikasi.
       5. *Evaluation Metrics:* Kelengkapan metrik evaluasi multikelas (Akurasi, Presisi, Recall, F1-Score, dan EOD).
       6. *Language & Grammar:* Pemeriksaan tata bahasa Inggris akademik secara menyeluruh.
       7. *IEEE References Format:* Kepatuhan ketat gaya bibliografi IEEE Style Manual.
     - **Reviewer 2 (R2 — 2 Komentar Kritis):**
       1. *Comparison with Prior Works:* Matriks komparasi empiris langsung dengan penelitian mutakhir pada dataset yang sama (DemogPairs).
       2. *Subject Overlap & Cross-Subject Generalization:* Mengatasi cacat metodologis kebocoran data (*data leakage*) akibat kehadiran subjek yang sama pada train dan test set; validasi generalisasi sejati pada identitas wajah yang belum pernah dilihat (*unseen subjects*).
3. **Penyusunan Rencana Aksi (*Remedy Action Plan*):**
   - Tetapkan solusi konkret untuk setiap butir masukan.
   - Petakan modul berkas target di `paper/` dan `paper_latex_en/` yang akan dimodifikasi.

#### Langkah 5.2: Eksekusi Eksperimen Komparatif & Validasi Bebas Kebocoran Data (Dual-Benchmark)
1. **Pembangunan Primary Benchmark (Subject-Disjoint Partitioning):**
   - Lakukan partisi subjek terisolasi (*subject-disjoint split*): dari total 600 subjek (10.800 citra), isolasi **120 subjek independen (2.160 citra)** ke dalam *held-out test set* (360 citra per kelas interseksional). Sisa **480 subjek (8.640 citra)** dialokasikan untuk data latih dan validasi.
   - Jamin tingkat kebocoran identitas adalah **0,00% (Zero Leakage)**.
   - Terapkan 5-Fold Stratified Cross-Validation pada data latih dengan pembungkus `Pipeline` scikit-learn agar transformasi normalisasi (MinMaxScaler) dan reduksi dimensi (PCA) hanya di-*fit* pada fold pelatihan.
   - Jalankan optimasi hyperparameter menyeluruh (1.086 kombinasi parameter; 38.010 total *fit*) pada 28 model klasifikasi (4 keluarga: SVM, LR, RF, GNB).
   - Catat hasil benchmark primer: **Logistic Regression Tri-Domain meraih akurasi 88,66%** (Macro F1: 0,8868) dan **SVM Tri-Domain meraih akurasi 88,61%** (Macro F1: 0,8863).
2. **Preservasi Historical Baseline Archive (Subject-Overlap Baseline):**
   - Arsipkan 28 model eksperimen lama pada [`experiment/code/archive/`](experiment/code/archive/) (akurasi puncak SVM Tri-Domain: **93,70%**).
   - Gunakan data lama sebagai kontrol empiris untuk mengukur efek inflasi memori identitas wajah (*facial identity memorization*).
   - Penurunan nominal sebesar **-5,09 pp** (SVM) dan **-4,07 pp** (LR) mendokumentasikan batas atas distorsi kebocoran data dan memvalidasi integritas generalisasi out-of-subject.
3. **Uji Hipotesis Statistik Inferensial (Inferential Statistical Significance):**
   - Laksanakan **Paired McNemar Tests dengan koreksi kontinuitas Edwards** pada 2.160 citra uji subjek held-out:
     - Tri-Domain vs Single Face Biometrics pada SVM: $\chi^2 = 20,9612$, **$p = 3,46 \times 10^{-6} < 0,001$** (+53 citra benar bersih).
     - Tri-Domain vs Single Face Biometrics pada LR: $\chi^2 = 19,6923$, **$p = 6,78 \times 10^{-6} < 0,001$** (+49 citra benar bersih).
     - Membuktikan secara matematis bahwa keunggulan fusi multi-domain adalah kokoh dan tidak bergantung pada kebocoran identitas.
   - Hitung interval kepercayaan **95% Wilson Score CI** untuk seluruh 28 model (LR Tri: [87,25%, 89,93%]; SVM Tri: [87,20%, 89,88%]).
4. **Audit Efisiensi Komputasi & Algorithmic Fairness:**
   - Profil latensi inferensi per sampel: Logistic Regression menghasilkan **0,0054 ms/sampel** (>800x lebih cepat dibanding SVM 4,4481 ms).
   - Ukuran bobot model: Logistic Regression hanya **0,11 MB** (>330x lebih ringkas dibanding SVM 36,60 MB), menjadikannya arsitektur optimal untuk *edge devices*.
   - Evaluasi *Equal Opportunity Difference* (EOD): Disparitas antara recall tertinggi (White_Males 94,44%) dan terendah (Black_Females 84,72%) tercatat sebesar **9,72 percentage points**.

#### Langkah 5.3: Pembaruan Naskah Modular Markdown (`paper/*.md`) & Pelacakan Komitmen
1. **Pembaruan Isi Naskah Per Modul:**
   - `00_abstract.md`: Perbarui metrik utama menjadi 88,66% (LR) dan 88,61% (SVM) pada protokol bebas kebocoran subjek, serta sertakan baseline historis 93,70%.
   - `01_introduction.md`: Ringkas narasi pengantar sesuai R1 Komentar #1; perjelas butir kontribusi terkait dual-benchmark dan pembuktian bebas kebocoran identitas.
   - `02_related-works.md`: Restrukturisasi literatur secara tematik dan integrasikan formulasi matematis metode terdahulu $\text{Eq. } (1)\text{--}(3)$ sesuai R1 Komentar #2.
   - `03_materials-and-methods_*.md`:
     - Perbarui Figure 3 dengan diagram arsitektur ViT resolusi tinggi (R1 Komentar #3).
     - Standarkan formulasi matematika representasi multi-domain dan fungsi objektif klasifikasi $\text{Eq. } (4)\text{--}(17)$ (R1 Komentar #4).
     - Deskripsikan protokol partisi 480 subjek latih dan 120 subjek uji held-out secara transparan (R2 Komentar #2).
   - `04_results-and-discussion_*.md`:
     - Muat tabel performa global 28 model subject-disjoint (Table VII-X).
     - Sajikan tabel ablasi penurunan performa subject-overlap vs subject-disjoint.
     - Paparkan temuan uji signifikansi McNemar ($p < 0,001$) dan 95% Wilson Score CI.
     - Analisis matriks konfusi 6x6 dan profil disparitas interseksional (Table XI).
     - Sajikan tabel perbandingan langsung dengan studi terdahulu pada DemogPairs (Table XII, menjawab R2 Komentar #1).
   - `05_conclusion.md`: Selaraskan kesimpulan akhir dengan temuan empiris bebas kebocoran, limitasi dataset, dan arah riset edge computing.
   - `06_references.md` & `references.txt`: Pastikan seluruh 51 pustaka memenuhi format IEEE (R1 Komentar #7) dan tercatat pada registri sitasi kalimat.
2. **Pelacakan Komitmen Perubahan (*Commitment Ledger*):**
   - Lakukan verifikasi silang bahwa setiap komitmen perbaikan pada ulasan penelaah memiliki korespondensi nomor baris dan teks naskah yang konkret.

#### Langkah 5.4: Sinkronisasi LaTeX & Pembangkitan Dua Berkas PDF (Clean & Highlighted PDF)
1. **Sinkronisasi Kode Sumber LaTeX:**
   - Terapkan seluruh revisi teks dari `paper/*.md` ke berkas modular `paper_latex_en/sections/*.tex`.
   - Perbarui basis data `references.bib` dan metadata kepenulisan pada `00_title.tex`.
2. **Kompilasi Naskah Bersih (Clean PDF):**
   - Kompilasi `access.tex` melalui urutan standar (`pdflatex` $\rightarrow$ `bibtex` $\rightarrow$ `pdflatex` $\rightarrow$ `pdflatex`).
   - Hasilkan berkas **`access.pdf`** bebas dari penanda visual, siap untuk publikasi final.
3. **Pembangkitan Naskah Revisi Tersorot (Highlighted PDF):**
   - Sesuai regulasi IEEE Access Resubmission Checklist Butir 7, buat naskah revisi dengan penandaan warna kuning (*yellow highlight tool*) pada setiap perubahan teks, rumus baru, tabel baru, dan diagram yang dimodifikasi.
   - Simpan berkas sebagai **`access_highlighted.pdf`** (atau `access_revised_highlighted.pdf`).
   - Penandaan ini esensial bagi Associate Editor dan Reviewer untuk memverifikasi ketepatan revisi secara cepat.

#### Langkah 5.5: Finalisasi Berkas Respons Tertulis (*Point-by-Point Author Response Letter*) & Formulir Perubahan Daftar Penulis (*Byline Change*)
1. **Penyusunan Surat Tanggapan Resmi (*Author Response Letter*):**
   - Gunakan format template resmi IEEE Access ([`paper_reviews_ieee/IEEE-Access_Response-to-Reviewers-template.md`](paper_reviews_ieee/IEEE-Access_Response-to-Reviewers-template.md)).
   - Setiap butir komentar wajib dijawab menggunakan struktur baku tripartit IEEE:
     - **(a) Reviewer's Concern:** Pernyataan atau kutipan langsung komentar penelaah.
     - **(b) Author's Response:** Penjelasan logis, argumentasi ilmiah, dan konfirmasi penerimaan saran.
     - **(c) Action to Remedy:** Rincian tindakan revisi naskah secara spesifik, mencantumkan nomor halaman (*page*), nomor kolom (*column*), nomor persamaan/tabel (*Eq./Table*), serta kutipan teks blok naskah baru (*quoted block text*).
2. **Formulir Permohonan Perubahan Susunan Penulis (*Request for Byline Change*):**
   - Jika terdapat penambahan atau penyesuaian susunan penulis (seperti penambahan Dr. Shukor Sanim Mohd Fauzi dari Universiti Teknologi MARA untuk memperkuat analisis empirical software engineering), isi formulir formal [`paper_reviews_ieee/Request-for-Byline-Change.md`](paper_reviews_ieee/Request-for-Byline-Change.md).
   - Jelaskan kontribusi ilmiah substantif setiap penulis sesuai kriteria IEEE Publishing Operations Manual (Seksi 8.2.1.A.1) dan sertakan konfirmasi persetujuan dari seluruh penulis awal.
3. **Audit Kepatuhan Resubmission (10-Point Resubmission Checklist):**
   - Lakukan verifikasi mandiri menggunakan [`paper_reviews_ieee/Resubmission-Checklist.md`](paper_reviews_ieee/Resubmission-Checklist.md):
     - [x] Butir 1: Seluruh komentar reviewer telah terjawab tuntas.
     - [x] Butir 2: Tata bahasa dan ejaan telah ditinjau menyeluruh.
     - [x] Butir 3: Format persamaan matematika sesuai pedoman IEEE (huruf miring untuk variabel tunggal, huruf tegak untuk fungsi/label/satuan).
     - [x] Butir 4: Format sitasi dan daftar pustaka 100% konsisten dengan IEEE Style Manual.
     - [x] Butir 5: Berkas video (jika ada) memenuhi batasan ukuran (<100 MB).
     - [x] Butir 6: Dokumen Response to Reviewers lengkap dengan struktur concern-response-remedy.
     - [x] Butir 7: Berkas *Highlighted PDF* dengan penandaan kuning pada perubahan.
     - [x] Butir 8: Materi suplemen dikemas dalam arsip `.zip` (jika ada).
     - [x] Butir 9: Naskah utama dalam format LaTeX source package (`.zip`) lengkap dengan biografi dan foto.
     - [x] Butir 10: Naskah utama PDF bersih (*Clean PDF*).
4. **Pengemasan dan Pengunggahan Portal:**
   - Paketkan seluruh artefak final ke dalam direktori `paper_submission/` dan `upload/` untuk diunggah melalui [IEEE Author Portal](https://ieee.atyponrex.com/journal/ieee-access).

---

## 🔄 Matriks Pemetaan Universal (Universal Mapping Matrix)

| Modul Manuskrip | Draf Markdown (`paper/`) | Berkas LaTeX (`sections/*.tex`) | Elemen Standar yang Terkandung |
|:---|:---|:---|:---|
| **Judul & Penulis** | `00_abstract.md` | `00_title.tex` | Judul artikel, profil penulis, afiliasi, ORCID, korespondensi |
| **Abstrak & Keywords**| `00_abstract.md` | `00_abstract.tex` | Blok abstrak ringkas, daftar kata kunci (IEEE Keywords) |
| **I. Pendahuluan** | `01_introduction.md` | `01_introduction.tex` | Latar belakang, urgensi, kesenjangan riset, butir kontribusi, organisasi naskah |
| **II. Studi Terkait** | `02_related-works.md` | `02_related-works.tex` | Tinjauan pustaka tematik (klasifikasi atribut, fusi multi-domain, representasi ViT, disparitas), Eq. (1)-(3) |
| **III. Metodologi (Pengantar)**| `03_materials-and-methods_0-overview.md` | `03_materials-and-methods_0-overview.tex` | Narasi pengantar metodologi & Arsitektur Framework Sistem ([Figure 1](images/method.png)) |
| **III-A. Dataset** | `03_materials-and-methods_a-dataset.md` | `03_materials-and-methods_a-dataset.tex` | Deskripsi dataset DemogPairs, partisi subjek 480/120, [Figure 2](images/sample_Asian_Females.jpg), dan [Table I](#tab1) |
| **III-B. Vision Transformer** | `03_materials-and-methods_b-vision-transformer.md` | `03_materials-and-methods_b-vision-transformer.tex` | Ekstraksi fitur ViT [CLS], proyeksi patch, representasi multi-domain, [Figure 3](images/vit.png), Eq. (4)-(8) |
| **III-C. Random Forest** | `03_materials-and-methods_c-random-forest.md` | `03_materials-and-methods_c-random-forest.tex` | Formulasi ansambel Random Forest, kriteria Gini impurity, dan Eq. (9) |
| **III-D. Gaussian Naive Bayes**| `03_materials-and-methods_d-gaussian-naive-bayes.md`| `03_materials-and-methods_d-gaussian-naive-bayes.tex`| Teorema Bayes, asumsi independensi fitur Gaussian, dan Eq. (10) |
| **III-E. Logistic Regression**| `03_materials-and-methods_e-logistic-regression.md` | `03_materials-and-methods_e-logistic-regression.tex` | Regresi logistik multinomial, fungsi softmax, regularisasi L2, solver SAGA, dan Eq. (11) |
| **III-F. Support Vector Machine**| `03_materials-and-methods_f-support-vector-machine.md`| `03_materials-and-methods_f-support-vector-machine.tex`| Margin optimal, fungsi kernel RBF/polinomial, dan Eq. (12) |
| **III-G. Pipeline Klasifikasi**| `03_materials-and-methods_g-classification-pipeline.md`| `03_materials-and-methods_g-classification-pipeline.tex`| Pipeline terisolasi Scaler + PCA, 5-Fold Stratified Cross-Validation, GridSearchCV |
| **III-H. Metrik Evaluasi** | `03_materials-and-methods_h-evaluation-metrics.md` | `03_materials-and-methods_h-evaluation-metrics.tex` | Skema OvR, akurasi, presisi, recall, F1, McNemar test, Wilson CI, dan EOD, Eq. (13)-(17) |
| **IV-A. Performa Global** | `04_results-and-discussion_a-global-performance.md`| `04_results-and-discussion_a-global-performance.tex`| Tolok ukur 28 model Subject-Disjoint, evaluasi data uji held-out, ranking, [Table VII-X](#tab7) |
| **IV-B. Analisis Ablasi Fitur**| `04_results-and-discussion_b-feature-ablation-study.md`| `04_results-and-discussion_b-feature-ablation-study.tex`| Ablasi kontribusi domain, komparasi kebocoran data (Overlap vs Disjoint), McNemar test |
| **IV-C. Performa Subkelompok**| `04_results-and-discussion_c-intersectional-subgroup-performance.md`| `04_results-and-discussion_c-intersectional-subgroup-performance.tex`| Evaluasi 6 subkelompok interseksional & profil rentang disparitas EOD 9,72 pp, [Table XI](#tab11) |
| **IV-D. Pola Kesalahan** | `04_results-and-discussion_d-error-pattern-assessment.md`| `04_results-and-discussion_d-error-pattern-assessment.tex`| Analisis matriks konfusi 6x6 model terbaik LR/SVM Tri-Domain ([Figure 4](images/confusion_matrix_tri.png)) |
| **IV-E. Studi Terdahulu** | `04_results-and-discussion_e-comparison-with-prior-studies.md`| `04_results-and-discussion_e-comparison-with-prior-studies.tex`| Perbandingan langsung tolok ukur DemogPairs dengan studi terdahulu, [Table XII](#tab12) |
| **V. Kesimpulan** | `05_conclusion.md` | `05_conclusion.tex` | Kesimpulan utama, batasan penelitian, dan rekomendasi arah riset lanjutan |
| **Referensi** | `06_references.md` / `references.txt` | `references.bib` | Basis data BibTeX terpadu (`@article`, `@inproceedings`, `@book`) |
| **Biografi** | `07_biographies.md` | `07_biographies.tex` | Biografi akademik dan penyematan foto seluruh penulis |
| **Dossier Resubmission** | `paper_reviews_ieee/Comments.md` | `paper_reviews_ieee/` | Surat tanggapan point-by-point, Highlighted PDF, Byline Change form, Resubmission Checklist |

---

## 🛡️ Standar Mutu Akademik & Aturan Eksekusi (Quality Assurance)

Untuk memastikan manuskrip memenuhi standar jurnal internasional bereputasi tinggi:

1. **Prinsip Ground-Truth Empiris (Zero-Tolerance for Inconsistency):**
   - Seluruh angka metrik (Akurasi, Precision, Recall, F1, Loss, Latensi) wajib persis sama di semua representasi (kode, log eksperimen, markdown, dan LaTeX) hingga batas desimal yang ditentukan (standar: 4 angka di belakang koma untuk skor metrik, 2 angka untuk persentase).
2. **Kepatuhan Tipografi & Format:**
   - **Hindari penggunaan tanda pisah em dash (`—` atau `–`)** pada naskah jika dilarang oleh pedoman penerbit; gunakan tanda hubung standar (`-`), titik dua (`:`), atau tanda kurung `(...)`.
   - Pisahkan teks deskriptif biasa (`224 × 224`, `80/20`, rasio sampel) dari variabel matematika dalam math mode ($N=2.160$, $\mathbf{z}_L^0$).
   - Gunakan layout lebar penuh (`table*` atau `figure*`) hanya untuk tabel/grafik perbandingan multi-kolom yang lebar; gunakan layout kolom tunggal (`table` atau `figure`) untuk elemen kompak.
3. **Pemberian Kalimat Topik & Kohesi Paragraf:**
   - Setiap paragraf harus diawali dengan kalimat topik (*topic sentence*) yang kuat, diikuti kalimat penjelas berbobot dan sitasi pendukung, serta ditutup dengan kalimat transisi kohesif menuju paragraf berikutnya.
4. **Protokol Delegasi Subagent (Modular Drafting & Auditing):**
   - Saat menulis atau mengaudit draf manuskrip, delegasikan **1 subagent independen untuk 1 file spesifik** dengan instruksi yang terfokus agar konteks penulisan dan akurasi tetap maksimal.
5. **Kepatuhan Struktur Sintaksis SPOK & Kesiapan Translasi SVO:**
   - Setiap kalimat dalam draf naskah wajib memiliki struktur Subjek (S) dan Predikat (P) yang definitif untuk mencegah kalimat menggantung (*dangling sentences*). Variasikan antara pola S-P-O-K murni, transisi K-S-P-O terukur, dan bentuk pasif akademis objektif pada metodologi untuk mempermudah pemetaan ke struktur SVO/SVOC pada naskah LaTeX Bahasa Inggris standar IEEE.
6. **Sistem Audit Sitasi Tingkat Kalimat (Sentence-Level Citation Audit):**
   - Seluruh klaim literatur dan fakta eksternal dalam naskah Markdown wajib dicatat secara granular pada `paper/references.txt` dan diverifikasi kecocokan teks kutipannya terhadap berkas sumber di `paper/references/` sebelum ditransformasikan ke berkas `references.bib` pada naskah LaTeX.
7. **Pelacakan Akronim Terpusat (Centralized Acronym Registry):**
   - Seluruh singkatan teknis dicatat pada `paper/acronyms.txt` untuk memastikan kepatuhan aturan pemunculan pertama kali (*first-mention full form*) dan mencegah repetisi kepanjangan akronim pada paragraf-paragraf berikutnya.
8. **Format Sitasi Interaktif Naskah (Interactive In-Text Citations):**
   - Sitasi dalam draf naskah Markdown menggunakan tautan interaktif ganda `[[N]](06_references.md#refN)` yang terhubung langsung ke jangkar `<a id="refN"></a>` pada daftar pustaka Bagian VI. Sitasi jamak dipisahkan koma dan spasi (`[[1]](06_references.md#ref1), [[2]](06_references.md#ref2)`), diletakkan menempel tepat sebelum tanda baca terminal (`.` atau ` |`), dengan penomoran monotonik meningkat sesuai urutan kemunculan pertama pada naskah (IEEE style).
9. **Protokol Resubmission Biner & Pelacakan Komitmen (Fail-Closed Revision Governance):**
   - Dalam model penelaahan biner IEEE Access, setiap butir keberatan penelaah (*reviewer concern*) wajib ditanggapi secara afirmatif dengan tindakan korektif nyata (*action to remedy*).
   - Seluruh komitmen revisi wajib tercermin pada naskah Markdown, disinkronkan ke naskah LaTeX, serta ditandai sorotan kuning pada *Highlighted PDF*. Dilarang membuat janji atau klaim perbaikan tanpa modifikasi teks konkret yang dapat diverifikasi.
10. **Integritas Kepenulisan & Regulasi Byline (Authorship Byline Compliance):**
    - Setiap penambahan, penghapusan, atau penyusunan ulang urutan penulis pada tahap revisi wajib mematuhi IEEE Publishing Operations Manual (Seksi 8.2.1.A.1).
    - Penulis korespondensi wajib mengisi formulir resmi *Request for Byline Change* yang memuat justifikasi ilmiah mendalam per individu dan mengantongi persetujuan tertulis dari seluruh penulis awal sebelum diajukan ke Associate Editor.
