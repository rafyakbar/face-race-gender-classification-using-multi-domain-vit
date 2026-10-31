# DOKUMENTASI SESI KERJA ANTIGRAVITY (AGY)
**Nama Berkas**: `docs/sessions/2026-10-31_penyempurnaan-spesifikasi-abstrak-outline-v1.1-dan-sinkronisasi.md`  
**Cermin Berkas**: `sessions/session_2026-10-31_penyempurnaan-spesifikasi-abstrak-outline-v1.1-dan-sinkronisasi.md`  
**Tanggal**: 31 Oktober 2026  
**Waktu Sesi**: 21:30:00 – 22:15:00 WIB  
**Workspace**: `D:\Rafy\Research\face-race-gender-classification-using-multi-domain-vit`  
**Konteks Repositori**: `rafyakbar/face-race-gender-multi-vit`  
**Target Publikasi**: IEEE Access (ID Manuskrip: `Access-2026-50857`, Keputusan: *Reject & Resubmit* — 1 Kesempatan Resubmission Tunggal Berbasis *Binary Peer Review*)  
**Lingkungan Eksekusi**: Windows 11, Python 3.11+, Git SSH, Antigravity Agentic Assistant / Gemini 3.8 Flash (High)  

---

## 1. IKHTISAR DAN TUJUAN UTAMA SESI

Sesi kerja ini berfokus pada penyempurnaan dokumen panduan penulisan naskah revisi `paper_outline_v1.1.md` dengan penekanan khusus pada seksi Abstrak dan pemeliharaan format murni *paper outline* (spesifikasi instruksional berbasis poin-poin/checklist, bukan penyisipan draf naskah langsung):

1. **Penyelarasan Spesifikasi Abstrak Sesuai 8 Batasan Ketat Pengguna & Referensi Abstrak Lama (`paper/00_abstract.md`):**
   - **Target Jumlah Kata:** Disesuaikan menjadi **150–250 kata** (standar artikel IEEE Access padat).
   - **Pembersihan Istilah Token Eksplisit:** Mengeliminasi seluruh penyebutan token arsitektur teknis seperti `[CLS]`.
   - **Penyelarasan Nomenklatur Model:** Menghapus label singkatan *custom* (`ViT-Face`, `ViT-Emotion`, `ViT-Age`) dan menggantinya dengan deskripsi fungsional sesuai referensi lama: *"tiga model Vision Transformer (ViT) pre-trained spesifik tugas untuk biometrik wajah, ekspresi afektif, dan estimasi usia"*.
   - **Pembersihan Metrik Partisi Spesifik Subjek:** Menghapus penyebutan angka spesifik "120 subjek" maupun ukuran file/parameter model di dalam Abstrak.
   - **Pembersihan Detail Hiperparameter:** Menghapus detail pencarian *grid search* atau daftar parameter teknis dari spesifikasi abstrak.
   - **Pelaporan Dual-Benchmark Komparatif Lengkap:** Memasukkan hasil kuantitatif dari kedua protokol evaluasi:
     * *Split Stratified Class Biasa (Subject-Overlap)*: SVM Tri-Domain meraih Akurasi **93.70%** dan F1-Score **93.69%**.
     * *Zero Identity Leakage (Subject-Disjoint)*: Logistic Regression Tri-Domain meraih Akurasi **88.66%** dan F1-Score **88.68%**, disusul SVM Tri-Domain dengan Akurasi **88.61%** dan F1-Score **88.63%**.
   - **Preservasi Kata Kunci Resmi:** Menjaga keutuhan kata kunci sesuai formulir pengajuan IEEE: `Biometrics, face recognition, feature extraction, intersectional demographic recognition, multi-domain feature fusion, Vision Transformer.`
2. **Kepatuhan Format Murni Paper Outline (Bukan Draf Naratif):**
   - Menghapus blok draf teks prosa berkelanjutan (*draft prose*) yang sebelumnya sempat disisipkan secara tidak sengaja di bawah judul Abstrak.
   - Menstrukturkan kembali seksi Abstrak menjadi poin-poin checklist instruksional (*outline bullets*) yang terbagi rapi ke dalam: Latar Belakang & Tantangan, Metode yang Diusulkan, Evaluasi Dual-Benchmark & Hasil, dan Kesimpulan Generalisasi.
3. **Penyempurnaan Profil Efisiensi Komputasi Dual-Hardware & Table XIV:**
   - Memutakhirkan Executive Summary (Poin 4) dan Bagian IV.C dengan menyajikan data komparasi perangkat keras: ekstraksi CPU *unbatched* (~1.487 ms/citra; 4,46 jam) vs ekstraksi GPU NVIDIA RTX 4060 terakselerasi *in-memory processor caching* (124,5 ms/citra; 22,4 menit; akselerasi 11,9×).
   - Menggantikan *Peak RAM TBD* pada Table XIV dengan jejak memori pasti representasi array NumPy float32 untuk 2.160 sampel uji (**18.98 MB** untuk Tri-Domain, **12.66 MB** untuk Dual-Domain).
4. **Pembaruan Berkas Riwayat Prompt (`prompts.txt`):**
   - Menambahkan riwayat prompt aktif terbaru secara terurut kronologis ke dalam `prompts.txt`.

---

## 2. KRONOLOGI PERMINTAAN PENGGUNA & TINDAKAN YANG DIAMBIL

### A. Evaluasi Ulang dan Koreksi Seksi Abstrak
* **Permintaan Pengguna:**
  ```text
  perbaiki paper_outline_v1.1.md:
  Abstract:
  - ubah target kata menjadi 150 - 250.
  - tidak usah ada kata [CLS].
  - jangan kata seperti ViT-Face/Emotion/Age, coba cek referensi abstrak yang lama (paper/00_abstract.md)
  - tidak usah menyebutkan seperti 120 subjek atau ukuran model
  - tidak usah menyebutkan seperti parameter, coba cek referensi abstrak yang lama (paper/00_abstract.md)
  - seharusnya ada juga hasil dari Zero Identity Leakage dan juga yang split stratified class biasa
  - keywordnya tetap: Biometrics, face recognition, feature extraction, intersectional demographic recognition, multi-domain feature fusion, Vision Transformer
  - coba cek referensi abstrak yang lama (paper/00_abstract.md)
  perbaiki dengan sangat amat teliti, jika ingin cek-cek folder terkait bisa delegasi subagent.
  ```
  Disusul penegasan format:
  ```text
  INI PAPER OUTLINE, JANGAN DIKASIH DRAF LANGSUNG DI SANA
  ```
* **Tindakan yang Diambil:**
  1. Membaca dan menelaah naskah abstrak lama pada [paper/00_abstract.md](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/paper/00_abstract.md).
  2. Mengidentifikasi struktur kalimat dan terminologi yang digunakan pada abstrak lama, khususnya frasa pembuka dan cara mendeskripsikan model ViT.
  3. Membuang seluruh blok draf naratif langsung (baik bahasa Indonesia maupun bahasa Inggris) yang sempat dimasukkan ke dalam outline.
  4. Merumuskan ulang seksi `### Abstract` pada [paper_outline_v1.1.md](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/paper_outline_v1.1.md#L57-L67) menjadi outline poin-poin struktural:
     - **Target Kata**: 150–250 kata dalam satu paragraf padat terpadu.
     - **Latar Belakang & Tantangan**: Variasi ekspresi, penuaan biologis, tumpang tindih fenotipik, keterbatasan domain tunggal, serta risiko kebocoran identitas subjek.
     - **Metode**: Fusi fitur dari tiga model Vision Transformer pre-trained spesifik tugas untuk biometrik wajah, ekspresi afektif, dan estimasi usia, dioptimasi dengan 4 classifier klasik (RF, GNB, LR, SVM).
     - **Evaluasi Dual-Benchmark**: Melaporkan angka pasti Split Stratified Class Biasa (SVM Tri: 93.70% Acc / 93.69% F1) bersanding dengan Zero Identity Leakage (LR Tri: 88.66% Acc / 88.68% F1; SVM Tri: 88.61% Acc / 88.63% F1).
     - **Kesimpulan**: Menguantifikasi penurunan nominal 5.09 pp akibat efek memorisasi identitas dan membuktikan generalisasi fusi fitur multi-domain pada subjek baru.
     - **Keywords**: `Biometrics, face recognition, feature extraction, intersectional demographic recognition, multi-domain feature fusion, Vision Transformer.`


### B. Penegakan Aturan Sitasi Global & Pembersihan Struktur Outline (Introduction & Related Works)
* **Permintaan Pengguna:**
  ```text
  perbaiki paper_outline_v1.1.md:
  GLOBAL:
  - tambahkan aturan pada paper outline dan pada folder rules, kalau per kalimat itu hanya maksimal 2 sitasi.
  I. INTRODUCTION:
  - tidak usah ada diagram narasi pada paper outline.
  - Paragraph 3: ubah target kata menjadi 135–250. dan beri note kalau per kalimat itu hanya maksimal 2 sitasi.
  - Paragraph 5: jangan ada kata [CLS].
  II. RELATED WORKS:
  - tidak usah ada struktur seperti II. RELATED WORKS
  ├── A.
  perbaiki dengan sangat amat teliti, jika ingin cek-cek folder terkait bisa delegasi subagent.
  ```
* **Tindakan yang Diambil:**
  1. **Folder Rules (`rules/`):**
     - Memperbarui `rules/latex_rules.txt` (subseksi 6.1) dari batas 4 sitasi menjadi: *"Maksimal 2 sitasi dalam satu kalimat untuk mencegah penumpukan (*citation dumping*) dan menjaga keterbacaan naskah."*
     - Memperbarui `rules/md_rules.txt` (subseksi 7.4) dari batas 4 sitasi menjadi: *"Maksimal 2 sitasi dalam satu kalimat untuk mencegah penumpukan sitasi (citation dumping) dan menjaga kepadatan sintaksis."*
  2. **Global Rules pada `paper_outline_v1.1.md`:**
     - Menambahkan Butir 8 pada Allowed Claims: *"Disiplin Sitasi Per Kalimat (Maksimal 2 Sitasi)"*.
     - Menambahkan Butir 5 pada Negative Constraints: *"Dilarang menumpuk lebih dari 2 sitasi dalam satu kalimat"*.
  3. **Introduction (`paper_outline_v1.1.md`):**
     - Menghapus diagram alur naratif ASCII 7 paragraf di bawah heading `## I. INTRODUCTION`.
     - Mengubah target kata Paragraph 3 dari 135–225 kata menjadi **135–250 kata**, serta mempertegas catatan aturan sitasi: *"Ditetapkan aturan ketat bahwa per kalimat hanya maksimal 2 sitasi untuk menjaga keterbacaan naskah dan mencegah penumpukan sitasi (*citation dumping*)"*.
     - Menghapus penyebutan token arsitektur `[CLS]` pada Paragraf 5 Poin 2, diselaraskan menjadi: *"Ekstraksi representasi laten visual dilakukan secara offline dari backbone Vision Transformer pra-latih yang dibekukan (frozen)..."*.
  4. **Related Works (`paper_outline_v1.1.md`):**
     - Menghapus struktur pohon ASCII `II. RELATED WORKS ├── A. ...` sehingga outline bersih dari diagram struktural yang tidak diperlukan.


### C. Audit Akademik Komprehensif Introduction (P3 & P4) & Related Works via Subagent
* **Permintaan Pengguna:**
  ```text
  sekarang tolong audit "I. INTRODUCTION - Paragraph 3 & Paragraph 4" dan "II. RELATED WORKS" apakah sudah sesuai dengan "related_works/" atau belum, delegasikan ke subagent
  ```
* **Hasil Eksekusi Subagent:**
  - Pendelegasian tugas audit komprehensif kepada subagent riset (`research`) untuk membandingkan Section I (P3 & P4) dan Section II (II.A–C beserta Eq. 1–4) terhadap berkas ground truth di direktori `related_works/` (`gap_analysis.md`, `literature_matrix.md`, `sintesis_literatur.md`, `tren_analisis.md`, dan 10 berkas `summaries/*.md`).
  - **Verdict Subagent**: **MINOR FIXES (Tingkat Keselarasan ~95%)**. Formulasi matematika Eq. 1 (KELM), Eq. 2 (Patch Flattening), Eq. 3 (MHSA), dan Eq. 4 (Concatenative Direct Sum) terbukti 100% akurat secara matematis dan selaras dengan literatur. Tiga pilar research gap pada Paragraf 4 juga 100% selaras dengan `gap_analysis.md`.
* **Tindakan Perbaikan yang Diterapkan:**
  1. **Koreksi Venue Belcar et al. (2022):** Mengoreksi atribusi jurnal dari *Sensors 2022* menjadi *Informatics 2022* (MDPI, Vol. 9, Art. 18, penulis: Belcar, Grd, & Tomičić) pada 5 lokasi di `paper_outline_v1.1.md` dan tabel `related_works/literature_matrix.md`.
  2. **Dekonstruksi Kalimat II.A Paragraf 2:** Memecah kalimat komparasi pengklasifikasi hilir yang sebelumnya menumpuk 4 sitasi (dan 3 sitasi sekaligus di akhir) menjadi 2 kalimat terpisah yang kohesif guna mematuhi aturan baku maksimal 2 sitasi per kalimat.
  3. **Pembersihan Rujukan II.C Paragraf 1:** Menghapus entri Ramachandran & Rattani (2023) dari daftar sumber II.C Paragraf 1 karena fokus paper tersebut berada pada mitigasi bias generatif di II.B Paragraf 2.
  4. **Koreksi Ekspansi Jurnal JIEET (Putri et al. 2025):** Memperbaiki penulisan kepanjangan JIEET dari *Journal of Integrated and Advanced Engineering* menjadi nama resmi *Journal of Information Engineering and Educational Technology* (UNESA).

---

## 3. HASIL VERIFIKASI FILE

1. **`paper_outline_v1.1.md`**:
   - Struktur outline terjaga 100% konsisten, bersih dari blok draf teks mengambang.
   - Seksi Abstrak memuat batasan panduan penulisan yang lengkap dan akurat.
   - Profil komputasi pada Executive Summary dan Section IV.C (Table XIV) telah tersinkronisasi dengan metrik empiris GPU RTX 4060 dan CPU baseline.
2. **`prompts.txt`**:
   - Berkas riwayat prompt telah diperbarui dengan seluruh prompt instruksi sesi ini di bagian atas.

---

## 4. STATUS GIT DAN LANGKAH SELANJUTNYA

- Perubahan pada `paper_outline_v1.1.md` dan `prompts.txt` siap untuk di-stage dan di-commit menggunakan Conventional Commits.
- Dokumentasi sesi telah dicatat di `docs/sessions/` dan cerminnya di `sessions/`.
- Tahap berikutnya: Melakukan commit dan push ke remote `origin/main`.
