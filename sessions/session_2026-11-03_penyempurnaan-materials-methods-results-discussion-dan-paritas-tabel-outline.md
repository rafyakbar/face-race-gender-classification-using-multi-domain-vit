# DOKUMENTASI SESI KERJA ANTIGRAVITY (AGY)
**Nama Berkas**: `sessions/session_2026-11-03_penyempurnaan-materials-methods-results-discussion-dan-paritas-tabel-outline.md`  
**Tanggal**: 03 November 2026  
**Waktu Sesi**: 11:00:00 – 12:30:00 WIB  
**Workspace**: `D:\Research\face-race-gender-classification-using-multi-domain-vit`  
**Konteks Repositori**: `rafyakbar/face-race-gender-classification-using-multi-domain-vit`  
**Target Publikasi**: IEEE Access (ID Manuskrip: `Access-2026-50857`, Keputusan: *Reject & Resubmit* — 1 Kesempatan Resubmission Tunggal Berbasis *Binary Peer Review*)  
**Lingkungan Eksekusi**: Windows 11, Python 3.11+, Git SSH, Antigravity Agentic Assistant / Gemini 3.8 Flash (High)  

---

## 1. IKHTISAR DAN TUJUAN UTAMA SESI

Sesi kerja intensif pada 2–3 November 2026 difokuskan pada penyempurnaan menyeluruh dan finalisasi Master Outline Manuskrip revisi IEEE Access ([`paper_outline_v1.1.md`](../paper_outline_v1.1.md)):
1. **Rekonstruksi Section III (Materials and Methods)**:
   - Penyederhanaan kolom pada Tabel I Distribusi Dataset DemogPairs (`Subgroup, Subjects, Train (80%), Test (20%), Total`).
   - Restrukturisasi subseksi Vision Transformer menjadi tepat 3 paragraf tematik, meniadakan tabel spesifikasi checkpoint terpisah dan mengintegrasikan rincian checkpoint HuggingFace (`skutaada/VIT-VGGFace`, `dima806/facial_emotions_image_detection`, `dima806/facial_age_image_detection`), korpus pra-latih, normalisasi kanal $\mu=\sigma=[0.5, 0.5, 0.5]$, dan *in-memory processor caching* secara naratif.
   - Penyelarasan format ruang pencarian hyperparameter untuk 4 classifier klasik (Tabel III Random Forest, Tabel IV Gaussian Naive Bayes, Tabel V Logistic Regression, Tabel VI Support Vector Machine) agar konsisten dengan `paper_outline_v1.0.md`.
   - Penyusunan subseksi baru **III.I (Computational Environment and Experimental Setup)** mencakup perangkat keras (Intel Core i9-13900H, RAM 32GB DDR5, GPU NVIDIA RTX 4060 8GB), arsitektur alokasi beban (ekstraksi fitur pada GPU vs training 5-Fold GridSearchCV pada CPU), serta *stack* perangkat lunak (Python, PyTorch, Scikit-learn).
2. **Restrukturisasi Total Section IV (Results and Discussion)**:
   - Mengembalikan penamaan dan alur judul subseksi agar selaras dengan `paper_outline_v1.0.md` namun mengakomodasi secara ketat seluruh tuntutan penelaah IEEE Access (`paper_reviews_ieee/Comments.md`).
   - Mengintegrasikan hasil empiris Primary Benchmark Subject-Disjoint ($N = 2.160$ data uji terisolasi) dari `experiment/code/md/` ke dalam tabel performa global (Table VII RF, Table VIII GNB, Table IX LR, Table X SVM).
   - Menyusun **Table XI (Computational Efficiency and Resource Consumption Profile)** berformat Full Width (`table*`) dengan waktu ekstraksi GPU (ms/citra), durasi training CPU dalam satuan menit, latensi inferensi (ms/sampel), ukuran model (MB), dan RAM footprint.
   - Menyertakan **Table XII (Studi Komparatif Ablasi Kebocoran Data)** dan **Table XIII (Uji McNemar Berpasangan & Exact Binomial Test)** pada Subseksi IV.B.
   - Menyertakan **Table XIV (Intersectional Subgroup Performance & Fairness Profile)** pada Subseksi IV.C.
   - Menyertakan **Figure 4 (Confusion Matrices LR Single, Dual, Tri)** beserta 3 tabel matriks acuan angka empiris non-numbered pada Subseksi IV.D.
   - Menyertakan **Table XV (Perbandingan Kontekstual Bagian A vs Terkontrol Bagian B)** pada Subseksi IV.E.
3. **Penyelarasan Paritas Visual Tabel & Gambar terhadap `v1.0`**:
   - Menampilkan berkas gambar komposit `sample_demogpairs.png` pada Figure 2 di samping 6 citra sampel individual.
   - Menstandardisasi blok penyajian Figure 1–4 (`Sitasi Gambar Wajib`, `Ketentuan Layout LaTeX`, `Caption Figure`, `Visual Markdown`).
   - Memastikan seluruh tabel utama (Table I, II, VII–XV) memiliki spesifikasi layout LaTeX dan label subjudul bahasa Indonesia eksplisit.
4. **Penyederhanaan Kolom Tabel IV.A (Eliminasi `95% CI`)**:
   - Menghapus kolom redundan `95% CI` dari Tabel VII, VIII, IX, dan X sehingga kembali ramping menjadi 6 kolom standar persis `v1.0`.
   - Nilai 95% Wilson Score CI tetap dipertahankan dan didokumentasikan di dalam teks narasi paragraf untuk model puncak (LR Tri `88.66% [87.25%, 89.93%]` dan SVM Tri `88.61% [87.20%, 89.88%]`).
5. **Kepatuhan Master Elemen & Peluncuran Git**:
   - Memverifikasi kronologis 4 Figures (Figure 1–4), 15 Tables (Table I–XV), dan 23 Equations (Eq. 1–23).
   - Menerbitkan commit Git `0e5167e` dan mendorong (*push*) ke remote GitHub `main`.

---

## 2. KRONOLOGI PERMINTAAN PENGGUNA & TINDAKAN YANG DIAMBIL

### A. Tahap 1: Rekonstruksi Section III (Materials and Methods)
* **Permintaan Pengguna:** Memperbaiki outline Section III: Table I sederhanakan kolom; ViT bagi 3 paragraf naratif tanpa tabel spesifikasi checkpoint terpisah; samakan RF, GNB, LR, SVM dengan v1.0; audit pipeline pencarian dan metrik evaluasi.
* **Tindakan yang Diambil:**
  1. Menyederhanakan Tabel I menjadi 5 kolom: `Subgroup, Subjects, Train (80%), Test (20%), Total`.
  2. Membagi Subseksi III.B ViT menjadi 3 paragraf berbobot 100–125 kata, merinci checkpoint HuggingFace, normalisasi $\mu=\sigma=[0.5,0.5,0.5]$, ekstraksi token `[CLS]` Eq. (7), fusi direct sum Eq. (8), dan Table II skema fusi 7 konfigurasi.
  3. Menyelaraskan teks dan tabel hyperparameter Tabel III (RF: 576 kandidat), Tabel IV (GNB: 48 kandidat), Tabel V (LR: 54 kandidat), dan Tabel VI (SVM: 408 kandidat).
  4. Menambahkan Subseksi III.I Computational Environment mencakup Intel Core i9-13900H, RAM 32GB DDR5, NVIDIA RTX 4060 8GB, Python, PyTorch, Scikit-learn (100–115 kata).

### B. Tahap 2: Restrukturisasi Section IV (Results and Discussion) & Integrasi Tabel Subject-Disjoint
* **Permintaan Pengguna:** Perbaiki Section IV agar judul section tetap selaras dengan v1.0 dan sesuai ulasan IEEE Access; tampilkan tabel-tabel hasil Subject-Disjoint dari `experiment/code/md/`; pada tabel komputasi buat nama kolom singkat, durasi training dalam menit, dan layout full width LaTeX.
* **Tindakan yang Diambil:**
  1. Menyelaraskan struktur 5 subseksi utama: `IV.A Global Performance`, `IV.B Feature Ablation Study`, `IV.C Intersectional Subgroup Performance`, `IV.D Error Pattern Assessment`, dan `IV.E Comparison with Prior Studies`.
  2. Mengisi Table VII (RF: puncak Tri 85.00%), Table VIII (GNB: puncak Dual 84.31%), Table IX (LR: puncak Tri 88.66%), dan Table X (SVM: puncak Tri 88.61%) dengan metrik Subject-Disjoint held-out ($N=2.160$).
  3. Membangun Table XI Profil Efisiensi Komputasi (Full Width `table*`): GPU extraction 124.5 ms, training CPU (LR Tri 54.8 min vs SVM Tri 511.1 min), inferensi (LR 0.0054 ms vs SVM 4.4481 ms), ukuran model (LR 0.11 MB vs SVM 36.60 MB), RAM footprint 18.98 MB.
  4. Mengintegrasikan Table XII (Penurunan 5.09 pp sebagai efek memorisasi identitas) dan Table XIII (Uji McNemar berpasangan Edwards $\chi^2$ & Exact Binomial $p$-value).
  5. Menyusun Table XIV metrik OvR granular 6 subkelompok (TPR, FNR, dan EOD 9.72 pp).
  6. Menyajikan Figure 4 dan 3 tabel matriks konfusi empiris acuan non-numbered.
  7. Menyusun Table XV komparasi kontekstual Bagian A (studi terdahulu subject-overlap) vs komparasi terkontrol Bagian B (benchmark internal subject-disjoint).

### C. Tahap 3: Pemulihan Paritas Visual Tampilan Tabel & Gambar
* **Permintaan Pengguna:** *"saat ini seperti tabel/figure masih ada yang belum ditampilkan. seharusnya ditampilkan juga seperti pada paper_outline_v1.0.md."*
* **Tindakan yang Diambil:**
  1. Menemukan diskrepansi pada Figure 2: gambar komposit `sample_demogpairs.png` belum ditampilkan di Markdown; diperbaiki dengan menyematkan gambar komposit beresolusi tinggi di atas rincian sampel individual.
  2. Menstandarkan format blok Figure 3 dan Figure 4 agar memuat `Sitasi Gambar Wajib`, `Ketentuan Layout LaTeX`, `Caption Figure`, dan `Visual Markdown`.
  3. Menambahkan ketentuan layout LaTeX dan judul subseksi bahasa Indonesia pada Table I, Table II, dan Table XV.

### D. Tahap 4: Penghapusan Kolom `95% CI` pada Tabel IV.A
* **Permintaan Pengguna:** *"pada A. Global Performance apakah perlu ada kolom 95% CI?"* -> *"ok hilangkan"*
* **Tindakan yang Diambil:**
  1. Mengaudit relevansi kolom 95% CI: tidak diminta oleh Reviewer (Reviewer 2 hanya meminta Uji McNemar yang sudah ada di Tabel XIII); pada outline v1.0 kolom ini tidak ada.
  2. Menghapus kolom `95% CI` dari Table VII, Table VIII, Table IX, dan Table X.
  3. Mengembalikan format tabel ke 6 kolom bersih: `Configuration | Accuracy | Precision | Recall | F1-Score | Best Parameters`.
  4. Mempertahankan nilai interval Wilson Score CI pada teks narasi model terbaik di Paragraf 3 dan 4.

### E. Tahap 5: Sinkronisasi Master Element Sequence & Git Commit/Push
* **Permintaan Pengguna:** *"buat commit dan push"*
* **Tindakan yang Diambil:**
  1. Memverifikasi kelengkapan dan sinkronisasi urutan kronologis Master Element: 4 Gambar (Figure 1–4), 15 Tabel (Table I–XV), dan 23 Persamaan Matematika (Eq. 1–23).
  2. Menerbitkan commit Git `0e5167e` (`docs: update paper_outline_v1.1.md with computational setup, table parity, and streamlined performance metrics`).
  3. Mendorong pembaruan ke repositori GitHub `main`.

---

## 3. REKAPITULASI ELEMEN MASTER DEFINITIF PADA `paper_outline_v1.1.md`

| Elemen ID | Tipe | Subseksi Kemunculan | Format LaTeX | Deskripsi Singkat |
|:---:|:---:|:---:|:---:|---|
| **Figure 1** | Gambar | Section III (Overview) | `figure*` | Diagram End-to-End Framework Tri-Domain ViT & Klasifikasi Klasik. |
| **Figure 2** | Gambar | Section III.A (Paragraph 1) | `figure*` | Sampel citra DemogPairs 6 subkelompok (komposit `sample_demogpairs.png` & sampel individual). |
| **Table I** | Tabel | Section III.A (Paragraph 2) | `table` | Partisi dataset DemogPairs Subject-Disjoint (480 subjek latih, 120 subjek uji held-out). |
| **Figure 3** | Gambar | Section III.B (Paragraph 1) | `figure*` | Redesain vektor arsitektur ekstraksi token `[CLS]` ViT paralel 300+ DPI (`images/vit_v2.2.png`). |
| **Table II** | Tabel | Section III.B (Paragraph 3) | `table` | Skema konfigurasi fusi fitur 7 skema & desain studi ablasi. |
| **Table III** | Tabel | Section III.C (Random Forest) | `table*` | Ruang pencarian hyperparameter Random Forest (576 kombinasi). |
| **Table IV** | Tabel | Section III.D (Gaussian NB) | `table*` | Ruang pencarian hyperparameter Gaussian Naive Bayes (48 kombinasi). |
| **Table V** | Tabel | Section III.E (Logistic Reg) | `table*` | Ruang pencarian hyperparameter Logistic Regression (54 kombinasi). |
| **Table VI** | Tabel | Section III.F (Support Vector) | `table*` | Ruang pencarian hyperparameter Support Vector Machine (408 kombinasi). |
| **Table VII** | Tabel | Section IV.A (Random Forest) | `table*` | Benchmark performa Random Forest melintasi 7 konfigurasi (Subject-Disjoint). |
| **Table VIII** | Tabel | Section IV.A (Gaussian NB) | `table*` | Benchmark performa Gaussian Naive Bayes melintasi 7 konfigurasi (Subject-Disjoint). |
| **Table IX** | Tabel | Section IV.A (Logistic Reg) | `table*` | Benchmark performa Logistic Regression melintasi 7 konfigurasi (Subject-Disjoint). |
| **Table X** | Tabel | Section IV.A (Support Vector) | `table*` | Benchmark performa Support Vector Machine melintasi 7 konfigurasi (Subject-Disjoint). |
| **Table XI** | Tabel | Section IV.A (Komputasi) | `table*` | Profil efisiensi komputasi, waktu training (menit), latensi, memori, & ukuran model. |
| **Table XII** | Tabel | Section IV.B (Ablasi Leakage) | `table*` | Studi ablasi kebocoran data: Subject-Overlap (93.70%) vs Subject-Disjoint (88.61%). |
| **Table XIII** | Tabel | Section IV.B (Uji Statistik) | `table*` | Uji hipotesis inferensial berpasangan McNemar (Edwards $\chi^2$) & Exact Binomial. |
| **Table XIV** | Tabel | Section IV.C (Subkelompok) | `table*` | Profil performa granular 6 subkelompok & kalibrasi keadilan empiris EOD (9.72 pp). |
| **Figure 4** | Gambar | Section IV.D (Error Pattern) | `figure*` | Visualisasi 6×6 confusion matrices komparatif model Logistic Regression. |
| **Table XV** | Tabel | Section IV.E (Studi Terdahulu) | `table*` | Komparasi kontekstual studi terdahulu (Part A) vs komparasi terkontrol internal (Part B). |

---

## 4. STATUS DAN KESIAPAN TAHAP SELANJUTNYA

- Master Outline [`paper_outline_v1.1.md`](../paper_outline_v1.1.md) telah berstatus **DEFINITIF** dan terbukti kokoh, lengkap, serta memenuhi 100% rekomendasi Associate Editor dan kedua Reviewer IEEE Access.
- Repositori siap untuk melangkah ke penulisan draf naskah bab per bab di direktori `paper/` dan pemutakhiran paket LaTeX `paper_latex_en/`.
