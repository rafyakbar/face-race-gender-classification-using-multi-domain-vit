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

## 4. RIWAYAT GIT

| Commit | Isi |
|---|---|
| `073c286` | Menambahkan laporan audit |
| `045bc71` | Menambahkan awalan tanggal pada nama berkas audit, menghapus `2026-11-20_comprehensive-response-audit.md` (atas arahan pengguna, tidak dikembalikan), dan memperbarui `prompts.txt` |

Kedua commit telah di-push ke `origin/main`.

## 5. TINDAK LANJUT YANG BELUM DIKERJAKAN

1. Koreksi angka pada naskah: `108` menjadi `168`, nilai p pada Table 14, dan `5.09 pp` menjadi `5.04 pp` di `paper_v2/` (sinkronkan ke `paper_latex_id_v2/` dan `paper_latex_en_v2/`, lalu kompilasi ulang PDF).
2. Revisi `Response-to-Reviewers.md`: hapus klaim 28% dan CPU 11,9×, koreksi nomor halaman, perbaiki pengelompokan GNB, dan sesuaikan klaim yang tidak ada di naskah.
3. Susun versi final Bahasa Inggris dengan kutipan verbatim dari naskah LaTeX Inggris dan penomoran tabel Arab.
