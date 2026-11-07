# Hasil Audit dan Perbaikan Referensi [41] - [45]

Dokumen ini memuat laporan audit komprehensif dan teks perbaikan final untuk entri referensi nomor [41] sampai [45] pada berkas `paper/06_references.md`. Audit dilakukan secara teliti terhadap berkas sumber asli di `paper/references/` dengan berpedoman pada kaidah IEEE di `rules/IEEE_citation_guidelines.md` serta aturan format Markdown di `rules/md_rules.txt`.

---

## 1. Rincian Temuan Audit Tiap Referensi

### [41] Yang et al. (2022)
- **Berkas Sumber**: `paper/references/2022_Hybrid fuzzy multiple SVM classifier through feature fusion based on convolution neural networks and its practical applications.bib`
- **Tipe Dokumen**: Artikel Jurnal (*Expert Systems with Applications*)
- **Penulis di Sumber**:
  - `Cheng Yang` -> `C. Yang`
  - `Sung-Kwun Oh` -> `S.-K. Oh`
  - `Bo Yang` -> `B. Yang`
  - `Witold Pedrycz` -> `W. Pedrycz`
  - `Lin Wang` -> `L. Wang`
  - Total penulis: 5 orang.
- **Evaluasi Penulis**: Jumlah penulis <= 6, sehingga seluruh nama penulis wajib dicantumkan lengkap dengan format inisial nama depan diikuti nama keluarga (`C. Yang, S.-K. Oh, B. Yang, W. Pedrycz, and L. Wang`).
- **Judul Artikel**:
  - Teks: `"Hybrid fuzzy multiple SVM classifier through feature fusion based on convolution neural networks and its practical applications"`
  - Evaluasi: Judul telah memenuhi kaidah *sentence-case*. Huruf pertama kalimat ("Hybrid") dan akronim teknis ("SVM") ditulis kapital, sedangkan frasa lainnya ("fuzzy multiple", "classifier through feature fusion based on convolution neural networks and its practical applications") ditulis dengan huruf kecil. Diapit tanda kutip ganda.
- **Nama Jurnal**:
  - Sumber: `Expert Systems with Applications`
  - Format IEEE: `*Expert Systems with Applications*` (dicetak miring dengan tanda bintang Markdown).
- **Volume, Isu, Halaman / Nomor Artikel, Tahun, & DOI**:
  - Volume: `vol. 202`
  - Nomor Artikel: `Art. no. 117392` (Elsevier mengalokasikan nomor artikel 6-digit untuk edisi ini).
  - Tahun: `2022`
  - DOI: `doi: 10.1016/j.eswa.2022.117392` (tanpa prefiks `https://doi.org/`).
- **Pemeriksaan Karakter Terlarang & Anchor**:
  - Bebas dari em dash (`—`), tanda pemisah menggunakan tanda hubung biasa (`-`).
  - Bebas dari kata terlarang (`kendati`, `paradigma`, `guna`).
  - Tag anchor `<a id="ref41"></a>` terpasang sebelum entri.
- **Status Audit**: SUDAH VALID dan sesuai standar IEEE.

---

### [42] Nguyen Nhu Y. et al. (2022)
- **Berkas Sumber**: `paper/references/2022_Churn prediction in telecommunication industry using kernel Support Vector Machines.bib`
- **Tipe Dokumen**: Artikel Jurnal (*PLOS ONE*)
- **Penulis di Sumber**:
  - Sumber BibTeX: `Y., Nguyen Nhu AND Ly, Tran Van AND Son, Dao Vu Truong`
  - Analisis Struktur Nama:
    - Penulis pertama merupakan peneliti asal Vietnam (Nguyen Nhu Y). Dalam sistem pengindeksan penerbit PLOS ONE dan CrossRef, nama keluarga tercatat sebagai `Y.` dengan nama depan `Nguyen Nhu`. Berdasarkan format inisial diikuti nama keluarga, entri menghasilkan `N. N. Y.`.
    - Penulis kedua: `Ly, Tran Van` -> inisial `T. V.`, nama keluarga `Ly` -> `T. V. Ly`.
    - Penulis ketiga: `Son, Dao Vu Truong` -> inisial `D. V. T.`, nama keluarga `Son` -> `D. V. T. Son`.
  - Total penulis: 3 orang.
- **Evaluasi Penulis**: Jumlah penulis <= 6, sehingga seluruh penulis dicantumkan: `N. N. Y., T. V. Ly, and D. V. T. Son`.
- **Judul Artikel**:
  - Teks awal: `"Churn prediction in telecommunication industry using kernel Support Vector Machines,"`
  - Temuan audit: Kata "Support Vector Machines" pada teks awal masih memakai huruf kapital (Title Case).
  - Pembetulan: Sesuai kaidah *sentence-case* IEEE, nama metode pembelajaran mesin umum seperti *support vector machines* bukan nama diri (*proper noun*) sehingga wajib ditulis dalam huruf kecil.
  - Teks setelah perbaikan: `"Churn prediction in telecommunication industry using kernel support vector machines,"`
- **Nama Jurnal**:
  - Sumber: `PLOS ONE`
  - Format IEEE: `*PLOS ONE*` (dicetak miring).
- **Volume, Isu, Rentang Halaman, Tahun, & DOI**:
  - Volume: `vol. 17`
  - Isu: `no. 5`
  - Halaman: `pp. 1-18` (sesuai data pada berkas sumber BibTeX `pages = {1-18}` dan konsisten dengan referensi PLOS ONE lainnya seperti [50]).
  - Tahun: `2022`
  - DOI: `doi: 10.1371/journal.pone.0267935` (tanpa prefiks `https://doi.org/`).
- **Pemeriksaan Karakter Terlarang & Anchor**:
  - Bebas dari em dash (`—`), seluruh pemisah berupa tanda hubung biasa (`-`).
  - Bebas dari kata terlarang (`kendati`, `paradigma`, `guna`).
  - Tag anchor `<a id="ref42"></a>` terpasang sebelum entri.
- **Status Audit**: DIBETULKAN (kapitalisasi judul diubah menjadi *sentence-case* murni).

---

### [43] Guido, Groccia, & Conforti (2023)
- **Berkas Sumber**: `paper/references/2022_A hyper-parameter tuning approach for cost-sensitive support vector machine classifiers.ris`
- **Tipe Dokumen**: Artikel Jurnal (*Soft Computing*)
- **Penulis di Sumber**:
  - `Guido, Rosita` -> `R. Guido`
  - `Groccia, Maria Carmela` -> `M. C. Groccia`
  - `Conforti, Domenico` -> `D. Conforti`
  - Total penulis: 3 orang.
- **Evaluasi Penulis**: Jumlah penulis <= 6, seluruh 3 nama penulis dicantumkan lengkap (`R. Guido, M. C. Groccia, and D. Conforti`).
- **Judul Artikel**:
  - Teks: `"A hyper-parameter tuning approach for cost-sensitive support vector machine classifiers,"`
  - Evaluasi: Judul telah menggunakan format *sentence-case* yang tepat. Istilah "support vector machine" telah berhuruf kecil, dan kata majemuk "hyper-parameter" serta "cost-sensitive" menggunakan tanda hubung biasa.
- **Nama Jurnal**:
  - Sumber: `Soft Computing`
  - Format IEEE: `*Soft Computing*` (dicetak miring).
- **Volume, Isu, Rentang Halaman, Tahun, & DOI**:
  - Volume: `vol. 27`
  - Isu: `no. 18`
  - Halaman: `pp. 12863-12881` (menggunakan tanda hubung `-`).
  - Tahun: `2023` (berkas RIS memuat `PY - 2023` dan `DA - 2023/09/01`; publikasi daring awal dimulai akhir 2022 namun volume dan nomor terbit resmi pada September 2023).
  - DOI: `doi: 10.1007/s00500-022-06768-8` (tanpa prefiks `https://doi.org/`).
- **Pemeriksaan Karakter Terlarang & Anchor**:
  - Bebas dari em dash (`—`).
  - Bebas dari kata terlarang (`kendati`, `paradigma`, `guna`).
  - Tag anchor `<a id="ref43"></a>` terpasang sebelum entri.
- **Status Audit**: SUDAH VALID dan sesuai standar IEEE.

---

### [44] Rashidi et al. (2023)
- **Berkas Sumber**: `paper/references/2023_Common statistical concepts in the supervised Machine Learning arena.nbib`
- **Tipe Dokumen**: Artikel Jurnal (*Frontiers in Oncology*)
- **Penulis di Sumber**:
  - `Rashidi, Hooman H` -> `H. H. Rashidi`
  - `Albahra, Samer` -> `S. Albahra`
  - `Robertson, Scott` -> `S. Robertson`
  - `Tran, Nam K` -> `N. K. Tran`
  - `Hu, Bo` -> `B. Hu`
  - Total penulis: 5 orang.
- **Evaluasi Penulis**: Jumlah penulis <= 6, seluruh 5 nama penulis dicantumkan lengkap (`H. H. Rashidi, S. Albahra, S. Robertson, N. K. Tran, and B. Hu`).
- **Judul Artikel**:
  - Teks awal: `"Common statistical concepts in the supervised Machine Learning arena,"`
  - Temuan audit: Kata "Machine Learning" ditulis dengan huruf kapital M dan L, menyalahi aturan *sentence-case*.
  - Pembetulan: Bidang "machine learning" bukan nama diri (*proper noun*), sehingga diubah menjadi huruf kecil (*sentence-case*).
  - Teks setelah perbaikan: `"Common statistical concepts in the supervised machine learning arena,"`
- **Nama Jurnal**:
  - Sumber: `Frontiers in oncology`
  - Format IEEE: `*Frontiers in Oncology*` (dicetak miring, Title Case).
- **Volume, Nomor Artikel, Tahun, & DOI**:
  - Volume: `vol. 13`
  - Nomor Artikel: `Art. no. 1130229` (pengidentifikasi artikel e-collection Frontiers).
  - Tahun: `2023`
  - DOI: `doi: 10.3389/fonc.2023.1130229` (tanpa prefiks `https://doi.org/`).
- **Pemeriksaan Karakter Terlarang & Anchor**:
  - Bebas dari em dash (`—`).
  - Bebas dari kata terlarang (`kendati`, `paradigma`, `guna`).
  - Tag anchor `<a id="ref44"></a>` terpasang sebelum entri.
- **Status Audit**: DIBETULKAN (kapitalisasi judul diubah menjadi *sentence-case* murni).

---

### [45] De Diego et al. (2022)
- **Berkas Sumber**: `paper/references/2022_General Performance Score for classification problems.ris`
- **Tipe Dokumen**: Artikel Jurnal (*Applied Intelligence*)
- **Penulis di Sumber**:
  - `De Diego, Isaac Martín` -> `I. M. De Diego` (nama keluarga gabungan Spanyol)
  - `Redondo, Ana R.` -> `A. R. Redondo`
  - `Fernández, Rubén R.` -> `R. R. Fernández`
  - `Navarro, Jorge` -> `J. Navarro`
  - `Moguerza, Javier M.` -> `J. M. Moguerza`
  - Total penulis: 5 orang.
- **Evaluasi Penulis**: Jumlah penulis <= 6, seluruh 5 nama penulis dicantumkan lengkap (`I. M. De Diego, A. R. Redondo, R. R. Fernández, J. Navarro, and J. M. Moguerza`).
- **Judul Artikel**:
  - Teks awal: `"General Performance Score for classification problems,"`
  - Temuan audit: Kata "Performance Score" ditulis dengan huruf kapital P dan S.
  - Pembetulan: Sesuai pedoman IEEE mengenai *sentence-style capitalization*, hanya huruf pertama judul, nama diri, dan akronim yang dikapitalisasi. Frasa umum "performance score" diubah menjadi huruf kecil.
  - Teks setelah perbaikan: `"General performance score for classification problems,"`
- **Nama Jurnal**:
  - Sumber: `Applied Intelligence`
  - Format IEEE: `*Applied Intelligence*` (dicetak miring).
- **Volume, Isu, Rentang Halaman, Tahun, & DOI**:
  - Volume: `vol. 52`
  - Isu: `no. 10`
  - Halaman: `pp. 12049-12063` (menggunakan tanda hubung biasa `-`).
  - Tahun: `2022`
  - DOI: `doi: 10.1007/s10489-021-03041-7` (tanpa prefiks `https://doi.org/`).
- **Pemeriksaan Karakter Terlarang & Anchor**:
  - Bebas dari em dash (`—`).
  - Bebas dari kata terlarang (`kendati`, `paradigma`, `guna`).
  - Tag anchor `<a id="ref45"></a>` terpasang sebelum entri.
- **Status Audit**: DIBETULKAN (kapitalisasi judul disesuaikan ke *sentence-case*).

---

## 2. Teks Final Entri Referensi [41] - [45]

Berikut adalah teks referensi final yang telah diaudit, disesuaikan dengan seluruh aturan IEEE, diverifikasi terhadap berkas sumber, serta disinkronkan ke dalam `paper/06_references.md`:

```markdown
<a id="ref41"></a>
[41] C. Yang, S.-K. Oh, B. Yang, W. Pedrycz, and L. Wang, "Hybrid fuzzy multiple SVM classifier through feature fusion based on convolution neural networks and its practical applications," *Expert Systems with Applications*, vol. 202, Art. no. 117392, 2022, doi: 10.1016/j.eswa.2022.117392.

<a id="ref42"></a>
[42] N. N. Y., T. V. Ly, and D. V. T. Son, "Churn prediction in telecommunication industry using kernel support vector machines," *PLOS ONE*, vol. 17, no. 5, pp. 1-18, 2022, doi: 10.1371/journal.pone.0267935.

<a id="ref43"></a>
[43] R. Guido, M. C. Groccia, and D. Conforti, "A hyper-parameter tuning approach for cost-sensitive support vector machine classifiers," *Soft Computing*, vol. 27, no. 18, pp. 12863-12881, 2023, doi: 10.1007/s00500-022-06768-8.

<a id="ref44"></a>
[44] H. H. Rashidi, S. Albahra, S. Robertson, N. K. Tran, and B. Hu, "Common statistical concepts in the supervised machine learning arena," *Frontiers in Oncology*, vol. 13, Art. no. 1130229, 2023, doi: 10.3389/fonc.2023.1130229.

<a id="ref45"></a>
[45] I. M. De Diego, A. R. Redondo, R. R. Fernández, J. Navarro, and J. M. Moguerza, "General performance score for classification problems," *Applied Intelligence*, vol. 52, no. 10, pp. 12049-12063, 2022, doi: 10.1007/s10489-021-03041-7.
```
