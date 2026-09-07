# Audit dan Pembetulan Referensi [1] - [5]

Dokumen ini memuat hasil audit komprehensif dan teks perbaikan final untuk referensi nomor [1] sampai [5] pada naskah artikel ilmiah, merujuk pada pedoman IEEE (`rules/IEEE_citation_guidelines.md`), aturan penulisan Markdown (`rules/md_rules.txt`), serta berkas sumber referensi di `paper/references/`.

---

## 1. Rincian Temuan Audit per Referensi

### [1] Rusia & Singh (2023)
- **Berkas Sumber**: `paper/references/2022_A comprehensive survey on techniques to handle face identity threats challenges and opportunities.ris`
- **Audit Penulis**:
  - Penulis pada berkas sumber: Mayank Kumar Rusia dan Dushyant Kumar Singh (total 2 penulis).
  - Evaluasi aturan: Karena jumlah penulis $\le 6$, seluruh penulis ditulis lengkap (inisial nama depan diikuti nama keluarga).
  - Format IEEE: `M. K. Rusia and D. K. Singh` (sesuai).
- **Audit Judul Artikel**:
  - Teks: `"A comprehensive survey on techniques to handle face identity threats: challenges and opportunities,"`
  - Evaluasi format: Menerapkan format sentence-case. Hanya huruf pertama "A" yang kapital; tidak ada nama diri khusus atau akronim. Teks diapit tanda kutip ganda dengan tanda koma di dalam tanda kutip penutup (sesuai).
- **Audit Nama Jurnal**:
  - Sumber: `Multimedia Tools and Applications`
  - Format IEEE: `*Multimedia Tools and Applications*` (cetak miring, Title Case, sesuai).
- **Audit Volume, Isu, Rentang Halaman, Tahun, & DOI**:
  - Volume: `vol. 82`
  - Isu: `no. 2`
  - Rentang halaman: `pp. 1669-1748` (memakai tanda hubung biasa `-`).
  - Tahun: `2023` (berdasarkan `PY - 2023` dan `DA - 2023/01/01`).
  - DOI: `doi: 10.1007/s11042-022-13248-6` (format `doi: 10.xxxx/...` tanpa prefiks `https://doi.org/`).
- **Audit Karakter Terlarang & Anchor**:
  - Bebas dari karakter em dash, seluruh tanda pemisah memakai tanda hubung biasa (`-`).
  - Bebas dari kata terlarang (kendati, paradigma, g-u-n-a).
  - Tag anchor `<a id="ref1"></a>` terpasang sebelum entri.
- **Kesimpulan Status**: Entri terverifikasi valid dan akurat sesuai sumber.

---

### [2] Meden et al. (2021)
- **Berkas Sumber**: `paper/references/2021_Privacy–Enhancing Face Biometrics A Comprehensive Survey.bib`
- **Audit Penulis**:
  - Penulis pada berkas sumber: Blaž Meden, Peter Rot, Philipp Terhörst, Naser Damer, Arjan Kuijper, Walter J. Scheirer, Arun Ross, Peter Peer, Vitomir Štruc (total 9 penulis).
  - Evaluasi aturan: Karena jumlah penulis $> 6$, dicantumkan nama penulis pertama diikuti 'et al.'.
  - Format IEEE: `B. Meden et al.,` (sesuai).
- **Audit Judul Artikel**:
  - Teks awal: `"Privacy-Enhancing Face Biometrics: A Comprehensive Survey,"`
  - Temuan audit:
    1. Judul awal tertulis dalam Title Case kapitalisasi penuh pada setiap kata (`Enhancing`, `Face`, `Biometrics`, `Comprehensive`, `Survey`).
    2. Pada berkas sumber BibTeX terdapat tanda en dash (U+2013) pada kata `Privacy–Enhancing`. Sesuai aturan penulisan naskah, karakter pemisah wajib memakai tanda hubung biasa (`-`).
  - Pembetulan: Diubah menjadi sentence-case murni. Hanya kata pertama "Privacy" yang kapital. Kata setelah tanda titik dua ("a") ditulis dengan huruf kecil karena bukan kata benda khusus atau akronim.
  - Teks setelah perbaikan: `"Privacy-enhancing face biometrics: a comprehensive survey,"`
- **Audit Nama Jurnal**:
  - Sumber: `IEEE Transactions on Information Forensics and Security`
  - Format IEEE: `*IEEE Transactions on Information Forensics and Security*` (cetak miring, Title Case, sesuai).
- **Audit Volume, Isu, Rentang Halaman, Tahun, & DOI**:
  - Volume: `vol. 16`
  - Isu: Tidak memiliki nomor isu (`number={}` pada BibTeX).
  - Rentang halaman: `pp. 4147-4183` (memakai tanda hubung biasa `-`).
  - Tahun: `2021`
  - DOI: `doi: 10.1109/TIFS.2021.3096024` (sesuai).
- **Audit Karakter Terlarang & Anchor**:
  - Bebas dari karakter em dash maupun en dash pada teks entri; digantikan tanda hubung biasa (`-`).
  - Bebas dari kata terlarang (kendati, paradigma, g-u-n-a).
  - Tag anchor `<a id="ref2"></a>` terpasang sebelum entri.
- **Kesimpulan Status**: Diperbaiki kapitalisasi judul menjadi sentence-case.

---

### [3] Birhane (2022)
- **Berkas Sumber**: `paper/references/2022_The unseen Black faces of AI algorithms.nbib`
- **Audit Penulis**:
  - Penulis pada berkas sumber: Abeba Birhane (total 1 penulis).
  - Evaluasi aturan: Karena jumlah penulis $\le 6$, nama penulis ditulis lengkap.
  - Format IEEE: `A. Birhane` (sesuai).
- **Audit Judul Artikel**:
  - Teks: `"The unseen Black faces of AI algorithms,"`
  - Evaluasi format:
    - Huruf pertama "The" kapital.
    - Kata "Black" tetap kapital karena merupakan nama diri/etnisitas kelompok ras manusia (sesuai kaidah ortografi baku dan deskriptor Medline: `*Black People`).
    - Singkatan "AI" tetap kapital karena merupakan akronim resmi (*Artificial Intelligence*).
    - Kata lainnya ("unseen", "faces of", "algorithms") ditulis dalam huruf kecil.
    - Format telah memenuhi kaidah sentence-case IEEE secara tepat.
- **Audit Nama Jurnal**:
  - Sumber: `Nature`
  - Format IEEE: `*Nature*` (cetak miring, sesuai).
- **Audit Volume, Isu, Rentang Halaman, Tahun, & DOI**:
  - Volume: `vol. 610`
  - Isu: `no. 7932`
  - Rentang halaman: `pp. 451-452` (memakai tanda hubung biasa `-`).
  - Bulan & Tahun: `Oct. 2022` (sesuai `DP - 2022 Oct` pada sumber NBIB dan singkatan bulan standar IEEE).
  - DOI: `doi: 10.1038/d41586-022-03050-7` (sesuai).
- **Audit Karakter Terlarang & Anchor**:
  - Bebas dari karakter em dash.
  - Bebas dari kata terlarang (kendati, paradigma, g-u-n-a).
  - Tag anchor `<a id="ref3"></a>` terpasang sebelum entri.
- **Kesimpulan Status**: Entri terverifikasi valid dan akurat sesuai sumber.

---

### [4] Overbye-Thompson, Hamilton, & Mastro (2024)
- **Berkas Sumber**: `paper/references/2024_Reinvention mediates impacts of skin tone bias in algorithms implications for technology diffusion.bib`
- **Audit Penulis**:
  - Penulis pada berkas sumber: Hannah Overbye-Thompson, Kristy A Hamilton, Dana Mastro (total 3 penulis).
  - Evaluasi aturan: Karena jumlah penulis $\le 6$, seluruh 3 nama penulis ditulis lengkap. Nama keluarga ganda dengan tanda hubung dipertahankan (`Overbye-Thompson`).
  - Format IEEE: `H. Overbye-Thompson, K. A. Hamilton, and D. Mastro` (sesuai).
- **Audit Judul Artikel**:
  - Teks: `"Reinvention mediates impacts of skin tone bias in algorithms: implications for technology diffusion,"`
  - Evaluasi format: Telah berformat sentence-case yang tepat. Hanya huruf pertama "Reinvention" yang kapital. Kata setelah tanda titik dua ("implications") ditulis dalam huruf kecil karena bukan nama diri atau akronim.
- **Audit Nama Jurnal**:
  - Sumber: `Journal of Computer-Mediated Communication`
  - Format IEEE: `*Journal of Computer-Mediated Communication*` (cetak miring, Title Case, sesuai).
- **Audit Volume, Isu, Nomor Artikel, Tahun, & DOI**:
  - Volume: `vol. 29`
  - Isu: `no. 5`
  - Nomor artikel: `Art. no. zmae016` (pengidentifikasi artikel elektronik Oxford University Press, sesuai aturan nomor artikel IEEE).
  - Tahun: `2024`
  - DOI: `doi: 10.1093/jcmc/zmae016` (sesuai).
- **Audit Karakter Terlarang & Anchor**:
  - Bebas dari karakter em dash.
  - Bebas dari kata terlarang (kendati, paradigma, g-u-n-a).
  - Tag anchor `<a id="ref4"></a>` terpasang sebelum entri.
- **Kesimpulan Status**: Entri terverifikasi valid dan akurat sesuai sumber.

---

### [5] Terhörst et al. (2022)
- **Berkas Sumber**: `paper/references/2022_A Comprehensive Study on Face Recognition Biases Beyond Demographics.bib`
- **Audit Penulis**:
  - Penulis pada berkas sumber: Philipp Terhörst, Jan Niklas Kolf, Marco Huber, Florian Kirchbuchner, Naser Damer, Aythami Morales Moreno, Julian Fierrez, Arjan Kuijper (total 8 penulis).
  - Evaluasi aturan: Karena jumlah penulis $> 6$, dicantumkan nama penulis pertama diikuti 'et al.'.
  - Format IEEE: `P. Terhörst et al.,` (sesuai).
- **Audit Judul Artikel**:
  - Teks awal: `"A Comprehensive Study on Face Recognition Biases Beyond Demographics,"`
  - Temuan audit: Judul awal tertulis dalam Title Case kapitalisasi penuh pada setiap kata (`Comprehensive`, `Study`, `Face`, `Recognition`, `Biases`, `Beyond`, `Demographics`).
  - Pembetulan: Sesuai kaidah IEEE, judul artikel wajib berformat sentence-case. Tidak ada kata benda khusus, nama diri, maupun akronim pada judul ini. Seluruh kata setelah kata pertama "A" wajib memakai huruf kecil.
  - Teks setelah perbaikan: `"A comprehensive study on face recognition biases beyond demographics,"`
- **Audit Nama Jurnal**:
  - Sumber: `IEEE Transactions on Technology and Society`
  - Format IEEE: `*IEEE Transactions on Technology and Society*` (cetak miring, Title Case, sesuai).
- **Audit Volume, Isu, Rentang Halaman, Tahun, & DOI**:
  - Volume: `vol. 3`
  - Isu: `no. 1`
  - Rentang halaman: `pp. 16-30` (memakai tanda hubung biasa `-`).
  - Tahun: `2022` (berdasarkan `year={2022}` pada BibTeX).
  - DOI: `doi: 10.1109/TTS.2021.3111823` (sesuai).
- **Audit Karakter Terlarang & Anchor**:
  - Bebas dari karakter em dash.
  - Bebas dari kata terlarang (kendati, paradigma, g-u-n-a).
  - Tag anchor `<a id="ref5"></a>` terpasang sebelum entri.
- **Kesimpulan Status**: Diperbaiki kapitalisasi judul menjadi sentence-case.

---

## 2. Teks Final Entri Referensi [1] - [5]

Berikut adalah teks entri final yang telah diaudit, diverifikasi terhadap berkas sumber metadata, dan disinkronkan ke dalam `paper/06_references.md`:

```markdown
<a id="ref1"></a>
[1] M. K. Rusia and D. K. Singh, "A comprehensive survey on techniques to handle face identity threats: challenges and opportunities," *Multimedia Tools and Applications*, vol. 82, no. 2, pp. 1669-1748, 2023, doi: 10.1007/s11042-022-13248-6.

<a id="ref2"></a>
[2] B. Meden et al., "Privacy-enhancing face biometrics: a comprehensive survey," *IEEE Transactions on Information Forensics and Security*, vol. 16, pp. 4147-4183, 2021, doi: 10.1109/TIFS.2021.3096024.

<a id="ref3"></a>
[3] A. Birhane, "The unseen Black faces of AI algorithms," *Nature*, vol. 610, no. 7932, pp. 451-452, Oct. 2022, doi: 10.1038/d41586-022-03050-7.

<a id="ref4"></a>
[4] H. Overbye-Thompson, K. A. Hamilton, and D. Mastro, "Reinvention mediates impacts of skin tone bias in algorithms: implications for technology diffusion," *Journal of Computer-Mediated Communication*, vol. 29, no. 5, Art. no. zmae016, 2024, doi: 10.1093/jcmc/zmae016.

<a id="ref5"></a>
[5] P. Terhörst et al., "A comprehensive study on face recognition biases beyond demographics," *IEEE Transactions on Technology and Society*, vol. 3, no. 1, pp. 16-30, 2022, doi: 10.1109/TTS.2021.3111823.
```
