# DOKUMENTASI SESI KERJA OPENCODE
**Nama Berkas**: `sessions/session_2026-09-08_opencode_audit-referensi-dan-sitasi-naskah.md`  
**Tanggal**: 08 September 2026  
**Workspace**: `D:\Research\face-race-gender-classification-using-multi-domain-vit`  
**Konteks Repositori**: `rafyakbar/face-race-gender-classification-using-multi-domain-vit`  
**Target Publikasi**: IEEE Access (Template resmi `ieeeaccess.cls`, format 13 halaman)  
**Agen**: OpenCode (Omen Alpha)

---

## 1. IKHTISAR DAN TUJUAN UTAMA SESI

Sesi kerja pada 08 September 2026 difokuskan pada tiga tahap audit menyeluruh yang saling berkaitan atas sistem referensi ilmiah naskah, seluruhnya didelegasikan ke subagent paralel dengan aturan ketat satu subagent untuk satu cakupan tugas:

1. **Audit Ulang Entri Bibliografi (`paper/06_references.md`)**:
   - Mengaudit ulang seluruh 51 entri referensi berdasarkan koleksi berkas asli di `paper/references/` (51 berkas `.bib`, `.ris`, `.nbib`, `.bibtex`), registri `paper/references.txt`, dan panduan `rules/IEEE_citation_guidelines.md`.
   - Verifikasi metadata field-by-field: penulis, judul, jurnal/konferensi, volume, nomor, halaman/article number, bulan, tahun, DOI.
   - Verifikasi aturan penulis (lebih dari 6 penulis menggunakan *et al.*; 6 atau kurang ditulis seluruhnya) serta format IEEE (inisial-nama keluarga, judul dalam tanda kutip *sentence-case*, nama jurnal miring, vol./no./pp./Art. no., tahun, doi).
2. **Audit Konsistensi Bulan/Tanggal Terbit (Month/Date Consistency)**:
   - Memastikan setiap bulan yang muncul pada entri benar-benar didukung oleh berkas sumber dan sesuai template jurnal (`Mon. year`) versus konferensi (tahun saja) pada panduan IEEE.
   - Menambahkan bulan yang tersedia di sumber namun terlewat, serta menolak penambahan bulan yang tidak didukung sumber (tidak merekayasa data).
3. **Audit Ulang Nomor Referensi pada Seluruh Kalimat Klaim (`paper/*.md`)**:
   - Memverifikasi seluruh tautan sitasi interaktif `[[N]](06_references.md#refN)` pada 12 berkas naskah berklaim terhadap pemetaan `paper/references.txt`.
   - Memastikan format, posisi (sebelum tanda baca/pemisah tabel), reuse nomor untuk sumber yang sama, urutan kemunculan pertama yang menaik, serta ketiadaan sitasi yang hilang/salah nomor pada seluruh korpus naskah.
4. **Perubahan Pola Penamaan Berkas Sesi (`sessions/`) dan Pembaruan Dokumentasi**:
   - Mengubah pola nama seluruh berkas sesi menjadi `session_TAHUN-BULAN-TANGGAL_NAMAAGENT_judul-session.md` (tanggal terlebih dahulu, kemudian nama agen).
   - Memutakhirkan seluruh referensi berkas sesi pada `folder_structure.txt`, `README.md`, `README.AI.md`, serta metadata `Nama Berkas` di dalam tiap berkas sesi.
5. **Sinkronisasi Penuh `paper_latex_id/` dengan `paper/`**:
   - Memperluas `references.bib` dari 11 menjadi 51 entri (kunci `ref1` s.d. `ref51`) dan menyinkronkan 20 berkas section LaTeX terhadap 19 berkas Markdown ground truth melalui 21 subagent paralel.
   - Memverifikasi kesamaan template terhadap proyek referensi `chexnet-raddino-medical-captioning\paper_latex_id` dan mengompilasi ulang `access.pdf` (14 halaman).
6. **Audit Konformansi Template Asli IEEE Access (`template/ACCESS_latex_template_20260513`)**:
   - Membandingkan seluruh berkas pendukung `paper_latex_id/` dengan template asli IEEE Access (hash MD5), mengaudit struktur dokumen, dan memperbaiki deviasi yang ditemukan.
7. **Normalisasi Format Metrik Performa ke Persentase**:
   - Mengaudit dan mengonversi seluruh nilai Accuracy/Precision/Recall/F1-Score menjadi format persentase tunggal (menghapus format ganda `93.69% (0.9369)` dan mengonversi desimal murni) pada `paper_outline.md`, `paper/*.md`, dan `paper_latex_id/sections/*.tex` melalui 11 subagent paralel (satu berkas satu subagent).
8. **Penyempurnaan Layout Manuskrip LaTeX**:
   - Menyamakan tinggi citra Figure 2 (regenerasi komposit `sample_demogpairs.png` dengan susunan asli 1 baris × 6 kolom), menghapus bold Table II, menggabungkan baris Total Grid Combinations Tables III-VI (`\multicolumn{2}{r}`), menyederhanakan label Table XII menjadi `Ours` + single column, serta menghapus tautan ORCID pada biografi (`07_biographies.tex` + md).
9. **Normalisasi INDEX TERMS dan Kata Pertama Introduction**:
   - Menyamakan pemisah kata kunci ke koma sesuai instruksi template, dan menyaring usage `\PARstart` sesuai preferensi pengguna (akhirnya kata pertama Introduction ditulis normal).

---

## 2. KRONOLOGI PERMINTAAN PENGGUNA & TINDAKAN YANG DIAMBIL

### A. Persiapan dan Pemetaan Acuan Audit
* **Permintaan Pengguna**: Mengaudit ulang `paper/06_references.md` berdasarkan `paper/references.txt` dan `paper/references/` dengan aturan ketat sesuai `rules/IEEE_citation_guidelines.md`, urutan entri [1] s.d. [N] persis mengikuti kemunculan pertama setiap berkas pada `paper/references.txt`, pemeriksaan metadata satu per satu, aturan penulis, format sitasi, pencegahan karakter terlarang, dan pendelegasian paralel dengan alokasi satu rentang nomor per subagent.
* **Tindakan yang Diambil**:
  - Membaca `rules/IEEE_citation_guidelines.md` (331 baris) sebagai acuan format utama.
  - Membaca `paper/references.txt` (209 baris) dan memetakan urutan kemunculan pertama seluruh 51 berkas sumber ke entri [1] s.d. [51]; hasil: pemetaan **cocok sempurna** dengan penomoran yang ada.
  - Memverifikasi inventaris `paper/references/`: tepat 51 berkas, semuanya terpetakan (tidak ada berkas tanpa rujukan, tidak ada entri tanpa berkas sumber).
  - Membaca `paper/06_references.md` (154 baris) sebagai baseline audit.

### B. Audit Paralel Entri [1] s.d. [51] oleh 10 Subagent
* **Delegasi**: 10 subagent independen dengan alokasi rentang: [1]-[5], [6]-[10], [11]-[15], [16]-[20], [21]-[25], [26]-[30], [31]-[35], [36]-[40], [41]-[45], [46]-[51]. Setiap subagent hanya boleh memodifikasi baris entri pada rentangnya sendiri.
* **Hasil Verifikasi (PASS tanpa koreksi)**:
  - Aturan penulis terkonfirmasi dari sumber: [2] 9 penulis → et al.; [5] 8 → et al.; [7] 9 → et al.; [10] 8 → et al.; [31] 7 → et al.; [47] 7 → et al.; [48] 7 → et al. (diakritik *Hanczár* terjaga); [49] 7 → et al.; entri 6 penulis ([12], [29], [36]) ditulis seluruhnya.
  - Format konferensi sesuai template: [14] ICCV (Paris), [19] ICVEE (Surabaya, Indonesia), [23] AAAI, [25] IEEE FG (Lille, France).
  - Semua DOI, vol./no./pp./Art. no. cocok karakter-per-karakter dengan berkas sumber.
* **Koreksi yang Diterapkan**:

| Entri | Perbaikan | Bukti Sumber |
|---|---|---|
| [1] | + `Jan. 2023` | RIS `DA - 2023/01/01` |
| [8] | + `Aug. 2022` | bib `month = aug` |
| [9] | + `Aug. 2023` | nbib `DEP - 20230808` |
| [20] | `multidomain` → `Multidomain` (kapital kata pertama setelah titik dua, aturan sentence-case IEEE) | konvensi sentence-case |
| [42] | Penulis `N. N. Y., T. V. Ly, and D. V. T. Son` → **`N.-Y. Nguyen, L. V. Tran, and V. T. S. Dao`**; + `May 2022`; `Support Vector Machines` → `support vector machines` (sentence-case) | BibTeX sumber malformed (`Y., Nguyen Nhu AND Ly, Tran Van AND Son, Dao Vu Truong`); diverifikasi silang ke halaman resmi PLOS ONE (doi: 10.1371/journal.pone.0267935, penulis terdaftar: *Nguyen Nhu Y., Tran Van Ly, Dao Vu Truong Son*) |
| [51] | Hapus elemen non-template `scikit-learn,` yang tidak ada di bib sumber (tidak merekayasa versi/tahun) | format software per guidelines; bib `2026_SVC.bib` |

* **Intervensi Manual Orkestrator (di luar subagent)**: Koreksi subagent rentang [41]-[45] atas entri [42] ditemukan keliru (subagent mengikuti field BibTeX yang malformed sehingga nama keluarga/nama depan tertukar menjadi `N. N. Y., T. V. Ly, and D. V. T. Son`). Orkestrator memverifikasi ke halaman resmi PLOS ONE via web search, mengonfirmasi nama keluarga sebenarnya adalah Nguyen/Tran/Dao, lalu memperbaiki langsung menjadi `N.-Y. Nguyen, L. V. Tran, and V. T. S. Dao`.

### C. Verifikasi Karakter/Kata Terlarang dan Integritas Struktur
* **Permintaan Pengguna**: Memastikan tidak ada karakter terlarang (em dash, `kendati`, `paradigma`, `guna`).
* **Tindakan yang Diambil** (skrip PowerShell):
  - Em dash (U+2014): **0 temuan**.
  - En dash (U+2013): **0 temuan**.
  - Double-hyphen (`--`): **0 temuan**.
  - `kendati`: **0 temuan**; `paradigma`: **0 temuan**; `\bguna\b` (standalone): **0 temuan**.
  - Jumlah entri: **51**; jumlah anchor `<a id="refN"></a>`: **51**; seluruh nomor [1] s.d. [51] hadir tanpa kekurangan.
  - `git diff`: 1 berkas berubah (`paper/06_references.md`, 18 baris dihapus + 18 baris ditambah).

### D. Audit Ulang Konsistensi Bulan/Tanggal oleh 10 Subagent
* **Permintaan Pengguna**: "Apakah memang references-nya ada bulannya? Apakah sudah sesuai dengan rules/IEEE_citation_guidelines.md?" dilanjutkan permintaan audit ulang via subagent.
* **Tindakan yang Diambil**:
  - Pemindaian langsung seluruh 51 berkas sumber untuk field tanggal (`month`, RIS `DA -`/`PY -`, nbib `DP -`/`DEP -`) via skrip PowerShell.
  - Delegasi ulang ke 10 subagent dengan aturan eksplisit: (1) entri yang sudah berbulan diverifikasi ke sumber; (2) entri jurnal tanpa bulan diberi bulan HANYA bila sumber memuat tanggal terbit yang konsisten dengan tahun entri; (3) tanggal epub dengan tahun berbeda dari tahun terbit resmi TIDAK ditambahkan; (4) entri konferensi tidak boleh berbulan sesuai template IEEE; (5) tanpa data sumber, bulan tidak direkayasa.
* **Hasil Verifikasi**:
  - **21 entri jurnal berbulan** terverifikasi cocok dengan sumber: [1] Jan. 2023 (`DA 2023/01/01`); [3] Oct. 2022 (`DP 2022 Oct`); [4] Sept. 2024 (`month={09}`); [5] Mar. 2022 (`month={March}`); [8] Aug. 2022 (`month=aug`); [9] Aug. 2023 (`DEP 20230808`, tahun sama dengan DP 2023, valid); [20] Dec. 2025 (`month={12}`); [26] Jan. 2026 (`DA 2026/01/16`); [27] Feb. 2023 (`DP 2023 Feb`); [32] Dec. 2025 (`month=dec`); [34] Feb. 2024 (`DA 2024/02/23`); [35] Mar. 2023 (`DA 2023/03/24`); [37] Dec. 2023 (`month={12}`); [42] May 2022 (`month={05}`); [43] Sept. 2023 (`DA 2023/09/01`); [44] Feb. 2023 (`DEP 20230214`, tahun sama, valid); [45] Aug. 2022 (`DA 2022/08/01`); [46] Mar. 2021 (`month={03}`); [47] Apr. 2022 (`DA 2022/04/08`); [48] Oct. 2023 (`month={oct}`); [50] Jan. 2023 (`month={01}`).
  - **23 entri jurnal tanpa bulan** terverifikasi disengaja: sumber tidak memuat field bulan sama sekali ([2], [6], [7], [10]-[13], [16]-[18], [22], [24], [28]-[31], [33], [36], [38]-[41], [49]) sesuai aturan panduan *"omit it rather than inventing one"*.
  - **Kasus khusus [21]**: sumber memiliki tanggal epub `DEP - 20220615` (2022), tetapi tahun terbit resmi 2023 (`DP - 2023`); bulan sengaja TIDAK ditambahkan agar tidak bertentangan dengan tahun entri.
  - **Entri konferensi tanpa bulan (disengaja, sesuai template konferensi)** meskipun sumber memuat bulan: [14] ICCV (`month={Oct}`), [19] ICVEE (`month={Sep.}`), [25] IEEE FG (`month={May}`).
  - **[51] software**: `[Accessed: Feb. 2, 2026]` cocok persis dengan field `note` pada `2026_SVC.bib`.
* **Koreksi Konsistensi yang Diterapkan** (bulan tersedia di sumber namun terlewat):

| Entri | Perbaikan | Bukti Sumber |
|---|---|---|
| [34] | + `Feb. 2024` | RIS `DA - 2024/02/23` |
| [35] | + `Mar. 2023` | RIS `DA - 2023/03/24` |
| [44] | + `Feb. 2023` | nbib `DEP - 20230214` |

### E. Audit Ulang Nomor Referensi pada Seluruh Kalimat Klaim `paper/*.md` oleh 13 Subagent
* **Permintaan Pengguna**: Mengaudit ulang nomor referensi pada seluruh kalimat klaim `paper/*.md` dengan aturan: format tautan interaktif `[[N]](06_references.md#refN)`, sitasi majemuk terpisah koma-spasi, nomor merujuk entri yang ada di `paper/06_references.md` (tanpa membuat nomor baru), reuse nomor untuk sumber yang sama, urutan kemunculan pertama menaik sesuai IEEE, posisi sebelum tanda baca, tanpa mengubah isi kalimat, dan delegasi satu subagent per satu berkas.
* **Delegasi**: 12 subagent untuk 12 berkas berklaim (sesuai pemetaan `paper/references.txt`) + 1 subagent sweep untuk 7 berkas tanpa klaim:
  1. `01_introduction.md`: 16 kalimat klaim, 33 tautan sitasi ([1] s.d. [24], reuse [9], [11]-[13], [17]-[20]) — **semua cocok, 0 koreksi**.
  2. `02_related-works.md`: 15 kalimat klaim, 17 tautan ([11] s.d. [20], reuse [11]-[14], [16]) — **semua cocok, 0 koreksi**.
  3. `03_materials-and-methods_a-dataset.md`: 2 klaim, 2 tautan ([25], [20]) — **cocok**.
  4. `03_materials-and-methods_b-vision-transformer.md`: 5 klaim, 5 tautan ([26]-[29]; [27] dipakai ulang 2x) — **cocok**; rujukan persamaan `[(1)](#eq1)` s.d. `[(5)](#eq5)` diidentifikasi sebagai rujukan persamaan (bukan sitasi) dan tidak disentuh.
  5. `03_materials-and-methods_c-random-forest.md`: 5 klaim, 5 tautan ([30]-[34]) — **cocok**.
  6. `03_materials-and-methods_d-gaussian-naive-bayes.md`: 3 klaim, 3 tautan ([35] 2x, [36]) — **cocok**.
  7. `03_materials-and-methods_e-logistic-regression.md`: 3 klaim, 3 tautan ([37]-[39]) — **cocok**.
  8. `03_materials-and-methods_f-support-vector-machine.md`: 4 klaim, 4 tautan ([40]-[43]) — **cocok**.
  9. `03_materials-and-methods_h-evaluation-metrics.md`: 5 klaim, 5 tautan ([44]-[47]; [47] 2x) — **cocok**.
  10. `04_results-and-discussion_a-global-performance.md`: 4 klaim, 4 tautan ([48]-[51]) — **cocok**.
  11. `04_results-and-discussion_d-error-pattern-assessment.md`: 1 klaim, 1 tautan ([18]) — **cocok**.
  12. `04_results-and-discussion_e-comparison-with-prior-studies.md`: 5 klaim + Table XII, 7 tautan ([19], [20], [25]; posisi sebelum pemisah kolom ` |` benar) — **cocok**.
  13. Sweep 7 berkas tanpa klaim (`00_abstract.md`, `03_materials-and-methods_0-overview.md`, `03_materials-and-methods_g-classification-pipeline.md`, `04_results-and-discussion_b-feature-ablation-study.md`, `04_results-and-discussion_c-intersectional-subgroup-performance.md`, `05_conclusion.md`, `07_biographies.md`) — **semua bersih**: tidak ada tautan sitasi yatim, tidak ada penanda sitasi format lama, tidak ada klaim literatur tanpa sitasi.
* **Verifikasi Global Otomatis (Skrip PowerShell)**:
  - Total tautan sitasi interaktif di seluruh korpus naskah: **91**.
  - Nomor unik yang digunakan: **51 dari 51** (seluruh entri [1] s.d. [51] tersitasi; tidak ada nomor di luar rentang; tidak ada entri tak terpakai).
  - Pelanggaran urutan kemunculan pertama (monotonik menaik): **0**.
  - Grep anomali format (tautan rusak, koma ganda, spasi hilang, sitasi author-year tersisa): **0 temuan**.
* **Catatan Temuan Opsional (tidak diedit, menunggu keputusan pengguna)**:
  - `02_related-works.md` baris 3: kalimat *"Selain itu, mekanisme berbagi fitur paralel dengan atensi visual dikembangkan untuk menangkap keterkaitan antaratribut wajah sekaligus mengurangi keterbatasan representasi lokal."* mendeskripsikan metode dari [16] tetapi tidak memiliki tautan sitasi. Registri `paper/references.txt` hanya memetakan kalimat berikutnya ("Pendekatan ini menunjukkan pergeseran...") ke [16]. Karena tercakup kontekstual oleh `[[16]]` pada kalimat sesudahnya, statusnya wajar tanpa sitasi; opsi penambahan `[[16]]` ditawarkan kepada pengguna.

### F. Perubahan Pola Penamaan Berkas Sesi dan Pembaruan Dokumentasi
* **Permintaan Pengguna**: Mengubah pola nama berkas sesi menjadi `session_tahun-bulan-tanggal_namaagent_judul-session.md` dan memutakhirkan berkas yang diperlukan (`folder_structure.txt`, README, dll.).
* **Tindakan yang Diambil**:
  - Rename 4 berkas sesi (`git mv` untuk 3 berkas terlacak; rename biasa untuk 1 berkas baru):
    * `session_agy_2026-09-06_audit-paper-dan-sinkronisasi-latex-id.md` → `session_2026-09-06_agy_audit-paper-dan-sinkronisasi-latex-id.md`
    * `session_agy_2026-09-07_audit-sitasi-dan-pembaruan-dokumentasi-sistem.md` → `session_2026-09-07_agy_audit-sitasi-dan-pembaruan-dokumentasi-sistem.md`
    * `session_agy_2026-09-08_standardisasi-ieee-dan-sitasi-interaktif-manuskrip.md` → `session_2026-09-08_agy_standardisasi-ieee-dan-sitasi-interaktif-manuskrip.md`
    * `session_opencode_2026-09-08_audit-referensi-dan-sitasi-naskah.md` → `session_2026-09-08_opencode_audit-referensi-dan-sitasi-naskah.md`
  - Memperbarui baris metadata `**Nama Berkas**` di dalam keempat berkas sesi.
  - Memperbarui `folder_structure.txt`: pohon direktori `sessions/` (4 berkas) dan glosarium Direktori `sessions/` (ditambah entri sesi opencode).
  - Memperbarui `README.md` dan `README.AI.md`: pola glob `session_agy_*.md` → `session_*.md` dengan keterangan pola `session_YYYY-MM-DD_agent_title`.
  - Dua pengecualian yang sengaja tidak diubah: `prompts.txt` baris 66 (teks prompt historis pengguna, berkas terproteksi) dan blok `git status` historis pada sesi 06 September (catatan keadaan repo saat itu).

### G. Sinkronisasi Penuh `paper_latex_id/` dengan `paper/` (21 Subagent)
* **Permintaan Pengguna**: Memastikan isi `paper_latex_id` sama dengan `paper`; cek dahulu berkas section yang ada, lalu delegasikan ke subagent, satu berkas satu subagent.
* **Inventarisasi Awal**:
  - `paper_latex_id/sections/` memuat 20 berkas `.tex` (00_title s.d. 07_biographies), seluruhnya di-input oleh `access.tex` — pemetaan 1:1 dengan 19 berkas Markdown (+ `00_title.tex` yang padanannya berada pada metadata judul/penulis `00_abstract.md` dan `authors.txt`).
  - **Gap kritis**: `references.bib` hanya memuat 11 entri (`ref1`-`ref11`), sedangkan `paper/06_references.md` telah diperluas menjadi 51 entri.
* **Delegasi Gelombang 1 (11 subagent)**:
  1. `references.bib`: 11 → **51 entri** (`ref1` s.d. `ref51`, tanpa gap/duplikat). Kunci lama `ref1`-`ref11` ternyata menunjuk sumber yang salah setelah restrukturisasi penomoran, seluruhnya dipetakan ulang (ref1→ref11, ref2→ref12, ... ref10→ref20, ref11→ref25); metadata `ref18` diperbaiki (`Kalkatawi, Manal` → `Kalkatawi, A.-A.`); konvensi brace-protection akronim ({MD-ViT}, {ViT}, {RFMS}, {HIV}, {DemogPairs}, {Balanced Faces in the Wild}, {SVC}, dll.) dan `pages` dengan `--` dipertahankan; entri [51] sebagai `@misc` dengan `howpublished` URL + `note` Accessed.
  2. `00_title.tex`: sudah sinkron (judul, urutan 4 penulis Putra-Putri-Yamasari-Akbar, ORCID, afiliasi) - 0 koreksi.
  3. `00_abstract.tex`: teks abstrak sudah sinkron kata-per-kata; pemisah kata kunci `,` → `;` disesuaikan dengan md (5 kata kunci).
  4. `01_introduction.tex`: **penulisan ulang besar** - narasi lama yang parafrasif disamakan kata-per-kata dengan md (7 paragraf); sitasi lama `ref1`-`ref10` di P3/P4 dinomori ulang ke `ref11`-`ref24` sesuai pemetaan teraudit; 33 instance `\cite` final.
  5. `02_related-works.tex`: 6 paragraf disamakan verbatim; sitasi `ref11`-`ref20` (17 instance); kalimat tanpa sitasi sengaja dipertahankan sesuai md.
  6. `03_materials-and-methods_0-overview.tex`: 1 koreksi kata ("resolusi" berlebih dihapus).
  7. `03_materials-and-methods_a-dataset.tex`: `ref11` → `ref25`, tambah `ref20`; nama subgrup `Black\_Males` dll. diselaraskan dengan md.
  8. `03_materials-and-methods_b-vision-transformer.tex`: +5 sitasi (`ref26`, `ref27` 2x, `ref28`, `ref29`); struktur paragraf-ekuasi diurut ulang sesuai md; rujukan persamaan `eq:1`-`eq:5` dipertahankan.
  9. `03_materials-and-methods_c-random-forest.tex`: +5 sitasi (`ref30`-`ref34`).
  10. `03_materials-and-methods_d-gaussian-naive-bayes.tex`: +3 sitasi (`ref35` 2x, `ref36`).
  11. `03_materials-and-methods_e-logistic-regression.tex`: +3 sitasi (`ref37`-`ref39`).
* **Delegasi Gelombang 2 (10 subagent)**:
  12. `03_materials-and-methods_f-support-vector-machine.tex`: +4 sitasi (`ref40`-`ref43`).
  13. `03_materials-and-methods_g-classification-pipeline.tex`: sudah sinkron; tanpa sitasi (benar, sesuai md).
  14. `03_materials-and-methods_h-evaluation-metrics.tex`: narasi direstrukturisasi sesuai md (paragraf mendahului ekuasi 10-13); +5 sitasi (`ref44`-`ref47`, `ref47` 2x).
  15. `04_results-and-discussion_a-global-performance.tex`: narasi RF/GNB/LR/SVM dipadatkan sesuai md; +4 sitasi (`ref48`-`ref51`); Tables VII-X (28 baris, sel multi-baris) sudah cocok.
  16. `04_results-and-discussion_b-feature-ablation-study.tex`: sudah sinkron penuh - 0 koreksi.
  17. `04_results-and-discussion_c-intersectional-subgroup-performance.tex`: sudah sinkron penuh (Table XI, 24 baris data, nilai disparitas, kata peringatan OvR 5:1) - 0 koreksi.
  18. `04_results-and-discussion_d-error-pattern-assessment.tex`: +1 sitasi (`ref18`).
  19. `04_results-and-discussion_e-comparison-with-prior-studies.tex`: sitasi tabel `ref9`/`ref10` → `ref19`/`ref20`; +5 sitasi teks (`ref19` 4x, `ref20` 4x, `ref25` 1x); atribusi naratif "oleh Putri et al." diganti sitasi numerik IEEE.
  20. `05_conclusion.tex`: sudah sinkron penuh - 0 koreksi.
  21. `07_biographies.tex`: sudah sinkron penuh (4 biografi, foto, ORCID terverifikasi) - 0 koreksi.

### H. Verifikasi Template dan Kompilasi Ulang Manuskrip
* **Permintaan Pengguna**: Jika ada error saat build LaTeX, cek `D:\Research\chexnet-raddino-medical-captioning\paper_latex_id` apakah template sudah sama.
* **Tindakan yang Diambil**:
  - Perbandingan template: `ieeeaccess.cls` dan `IEEEtran.bst` **identik** (hash sama) antara kedua proyek; tidak ada berkas pendukung yang hilang (perbedaan hanya berkas konten/aset).
  - **Perbandingan overfull box**: build proyek referensi sendiri menghasilkan 39x overfull `505.12177pt` yang identik - terbukti artefak kosmetik bawaan *output routine* kelas `ieeeaccess` (juga 2x `9.2679pt` identik), **bukan error dan bukan akibat konten**.
  - Isolasi diagnostik: kompilasi uji dengan `references.bib` versi HEAD mengonfirmasi artefak 505pt sudah ada sebelumnya (27x).
  - **Satu overfull nyata ditemukan dan diperbaiki**: nama checkpoint HuggingFace panjang `dima806/facial\_emotions\_image\_detection` pada `03_materials-and-methods_b-vision-transformer.tex` (86.96277pt) diberi titik putih `\allowbreak` (tanpa mengubah isi; nama checkpoint memang ada di md dalam *inline code*).
  - Kompilasi final `pdflatex` → `bibtex` → `pdflatex` → `pdflatex`: **PASS, 14 halaman** (naik dari 13 karena referensi bertambah 20→51), 0 undefined citations/references, 0 BibTeX warnings.

### I. Audit Konformansi Template Asli IEEE Access
* **Permintaan Pengguna**: `template/ACCESS_latex_template_20260513` adalah template asli IEEE Access; `paper_latex_id` adalah pemecahannya menjadi berkas section — audit apakah template sudah sama.
* **Tindakan yang Diambil**:
  - Perbandingan hash seluruh berkas pendukung: `ieeeaccess.cls`, `IEEEtran.bst`, `IEEEtran.cls`, `spotcolor.sty`, 22 font `.pfb`, 16 `.tfm`, 4 `.map`, 4 `.fd`, serta aset `bullet.png`/`logo.png`/`notaglinelogo.png` — **semua identik konten**; satu-satunya perbedaan adalah penambahan line-ending CRLF (selisih byte = jumlah baris persis).
  - Aset demo template (`author1-3.png`, `equation3.png`, `fig1.png`) absen dengan benar (kita memakai `images/` sendiri).
  - Struktur dokumen terpreservasi penuh: `\documentclass`, `\history`, `\doi`, `\title`, `\author`, `\address`, `\tfootnote`, `\markboth`, `\corresp`, abstract, keywords, `\titlepgskip`, `\maketitle`, `\bibliographystyle{IEEEtran}`, biografi, `\EOD`.
  - Modifikasi sadar terdokumentasi: `\usepackage{cite}` diganti custom `\@citex` hyperlinked (kutipan biru berklik), +`hyperref`/`booktabs`/`tabularx`/`multirow`/`subfigure`/`url`, custom `\eqref`, `\graphicspath{{images/}}`, superskrip ORCID menggantikan `\authorrefmark`+`\IEEEmembership`.
  - **Deviasi diperbaiki**: `\PARstart` (drop-cap) hilang pada Introduction → ditambahkan `\PARstart{P}{engenalan}`; kompilasi PASS.
  - **Deviasi dilaporkan (menunggu keputusan)**: `\section*{Acknowledgment}` tidak ada (naskah md juga tidak memuatnya — keputusan konten).

### J. Normalisasi INDEX TERMS
* **Permintaan Pengguna**: Cek apakah INDEX TERMS sudah sesuai style template asli.
* **Tindakan yang Diambil**:
  - Mekanisme render identik (environment `keywords` + cls yang sama menampilkan heading "INDEX TERMS" biru dengan bullet) — diverifikasi via `pdftotext` halaman 1 kedua PDF.
  - Deviasi: template menginstruksikan *"separated by commas"* sedangkan naskah memakai titik koma (warisan md).
  - **Diterapkan**: pemisah kata kunci `;` → `,` pada `paper/00_abstract.md` + `paper_latex_id/sections/00_abstract.tex` (urutan dipertahankan sesuai md; opsi pengurutan alfabetis tetap terbuka).
  - Recompile PASS; render terverifikasi: `INDEX TERMS Race and gender classification, intersectional demographic recognition, ...`.

### K. Kata Pertama Introduction
* **Permintaan Pengguna**: Kata pertama Introduction tidak usah huruf besar (drop-cap), buat biasa saja.
* **Tindakan yang Diambil**: `\PARstart{P}{engenalan}` yang sebelumnya ditambahkan untuk konforman template dihapus → "Pengenalan otomatis..." ditulis normal; recompile PASS (terverifikasi via `pdftotext`).

### L. Normalisasi Format Metrik ke Persentase (11 Subagent)
* **Permintaan Pengguna**: Metrik Accuracy hingga F1-Score harus memakai persentase saja; tidak perlu format ganda seperti `93.69% (0.9369)`. Delegasikan ke subagent, satu subagent satu berkas.
* **Konfirmasi kepada Pengguna (dijawab)**: tabel VII-XII ikut dikonversi ke %; `paper_outline.md` ikut dinormalisasi; berkas tanpa metrik (51 berkas sumber `paper/references/`, `ref_part_*.md`, dll.) diverifikasi via pemindaian pola rg oleh agen utama.
* **Delegasi (11 subagent paralel, semua berhasil)**:
  1. `paper_outline.md`: 9 lokasi narasi + 6 tabel benchmark (VII-XII) → % (termasuk `(0.8685)`→`(86.85%)`, rentang `0.9174 s.d. 0.9614`→`91.74% s.d. 96.14%`, rata-rata `$\text{SVM }(0.9147)$`→`(91.47%)`).
  2. `04_results-and-discussion_a-global-performance.md`: 112 sel (4 tabel × 28 baris) → %.
  3. `04_results-and-discussion_a-global-performance.tex`: 112 sel → `\%` ter-escape; struktur `\textbf`/tabular utuh.
  4-5. `04_results-and-discussion_b-feature-ablation-study.md` + `.tex`: hapus `(0.0246)`, `(0.0287)`, `(0.0172)`.
  6-7. `04_results-and-discussion_c-intersectional-subgroup-performance.md` + `.tex`: 36/24 sel Table XI (Precision/Recall/F1) → %; hapus `(0.0440)`, `(0.0422)`; `1.39 pp` dan rasio `5:1` tidak disentuh.
  8-9. `04_results-and-discussion_e-comparison-with-prior-studies.md` + `.tex`: 9 sel Table XII → %; narasi `Presisi 0.9372` → `93.72%` dst.
  10-11. `05_conclusion.md` + `.tex`: hapus `(0.9369)` dan `(0.9174 hingga 0.9614)`.
* **Verifikasi Agen Utama**: 0 sisa pola `% (0.xxxx)`; desimal tersisa hanya hyperparameter (`PCA 0.50/0.75`, `C=0.1`, `coef0=0.0`, `var_smoothing`), lebar figure, DOI; recompile PASS 14 halaman.

### M. Penyempurnaan Layout `paper_latex_id`
* **Permintaan Pengguna**: (1) citra Figure 2 tinggi sama; (2) Table 2 tanpa bold; (3) Tables 3-6 baris Total Grid Combinations merge 2 kolom align right; (4) Table 12 label `Ours` dan tidak full width.
* **Tindakan yang Diambil**:
  - **Figure 2 (2 iterasi)**: iterasi 1 mengganti gambar komposit dengan grid subfigure 3×2 (`height=4.5cm, keepaspectratio`); atas koreksi pengguna *"jangan mengubah susunan citra"*, dikembalikan ke tampilan single image dan **`images/sample_demogpairs.png` diregenerasi** (3225×620 px) via PowerShell System.Drawing dari 6 JPG sumber dengan tinggi seragam 500 px — susunan asli 1 baris × 6 kolom dan label tebal (a)-(f) di atas citra dipertahankan persis; spesifikasi layout di `paper_outline.md` dikoreksi (grid 3×2 → komposit full width 1×6 tinggi seragam).
  - **Table II**: `\textbf{Tri-Domain (Proposed)}`/`\textbf{2,304}` → tanpa bold di tex, disinkronkan ke `03_...b-vision-transformer.md` dan `paper_outline.md`.
  - **Tables III/IV/V/VI**: baris Total Grid Combinations → `\multicolumn{2}{r}{\textbf{Total Grid Combinations}} & \textbf{288 (1,440 fits)}` (merge 2 kolom, align right; bold dipertahankan).
  - **Table XII**: `\textbf{Ours (Tri-Domain ViT + SVM)}` → `\textbf{Ours}`; `table*` → `table` (single column); `paper_outline.md` disamakan ke `**Ours**` (md memang sudah `Ours`).
  - Recompile PASS; bonus: ukuran PDF 3.62 MB → 2.28 MB (kembali 5.45 MB setelah PNG komposit resolusi tinggi) dan overfull 1.6pt hilang.

### N. Penghapusan Tautan ORCID pada Biografi
* **Permintaan Pengguna**: `07_biographies.tex` tidak usah ada link ORCID pada biografi karena sudah ada di atas.
* **Tindakan yang Diambil**: kalimat penutup berisi tautan ORCID dihapus dari keempat biografi (Ricky, Rezky, Yuni, Rafy) di `07_biographies.tex` dan disinkronkan ke `paper/07_biographies.md`; ORCID pada outline baris 62-65 (bagian Authors) dipertahankan. Verifikasi: 0 sisa `ORCID` di kedua berkas biografi; 4 superskrip ORCID tetap utuh di `00_title.tex`; recompile PASS.

---

## 3. ARSITEKTUR VERIFIKASI TIGA LAPIS

Sesi ini menuntaskan verifikasi integritas tiga lapis sistem sitasi:

```
[Lapis 1: Berkas Sumber Primer - paper/references/ (51 berkas)]
  └── Metadata asli: penulis, judul, jurnal, vol/no/pp/Art. no., month/year, DOI
        │  (audit field-by-field oleh 10 subagent rentang [1]-[51])
        ▼
[Lapis 2: Daftar Pustaka - paper/06_references.md (entri [1]-[51])]
  └── 51 anchor <a id="refN"></a>; format IEEE sesuai rules/IEEE_citation_guidelines.md
        │  (audit tautan interaktif oleh 13 subagent per berkas naskah)
        ▼
[Lapis 3: Kalimat Klaim Naskah - paper/*.md (91 tautan sitasi interaktif)]
  └── Format [[N]](06_references.md#refN); urutan kemunculan pertama menaik; reuse konsisten
        │
        ▼
[Registri Audit: paper/references.txt - pemetaan kalimat → berkas sumber]
```

Lapis 1-3 di atas menjamin integritas naskah Markdown. Setelah sinkronisasi, rantai verifikasi diperluas ke lapis publikasi LaTeX:

```
[Lapis 4: Bibliografi BibTeX - paper_latex_id/references.bib (51 entri ref1-ref51)]
  └── Metadata disamakan dengan entri [1]-[51] pada paper/06_references.md
        │  (audit \cite{refN} per section oleh 21 subagent)
        ▼
[Lapis 5: Manuskrip LaTeX - paper_latex_id/sections/*.tex (20 berkas) → access.pdf (14 hal)]
  └── 91 instance \cite{refN} = persis 91 tautan sitasi Markdown; 0 undefined; kompilasi PASS
```

---

## 4. REKAPITULASI MODIFIKASI BERKAS SESI INI

| Berkas | Status | Ringkasan Perubahan |
|---|---|---|
| `paper/06_references.md` | Dimodifikasi | 21 baris diperbarui: penambahan bulan pada [1], [8], [9], [34], [35], [44]; koreksi penulis [42] (+ `May 2022`, sentence-case); kapitalisasi [20]; pembersihan format [51]. Seluruh perubahan terverifikasi terhadap berkas sumber. |
| `paper/*.md` naskah lainnya | Dimodifikasi (8 berkas) | 00_abstract (pemisah keywords `,`), 03b (unbold Table II), 04a/04b/04c/04e/05 (normalisasi metrik → %), 07_biographies (hapus kalimat ORCID). 13 berkas naskah lainnya tidak berubah; 91 tautan sitasi tetap terverifikasi benar. |
| `paper_outline.md` | Dimodifikasi | Normalisasi metrik (9 narasi + 6 tabel → %), unbold Table II, label `Ours` Table XII, spesifikasi layout Figure 2 dikoreksi (komposit 1×6 tinggi seragam). |
| `paper_latex_id/images/sample_demogpairs.png` | Diregenerasi | 3225×620 px dari 6 JPG sumber, tinggi seragam 500 px, susunan 1×6 + label (a)-(f) di atas dipertahankan. |
| `paper_latex_id/references.bib` | Dimodifikasi | 11 → 51 entri (`ref1`-`ref51`); remapping kunci lama; perbaikan metadata `ref18`; konvensi brace-protection dan `pages` dengan `--` dipertahankan. |
| `paper_latex_id/sections/*.tex` | Dimodifikasi (18 dari 20) | 00_abstract (keywords `,`), 01_introduction (rewrite + renumber sitasi + kata pertama normal), 02_related-works (verbatim sync), 03_0 (1 kata), 03a (sitasi + nama subgrup), 03b (5 sitasi, `\allowbreak`, unbold Table II), 03c/03d/03e/03f (15 sitasi + multicolumn Total Grid), 03h (restrukturisasi + 5 sitasi), 04a (112 sel % + 4 sitasi + narasi), 04b/04c (metrik % + hapus format ganda), 04d (1 sitasi), 04e (9 sel % + label Ours + single column), 05 (metrik %), 07 (hapus ORCID). 03g dan 00_title tidak berubah. |
| `paper_latex_id/access.pdf` (+ aux/log/bbl/out) | Dimodifikasi | Hasil kompilasi ulang berkali-kali sepanjang sesi: 14 halaman, 0 undefined citations/references, 0 BibTeX warnings. |
| `sessions/*.md` (4 berkas) | Di-rename + metadata | Pola baru `session_YYYY-MM-DD_agent_title.md`; baris `Nama Berkas` diperbarui di tiap berkas. |
| `folder_structure.txt` | Dimodifikasi | Pohon `sessions/` (4 berkas) + glosarium (entri sesi opencode ditambahkan). |
| `README.md`, `README.AI.md` | Dimodifikasi | Pola glob `session_agy_*.md` → `session_*.md` + keterangan pola `session_YYYY-MM-DD_agent_title`. |

* **Tidak diubah (sengaja)**: `prompts.txt` baris 66 (teks prompt historis pengguna, berkas terproteksi) dan blok `git status` historis pada sesi 06 September.
* **Status Git**: Perubahan BELUM di-commit (menunggu instruksi pengguna). Working tree menampilkan: `paper_outline.md`, `paper/` (06_references + 8 naskah), `paper_latex_id/` (bib, 18 sections, images/sample_demogpairs.png, pdf), `README.md`, `README.AI.md`, `folder_structure.txt`, rename 3 berkas sesi terlacak, dan 1 berkas sesi opencode baru (untracked). Catatan: `prompts.txt` juga tampil termodifikasi di working tree, bukan akibat tindakan sesi ini.

---

## 5. HASIL VERIFIKASI AKHIR & INTEGRITAS SISTEM

1. **Kelengkapan Pemetaan**: 51 berkas sumber ↔ 51 entri `paper/06_references.md` ↔ urutan kemunculan pertama `paper/references.txt` — cocok sempurna tanpa berkas yatim atau entri tanpa sumber.
2. **Kepatuhan Format IEEE**: Seluruh entri mengikuti template artikel jurnal/konferensi/software pada `rules/IEEE_citation_guidelines.md`.
3. **Konsistensi Bulan**: 21 entri jurnal berbulan (semua berdasar sumber), 23 entri jurnal tanpa bulan (sumber tidak menyediakan), 3 entri konferensi tanpa bulan (template), 1 entri software dengan Accessed date.
4. **Integritas Sitasi Naskah**: 91 tautan interaktif, 51/51 entri tersitasi, 0 pelanggaran urutan, 0 sitasi salah nomor, 0 sitasi hilang pada klaim terpetakan.
5. **Kebersihan Kosakata/Karakter**: Em dash, en dash, double-hyphen, `kendati`, `paradigma`, standalone `guna` — seluruhnya 0 temuan pada `paper/06_references.md`.
6. **Aturan Penulis**: Seluruh 51 entri terverifikasi (et al. hanya untuk sumber dengan lebih dari 6 penulis; 6 atau kurang ditulis seluruhnya).
7. **Integritas Manuskrip LaTeX**:
   - Kompilasi PASS: `access.pdf` 14 halaman; 0 undefined citations/references; 0 BibTeX warnings.
   - 91 instance `\cite{refN}` = persis 91 tautan sitasi interaktif Markdown; key `ref1`-`ref51` lengkap dan seluruhnya tersitasi.
   - Template `ieeeaccess.cls` dan `IEEEtran.bst` identik dengan proyek referensi `chexnet-raddino-medical-captioning`.
   - Overfull hbox tersisa seluruhnya artefak kelas (29x 505.12pt dan 2x 9.27pt, identik dengan build proyek referensi) plus 1x 1.60pt yang dapat diabaikan; satu-satunya overfull nyata (86.96pt, nama checkpoint HuggingFace) telah diperbaiki dengan `\allowbreak`.
8. **Konformansi Template Asli IEEE Access**: seluruh berkas pendukung identik (CRLF-only) dengan `template/ACCESS_latex_template_20260513`; struktur dokumen terpreservasi; deviasi `\PARstart` diperbaiki lalu disesuaikan preferensi pengguna (kata pertama normal); INDEX TERMS memakai pemisah koma sesuai instruksi template.
9. **Normalisasi Format Metrik**: 0 sisa format ganda `% (0.xxxx)` dan 0 nilai metrik desimal murni di `paper_outline.md`, `paper/*.md`, dan `sections/*.tex`; seluruh Accuracy-Precision-Recall-F1 kini berformat persentase; nilai yang sah (hyperparameter, DOI, lebar figure, `1.39 pp`, rasio `5:1`) tidak tersentuh.
10. **Layout Terverifikasi**: Figure 2 komposit 1×6 dengan tinggi citra seragam (visual diperiksa langsung); Tables III-VI baris Total Grid `\multicolumn{2}{r}` (4/4); Table II tanpa bold; Table XII label `Ours` single column; biografi tanpa tautan ORCID (4 superskrip di judul tetap utuh).

---

## 6. REKOMENDASI TAHAP BERIKUTNYA

1. **Sinkronisasi Log Audit Lama (`paper/ref_part_*.md`)**:
   - Berkas `paper/ref_part_41_45.md` masih memuat entri [42] versi lama yang keliru (`N. N. Y., T. V. Ly, and D. V. T. Son`). Disarankan menyinkronkan 10 berkas log audit modular dengan kondisi terkini `paper/06_references.md`.
2. **Keputusan Sitasi Opsional**:
   - Menentukan apakah kalimat "Selain itu, mekanisme berbagi fitur paralel dengan atensi visual..." pada `02_related-works.md` baris 3 diberi tautan `[[16]]` tambahan atau dibiarkan tercakup kontekstual.
3. **Keputusan Bagian Acknowledgment**:
   - Template asli IEEE Access menyediakan `\section*{Acknowledgment}` namun naskah (md dan tex) tidak memuatnya. Perlu diputuskan: menambahkan bagian Acknowledgment (mis. dukungan Departemen Informatika UNESA yang sudah tersirat di `\tfootnote`) atau membiarkan tanpa bagian tersebut.
4. **Keputusan Urutan Kata Kunci**:
   - Pemisah INDEX TERMS sudah koma sesuai template; template juga menginstruksikan urutan alfabetis sedangkan urutan saat ini mengikuti md (`Race...`, `intersectional...`, `multi-domain...`, `algorithmic...`, `Vision Transformer`). Opsi pengurutan alfabetis tetap terbuka.
5. **Commit dan Push**:
   - Seluruh perubahan (referensi teraudit, sinkronisasi LaTeX, normalisasi metrik, penyempurnaan layout, rename sesi, pembaruan dokumentasi, regenerasi `sample_demogpairs.png`) siap di-commit secara atomik per kelompok dan didorong ke `origin/main` setelah persetujuan pengguna.
6. **Sinkronisasi ke `paper_latex_en/`**:
   - Mereplikasi seluruh hasil sinkronisasi `paper_latex_id/` (51 entri bib, 20 section, 91 sitasi, metrik persentase, layout terkini) ke paket manuskrip Bahasa Inggris, lalu mengompilasi ulang `access.pdf` dengan rantai `pdflatex` -> `bibtex` -> `pdflatex` -> `pdflatex` dan memverifikasi paginasi.
