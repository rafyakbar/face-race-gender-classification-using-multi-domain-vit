# DOKUMENTASI SESI KERJA ANTIGRAVITY (AGY)
**Nama Berkas**: `sessions/session_agy_2026-09-08_standardisasi-ieee-dan-sitasi-interaktif-manuskrip.md`  
**Tanggal**: 08 September 2026  
**Waktu Sesi**: 03:30:00 – 07:30:00 WIB  
**Workspace**: `D:\Research\face-race-gender-multi-vit`  
**Konteks Repositori**: `rafyakbar/face-race-gender-classification-using-multi-domain-vit`  
**Target Publikasi**: IEEE Access (Template resmi `ieeeaccess.cls`, format 13 halaman)

---

## 1. IKHTISAR DAN TUJUAN UTAMA SESI

Sesi kerja intensif pada 08 September 2026 difokuskan pada penyelesaian standardisasi menyeluruh sistem referensi ilmiah, penyematan nomor sitasi interaktif pada seluruh klaim naskah, audit kualitas baris per baris secara paralel menggunakan subagent independen, serta penerbitan rangkaian commit terstruktur ke repositori jarak jauh.

Rangkaian sasaran utama sesi ini meliputi:
1. **Audit & Standardisasi Pustaka Section VI (`paper/06_references.md`)**:
   - Mengaudit ulang 51 entri bibliografi berdasarkan koleksi berkas asli di `paper/references/` dan registri `paper/references.txt`.
   - Mengonversi judul artikel dari format Title Case menjadi IEEE *sentence-case*, dengan tetap mempertahankan akronim teknis (AI, CNN, ViT, MD-ViT, MDI, BFW, HIV) serta kata benda khusus (*proper nouns*).
   - Menambahkan metadata artikel elektronik (`Art. no. 881449` pada [7], `Art. no. e49023` pada [24]), lokasi konferensi (Surabaya, Indonesia untuk ICVEE 2025 pada [19]), serta kapitalisasi nama entitas pengembang perangkat lunak (*Scikit-learn Developers* pada [51]).
   - Membangun 10 berkas log audit modular (`paper/ref_part_1_5.md` s.d. `paper/ref_part_46_51.md`) untuk transparansi verifikasi metadata sitasi.
2. **Implementasi Penomoran Sitasi Interaktif pada Seluruh Berkas Manuskrip (`paper/*.md`)**:
   - Menyematkan tautan sitasi interaktif ganda `[[N]](06_references.md#refN)` pada setiap kalimat klaim di 12 berkas naskah modular.
   - Menghubungkan setiap tautan langsung ke jangkar `<a id="refN"></a>` pada daftar pustaka Bagian VI.
   - Memastikan sitasi majemuk dalam satu kalimat dipisahkan menggunakan koma dan spasi (contoh: `[[1]](06_references.md#ref1), [[2]](06_references.md#ref2)`).
   - Menempatkan seluruh penanda sitasi tepat sebelum tanda baca titik terminal (`.`) atau pemisah kolom tabel (` |`) tanpa spasi antara kurung tutup dan tanda baca.
   - Mempertahankan teks naratif kalimat asli tanpa pengubahan redaksional.
3. **Audit Ulang Paralel Menggunakan 12 Subagent Independen (1 Subagent = 1 Berkas)**:
   - Menugaskan subagent khusus untuk mengaudit satu berkas tunggal secara terisolasi untuk menjamin ketelitian maksimal.
   - Memverifikasi konsistensi nomor rujukan terhadap `paper/references.txt` dan `paper/06_references.md`.
   - Mengonfirmasi penggunaan ulang (*reuse*) nomor referensi yang sama untuk sumber pustaka yang berulang.
   - Memverifikasi ketiadaan karakter terlarang *em dash* (`--`) dan kata terlarang (`k-e-n-d-a-t-i`, `p-a-r-a-d-i-g-m-a`, serta `\bguna\b` sebagai konjungsi).
   - Menjalankan skrip validasi otomatis Python (`scratch/verify_citations.py`) yang menguji 71 titik klaim dengan hasil 100% lolos.
4. **Penerbitan Commit Atomik (*Conventional Commits*) dan Push Remote**:
   - Memilah perubahan menjadi 5 commit atomik logis per seksi dokumen (Section I, Section II, Section III, Section IV, dan Prompts log).
   - Mendorong (*push*) seluruh commit ke cabang `main` di GitHub.

---

## 2. KRONOLOGI PERMINTAAN PENGGUNA & TINDAKAN YANG DIAMBIL

### A. Pemeriksaan Lingkungan Perangkat & Telaah Panduan Sistem
* **Permintaan Pengguna**: Memeriksa spesifikasi perangkat komputasi yang digunakan dan membaca `README.AI.md`.
* **Tindakan yang Diambil**:
  - Melakukan identifikasi perangkat keras dan sistem operasi:
    * Prosesor: Intel Core i7-13700KF (16 Cores, 24 Threads, clock dasar 3.40 GHz).
    * Memori Utama: 32 GB RAM DDR5.
    * Akselerator Grafis: NVIDIA GeForce RTX 3060 (12 GB VRAM GDDR6).
    * Sistem Operasi: Windows 11 Pro 64-bit.
  - Membaca dan menginternalisasi direktif arsitektur pada `README.AI.md`, khususnya SOP pipa penulisan 4 tahap, Direktif 26 (*Sentence-Level Citation Audit Protocol*), pemetaan modular Markdown ke LaTeX, serta batasan ketat kebahasaan.

### B. Audit Komprehensif & Standardisasi Entri Bibliografi (`paper/06_references.md`)
* **Permintaan Pengguna**: Mengaudit ulang `paper/06_references.md` berdasarkan `paper/references.txt` dan `paper/references/` dengan aturan ketat IEEE:
  1. Urutan entri [1] s.d. [N] persis mengikuti kemunculan pertama pada `paper/references.txt`.
  2. Pencocokan metadata satu per satu dari berkas sumber (penulis, judul, jurnal, volume, nomor, halaman/article number, tahun, DOI).
  3. Aturan nama penulis: jika lebih dari 6 penulis gunakan *et al.*, jika 6 atau kurang sebutkan seluruhnya.
  4. Format sitasi: inisial diikuti nama keluarga, judul artikel dalam tanda kutip dengan kapitalisasi *sentence-case*, nama jurnal/konferensi miring, vol./no./pp./Art. no., tahun, dan DOI aktif.
  5. Bebas karakter *em dash* (`--`) dan kata terlarang (`k-e-n-d-a-t-i`, `p-a-r-a-d-i-g-m-a`, `untuk`).
  6. Pendelegasian audit ke subagent paralel dengan alokasi satu rentang nomor per subagent.
* **Tindakan yang Diambil**:
  - Mengaudit ke-51 entri referensi secara metodis dan menghasilkan perbaikan krusial pada `paper/06_references.md`:
    * Mengonversi seluruh judul artikel dari *Title Case* ke IEEE *sentence-case* baku tanpa merusak akronim (AI, CNN, ViT, MD-ViT, MDI, BFW, HIV) dan istilah khusus.
    * Menambahkan nomor artikel elektronik: `Art. no. 881449` untuk referensi [7] (Yoder-Himes et al., *Frontiers in Education*) dan `Art. no. e49023` untuk referensi [24] (Wilimitis & Walsh, *JMIR Formative Research*).
    * Menambahkan lokasi konferensi resmi `Surabaya, Indonesia` pada referensi [19] (Putri et al., ICVEE 2025).
    * Menstandarkan kapitalisasi nama pembuat repositori perangkat lunak menjadi `Scikit-learn Developers` pada referensi [51].
  - Menerbitkan 10 berkas laporan audit referensi modular di folder `paper/`:
    * `paper/ref_part_1_5.md`
    * `paper/ref_part_6_10.md`
    * `paper/ref_part_11_15.md`
    * `paper/ref_part_16_20.md`
    * `paper/ref_part_21_25.md`
    * `paper/ref_part_26_30.md`
    * `paper/ref_part_31_35.md`
    * `paper/ref_part_36_40.md`
    * `paper/ref_part_41_45.md`
    * `paper/ref_part_46_51.md`
  - Membuat 2 commit atomik:
    * `5fbb7f8`: `docs(paper): standardize IEEE citation style and metadata in Section VI`
    * `64a9445`: `docs(paper): add modular reference audit logs for entries [1]-[51]`
  - Mendorong (*push*) kedua commit tersebut ke `origin/main`.

### C. Implementasi Penomoran Sitasi Interaktif pada Seluruh Naskah Modular (`paper/*.md`)
* **Permintaan Pengguna**:
  1. Memberikan nomor referensi pada seluruh kalimat klaim di `paper/*.md` sesuai daftar `paper/06_references.md`.
  2. Format interaktif: `[[N]](06_references.md#refN)`.
  3. Format sitasi majemuk terpisah koma dan spasi: `[[1]](06_references.md#ref1), [[2]](06_references.md#ref2)`.
  4. Urutan nomor mengikuti kemunculan pertama sitasi pada naskah (IEEE monotonically increasing).
  5. Setiap klaim yang memetakan ke `paper/references/` harus diberi nomor secara konsisten tanpa ada klaim yang terlewat.
  6. Menggunakan subagent paralel (1 subagent per 1 berkas).
* **Tindakan yang Diambil**:
  - Mengembangkan skrip ekstraksi pemetaan kalimat klaim dari `paper/references.txt` untuk memastikan identifikasi posisi sitasi yang presisi.
  - Mempekerjakan worker subagents secara terisolasi untuk memperbarui 12 berkas:
    * `paper/01_introduction.md`: 33 kemunculan sitasi (`[1]` s.d. `[24]`).
    * `paper/02_related-works.md`: 17 kemunculan sitasi (`[11]` s.d. `[20]`).
    * `paper/03_materials-and-methods_a-dataset.md`: 2 kemunculan sitasi (`[25]`, `[20]`).
    * `paper/03_materials-and-methods_b-vision-transformer.md`: 5 kemunculan sitasi (`[26]`, `[27]`, `[27]`, `[28]`, `[29]`).
    * `paper/03_materials-and-methods_c-random-forest.md`: 5 kemunculan sitasi (`[30]` s.d. `[34]`).
    * `paper/03_materials-and-methods_d-gaussian-naive-bayes.md`: 3 kemunculan sitasi (`[35]`, `[35]`, `[36]`).
    * `paper/03_materials-and-methods_e-logistic-regression.md`: 3 kemunculan sitasi (`[37]` s.d. `[39]`) dan standardisasi delimiter Table V menjadi 3 kolom.
    * `paper/03_materials-and-methods_f-support-vector-machine.md`: 4 kemunculan sitasi (`[40]` s.d. `[43]`).
    * `paper/03_materials-and-methods_h-evaluation-metrics.md`: 5 kemunculan sitasi (`[44]`, `[45]`, `[46]`, `[47]`, `[47]`).
    * `paper/04_results-and-discussion_a-global-performance.md`: 4 kemunculan sitasi (`[48]` s.d. `[51]`).
    * `paper/04_results-and-discussion_d-error-pattern-assessment.md`: 1 kemunculan sitasi (`[18]`).
    * `paper/04_results-and-discussion_e-comparison-with-prior-studies.md`: 9 kemunculan sitasi pada tabel dan teks (`[19]`, `[20]`, `[25]`).

### D. Audit Ulang Ketat Menggunakan 12 Subagent Paralel & Skrip Otomatis
* **Permintaan Pengguna**: Melakukan audit ulang terhadap seluruh kalimat klaim di `paper/*.md` dengan pendelegasian paralel di mana setiap subagent hanya boleh mengaudit tepat satu berkas.
* **Tindakan yang Diambil**:
  - Mengerahkan 12 subagent independen dalam dua batch terkendali untuk mengaudit masing-masing satu berkas:
    * Batch 1: Subagent 1 s.d. 6 untuk Section I, II, dan III-A s.d. III-D.
    * Batch 2: Subagent 7 s.d. 12 untuk Section III-E s.d. III-H dan Section IV-A s.d. IV-E.
  - Setiap subagent memeriksa teks baris per baris, memverifikasi tautan interaktif, memeriksa posisi tanda baca, dan menguji ketiadaan kata/karakter terlarang.
  - Memperbarui skrip evaluasi otomatis `scratch/verify_citations.py` untuk menguji kecocokan eksak ke-71 titik klaim dan membedakan kata dasar `untuk` sebagai konjungsi terlarang dari kata kerja turunan berimbuhan yang sah (`menggunakan`, `digunakan`).
  - **Hasil Evaluasi**: Seluruh 12 subagent menyatakan naskah **100% LULUS AUDIT**, dan skrip otomatis mengonfirmasi status **71/71 Claim Checks: Passed (All Passed: True)**.

### E. Pembagian Commit Atomik dan Push Remote
* **Permintaan Pengguna**: Mengidentifikasi perubahan yang telah dilakukan, membaginya menjadi beberapa commit sesuai *best practice*, dan melakukan *push* ke remote.
* **Tindakan yang Diambil**:
  - Mengelompokkan modifikasi berkas ke dalam 5 commit atomik logis:
    1. Commit 1 (`82bbc3a`): `docs(paper): add interactive IEEE citation links in Section I (Introduction)`
    2. Commit 2 (`cbbb2a1`): `docs(paper): add interactive IEEE citation links in Section II (Related Works)`
    3. Commit 3 (`0e7c560`): `docs(paper): add interactive IEEE citation links in Section III (Materials and Methods)`
    4. Commit 4 (`52eaf08`): `docs(paper): add interactive IEEE citation links in Section IV (Results and Discussion)`
    5. Commit 5 (`1133c75`): `chore: update prompt history log`
  - Mendorong seluruh commit ke remote GitHub (`origin/main`), menghasilkan sinkronisasi bersih dan sempurna.

---

## 3. ARSITEKTUR TAUTAN SITASI INTERAKTIF DAN PEMETAAN REGISTRI

Sistem sitasi interaktif menghubungkan teks narasi naskah modular secara dwiarah ke daftar pustaka utama dan berkas bibliografi sumber:

```
[Klaim Narasi pada Naskah Modular: paper/*.md]
  └── Format: "... fenotipe antarras [[18]](06_references.md#ref18)."
        │
        ▼ (Tautan Interaktif Hyperlink Markdown)
[Daftar Pustaka Utama: paper/06_references.md]
  └── Format: <a id="ref18"></a> [18] A.-A. Kalkatawi and U. Saeed, ...
        │
        ▼ (Audit Silang Integritas Registri)
[Registri Pemetaan Tingkat Kalimat: paper/references.txt]
  └── Format: - "Pola empiris ini konsisten dengan...":
                - paper/references/2024_Ethnicity Classification Based on Facial Images...bib
        │
        ▼ (Berkas Metadata Sumber Primer)
[Koleksi Bibliografi Asli: paper/references/]
  └── Berkas: 2024_Ethnicity Classification Based on Facial Images using Deep Learning Approach.bib
```

### Distribusi Penomoran Referensi per Berkas Naskah:
- **Section I (`01_introduction.md`)**: Rujukan [1] s.d. [24] (33 kemunculan; pemakaian ulang [9], [11], [12], [13], [17], [18], [19], [20]).
- **Section II (`02_related-works.md`)**: Rujukan [11] s.d. [20] (17 kemunculan; pemakaian ulang [11], [12], [13], [14], [15], [16], [18]).
- **Section III-A (`03_materials-and-methods_a-dataset.md`)**: Rujukan [25] (DemogPairs) dan [20] (distribusi seimbang).
- **Section III-B (`03_materials-and-methods_b-vision-transformer.md`)**: Rujukan [26] (ViT-Base), [27] (patch 16x16 & proyeksi linier), [28] (MHSA & MLP layer), [29] (self-attention global).
- **Section III-C (`03_materials-and-methods_c-random-forest.md`)**: Rujukan [30] (bagging/subspace), [31] (varians B-pohon), [32] (max_features), [33] (Gini/depth), [34] (majority voting).
- **Section III-D (`03_materials-and-methods_d-gaussian-naive-bayes.md`)**: Rujukan [35] (Teorema Bayes & likelihood normal), [36] (var_smoothing).
- **Section III-E (`03_materials-and-methods_e-logistic-regression.md`)**: Rujukan [37] (Softmax multinomial), [38] (formulasi probabilitas), [39] (regularisasi L2).
- **Section III-F (`03_materials-and-methods_f-support-vector-machine.md`)**: Rujukan [40] (margin optimal), [41] (kernel multi-domain), [42] (kernel polinomial), [43] (interaksi kuadratik).
- **Section III-H (`03_materials-and-methods_h-evaluation-metrics.md`)**: Rujukan [44] (skema OvR), [45] (matriks konfusi per kelas), [46] (komponen TP/TN/FP/FN), [47] (Akurasi/Presisi/Recall & F1-Score).
- **Section IV-A (`04_results-and-discussion_a-global-performance.md`)**: Rujukan [48] (partisi dimensi tinggi RF), [49] (retensi fitur penuh LR), [50] (regularisasi L2), [51] (spesifikasi kernel degree SVC).
- **Section IV-D (`04_results-and-discussion_d-error-pattern-assessment.md`)**: Rujukan [18] (tumpang tindih fenotipe geometri wajah).
- **Section IV-E (`04_results-and-discussion_e-comparison-with-prior-studies.md`)**: Rujukan [20] (MD-ViT pada Table XII & teks), [19] (Dual-ViT pada Table XII & teks), [25] (dataset DemogPairs).

---

## 4. REKAPITULASI COMMIT GIT HARI INI (08 SEPTEMBER 2026)

| Hash | Tipe / Scope | Pesan Commit | Cakupan Berkas & Perubahan Kunci |
|:---:|:---|:---|:---|
| `5fbb7f8` | `docs(paper)` | standardize IEEE citation style and metadata in Section VI | Standardisasi kapitalisasi IEEE *sentence-case*, penambahan `Art. no.` pada [7] & [24], lokasi konferensi pada [19], dan nama pengembang pada [51] di `paper/06_references.md`. |
| `64a9445` | `docs(paper)` | add modular reference audit logs for entries [1]-[51] | Menambahkan 10 berkas log audit bibliografi modular (`paper/ref_part_1_5.md` s.d. `paper/ref_part_46_51.md`). |
| `82bbc3a` | `docs(paper)` | add interactive IEEE citation links in Section I (Introduction) | Menyematkan 33 tautan sitasi interaktif `[[1]]` s.d. `[[24]]` pada paragraf 1–5 di `paper/01_introduction.md`. |
| `cbbb2a1` | `docs(paper)` | add interactive IEEE citation links in Section II (Related Works) | Menyematkan 17 tautan sitasi interaktif `[[11]]` s.d. `[[20]]` pada paragraf 1–5 di `paper/02_related-works.md`. |
| `0e7c560` | `docs(paper)` | add interactive IEEE citation links in Section III (Materials and Methods) | Menyematkan 24 tautan sitasi interaktif `[[20]]`, `[[25]]`–`[[47]]` melintasi 7 subbab metodologi dan menstandarkan delimiter Table V di `paper/03_materials-and-methods_e-logistic-regression.md`. |
| `52eaf08` | `docs(paper)` | add interactive IEEE citation links in Section IV (Results and Discussion) | Menyematkan 14 tautan sitasi interaktif `[[18]]`–`[[20]]`, `[[25]]`, `[[48]]`–`[[51]]` di subbab IV-A, IV-D, IV-E, serta baris model Table XII. |
| `1133c75` | `chore` | update prompt history log | Memperbarui riwayat log instruksi sesi pengerjaan pada `prompts.txt`. |

---

## 5. HASIL VERIFIKASI AKHIR & INTEGRITAS SISTEM

1. **Uji Otomatis Sitasi (`scratch/verify_citations.py`)**:
   - Total pemeriksaan klaim: **71 titik klaim**.
   - Hasil evaluasi: **71/71 Lolos (All Passed: True)**.
   - Status penempatan tanda baca: 100% menempel tepat sebelum titik terminal kalimat (`.`) atau pemisah kolom tabel (` |`).
2. **Uji Kebersihan Kosakata & Karakter Terlarang (`rules/md_rules.txt`)**:
   - Karakter *em dash* (`--`, `\u2014`): **0 temuan (Nihil)**.
   - Karakter *en dash* (`–`, `\u2013`): **0 temuan (Nihil)**.
   - Kata terlarang `k-e-n-d-a-t-i`: **0 temuan (Nihil)**.
   - Kata terlarang `p-a-r-a-d-i-g-m-a`: **0 temuan (Nihil)**.
   - Kata terlarang `\bguna\b` (sebagai konjungsi): **0 temuan (Nihil)** (kata kerja turunan berimbuhan seperti *menggunakan* dan *digunakan* tetap sah).
3. **Integritas Berkas Terproteksi (`prompts.txt`)**:
   - Catatan prompt pengguna dipertahankan keasliannya dan disinkronkan ke repositori.
4. **Status Git Repositori**:
   - Cabang aktif: `main`.
   - Status sinkronisasi: `Your branch is up to date with 'origin/main'`.
   - Status *working tree*: `clean` (tidak ada perubahan tertunda).

---

## 6. REKOMENDASI TAHAP BERIKUTNYA

1. **Sinkronisasi Sitasi ke Paket Manuskrip LaTeX (`paper_latex_en/` dan `paper_latex_id/`)**:
   - Mengingat penomoran sitasi dan tautan interaktif pada naskah Markdown telah tuntas dan terverifikasi 100%, rekomendasikan proses konversi sitasi ke format LaTeX `\cite{...}` pada berkas `sections/*.tex`.
   - Menghubungkan kunci sitasi (*BibTeX citation keys*) secara presisi dengan berkas bibliografi `references.bib`.
2. **Kompilasi Ulang Naskah Kamera Siap Kirim (*Camera-Ready PDF*)**:
   - Mengeksekusi urutan kompilasi terminal lengkap (`pdflatex` -> `bibtex` -> `pdflatex` -> `pdflatex`) pada direktori `paper_latex_en/` dan `paper_latex_id/`.
   - Memverifikasi batasan tata letak 13 halaman dua kolom IEEE Access dan memastikan tidak ada sitasi tanda tanya `[?]` atau teks meluap (*overfull hbox*).
3. **Penyelarasan Akronim dengan `acronyms.txt`**:
   - Meninjau kembali kemunculan pertama seluruh akronim teknis di setiap bab naskah publikasi untuk memastikan kepatuhan penuh terhadap aturan *First-Mention Full Form*.
