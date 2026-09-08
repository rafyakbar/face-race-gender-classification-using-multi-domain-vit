# DOKUMENTASI SESI KERJA ANTIGRAVITY (AGY)
**Nama Berkas**: `sessions/session_2026-09-07_agy_audit-sitasi-dan-pembaruan-dokumentasi-sistem.md`  
**Tanggal**: 07 September 2026  
**Waktu Sesi**: 16:30:00 – 21:35:00 WIB  
**Workspace**: `D:\Research\face-race-gender-classification-using-multi-domain-vit`  
**Konteks Repositori**: `rafyakbar/face-race-gender-classification-using-multi-domain-vit`  
**Target Publikasi**: IEEE Access (Template resmi `ieeeaccess.cls`, format 13 halaman)

---

## 1. IKHTISAR DAN TUJUAN UTAMA SESI

Tujuan utama sesi kerja pada 07 September 2026 difokuskan pada:
1. **Penyempurnaan Narasi Manuskrip (`paper/`)**:
   - Memperhalus klaim ilmiah pada Bagian I (*Introduction*), Bagian II (*Related Works*), dan Bagian III (*Materials and Methods*) agar terbebas dari klaim absolut serta hubungan kausalitas yang berlebihan.
   - Menghapus penomoran sitasi sementara berformat `[(N)]` pada teks naratif setelah dipetakan secara formal ke berkas registri sitasi.
   - Memastikan tautan rujukan persamaan matematika kanonikal `[(1)](#eq1)` s.d. `[(5)](#eq5)` pada Bagian III-B tetap terjaga dan tidak terhapus.
2. **Pembentukan Sistem Audit Sitasi Tingkat Kalimat (*Sentence-Level Citation Audit*)**:
   - Mengonsolidasikan seluruh berkas bibliografi (`.bib`, `.ris`, `.nbib`, `.bibtex`) ke direktori [`paper/references/`](../paper/references/).
   - Membangun dan memperbarui [`paper/references.txt`](../paper/references.txt) sebagai basis data pemetaan kalimat demi kalimat dari teks manuskrip ke berkas sumber sitasi dengan tingkat pencocokan teks kutipan (*exact substring match*) 100%.
3. **Penyelarasan Sinkronisasi Remote Git (`git pull` & `git push`)**:
   - Mengambil pembaruan terkini dari repositori jarak jauh (`origin/main`) terkait sintesis performa global dan penambahan referensi Bagian IV-A.
4. **Pembaruan Menyeluruh Dokumentasi Inti Proyek**:
   - Memutakhirkan [`README.md`](../README.md), [`README.AI.md`](../README.AI.md), dan [`WORKFLOW.md`](../WORKFLOW.md) agar secara akurat mencerminkan keberadaan naskah publikasi LaTeX (`paper_latex_en/` dan `paper_latex_id/`), registri sitasi, profil penulis (`authors.txt`), serta prosedur operasional baku (*SOP*) terbaru.
5. **Kepatuhan Terhadap Batasan Ketat (*Strict Constraints*)**:
   - **DILARANG MENGUBAH `prompts.txt`**: Seluruh riwayat prompt pengguna tetap terjaga keasliannya tanpa campur tangan asisten AI.
   - **Kepatuhan Aturan Penulisan (`rules/md_rules.txt`)**: Bebas kata terlarang (`kendati`, `paradigma`, `\bguna\b`), bebas tanda pisah *em dash* (`—`), dan mempertahankan konsistensi angka ground-truth.

---

## 2. KRONOLOGI PERMINTAAN PENGGUNA & TINDAKAN YANG DIAMBIL

### A. Penyempurnaan Narasi Introduction (`paper/01_introduction.md`)
* **Permintaan Pengguna**:
  1. Paragraf 1: Ganti kalimat klaim absolut "Namun, sejumlah studi melaporkan bahwa sistem pengenalan wajah kerap memperlihatkan disparitas performa secara konsisten dan substansial..." menjadi "Namun, sejumlah studi melaporkan adanya disparitas performa pada subkelompok demografis tertentu, termasuk perempuan dan individu dengan warna kulit lebih gelap."
  2. Paragraf 1: Ganti kalimat kausalitas kuat "Ketimpangan akurasi tersebut bersumber dari beragam faktor fundamental..." menjadi "Ketimpangan tersebut dapat dipengaruhi oleh berbagai faktor, termasuk ketidakseimbangan distribusi data dan keterbatasan representasi fitur terhadap variasi visual."
  3. Paragraf 2: Ganti kalimat pemodelan terpisah menjadi: "Sebagian pendekatan pengenalan atribut wajah memodelkan atribut secara terpisah, sedangkan multi-task learning memungkinkan pembelajaran bersama pola visual lintas atribut melalui pembagian parameter representasi."
  4. Paragraf 3: Pertajam narasi bahwa sebagian besar metode masih terfokus pada pengenalan atribut tunggal dan belum mengeksplorasi representasi terpadu untuk demografis interseksional.
  5. Paragraf 4 & 5: Salin sitasi dari `paper_outline.md` dan `related_works/bib` ke `paper/references/`, catat di `paper/references.txt`, dan hapus penomoran sitasi sementara `[(1)]` s.d. `[(5)]`.
* **Tindakan yang Diambil**:
  - Merevisi naskah `paper/01_introduction.md` per paragraf dengan memenuhi target rentang kata.
  - Memperbaiki tautan silang organisasi naskah pada Paragraf 7 agar mengarah ke `03_materials-and-methods_0-overview.md`.
  - Menghapus seluruh penanda sitasi `[(N)]` di Bagian I karena telah terindeks pada `paper/references.txt`.

### B. Penyempurnaan Narasi Related Works (`paper/02_related-works.md`)
* **Permintaan Pengguna**:
  - Salin referensi dari `related_works/bib` ke `paper/references/`.
  - Perbaiki daftar pemetaan per paragraf pada `paper/references.txt`.
  - Hapus seluruh penomoran sitasi `[(1)]` s.d. `[(10)]` pada teks `paper/02_related-works.md`.
* **Tindakan yang Diambil**:
  - Memutakhirkan 5 paragraf tematik pada `02_related-works.md` sesuai outline (Single/Multi-Attribute Facial Recognition, Multi-Domain Feature Fusion, Vision Transformer Representations, Algorithmic Fairness & Intersectional Disparity, dan Research Gap Positioning).
  - Menghapus penomoran sitasi `[(1)]` s.d. `[(10)]` dari teks narasi.

### C. Pembersihan Sitasi pada Materials and Methods (`paper/03_materials-and-methods_*.md`)
* **Permintaan Pengguna**:
  1. Hapus penomoran referensi `[(11)]` pada `03_materials-and-methods_a-dataset.md`.
  2. Hapus penomoran referensi pada `03_materials-and-methods_b-vision-transformer.md` tanpa mengubah rujukan formula matematika.
* **Klarifikasi & Tindakan yang Diambil**:
  - Pada berkas `03_materials-and-methods_a-dataset.md`, menghapus `[(11)]` dan memperhalus kalimat evaluasi terkontrol.
  - Pada berkas `03_materials-and-methods_b-vision-transformer.md`, mengidentifikasi bahwa simbol kurung siku yang ada adalah rujukan nomor persamaan matematika (`[(1)](#eq1)` s.d. `[(5)](#eq5)`), bukan sitasi literatur pustaka. Berdasarkan konfirmasi aturan `rules/md_rules.txt`, tautan formula matematika tersebut tetap dipertahankan.
  - Memperbaiki salah ketik (*typo*) `antarpatach` menjadi `antarpatch` pada narasi mekanisme self-attention.

### D. Eksekusi Rangkaian Commit Pertama (5 Commit Atomik) & Push
* **Permintaan Pengguna**: "Identifikasi dan pelajari perubahan yang telah terjadi dilakukan, jika bisa dibuat menjadi beberapa commit, maka buat menjadi beberapa commit! Sekarang buat commit untuk perubahan-perubahan tersebut dan push!"
* **Tindakan yang Diambil**:
  - Membagi perubahan menjadi 5 commit terpisah:
    1. `78d7007`: `docs(paper): add bibliographic references and sentence-level citation mapping` (44 files)
    2. `3b04f8d`: `docs(paper): refine Section I Introduction narrative and remove citation markers`
    3. `a8bdcd1`: `docs(paper): refine Section II Related Works narrative and remove citation markers`
    4. `077d395`: `docs(paper): refine Section III Materials and Methods subsections A and B`
    5. `eb5a195`: `chore: update prompts log` (staging user edits tanpa modifikasi AI)
  - Mendorong (*push*) kelima commit ke `origin/main`.

### E. Integrasi Referensi Metrik Evaluasi (Sub-seksi III-H)
* **Permintaan Pengguna**: Menambahkan 4 berkas referensi baru dan memetakan Paragraf 1 Sub-seksi III-H (*Evaluation Metrics*) pada `paper/references.txt`.
* **Tindakan yang Diambil**:
  - Menambahkan 4 berkas sumber:
    * `2021_Attention-gating for improved radio galaxy classification.bib`
    * `2022_General Performance Score for classification problems.ris`
    * `2022_On evaluation metrics for medical applications of artificial intelligence.ris`
    * `2023_Common statistical concepts in the supervised Machine Learning arena.nbib`
  - Memetakan 5 kalimat formula matriks konfusi dan skema One-vs-Rest ke dalam `paper/references.txt`.
  - Merapikan baris placeholder kosong `- ""` di akhir berkas.
  - Mengompilasi 2 commit atomik:
    1. `cbf312b`: `docs(paper): add reference files for Section III-H evaluation metrics`
    2. `bab69c9`: `docs(paper): map Section III-H evaluation metrics citations in references.txt`
  - Mendorong (*push*) kedua commit ke `origin/main`.

### F. Sinkronisasi Remote Git (`git pull`)
* **Permintaan Pengguna**: "lakukan git pull"
* **Tindakan yang Diambil**:
  - Mengeksekusi `git pull` dan menerima dua commit dari kolaborator remote via *Fast-forward*:
    * `aeea95d`: `docs(paper): add supporting global performance references` (menambahkan 4 file bib dan pemetaan Seksi IV-A)
    * `df9b76a`: `docs(paper): simplify global performance synthesis` (penyederhanaan narasi `04_results-and-discussion_a-global-performance.md`)
  - Status lokal sinkron 100% pada commit `df9b76a`.

### G. Pemutakhiran Komprehensif Dokumentasi Inti (`README.md`, `README.AI.md`, `WORKFLOW.md`)
* **Permintaan Pengguna**: "tolong update readme md, readme ai md, dan workflow"
* **Tindakan yang Diambil**:
  - Memperbarui `README.md`:
    * Menyertakan paket `paper_latex_en/` dan `paper_latex_id/` (dengan status kompilasi PDF `access.pdf` 13 halaman dua kolom).
    * Menyertakan registri sitasi `paper/references.txt` dan koleksi `paper/references/`.
    * Menyertakan berkas `authors.txt` pada pohon direktori dan tabel ikhtisar dokumen.
  - Memperbarui `README.AI.md`:
    * Memperbarui diagram pohon Bagian 9 (*Repository & Codebase Architecture*).
    * Menambahkan Bagian 11.4 mengenai alur kompilasi terminal LaTeX (`pdflatex` -> `bibtex` -> `pdflatex` -> `pdflatex`).
    * Menyelaraskan Direktif 25 (SOP pipa 4 tahap) dan menambahkan Direktif 26 (*Sentence-Level Citation Audit Protocol*).
  - Memperbarui `WORKFLOW.md`:
    * Mengganti istilah terlarang *Paradigma* menjadi *Kerangka Kerja Alur 4 Tahap*.
    * Memutakhirkan pohon draf modular Markdown Tahap 2 dengan daftar konkret seluruh 9 sub-seksi Metodologi dan 6 sub-seksi Hasil.
    * Memperluas Matriks Pemetaan Universal mencakup seluruh 21 pasangan modul Markdown ke `sections/*.tex`.
    * Menambahkan panduan kompilasi LaTeX dan aturan penjaminan mutu ke-6 (Audit Sitasi Kalimat) dan ke-7 (Registri Akronim Terpusat).
  - Membuat 2 commit atomik:
    1. `ce4d597`: `docs: synchronize repository structure, LaTeX packages, and citation registry in README.md and README.AI.md`
    2. `1e03ec4`: `docs(workflow): refine 4-stage manuscript pipeline SOP and 21-module mapping matrix in WORKFLOW.md`
  - Mendorong (*push*) kedua commit ke `origin/main`.

---

## 3. STRUKTUR ARSITEKTUR CITATION AUDIT REGISTRY

Sistem audit sitasi yang dibangun pada sesi ini mengimplementasikan kepatuhan 100% antara klaim faktual narasi teks draf dengan basis data bibliografi:

```
paper/
├── references/                               # Direktori 47 Berkas Bibliografi
│   ├── 2019_DemogPairs...bib
│   ├── 2021_A Multifeature Learning and Fusion...bib
│   ├── 2021_Attention-gating for improved radio galaxy...bib
│   ├── 2022_General Performance Score for classification...ris
│   ├── 2022_On evaluation metrics for medical applications...ris
│   ├── 2023_Common statistical concepts in the supervised...nbib
│   └── ... (47 total files)
│
├── references.txt                            # Registri Pemetaan Tingkat Kalimat
│   ├── paper/01_introduction.md              # Pemetaan klaim latar belakang, disparitas, & ViT
│   ├── paper/02_related-works.md             # Pemetaan tinjauan pustaka tematik paragraf 1-5
│   ├── paper/03_materials-and-methods_*.md   # Pemetaan dataset, ViT, model RF/GNB/LR/SVM, & metrik
│   └── paper/04_results-and-discussion_*.md  # Pemetaan sintesis komparasi performa global
│
└── acronyms.txt                              # Registri Pelacakan Akronim Terpusat
    └── Menjamin kepatuhan First-Mention Full Form (Rule 1.3)
```

Setiap entri pada `references.txt` memuat potongan kalimat asli naskah (*exact substring*) yang diikuti dengan jalur relatif berkas sitasi sumber di dalam `paper/references/`, memastikan audit sitasi dapat ditelusuri secara mekanis sebelum ditransfer ke berkas BibTeX naskah LaTeX (`references.bib`).

---

## 4. REKAPITULASI COMMIT GIT HARI INI (07 SEPTEMBER 2026)

| Hash | Tipe / Scope | Pesan Commit | Peran & Cakupan Berkas |
|:---:|:---|:---|:---|
| `78d7007` | `docs(paper)` | add bibliographic references and sentence-level citation mapping | Menambahkan 43 file referensi di `paper/references/` dan registri `paper/references.txt` |
| `3b04f8d` | `docs(paper)` | refine Section I Introduction narrative and remove citation markers | Refinement narasi disparitas demografis, multi-task, kontribusi, dan hapus `[(1)]`-`[(5)]` |
| `a8bdcd1` | `docs(paper)` | refine Section II Related Works narrative and remove citation markers | Refinement narasi tinjauan pustaka tematik dan hapus `[(1)]`-`[(10)]` |
| `077d395` | `docs(paper)` | refine Section III Materials and Methods subsections A and B | Hapus `[(11)]` di dataset, perbaiki narasi ViT antarpatch, dan amankan formula `[(1)]`-`[(5)]` |
| `eb5a195` | `chore` | update prompts log | Mencatat pembaruan entri pengguna pada `prompts.txt` |
| `cbf312b` | `docs(paper)` | add reference files for Section III-H evaluation metrics | Menambahkan 4 berkas sitasi metrik klasifikasi dan matriks konfusi |
| `bab69c9` | `docs(paper)` | map Section III-H evaluation metrics citations in references.txt | Pemetaan tingkat kalimat Paragraf 1 Bagian III-H ke `paper/references.txt` |
| `aeea95d` | `docs(paper)` | add supporting global performance references *(remote)* | Penambahan 4 file referensi dan pemetaan Seksi IV-A dari kolaborator |
| `df9b76a` | `docs(paper)` | simplify global performance synthesis *(remote)* | Penyederhanaan narasi Bagian IV-A dari kolaborator |
| `ce4d597` | `docs` | synchronize repository structure, LaTeX packages, and citation registry in README.md and README.AI.md | Sinkronisasi pohon repositori, panduan kompilasi LaTeX, dan Direktif 26 |
| `1e03ec4` | `docs(workflow)` | refine 4-stage manuscript pipeline SOP and 21-module mapping matrix in WORKFLOW.md | SOP pipa 4 tahap, matriks pemetaan 21 modul, panduan kompilasi IEEE Access, & aturan audit sitasi |

---

## 5. HASIL VERIFIKASI AKHIR & INTEGRITAS SISTEM

1. **Uji Kata Terlarang (`rules/md_rules.txt`)**:
   - `kendati`: **0 temuan** di seluruh berkas yang dimodifikasi.
   - `paradigma`: **0 temuan** (telah diganti dengan *kerangka kerja* atau *metode*).
   - `\bguna\b`: **0 temuan** sebagai preposisi.
2. **Uji Tipografi Tanda Pisah Em Dash (`—`)**:
   - **0 temuan** pada `README.md`, `README.AI.md`, dan `WORKFLOW.md`.
3. **Integritas Berkas Terproteksi (`prompts.txt`)**:
   - Berkas `prompts.txt` **tidak dimodifikasi oleh asisten AI** sepanjang sesi kerja berlangsung, mempertahankan catatan asli pengguna.
4. **Status Git Repositori**:
   - Branch aktif: `main`
   - Status: *Your branch is up to date with 'origin/main'.*
   - Working tree: *clean* (semua perubahan telah dikomit dan didorong ke remote GitHub).

---

## 6. REKOMENDASI TAHAP BERIKUTNYA

1. **Sinkronisasi Terjadwal ke Naskah LaTeX (`paper_latex_en/` & `paper_latex_id/`)**:
   - Mengingat draf naratif Markdown pada `01_introduction.md`, `02_related-works.md`, `03a_dataset.md`, dan `04a_global-performance.md` telah diperhalus, rekomendasikan proses sinkronisasi terarah ke naskah LaTeX masing-masing menggunakan subagent terisolasi per file.
2. **Kompilasi Ulang Naskah Kamera Siap Kirim**:
   - Lakukan verifikasi kompilasi akhir pada `paper_latex_en/access.pdf` dan `paper_latex_id/access.pdf` pasca-sinkronisasi narasi naskah.
3. **Audit Kelengkapan Sitasi pada Seksi IV-B s.d. IV-F**:
   - Lanjutkan pemetaan kalimat untuk sub-seksi analisis hasil lainnya pada `paper/references.txt` seiring penambahan referensi pendukung baru.
