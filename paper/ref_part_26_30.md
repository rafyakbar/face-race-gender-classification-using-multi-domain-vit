# Laporan Audit dan Perbaikan Referensi [26] - [30]

Dokumen ini menyajikan hasil audit mendalam dan perbaikan referensi nomor [26] sampai [30] pada naskah artikel ilmiah `paper/06_references.md`. Seluruh entri dicocokkan secara komparatif terhadap berkas sumber primer di direktori `paper/references/` dan diselaraskan dengan pedoman sitasi IEEE (`rules/IEEE_citation_guidelines.md`) serta aturan penulisan dokumen.

---

## 1. Ringkasan Hasil Audit

| No | Berkas Sumber Metadata | Status Awal | Masalah yang Teridentifikasi | Status Akhir |
|---|---|---|---|---|
| **[26]** | `2026_Visual perception based deep learning transformers for classifying paintings and photographs through feature extraction.ris` | Sesuai | Tidak ditemukan kesalahan. Penulis tunggal (L. Yu), judul sentence-case, nama jurnal (*Scientific Reports*), volume 16, nomor 1, nomor artikel (Art. no. 5326), tahun 2026, dan DOI valid. | Terverifikasi valid |
| **[27]** | `2023_Mask usage recognition using vision transformer with transfer learning and data augmentation.nbib` | Sesuai | Tidak ditemukan kesalahan. Penulis 3 orang ditulis lengkap, judul sentence-case, nama jurnal (*Intelligent Systems with Applications*), volume 17, nomor artikel (Art. no. 200186), tahun 2023, dan DOI valid. | Terverifikasi valid |
| **[28]** | `2021_Vision Transformers for Remote Sensing Image Classification.bib` | Perlu Perbaikan | Kapitalisasi judul artikel memakai Title Case (*Vision Transformers for Remote Sensing Image Classification*). Sesuai kaidah IEEE, judul artikel wajib memakai sentence-case. | Selesai diperbaiki |
| **[29]** | `2024_Visualizing and Understanding Patch Interactions in Vision Transformer.bib` | Perlu Perbaikan | Kapitalisasi judul artikel memakai Title Case (*Visualizing and Understanding Patch Interactions in Vision Transformer*). Sesuai kaidah IEEE, judul artikel wajib memakai sentence-case. | Selesai diperbaiki |
| **[30]** | `2022_Oblique and rotation double random forest.bib` | Sesuai | Tidak ditemukan kesalahan. Penulis 4 orang ditulis lengkap dengan inisial berjarak, judul sentence-case, nama jurnal (*Neural Networks*), volume 153, rentang halaman (pp. 496-517), tahun 2022, dan DOI valid. | Terverifikasi valid |

---

## 2. Rincian Temuan Audit per Referensi

### Referensi [26]
- **Berkas Sumber**: `paper/references/2026_Visual perception based deep learning transformers for classifying paintings and photographs through feature extraction.ris`
- **Tipe Publikasi**: Artikel Jurnal (*Journal Article*, Nature Portfolio / *Scientific Reports*)
- **Audit Penulis**:
  - Sumber RIS: `AU  - Yu, Liu`
  - Jumlah penulis: 1 penulis ($\le 6$, wajib ditulis lengkap).
  - Format IEEE: `L. Yu` (Inisial nama depan diikuti nama keluarga).
  - Evaluasi: Sesuai.
- **Audit Judul Artikel**:
  - Teks sumber: `"Visual perception based deep learning transformers for classifying paintings and photographs through feature extraction"`
  - Evaluasi format: Memakai sentence-case. Huruf pertama kata "Visual" kapital, sedangkan kata-kata lainnya memakai huruf kecil karena bukan nama diri atau akronim khusus. Teks diapit tanda kutip ganda dengan tanda koma di dalam tanda kutip penutup.
  - Evaluasi: Sesuai.
- **Audit Nama Jurnal**:
  - Sumber RIS: `JO  - Scientific Reports`
  - Format IEEE: `*Scientific Reports*` (Cetak miring).
  - Evaluasi: Sesuai.
- **Audit Volume, Isu, Nomor Artikel, Tahun, & DOI**:
  - Volume: `VL  - 16` $\rightarrow$ `vol. 16`
  - Isu: `IS  - 1` $\rightarrow$ `no. 1`
  - Nomor artikel: `SP  - 5326` $\rightarrow$ `Art. no. 5326`
  - Tahun: `PY  - 2026` $\rightarrow$ `2026`
  - DOI: `DO  - 10.1038/s41598-026-36298-4` $\rightarrow$ `doi: 10.1038/s41598-026-36298-4.`
  - Evaluasi: Sesuai.
- **Audit Karakter & Anchor**:
  - Tag anchor `<a id="ref26"></a>` terpasang sebelum entri sitasi.
  - Tanda hubung memakai tanda hubung biasa (`-`).
  - Seluruh teks mematuhi batasan leksikal dan ortografi.
- **Teks Entri Final**:
  ```markdown
  <a id="ref26"></a>
  [26] L. Yu, "Visual perception based deep learning transformers for classifying paintings and photographs through feature extraction," *Scientific Reports*, vol. 16, no. 1, Art. no. 5326, 2026, doi: 10.1038/s41598-026-36298-4.
  ```

---

### Referensi [27]
- **Berkas Sumber**: `paper/references/2023_Mask usage recognition using vision transformer with transfer learning and data augmentation.nbib`
- **Tipe Publikasi**: Artikel Jurnal (*Journal Article*, Elsevier / *Intelligent Systems with Applications*)
- **Audit Penulis**:
  - Sumber NBIB:
    - `FAU - Jahja, Hensel D` / `AU  - Jahja HD`
    - `FAU - Yudistira, Novanto` / `AU  - Yudistira N`
    - `FAU - Sutrisno` / `AU  - Sutrisno`
  - Jumlah penulis: 3 penulis ($\le 6$, seluruh nama penulis wajib dicantumkan).
  - Format IEEE: `H. D. Jahja, N. Yudistira, and Sutrisno` (Dilengkapi koma serial Oxford).
  - Evaluasi: Sesuai.
- **Audit Judul Artikel**:
  - Teks sumber: `"Mask usage recognition using vision transformer with transfer learning and data augmentation."`
  - Evaluasi format: Memakai sentence-case. Hanya huruf pertama "Mask" yang kapital; istilah "vision transformer" ditulis dengan huruf kecil.
  - Evaluasi: Sesuai.
- **Audit Nama Jurnal**:
  - Sumber NBIB: `JT  - Intelligent systems with applications`
  - Format IEEE: `*Intelligent Systems with Applications*` (Cetak miring).
  - Evaluasi: Sesuai.
- **Audit Volume, Nomor Artikel, Tahun, & DOI**:
  - Volume: `VI  - 17` $\rightarrow$ `vol. 17`
  - Nomor artikel: `PG  - 200186` $\rightarrow$ `Art. no. 200186`
  - Tahun: `DP  - 2023 Feb` $\rightarrow$ `2023`
  - DOI: `LID - 10.1016/j.iswa.2023.200186 [doi]` $\rightarrow$ `doi: 10.1016/j.iswa.2023.200186.`
  - Evaluasi: Sesuai.
- **Audit Karakter & Anchor**:
  - Tag anchor `<a id="ref27"></a>` terpasang sebelum entri sitasi.
  - Tanda hubung memakai tanda hubung biasa (`-`).
  - Seluruh teks mematuhi batasan leksikal dan ortografi.
- **Teks Entri Final**:
  ```markdown
  <a id="ref27"></a>
  [27] H. D. Jahja, N. Yudistira, and Sutrisno, "Mask usage recognition using vision transformer with transfer learning and data augmentation," *Intelligent Systems with Applications*, vol. 17, Art. no. 200186, 2023, doi: 10.1016/j.iswa.2023.200186.
  ```

---

### Referensi [28]
- **Berkas Sumber**: `paper/references/2021_Vision Transformers for Remote Sensing Image Classification.bib`
- **Tipe Publikasi**: Artikel Jurnal (*Article*, MDPI / *Remote Sensing*)
- **Audit Penulis**:
  - Sumber BibTeX: `AUTHOR = {Bazi, Yakoub and Bashmal, Laila and Rahhal, Mohamad M. Al and Dayil, Reham Al and Ajlan, Naif Al}`
  - Jumlah penulis: 5 penulis ($\le 6$, seluruh nama penulis wajib dicantumkan).
  - Format IEEE: `Y. Bazi, L. Bashmal, M. M. A. Rahhal, R. A. Dayil, and N. A. Ajlan`
  - Evaluasi: Sesuai.
- **Audit Judul Artikel**:
  - Teks sumber: `"Vision Transformers for Remote Sensing Image Classification"`
  - Teks awal di `06_references.md`: `"Vision Transformers for Remote Sensing Image Classification,"` (Title Case).
  - Temuan audit: Kapitalisasi judul memakai Title Case di mana kata `Transformers`, `Remote`, `Sensing`, `Image`, dan `Classification` diawali huruf besar. Kata-kata tersebut merupakan kosakata umum dan istilah teknis umum, bukan nama diri atau singkatan akronim. Sesuai aturan IEEE, artikel wajib ditulis dalam format sentence-case.
  - Perbaikan: Diubah menjadi `"Vision transformers for remote sensing image classification,"`.
- **Audit Nama Jurnal**:
  - Sumber BibTeX: `JOURNAL = {Remote Sensing}`
  - Format IEEE: `*Remote Sensing*` (Cetak miring).
  - Evaluasi: Sesuai.
- **Audit Volume, Isu, Nomor Artikel, Tahun, & DOI**:
  - Volume: `VOLUME = {13}` $\rightarrow$ `vol. 13`
  - Isu: `NUMBER = {3}` $\rightarrow$ `no. 3`
  - Nomor artikel: `ARTICLE-NUMBER = {516}` $\rightarrow$ `Art. no. 516`
  - Tahun: `YEAR = {2021}` $\rightarrow$ `2021`
  - DOI: `DOI = {10.3390/rs13030516}` $\rightarrow$ `doi: 10.3390/rs13030516.`
  - Evaluasi: Sesuai.
- **Audit Karakter & Anchor**:
  - Tag anchor `<a id="ref28"></a>` terpasang sebelum entri sitasi.
  - Tanda hubung memakai tanda hubung biasa (`-`).
  - Seluruh teks mematuhi batasan leksikal dan ortografi.
- **Teks Entri Final**:
  ```markdown
  <a id="ref28"></a>
  [28] Y. Bazi, L. Bashmal, M. M. A. Rahhal, R. A. Dayil, and N. A. Ajlan, "Vision transformers for remote sensing image classification," *Remote Sensing*, vol. 13, no. 3, Art. no. 516, 2021, doi: 10.3390/rs13030516.
  ```

---

### Referensi [29]
- **Berkas Sumber**: `paper/references/2024_Visualizing and Understanding Patch Interactions in Vision Transformer.bib`
- **Tipe Publikasi**: Artikel Jurnal (*Article*, IEEE / *IEEE Transactions on Neural Networks and Learning Systems*)
- **Audit Penulis**:
  - Sumber BibTeX: `author={Ma, Jie and Bai, Yalong and Zhong, Bineng and Zhang, Wei and Yao, Ting and Mei, Tao}`
  - Jumlah penulis: 6 penulis ($\le 6$, seluruh 6 nama penulis wajib dicantumkan lengkap).
  - Format IEEE: `J. Ma, Y. Bai, B. Zhong, W. Zhang, T. Yao, and T. Mei`
  - Evaluasi: Sesuai.
- **Audit Judul Artikel**:
  - Teks sumber: `"Visualizing and Understanding Patch Interactions in Vision Transformer"`
  - Teks awal di `06_references.md`: `"Visualizing and Understanding Patch Interactions in Vision Transformer,"` (Title Case).
  - Temuan audit: Judul awal ditulis dengan kapitalisasi Title Case penuh (`Understanding`, `Patch`, `Interactions`, `Vision`, `Transformer`). Istilah-istilah ini bukan nama diri entitas atau akronim, melainkan kata umum dan frasa teknis. Sesuai kaidah IEEE, hanya huruf pertama judul yang ditulis kapital.
  - Perbaikan: Diubah menjadi `"Visualizing and understanding patch interactions in vision transformer,"`.
- **Audit Nama Jurnal**:
  - Sumber BibTeX: `journal={IEEE Transactions on Neural Networks and Learning Systems}`
  - Format IEEE: `*IEEE Transactions on Neural Networks and Learning Systems*` (Cetak miring).
  - Evaluasi: Sesuai.
- **Audit Volume, Isu, Rentang Halaman, Tahun, & DOI**:
  - Volume: `volume={35}` $\rightarrow$ `vol. 35`
  - Isu: `number={10}` $\rightarrow$ `no. 10`
  - Rentang halaman: `pages={13671-13680}` $\rightarrow$ `pp. 13671-13680` (Memakai tanda hubung standar `-`).
  - Tahun: `year={2024}` $\rightarrow$ `2024`
  - DOI: `doi={10.1109/TNNLS.2023.3270479}` $\rightarrow$ `doi: 10.1109/TNNLS.2023.3270479.`
  - Evaluasi: Sesuai.
- **Audit Karakter & Anchor**:
  - Tag anchor `<a id="ref29"></a>` terpasang sebelum entri sitasi.
  - Tanda hubung memakai tanda hubung biasa (`-`).
  - Seluruh teks mematuhi batasan leksikal dan ortografi.
- **Teks Entri Final**:
  ```markdown
  <a id="ref29"></a>
  [29] J. Ma, Y. Bai, B. Zhong, W. Zhang, T. Yao, and T. Mei, "Visualizing and understanding patch interactions in vision transformer," *IEEE Transactions on Neural Networks and Learning Systems*, vol. 35, no. 10, pp. 13671-13680, 2024, doi: 10.1109/TNNLS.2023.3270479.
  ```

---

### Referensi [30]
- **Berkas Sumber**: `paper/references/2022_Oblique and rotation double random forest.bib`
- **Tipe Publikasi**: Artikel Jurnal (*Article*, Elsevier / *Neural Networks*)
- **Audit Penulis**:
  - Sumber BibTeX: `author = {M.A. Ganaie and M. Tanveer and P.N. Suganthan and V. Snasel}`
  - Jumlah penulis: 4 penulis ($\le 6$, seluruh 4 nama penulis wajib dicantumkan lengkap).
  - Format IEEE: `M. A. Ganaie, M. Tanveer, P. N. Suganthan, and V. Snasel` (Inisial nama diberi spasi sesuai standar IEEE).
  - Evaluasi: Sesuai.
- **Audit Judul Artikel**:
  - Teks sumber: `"Oblique and rotation double random forest"`
  - Evaluasi format: Memakai sentence-case. Hanya huruf pertama "Oblique" yang kapital; istilah "double random forest" ditulis dengan huruf kecil.
  - Evaluasi: Sesuai.
- **Audit Nama Jurnal**:
  - Sumber BibTeX: `journal = {Neural Networks}`
  - Format IEEE: `*Neural Networks*` (Cetak miring).
  - Evaluasi: Sesuai.
- **Audit Volume, Isu, Rentang Halaman, Tahun, & DOI**:
  - Volume: `volume = {153}` $\rightarrow$ `vol. 153`
  - Isu: Tidak ada nomor isu terpisah pada volume ini.
  - Rentang halaman: `pages = {496-517}` $\rightarrow$ `pp. 496-517` (Memakai tanda hubung standar `-`).
  - Tahun: `year = {2022}` $\rightarrow$ `2022`
  - DOI: `doi = {https://doi.org/10.1016/j.neunet.2022.06.012}` $\rightarrow$ `doi: 10.1016/j.neunet.2022.06.012.`
  - Evaluasi: Sesuai.
- **Audit Karakter & Anchor**:
  - Tag anchor `<a id="ref30"></a>` terpasang sebelum entri sitasi.
  - Tanda hubung memakai tanda hubung biasa (`-`).
  - Seluruh teks mematuhi batasan leksikal dan ortografi.
- **Teks Entri Final**:
  ```markdown
  <a id="ref30"></a>
  [30] M. A. Ganaie, M. Tanveer, P. N. Suganthan, and V. Snasel, "Oblique and rotation double random forest," *Neural Networks*, vol. 153, pp. 496-517, 2022, doi: 10.1016/j.neunet.2022.06.012.
  ```

---

## 3. Teks Final Entri Referensi [26] - [30]

Berikut adalah blok teks referensi final nomor [26] sampai [30] yang telah diverifikasi dan disinkronkan ke dalam `paper/06_references.md`:

```markdown
<a id="ref26"></a>
[26] L. Yu, "Visual perception based deep learning transformers for classifying paintings and photographs through feature extraction," *Scientific Reports*, vol. 16, no. 1, Art. no. 5326, 2026, doi: 10.1038/s41598-026-36298-4.

<a id="ref27"></a>
[27] H. D. Jahja, N. Yudistira, and Sutrisno, "Mask usage recognition using vision transformer with transfer learning and data augmentation," *Intelligent Systems with Applications*, vol. 17, Art. no. 200186, 2023, doi: 10.1016/j.iswa.2023.200186.

<a id="ref28"></a>
[28] Y. Bazi, L. Bashmal, M. M. A. Rahhal, R. A. Dayil, and N. A. Ajlan, "Vision transformers for remote sensing image classification," *Remote Sensing*, vol. 13, no. 3, Art. no. 516, 2021, doi: 10.3390/rs13030516.

<a id="ref29"></a>
[29] J. Ma, Y. Bai, B. Zhong, W. Zhang, T. Yao, and T. Mei, "Visualizing and understanding patch interactions in vision transformer," *IEEE Transactions on Neural Networks and Learning Systems*, vol. 35, no. 10, pp. 13671-13680, 2024, doi: 10.1109/TNNLS.2023.3270479.

<a id="ref30"></a>
[30] M. A. Ganaie, M. Tanveer, P. N. Suganthan, and V. Snasel, "Oblique and rotation double random forest," *Neural Networks*, vol. 153, pp. 496-517, 2022, doi: 10.1016/j.neunet.2022.06.012.
```
