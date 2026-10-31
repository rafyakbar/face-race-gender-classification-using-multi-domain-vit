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
