# Audit dan Perbaikan Referensi [16] - [20]

Dokumen ini memuat hasil audit mendalam dan perbaikan untuk entri referensi nomor [16] sampai [20] pada berkas `paper/06_references.md`, berdasarkan berkas sumber BibTeX di `paper/references/` dan pedoman IEEE di `rules/IEEE_citation_guidelines.md`.

---

## 1. Ringkasan Hasil Audit

| No. Ref | Penulis (<= 6 ditulis semua) | Judul (Sentence-case & Kutip Ganda) | Sumber Publikasi | Volume, Nomor, Halaman/Art. no. | Tahun & DOI | Status & Temuan Utama |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **[16]** | 5 penulis (Sesuai) | Sudah sentence-case | *Journal of Visual Communication and Image Representation* | vol. 90, Art. no. 103745 | 2023, doi: 10.1016/j.jvcir.2022.103745 | **Valid** (format sudah tepat dan konsisten). |
| **[17]** | 4 penulis (Sesuai) | Sebelumnya Title Case -> Diperbaiki ke sentence-case | *International Journal on Informatics Visualization* | vol. 8, no. 1, pp. 18-25 | 2024, doi: 10.62527/joiv.8.1.1923 | **Perbaikan Judul** (huruf kapital non-awal/non-akronim diubah ke huruf kecil). |
| **[18]** | 2 penulis (Sesuai) | Sebelumnya Title Case -> Diperbaiki ke sentence-case | *International Journal of Advanced Computer Science and Applications* | vol. 15, no. 2, pp. 217-226 | 2024, doi: 10.14569/IJACSA.2024.0150223 | **Perbaikan Judul** (huruf kapital non-awal diubah ke huruf kecil; rentang halaman pp. 217-226 terverifikasi). |
| **[19]** | 5 penulis (Sesuai) | Sebelumnya Title Case -> Diperbaiki ke sentence-case | *Proc. 2025 8th Int. Conf. Vocational Educ. Elect. Eng. (ICVEE)* | pp. 258-264 | Surabaya, Indonesia, 2025, doi: 10.1109/ICVEE66651.2025.11281432 | **Perbaikan Judul & Lokasi Konferensi** (sentence-case serta penambahan lokasi Surabaya, Indonesia sesuai standar prosiding IEEE). |
| **[20]** | 3 penulis (Sesuai) | Sebelumnya Title Case -> Diperbaiki ke sentence-case (akronim MD-ViT tetap kapital) | *Journal of Information Engineering and Educational Technology* | vol. 9, no. 2, pp. 64-79 | Dec. 2025, doi: 10.26740/jieet.v9n2.p64-79 | **Perbaikan Judul** (sentence-case dengan menjaga akronim MD-ViT). |

---

## 2. Rincian Audit Tiap Referensi

### Referensi [16]
- **Berkas Sumber**: `paper/references/2023_Learning an attention-aware parallel sharing network for facial attribute recognition.bib`
- **Metadata Sumber**:
  - Penulis: Si Chen, Xinyu Lai, Yan Yan, Da-Han Wang, Shunzhi Zhu (5 orang).
  - Judul: "Learning an attention-aware parallel sharing network for facial attribute recognition"
  - Jurnal: *Journal of Visual Communication and Image Representation*
  - Volume/Pages: vol. 90, pages 103745
  - Tahun: 2023
  - DOI: 10.1016/j.jvcir.2022.103745
- **Evaluasi Kepatuhan**:
  - Penulis (5 orang <= 6): ditulis lengkap dengan inisial dan nama keluarga `S. Chen, X. Lai, Y. Yan, D.-H. Wang, and S. Zhu`. Pemakaian tanda hubung pada inisial `D.-H.` sudah tepat.
  - Judul: sudah sentence-case dan berada di dalam tanda kutip ganda.
  - Nama Jurnal: dicetak miring dengan tanda bintang markdown (`*Journal of Visual Communication and Image Representation*`).
  - Penomoran: artikel tanpa nomor halaman konvensional menggunakan format `Art. no. 103745`.
  - DOI: format `doi: 10.1016/j.jvcir.2022.103745.` tanpa awalan URL.
  - Karakter terlarang: tidak ditemukan em dash maupun kata terlarang.
- **Teks Final**:
```markdown
<a id="ref16"></a>
[16] S. Chen, X. Lai, Y. Yan, D.-H. Wang, and S. Zhu, "Learning an attention-aware parallel sharing network for facial attribute recognition," *Journal of Visual Communication and Image Representation*, vol. 90, Art. no. 103745, 2023, doi: 10.1016/j.jvcir.2022.103745.
```

---

### Referensi [17]
- **Berkas Sumber**: `paper/references/2024_Classifying Gender Based on Face Images Using Vision Transformer.bib`
- **Metadata Sumber**:
  - Penulis: Ganjar Gingin Tahyudin, Mahmud Dwi Sulistiyo, Muhammad Arzaki, Ema Rachmawati (4 orang).
  - Judul: "Classifying Gender Based on Face Images Using Vision Transformer"
  - Jurnal: *International Journal on Informatics Visualization*
  - Volume/Nomor/Pages: vol. 8, no. 1, pp. 18-25
  - Tahun: 2024
  - DOI: 10.62527/joiv.8.1.1923
- **Evaluasi Kepatuhan & Perbaikan**:
  - Penulis (4 orang <= 6): ditulis lengkap dengan inisial dan nama keluarga `G. G. Tahyudin, M. D. Sulistiyo, M. Arzaki, and E. Rachmawati`.
  - Judul artikel: sebelumnya tertulis dalam bentuk Title Case `"Classifying Gender Based on Face Images Using Vision Transformer,"`. Berdasarkan pedoman IEEE dan instruksi, judul artikel jurnal wajib berupa sentence-case (hanya huruf pertama kalimat kapital, sisanya huruf kecil kecuali kata benda khusus dan akronim). Kata "gender", "based", "on", "face", "images", "using", dan "vision transformer" diubah ke huruf kecil.
  - Nama Jurnal: dicetak miring dengan tanda bintang markdown (`*International Journal on Informatics Visualization*`).
  - Volume, issue, halaman: `vol. 8, no. 1, pp. 18-25`. Tanda hubung biasa tanpa spasi.
  - DOI: format `doi: 10.62527/joiv.8.1.1923.` tanpa awalan URL.
  - Karakter terlarang: bebas dari em dash dan kata terlarang.
- **Teks Final**:
```markdown
<a id="ref17"></a>
[17] G. G. Tahyudin, M. D. Sulistiyo, M. Arzaki, and E. Rachmawati, "Classifying gender based on face images using vision transformer," *International Journal on Informatics Visualization*, vol. 8, no. 1, pp. 18-25, 2024, doi: 10.62527/joiv.8.1.1923.
```

---

### Referensi [18]
- **Berkas Sumber**: `paper/references/2024_Ethnicity Classification Based on Facial Images using Deep Learning Approach.bib`
- **Metadata Sumber**:
  - Penulis: Abdul-aziz Kalkatawi, Usman Saeed (2 orang).
  - Judul: "Ethnicity Classification Based on Facial Images using Deep Learning Approach"
  - Jurnal: *International Journal of Advanced Computer Science and Applications*
  - Volume/Nomor/Pages: vol. 15, no. 2, pp. 217-226
  - Tahun: 2024
  - DOI: 10.14569/IJACSA.2024.0150223
- **Evaluasi Kepatuhan & Perbaikan**:
  - Penulis (2 orang <= 6): ditulis lengkap. Inisial untuk Abdul-aziz adalah `A.-A.` (sesuai kaidah penyingkatan nama ganda dengan tanda hubung IEEE). Format: `A.-A. Kalkatawi and U. Saeed`.
  - Judul artikel: sebelumnya tertulis dalam Title Case `"Ethnicity Classification Based on Facial Images using Deep Learning Approach,"`. Diperbaiki menjadi sentence-case: `"Ethnicity classification based on facial images using deep learning approach,"`.
  - Halaman: rentang halaman `pp. 217-226` diverifikasi langsung pada berkas penerbit resmi The Science and Information Organization (IJACSA) Vol. 15, No. 2, Paper 23.
  - DOI: format `doi: 10.14569/IJACSA.2024.0150223.` tanpa awalan URL.
  - Karakter terlarang: bebas dari em dash dan kata terlarang.
- **Teks Final**:
```markdown
<a id="ref18"></a>
[18] A.-A. Kalkatawi and U. Saeed, "Ethnicity classification based on facial images using deep learning approach," *International Journal of Advanced Computer Science and Applications*, vol. 15, no. 2, pp. 217-226, 2024, doi: 10.14569/IJACSA.2024.0150223.
```

---

### Referensi [19]
- **Berkas Sumber**: `paper/references/2025_Dual Vision Transformer Integration for Race and Gender Recognition Based on Facial Images.bib`
- **Metadata Sumber**:
  - Penulis: Rezky Arisanti Putri, Lilik Anifah, Ricky Eka Putra, Yuni Yamasari, Rafy Aulia Akbar (5 orang).
  - Judul: "Dual Vision Transformer Integration for Race and Gender Recognition Based on Facial Images"
  - Prosiding: 2025 Eight International Conference on Vocational Education and Electrical Engineering (ICVEE)
  - Lokasi Acara: Surabaya, Indonesia
  - Waktu: 24-25 September 2025
  - Halaman: pp. 258-264
  - DOI: 10.1109/ICVEE66651.2025.11281432
- **Evaluasi Kepatuhan & Perbaikan**:
  - Penulis (5 orang <= 6): ditulis seluruhnya dengan inisial dan nama keluarga `R. A. Putri, L. Anifah, R. E. Putra, Y. Yamasari, and R. A. Akbar`.
  - Judul artikel: sebelumnya tertulis dalam Title Case `"Dual Vision Transformer Integration for Race and Gender Recognition Based on Facial Images,"`. Diperbaiki menjadi sentence-case `"Dual vision transformer integration for race and gender recognition based on facial images,"`.
  - Format Prosiding Konferensi IEEE: pedoman IEEE untuk paper konferensi (`rules/IEEE_citation_guidelines.md` baris 170-172) menetapkan format `in Proc. <Conference Name>, <City>, <Country>, year, pp. xx-yy.`. Nama singkatan standar prosiding adalah `*Proc. 2025 8th Int. Conf. Vocational Educ. Elect. Eng. (ICVEE)*`. Lokasi konferensi `Surabaya, Indonesia` ditambahkan untuk melengkapi kepatuhan format prosiding IEEE sebagaimana entri referensi konferensi lainnya ([14] dan [25]).
  - Halaman: `pp. 258-264` dengan tanda hubung standar.
  - DOI: format `doi: 10.1109/ICVEE66651.2025.11281432.` tanpa awalan URL.
  - Karakter terlarang: bebas dari em dash dan kata terlarang.
- **Teks Final**:
```markdown
<a id="ref19"></a>
[19] R. A. Putri, L. Anifah, R. E. Putra, Y. Yamasari, and R. A. Akbar, "Dual vision transformer integration for race and gender recognition based on facial images," in *Proc. 2025 8th Int. Conf. Vocational Educ. Elect. Eng. (ICVEE)*, Surabaya, Indonesia, 2025, pp. 258-264, doi: 10.1109/ICVEE66651.2025.11281432.
```

---

### Referensi [20]
- **Berkas Sumber**: `paper/references/2025_MD-ViT Multidomain Vision Transformer Fusion for Fair Demographic Attribute Recognition.bib`
- **Metadata Sumber**:
  - Penulis: Rezky Arisanti Putri, Ricky Eka Putra, Yuni Yamasari (3 orang).
  - Judul: "MD-ViT: Multidomain Vision Transformer Fusion for Fair Demographic Attribute Recognition"
  - Jurnal: *Journal of Information Engineering and Educational Technology*
  - Volume/Issue/Pages: vol. 9, issue 2, pp. 64-79
  - Bulan/Tahun: 12 (Dec.) 2025
  - DOI: 10.26740/jieet.v9n2.p64-79
- **Evaluasi Kepatuhan & Perbaikan**:
  - Penulis (3 orang <= 6): ditulis lengkap dengan inisial dan nama keluarga `R. A. Putri, R. E. Putra, and Y. Yamasari`.
  - Judul artikel: sebelumnya tertulis dalam Title Case `"MD-ViT: Multidomain Vision Transformer Fusion for Fair Demographic Attribute Recognition,"`. Akronim "MD-ViT" dipertahankan dalam huruf kapital karena merupakan akronim model yang diusulkan. Kata-kata setelah tanda titik dua diubah menjadi sentence-case huruf kecil `"MD-ViT: multidomain vision transformer fusion for fair demographic attribute recognition,"` selaras dengan gaya penulisan subjudul pada referensi [1], [4], dan [23].
  - Nama Jurnal: dicetak miring dengan tanda bintang markdown (`*Journal of Information Engineering and Educational Technology*`).
  - Volume, issue, halaman: `vol. 9, no. 2, pp. 64-79`.
  - Bulan dan Tahun: `Dec. 2025` sesuai format bulan IEEE dan metadata berkas sumber.
  - DOI: format `doi: 10.26740/jieet.v9n2.p64-79.` tanpa awalan URL.
  - Karakter terlarang: bebas dari em dash dan kata terlarang.
- **Teks Final**:
```markdown
<a id="ref20"></a>
[20] R. A. Putri, R. E. Putra, and Y. Yamasari, "MD-ViT: multidomain vision transformer fusion for fair demographic attribute recognition," *Journal of Information Engineering and Educational Technology*, vol. 9, no. 2, pp. 64-79, Dec. 2025, doi: 10.26740/jieet.v9n2.p64-79.
```

---

## 3. Entri Final Bersih [16] sampai [20] untuk `paper/06_references.md`

Berikut adalah blok entri final yang telah disesuaikan secara utuh:

```markdown
<a id="ref16"></a>
[16] S. Chen, X. Lai, Y. Yan, D.-H. Wang, and S. Zhu, "Learning an attention-aware parallel sharing network for facial attribute recognition," *Journal of Visual Communication and Image Representation*, vol. 90, Art. no. 103745, 2023, doi: 10.1016/j.jvcir.2022.103745.

<a id="ref17"></a>
[17] G. G. Tahyudin, M. D. Sulistiyo, M. Arzaki, and E. Rachmawati, "Classifying gender based on face images using vision transformer," *International Journal on Informatics Visualization*, vol. 8, no. 1, pp. 18-25, 2024, doi: 10.62527/joiv.8.1.1923.

<a id="ref18"></a>
[18] A.-A. Kalkatawi and U. Saeed, "Ethnicity classification based on facial images using deep learning approach," *International Journal of Advanced Computer Science and Applications*, vol. 15, no. 2, pp. 217-226, 2024, doi: 10.14569/IJACSA.2024.0150223.

<a id="ref19"></a>
[19] R. A. Putri, L. Anifah, R. E. Putra, Y. Yamasari, and R. A. Akbar, "Dual vision transformer integration for race and gender recognition based on facial images," in *Proc. 2025 8th Int. Conf. Vocational Educ. Elect. Eng. (ICVEE)*, Surabaya, Indonesia, 2025, pp. 258-264, doi: 10.1109/ICVEE66651.2025.11281432.

<a id="ref20"></a>
[20] R. A. Putri, R. E. Putra, and Y. Yamasari, "MD-ViT: multidomain vision transformer fusion for fair demographic attribute recognition," *Journal of Information Engineering and Educational Technology*, vol. 9, no. 2, pp. 64-79, Dec. 2025, doi: 10.26740/jieet.v9n2.p64-79.
```
