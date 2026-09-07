# Laporan Audit dan Perbaikan Referensi [31] - [35]

Dokumen ini menyajikan audit menyeluruh dan perbaikan referensi nomor [31] sampai [35] pada `paper/06_references.md` berdasarkan pedoman IEEE (`rules/IEEE_citation_guidelines.md`) serta berkas sumber primer di `paper/references/`.

---

## 1. Ringkasan Hasil Audit

| No | Berkas Sumber | Status Awal | Masalah Utama yang Ditemukan | Status Akhir |
|---|---|---|---|---|
| [31] | `2022_BoostTree and BoostForest for Ensemble Learning.bib` | Perlu Perbaikan | Judul artikel menggunakan Title Case pada kata "Ensemble Learning" yang seharusnya huruf kecil (sentence-case). | Selesai diperbaiki |
| [32] | `2025_Interpreting Deep Forest through Feature Contribution and MDI Feature Importance.bib` | Perlu Perbaikan | Judul artikel menggunakan Title Case pada frasa "Deep Forest through Feature Contribution and MDI Feature Importance" di mana istilah teknis selain akronim MDI harus menggunakan huruf kecil. | Selesai diperbaiki |
| [33] | `2022_Optimization of the Random Forest Hyperparameters for Power Industrial Control Systems Intrusion Detection Using an Improved Grid Search Algorithm.bib` | Perlu Perbaikan | Judul artikel menggunakan Title Case secara penuh tanpa mematuhi prinsip sentence-case IEEE. Seluruh kata non-akronim/nama diri harus diubah ke huruf kecil. | Selesai diperbaiki |
| [34] | `2024_Data-driven multinomial random forest a new random forest variant with strong consistency.ris` | Sesuai | Format penulis, judul sentence-case, nama jurnal, volume, nomor, nomor artikel (Art. no.), tahun, dan DOI sudah sesuai standar IEEE. | Terverifikasi valid |
| [35] | `2023_Quantile-distribution functions and their use for classification, with application to naïve Bayes classifiers.ris` | Perlu Perbaikan | Kata "naive" pada judul artikel di berkas sumber aslinya dieja "naïve" (dengan diaeresis). Perbaikan mempertahankan ketepatan ejaan sumber asli. | Selesai diperbaiki |

---

## 2. Rincian Audit dan Verifikasi Metadata

### Referensi [31]

- **Berkas Sumber**: `paper/references/2022_BoostTree and BoostForest for Ensemble Learning.bib`
- **Metadata Sumber**:
  - Tipe entri: `@ARTICLE`
  - Penulis: `Zhao, Changming and Wu, Dongrui and Huang, Jian and Yuan, Ye and Zhang, Hai-Tao and Peng, Ruimin and Shi, Zhenhua` (total 7 penulis)
  - Judul: `BoostTree and BoostForest for Ensemble Learning`
  - Jurnal: `IEEE Transactions on Pattern Analysis and Machine Intelligence`
  - Tahun: `2023`
  - Volume: `45`
  - Nomor: `7`
  - Halaman: `8110-8126`
  - DOI: `10.1109/TPAMI.2022.3227370`
- **Analisis Pedoman IEEE**:
  1. *Penulis*: Terdapat 7 penulis (> 6 penulis). Sesuai aturan IEEE, jika penulis lebih dari 6 orang, sebutkan nama penulis pertama diikuti singkatan `et al.` (menjadi `C. Zhao et al.,`).
  2. *Judul Artikel*: Format IEEE mewajibkan kapitalisasi sentence-case (hanya huruf awal kalimat, nama diri/kata benda khusus, dan akronim yang dikapitalisasi). Nama algoritma usulan `BoostTree` dan `BoostForest` merupakan nama diri teknis yang mempertahankan format camelCase/PascalCase. Namun, frasa "Ensemble Learning" adalah istilah umum bidang pembelajaran mesin sehingga wajib ditulis huruf kecil ("ensemble learning").
  3. *Nama Jurnal*: Dicetak miring dengan markdown: `*IEEE Transactions on Pattern Analysis and Machine Intelligence*,`.
  4. *Volume, Isu, Halaman*: `vol. 45, no. 7, pp. 8110-8126,`. Rentang halaman menggunakan tanda hubung biasa (`-`), bukan em dash.
  5. *Tahun & DOI*: `2023, doi: 10.1109/TPAMI.2022.3227370.` (tanpa awalan URL).
  6. *Anchor*: Didahului oleh `<a id="ref31"></a>`.
- **Teks Awal**:
  ```markdown
  <a id="ref31"></a>
  [31] C. Zhao et al., "BoostTree and BoostForest for Ensemble Learning," *IEEE Transactions on Pattern Analysis and Machine Intelligence*, vol. 45, no. 7, pp. 8110-8126, 2023, doi: 10.1109/TPAMI.2022.3227370.
  ```
- **Teks Hasil Perbaikan**:
  ```markdown
  <a id="ref31"></a>
  [31] C. Zhao et al., "BoostTree and BoostForest for ensemble learning," *IEEE Transactions on Pattern Analysis and Machine Intelligence*, vol. 45, no. 7, pp. 8110-8126, 2023, doi: 10.1109/TPAMI.2022.3227370.
  ```

---

### Referensi [32]

- **Berkas Sumber**: `paper/references/2025_Interpreting Deep Forest through Feature Contribution and MDI Feature Importance.bib`
- **Metadata Sumber**:
  - Tipe entri: `@article`
  - Penulis: `He, Yi-Xiao and Lyu, Shen-Huan and Jiang, Yuan` (total 3 penulis)
  - Judul: `Interpreting Deep Forest through Feature Contribution and MDI Feature Importance`
  - Jurnal: `ACM Trans. Knowl. Discov. Data` (nama resmi lengkap: `ACM Transactions on Knowledge Discovery from Data`)
  - Tahun: `2025`
  - Volume: `20`
  - Nomor: `1`
  - Nomor Artikel: `articleno = {15}`
  - DOI: `10.1145/3641108`
- **Analisis Pedoman IEEE**:
  1. *Penulis*: Berjumlah 3 orang (<= 6 penulis). Seluruh nama penulis wajib dicantumkan lengkap dengan format inisial nama depan diikuti nama keluarga: `Y.-X. He, S.-H. Lyu, and Y. Jiang,`.
  2. *Judul Artikel*: Disesuaikan dengan kaidah sentence-case:
     - "Interpreting": kata pertama dikapitalisasi.
     - "deep forest": kelas model pembelajaran mesin (sebagaimana penulisan "random forest" dan "vision transformer"), ditulis dengan huruf kecil.
     - "feature contribution": frasa nomina umum, ditulis dengan huruf kecil.
     - "MDI": singkatan akronim dari *Mean Decrease Impurity*, wajib tetap ditulis huruf kapital penuh.
     - "feature importance": istilah umum, ditulis dengan huruf kecil.
     - Menjadi: `"Interpreting deep forest through feature contribution and MDI feature importance,"`.
  3. *Nama Jurnal*: Menggunakan nama formal lengkap dan dicetak miring: `*ACM Transactions on Knowledge Discovery from Data*,`.
  4. *Volume, Nomor, Artikel*: Format nomor artikel IEEE: `vol. 20, no. 1, Art. no. 15,`.
  5. *Tahun & DOI*: `2025, doi: 10.1145/3641108.`.
  6. *Anchor*: Didahului oleh `<a id="ref32"></a>`.
- **Teks Awal**:
  ```markdown
  <a id="ref32"></a>
  [32] Y.-X. He, S.-H. Lyu, and Y. Jiang, "Interpreting Deep Forest through Feature Contribution and MDI Feature Importance," *ACM Transactions on Knowledge Discovery from Data*, vol. 20, no. 1, Art. no. 15, 2025, doi: 10.1145/3641108.
  ```
- **Teks Hasil Perbaikan**:
  ```markdown
  <a id="ref32"></a>
  [32] Y.-X. He, S.-H. Lyu, and Y. Jiang, "Interpreting deep forest through feature contribution and MDI feature importance," *ACM Transactions on Knowledge Discovery from Data*, vol. 20, no. 1, Art. no. 15, 2025, doi: 10.1145/3641108.
  ```

---

### Referensi [33]

- **Berkas Sumber**: `paper/references/2022_Optimization of the Random Forest Hyperparameters for Power Industrial Control Systems Intrusion Detection Using an Improved Grid Search Algorithm.bib`
- **Metadata Sumber**:
  - Tipe entri: `@Article`
  - Penulis: `Zhu, Ningyuan and Zhu, Chaoyang and Zhou, Liang and Zhu, Yayun and Zhang, Xiaojuan` (total 5 penulis)
  - Judul: `Optimization of the Random Forest Hyperparameters for Power Industrial Control Systems Intrusion Detection Using an Improved Grid Search Algorithm`
  - Jurnal: `Applied Sciences`
  - Tahun: `2022`
  - Volume: `12`
  - Nomor: `20`
  - Nomor Artikel: `ARTICLE-NUMBER = {10456}`
  - DOI: `10.3390/app122010456`
- **Analisis Pedoman IEEE**:
  1. *Penulis*: Berjumlah 5 orang (<= 6 penulis). Seluruh penulis dicantumkan: `N. Zhu, C. Zhu, L. Zhou, Y. Zhu, and X. Zhang,`.
  2. *Judul Artikel*: Teks awal masih menggunakan format Title Case secara utuh. Pada kaidah sentence-case IEEE:
     - Hanya kata pertama ("Optimization") yang kapital.
     - Frasa "random forest hyperparameters", "power industrial control systems intrusion detection", serta "using an improved grid search algorithm" seluruhnya adalah istilah deskriptif umum tanpa akronim atau nama diri khusus.
     - Judul diperbaiki menjadi: `"Optimization of the random forest hyperparameters for power industrial control systems intrusion detection using an improved grid search algorithm,"`.
  3. *Nama Jurnal*: `*Applied Sciences*,`.
  4. *Volume, Nomor, Artikel*: Format artikel bernomor: `vol. 12, no. 20, Art. no. 10456,`.
  5. *Tahun & DOI*: `2022, doi: 10.3390/app122010456.`.
  6. *Anchor*: Didahului oleh `<a id="ref33"></a>`.
- **Teks Awal**:
  ```markdown
  <a id="ref33"></a>
  [33] N. Zhu, C. Zhu, L. Zhou, Y. Zhu, and X. Zhang, "Optimization of the Random Forest Hyperparameters for Power Industrial Control Systems Intrusion Detection Using an Improved Grid Search Algorithm," *Applied Sciences*, vol. 12, no. 20, Art. no. 10456, 2022, doi: 10.3390/app122010456.
  ```
- **Teks Hasil Perbaikan**:
  ```markdown
  <a id="ref33"></a>
  [33] N. Zhu, C. Zhu, L. Zhou, Y. Zhu, and X. Zhang, "Optimization of the random forest hyperparameters for power industrial control systems intrusion detection using an improved grid search algorithm," *Applied Sciences*, vol. 12, no. 20, Art. no. 10456, 2022, doi: 10.3390/app122010456.
  ```

---

### Referensi [34]

- **Berkas Sumber**: `paper/references/2024_Data-driven multinomial random forest a new random forest variant with strong consistency.ris`
- **Metadata Sumber**:
  - Tipe entri: `TY - JOUR`
  - Penulis: `Chen, JunHao; Wang, XueLi; Lei, Fei` (total 3 penulis)
  - Judul: `Data-driven multinomial random forest: a new random forest variant with strong consistency`
  - Jurnal: `Journal of Big Data`
  - Tahun: `2024`
  - Volume: `11`
  - Nomor: `1`
  - Nomor Artikel / Halaman: `SP - 34` (artikelnr. 34)
  - DOI: `10.1186/s40537-023-00874-6`
- **Analisis Pedoman IEEE**:
  1. *Penulis*: Berjumlah 3 orang (<= 6 penulis). Dituliskan semua: `J. Chen, X. Wang, and F. Lei,`.
  2. *Judul Artikel*: Sudah menggunakan kaidah sentence-case yang tepat. Huruf pertama "Data-driven" kapital, kata setelah titik dua diawali huruf kecil ("a new random forest variant with strong consistency"), dan nama model ditulis huruf kecil ("multinomial random forest").
  3. *Nama Jurnal*: Dicetak miring `*Journal of Big Data*,`.
  4. *Volume, Isu, Artikel*: Pada jurnal SpringerOpen *Journal of Big Data*, nilai SP (34) berperan sebagai nomor artikel unik. Format `vol. 11, no. 1, Art. no. 34,` sudah tepat dan konsisten dengan jurnal bersistem penomoran artikel.
  5. *Tahun & DOI*: `2024, doi: 10.1186/s40537-023-00874-6.`.
  6. *Anchor*: Didahului oleh `<a id="ref34"></a>`.
- **Teks Awal & Perbaikan (Identik/Valid)**:
  ```markdown
  <a id="ref34"></a>
  [34] J. Chen, X. Wang, and F. Lei, "Data-driven multinomial random forest: a new random forest variant with strong consistency," *Journal of Big Data*, vol. 11, no. 1, Art. no. 34, 2024, doi: 10.1186/s40537-023-00874-6.
  ```

---

### Referensi [35]

- **Berkas Sumber**: `paper/references/2023_Quantile-distribution functions and their use for classification, with application to naïve Bayes classifiers.ris`
- **Metadata Sumber**:
  - Tipe entri: `TY - JOUR`
  - Penulis: `Redivo, Edoardo; Viroli, Cinzia; Farcomeni, Alessio` (total 3 penulis)
  - Judul: `Quantile-distribution functions and their use for classification, with application to naïve Bayes classifiers`
  - Jurnal: `Statistics and Computing`
  - Tahun: `2023`
  - Volume: `33`
  - Nomor: `2`
  - Nomor Artikel / Halaman: `SP - 55` (artikelnr. 55)
  - DOI: `10.1007/s11222-023-10224-4`
- **Analisis Pedoman IEEE**:
  1. *Penulis*: Berjumlah 3 orang (<= 6 penulis). Dituliskan semua: `E. Redivo, C. Viroli, and A. Farcomeni,`.
  2. *Judul Artikel*:
     - Sesuai berkas sumber primer, kata "naïve" ditulis dengan karakter diaeresis `ï` (*naïve Bayes*).
     - Nama "Bayes" adalah nama tokoh (Thomas Bayes / proper noun) sehingga wajib dikapitalisasi.
     - Kata-kata lain mengikuti kaidah sentence-case huruf kecil.
     - Judul disempurnakan menjadi: `"Quantile-distribution functions and their use for classification, with application to naïve Bayes classifiers,"`.
  3. *Nama Jurnal*: `*Statistics and Computing*,`.
  4. *Volume, Isu, Artikel*: Pada jurnal Springer *Statistics and Computing*, SP (55) adalah nomor artikel. Format: `vol. 33, no. 2, Art. no. 55,`.
  5. *Tahun & DOI*: `2023, doi: 10.1007/s11222-023-10224-4.`.
  6. *Anchor*: Didahului oleh `<a id="ref35"></a>`.
- **Teks Awal**:
  ```markdown
  <a id="ref35"></a>
  [35] E. Redivo, C. Viroli, and A. Farcomeni, "Quantile-distribution functions and their use for classification, with application to naive Bayes classifiers," *Statistics and Computing*, vol. 33, no. 2, Art. no. 55, 2023, doi: 10.1007/s11222-023-10224-4.
  ```
- **Teks Hasil Perbaikan**:
  ```markdown
  <a id="ref35"></a>
  [35] E. Redivo, C. Viroli, and A. Farcomeni, "Quantile-distribution functions and their use for classification, with application to naïve Bayes classifiers," *Statistics and Computing*, vol. 33, no. 2, Art. no. 55, 2023, doi: 10.1007/s11222-023-10224-4.
  ```

---

## 3. Teks Perbaikan Final untuk Bagian [31] - [35]

Berikut adalah teks utuh referensi nomor [31] sampai [35] yang telah diperbaiki dan diverifikasi:

```markdown
<a id="ref31"></a>
[31] C. Zhao et al., "BoostTree and BoostForest for ensemble learning," *IEEE Transactions on Pattern Analysis and Machine Intelligence*, vol. 45, no. 7, pp. 8110-8126, 2023, doi: 10.1109/TPAMI.2022.3227370.

<a id="ref32"></a>
[32] Y.-X. He, S.-H. Lyu, and Y. Jiang, "Interpreting deep forest through feature contribution and MDI feature importance," *ACM Transactions on Knowledge Discovery from Data*, vol. 20, no. 1, Art. no. 15, 2025, doi: 10.1145/3641108.

<a id="ref33"></a>
[33] N. Zhu, C. Zhu, L. Zhou, Y. Zhu, and X. Zhang, "Optimization of the random forest hyperparameters for power industrial control systems intrusion detection using an improved grid search algorithm," *Applied Sciences*, vol. 12, no. 20, Art. no. 10456, 2022, doi: 10.3390/app122010456.

<a id="ref34"></a>
[34] J. Chen, X. Wang, and F. Lei, "Data-driven multinomial random forest: a new random forest variant with strong consistency," *Journal of Big Data*, vol. 11, no. 1, Art. no. 34, 2024, doi: 10.1186/s40537-023-00874-6.

<a id="ref35"></a>
[35] E. Redivo, C. Viroli, and A. Farcomeni, "Quantile-distribution functions and their use for classification, with application to naïve Bayes classifiers," *Statistics and Computing*, vol. 33, no. 2, Art. no. 55, 2023, doi: 10.1007/s11222-023-10224-4.
```

---

## 4. Verifikasi Pembatasan Karakter dan Kata

- Penggunaan tanda hubung em dash (`—`): **Nihil** (seluruh rentang menggunakan tanda hubung biasa `-`).
- Penggunaan kata terlarang (`kendati`, `paradigma`, `guna`): **Nihil**.
- Keberadaan jangkar HTML (`<a id="refX"></a>`): **Lengkap** untuk seluruh entri [31] sampai [35].
- Struktur DOI: **Sesuai** dengan format `doi: 10.xxxx/...` (tanpa protokol `https://doi.org/`).
