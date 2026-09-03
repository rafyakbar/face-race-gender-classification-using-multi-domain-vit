# Standard Operating Procedure: Research Manuscript Pipeline (WORKFLOW.md)

Dokumen ini merupakan **panduan standar operasional universal (*Universal Research Manuscript Pipeline SOP*)** untuk mentransformasikan ide, metodologi, dan hasil eksperimen penelitian menjadi manuskrip publikasi jurnal internasional bereputasi tinggi (misal: IEEE, Elsevier, Springer, Nature, dsb.).

Pedoman ini bersifat **agnostik terhadap topik penelitian** (*project-independent*) dan dirancang untuk dapat direplikasi pada berbagai repositori riset berbasis kecerdasan buatan (*AI*), visi komputer (*Computer Vision*), pemrosesan bahasa alami (*NLP*), maupun komputasi biomedis.

---

## 🗺️ Paradigma Alur 4 Tahap (The 4-Stage Manuscript Lifecycle)

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
│   - Kepatuhan ketat terhadap target kata per paragraf & sitasi literatur terkait │
│   - Integrasi tabel dan visualisasi data hasil eksperimen                        │
└────────────────────────────────────────┬─────────────────────────────────────────┘
                                         │
                    ┌────────────────────┴────────────────────┐
                    ▼                                         ▼
┌───────────────────────────────────────┐ ┌───────────────────────────────────────┐
│     TAHAP 3: LATEX BAHASA INDONESIA   │ │      TAHAP 4: LATEX BAHASA INGGRIS    │
│           (paper_latex_id/)           │ │           (paper_latex_en/)           │
│ - Implementasi template jurnal target │ │ - Implementasi template jurnal target │
│ - Modularisasi naskah (sections/*.tex)│ │ - Naskah final siap submit (Camera-   │
│ - Kompilasi master: main.tex /        │ │   Ready / Submission Package)         │
│   access.tex                          │ │ - Sinkronisasi 1-ke-1 label, rumus,   │
│ - Validasi struktur & tinjauan tim    │ │   tabel, gambar, dan references.bib   │
└───────────────────────────────────────┘ └───────────────────────────────────────┘
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

#### Konvensi Penamaan Berkas Universal:
```
paper/
├── 00_abstract.md                                      # Metadata, Judul, Abstrak, Kata Kunci
├── 01_introduction.md                                  # Latar belakang, urgensi, gap, kontribusi, sistematika
├── 02_related-works.md                                 # Tinjauan literatur tematik & posisi riset
├── 03_materials-and-methods_overview.md                # Teks pengantar metodologi & Figure 1 (Arsitektur Pipeline)
├── 03_materials-and-methods_a-dataset.md               # A. Deskripsi dataset, partisi data, pra-pemrosesan
├── 03_materials-and-methods_b-[core-component-1].md    # B. Komponen metodologi 1 (e.g. feature extractors)
├── 03_materials-and-methods_c-[core-component-2].md    # C. Komponen metodologi 2 (e.g. fusion framework)
├── 03_materials-and-methods_d-[core-component-3].md    # D. Pengklasifikasi / model / optimasi pipeline
├── 03_materials-and-methods_e-experimental-setup.md    # E. Desain eksperimen, validasi silang, parameter komputasi
├── 03_materials-and-methods_f-computational-env.md      # F. Lingkungan komputasi & spesifikasi reproduktibilitas
├── 03_materials-and-methods_g-evaluation-metrics.md    # G. Formulasi metrik evaluasi & kriteria disparitas
├── 04_results-and-discussion_a-[main-benchmark].md     # A. Hasil evaluasi tolok ukur utama (global benchmark)
├── 04_results-and-discussion_b-ablation-study.md       # B. Analisis ablasi fitur/komponen
├── 04_results-and-discussion_c-subgroup-analysis.md    # C. Analisis granular per kelas/subgrup/disparitas
├── 04_results-and-discussion_d-error-analysis.md       # D. Analisis pola kesalahan / matriks konfusi
├── 04_results-and-discussion_e-complexity.md           # E. Kompleksitas komputasi & efisiensi waktu
├── 04_results-and-discussion_f-prior-comparison.md     # F. Perbandingan komparatif dengan studi terdahulu
├── 05_conclusion.md                                    # Kesimpulan, limitasi riset, dan arah riset mendatang
├── 06_references.md                                    # Daftar pustaka lengkap
├── 07_biographies.md                                   # Profil akademik dan biografi penulis
└── images/                                             # Arsip visual diagram, grafik, dan foto
```

---

### 3. Tahap 3 & 4: Modular LaTeX (`paper_latex_id/` & `paper_latex_en/`)
Folder LaTeX mengimplementasikan template resmi penerbit (misal: `IEEEtran.cls`, `ieeeaccess.cls`, `elsarticle.cls`, `springer.cls`).

#### Struktur Direktori LaTeX:
```
paper_latex_[id|en]/
├── main.tex (atau access.tex)        # File induk LaTeX (memuat preamble & \input{})
├── references.bib                    # Basis data BibTeX lengkap
├── template_class.cls / .bst         # Style class & bibliography format resmi
├── images/                           # File gambar beresolusi tinggi (PDF/EPS/PNG 300 DPI)
└── sections/                         # Berkas teks LaTeX modular
    ├── 00_title.tex                  # \title{}, \author{}, \affil{}, \corresp{}
    ├── 00_abstract.tex               # \begin{abstract} ... \end{abstract}
    ├── 01_introduction.tex           # \section{Introduction}
    ├── 02_related-works.tex          # \section{Related Works}
    ├── 03_materials-and-methods_*.tex# \section{Materials and Methods} & \subsection{}
    ├── 04_results-and-discussion_*.tex# \section{Results and Discussion} & \subsection{}
    ├── 05_conclusion.tex             # \section{Conclusion}
    └── 07_biographies.tex            # Biografi & foto (\begin{IEEEbiography})
```

---

## 🔄 Matriks Pemetaan Universal (Universal Mapping Matrix)

| Modul Manuskrip | Draf Markdown (`paper/`) | Berkas LaTeX (`sections/*.tex`) | Elemen Standar yang Terkandung |
|:---|:---|:---|:---|
| **Judul & Penulis** | `00_abstract.md` | `00_title.tex` | Title, Authors, Affiliation, ORCID, Corresponding Email |
| **Abstrak & Keywords**| `00_abstract.md` | `00_abstract.tex` | Abstract block, Index Terms / Keywords |
| **I. Pendahuluan** | `01_introduction.md` | `01_introduction.tex` | Background, Problem, Gap, Contributions (bullet), Paper Organization |
| **II. Studi Terkait** | `02_related-works.md` | `02_related-works.tex` | Literature Review by thematic topics, Positioning table |
| **III. Metodologi (Pengantar)**| `03_materials-and-methods_overview.md` | `03_materials-and-methods_overview.tex` | Lead-in text & Overall Pipeline Architecture (Figure 1) |
| **III-A. Dataset** | `03_materials-and-methods_a-dataset.md` | `03_materials-and-methods_a-dataset.tex` | Dataset Partition & Distribution (Figure 2 & Table I) |
| **III-B s.d. III-G. Metodologi**| `03_materials-and-methods_[b-g]-*.md` | `03_materials-and-methods_[b-g]-*.tex` | Feature extraction (Figure 3, Table II, Eq 1-4), Fusion (Eq 5), Classifiers (Table III-VI, Eq 6-9), Setup, Metrics (Eq 10-19) |
| **IV-A s.d. IV-F. Hasil & Diskusi**| `04_results-and-discussion_[a-f]-*.md`| `04_results-and-discussion_[a-f]-*.tex`| Benchmark (Table VII-X), Ablation, Subgroup/Disparity (Table XI), Error Matrix (Figure 4), Complexity, Prior Studies (Table XII) |
| **V. Kesimpulan** | `05_conclusion.md` | `05_conclusion.tex` | Concluding remarks, Limitations (bullet), Future Directions (bullet) |
| **Referensi** | `06_references.md` | `references.bib` | Standard BibTeX database (`@article`, `@inproceedings`, `@book`) |
| **Biografi** | `07_biographies.md` | `07_biographies.tex` | Biographies with photo embeddings |

---

## 🛡️ Standar Mutu Akademik & Aturan Eksekusi (Quality Assurance)

Untuk memastikan manuskrip memenuhi standar jurnal internasional bereputasi tinggi:

1. **Prinsip Ground-Truth Empiris (Zero-Tolerance for Inconsistency):**
   - Seluruh angka metrik (Akurasi, Precision, Recall, F1, Loss, Latensi) wajib persis sama di semua representasi (kode, log eksperimen, markdown, dan LaTeX) hingga batas desimal yang ditentukan (standar: 4 angka di belakang koma).
2. **Kepatuhan Tipografi & Format:**
   - **Hindari penggunaan tanda pisah em dash (`—` atau `–`)** pada naskah jika dilarang oleh pedoman; gunakan tanda hubung standar (`-`), titik dua (`:`), atau tanda kurung `(...)`.
   - Pisahkan teks deskriptif biasa (`224 × 224`, `80/20`, rasio sampel) dari variabel matematika dalam math mode ($N=2.160$, $\mathbf{z}_L^0$).
   - Gunakan layout lebar penuh (`table*` atau `figure*`) hanya untuk tabel/grafik perbandingan multi-kolom yang lebar; gunakan layout kolom tunggal (`table` atau `figure`) untuk elemen kompak.
3. **Pemberian Kalimat Topik & Kohesi Paragraf:**
   - Setiap paragraf harus diawali dengan kalimat topik (*topic sentence*) yang kuat, diikuti kalimat penjelas berbobot dan sitasi pendukung, serta ditutup dengan kalimat transisi kohesif menuju paragraf berikutnya.
4. **Protokol Delegasi Subagent (Modular Drafting & Auditing):**
   - Saat menulis atau mengaudit draf manuskrip, delegasikan **1 subagent independen untuk 1 file spesifik** dengan instruksi yang terfokus agar konteks penulisan dan akurasi tetap maksimal.
