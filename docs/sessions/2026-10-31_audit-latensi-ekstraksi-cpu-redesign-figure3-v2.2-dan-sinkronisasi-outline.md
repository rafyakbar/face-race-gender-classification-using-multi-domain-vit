# DOKUMENTASI SESI KERJA ANTIGRAVITY (AGY)
**Nama Berkas**: `docs/sessions/2026-10-31_audit-latensi-ekstraksi-cpu-redesign-figure3-v2.2-dan-sinkronisasi-outline.md`  
**Cermin Berkas**: `sessions/session_2026-10-31_audit-latensi-ekstraksi-cpu-redesign-figure3-v2.2-dan-sinkronisasi-outline.md`  
**Tanggal**: 31 Oktober 2026  
**Waktu Sesi**: 19:15:00 – 20:00:00 WIB  
**Workspace**: `D:\Rafy\Research\face-race-gender-classification-using-multi-domain-vit`  
**Konteks Repositori**: `rafyakbar/face-race-gender-classification-using-multi-domain-vit`  
**Target Publikasi**: IEEE Access (ID Manuskrip: `Access-2026-50857`, Keputusan: *Reject & Resubmit* — 1 Kesempatan Resubmission Tunggal Berbasis *Binary Peer Review*)  
**Lingkungan Eksekusi**: Windows 11, Python 3.11+ (Conda `torch-gpu`), Git SSH, Antigravity Agentic Assistant / Gemini 3.8 Flash (High)  

---

## 1. IKHTISAR DAN TUJUAN UTAMA SESI

Sesi kerja intensif pada 31 Oktober 2026 difokuskan pada lima pilar krusial dalam mempersiapkan naskah resubmission IEEE Access:
1. **Audit & Evaluasi Perancangan Ulang Figure 3 (Reviewer 1 Poin 3):**
   - Menelaah diagram arsitektur Vision Transformer pada berkas PowerPoint `images/vit_v2.2.pptx`.
   - Mengonfirmasi kepatuhan terhadap masukan Reviewer 1 (eksplisit menampilkan 3 cabang backbone ViT yang dibekukan, ekstraksi token [CLS] layer-12 768-D per domain, fusi direct sum 2.304-D $z_{\text{tri}}$, dan klasifikasi 6 kelas interseksional).
   - Mengekspor diagram ke format PNG resolusi tinggi 300 DPI (`images/vit_v2.2.png`) dan menyinkronkannya ke folder manuskrip (`paper/images/`, `paper_latex_en/images/`, `paper_latex_id/images/`).
2. **Audit Kritis dan Penyelarasan `paper_outline_v1.1.md` terhadap Komentar Reviewer IEEE:**
   - Mengoreksi inkonsistensi nilai normalisasi citra ViT pada Tabel II dari ImageNet standard (`[0.485, 0.456, 0.406]`) ke konfigurasi empiris HuggingFace preprocessor yang sebenarnya digunakan pada eksperimen (`[0.5, 0.5, 0.5]`).
   - Mengoreksi klaim overclaim konfusi lintas-gender pada Bagian IV.E: mengubah klaim fiktif `"<0.4%"` menjadi angka empiris yang terbukti secara matematis dari matriks konfusi (80 citra atau 3,70% pada LR Tri; 69 citra atau 3,19% pada SVM Tri), serta mengkuantifikasi bahwa mayoritas kesalahan (67,3% atau 165 citra) merupakan kesalahan intra-gender lintas-ras (*same-gender cross-race*).
   - Mengintegrasikan rujukan langkah ①–⑦ pada diagram Figure 3 v2.2 secara eksplisit ke dalam narasi metodologi Bagian III.B.
   - Menambahkan Tabel XIV (profil efisiensi komputasi terverifikasi) dan Tabel XVI (struktur komparasi literatur kontekstual vs terkontrol).
3. **Regenerasi Aset Visual Matriks Konfusi 6×6 Figure 4 (Reviewer 1 Poin 4 & Reviewer 2 Poin 9):**
   - Mengomputasi ulang matriks konfusi 6×6 dari `y_test` dan `y_pred` pada set uji held-out ($N=2.160$) untuk model Logistic Regression (Single Face, Dual Emotion+Face, Tri-Domain).
   - Memastikan pengurutan label matriks konfusi konsisten dengan indeks resmi `DEMOGPairs_LABEL_TO_IDX` dan menghasilkan berkas gambar resolusi tinggi (`images/confusion_matrix_lr_{single,dual,tri}_v1.1.png`).
4. **Audit Empiris Teliti atas Waktu Komputasi dan Kecepatan Ekstraksi Citra (`experiment/code/md/`):**
   - Menjawab pertanyaan pengguna mengenai urgensi pelaporan kecepatan citra (Reviewer 1 #5 & Reviewer 2 #8).
   - Melakukan inspeksi baris demi baris pada log ekstraksi fitur ViT (`1.1_vit-face.md`, `1.1_vit-emotion.md`, `1.1_vit-age.md`).
   - Menemukan fakta empiris fundamental: **seluruh proses ekstraksi fitur pada repositori ini dieksekusi pada CPU (`device(type='cpu')`) dengan `batch_size = 1`**.
   - Menghitung secara eksak throughput dan latensi ekstraksi: Face 467,04 ms/citra (2,14 it/s), Emotion 476,67 ms/citra (2,10 it/s), Age 543,06 ms/citra (1,84 it/s); total Tri-Domain 1.486,76 ms/citra (~1,49 s/citra; total seluruh dataset 10.800 citra = 4 jam 27 menit 37 detik).
   - Mengklarifikasi bahwa angka lama `"~15.2 ms GPU"` dan `"~45.6 ms total"` pada draf lama adalah estimasi hipotetis server GPU yang tidak memiliki log empiris di repositori, sehingga penyajian data CPU empiris justru menjamin kejujuran ilmiah 100%.
   - Mengompilasi profil lengkap 28 model klasifikasi hilir (waktu latih 5-fold, latensi inferensi batch, dan ukuran model).
5. **Manajemen Git Commit & Sinkronisasi Remote:**
   - Membagi seluruh pekerjaan ke dalam 3 commit logis atomik berstandar *Conventional Commits*.
   - Menerbitkan commit ke branch `main` dan melakukan `git push` ke GitHub remote repository.

---

## 2. KRONOLOGI PERMINTAAN PENGGUNA & TINDAKAN YANG DIAMBIL

### A. Pembelajaran Cepat Repositori dan Fokus pada Figure 3 v2.2
* **Permintaan Pengguna:**
  1. *"pelajari: 1. README.md, 2. paper/, 3. paper_reviews_ieee/, 4. experiment/code/archive/md_old/, 5. experiment/code/md/, 6. paper_outline_v1.1.md. pelajari dengan cepat"*
  2. *"sekarang fokus pada komentar Reviewer 1 mengenai Perancangan Ulang dan Penjelasan Figure 3 (paper_reviews_ieee/Comments.md). apakah images/vit_v2.2.pptx sudah sesuai?"*
* **Tindakan yang Diambil:**
  - Melakukan inspeksi menyeluruh terhadap seluruh berkas kunci repositori, arsitektur eksperimen subject-disjoint, dan komentar reviewer IEEE Access.
  - Memeriksa struktur diagram PowerPoint `images/vit_v2.2.pptx`:
    1. Mengonfirmasi bahwa diagram telah memperbaiki kelemahan Figure 3 lama (`images/vit.png`) yang hanya menampilkan 1 ViT generik.
    2. Mengonfirmasi bahwa versi 2.2 secara eksplisit menggambarkan alur 3 backbone paralel (`ViT-Face`, `ViT-Emotion`, `ViT-Age`), penanda status bobot dibekukan (*frozen*), ekstraksi token [CLS] layer-12 768-D per domain, fusi konkatenasi *direct sum* 2.304-D, dan klasifikasi 6 kelas interseksional.
    3. Memberikan evaluasi bahwa `vit_v2.2.pptx` telah 100% memenuhi masukan Reviewer 1 Poin 3.

### B. Konversi ke PNG & Sinkronisasi Folder Publikasi
* **Permintaan Pengguna:**
  *"tolong convert ke png"* $\to$ *"lanjutkan"*
* **Tindakan yang Diambil:**
  - Mengonversi `images/vit_v2.2.pptx` slide 1 ke berkas gambar PNG beresolusi tinggi 300 DPI (`images/vit_v2.2.png`).
  - Menyalin dan menyinkronkan aset gambar `vit_v2.2.png` ke:
    - [`paper/images/vit_v2.2.png`](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/paper/images/vit_v2.2.png)
    - [`paper_latex_en/images/vit_v2.2.png`](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/paper_latex_en/images/vit_v2.2.png)
    - [`paper_latex_id/images/vit_v2.2.png`](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/paper_latex_id/images/vit_v2.2.png)

### C. Audit Kritis dan Perbaikan `paper_outline_v1.1.md`
* **Permintaan Pengguna:**
  1. *"tolong audit paper_outline_v1.1.md apakah sudah sesuai dengan paper_reviews_ieee atau belum"*
  2. *"tolong perbaiki paper outline nya"* $\to$ *"lanjutkan"*
* **Tindakan yang Diambil:**
  - Menemukan sejumlah ketidaksesuaian kritis antara draf outline dengan log empiris dan komentar reviewer:
    1. *Tabel II*: Normalisasi citra ViT sebelumnya tertulis standar ImageNet `mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]`. Divalidasi langsung ke `preprocessor_config.json` HuggingFace ketiga model, nilai riilnya adalah `mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5]`. Nilai pada Tabel II langsung dikoreksi.
    2. *Section IV.E (Error Analysis)*: Klaim lama menyebutkan tingkat kesalahan lintas-gender *"<0.4%"*. Berdasarkan audit matriks konfusi `demogpairs_lr_vit-face-emotion-age_LogisticRegression.json`, kesalahan lintas-gender tercatat **80 citra (3,70% dari N=2.160)** pada LR Tri dan **69 citra (3,19%)** pada SVM Tri. Kesalahan didominasi oleh intra-gender lintas-ras (**165 citra / 67,3% dari total 245 kesalahan LR Tri**). Outline dikoreksi total agar berbasis bukti empiris murni.
    3. *Section III.B*: Menghubungkan narasi teks secara eksplisit dengan langkah bernomor ①–⑦ pada Figure 3 v2.2.
    4. *Tabel XIV & XVI*: Menambahkan matriks waktu pelatihan 5-fold, latensi inferensi, dan perbandingan literatur terstruktur (Bagian A kontekstual vs Bagian B terkontrol).
    5. Menghasilkan aset matriks konfusi terstandardisasi `images/confusion_matrix_lr_{single,dual,tri}_v1.1.png`.

### D. Audit Komprehensif Kecepatan Citra dari Log Eksperimen
* **Permintaan Pengguna:**
  1. *"kenapa harus ada kecepatan citra? apakah ada komentar dari reviewer terkait itu?"*
  2. *"untuk itu bisa dicek dan dihitung dari: experiment/code/md/1.1_vit-age.md, experiment/code/md/1.1_vit-emotion.md, experiment/code/md/1.1_vit-face.md, experiment/code/md coba cek dengan sangat amat teliti"*
* **Tindakan yang Diambil:**
  - Menjelaskan urgensi pelaporan kecepatan citra berdasarkan komentar penelaah:
    - **Reviewer 1 Poin 5**: *"It is recommended that the author consider the time cost in the evaluation."*
    - **Reviewer 2 Poin 8**: *"report the computational environment, feature extraction time, classifier training time, inference latency, memory consumption, and model storage requirements."*
  - Mengembangkan skrip parsing terinci untuk memeriksa berkas log di `experiment/code/md/1.1_vit-*.md` dan 28 berkas JSON hasil evaluasi di `experiment/code/results/`.
  - Melakukan verifikasi matematis dan logaritma komputasi untuk seluruh metrik waktu, latensi, dan ukuran model (rincian lengkap disajikan pada Bagian 3).

### E. Manajemen Git Commit Atomik dan Push Remote
* **Permintaan Pengguna:**
  *"Identifikasi dan pelajari perubahan yang telah terjadi dilakukan, jika bisa dibuat menjadi beberapa commit, maka buat menjadi beberapa commit! Sekarang buat commit untuk perubahan-perubahan tersebut dan PUSH! Gunakan skill 'git-commit' atau sesuai dengan best practice!"*
* **Tindakan yang Diambil:**
  - Mengidentifikasi seluruh perubahan uncommitted dan untracked.
  - Memilah perubahan menjadi 3 commit atomik logis berstandar *Conventional Commits*:
    1. `6d44881` (`feat(figures)`): Redesign Figure 3 architecture to v2.2.
    2. `1fa206a` (`feat(figures)`): Standardized 6x6 confusion matrices for LR ablation.
    3. `e911dc6` (`docs(outline)`): Align paper outline v1.1 and prompts with IEEE Access review audit.
  - Mendorong (*push*) commit ke `origin/main` di GitHub dan memverifikasi kondisi working tree bersih (*clean*).

---

## 3. BUKU BESAR HASIL AUDIT METRIK KOMPUTASI & LATENSI EMPIRIS

### A. Ekstraksi Fitur Vision Transformer (10.800 Citra DemogPairs)
*Lingkungan Runtime: CPU Murni (`device(type='cpu')`), batch size = 1, I/O disk sekuensial.*

| Domain Fitur | Model HuggingFace | Total Citra | Waktu Log Tqdm | Durasi Total (s) | Throughput Empiris | Latensi per Citra (ms) | Dimensi CLS Token |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Wajah (*Face*)** | `skutaada/VIT-VGGFace` | 10.800 | `1:24:04` | 5.044 s (1,40 jam) | **2,14 it/s** | **467,04 ms** | (768,) |
| **Emosi (*Emotion*)** | `dima806/facial_emotions_image_detection` | 10.800 | `1:25:48` | 5.148 s (1,43 jam) | **2,10 it/s** | **476,67 ms** | (768,) |
| **Umur (*Age*)** | `dima806/facial_age_image_detection` | 10.800 | `1:37:45` | 5.865 s (1,63 jam) | **1,84 it/s** | **543,06 ms** | (768,) |

#### Latensi Akumulatif Ekstraksi Fitur (Pipeline Serial):
- **Single-Domain**: Face: 467,04 ms | Emotion: 476,67 ms | Age: 543,06 ms
- **Dual-Domain (`Emotion ⊕ Face`)**: $476,67 + 467,04 = \mathbf{943,71\text{ ms/citra}}$ (0,94 s; total 10.800 citra: 2 jam 49 menit 52 detik)
- **Dual-Domain (`Face ⊕ Age`)**: $467,04 + 543,06 = \mathbf{1.010,10\text{ ms/citra}}$ (1,01 s; total 10.800 citra: 3 jam 01 menit 49 detik)
- **Dual-Domain (`Emotion ⊕ Age`)**: $476,67 + 543,06 = \mathbf{1.019,73\text{ ms/citra}}$ (1,02 s; total 10.800 citra: 3 jam 03 menit 33 detik)
- **Tri-Domain (`Face ⊕ Emotion ⊕ Age`)**: $467,04 + 476,67 + 543,06 = \mathbf{1.486,76\text{ ms/citra}}$ ($\mathbf{\approx 1,49\text{ detik/citra}}$)
  - **Total Waktu Ekstraksi Dataset Tri-Domain:** $5.044 + 5.148 + 5.865 = \mathbf{16.057\text{ detik}} = \mathbf{267,62\text{ menit}} = \mathbf{4\text{ jam } 27\text{ menit } 37\text{ detik}}$.

### B. Evaluasi Klasifikasi Hilir: 28 Model Benchmark Subject-Disjoint
*Data Uji Held-Out Independen: 120 Subjek Baru / 2.160 Citra Uji.*

| Klasifier | Fitur | Akurasi | Waktu Latih 5-Fold (s) | Waktu Latih (Menit / Jam) | Total Waktu Inferensi (s) | Latensi per Sampel (ms) | Ukuran File Model (MB) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **LR** | `vit-face-emotion-age` (Tri) | **88,66%** | **3.287,07 s** | **54,78 m** | **0,0098 s** | **0,0046 ms** | **0,11 MB** |
| **LR** | `vit-emotion-face` (Dual) | 87,45% | 1.941,15 s | 32,35 m | 0,0075 s | 0,0035 ms | 0,08 MB |
| **LR** | `vit-face-age` (Dual) | 87,41% | 1.825,33 s | 30,42 m | 0,0120 s | 0,0056 ms | 0,11 MB |
| **LR** | `vit-emotion-age` (Dual) | 86,67% | 1.796,56 s | 29,94 m | 0,0075 s | 0,0035 ms | 0,08 MB |
| **LR** | `vit-face` (Single) | 86,39% | 833,89 s | 13,90 m | 0,0017 s | 0,0008 ms | 0,04 MB |
| **LR** | `vit-emotion` (Single) | 85,23% | 775,85 s | 12,93 m | 0,0070 s | 0,0032 ms | 0,06 MB |
| **LR** | `vit-age` (Single) | 81,48% | 782,22 s | 13,04 m | 0,0042 s | 0,0019 ms | 0,06 MB |
| **SVM** | `vit-face-emotion-age` (Tri) | **88,61%** | **30.666,02 s** | **511,10 m (8,52 jam)** | **10,1057 s** | **4,6785 ms** | **36,60 MB** |
| **SVM** | `vit-emotion-face` (Dual) | 88,43% | 18.576,07 s | 309,60 m (5,16 jam) | 2,0498 s | 0,9490 ms | 15,27 MB |
| **SVM** | `vit-face-age` (Dual) | 87,55% | 29.541,08 s | 492,35 m (8,21 jam) | 5,5010 s | 2,5468 ms | 23,48 MB |
| **SVM** | `vit-emotion-age` (Dual) | 86,25% | 24.482,36 s | 408,04 m (6,80 jam) | 8,0413 s | 3,7228 ms | 32,76 MB |
| **SVM** | `vit-face` (Single) | 86,16% | 9.997,44 s | 166,62 m (2,78 jam) | 0,7858 s | 0,3638 ms | 7,56 MB |
| **SVM** | `vit-emotion` (Single) | 85,79% | 15.207,00 s | 253,45 m (4,22 jam) | 3,7752 s | 1,7478 ms | 15,30 MB |
| **SVM** | `vit-age` (Single) | 82,55% | 14.673,08 s | 244,55 m (4,08 jam) | 4,7926 s | 2,2188 ms | 18,22 MB |
| **RF** | `vit-face-emotion-age` (Tri) | 85,00% | 6.628,03 s | 110,47 m (1,84 jam) | 0,0723 s | 0,0334 ms | 6,19 MB |
| **RF** | `vit-emotion-face` (Dual) | 84,86% | 4.126,01 s | 68,77 m | 0,0619 s | 0,0286 ms | 8,58 MB |
| **RF** | `vit-face-age` (Dual) | 84,86% | 4.098,86 s | 68,31 m | 0,0673 s | 0,0312 ms | 6,19 MB |
| **RF** | `vit-face` (Single) | 84,03% | 2.324,29 s | 38,74 m | 0,0716 s | 0,0332 ms | 5,99 MB |
| **RF** | `vit-emotion-age` (Dual) | 77,31% | 4.161,13 s | 69,35 m | 0,0702 s | 0,0325 ms | 12,35 MB |
| **RF** | `vit-emotion` (Single) | 76,11% | 2.465,57 s | 41,09 m | 0,0694 s | 0,0321 ms | 10,34 MB |
| **RF** | `vit-age` (Single) | 71,81% | 2.372,49 s | 39,54 m | 0,0544 s | 0,0252 ms | 11,21 MB |
| **GNB** | `vit-emotion-face` (Dual) | 84,31% | 1.529,47 s | 25,49 m | 0,0190 s | 0,0088 ms | 0,78 MB |
| **GNB** | `vit-face-emotion-age` (Tri) | 83,61% | 3.250,06 s | 54,17 m | 0,0139 s | 0,0064 ms | 1,36 MB |
| **GNB** | `vit-face-age` (Dual) | 83,06% | 1.587,84 s | 26,46 m | 0,0150 s | 0,0069 ms | 0,75 MB |
| **GNB** | `vit-face` (Single) | 82,55% | 571,00 s | 9,52 m | 0,0077 s | 0,0035 ms | 0,19 MB |
| **GNB** | `vit-emotion-age` (Dual) | 75,88% | 1.527,46 s | 25,46 m | 0,0090 s | 0,0042 ms | 0,24 MB |
| **GNB** | `vit-emotion` (Single) | 72,13% | 563,99 s | 9,40 m | 0,0052 s | 0,0024 ms | 0,13 MB |
| **GNB** | `vit-age` (Single) | 67,08% | 548,64 s | 9,14 m | 0,0076 s | 0,0035 ms | 0,37 MB |

### C. Analisis Latensi Pipa Lengkap (End-to-End Latency)
$$\text{Latensi Total} = \text{Latensi Ekstraksi ViT (CPU)} + \text{Latensi Klasifikasi}$$
1. **Tri-Domain + Logistic Regression (LR):**
   - ViT Extraction (3 model di CPU): $1.486,76\text{ ms}$ (99,9997% waktu)
   - LR Classification: $0,0046\text{ ms}$ (0,0003% waktu)
   - **Total Pipeline:** $\mathbf{1.486,7646\text{ ms}}$ ($\approx \mathbf{1,487\text{ detik/citra}}$).
2. **Tri-Domain + Support Vector Machine (SVM):**
   - ViT Extraction (3 model di CPU): $1.486,76\text{ ms}$ (99,69% waktu)
   - SVM Classification: $4,6785\text{ ms}$ (0,31% waktu)
   - **Total Pipeline:** $\mathbf{1.491,4385\text{ ms}}$ ($\approx \mathbf{1,491\text{ detik/citra}}$).
3. **Keunggulan Relatif LR terhadap SVM pada Fusi Tri-Domain:**
   - **Kecepatan Pelatihan**: LR 9,33$\times$ lebih cepat dilatih ($54,78\text{ m}$ vs $511,10\text{ m} / 8,52\text{ jam}$).
   - **Kecepatan Inferensi Klasifier**: LR 1.017$\times$ lebih cepat ($0,0046\text{ ms}$ vs $4,6785\text{ ms}$).
   - **Efisiensi Penyimpanan**: LR 332,7$\times$ lebih ringkas ($0,11\text{ MB}$ vs $36,60\text{ MB}$).

---

## 4. INVENTARIS PERUBAHAN BERKAS & COMMIT GIT

### A. Tabel Berkas yang Dimodifikasi dan Dibuat

| No | Berkas | Status Tindakan | Deskripsi Perubahan Utama |
|:---:|---|:---:|---|
| 1 | [`images/vit_v2.1.pptx`](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/images/vit_v2.1.pptx) & `vit_v2.1.png` | Ditambahkan (*Added*) | Draf perbaikan diagram arsitektur ViT paralel versi 2.1. |
| 2 | [`images/vit_v2.2.pptx`](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/images/vit_v2.2.pptx) & `vit_v2.2.png` | Ditambahkan (*Added*) | Diagram arsitektur final Figure 3 v2.2 resolusi 300 DPI dengan anotasi 3 backbone ViT, token CLS 768-D, fusi konkatenasi 2.304-D, dan klasifikasi 6 kelas. |
| 3 | [`paper/images/vit_v2.2.png`](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/paper/images/vit_v2.2.png) | Ditambahkan (*Added*) | Sinkronisasi aset visual diagram ke direktori naskah Markdown. |
| 4 | [`paper_latex_en/images/vit_v2.2.png`](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/paper_latex_en/images/vit_v2.2.png) | Ditambahkan (*Added*) | Sinkronisasi aset visual diagram ke template LaTeX Bahasa Inggris. |
| 5 | [`paper_latex_id/images/vit_v2.2.png`](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/paper_latex_id/images/vit_v2.2.png) | Ditambahkan (*Added*) | Sinkronisasi aset visual diagram ke template LaTeX Bahasa Indonesia. |
| 6 | [`images/confusion_matrix_lr_single_v1.1.png`](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/images/confusion_matrix_lr_single_v1.1.png) | Ditambahkan (*Added*) | Matriks konfusi 6×6 terstandardisasi Single-Domain (Face) Logistic Regression. |
| 7 | [`images/confusion_matrix_lr_dual_v1.1.png`](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/images/confusion_matrix_lr_dual_v1.1.png) | Ditambahkan (*Added*) | Matriks konfusi 6×6 terstandardisasi Dual-Domain (`Emotion ⊕ Face`) Logistic Regression. |
| 8 | [`images/confusion_matrix_lr_tri_v1.1.png`](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/images/confusion_matrix_lr_tri_v1.1.png) | Ditambahkan (*Added*) | Matriks konfusi 6×6 terstandardisasi Tri-Domain (`Face ⊕ Emotion ⊕ Age`) Logistic Regression. |
| 9 | [`paper_outline_v1.1.md`](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/paper_outline_v1.1.md) | Diperbarui (*Modified*) | Audit dan kalibrasi penuh normalisasi Tabel II, narasi Figure 3 langkah ①–⑦, angka kesalahan empiris Bagian IV.E, Tabel XIV profil komputasi CPU, dan Tabel XVI komparasi literatur. |
| 10 | [`prompts.txt`](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/prompts.txt) | Diperbarui (*Modified*) | Sinkronisasi riwayat prompt aktif dan arahan audit komputasi. |

### B. Daftar Git Commit yang Diterbitkan ke Remote Repository

```text
commit 6d44881c3a1582a98022e0f837067b491f11fd94
Author: rafy683 <rafy683@gmail.com>
Date:   Sat Oct 31 19:42:11 2026 +0700
    feat(figures): redesign Figure 3 architecture to v2.2 with explicit multi-domain ViT pipeline

commit 1fa206a4b8bf6ee104049f3b27c7b3d7faf1d608
Author: rafy683 <rafy683@gmail.com>
Date:   Sat Oct 31 19:42:23 2026 +0700
    feat(figures): add standardized 6x6 confusion matrices for LR ablation (v1.1)

commit e911dc64631a5e070716d1de744f3c3c66f97b4d
Author: rafy683 <rafy683@gmail.com>
Date:   Sat Oct 31 19:42:38 2026 +0700
    docs(outline): align paper outline v1.1 and prompts with IEEE Access review audit
```

Status sinkronisasi remote: `3036167..e911dc6  main -> main` (**Sinkron Penuh & Bersih**).

---

## 5. STATUS DAN KESIAPAN TAHAP SELANJUTNYA

* **Integritas Outline Manuskrip**: [paper_outline_v1.1.md](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/paper_outline_v1.1.md) kini telah menjadi cetak biru (*master blueprint*) yang 100% konsisten, terlacak ke data eksperimen riil, bebas dari spekulasi klaim GPU yang tidak terbukti, dan memiliki mitigasi konkret untuk seluruh 17 poin keberatan penelaah IEEE Access.
* **Aset Visual & Diagramatik**:
  - Figure 3 v2.2 siap digunakan dan telah disalin ke seluruh folder manuskrip LaTeX dan Markdown.
  - Figure 4 (matriks konfusi v1.1) telah siap dengan pengurutan kelas standar.
* **Rekomendasi Tindakan Berikutnya**:
  1. Memulai eksekusi penulisan naskah lengkap pada [`paper/`](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/paper/) (Bab I s.d. V) mengacu langsung pada rincian per-paragraf di `paper_outline_v1.1.md`.
  2. Menyusun surat tanggapan formal penelaah (*Response to Reviewers*) pada [`paper_reviews_ieee/10_response_letter_skeleton.md`](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/paper_reviews_ieee/10_response_letter_skeleton.md) menggunakan data empiris CPU terverifikasi yang telah diaudit pada sesi ini.
  3. Mengompilasi naskah ke template resmi IEEE Access LaTeX (`paper_latex_en/`) untuk menghasilkan draf naskah final bersih dan *highlighted revised version*.
