# Audit dan Pembetulan Referensi [36] - [40]

Dokumen ini memuat hasil audit komprehensif dan teks perbaikan final untuk referensi nomor [36] sampai [40] pada naskah artikel ilmiah, merujuk pada pedoman IEEE (`rules/IEEE_citation_guidelines.md`), aturan Markdown (`rules/md_rules.txt`), serta berkas sumber BibTeX di `paper/references/`.

---

## 1. Rincian Temuan Audit per Referensi

### [36] Norrena et al. (2024)
- **Berkas Sumber**: `paper/references/2024_Coupling of Solidification and Heat Transfer Simulations with Interpretable Machine Learning Algorithms to Predict Transverse Cracks in Continuous Cast.bibtex`
- **Audit Penulis**:
  - Penulis pada sumber: Julius Norrena, Seppo Louhenkilpi, Ville-Valtteri Visuri, Tuomas Alatarvas, Agne Bogdanoff, Timo Fabritius (total 6 penulis).
  - Evaluasi aturan: Karena jumlah penulis $\le 6$, seluruh 6 nama penulis wajib ditulis lengkap (inisial nama depan diikuti nama keluarga).
  - Format IEEE: `J. Norrena, S. Louhenkilpi, V.-V. Visuri, T. Alatarvas, A. Bogdanoff, and T. Fabritius` (sesuai).
- **Audit Judul Artikel**:
  - Teks awal: `"Coupling of Solidification and Heat Transfer Simulations with Interpretable Machine Learning Algorithms to Predict Transverse Cracks in Continuous Casting of Steel,"`
  - Temuan audit: Judul awal masih menggunakan Title Case (setiap kata diawali huruf kapital).
  - Pembetulan: Sesuai kaidah IEEE, judul artikel wajib menggunakan sentence-case (hanya huruf pertama kalimat dan nama diri/akronim yang kapital). Tidak ada kata benda khusus/akronim dalam judul ini ("steel" adalah kata benda umum).
  - Teks setelah perbaikan: `"Coupling of solidification and heat transfer simulations with interpretable machine learning algorithms to predict transverse cracks in continuous casting of steel,"`
- **Audit Nama Jurnal**:
  - Sumber: `steel research international`
  - Format IEEE: `*Steel Research International*` (cetak miring, Title Case, sesuai).
- **Audit Volume, Isu, Halaman / Nomor Artikel, Tahun, & DOI**:
  - Volume: `vol. 95`
  - Isu: `no. 4`
  - Nomor artikel: `Art. no. 2300529` (pengidentifikasi artikel Wiley, bukan halaman biasa).
  - Tahun: `2024`
  - DOI: `doi: 10.1002/srin.202300529` (format `doi: 10.xxxx/...` tanpa prefiks `https://doi.org/`).
- **Audit Karakter Terlarang & Anchor**:
  - Tidak ditemukan em dash (`—`), seluruh tanda pemisah menggunakan tanda hubung biasa (`-`).
  - Tidak mengandung kata terlarang (`kendati`, `paradigma`, `guna`).
  - Tag anchor `<a id="ref36"></a>` terpasang sebelum entri.

---

### [37] Molstad & Motwani (2023)
- **Berkas Sumber**: `paper/references/2023_Multiresolution Categorical Regression for Interpretable Cell-Type Annotation.bibtex`
- **Audit Penulis**:
  - Penulis pada sumber: Aaron J. Molstad dan Keshav Motwani (total 2 penulis).
  - Evaluasi aturan: Jumlah penulis $\le 6$, ditulis lengkap.
  - Format IEEE: `A. J. Molstad and K. Motwani` (sesuai).
- **Audit Judul Artikel**:
  - Teks awal: `"Multiresolution Categorical Regression for Interpretable Cell-Type Annotation,"`
  - Temuan audit: Judul awal masih menggunakan Title Case kapitalisasi penuh pada setiap kata.
  - Pembetulan: Diubah menjadi sentence-case. Istilah "cell-type" ditulis dalam huruf kecil biasa dengan tanda hubung biasa.
  - Teks setelah perbaikan: `"Multiresolution categorical regression for interpretable cell-type annotation,"`
- **Audit Nama Jurnal**:
  - Sumber: `Biometrics`
  - Format IEEE: `*Biometrics*` (cetak miring, sesuai).
- **Audit Volume, Isu, Rentang Halaman, Tahun, & DOI**:
  - Volume: `vol. 79`
  - Isu: `no. 4`
  - Halaman: `pp. 3485-3496` (menggunakan tanda hubung biasa `-`).
  - Tahun: `2023`
  - DOI: `doi: 10.1111/biom.13926` (sesuai).
- **Audit Karakter Terlarang & Anchor**:
  - Bebas dari karakter em dash (`—`).
  - Bebas dari kata terlarang (`kendati`, `paradigma`, `guna`).
  - Tag anchor `<a id="ref37"></a>` terpasang sebelum entri.

---

### [38] Zhang, Wang, & Xiu (2022)
- **Berkas Sumber**: `paper/references/2022_Multinomial logistic regression classifier via 𝑙𝑞,0-proximal Newton algorithm.bib`
- **Audit Penulis**:
  - Penulis pada sumber: Penghe Zhang, Rui Wang, Naihua Xiu (total 3 penulis).
  - Evaluasi aturan: Jumlah penulis $\le 6$, seluruh penulis dicantumkan.
  - Format IEEE: `P. Zhang, R. Wang, and N. Xiu` (sesuai).
- **Audit Judul Artikel**:
  - Teks: `"Multinomial logistic regression classifier via lq,0-proximal Newton algorithm,"`
  - Temuan audit: Judul telah berformat sentence-case yang tepat. Kata "Newton" tetap ditulis kapital karena merupakan nama diri/eponim ilmiah (Sir Isaac Newton). Parameter indeks "lq,0-proximal" menggunakan tanda hubung biasa.
- **Audit Nama Jurnal**:
  - Sumber: `Neurocomputing`
  - Format IEEE: `*Neurocomputing*` (cetak miring, sesuai).
- **Audit Volume, Isu, Rentang Halaman, Tahun, & DOI**:
  - Volume: `vol. 468` (tidak memiliki nomor isu).
  - Halaman: `pp. 148-164` (menggunakan tanda hubung biasa `-`).
  - Tahun: `2022`
  - DOI: `doi: 10.1016/j.neucom.2021.10.005` (sesuai, tanpa `https://doi.org/`).
- **Audit Karakter Terlarang & Anchor**:
  - Bebas dari em dash (`—`).
  - Bebas dari kata terlarang (`kendati`, `paradigma`, `guna`).
  - Tag anchor `<a id="ref38"></a>` terpasang sebelum entri.

---

### [39] Zhang, Wei, & Liu (2022)
- **Berkas Sumber**: `paper/references/2022_Group Logistic Regression Models with lp,q Regularization.bib`
- **Audit Penulis**:
  - Penulis pada sumber: Yanfang Zhang, Chuanhua Wei, Xiaolin Liu (total 3 penulis).
  - Evaluasi aturan: Jumlah penulis $\le 6$, seluruh penulis dicantumkan.
  - Format IEEE: `Y. Zhang, C. Wei, and X. Liu` (sesuai).
- **Audit Judul Artikel**:
  - Teks awal: `"Group Logistic Regression Models with lp,q Regularization,"`
  - Temuan audit: Kata-kata "Logistic", "Regression", "Models", dan "Regularization" sebelumnya dikapitalisasi (Title Case).
  - Pembetulan: Disesuaikan ke format sentence-case. Hanya kata pertama "Group" yang kapital. Notasi parameter "lp,q" dipertahankan.
  - Teks setelah perbaikan: `"Group logistic regression models with lp,q regularization,"`
- **Audit Nama Jurnal**:
  - Sumber: `Mathematics`
  - Format IEEE: `*Mathematics*` (cetak miring, sesuai).
- **Audit Volume, Isu, Nomor Artikel, Tahun, & DOI**:
  - Volume: `vol. 10`
  - Isu: `no. 13`
  - Nomor artikel: `Art. no. 2227` (artikel MDPI menggunakan article number).
  - Tahun: `2022`
  - DOI: `doi: 10.3390/math10132227` (sesuai).
- **Audit Karakter Terlarang & Anchor**:
  - Bebas dari em dash (`—`).
  - Bebas dari kata terlarang (`kendati`, `paradigma`, `guna`).
  - Tag anchor `<a id="ref39"></a>` terpasang sebelum entri.

---

### [40] Lai et al. (2023)
- **Berkas Sumber**: `paper/references/2023_Maximal Margin Support Vector Machine for Feature Representation and Classification.bib`
- **Audit Penulis**:
  - Penulis pada sumber: Zhihui Lai, Xi Chen, Junhong Zhang, Heng Kong, Jiajun Wen (total 5 penulis).
  - Evaluasi aturan: Jumlah penulis $\le 6$, seluruh penulis dicantumkan.
  - Format IEEE: `Z. Lai, X. Chen, J. Zhang, H. Kong, and J. Wen` (sesuai).
- **Audit Judul Artikel**:
  - Teks awal: `"Maximal Margin Support Vector Machine for Feature Representation and Classification,"`
  - Temuan audit: Seluruh kata konten menggunakan huruf kapital awal (Title Case).
  - Pembetulan: Sesuai standar penulisan IEEE, nama algoritma/metode umum seperti "support vector machine" bukan merupakan nama diri dan ditulis dengan huruf kecil pada format sentence-case.
  - Teks setelah perbaikan: `"Maximal margin support vector machine for feature representation and classification,"`
- **Audit Nama Jurnal**:
  - Sumber: `IEEE Transactions on Cybernetics`
  - Format IEEE: `*IEEE Transactions on Cybernetics*` (cetak miring, Title Case, sesuai).
- **Audit Volume, Isu, Rentang Halaman, Tahun, & DOI**:
  - Volume: `vol. 53`
  - Isu: `no. 10`
  - Halaman: `pp. 6700-6713` (menggunakan tanda hubung biasa `-`).
  - Tahun: `2023`
  - DOI: `doi: 10.1109/TCYB.2022.3232800` (sesuai).
- **Audit Karakter Terlarang & Anchor**:
  - Bebas dari em dash (`—`).
  - Bebas dari kata terlarang (`kendati`, `paradigma`, `guna`).
  - Tag anchor `<a id="ref40"></a>` terpasang sebelum entri.

---

## 2. Teks Final Entri Referensi [36] - [40]

Berikut adalah teks entri final yang telah diaudit, diverifikasi terhadap berkas sumber BibTeX, dan disinkronkan ke dalam `paper/06_references.md`:

```markdown
<a id="ref36"></a>
[36] J. Norrena, S. Louhenkilpi, V.-V. Visuri, T. Alatarvas, A. Bogdanoff, and T. Fabritius, "Coupling of solidification and heat transfer simulations with interpretable machine learning algorithms to predict transverse cracks in continuous casting of steel," *Steel Research International*, vol. 95, no. 4, Art. no. 2300529, 2024, doi: 10.1002/srin.202300529.

<a id="ref37"></a>
[37] A. J. Molstad and K. Motwani, "Multiresolution categorical regression for interpretable cell-type annotation," *Biometrics*, vol. 79, no. 4, pp. 3485-3496, 2023, doi: 10.1111/biom.13926.

<a id="ref38"></a>
[38] P. Zhang, R. Wang, and N. Xiu, "Multinomial logistic regression classifier via lq,0-proximal Newton algorithm," *Neurocomputing*, vol. 468, pp. 148-164, 2022, doi: 10.1016/j.neucom.2021.10.005.

<a id="ref39"></a>
[39] Y. Zhang, C. Wei, and X. Liu, "Group logistic regression models with lp,q regularization," *Mathematics*, vol. 10, no. 13, Art. no. 2227, 2022, doi: 10.3390/math10132227.

<a id="ref40"></a>
[40] Z. Lai, X. Chen, J. Zhang, H. Kong, and J. Wen, "Maximal margin support vector machine for feature representation and classification," *IEEE Transactions on Cybernetics*, vol. 53, no. 10, pp. 6700-6713, 2023, doi: 10.1109/TCYB.2022.3232800.
```
