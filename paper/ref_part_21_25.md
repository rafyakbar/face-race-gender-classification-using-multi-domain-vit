# Laporan Audit dan Perbaikan Referensi [21] - [25]

Dokumen ini memuat hasil audit mendalam serta perbaikan referensi [21] sampai [25] pada berkas `paper/06_references.md` berdasarkan pedoman sitasi IEEE (`rules/IEEE_citation_guidelines.md`) dan berkas sumber primer pada direktori `paper/references/`.

---

## 1. Rekapitulasi Entri Final Referensi [21] - [25]

Berikut adalah teks perbaikan final yang telah disesuaikan dan disimpan pada `paper/06_references.md`:

<a id="ref21"></a>
[21] S. K. Gupta and N. Nain, "Review: single attribute and multi attribute facial gender and age estimation," *Multimedia Tools and Applications*, vol. 82, no. 1, pp. 1289-1311, 2023, doi: 10.1007/s11042-022-12678-6.

<a id="ref22"></a>
[22] Y. Deng, S. Teng, L. Fei, W. Zhang, and I. Rida, "A multifeature learning and fusion network for facial age estimation," *Sensors*, vol. 21, no. 13, Art. no. 4597, 2021, doi: 10.3390/s21134597.

<a id="ref23"></a>
[23] Z. Wang, L. Xiao, Z. Cao, and H. Lu, "Vision transformer off-the-shelf: a surprising baseline for few-shot class-agnostic counting," in *Proc. AAAI Conf. Artif. Intell. (AAAI)*, 2024, Art. no. 648, doi: 10.1609/aaai.v38i6.28396.

<a id="ref24"></a>
[24] D. Wilimitis and C. G. Walsh, "Practical considerations and applied examples of cross-validation for model development and evaluation in health care: tutorial," *JMIR AI*, vol. 2, Art. no. e49023, 2023, doi: 10.2196/49023.

<a id="ref25"></a>
[25] I. Hupont and C. Fernández, "DemogPairs: quantifying the impact of demographic imbalance in deep face recognition," in *Proc. 2019 14th IEEE Int. Conf. Autom. Face Gesture Recognit. (FG)*, Lille, France, 2019, pp. 1-7, doi: 10.1109/FG.2019.8756625.

---

## 2. Rincian Temuan Audit per Referensi

### Referensi [21]
- **Berkas Sumber**: `paper/references/2022_Review Single attribute and multi attribute facial gender and age estimation.nbib`
- **Teks Awal**:
  `<a id="ref21"></a>`
  `[21] S. K. Gupta and N. Nain, "Review: Single attribute and multi attribute facial gender and age estimation," *Multimedia Tools and Applications*, vol. 82, no. 1, pp. 1289-1311, 2023, doi: 10.1007/s11042-022-12678-6.`
- **Pencocokan Metadata**:
  - **Penulis**: 2 orang (Sandeep Kumar Gupta, Neeta Nain). Sesuai aturan IEEE (<= 6 penulis), seluruh nama dicantumkan dalam format inisial dan nama keluarga: `S. K. Gupta and N. Nain`. (Sesuai)
  - **Judul Artikel**: Berkas sumber memuat judul `Review: Single attribute and multi attribute facial gender and age estimation.`. Pada teks awal, kata `Single` setelah tanda titik dua ditulis dengan huruf kapital. Berdasarkan kaidah sentence-case IEEE (hanya huruf pertama judul, kata benda khusus, dan akronim yang dikapitalisasi), kata `single` bukan kata benda khusus atau akronim, sehingga harus ditulis dengan huruf kecil `single`.
  - **Nama Jurnal**: `*Multimedia Tools and Applications*` dicetak miring dengan tanda bintang markdown. (Sesuai)
  - **Volume, Nomor, Halaman**: `vol. 82, no. 1, pp. 1289-1311` memakai tanda hubung standar `-`. (Sesuai)
  - **Tahun & DOI**: Terbit cetak tahun 2023 (`DP - 2023`), format DOI `doi: 10.1007/s11042-022-12678-6` tanpa awalan URL. (Sesuai)
  - **Anchor**: `<a id="ref21"></a>`. (Sesuai)
- **Teks Perbaikan Final**:
  `<a id="ref21"></a>`
  `[21] S. K. Gupta and N. Nain, "Review: single attribute and multi attribute facial gender and age estimation," *Multimedia Tools and Applications*, vol. 82, no. 1, pp. 1289-1311, 2023, doi: 10.1007/s11042-022-12678-6.`

---

### Referensi [22]
- **Berkas Sumber**: `paper/references/2021_A Multifeature Learning and Fusion Network for Facial Age Estimation.bib`
- **Teks Awal**:
  `<a id="ref22"></a>`
  `[22] Y. Deng, S. Teng, L. Fei, W. Zhang, and I. Rida, "A Multifeature Learning and Fusion Network for Facial Age Estimation," *Sensors*, vol. 21, no. 13, Art. no. 4597, 2021, doi: 10.3390/s21134597.`
- **Pencocokan Metadata**:
  - **Penulis**: 5 orang (Yulan Deng, Shaohua Teng, Lunke Fei, Wei Zhang, Imad Rida). Karena <= 6 penulis, seluruh penulis dicantumkan: `Y. Deng, S. Teng, L. Fei, W. Zhang, and I. Rida`. (Sesuai)
  - **Judul Artikel**: Pada berkas sumber tertulis dalam Title Case `A Multifeature Learning and Fusion Network for Facial Age Estimation`. Teks awal belum diubah ke sentence-case. Berdasarkan pedoman IEEE, judul artikel wajib diubah ke sentence-case menjadi `"A multifeature learning and fusion network for facial age estimation,"`.
  - **Nama Jurnal**: `*Sensors*` dicetak miring dengan tanda bintang markdown. (Sesuai)
  - **Volume, Nomor, Nomor Artikel**: `vol. 21, no. 13, Art. no. 4597`. (Sesuai)
  - **Tahun & DOI**: Tahun 2021, DOI `doi: 10.3390/s21134597`. (Sesuai)
  - **Anchor**: `<a id="ref22"></a>`. (Sesuai)
- **Teks Perbaikan Final**:
  `<a id="ref22"></a>`
  `[22] Y. Deng, S. Teng, L. Fei, W. Zhang, and I. Rida, "A multifeature learning and fusion network for facial age estimation," *Sensors*, vol. 21, no. 13, Art. no. 4597, 2021, doi: 10.3390/s21134597.`

---

### Referensi [23]
- **Berkas Sumber**: `paper/references/2024_Vision Transformer Off-the-Shelf A Surprising Baseline for Few-Shot Class-Agnostic Counting.bib`
- **Teks Awal**:
  `<a id="ref23"></a>`
  `[23] Z. Wang, L. Xiao, Z. Cao, and H. Lu, "Vision transformer off-the-shelf: a surprising baseline for few-shot class-agnostic counting," in *Proc. AAAI Conf. Artif. Intell. (AAAI)*, 2024, Art. no. 648, doi: 10.1609/aaai.v38i6.28396.`
- **Pencocokan Metadata**:
  - **Penulis**: 4 orang (Zhicheng Wang, Liwen Xiao, Zhiguo Cao, Hao Lu). Seluruh nama ditulis lengkap (<= 6): `Z. Wang, L. Xiao, Z. Cao, and H. Lu`. (Sesuai)
  - **Judul Artikel**: Berkas sumber mencatat `Vision transformer off-the-shelf: a surprising baseline for few-shot class-agnostic counting`. Teks sudah berada dalam sentence-case yang tepat. (Sesuai)
  - **Nama Konferensi**: Prosiding AAAI disingkat sesuai konvensi IEEE menjadi `in *Proc. AAAI Conf. Artif. Intell. (AAAI)*`. (Sesuai)
  - **Penomoran Artikel / Halaman**: Pada berkas sumber `.bib`, entri mencantumkan `articleno = {648}` tanpa nomor halaman, sehingga representasi `2024, Art. no. 648` tepat dan selaras dengan berkas sumber lokal. Pada indeks publikasi resmi AAAI, artikel ini termuat pada `vol. 38, no. 6, pp. 5832-5840`. Format `Art. no. 648` dipertahankan karena selaras langsung dengan metadata berkas sumber lokal. (Sesuai)
  - **Tahun & DOI**: Tahun 2024, DOI `doi: 10.1609/aaai.v38i6.28396`. (Sesuai)
  - **Anchor**: `<a id="ref23"></a>`. (Sesuai)
- **Teks Perbaikan Final**:
  `<a id="ref23"></a>`
  `[23] Z. Wang, L. Xiao, Z. Cao, and H. Lu, "Vision transformer off-the-shelf: a surprising baseline for few-shot class-agnostic counting," in *Proc. AAAI Conf. Artif. Intell. (AAAI)*, 2024, Art. no. 648, doi: 10.1609/aaai.v38i6.28396.`
  *(Catatan alternatif lengkap: jika diinginkan bentuk prosiding berkala dengan nomor halaman resmi: `in *Proc. AAAI Conf. Artif. Intell. (AAAI)*, vol. 38, no. 6, pp. 5832-5840, 2024, doi: 10.1609/aaai.v38i6.28396.`)*

---

### Referensi [24]
- **Berkas Sumber**: `paper/references/2023_Practical Considerations and Applied Examples of Cross-Validation for Model Development and Evaluation in Health Care Tutorial.bib`
- **Teks Awal**:
  `<a id="ref24"></a>`
  `[24] D. Wilimitis and C. G. Walsh, "Practical considerations and applied examples of cross-validation for model development and evaluation in health care: Tutorial," *JMIR AI*, vol. 2, 2023, doi: 10.2196/49023.`
- **Pencocokan Metadata**:
  - **Penulis**: 2 orang (Drew Wilimitis, Colin G Walsh). Ditulis inisial dan nama keluarga: `D. Wilimitis and C. G. Walsh`. (Sesuai)
  - **Judul Artikel**: Berkas sumber menulis `Practical Considerations and Applied Examples of Cross-Validation for Model Development and Evaluation in Health Care: Tutorial`. Kata `Tutorial` setelah tanda titik dua pada teks awal berhuruf kapital. Berdasarkan kaidah sentence-case, kata `tutorial` bukan nama diri atau akronim, sehingga wajib diubah menjadi huruf kecil `tutorial`.
  - **Nama Jurnal**: `*JMIR AI*` dicetak miring dengan tanda bintang markdown. (Sesuai)
  - **Volume & Nomor Artikel**: Pada teks awal hanya tertulis `vol. 2, 2023`, tanpa nomor artikel. Pada publikasi daring JMIR AI, artikel ini memiliki nomor artikel unik `e49023`. Berdasarkan aturan IEEE untuk jurnal elektronik tanpa rentang halaman fisik, nomor artikel dicantumkan sebagai `Art. no. e49023`.
  - **Tahun & DOI**: Tahun 2023, DOI `doi: 10.2196/49023`. (Sesuai)
  - **Anchor**: `<a id="ref24"></a>`. (Sesuai)
- **Teks Perbaikan Final**:
  `<a id="ref24"></a>`
  `[24] D. Wilimitis and C. G. Walsh, "Practical considerations and applied examples of cross-validation for model development and evaluation in health care: tutorial," *JMIR AI*, vol. 2, Art. no. e49023, 2023, doi: 10.2196/49023.`

---

### Referensi [25]
- **Berkas Sumber**: `paper/references/2019_DemogPairs Quantifying the Impact of Demographic Imbalance in Deep Face Recognition.bib`
- **Teks Awal**:
  `<a id="ref25"></a>`
  `[25] I. Hupont and C. Fernández, "DemogPairs: Quantifying the Impact of Demographic Imbalance in Deep Face Recognition," in *Proc. 2019 14th IEEE Int. Conf. Autom. Face Gesture Recognit. (FG)*, Lille, France, 2019, pp. 1-7, doi: 10.1109/FG.2019.8756625.`
- **Pencocokan Metadata**:
  - **Penulis**: 2 orang (Isabelle Hupont, Carles Fernández). Sesuai aturan IEEE (<= 6 penulis): `I. Hupont and C. Fernández`. (Sesuai)
  - **Judul Artikel**: Teks awal masih berformat Title Case (`"DemogPairs: Quantifying the Impact of Demographic Imbalance in Deep Face Recognition"`). `DemogPairs` merupakan nama diri (nama himpunan data yang diperkenalkan dalam artikel), sehingga huruf kapitalnya tetap dipertahankan. Seluruh kata lainnya (`quantifying`, `the`, `impact`, `of`, `demographic`, `imbalance`, `in`, `deep`, `face`, `recognition`) diubah ke huruf kecil sesuai kaidah sentence-case IEEE.
  - **Nama Konferensi**: Ditulis `in *Proc. 2019 14th IEEE Int. Conf. Autom. Face Gesture Recognit. (FG)*`, lengkap dengan lokasi `Lille, France`. (Sesuai)
  - **Halaman & Tahun**: `2019, pp. 1-7` memakai tanda hubung standar `-`. (Sesuai)
  - **DOI**: `doi: 10.1109/FG.2019.8756625`. (Sesuai)
  - **Anchor**: `<a id="ref25"></a>`. (Sesuai)
- **Teks Perbaikan Final**:
  `<a id="ref25"></a>`
  `[25] I. Hupont and C. Fernández, "DemogPairs: quantifying the impact of demographic imbalance in deep face recognition," in *Proc. 2019 14th IEEE Int. Conf. Autom. Face Gesture Recognit. (FG)*, Lille, France, 2019, pp. 1-7, doi: 10.1109/FG.2019.8756625.`

---

## 3. Matriks Verifikasi Kepatuhan Aturan dan Karakter

| Nomor Referensi | Format Penulis (<= 6) | Sentence-Case Judul | Cetak Miring Publikasi | Format Vol/No/Hal/Art | Format Tahun & DOI | Format Anchor HTML | Bebas Karakter/Kata Terlarang |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **[21]** | Sesuai (2 penulis) | Sesuai (`single` kecil) | Sesuai (*Multimed.*) | Sesuai (`vol. 82, no. 1, pp. 1289-1311`) | Sesuai (`2023`, `doi: 10.1007/...`) | Sesuai (`<a id="ref21"></a>`) | Sesuai (tanda hubung `-`, tanpa em dash) |
| **[22]** | Sesuai (5 penulis) | Sesuai (sentence-case) | Sesuai (*Sensors*) | Sesuai (`vol. 21, no. 13, Art. no. 4597`) | Sesuai (`2021`, `doi: 10.3390/...`) | Sesuai (`<a id="ref22"></a>`) | Sesuai (tanda hubung `-`, tanpa em dash) |
| **[23]** | Sesuai (4 penulis) | Sesuai (sentence-case) | Sesuai (*Proc. AAAI...*) | Sesuai (`Art. no. 648`) | Sesuai (`2024`, `doi: 10.1609/...`) | Sesuai (`<a id="ref23"></a>`) | Sesuai (tanda hubung `-`, tanpa em dash) |
| **[24]** | Sesuai (2 penulis) | Sesuai (`tutorial` kecil) | Sesuai (*JMIR AI*) | Sesuai (`vol. 2, Art. no. e49023`) | Sesuai (`2023`, `doi: 10.2196/...`) | Sesuai (`<a id="ref24"></a>`) | Sesuai (tanda hubung `-`, tanpa em dash) |
| **[25]** | Sesuai (2 penulis) | Sesuai (`DemogPairs` tetap kapital) | Sesuai (*Proc. 2019...*) | Sesuai (`pp. 1-7`) | Sesuai (`2019`, `doi: 10.1109/...`) | Sesuai (`<a id="ref25"></a>`) | Sesuai (tanda hubung `-`, tanpa em dash) |
