# Standard Operating Procedure: Research Manuscript Pipeline (WORKFLOW.md)

Dokumen ini merupakan **panduan standar operasional universal (*Universal Research Manuscript Pipeline SOP*)** untuk mentransformasikan ide, metodologi, dan hasil eksperimen penelitian menjadi manuskrip publikasi jurnal internasional bereputasi tinggi (misal: IEEE, Elsevier, Springer, Nature, dsb.).

Pedoman ini bersifat **agnostik terhadap topik penelitian** (*project-independent*) dan dirancang untuk dapat direplikasi pada berbagai repositori riset berbasis kecerdasan buatan (*AI*), visi komputer (*Computer Vision*), pemrosesan bahasa alami (*NLP*), maupun komputasi biomedis.

---

## 🗺️ Kerangka Kerja Alur 4 Tahap (The 4-Stage Manuscript Lifecycle)

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
│ - Modularisasi naskah (sections/*.tex)│ │ - Naskah final siap submit (Camera-   │
│ - Kompilasi master: access.tex ->     │ │   Ready / Submission Package)         │
│   access.pdf                          │ │ - Kompilasi master: access.tex ->     │
│ - Validasi struktur & tinjauan tim    │ │   access.pdf                          │
│                                       │ │ - Sinkronisasi 1-ke-1 label, rumus,   │
│                                       │ │   tabel, gambar, dan references.bib   │
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
├── 04_results-and-discussion_a-global-performance.md   # Section IV-A: Benchmark performa global 28 model (Table II-V)
├── 04_results-and-discussion_b-feature-ablation-analysis.md # Section IV-B: Analisis ablasi fitur & kontribusi domain
├── 04_results-and-discussion_c-intersectional-subgroup-performance-analysis.md # Section IV-C: Evaluasi performa subkelompok & disparitas (Table VI)
├── 04_results-and-discussion_d-error-pattern-analysis.md # Section IV-D: Analisis pola kesalahan & confusion matrix (Figure 4)
├── 04_results-and-discussion_e-analysis-of-selected-svm-kernel-configuration.md # Section IV-E: Analisis konfigurasi kernel SVM
├── 04_results-and-discussion_f-comparison-with-prior-studies.md # Section IV-F: Perbandingan komparatif studi terdahulu (Table VII)
├── 05_conclusion.md                                    # Section V: Kesimpulan, limitasi riset, dan rencana masa depan
├── 06_references.md                                    # Section VI: Daftar pustaka format IEEE
├── 07_biographies.md                                   # Section VII: Biografi akademik seluruh penulis
├── acronyms.txt                                        # Registri pelacakan singkatan & akronim pertama kali (Rule 1.3)
├── references.txt                                      # Registri audit sitasi tingkat kalimat (Sentence-Level Citation)
├── references/                                         # Direktori 47 berkas sumber bibliografi (.bib, .ris, .nbib, .bibtex)
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
    ├── 04_results-and-discussion_*.tex# \section{Results and Discussion} & 6 sub-bagian modular
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

## 🔄 Matriks Pemetaan Universal (Universal Mapping Matrix)

| Modul Manuskrip | Draf Markdown (`paper/`) | Berkas LaTeX (`sections/*.tex`) | Elemen Standar yang Terkandung |
|:---|:---|:---|:---|
| **Judul & Penulis** | `00_abstract.md` | `00_title.tex` | Judul artikel, profil penulis, afiliasi, ORCID, korespondensi |
| **Abstrak & Keywords**| `00_abstract.md` | `00_abstract.tex` | Blok abstrak ringkas, daftar kata kunci (IEEE Keywords) |
| **I. Pendahuluan** | `01_introduction.md` | `01_introduction.tex` | Latar belakang, urgensi, kesenjangan riset, butir kontribusi, organisasi naskah |
| **II. Studi Terkait** | `02_related-works.md` | `02_related-works.tex` | Tinjauan pustaka tematik (klasifikasi atribut, fusi multi-domain, representasi ViT, disparitas) |
| **III. Metodologi (Pengantar)**| `03_materials-and-methods_0-overview.md` | `03_materials-and-methods_0-overview.tex` | Narasi pengantar metodologi & Arsitektur Framework Sistem ([Figure 1](images/method.png)) |
| **III-A. Dataset** | `03_materials-and-methods_a-dataset.md` | `03_materials-and-methods_a-dataset.tex` | Deskripsi dataset DemogPairs, partisi data 80/20, [Figure 2](images/sample_Asian_Females.jpg), dan [Table I](#tab1) |
| **III-B. Vision Transformer** | `03_materials-and-methods_b-vision-transformer.md` | `03_materials-and-methods_b-vision-transformer.tex` | Ekstraksi fitur ViT [CLS], proyeksi patch, representasi multi-domain, [Figure 3](images/vit.png), Eq. (1)-(5) |
| **III-C. Random Forest** | `03_materials-and-methods_c-random-forest.md` | `03_materials-and-methods_c-random-forest.tex` | Formulasi ansambel Random Forest, kriteria Gini impurity, dan Eq. (6) |
| **III-D. Gaussian Naive Bayes**| `03_materials-and-methods_d-gaussian-naive-bayes.md`| `03_materials-and-methods_d-gaussian-naive-bayes.tex`| Teorema Bayes, asumsi independensi fitur Gaussian, dan Eq. (7) |
| **III-E. Logistic Regression**| `03_materials-and-methods_e-logistic-regression.md` | `03_materials-and-methods_e-logistic-regression.tex` | Regresi logistik multinomial, fungsi softmax, regularisasi L2, dan Eq. (8) |
| **III-F. Support Vector Machine**| `03_materials-and-methods_f-support-vector-machine.md`| `03_materials-and-methods_f-support-vector-machine.tex`| Margin optimal, fungsi kernel polinomial derajat 2, dan Eq. (9) |
| **III-G. Pipeline Klasifikasi**| `03_materials-and-methods_g-classification-pipeline.md`| `03_materials-and-methods_g-classification-pipeline.tex`| Pipeline terisolasi Scaler + PCA, 5-Fold Stratified Cross-Validation, GridSearchCV |
| **III-H. Metrik Evaluasi** | `03_materials-and-methods_h-evaluation-metrics.md` | `03_materials-and-methods_h-evaluation-metrics.tex` | Skema One-vs-Rest (OvR), akurasi, presisi, recall, F1-score subkelompok & global, Eq. (10)-(17) |
| **IV-A. Performa Global** | `04_results-and-discussion_a-global-performance.md`| `04_results-and-discussion_a-global-performance.tex`| Tolok ukur 28 model, evaluasi data uji held-out, ranking pengklasifikasi, [Table II-V](#tab2) |
| **IV-B. Analisis Ablasi Fitur**| `04_results-and-discussion_b-feature-ablation-analysis.md`| `04_results-and-discussion_b-feature-ablation-analysis.tex`| Perbandingan skema representasi single, dual, dan tri-domain |
| **IV-C. Performa Subkelompok**| `04_results-and-discussion_c-intersectional-subgroup-performance-analysis.md`| `04_results-and-discussion_c-intersectional-subgroup-performance-analysis.tex`| Evaluasi performa 6 kelas demografis interseksional & profil rentang disparitas, [Table VI](#tab6) |
| **IV-D. Pola Kesalahan** | `04_results-and-discussion_d-error-pattern-analysis.md`| `04_results-and-discussion_d-error-pattern-analysis.tex`| Analisis matriks konfusi 6x6 model terbaik SVM Tri-Domain ([Figure 4](images/confusion_matrix.png)) |
| **IV-E. Konfigurasi Kernel SVM**| `04_results-and-discussion_e-analysis-of-selected-svm-kernel-configuration.md`| `04_results-and-discussion_e-analysis-of-selected-svm-kernel-configuration.tex`| Justifikasi empiris pemilihan kernel polynomial derajat dua dan parameterisasi $C=10$ |
| **IV-F. Studi Terdahulu** | `04_results-and-discussion_f-comparison-with-prior-studies.md`| `04_results-and-discussion_f-comparison-with-prior-studies.tex`| Perbandingan langsung tolok ukur DemogPairs dengan studi terdahulu, [Table VII](#tab7) |
| **V. Kesimpulan** | `05_conclusion.md` | `05_conclusion.tex` | Kesimpulan utama, batasan penelitian, dan rekomendasi arah riset lanjutan |
| **Referensi** | `06_references.md` / `references.txt` | `references.bib` | Basis data BibTeX terpadu (`@article`, `@inproceedings`, `@book`) |
| **Biografi** | `07_biographies.md` | `07_biographies.tex` | Biografi akademik dan penyematan foto seluruh penulis |

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
5. **Kepatuhan Struktur Sintaksis SPOK & Kesiapan Translasi SVO:**
   - Setiap kalimat dalam draf naskah wajib memiliki struktur Subjek (S) dan Predikat (P) yang definitif untuk mencegah kalimat menggantung (*dangling sentences*). Variasikan antara pola S-P-O-K murni, transisi K-S-P-O terukur, dan bentuk pasif akademis objektif pada metodologi untuk mempermudah pemetaan ke struktur SVO/SVOC pada naskah LaTeX Bahasa Inggris standar IEEE.
6. **Sistem Audit Sitasi Tingkat Kalimat (Sentence-Level Citation Audit):**
   - Seluruh klaim literatur dan fakta eksternal dalam naskah Markdown wajib dicatat secara granular pada `paper/references.txt` dan diverifikasi kecocokan teks kutipannya terhadap berkas sumber di `paper/references/` sebelum ditransformasikan ke berkas `references.bib` pada naskah LaTeX.
7. **Pelacakan Akronim Terpusat (Centralized Acronym Registry):**
   - Seluruh singkatan teknis dicatat pada `paper/acronyms.txt` untuk memastikan kepatuhan aturan pemunculan pertama kali (*first-mention full form*) dan mencegah repetisi kepanjangan akronim pada paragraf-paragraf berikutnya.
