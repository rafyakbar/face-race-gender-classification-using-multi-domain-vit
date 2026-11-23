# Laporan Audit Ulang (Re-Audit) Kesesuaian *Response to Reviewers* (`Access-2026-50857`)

- **Dokumen Utama yang Diaudit:** `paper_reviews_ieee/Response-to-Reviewers.md` (pasca-revisi commit `a780284`)
- **Dokumen Pembanding (*Ground Truth*):**
  1. `paper_reviews_ieee/Comments.md` & `paper_reviews_ieee/IEEE-Access_Decision-on-Manuscript-ID-Access-2026-50857.md`
  2. `paper_reviews_ieee/IEEE-Access_Response-to-Reviewers-template.md` & `paper_reviews_ieee/Resubmission-Checklist.md`
  3. Naskah modular `paper_v2/` (`00_abstract.md` s.d. `05_conclusion.md`)
  4. PDF terkompilasi ulang `paper_latex_en_v2/access.pdf` (16 halaman) sebagai acuan mutlak verifikasi halaman, tabel, dan angka final
  5. Log eksperimen `experiment/code/md/` (`3.0_compare.md`, `3.1_statistical_significance.md`, `3.2_memory_consumption.md`), arsip `experiment/code/archive/md_old/3.0_compare.md`, dan JSON prediksi mentah (`experiment/code/results/*.json`)
- **Tanggal Re-Audit:** 23 November 2026
- **Metode:** Delegasi paralel ke 3 subagent independen (R1 #1–#7, R2 #1–#5, R2 #6–#10 & Format) + verifikasi deterministik PyMuPDF terhadap `paper_latex_en_v2/access.pdf`. Tidak ada berkas `paper_v2/` maupun `Response-to-Reviewers.md` yang diubah pada sesi audit ulang ini.

---

## Ringkasan Eksekutif (Perbandingan Audit 20 Nov → Re-Audit 23 Nov)

| Kategori Keparahan | Audit Awal (20 Nov) | Re-Audit (23 Nov) | Ringkasan Status |
| :--- | :---: | :---: | :--- |
| **Kritis** | 7 | **1** *(operasional bahasa saja)* | **0 temuan kritis faktual, angka, maupun halaman.** Seluruh 6 isu kritis teknis sebelumnya (`28%`, CPU `~1.487 ms / 11.9×`, `108 → 168`, Table 14 `0.0077/0.0073` & `0.7341/0.7343`, `5.04 pp` di `paper_v2`, dan rujukan halaman utama) telah **100% tuntas**. Sisa 1 item kritis adalah status operasional: dokumen masih berbahasa Indonesia (wajib versi Inggris untuk portal *IEEE Access*). |
| **Mayor** | 9 | **1** | 8 dari 9 isu mayor sebelumnya **100% tuntas**. Tersisa 1 isu mayor tipografi: pencampuran pemisah ribuan koma (`3,287.07`, `30,666.02` di L213) vs titik (`1.027× [>1.000×]`, `2.160`, `10.800`, `31.920`) di kalimat yang sama dengan titik desimal. |
| **Minor** | 10 | **4** | (1) Rujukan Seksi III-F pada R2 #4 (L165) tertulis `Halaman 6`, padahal angka `168` berlanjut ke `Halaman 7` (seharusnya `Halaman 6–7`); (2) Lintas-rujukan R1 #7 (L106) menyebut Paragraf 2 R2 #10 mengutip *"batasan penelitian dan arah riset lanjutan"*, padahal R2 #10 hanya mengutip 3 kalimat batasan; (3) Redaksi redundan `330× [>330×]` di R2 #8 (L216); (4) Pengulangan ringan *"168 konfigurasi unik efektif"* di R2 #4 (L154) & path internal `` `experiment/code/archive/` `` di R2 #2 (L129). |
| **Sesuai** | 5 | **21** | Seluruh 17/17 kutipan komentar asli, seluruh 6/6 kutipan blok verbatim (`R1 #1, #4, #7`, `R2 #6, #9, #10`), seluruh 26 referensi `Table 1`–`Table 16` (0 sisa Romawi), seluruh angka eksperimen & statistik, serta seluruh angka pada `paper_v2/` dan `paper_latex_en_v2/access.pdf` **100% terverifikasi sesuai**. |

---

## Bagian A — Re-Audit Format, Header, Penomoran Tabel, Angka, dan Bahasa

| Kode | Aspek yang Diaudit | Temuan Kesesuaian / Ketidaksesuaian | Keparahan | Rekomendasi Perbaikan |
| :--- | :--- | :--- | :---: | :--- |
| **RA-FMT-01** | Header, garis pemisah `---`, heading `## Penelaah #1/#2`, rincian 3 berkas, & catatan kaki resmi | **Sesuai:** Seluruh struktur surat pengantar, metadata (`Access-2026-50857`), pemisah `---`, rincian berkas *(c) Main Manuscript* (LaTeX + PDF), heading pembatas `## Penelaah #1` & `## Penelaah #2`, serta catatan kaki `ieeeaccesseic@ieee.org` telah sesuai 100% dengan `IEEE-Access_Response-to-Reviewers-template.md` dan `Resubmission-Checklist.md`. | **Sesuai** | Pertahankan struktur ini sebagai acuan langsung penyusunan versi Inggris. |
| **RA-FMT-02** | Penomoran tabel (`Table 1`–`Table 16`) | **Sesuai:** Pemindaian penuh menemukan **26 rujukan tabel** dan **0 sisa angka Romawi** (`Table I`–`XVI`). Seluruh rujukan (`Table 1`–`Table 16`) cocok 100% dengan penomoran Arab (`TABLE 1`–`TABLE 16`) pada `paper_latex_en_v2/access.pdf`. | **Sesuai** | Tidak diperlukan perubahan. |
| **RA-FMT-03** | Konsistensi pemisah ribuan vs. titik desimal | **Ketidaksesuaian:** Pemisah desimal konsisten memakai titik (`.`), tetapi **pemisah ribuan tercampur**: L213 memakai **koma** (`3,287.07 detik`, `30,666.02 detik`), sedangkan bagian lain memakai **titik** (`2.304`, `2.160`, `10.800`, `8.640`, `31.920`, `1.915`, `1.914`, serta `1.027× (>1.000×)` pada L84 dan `1.027× [>1.000×]` pada L214). Pada L84 dan L214, `1.027×` berdampingan dengan `4.6785 ms` dan `124.505 ms` sehingga rawan terbaca ambigu sebagai *1,027 kali* (satu koma nol dua tujuh) alih-alih *seribu dua puluh tujuh kali*. | **Mayor** | Seragamkan seluruh pemisah ribuan pada `Response-to-Reviewers.md` menjadi **koma (`,`)** (`1,027× (>1,000×)`, `2,160`, `10,800`, `8,640`, `2,304`, `31,920`, `1,915`, `1,914`, dll.) agar selaras dengan titik desimal dan `3,287.07` / `30,666.02` (kecuali bila mempertahankan gaya asli di dalam kutipan verbatim `paper_v2/`). |
| **RA-FMT-04** | Bahasa dokumen untuk unggahan portal *IEEE Access* | **Belum Siap Unggah (Operasional):** `Response-to-Reviewers.md` masih berbahasa Indonesia (draf kerja internal), sementara portal resubmisi *IEEE Access* mewajibkan berkas *Author's Response Files* dalam Bahasa Inggris formal. | **Kritis** | Susun berkas final Bahasa Inggris (`Response-to-Reviewers_EN.md` / `.docx` / `.pdf`) berdasarkan versi ID yang telah bersih ini, dengan seluruh kutipan blok (`> ...`) disalin **100% verbatim dari `paper_latex_en_v2/access.pdf`**. |

---

## Bagian B — Re-Audit Verifikasi Nomor Halaman & Angka pada `paper_latex_en_v2/access.pdf`

| Kode | Aspek yang Diaudit | Temuan Kesesuaian / Ketidaksesuaian | Keparahan | Rekomendasi Perbaikan |
| :--- | :--- | :--- | :---: | :--- |
| **RA-HAL-01** | Verifikasi angka kritikal pada PDF terkompilasi ulang (`access.pdf`, 16 halaman) | **Sesuai 100%:** Pemindaian PyMuPDF pada `paper_latex_en_v2/access.pdf` mengonfirmasi jumlah halaman tetap **16 halaman**; angka lama yang salah sudah **0 kemunculan** (`108`: `[]`, `0.0075`: `[]`, `0.7500`: `[]`), sedangkan angka hasil koreksi seluruhnya terverifikasi hadir (`168`: Hal. 7; `0.0077`, `0.0073`, `0.7341`, `0.7343`: Hal. 12 Table 14; `5.04`: Hal. 13). | **Sesuai** | Tidak diperlukan perubahan pada `paper_v2/`, `paper_latex_id_v2/`, maupun `paper_latex_en_v2/`. |
| **RA-HAL-02** | Seluruh koreksi halaman sebelumnya (`HAL-01` s.d. `HAL-05`) | **Sesuai 100%:** Rujukan Seksi II (Hal. 2–4), II-C P2 (Hal. 3–4), III-B P2–3 (Hal. 4–5), IV-A P6 (Hal. 9 dan 11), IV-C (Hal. 11), dan IV-D (Hal. 11 dan 13; kutipan di Hal. 13) seluruhnya cocok 100% dengan `paper_latex_en_v2/access.pdf`. | **Sesuai** | Pertahankan. |
| **RA-HAL-03** | Rujukan halaman Seksi III-F pada R2 #4 (L165) | **Ketidaksesuaian Minor:** L165 menulis *"narasi Seksi III-F (Halaman 6, mengenai 288 kombinasi grid Cartesian atau 168 konfigurasi unik efektif SVM dan 1.440 fits)"*. Pada `paper_latex_en_v2/access.pdf`, judul dan awal Seksi III-F berada di **Halaman 6**, namun kalimat yang memuat **`168 effective unique configurations`** berlanjut ke **Halaman 7**. | **Minor** | Ubah rujukan L165 menjadi **`narasi Seksi III-F (Halaman 6–7, ...)`**. |

---

## Bagian C — Re-Audit Komentar Reviewer 1 (`R1 #1` s.d. `R1 #7`)

| Kode | Aspek yang Diaudit | Temuan Kesesuaian / Ketidaksesuaian | Keparahan | Rekomendasi Perbaikan |
| :--- | :--- | :--- | :---: | :--- |
| **RA-R1-01** | R1 #1 — Pemadatan *Introduction* (L25–39) | **Sesuai:** Kutipan komentar R1 100% verbatim; klaim `"sekitar 28%"` telah dihapus; struktur 7 paragraf & batas ≤2 sitasi/kalimat terverifikasi di `paper_v2/01_introduction.md`; kutipan blok 4 kontribusi (L34–38) **100% verbatim identik**. | **Sesuai** | Tidak diperlukan perubahan. |
| **RA-R1-02** | R1 #2 — *Related Works* & Persamaan (L42–50) | **Sesuai:** Kutipan komentar R1 100% verbatim; deskripsi Eq. (3) telah diperbaiki menjadi *Scaled Dot-Product Attention* dalam MHSA; Subseksi II-A–II-C, Eq. (1)–(4), dan rujukan halaman (Hal. 2–4, Hal. 3, Hal. 3–4) cocok 100%. | **Sesuai** | Tidak diperlukan perubahan. |
| **RA-R1-03** | R1 #3 — Desain Ulang Figure 3 (L53–61) | **Sesuai:** Kutipan komentar R1 100% verbatim; klaim *"diagram vektor"* telah diganti *"diagram arsitektur beresolusi tinggi"*; alur 7 tahapan, Eq. (5)–(8), dan halaman (Fig. 3 Hal. 6, III-B Hal. 4–5) cocok 100%. | **Sesuai** | Tidak diperlukan perubahan. |
| **RA-R1-04** | R1 #4 — Pembahasan Figure 4 (L64–74) | **Sesuai:** Kutipan komentar R1 dan kutipan blok dekomposisi kesalahan (L73) **100% verbatim identik** dengan `paper_v2/04_results-and-discussion_d-error-pattern-assessment.md` L13; seluruh angka (`245`, `165` [67.35%], `80` [32.65%], `84.72%`, `37/55`) dan halaman (Hal. 11 dan 13, kutipan Hal. 13) cocok 100%. | **Sesuai** | Tidak diperlukan perubahan. |
| **RA-R1-05** | R1 #5 — Detail Dataset, Kontribusi, & *Time Cost* (L77–85) | **Sesuai secara substansi & angka:** Klaim fiktif CPU `~1.487 ms / 11.9×` sudah dihapus bersih; rujukan Seksi III-I (Hal. 8) dan Seksi IV-B/Table 14 (Hal. 11–12) sudah ditambahkan; seluruh angka GPU/pelatihan/inferensi cocok 100% dengan `paper_v2/` dan `3.2_memory_consumption.md`. *(Catatan pemisah ribuan `1.027× (>1.000×)`: dicakup di **RA-FMT-03**).* | **Sesuai** | Cukup selaraskan pemisah ribuan sesuai **RA-FMT-03**. |
| **RA-R1-06** | R1 #6 — Perbandingan Metode Pembanding (L88–96) | **Sesuai:** Pengelompokan 12 entri Table 16 kini 100% akurat (3 *Stratified* + 9 *Subject-Disjoint*: 4 single-domain, 2 dual-domain `Emotion ⊕ Face` [SVM `88.43%` & GNB `84.31%`], 3 tri-domain [RF `85.00%`, SVM `88.61%`, LR `88.66%`]). Kesalahan `5.09 → 5.04 pp` di `paper_v2` IV-E L23 juga sudah tuntas. | **Sesuai** | Tidak diperlukan perubahan. |
| **RA-R1-07** | R1 #7 — Penyempurnaan *Conclusion* (L99–109) | **Sesuai dengan 1 temuan Minor baru:** Kutipan komentar R1 dan kutipan blok Paragraf 1 (L108) **100% verbatim identik** dengan `paper_v2/05_conclusion.md` L3. **Temuan Minor:** Pengantar L106 menulis *"(sementara paragraf kedua mengenai batasan penelitian **dan arah riset lanjutan** dikutip pada tanggapan Penelaah #2, Komentar #10)"*, padahal R2 #10 (L245) hanya mengutip 3 kalimat pertama (batasan penelitian) dan tidak mengutip 4 kalimat arah riset lanjutan. | **Minor** | Ubah frasa L106 menjadi *"(sementara bagian batasan penelitian pada paragraf kedua dikutip pada tanggapan Penelaah #2, Komentar #10)"* agar 100% presisi. |

---

## Bagian D — Re-Audit Komentar Reviewer 2 (`R2 #1` s.d. `R2 #10`)

| Kode | Aspek yang Diaudit | Temuan Kesesuaian / Ketidaksesuaian | Keparahan | Rekomendasi Perbaikan |
| :--- | :--- | :--- | :---: | :--- |
| **RA-R2-01** | R2 #1 — *Novelty and Contribution* (L114–122) | **Sesuai:** Klaim *"interferensi gradien negatif"* sudah dihapus dan diselaraskan dengan efisiensi komputasi *offline* tanpa *fine-tuning* ulang; pemisahan rujukan narasi konseptual (I P5–6 Hal. 2, II-C P2 Hal. 3–4, III Overview Hal. 4) vs. pembuktian empiris (IV-B Hal. 11–12) 100% akurat. | **Sesuai** | Tidak diperlukan perubahan. |
| **RA-R2-02** | R2 #2 — *Data Leakage and Generalization* (L125–133) | **Sesuai (1 catatan editorial Minor):** Sumber angka `593 dari 600 subjek` telah diklarifikasi secara transparan sebagai audit partisi historis, dan seluruh angka partisi (480/120, 8.640/2.160, 0%) serta ablasi (`-5.09 pp` SVM, `-4.07 pp` LR) cocok 100%. **Catatan Minor:** L129 menyebut path internal `` `experiment/code/archive/` `` yang bersifat internal repositori. | **Minor** | Opsional: pada versi EN untuk penelaah eksternal, ganti path `` `experiment/code/archive/` `` dengan frasa *"our internal historical partition audit"*. |
| **RA-R2-03** | R2 #3 — *Preprocessing and Reproducibility* (L136–147) | **Sesuai:** Jargon *"Git SHA"* telah bersih seluruhnya; pemisahan spesifikasi tertulis di Seksi III-A/III-B/Table 2 dengan rincian tambahan konfigurasi *processor* (`12 attention heads`, *pre-cropped* tanpa MTCNN, interpolasi bilinear, penskalaan $1/255$ ke $[-1, 1]$) 100% akurat dan jujur. | **Sesuai** | Tidak diperlukan perubahan. |
| **RA-R2-04** | R2 #4 — *Hyperparameter Search Consistency* (L150–166) | **Sesuai secara substansi & aritmatika (1 catatan redaksi Minor):** Angka **`168` konfigurasi unik efektif** SVM ($24+48+96=168$) kini 100% konsisten di `Response-to-Reviewers.md`, `Comments.md`, `paper_v2/`, `paper_outline_v1.1.md`, dan kedua `access.pdf`; seluruh rujukan fiktif (I P5, IV-A P6, footnote Table VI) telah dihapus bersih. **Catatan Minor:** Pengulangan frasa ringan pada L154 (`"jumlah konfigurasi unik efektifnya adalah **168 konfigurasi unik efektif**"`). *(Catatan halaman III-F: lihat **RA-HAL-03**).* | **Minor** | Sederhanakan L154 menjadi `"jumlah konfigurasi unik efektifnya adalah **168**"` dan perbarui halaman III-F sesuai **RA-HAL-03**. |
| **RA-R2-05** | R2 #5 — *Statistical Interpretation* (L169–180) | **Sesuai 100%:** Seluruh pasangan nilai McNemar $\chi^2$ $p$-value dan Exact Binomial $p$-value (`0.7341` / `0.7343` untuk SVM Tri vs Dual; `0.0077` / `0.0073` untuk LR Tri vs Dual; `1.0000` untuk LR vs SVM) 100% konsisten dengan `paper_v2` Table XIV, `access.pdf` Table 14, dan `3.1_statistical_significance.md`; pengujian `Face ⊕ Age` ($p = 0.0086$) dikualifikasikan secara akurat sebagai verifikasi tambahan dari log prediksi. | **Sesuai** | Tidak diperlukan perubahan. |
| **RA-R2-06** | R2 #6 — *Fairness Analysis* (L183–193) | **Sesuai 100%:** Kualifikasi EOD (`9.72 pp`), rujukan Seksi III-H Eq. (23), Table 15 (Hal. 12), Seksi IV-C (Hal. 11), dan kutipan blok *Responsible AI* (L192) **100% verbatim identik** dengan `paper_v2/04_results-and-discussion_c-intersectional-subgroup-performance.md` L23. | **Sesuai** | Tidak diperlukan perubahan. |
| **RA-R2-07** | R2 #7 — *Baseline Comparison* (L196–204) | **Sesuai 100%:** Ketiga unsur pertanyaan penelaah (*partisi data, prapemrosesan, dan protokol evaluasi*) sudah dijawab eksplisit pada L200; rujukan Table 16 dan narasi kualifikasi Seksi IV-E (Hal. 13) akurat. | **Sesuai** | Tidak diperlukan perubahan. |
| **RA-R2-08** | R2 #8 — *Computational Efficiency* (L207–220) | **Sesuai secara substansi & angka (1 Minor redaksi):** Klaim fiktif CPU `~1.487 ms / 11.9×` dan istilah `"Edge AI"` sudah dihapus bersih; angka *end-to-end* GPU (`124.505 ms` vs `129.179 ms`) dikualifikasikan akurat sebagai penjumlahan kumulatif Table 11 + Table 12; seluruh 5 dimensi cocok 100% dengan `3.2_memory_consumption.md` dan `paper_v2/`. **Catatan Minor:** Redaksi L216 `(**330× [>330×] lebih ringkas**)` redundan. *(Catatan pemisah ribuan L212–215: dicakup di **RA-FMT-03**).* | **Minor** | Rapikan L216 menjadi `(**>330× lebih ringkas**)` (atau `**332.7× (>330×) lebih ringkas**`) dan seragamkan pemisah ribuan sesuai **RA-FMT-03**. |
| **RA-R2-09** | R2 #9 — *Results and Discussion* (L223–233) | **Sesuai 100%:** Seluruh 4 kalimat kutipan blok Paragraf 3 Seksi IV-D (L232) kini **100% verbatim identik** dan utuh dengan `paper_v2/04_results-and-discussion_d-error-pattern-assessment.md` L15; rujukan halaman (Abstrak Hal. 1, IV-C Hal. 11, IV-D Hal. 11 dan 13, kutipan Hal. 13) akurat. | **Sesuai** | Tidak diperlukan perubahan. |
| **RA-R2-10** | R2 #10 — *Conclusion and Limitations* (L236–246) | **Sesuai 100%:** Pengantar L243 akurat merujuk pernyataan batasan penelitian pada Paragraf 2 Seksi V (Hal. 14), dan kutipan blok 3 kalimat (L245) **100% verbatim identik** dengan `paper_v2/05_conclusion.md` L5. | **Sesuai** | Tidak diperlukan perubahan. |

---

## Kesimpulan Kesiapan Resubmisi

- **Integritas Naskah (`paper_v2/`, `paper_latex_id_v2/`, `paper_latex_en_v2/access.pdf`):** **100% BERSIH & TERVERIFIKASI** (0 temuan sisa).
- **Integritas Substansi `Response-to-Reviewers.md` (Versi ID):** **LULUS PENUH secara teknis/substansi/halaman** — tinggal 1 perapihan format pemisah ribuan (**RA-FMT-03**) dan 4 polesan minor (**RA-HAL-03**, **RA-R1-07**, **RA-R2-04**, **RA-R2-08**).
- **Langkah Terakhir Wajib Sebelum Unggah Portal:** Menyusun versi final **Bahasa Inggris** (`Response-to-Reviewers_EN`) dengan seluruh kutipan blok disalin verbatim dari `paper_latex_en_v2/access.pdf` (**RA-FMT-04**).
