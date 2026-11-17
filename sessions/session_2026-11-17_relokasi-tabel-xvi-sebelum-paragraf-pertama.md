# Sesi 2026-11-17: Relokasi Tabel XVI dan Perbaikan Penempatan Tata Letak Halaman LaTeX

## 1. Konteks dan Permintaan Pengguna
- **Permintaan 1:**
  Pada naskah Bab IV Bagian E (`Comparison with Prior Studies`):
  1. Letakkan tabel sebelum paragraf pertama pada file markdown `paper_v2/04_results-and-discussion_e-comparison-with-prior-studies.md`.
  2. Perbarui berkas LaTeX `paper_latex_id_v2/sections/04_results-and-discussion_e-comparison-with-prior-studies.tex`.
  3. Kompilasi ulang PDF `access.pdf` via MiKTeX.
  4. Lakukan commit dan push ke remote repository.
- **Permintaan 2:**
  "masalahnya adalah tabel 16 pada latex terletak pada halaman references, seharusnya tidak"

## 2. Investigasi & Akar Masalah (Root Cause)
- Pada format dua-kolom IEEE Access, float lebar penuh `\begin{table*}` yang dideklarasikan pada pertengahan Halaman 13 (setelah Bagian IV.D) tidak dapat ditempatkan di halaman yang sama jika teks kolom pertama sudah terisi.
- Akibatnya, LaTeX secara otomatis menunda float `table*` tersebut ke halaman berikutnya (Halaman 14).
- Karena Bagian V (`Conclusion`) dan awal `References` dimulai di akhir Halaman 13 dan berlanjut ke Halaman 14, Tabel 16 akhirnya ditaruh di puncak Halaman 14 di atas bagian daftar pustaka (References).

## 3. Tindakan & Solusi yang Diterapkan
1. **Konversi Float Menjadi Kolom Tunggal (`table`):**
   - Mengubah lingkungan `\begin{table*}[htbp] ... \end{table*}` menjadi lingkungan kolom tunggal `\begin{table}[htbp] ... \end{table}` pada `paper_latex_id_v2/sections/04_results-and-discussion_e-comparison-with-prior-studies.tex`.
   - Menyesuaikan `\resizebox{\columnwidth}{!}{% ... }` dan `\setlength{\tabcolsep}{2.5pt}` agar tabel 6-kolom muat secara proporsional dan presisi di dalam 1 kolom teks IEEE Access tanpa overfull hbox.
   - Pola ini konsisten dengan naskah baseline `paper_latex_id` (di mana tabel komparasi studi terdahulu juga menggunakan float 1 kolom `table`).
2. **Kompilasi Penuh via MiKTeX:**
   - Menjalankan pipeline kompilasi 4-tahap: `pdflatex` -> `bibtex` -> `pdflatex` -> `pdflatex`.
   - Hasil kompilasi: Exit code 0, 0 error, 0 undefined citations/references.
3. **Verifikasi Penempatan Halaman:**
   - **Halaman 13:** Berisi subjudul `E. COMPARISON WITH PRIOR STUDIES`, `TABLE 16` (langsung di bawah subjudul), narasi pembahasan IV.E, dan `V. CONCLUSION`.
   - **Halaman 14:** Murni berisi `REFERENCES` (tidak ada lagi elemen Tabel 16).
   - **Halaman 15–16:** Lanjutan referensi dan biografi penulis.
4. **Git Commit & Push:**
   - Menambahkan berkas perubahan, commit deskriptif, dan push ke remote repository `origin/main`.
