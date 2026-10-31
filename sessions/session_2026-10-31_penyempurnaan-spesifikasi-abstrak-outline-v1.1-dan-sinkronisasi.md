# DOKUMENTASI SESI KERJA ANTIGRAVITY (AGY)
**Nama Berkas**: `docs/sessions/2026-10-31_penyempurnaan-spesifikasi-abstrak-outline-v1.1-dan-sinkronisasi.md`  
**Cermin Berkas**: `sessions/session_2026-10-31_penyempurnaan-spesifikasi-abstrak-outline-v1.1-dan-sinkronisasi.md`  
**Tanggal**: 31 Oktober 2026 – 1 November 2026  
**Waktu Sesi**: 21:30:00 – 00:15:00 WIB  
**Workspace**: `D:\Rafy\Research\face-race-gender-classification-using-multi-domain-vit`  
**Konteks Repositori**: `rafyakbar/face-race-gender-multi-vit`  
**Target Publikasi**: IEEE Access (ID Manuskrip: `Access-2026-50857`, Keputusan: *Reject & Resubmit* — 1 Kesempatan Resubmission Tunggal Berbasis *Binary Peer Review*)  
**Lingkungan Eksekusi**: Windows 11, Python 3.11+, Git SSH, Antigravity Agentic Assistant / Gemini 3.8 Flash (High)  

---

## 1. IKHTISAR DAN TUJUAN UTAMA SESI

Sesi kerja intensif ini berfokus pada audit akademik menyeluruh, penyempurnaan spesifikasi penulisan pada dokumen panduan `paper_outline_v1.1.md`, pemeliharaan format murni *paper outline* (spesifikasi instruksional berbasis poin-poin/checklist tanpa draf prosa langsung), serta sinkronisasi aturan sitasi dan riwayat prompt di seluruh repositori:

1. **Penyelarasan Spesifikasi Abstrak Sesuai 8 Batasan Ketat Pengguna & Referensi Abstrak Lama (`paper/00_abstract.md`):**
   - **Target Jumlah Kata:** Disesuaikan menjadi **150–250 kata** (standar artikel padat IEEE Access).
   - **Pembersihan Istilah Token Eksplisit:** Mengeliminasi seluruh penyebutan token arsitektur teknis seperti `[CLS]`.
   - **Penyelarasan Nomenklatur Model:** Menghapus label singkatan kustom (`ViT-Face`, `ViT-Emotion`, `ViT-Age`) dan menggantinya dengan deskripsi fungsional sesuai referensi lama: *"tiga model Vision Transformer (ViT) pre-trained spesifik tugas untuk biometrik wajah, ekspresi afektif, dan estimasi usia"*.
   - **Pembersihan Metrik Partisi Spesifik Subjek:** Menghapus penyebutan angka spesifik "120 subjek" maupun ukuran model di dalam Abstrak.
   - **Pembersihan Detail Hiperparameter:** Menghapus parameter pencarian *grid search* atau daftar parameter teknis dari spesifikasi abstrak.
   - **Pelaporan Dual-Benchmark Komparatif Lengkap:** Memasukkan hasil kuantitatif dari kedua protokol evaluasi:
     * *Split Stratified Class Biasa (Subject-Overlap)*: SVM Tri-Domain meraih Akurasi **93.70%** dan F1-Score **93.69%**.
     * *Zero Identity Leakage (Subject-Disjoint)*: Logistic Regression Tri-Domain meraih Akurasi **88.66%** dan F1-Score **88.68%**, disusul SVM Tri-Domain dengan Akurasi **88.61%** dan F1-Score **88.63%**.
   - **Preservasi Kata Kunci Resmi:** Menjaga keutuhan kata kunci sesuai formulir pengajuan IEEE: `Biometrics, face recognition, feature extraction, intersectional demographic recognition, multi-domain feature fusion, Vision Transformer.`
2. **Kepatuhan Format Murni Paper Outline (Bukan Draf Naratif Langsung):**
   - Menghapus blok draf teks prosa berkelanjutan (*draft prose*) yang sebelumnya sempat disisipkan secara tidak sengaja di bawah heading Abstrak.
   - Menstrukturkan kembali seksi Abstrak menjadi poin-poin checklist instruksional (*outline bullets*) yang terbagi rapi ke dalam: Latar Belakang & Tantangan, Metode yang Diusulkan, Evaluasi Dual-Benchmark & Hasil, dan Kesimpulan Generalisasi.
3. **Penegakan Disiplin Sitasi Global (Maksimal 2 Sitasi per Kalimat):**
   - Menambahkan aturan pembatasan sitasi maksimal 2 referensi per kalimat ke dalam berkas aturan: `rules/latex_rules.txt` (Seksi 6.1) dan `rules/md_rules.txt` (Seksi 7.4).
   - Menambahkan aturan ini ke dalam *Allowed Claims* (Butir 8) dan *Negative Constraints* (Butir 5) pada `paper_outline_v1.1.md` guna mencegah penumpukan sitasi (*citation dumping*).
   - Menghapus diagram alur naratif ASCII pada Bagian I (Introduction) dan diagram pohon hierarkis ASCII pada Bagian II (Related Works).
   - Menyesuaikan target kata Bagian I Paragraf 3 menjadi **135–250 kata** dan menghapus token `[CLS]` pada Paragraf 5.
4. **Audit Akademik Komprehensif Introduction (P3 & P4) & Related Works via Subagent:**
   - Menjalankan subagent riset independen untuk mengaudit keselarasan Bagian I dan II terhadap basis data telaah literatur di `related_works/`.
   - Melakukan koreksi venue publikasi Belcar et al. (2022) dari *Sensors* menjadi *Informatics* (MDPI) di 5 lokasi file.
   - Mendekonstruksi kluster sitasi pada II.A Paragraf 2 agar patuh pada aturan maksimal 2 sitasi per kalimat.
   - Mengoreksi ekspansi nama jurnal JIEET (Putri et al. 2025) menjadi *Journal of Information Engineering and Educational Technology* (UNESA).
   - Membersihkan entri Ramachandran & Rattani (2023) yang redundan pada II.C Paragraf 1.
5. **Audit Empiris dan Konfirmasi Komprehensif Dataset DemogPairs:**
   - Memverifikasi secara matematis dan empiris bahwa dataset DemogPairs terdiri atas **600 subjek/identitas unik** (100 subjek per kelas) dengan **tepat 18 variasi foto per subjek**, menghasilkan total **10.800 citra**.
   - Mengonfirmasi pembagian data latih 80% (480 subjek / 8.640 citra) dan data uji 20% (120 subjek / 2.160 citra) yang menjamin kondisi *Zero Identity Leakage* (subject-disjoint) tanpa tumpang tindih identitas lintas partisi maupun lintas kelas.
   - Memvalidasi komposisi sumber dataset primer: CWF (6.262 citra), VGGFace2 (4.186 citra), dan VGGFace (352 citra), selaras 100% dengan paper acuan utama Hupont & Fernández (IEEE FG 2019).
6. **Penyempurnaan Section III (Materials and Methods):**
   - Memadatkan penamaan kolom Table I menjadi ringkas: `| Subgroup | Race | Gender | Subjects | Train (80%) | Test (20%) | Total Images |`.
   - Memendekkan judul subseksi menjadi `### B. Vision Transformer Feature Extraction`.
   - Memecah target kata menjadi per paragraf mandiri: Paragraf 1 (**110–130 kata**) dan Paragraf 2 (**110–130 kata**).
   - Menyitasi korpus pra-latih ViT dari publikasi prekursor terdahulu Rezky Arisanti Putri: VGGFace2 (`skutaada/VIT-VGGFace`) dari Putri et al. (ICVEE 2025; JIEET 2025), FER-2013 (`dima806/facial_emotions_image_detection`) dari Putri et al. (ICVEE 2025), dan UTKFace + IMDB-WIKI (`dima806/facial_age_image_detection`) dari Putri et al. (JIEET 2025).
   - Menyeragamkan target kata keempat model klasifikasi hilir (III.C s.d. III.F) menjadi **100–125 kata**.
   - Menyederhanakan judul subseksi evaluasi menjadi `### H. Evaluation Metrics`.
7. **Pembersihan & Sinkronisasi Riwayat Prompt (`prompts.txt`):**
   - Menghapus duplikasi entri prompt dan menyinkronkan seluruh instruksi pengguna secara terurut kronologis terbalik di bawah header utama.

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
     - Memperbarui [rules/latex_rules.txt](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/rules/latex_rules.txt) (subseksi 6.1) dari batas 4 sitasi menjadi: *"Maksimal 2 sitasi dalam satu kalimat untuk mencegah penumpukan (citation dumping) dan menjaga keterbacaan naskah."*
     - Memperbarui [rules/md_rules.txt](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/rules/md_rules.txt) (subseksi 7.4) dari batas 4 sitasi menjadi: *"Maksimal 2 sitasi dalam satu kalimat untuk mencegah penumpukan sitasi (citation dumping) dan menjaga kepadatan sintaksis."*
  2. **Global Rules pada `paper_outline_v1.1.md`:**
     - Menambahkan Butir 8 pada Allowed Claims: *"Disiplin Sitasi Per Kalimat (Maksimal 2 Sitasi)"*.
     - Menambahkan Butir 5 pada Negative Constraints: *"Dilarang menumpuk lebih dari 2 sitasi dalam satu kalimat"*.
  3. **Introduction (`paper_outline_v1.1.md`):**
     - Menghapus diagram alur naratif ASCII 7 paragraf di bawah heading `## I. INTRODUCTION`.
     - Mengubah target kata Paragraph 3 dari 135–225 kata menjadi **135–250 kata**, serta mempertegas catatan aturan sitasi: *"Ditetapkan aturan ketat bahwa per kalimat hanya maksimal 2 sitasi untuk menjaga keterbacaan naskah dan mencegah penumpukan sitasi (citation dumping)"*.
     - Menghapus penyebutan token arsitektur `[CLS]` pada Paragraf 5 Poin 2, diselaraskan menjadi: *"Ekstraksi representasi laten visual dilakukan secara offline dari backbone Vision Transformer pra-latih yang dibekukan (frozen)..."*.
  4. **Related Works (`paper_outline_v1.1.md`):**
     - Menghapus struktur pohon ASCII `II. RELATED WORKS ├── A. ...` sehingga outline bersih dari diagram struktural yang tidak diperlukan.


### C. Audit Akademik Komprehensif Introduction (P3 & P4) & Related Works via Subagent
* **Permintaan Pengguna:**
  ```text
  sekarang tolong audit "I. INTRODUCTION - Paragraph 3 & Paragraph 4" dan "II. RELATED WORKS" apakah sudah sesuai dengan "related_works/" atau belum, delegasikan ke subagent
  ```
* **Hasil Eksekusi Subagent:**
  - Pendelegasian tugas audit komprehensif kepada subagent riset (`research`) untuk membandingkan Section I (P3 & P4) dan Section II (II.A–C beserta Eq. 1–4) terhadap berkas *ground truth* di direktori `related_works/` (`gap_analysis.md`, `literature_matrix.md`, `sintesis_literatur.md`, `tren_analisis.md`, dan 10 berkas `summaries/*.md`).
  - **Verdict Subagent**: **MINOR FIXES (Tingkat Keselarasan ~95%)**. Formulasi matematika Eq. 1 (KELM), Eq. 2 (Patch Flattening), Eq. 3 (MHSA), dan Eq. 4 (Concatenative Direct Sum) terbukti 100% akurat secara matematis dan selaras dengan literatur. Tiga pilar *research gap* pada Paragraf 4 juga 100% selaras dengan `gap_analysis.md`.
* **Tindakan Perbaikan yang Diterapkan:**
  1. **Koreksi Venue Belcar et al. (2022):** Mengoreksi atribusi jurnal dari *Sensors 2022* menjadi *Informatics 2022* (MDPI, Vol. 9, Art. 18, penulis: Belcar, Grd, & Tomičić) pada 5 lokasi di `paper_outline_v1.1.md` dan tabel `related_works/literature_matrix.md`.
  2. **Dekonstruksi Kalimat II.A Paragraf 2:** Memecah kalimat komparasi pengklasifikasi hilir yang sebelumnya menumpuk 4 sitasi (dan 3 sitasi sekaligus di akhir) menjadi 2 kalimat terpisah yang kohesif guna mematuhi aturan baku maksimal 2 sitasi per kalimat.
  3. **Pembersihan Rujukan II.C Paragraf 1:** Menghapus entri Ramachandran & Rattani (2023) dari daftar sumber II.C Paragraf 1 karena fokus paper tersebut berada pada mitigasi bias generatif di II.B Paragraf 2.
  4. **Koreksi Ekspansi Jurnal JIEET (Putri et al. 2025):** Memperbaiki penulisan kepanjangan JIEET dari *Journal of Integrated and Advanced Engineering* menjadi nama resmi *Journal of Information Engineering and Educational Technology* (UNESA).


### D. Audit Empiris dan Validasi Komprehensif Dataset DemogPairs
* **Permintaan Pengguna:**
  ```text
  coba audit terkait dataset demogpairs Terdiri atas 600 subjek/identitas unik (100 subjek per kelas), di mana setiap subjek memiliki tepat 18 variasi foto
  ```
* **Metodologi dan Temuan Audit:**
  1. **Struktur Kuantitatif Dataset:**
     - Total citra dalam repositori: **10.800 citra**.
     - Terbagi seimbang ke dalam 6 subgrup demografis interseksional ($6 \text{ kelas} \times 1.800 \text{ citra} = 10.800 \text{ citra}$):
       * Asian Female (`asian_female`): 1.800 citra.
       * Asian Male (`asian_male`): 1.800 citra.
       * Black Female (`black_female`): 1.800 citra.
       * Black Male (`black_male`): 1.800 citra.
       * White Female (`white_female`): 1.800 citra.
       * White Male (`white_male`): 1.800 citra.
  2. **Distribusi Subjek & Variasi Citra Per Subjek:**
     - Setiap kelas memiliki tepat **100 subjek/identitas unik**, menghasilkan total **600 subjek unik** di seluruh dataset.
     - Setiap subjek memiliki **tepat 18 variasi foto wajah** ($100 \text{ subjek} \times 18 \text{ variasi} = 1.800 \text{ citra per kelas}$).
     - Seluruh subjek bersifat *mutually exclusive* (nol tumpang tindih identitas antar kelas).
  3. **Distribusi Korpus Asal Citra (*Underlying Corpora*):**
     - Citra DemogPairs dikompilasi secara selektif dari tiga dataset wajah terkemuka:
       * **CWF (Celebrities in the Wild Faces)**: 6.262 citra (58,0%).
       * **VGGFace2**: 4.186 citra (38,8%).
       * **VGGFace**: 352 citra (3,2%).
  4. **Verifikasi Publikasi Acuan Primer:**
     - Hasil audit ini selaras 100% secara literatur dengan paper perancang dataset DemogPairs:
       * **Sitasi Primer**: I. Hupont and C. Fernández, "DemogPairs: Quantifying the Impact of Demographic Imbalances in Face Recognition," in *Proc. 14th IEEE Int. Conf. Autom. Face Gesture Recognit. (FG 2019)*, Lille, France, 2019, pp. 1–8.
  5. **Dampak pada Protokol Partisi *Subject-Disjoint* (Zero Identity Leakage):**
     - Partisi data latih 80% mengambil tepat 80 subjek per kelas ($80 \times 18 = 1.440$ citra/kelas; total 480 subjek / 8.640 citra).
     - Partisi data uji 20% mengambil sisa 20 subjek per kelas ($20 \times 18 = 360$ citra/kelas; total 120 subjek / 2.160 citra).
     - Hal ini menjamin bahwa seluruh 120 subjek pada data uji belum pernah dilihat (*unseen identities*) oleh model saat proses fitting classifier hilir.


### E. Penyempurnaan Section III (Materials and Methods) Sesuai Panduan Penulisan & Verifikasi Literatur Prekursor
* **Permintaan Pengguna:**
  ```text
  perbaiki paper_outline_v1.1.md:
  III. MATERIALS AND METHODS:
  A. Dataset: nama kolom pada Table I jangan terlalu panjang
  B. Vision Transformer:
      - judul terlalu panjang.
      - target kata harus per paragraf, tidak boleh gabungan.
      - mengenai " (3) Model card tidak mendokumentasikan korpus pra-latih (klaim "VGGFace2" dan "FER-2013" pada draf lama tidak terverifikasi dan dihapus; jangan ditulis ulang tanpa sumber": ini sumbernya ada pada penelitian sebelumnya yang authornya ada nama rezky nya, coba cek.
  C., D., E., F.: ubah target kata menjadi 100-125 kata
  H. Evaluation Metrics: namanya cukup evaluation metrics saja.
  perbaiki dengan sangat amat teliti, jika ingin cek-cek folder atau file terkait bisa delegasi subagent.
  ```
* **Tindakan yang Diambil:**
  1. **Penyederhanaan Header Table I:**
     - Mengubah header tabel pembagian dataset agar proporsional dan tidak melebihi lebar kolom IEEE:
       `| Subgroup | Race | Gender | Subjects | Train (80%) | Test (20%) | Total Images |`.
  2. **Penyelarasan Subseksi III.B (Vision Transformer Feature Extraction):**
     - Memadatkan judul subseksi dari `### B. Vision Transformer Multi-Domain Feature Extraction` menjadi `### B. Vision Transformer Feature Extraction`.
     - Membagi alokasi kata menjadi target per paragraf mandiri:
       * **Paragraph 1: 110–130 kata** (arsitektur ViT patch embedding, layer frozen, ekstraksi token [CLS] 768-D).
       * **Paragraph 2: 110–130 kata** (tiga model ViT spesifik tugas dan fusi concatenative direct sum 2.304-D).
     - **Verifikasi Sumber Korpus Pra-latih ViT:**
       Menelaah paper prekursor terdahulu yang ditulis oleh Rezky Arisanti Putri:
       * Putri et al. (IEEE ICVEE 2025): *"Facial Expression and Biometrics Feature Extraction using Vision Transformer for Demographic Classification"*.
       * Putri et al. (JIEET 2025): *"Multi-Feature Extraction of Facial Biometrics, Expression, and Age Estimation based on Vision Transformer"*, *Journal of Information Engineering and Educational Technology (JIEET)*, Vol. 9, No. 1, 2025.
       * Mengonfirmasi dan menyitasi secara formal:
         1. `skutaada/VIT-VGGFace`: di-fine-tune pada **VGGFace2** (Putri et al. IEEE ICVEE 2025; Putri et al. JIEET 2025).
         2. `dima806/facial_emotions_image_detection`: di-fine-tune pada **FER-2013** (Putri et al. IEEE ICVEE 2025).
         3. `dima806/facial_age_image_detection`: di-fine-tune pada **UTKFace dan IMDB-WIKI** (Putri et al. JIEET 2025).
       * Memperbarui teks Paragraf 2, kolom deskripsi Table II, serta Catatan Verifikasi Table II Butir (3) dengan sitasi formal ke paper Putri et al. (2025).
  3. **Penyeragaman Target Kata Klasifikasi Hilir (III.C s.d. III.F):**
     - Mengubah target kata keempat subseksi algoritma pengklasifikasi menjadi seragam **100–125 kata**:
       * III.C Random Forest Classifier: 100–125 kata.
       * III.D Gaussian Naive Bayes Classifier: 100–125 kata.
       * III.E Logistic Regression Classifier: 100–125 kata.
       * III.F Support Vector Machine Classifier: 100–125 kata.
  4. **Penyederhanaan Judul Evaluasi (III.H):**
     - Mengubah judul subseksi dari `### H. Evaluation Metrics & Statistical Testing` menjadi `### H. Evaluation Metrics`.


### F. Sinkronisasi dan Pembersihan Riwayat Prompt (`prompts.txt`)
* **Tindakan yang Diambil:**
  - Melakukan deduplikasi entri prompt yang berulang di [prompts.txt](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/prompts.txt).
  - Menyusun urutan riwayat prompt secara terstruktur dengan urutan kronologis terbalik (prompt terbaru paling atas langsung di bawah baris pemisah aturan baku).
  - Mencatat prompt audit DemogPairs dan prompt permintaan pembaruan dokumentasi sesi ke dalam urutan yang tepat.

---

## 3. HASIL VERIFIKASI FILE & MATRIKS STATUS

| Berkas | Status Verifikasi | Perubahan Kunci yang Diterapkan |
| :--- | :---: | :--- |
| [`paper_outline_v1.1.md`](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/paper_outline_v1.1.md) | **VALIDATED** | Penyelarasan Abstrak (150–250 kata, dual-benchmark, outline murni), aturan sitasi maks 2/kalimat, pembersihan ASCII diagram, koreksi venue Belcar et al. (MDPI Informatics), pemadatan Table I, judul & target kata III.B (110–130 per P), sitasi korpus ViT Putri et al. (2025), classifier 100–125 kata, judul III.H. |
| [`rules/latex_rules.txt`](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/rules/latex_rules.txt) | **VALIDATED** | Pembaruan aturan sitasi per kalimat (subseksi 6.1) menjadi maksimal 2 sitasi per kalimat. |
| [`rules/md_rules.txt`](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/rules/md_rules.txt) | **VALIDATED** | Pembaruan aturan sitasi per kalimat (subseksi 7.4) menjadi maksimal 2 sitasi per kalimat. |
| [`related_works/literature_matrix.md`](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/related_works/literature_matrix.md) | **VALIDATED** | Koreksi entri venue Belcar et al. (2022) menjadi MDPI Informatics 2022. |
| [`prompts.txt`](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/prompts.txt) | **VALIDATED** | Pembersihan duplikasi dan sinkronisasi seluruh riwayat prompt secara kronologis terbalik. |
| [`docs/sessions/2026-10-31_penyempurnaan-spesifikasi-abstrak-outline-v1.1-dan-sinkronisasi.md`](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/docs/sessions/2026-10-31_penyempurnaan-spesifikasi-abstrak-outline-v1.1-dan-sinkronisasi.md) | **UPDATED** | Dokumentasi komprehensif seluruh audit, perbaikan outline, dan sinkronisasi berkas sesi kerja. |
| [`sessions/session_2026-10-31_penyempurnaan-spesifikasi-abstrak-outline-v1.1-dan-sinkronisasi.md`](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/sessions/session_2026-10-31_penyempurnaan-spesifikasi-abstrak-outline-v1.1-dan-sinkronisasi.md) | **UPDATED** | Berkas cermin 1-to-1 dokumentasi sesi kerja di folder root. |

---

## 4. STATUS GIT DAN LANGKAH SELANJUTNYA

- Seluruh modifikasi pada naskah panduan `paper_outline_v1.1.md`, berkas `rules/`, `related_works/`, `prompts.txt`, serta dokumentasi sesi di `docs/sessions/` dan `sessions/` telah disinkronkan dan diverifikasi.
- Riwayat git commit sesi ini:
  * `6a4cf26`: `fix(outline): align literature citations and fix sentence clustering in outline v1.1`
  * `6505067`: `docs: record audit findings and synchronize session documentation`
  * `af873c2`: `docs(outline): refine Section III specifications, headings, and pretraining corpus citations`
  * `d14b4e2`: `docs: record Section III refinements and synchronize prompt log`
  * Commit berikutnya: Mengonsolidasikan dokumentasi komprehensif sesi, sinkronisasi cermin `sessions/`, dan pembersihan `prompts.txt`.
- **Langkah Kerja Berikutnya**:
  1. Melakukan commit dan push ke remote repository `origin/main`.
  2. Melanjutkan penulisan naskah revisi IEEE Access berbasis panduan `paper_outline_v1.1.md` yang telah terverifikasi secara matematis, empiris, dan literatur.
