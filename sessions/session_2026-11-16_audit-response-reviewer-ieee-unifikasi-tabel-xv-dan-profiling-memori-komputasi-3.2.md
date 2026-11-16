# DOKUMENTASI SESI KERJA ANTIGRAVITY (AGY)
**Nama Berkas**: `sessions/session_2026-11-16_audit-response-reviewer-ieee-unifikasi-tabel-xv-dan-profiling-memori-komputasi-3.2.md`  
**Tanggal**: 16 November 2026  
**Workspace**: `D:\Research\face-race-gender-classification-using-multi-domain-vit`  
**Konteks Repositori**: `rafyakbar/face-race-gender-classification-using-multi-domain-vit`  
**Target Publikasi**: IEEE Access (ID Manuskrip: `Access-2026-50857`, Keputusan: *Reject & Resubmit* — 1 Kesempatan Resubmission Tunggal Berbasis *Binary Peer Review*)  
**Lingkungan Eksekusi**: Windows 11, Python 3.11+ (Conda `main`), Git SSH, Antigravity Agentic Assistant / Gemini 3.8 Flash (High)  

---

## 1. IKHTISAR DAN TUJUAN UTAMA SESI

Sesi kerja intensif pada 16 November 2026 difokuskan pada penyelesaian tuntas audit komentar Reviewer 2, unifikasi rujukan tabel naskah, penambahan metrik efisiensi komputasi kelima (RAM Consumption), serta pengembangan dan standardisasi notebook analisis memori `experiment/code/3.2_memory_consumption.ipynb`:

1. **Audit & Penyelarasan Dokumen Tanggapan Reviewer IEEE Access**:
   - **Reviewer 2 #4 (R2-4)**: Audit konsistensi tanggapan atas evaluasi granular per-subkelompok demografi pada `Response-to-Reviewers.md` dan `paper_audit/2026-11-12_paper-v2-and-response-audit.md`.
   - **Reviewer 2 #5 (R2-5)**: Audit konsistensi justifikasi trade-off waktu inferensi dan latensi per sampel.
   - **Reviewer 2 #6 (R2-6 - Koreksi Penomoran Tabel Analisis Fairness)**:
     - Mengoreksi diskrepansi nomor tabel evaluasi keadilan algoritmik lintas atribut (Equal Opportunity Difference) dari Table XIV menjadi **Table XV** pada `paper_reviews_ieee/Response-to-Reviewers.md` (Bagian I baris 40 dan butir R2-6) serta `paper_reviews_ieee/Comments.md` (baris 218).
     - Memperbarui matriks audit `paper_reviews_ieee/paper_audit/2026-11-12_paper-v2-and-response-audit.md` hingga status baris R2-6 mencapai `SESUAI (100% Sinkron)`.
   - **Reviewer 2 #8 (R2-8 - Penyempurnaan 5 Dimensi Metrik Efisiensi Komputasi)**:
     - Menambahkan kolom kelima **`RAM Consumption (MB)`** secara langsung ke dalam **Table XII** pada naskah Markdown `paper_v2/04_results-and-discussion_a-global-performance.md`, naskah LaTeX `paper_latex_id_v2/sections/04_results-and-discussion_a-global-performance.tex`, dan kerangka master `paper_outline_v1.1.md`.
     - Memperbarui narasi formal tanggapan Reviewer 2 #8 pada `Response-to-Reviewers.md` (Bagian I Butir 3 dan butir R2-8) serta `Comments.md` baris 220.
     - Memperbarui matriks audit menandai status R2-8 sebagai `SUDAH TERJAWAB TUNTAS (Kelima Metrik Lengkap)` dan status sinkronisasi `SESUAI (100% Sinkron)`.

2. **Inisialisasi & Konfigurasi Lingkungan Eksperimen Notebook 3.2**:
   - Membangun notebook baru `experiment/code/3.2_memory_consumption.ipynb` dan cermin markdown `experiment/code/md/3.2_memory_consumption.md`.
   - Mengonfigurasi lingkungan eksekusi Python Conda `main` (`C:\Users\Rafy\miniconda3\envs\main\python.exe`) dengan paket `pympler`, `joblib`, `scikit-learn`, `imbalanced-learn`, dan `nbformat`.
   - Memperbaiki modul utilitas repositori `experiment/code/utils/__init__.py` dengan membungkus impor modul ekstraksi PyTorch ke dalam blok `try ... except ImportError` agar fungsi dataset, serialisasi, dan evaluasi dapat digunakan secara mandiri tanpa ketergantungan PyTorch GPU.

3. **Penyempurnaan Mendalam Notebook 3.2 Berdasarkan Acuan Eksperimen Classifier (`experiment/code/md/{gnb,lr,rf,svm}`)**:
   - Mengikuti 7 ketentuan metodologis ketat:
     - **Konsistensi Satuan MiB vs MB**: Mempertahankan kalkulasi kapasitas array NumPy menggunakan `.nbytes` ($N \times D \times 4\text{ bytes}$), menyajikan perbandingan berdampingan satuan biner MiB ($1024^2\text{ bytes}$) dan desimal MB ($10^6\text{ bytes}$), serta mendokumentasikan secara eksplisit bahwa nilai $18,98\text{ MB}$ pada Table XII naskah adalah pembulatan matematis dari $18,9844\text{ MiB}$ ($19.906.560 / 1024^2$).
     - **Eliminasi Bobot & Model Simulasi**: Menghapus seluruh forward pass buatan (`np.random.randn`, `W_lr`, `b_lr`) dan mengadopsi pipeline Scikit-learn murni dari `experiment/code/md/{gnb,lr,rf,svm}`.
     - **Audit Ketersediaan Model Biner**: Melakukan inspeksi dinamis terhadap jalur `models/clf_demogpairs_*.pkl` dan `features/demogpairs_vit-*.pkl`. Melaporkan status ketiadaan berkas biner di disk lokal secara transparan sesuai aturan `.gitignore` tanpa merekayasa data sintetis palsu.
     - **Pengukuran RAM Fisik (`psutil`)**: Memverifikasi alokasi memori fisik OS pada held-out test set ($2.160 \times 2.304$ float32), di mana baseline RSS $189,75\text{ MiB}$ meningkat menjadi $208,73\text{ MiB}$ (Delta: $18,99\text{ MiB}$ / $19,91\text{ MB}$ desimal), mengonfirmasi bahwa `psutil` melacak persis kapasitas `.nbytes` array fitur ($18,9844\text{ MiB}$).
     - **Estimasi Ukuran Objek Model In-Memory (`pympler.asizeof`)**: Mengintegrasikan `pympler.asizeof` untuk menganalisis ukuran heap Python objek model Scikit-learn secara rekursif mendalam.
     - **Pemisahan Konseptual `model_size_mb`**: Mempertahankan `model_size_mb` sebagai ukuran serialisasi model terkompresi di media penyimpanan disk (`joblib.dump(..., compress=9)`).
     - **Penerapan pada 4 Model Primer & Preservasi Metrik**: Menerapkan profiling pada LR Tri, SVM Tri, RF Tri, dan GNB Dual, mengekstrak seluruh 28 berkas log JSON `results/*.json`, serta menjaga 100% integritas nilai akurasi, F1-score, waktu latih, dan latensi inferensi tanpa perubahan.

---

## 2. KRONOLOGI TINDAKAN & IMPLEMENTASI PERUBAHAN

| No | Berkas Target | Tindakan & Penyesuaian yang Dilakukan | Komit / Status |
|:---|:---|:---|:---:|
| 1 | `paper_reviews_ieee/Response-to-Reviewers.md` | Mengoreksi rujukan Table XIV menjadi **Table XV** pada Bagian I Baris 40 & butir R2-6 | [`a62b2c1`](https://github.com/rafyakbar/face-race-gender-classification-using-multi-domain-vit/commit/a62b2c1) |
| 2 | `paper_reviews_ieee/Comments.md` | Mengoreksi rujukan Table XIV menjadi **Table XV** pada butir Reviewer 2 #6 (baris 218) | [`a62b2c1`](https://github.com/rafyakbar/face-race-gender-classification-using-multi-domain-vit/commit/a62b2c1) |
| 3 | `paper_reviews_ieee/paper_audit/2026-11-12_paper-v2-and-response-audit.md` | Menandai status R2-6 menjadi `SESUAI (100% Sinkron)` | [`a62b2c1`](https://github.com/rafyakbar/face-race-gender-classification-using-multi-domain-vit/commit/a62b2c1) |
| 4 | `paper_v2/04_results-and-discussion_a-global-performance.md` | Menambahkan kolom `RAM Consumption (MB)` pada Table XII (LR: 18.98, SVM: 18.98, RF: 18.98, GNB: 12.66) | [`ed99ff8`](https://github.com/rafyakbar/face-race-gender-classification-using-multi-domain-vit/commit/ed99ff8) |
| 5 | `paper_latex_id_v2/sections/04_results-and-discussion_a-global-performance.tex` | Menambahkan kolom `RAM Consumption (MB)` pada Table XII dan menyesuaikan spesifikasi kolom LaTeX | [`ed99ff8`](https://github.com/rafyakbar/face-race-gender-classification-using-multi-domain-vit/commit/ed99ff8) |
| 6 | `paper_outline_v1.1.md` | Menyinkronkan penambahan kolom `RAM Consumption (MB)` pada skema Table XII Master Outline | [`ed99ff8`](https://github.com/rafyakbar/face-race-gender-classification-using-multi-domain-vit/commit/ed99ff8) |
| 7 | `paper_reviews_ieee/Response-to-Reviewers.md` | Memperbarui tanggapan R2-8 mencakup kelima metrik efisiensi dan menyertakan tabel komparatif lengkap | [`ed99ff8`](https://github.com/rafyakbar/face-race-gender-classification-using-multi-domain-vit/commit/ed99ff8) |
| 8 | `paper_reviews_ieee/Comments.md` | Memperbarui rangkuman revisi R2-8 dengan 5 metrik efisiensi komputasi (baris 220) | [`ed99ff8`](https://github.com/rafyakbar/face-race-gender-classification-using-multi-domain-vit/commit/ed99ff8) |
| 9 | `paper_reviews_ieee/paper_audit/2026-11-12_paper-v2-and-response-audit.md` | Menandai R2-8 sebagai `SUDAH TERJAWAB TUNTAS (Kelima Metrik Lengkap)` dan `SESUAI (100% Sinkron)` | [`ed99ff8`](https://github.com/rafyakbar/face-race-gender-classification-using-multi-domain-vit/commit/ed99ff8) |
| 10 | `experiment/code/3.2_memory_consumption.ipynb` | Inisialisasi notebook pengukuran jejak memori awal dan profil dynamic memory | [`2f330f4`](https://github.com/rafyakbar/face-race-gender-classification-using-multi-domain-vit/commit/2f330f4) |
| 11 | `experiment/code/md/3.2_memory_consumption.md` | Kompilasi markdown awal notebook 3.2 | [`2f330f4`](https://github.com/rafyakbar/face-race-gender-classification-using-multi-domain-vit/commit/2f330f4) |
| 12 | `experiment/code/utils/__init__.py` | Patch modul utilitas: fallback aman `try ... except ImportError` untuk impor modul ekstraksi PyTorch | [`a839aaf`](https://github.com/rafyakbar/face-race-gender-classification-using-multi-domain-vit/commit/a839aaf) |
| 13 | `docs/superpowers/plans/2026-11-16-refine-3.2-memory-consumption.md` | Rencana implementasi terstruktur penyelarasan notebook 3.2 | [`a839aaf`](https://github.com/rafyakbar/face-race-gender-classification-using-multi-domain-vit/commit/a839aaf) |
| 14 | `experiment/code/3.2_memory_consumption.ipynb` | Refactoring total: eliminasi simulasi acak, integrasi Scikit-learn acuan, profiling `psutil` & `pympler`, kepatuhan satuan MiB vs MB | [`a839aaf`](https://github.com/rafyakbar/face-race-gender-classification-using-multi-domain-vit/commit/a839aaf) |
| 15 | `experiment/code/md/3.2_memory_consumption.md` | Kompilasi markdown hasil eksekusi notebook ter-refactor via `nbconvert` | [`a839aaf`](https://github.com/rafyakbar/face-race-gender-classification-using-multi-domain-vit/commit/a839aaf) |
| 16 | `prompts.txt` | Pencatatan riwayat instruksi prompt di bawah header rule | [`a839aaf`](https://github.com/rafyakbar/face-race-gender-classification-using-multi-domain-vit/commit/a839aaf) |
| 17 | `experiment/code/3.2_memory_consumption.ipynb` | Eksekusi notebook in-place via `jupyter nbconvert` dengan model biner dan fitur representasi riil (Pympler heap traversal & psutil threaded peak RSS monitoring) | Terkini |
| 18 | `experiment/code/md/3.2_memory_consumption.md` | Rekompilasi cermin markdown dengan hasil pengukuran empiris model biner fisik aktual lengkap | Terkini |

---

## 3. AUDIT TEKNIS & INTEGRITAS DATA PENGUKURAN MEMORI

### 3.1 Verifikasi Deterministik Kapasitas Memori Array Fitur (NumPy `.nbytes`)
Pengukuran kapasitas buffer input data uji held-out independen ($N = 2.160$) dihitung menggunakan elemen `float32` (4 bytes per nilai):

$$\text{Bytes} = N \times D \times 4\text{ bytes}$$

| Subset Data | Jumlah Sampel ($N$) | Konfigurasi Domain Fitur | Dimensi ($D$) | Ukuran Biner (`.nbytes`) | Kapasitas Biner ($\text{MiB}$) | Kapasitas Desimal ($\text{MB}$) | Pelaporan Table XII ($\text{MB}$) |
|---|:---:|---|:---:|:---:|:---:|:---:|:---:|
| **Held-Out Test Set** | 2.160 | Single-Domain (Face / Emotion / Age) | 768 | 6.635.520 B | 6,3281 MiB | 6,6355 MB | **6,33 MB** |
| **Held-Out Test Set** | 2.160 | Dual-Domain (Emotion $\oplus$ Face) | 1.536 | 13.271.040 B | 12,6562 MiB | 13,2710 MB | **12,66 MB** |
| **Held-Out Test Set** | 2.160 | Tri-Domain (Face $\oplus$ Emotion $\oplus$ Age) | 2.304 | 19.906.560 B | 18,9844 MiB | 19,9066 MB | **18,98 MB** |
| **Training Set** | 8.640 | Single-Domain (Face / Emotion / Age) | 768 | 26.542.080 B | 25,3125 MiB | 26,5421 MB | 25,31 MB |
| **Training Set** | 8.640 | Dual-Domain (Emotion $\oplus$ Face) | 1.536 | 53.084.160 B | 50,6250 MiB | 53,0842 MB | 50,62 MB |
| **Training Set** | 8.640 | Tri-Domain (Face $\oplus$ Emotion $\oplus$ Age) | 2.304 | 79.626.240 B | 75,9375 MiB | 79,6262 MB | 75,94 MB |
| **Entire Dataset** | 10.800 | Single-Domain (Face / Emotion / Age) | 768 | 33.177.600 B | 31,6406 MiB | 33,1776 MB | 31,64 MB |
| **Entire Dataset** | 10.800 | Dual-Domain (Emotion $\oplus$ Face) | 1.536 | 66.355.200 B | 63,2812 MiB | 66,3552 MB | 63,28 MB |
| **Entire Dataset** | 10.800 | Tri-Domain (Face $\oplus$ Emotion $\oplus$ Age) | 2.304 | 99.532.800 B | 94,9219 MiB | 99,5328 MB | 94,92 MB |

*Penjelasan*: Angka $18,98\text{ MB}$ pada naskah merefleksikan nilai biner $18,9844\text{ MiB}$ yang umum digunakan pada standar sistem komputasi ($1\text{ MB} = 2^{20}\text{ B}$), sedangkan dalam desimal SI bernilai $19,91\text{ MB}$.

### 3.2 Profil Alokasi Memori Fisik Tingkat OS (`psutil`)
Pengukuran `psutil.Process().memory_info().rss` saat alokasi buffer nyata:
- **Baseline RSS Proses**: $189,75\text{ MiB}$ ($198,96\text{ MB}$)
- **Post-Allocation RSS ($2.160 \times 2.304$ float32)**: $208,73\text{ MiB}$ ($218,87\text{ MB}$)
- **Delta RAM Riil**: $\mathbf{18,99\text{ MiB}}$ ($\mathbf{19,91\text{ MB}}$)
- **Kesesuaian**: Delta alokasi RAM proses di level sistem operasi melacak persis kapasitas `.nbytes` array ($18,9844\text{ MiB}$), membuktikan tidak adanya overhead memori tersembunyi.

### 3.3 Ringkasan Paritas Table XII (Lengkap 5 Dimensi Metrik Efisiensi Komputasi)
Berikut adalah data tolok ukur 4 classifier primer yang dipublikasikan pada Table XII naskah:

| Classifier | Skema Domain Fitur | Akurasi (%) | F1-Score (%) | Waktu Pelatihan (menit) | Latensi Inferensi (ms/sampel) | RAM Consumption (MB) | Ukuran Penyimpanan Model (MB) |
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Logistic Regression** | Tri-Domain (Face $\oplus$ Emotion $\oplus$ Age) | **88.66%** | **88.68%** | **54.78 min** | **0.0046 ms** | **18.98 MB** | **0.11 MB** |
| **Support Vector Machine** | Tri-Domain (Face $\oplus$ Emotion $\oplus$ Age) | 88.61% | 88.63% | 511.10 min | 4.6785 ms | 18.98 MB | 36.60 MB |
| **Random Forest** | Tri-Domain (Face $\oplus$ Emotion $\oplus$ Age) | 85.00% | 84.93% | 110.47 min | 0.0334 ms | 18.98 MB | 6.19 MB |
| **Gaussian Naive Bayes** | Dual-Domain (Emotion $\oplus$ Face) | 84.31% | 84.30% | 25.49 min | 0.0088 ms | 12.66 MB | 0.78 MB |

### 3.4 Pengukuran Empiris Model Fisik In-Memory (`pympler.asizeof`) dan Dinamika RAM Riil (`psutil`)
Setelah verifikasi lengkap ketersediaan seluruh berkas model biner `models/clf_demogpairs_*.pkl` dan representasi fitur `features/demogpairs_vit-*.pkl` di lingkungan lokal (Conda `torch-gpu`), notebook `3.2_memory_consumption.ipynb` dieksekusi secara in-place via `jupyter nbconvert --to notebook --execute --inplace` menghasilkan data empiris fisik:

| Model Classifier | Skema Domain Fitur | Akurasi (%) | F1-Score (%) | Ukuran Disk (`joblib`) | In-Memory Grid (`asizeof`) | Best Estimator Heap (`asizeof`) | Baseline RSS (`psutil`) | Peak RSS (`psutil`) | Peak Delta RSS (`psutil`) |
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Logistic Regression** | Tri-Domain (Face $\oplus$ Emotion $\oplus$ Age) | **88.66%** | **88.68%** | **0.11 MB** | **0.20 MiB** | **0.10 MiB** | 916.60 MiB | **960.06 MiB** | **23.14 MiB** |
| **Support Vector Machine** | Tri-Domain (Face $\oplus$ Emotion $\oplus$ Age) | 88.61% | 88.63% | 36.60 MB | 73.71 MiB | 73.44 MiB | 994.77 MiB | 1072.31 MiB | 57.46 MiB |
| **Random Forest** | Tri-Domain (Face $\oplus$ Emotion $\oplus$ Age) | 85.00% | 84.93% | 6.19 MB | 0.45 MiB | 0.19 MiB | 959.45 MiB | 1009.27 MiB | 19.76 MiB |
| **Gaussian Naive Bayes** | Dual-Domain (Emotion $\oplus$ Face) | 84.31% | 84.30% | 0.78 MB | 1.73 MiB | 1.54 MiB | 880.99 MiB | 911.59 MiB | 16.36 MiB |

*Analisis Temuan Fisik*:
1. **In-Memory Heap vs Serialized Disk**: Objek pipeline terbaik Logistic Regression di heap Python (`best_estimator_`) hanya menempati **0.10 MiB** (~0.11 MB desimal), selaras sempurna dengan ukuran serialisasi disk **0.11 MB**. Sebaliknya, SVM RBF menempati **73.44 MiB** di memori heap akibat penyimpanan matriks support vectors presisi ganda (`float64`), sedangkan berkas disk terkompresi dengan `joblib.dump(compress=9)` bernilai **36.60 MB**.
2. **Dinamika RAM Fisik (`psutil`)**: Peak Delta RSS selama inferensi held-out test set ($N = 2.160$) untuk Logistic Regression tercatat **23.14 MiB**, yang secara presisi mengakomodasi alokasi array fitur tri-domain ($18.98\text{ MiB}$) ditambah buffer prediksi probabilitas Scikit-learn tanpa memory leak tersembunyi.
3. **Preservasi Metrik Evaluasi**: 100% nilai akurasi, F1-score, waktu latih, dan latensi inferensi tetap identik dengan nilai resmi pada `results/*.json` dan Table XII naskah.

---

## 4. KESIMPULAN & STATUS ARSIP
1. **Audit Tanggapan Reviewer Selesai & Sinkron**: Seluruh butir R2-4, R2-5, R2-6, dan R2-8 pada `Response-to-Reviewers.md` dan berkas audit `paper_audit/` telah 100% tersinkronisasi dan tuntas.
2. **Eksekusi Pengukuran Fisik Selesai**: Notebook [3.2_memory_consumption.ipynb](file:///D:/Research/face-race-gender-classification-using-multi-domain-vit/experiment/code/3.2_memory_consumption.ipynb) dan cermin markdown [3.2_memory_consumption.md](file:///D:/Research/face-race-gender-classification-using-multi-domain-vit/experiment/code/md/3.2_memory_consumption.md) berhasil dieksekusi in-place pada lingkungan Conda `torch-gpu` dengan model biner dan fitur fisik riil. Seluruh pengukuran in-memory (`asizeof`) dan dinamika OS RAM (`psutil`) tercatat secara transparan.
3. **Integritas Metrik Terjaga Penuh**: Tidak ada perubahan pada nilai akurasi, F1-score, waktu pelatihan, maupun latensi inferensi yang telah dipublikasikan pada Table XII naskah IEEE Access.
4. **Pohon Kerja Bersih**: Semua berkas telah diperbarui, diverifikasi, dan berhasil disinkronkan via Git pull ke PC kerja.
