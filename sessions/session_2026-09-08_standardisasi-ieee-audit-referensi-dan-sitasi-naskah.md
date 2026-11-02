# DOKUMENTASI KONSOLIDASI SESI KERJA: 08 SEPTEMBER 2026
**Nama Berkas**: `sessions/session_2026-09-08_standardisasi-ieee-audit-referensi-dan-sitasi-naskah.md`  
**Tanggal**: 08 September 2026  
**Waktu Sesi**: 03:30:00 – 23:45:00 WIB (Sesi Pagi: Antigravity/AGY; Sesi Siang–Malam: OpenCode/Omen Alpha)  
**Workspace**: `D:\Research\face-race-gender-classification-using-multi-domain-vit`  
**Konteks Repositori**: `rafyakbar/face-race-gender-classification-using-multi-domain-vit`  
**Target Publikasi**: IEEE Access (Template resmi `ieeeaccess.cls`, format 13–14 halaman)  
**Agen Kolaboratif**: Antigravity (AGY) & OpenCode (Omen Alpha)  

---

## 1. IKHTISAR DAN TUJUAN UTAMA SESI KONSOLIDASI

Sesi kerja intensif pada 08 September 2026 didedikasikan untuk standardisasi menyeluruh sistem referensi ilmiah IEEE, implementasi penomoran sitasi interaktif pada naskah Markdown, audit multi-lapis via puluhan subagent paralel, serta sinkronisasi penuh ke naskah publikasi LaTeX (`paper_latex_id/`):

1. **Sesi Pagi (Antigravity / AGY)**:
   - Audit dan standardisasi 51 entri bibliografi IEEE di `paper/06_references.md` (*sentence-case*, `Art. no.`, lokasi konferensi, registri `ref_part_*.md`).
   - Penomoran sitasi interaktif ganda `[[N]](06_references.md#refN)` kalimat per kalimat pada 12 berkas naskah modular (`paper/*.md`).
   - Audit paralel via 12 subagent independen dan validasi otomatis dengan skrip Python `scratch/verify_citations.py` (71/71 lolos).
   - Penerbitan rangkaian commit atomik untuk Section I s.d. IV.
2. **Sesi Siang–Malam (OpenCode / Omen Alpha)**:
   - Audit konsistensi bulan/tanggal terbit pada seluruh entri referensi terhadap 51 berkas sumber primer di `paper/references/`.
   - Perluasan basis data `references.bib` dari 11 menjadi 51 entri (`ref1` s.d. `ref51`) dan sinkronisasi 20 modul `paper_latex_id/sections/*.tex` via 21 subagent paralel.
   - Normalisasi representasi metrik performa (Akurasi/Presisi/Recall/F1-Score) ke format persentase tunggal pada seluruh draf naskah Markdown dan LaTeX via 11 subagent.
   - Penyempurnaan tata letak visual LaTeX: regenerasi gambar komposit Figure 2 (`images/sample_demogpairs.png`, resolusi 3225×620 px, tinggi seragam 500 px, susunan 1 baris × 6 kolom), penghapusan bold Table II, pemadatan label `Ours` Table XII (single-column), dan eliminasi tautan ORCID pada biografi.
   - Pengujian kompilasi `access.pdf` (14 halaman) dengan status 0 *undefined citations* dan 0 *BibTeX warnings*.

---

## 2. SESI PAGI (ANTIGRAVITY / AGY): STANDARDISASI IEEE & SITASI INTERAKTIF MANUSKRIP

### A. Pemeriksaan Lingkungan Perangkat & Telaah Panduan Sistem
* **Tindakan yang Diambil**:
  - Mengidentifikasi perangkat keras: Intel Core i7-13700KF (16 Cores, 24 Threads), 32 GB RAM DDR5, NVIDIA GeForce RTX 3060 (12 GB VRAM), Windows 11 Pro 64-bit.
  - Mempelajari SOP pipa penulisan 4 tahap, Direktif 26 (*Sentence-Level Citation Audit Protocol*), dan aturan kebahasaan baku.

### B. Audit & Standardisasi Entri Bibliografi (`paper/06_references.md`)
* **Tindakan yang Diambil**:
  - Mengonversi judul artikel dari *Title Case* ke IEEE *sentence-case* dengan mempertahankan akronim teknis (AI, CNN, ViT, MD-ViT, MDI, BFW, HIV).
  - Menambahkan nomor artikel elektronik: `Art. no. 881449` pada [7] (Yoder-Himes et al.) dan `Art. no. e49023` pada [24] (Wilimitis & Walsh).
  - Menambahkan lokasi konferensi resmi `Surabaya, Indonesia` pada [19] (Putri et al., ICVEE 2025).
  - Menstandarkan nama pengembang repositori perangkat lunak menjadi `Scikit-learn Developers` pada [51].
  - Menerbitkan 10 berkas log audit bibliografi modular (`paper/ref_part_1_5.md` s.d. `paper/ref_part_46_51.md`).
  - Menerbitkan commit: `5fbb7f8` dan `64a9445`.

### C. Penomoran Sitasi Interaktif Kalimat per Kalimat (`paper/*.md`)
* **Tindakan yang Diambil**:
  - Menyematkan tautan sitasi interaktif ganda `[[N]](06_references.md#refN)` pada setiap klaim di 12 berkas naskah modular:
    * `paper/01_introduction.md`: 33 kemunculan sitasi (`[1]` s.d. `[24]`).
    * `paper/02_related-works.md`: 17 kemunculan sitasi (`[11]` s.d. `[20]`).
    * `paper/03_materials-and-methods_a-dataset.md`: 2 kemunculan sitasi (`[25]`, `[20]`).
    * `paper/03_materials-and-methods_b-vision-transformer.md`: 5 kemunculan sitasi (`[26]`, `[27]`, `[28]`, `[29]`).
    * `paper/03_materials-and-methods_c-random-forest.md`: 5 kemunculan sitasi (`[30]` s.d. `[34]`).
    * `paper/03_materials-and-methods_d-gaussian-naive-bayes.md`: 3 kemunculan sitasi (`[35]`, `[36]`).
    * `paper/03_materials-and-methods_e-logistic-regression.md`: 3 kemunculan sitasi (`[37]` s.d. `[39]`).
    * `paper/03_materials-and-methods_f-support-vector-machine.md`: 4 kemunculan sitasi (`[40]` s.d. `[43]`).
    * `paper/03_materials-and-methods_h-evaluation-metrics.md`: 5 kemunculan sitasi (`[44]` s.d. `[47]`).
    * `paper/04_results-and-discussion_a-global-performance.md`: 4 kemunculan sitasi (`[48]` s.d. `[51]`).
    * `paper/04_results-and-discussion_d-error-pattern-assessment.md`: 1 kemunculan sitasi (`[18]`).
    * `paper/04_results-and-discussion_e-comparison-with-prior-studies.md`: 9 kemunculan sitasi (`[19]`, `[20]`, `[25]`).

### D. Audit Independen 12 Subagent & Skrip Validasi Otomatis
* Mengerahkan 12 subagent paralel dalam 2 batch untuk mengaudit seluruh kalimat klaim.
* Mengembangkan dan mengeksekusi `scratch/verify_citations.py` untuk menguji kecocokan 71 titik klaim: **71/71 Claim Checks: Passed (All Passed: True)**.
* Menerbitkan 5 commit atomik: `82bbc3a`, `cbbb2a1`, `0e7c560`, `52eaf08`, dan `1133c75`.

---

## 3. SESI SIANG–MALAM (OPENCODE): AUDIT REFERENSI, SINKRONISASI LATEX & PENYEMPURNAAN LAYOUT

### A. Audit 51 Entri Bibliografi & Konsistensi Bulan/Tanggal
* **Delegasi 10 Subagent Paralel** ([1]-[5], [6]-[10], dst.):
  - Menyesuaikan kapitalisasi [20] `Multidomain` dan koreksi nama penulis entri [42] menjadi **`N.-Y. Nguyen, L. V. Tran, and V. T. S. Dao`** (*PLOS ONE*).
  - Menambahkan data bulan resmi yang tersedia di sumber primer: [1] `Jan. 2023`, [8] `Aug. 2022`, [9] `Aug. 2023`, [34] `Feb. 2024`, [35] `Mar. 2023`, [44] `Feb. 2023`.
  - Memastikan 23 entri jurnal tanpa bulan tidak direkayasa sesuai kaidah IEEE bila sumber tidak mencantumkannya.

### B. Audit 91 Tautan Sitasi pada Seluruh Kalimat Klaim Naskah
* 12 subagent berklaim + 1 subagent sweep memastikan:
  - 91 tautan interaktif format `[[N]](06_references.md#refN)` cocok 100% dengan `paper/references.txt`.
  - 51 dari 51 nomor referensi unik terpakai lengkap secara monotonik menaik.

### C. Sinkronisasi Penuh `paper_latex_id/` dengan `paper/`
* Memperluas basis data BibTeX `paper_latex_id/references.bib` dari 11 menjadi 51 entri (`ref1`–`ref51`).
* Mengerahkan 21 subagent paralel untuk menyelaraskan 20 modul LaTeX terhadap berkas sumber Markdown.
* Menjalankan audit konformansi terhadap paket template resmi IEEE Access (`template/ACCESS_latex_template_20260513`).

### D. Normalisasi Format Metrik ke Persentase Tunggal
* 11 subagent paralel mengonversi seluruh format desimal ganda (misal `93.69% (0.9369)`) menjadi persentase murni pada `paper_outline.md`, `paper/*.md`, dan `paper_latex_id/sections/*.tex`.
* 0 sisa pola `% (0.xxxx)` terverifikasi di seluruh naskah.

### E. Penyempurnaan Tata Letak Visual LaTeX
* **Figure 2**: Meregenerasi `images/sample_demogpairs.png` (3225×620 px) dari 6 file gambar asli dengan tinggi seragam 500 px dalam susunan 1 baris × 6 kolom berlabel (a)-(f).
* **Table II**: Menghapus `\textbf` pada baris usulan agar tidak menonjol berlebihan.
* **Tables III–VI**: Meratakan baris *Total Grid Combinations* ke kanan menggunakan `\multicolumn{2}{r}`.
* **Table XII**: Menyederhanakan header menjadi single-column `Ours`.
* **Biografi Penulis**: Menghapus tautan ORCID di narasi paragraf biografi `paper/07_biographies.md` dan `07_biographies.tex` karena sudah tercantum pada superskrip judul.
* Kompilasi PDF: **14 halaman**, 0 *undefined citations*, 0 *BibTeX warnings*.

---

## 4. ARSITEKTUR TAUTAN SITASI DAN VERIFIKASI MULTI-LAPIS

```
[Lapis 1: Berkas Sumber Primer - paper/references/ (51 berkas .bib, .ris, .nbib)]
  └── Metadata resmi: penulis, judul, jurnal, vol/no/pp/Art. no., bulan/tahun, DOI
        │
        ▼ (Audit field-by-field oleh subagent)
[Lapis 2: Daftar Pustaka Utama - paper/06_references.md (entri [1]-[51])]
  └── Jangkar HTML <a id="refN"></a>; IEEE sentence-case; format IEEE Access
        │
        ▼ (Penyematan tautan interaktif [[N]](06_references.md#refN))
[Lapis 3: Teks Kalimat Klaim - paper/*.md (91 tautan sitasi interaktif)]
  └── Format presisi sebelum tanda baca terminal; urutan monotonik; reuse konsisten
        │
        ▼ (Audit pemetaan silang registri)
[Lapis 4: Registri Audit Kalimat - paper/references.txt]
        │
        ▼ (Sinkronisasi berkas bibliografi BibTeX)
[Lapis 5: Basis Data LaTeX - paper_latex_id/references.bib (51 entri ref1-ref51)]
        │
        ▼ (Kompilasi naskah publikasi)
[Lapis 6: Naskah Publikasi Resmi - paper_latex_id/access.pdf (14 Halaman, PASS)]
```

---

## 5. REKAPITULASI COMMIT GIT HARI INI (08 SEPTEMBER 2026)

| Hash | Agen / Pengunggah | Scope | Pesan Commit & Ringkasan |
|:---:|:---:|:---|:---|
| `5fbb7f8` | AGY | `docs(paper)` | standardize IEEE citation style and metadata in Section VI |
| `64a9445` | AGY | `docs(paper)` | add modular reference audit logs for entries [1]-[51] |
| `82bbc3a` | AGY | `docs(paper)` | add interactive IEEE citation links in Section I (Introduction) |
| `cbbb2a1` | AGY | `docs(paper)` | add interactive IEEE citation links in Section II (Related Works) |
| `0e7c560` | AGY | `docs(paper)` | add interactive IEEE citation links in Section III (Materials and Methods) |
| `52eaf08` | AGY | `docs(paper)` | add interactive IEEE citation links in Section IV (Results and Discussion) |
| `1133c75` | AGY | `chore` | update prompt history log |
| `b9c24de` | OpenCode | `docs(references)` | verify and polish 51 reference entries in Section VI |
| `453df67` | OpenCode | `docs(citations)` | audit interactive citations across paper/*.md and add month consistency |
| `a8ef192` | OpenCode | `style(latex)` | sync paper_latex_id to 51 bib entries, normalize metric percentages, and polish layout |

---

## 6. STATUS AKHIR & KESIAPAN TAHAP SELANJUTNYA

- Seluruh sistem referensi ilmiah korpus naskah Markdown dan paket LaTeX telah 100% tersinkronisasi, tervalidasi terhadap berkas sumber primer, dan bebas dari cacat redaksional maupun tata letak.
- Cabang `main` telah sinkron bersih dengan *remote repository* GitHub.
