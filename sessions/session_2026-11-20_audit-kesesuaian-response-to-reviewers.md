# DOKUMENTASI SESI KERJA ANTIGRAVITY (AGY)
**Nama Berkas**: `sessions/session_2026-11-20_audit-kesesuaian-response-to-reviewers.md`  
**Tanggal**: 20 November 2026  
**Workspace**: `D:\Research\face-race-gender-classification-using-multi-domain-vit`  
**Konteks Repositori**: `rafyakbar/face-race-gender-classification-using-multi-domain-vit`  
**Target Publikasi**: IEEE Access (ID Manuskrip: `Access-2026-50857`, Keputusan: *Reject & Resubmit*, 1 kesempatan resubmisi)

---

## 1. IKHTISAR DAN TUJUAN UTAMA SESI

1. **Orientasi cepat** terhadap `README.md`, `paper_v2/`, `paper_reviews_ieee/`, `experiment/code/archive/md_old/`, `experiment/code/md/`, `paper_outline_v1.1.md`, dan contoh surat tanggapan `D:\Research\ieee-access_response-to-reviewer_example_id.txt`.
2. **Audit kesesuaian** `paper_reviews_ieee/Response-to-Reviewers.md` terhadap `Comments.md`, `paper_v2/`, log eksperimen, dan PDF terkompilasi `paper_latex_en_v2/access.pdf` (16 halaman, sebagai acuan nomor halaman).
3. **Commit dan push** laporan audit.

## 2. METODE AUDIT

- Delegasi ke 3 subagent paralel (tanpa skill):
  - Reviewer 1 (R1 #1 s.d. #7)
  - Reviewer 2 (R2 #1 s.d. #5)
  - Reviewer 2 (R2 #6 s.d. #10) dan format/header/template
- Pemetaan halaman: ekstraksi teks `access.pdf` dengan PyMuPDF untuk menentukan halaman aktual setiap seksi, tabel, gambar, dan persamaan.
- Verifikasi angka terhadap `3.0_compare.md`, `3.1_statistical_significance.md`, `3.2_memory_consumption.md`, `archive/md_old/3.0_compare.md`, serta JSON mentah di `results/` dan `times/`.
- `paper_v2/` tidak diubah.

## 3. HASIL

Laporan: `paper_reviews_ieee/response_audit/2026-11-20_audit_response_to_reviewers.md`  
Format tabel: Kode, Aspek yang Diaudit, Temuan Kesesuaian/Ketidaksesuaian, Keparahan, Rekomendasi Perbaikan. Tabel dikelompokkan dalam 5 bagian (A format, B halaman, C Reviewer 1, D Reviewer 2, E angka pada naskah).

Ringkasan temuan: 7 kritis, 9 mayor, 10 minor.

Temuan kritis utama:
- Klaim pemadatan *Introduction* "sekitar 28%" tidak terbukti (aktual 3,77% s.d. 6,83%).
- Klaim baseline CPU `~1.487 ms/citra` (`11,9×`) tidak ada di naskah maupun log.
- Rujukan halaman keliru terhadap `access.pdf`: IV-A Paragraf 6 (Hal. 9 dan 11), IV-D (Hal. 11 dan 13), III-B Paragraf 2-3 (Hal. 4-5).
- Konfigurasi unik efektif SVM tertulis `108`, hitungan benar `24 + 48 + 96 = 168`.
- Nilai *McNemar p* dan *Exact Binomial p* pada Table 14 keliru: `0.0075` dan `0.7500` seharusnya `0.0073` dan `0.7343`, dengan *McNemar p* `0.0077` dan `0.7341`.
- Di `paper_v2/` IV-E, selisih `93.70%` vs `88.66%` tertulis `5.09 pp`, seharusnya `5.04 pp` (di `access.pdf` sudah benar).
- Dokumen masih berbahasa Indonesia, sedangkan portal IEEE Access memerlukan versi Inggris.

Temuan mayor utama: penomoran tabel di PDF memakai angka Arab (`TABLE 1-16`), GNB keliru dikelompokkan sebagai tri-domain di R1 #6, serta beberapa klaim yang tidak tertulis di `paper_v2/` (`593/600`, "interferensi gradien negatif", detail prapemrosesan, uji `Face ⊕ Age`, angka *end-to-end*, istilah "Edge AI").

Catatan konteks: sesi 18-20 November sebelumnya sengaja menghapus informasi `31.920` dari Section I dan III-G. Temuan audit tentang `31.920` perlu dibaca dengan konteks tersebut; rujukan di `Response-to-Reviewers.md` R2 #4 dan README perlu disesuaikan, bukan naskahnya.

## 4. EKSEKUSI PERBAIKAN (3 SUBAGENT PARALEL)

Seluruh rekomendasi audit telah dieksekusi secara paralel dengan perubahan sangat minimal pada naskah (`paper_v2/`, `paper_outline_v1.1.md`, `paper_latex_id_v2/`, `paper_latex_en_v2/`) dan revisi menyeluruh pada `Response-to-Reviewers.md`:

1. **Subagent 1 (`paper_v2/` & `paper_outline_v1.1.md` — Perubahan Minimal):**
   - **MS-01:** Mengoreksi `108 konfigurasi unik efektif` SVM menjadi `168 konfigurasi unik efektif` pada `paper_v2/03_materials-and-methods_f-support-vector-machine.md` dan `paper_outline_v1.1.md`.
   - **MS-02:** Mengoreksi nilai *McNemar $p$-value* dan *Exact Binomial $p$-value* pada Table XIV (`paper_v2/04_results-and-discussion_b-feature-ablation-study.md` & `paper_outline_v1.1.md`): LR Tri vs Dual `Emotion ⊕ Face` (`0.0077` dan `0.0073`) serta SVM Tri vs Dual `Emotion ⊕ Face` (`0.7341` dan `0.7343`).
   - **MS-03:** Menyelaraskan selisih `93.70%` vs `88.66%` menjadi `5.04 pp` (beserta rincian `-4.07 pp` LR dan `-5.09 pp` SVM) pada `paper_v2/04_results-and-discussion_e-comparison-with-prior-studies.md`.
2. **Subagent 2 (`paper_latex_id_v2/` & `paper_latex_en_v2/` + Kompilasi Ulang PDF):**
   - Menerapkan perbaikan minimal **MS-01**, **MS-02**, dan **MS-03** pada berkas `.tex` terkait di `paper_latex_id_v2/sections/` dan `paper_latex_en_v2/sections/`.
   - Mengompilasi ulang kedua `access.pdf` (`pdflatex` 2x) dan memverifikasi via PyMuPDF bahwa jumlah halaman tetap **16 halaman** dengan seluruh angka hasil koreksi (`168`, `0.0077`, `0.0073`, `0.7341`, `0.7343`, `5.04 pp`) tertera akurat.
3. **Subagent 3 (`paper_reviews_ieee/Response-to-Reviewers.md`, `Comments.md`, `README.md`, `README.ai.md`):**
   - Menambahkan pembatas `---`, memperjelas rincian berkas *(c) Main Manuscript*, dan menambahkan heading `## Penelaah #1` serta `## Penelaah #2` (**FMT-01**, **FMT-05**).
   - Menyeragamkan format angka desimal (`.`) dan ribuan (`.`), format dimensi polos (`224 × 224`), serta penomoran tabel Arab (`Table 1`–`Table 16`) sesuai `access.pdf` (**FMT-03**, **FMT-04**).
   - Mengoreksi seluruh rujukan nomor halaman agar 100% akurat terhadap `paper_latex_en_v2/access.pdf` (**HAL-01** s.d. **HAL-05**: IV-A Par. 6 di Hal. 9 & 11; IV-D & kutipannya di Hal. 11 & 13; III-B Par. 2–3 di Hal. 4–5; II-C Par. 2 di Hal. 3–4; IV-C di Hal. 11).
   - Menghapus klaim `"sekitar 28%"` (**R1-01**), klaim fiktif baseline CPU `~1.487 ms/citra` (`11,9×`) (**R1-05**, **R2-08**), klaim `"interferensi gradien negatif"` (**R2-01**), serta istilah `"Edge AI"` (**R2-08**).
   - Memperbaiki pengelompokan GNB sebagai Dual-Domain `Emotion ⊕ Face` (84.31%) pada **Table 16** (**R1-06**), menyelaraskan `168` konfigurasi unik efektif SVM (**R2-04**), mencantumkan nilai *McNemar $p$* & *Exact Binomial $p$* yang telah dikoreksi (**R2-05**), serta melengkapi kutipan verbatim Paragraf 3 Seksi IV-D (**R2-09**).
   - Menyelaraskan `108` → `168` pada `paper_reviews_ieee/Comments.md`, `README.md`, dan `README.ai.md`.

## 5. RIWAYAT GIT

| Commit | Isi |
|---|---|
| `073c286` | Menambahkan laporan audit |
| `045bc71` | Menambahkan awalan tanggal pada nama berkas audit (`2026-11-20_audit_response_to_reviewers.md`), menghapus `2026-11-20_comprehensive-response-audit.md`, dan memperbarui `prompts.txt` |
| `090e0fe` | Menambahkan dokumentasi log sesi awal |
| *(Commit terbaru)* | Mengeksekusi seluruh perbaikan hasil audit pada `Response-to-Reviewers.md`, `Comments.md`, `README.md`, `README.ai.md`, serta perbaikan minimal angka kritikal pada `paper_outline_v1.1.md`, `paper_v2/`, `paper_latex_id_v2/`, dan `paper_latex_en_v2/` beserta kompilasi ulang PDF |
