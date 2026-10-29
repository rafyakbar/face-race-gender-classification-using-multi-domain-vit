# Multi-Domain Vision Transformer Fusion for Intersectional Demographic Classification from Facial Images

> **Abstrak:** Kerangka kerja machine learning empiris untuk klasifikasi demografis 6 kelas interseksional (3 Ras × 2 Gender) dari citra wajah menggunakan offline multi-representation feature fusion pada tiga backbone Vision Transformer (ViT) spesifik tugas (**Face Biometrics**, **Facial Emotion**, dan **Facial Age**) yang dipadukan dengan pengklasifikasi klasik teroptimasi 5-Fold Stratified GridSearchCV secara komprehensif. Di bawah protokol ketat **Subject-Disjoint Partitioning** (Zero Identity Leakage — Milestone Revisi IEEE Access), representasi Tri-Domain ViT yang diusulkan mencapai **Akurasi Pengujian 88.66%** (Logistic Regression, Macro F1: **0.8868**) dan **Akurasi Pengujian 88.61%** (Support Vector Machine, Macro F1: **0.8863**) pada subjek held-out yang belum pernah dilihat sebelumnya ($N = 2,160$ sampel uji dari 120 identitas terisolasi). Secara bersamaan, repositori ini mempertahankan **Subject-Overlap Benchmark** historis (**93.70%** SVM Tri-Domain) sebagai baseline empiris yang ketat untuk analisis ablasi data leakage dan generalisasi lintas subjek (menjawab Komentar #2 Reviewer 2 IEEE Access).

---

## 📑 Daftar Isi

- [Status Publikasi & Peer Review](#status-publikasi--peer-review)
- [Sistem Dual-Benchmark](#sistem-dual-benchmark)
  - [1. Benchmark Utama: Subject-Disjoint Partitioning (Zero Data Leakage)](#1-benchmark-utama-subject-disjoint-partitioning-zero-data-leakage--revisi-ieee-access)
  - [2. Benchmark Historis: Subject-Overlap Partitioning (Baseline Identity Leakage 100%)](#2-benchmark-historis-subject-overlap-partitioning-baseline-identity-leakage-100)
  - [3. Analisis Komparatif Ablasi Data Leakage & Generalisasi](#3-analisis-komparatif-ablasi-data-leakage--generalisasi)
  - [4. Profil Disparitas Subkelompok Interseksional](#4-profil-disparitas-subkelompok-interseksional-held-out-subject-disjoint-test-set)
  - [5. Perbandingan dengan Studi Terdahulu pada DemogPairs](#5-perbandingan-dengan-studi-terdahulu-pada-demogpairs)
- [Kerangka Metodologi](#kerangka-metodologi)
- [Struktur Repositori](#struktur-repositori)
- [Panduan Memulai Cepat & Reproduksi Eksperimen](#panduan-memulai-cepat--reproduksi-eksperimen)
- [Tim Peneliti](#tim-peneliti)
- [Sitasi](#sitasi)

---

## Status Publikasi & Peer Review

> [!IMPORTANT]
> **Revisi IEEE Access Sedang Berjalan (ID Naskah: `Access-2026-50857`):**  
> Menyusul keputusan editorial resmi yang diterima pada **20 Oktober 2026** (*Reject & Resubmit* dengan tepat satu kesempatan resubmisi yang diizinkan di bawah kebijakan binary peer review IEEE Access), repositori ini menjalani revisi sistematis. Tujuan utamanya adalah menyelesaikan Komentar #2 Reviewer 2 terkait identity overlap dan generalisasi lintas subjek melalui re-benchmarking subject-disjoint yang ketat, paired inferential hypothesis testing (uji McNemar & 95% Wilson Score CI), serta profiling efisiensi komputasi (computational efficiency profiling).

- **Jurnal Sasaran:** [IEEE Access](https://ieeeaccess.ieee.org/) (Open Access, Q1 / Impact Factor: 3.4)
- **ID Pelacakan Naskah:** `Access-2026-50857`
- **Milestone Terkini:** Keputusan Editorial Diterima (20-10-2026) – Binary Peer Review (Reject & Resubmit dengan 1 Kesempatan Resubmisi).
- **Fokus Utama Revisi:** Menyelesaikan Komentar #2 Reviewer 2 mengenai identity overlap dan generalisasi lintas subjek melalui re-benchmarking subject-disjoint yang ketat, paired inferential hypothesis testing (uji McNemar & 95% Wilson Score CI), serta computational profiling.
- **Berkas Penelaahan Sejawat (Peer Review Dossier):** Dikelola di bawah direktori [`paper_reviews_ieee/`](paper_reviews_ieee/):
  - [`Comments.md`](paper_reviews_ieee/Comments.md) — Umpan balik reviewer yang didekonstruksi beserta matriks respons detail.
  - [`IEEE-Access_Decision-on-Manuscript-ID-Access-2026-50857.md`](paper_reviews_ieee/IEEE-Access_Decision-on-Manuscript-ID-Access-2026-50857.md) — Surat keputusan editorial resmi.
  - [`IEEE-Access_Response-to-Reviewers-template.md`](paper_reviews_ieee/IEEE-Access_Response-to-Reviewers-template.md) — Templat resmi surat tanggapan butir-per-butir (point-by-point response letter).
  - [`Request-for-Byline-Change.md`](paper_reviews_ieee/Request-for-Byline-Change.md) — Formulir resmi perubahan susunan kepengarangan (author byline change form).
  - [`Resubmission-Checklist.md`](paper_reviews_ieee/Resubmission-Checklist.md) — Daftar periksa kepatuhan resubmisi 10 poin resmi.
- **Panduan Operasional:**
  - [`WORKFLOW.md`](WORKFLOW.md) — Standard Operating Procedure (SOP) untuk siklus hidup naskah riset 5 tahap.
  - [`README.ai.md`](README.ai.md) — Panduan referensi teknis utama dan single source of truth untuk autonomous agents.

---

## Sistem Dual-Benchmark

Untuk menjamin transparansi ilmiah secara menyeluruh dan menjawab langsung Komentar #2 Reviewer 2 IEEE Access, repositori ini mengimplementasikan **Arsitektur Dual-Benchmark**:
1. **Benchmark Utama (Subject-Disjoint):** Zero identity leakage ($0.00\%$); mengevaluasi kemampuan generalisasi sejati pada identitas wajah yang sepenuhnya belum pernah dilihat sebelumnya (held-out unseen identities).
2. **Benchmark Historis (Subject-Overlap):** Split terstratifikasi berbasis citra ($100.00\%$ kehadiran identitas); berfungsi sebagai baseline komparatif untuk mengukur efek memorisasi identitas wajah (facial identity memorization).

> [!TIP]
> **Protokol Zero Identity Leakage:** Benchmark utama mengisolasi 120 subjek (2,160 citra uji) secara ketat ke dalam evaluasi held-out, menjamin nol tumpang tindih identitas ($0.00\%$) antara partisi pelatihan (training) dan pengujian (testing).

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                   DEMOGPAIRS DATASET                                   │
│                 10,800 Facial Images │ 600 Unique Subjects (18 images/subject)         │
│                 6 Intersectional Classes (1,800 images per demographic class)          │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │
                    ┌───────────────────────┴───────────────────────┐
                    ▼                                               ▼
┌───────────────────────────────────────┐       ┌───────────────────────────────────────┐
│       PRIMARY BENCHMARK REVISION      │       │     HISTORICAL BASELINE ARCHIVE       │
│      (Subject-Disjoint Partition)     │       │       (Subject-Overlap Split)         │
│ ───────────────────────────────────── │       │ ───────────────────────────────────── │
│ • 480 Train Subjects (8,640 images)   │       │ • Image-level 80/20 random partition  │
│ • 120 Held-Out Subjects (2,160 images)│       │ • 593/593 subjects overlap in test set│
│ • Identity Leakage: 0.00% (Zero)      │       │ • Identity Leakage: 100.00%           │
│ • Best: LR Tri (88.66%) / SVM (88.61%)│       │ • Best: SVM Tri (93.70%)              │
│ • Location: experiment/code/results/  │       │ • Location: experiment/code/archive/  │
└───────────────────────────────────────┘       └───────────────────────────────────────┘
```

---

### 1. Benchmark Utama: Subject-Disjoint Partitioning (Zero Data Leakage — Revisi IEEE Access)

Dievaluasi pada partisi uji subject-disjoint held-out ($N = 2,160$ citra dari 120 subjek unseen; tepat 360 citra per kelas interseksional) setelah 5-fold stratified cross-validation pada 480 subjek pelatihan ($N = 8,640$).

#### Konfigurasi Performa Terbaik per Famili Classifier

| Peringkat | Classifier | Skema Fitur Terbaik | Dimensi Fitur | Test Accuracy | Precision (Macro) | Recall (Macro) | F1-Score (Macro) | 95% Wilson Score CI | Latensi (ms/sampel) | Ukuran Model (MB) | Hyperparameter Terbaik |
|:---:|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 🥇 | **Logistic Regression (LR)** | **Tri-Domain (`Face ⊕ Emotion ⊕ Age`)** | **2,304** | **88.66%** | **0.8875** | **0.8866** | **0.8868** | **[87.25%, 89.93%]** | **0.0054 ms** | **0.11 MB** | `C=0.1, solver='saga', max_iter=500, scaler=MinMaxScaler, pca=None` |
| 🥈 | **Support Vector Machine (SVM)** | **Tri-Domain (`Face ⊕ Emotion ⊕ Age`)** | **2,304** | **88.61%** | **0.8871** | **0.8861** | **0.8863** | **[87.20%, 89.88%]** | 4.4481 ms | 36.60 MB | `C=10, kernel='rbf', gamma='scale', scaler=MinMaxScaler, pca=None` |
| 🥉 | **Random Forest (RF)** | **Tri-Domain (`Face ⊕ Emotion ⊕ Age`)** | **2,304** | **85.00%** | 0.8506 | 0.8500 | 0.8493 | [83.43%, 86.44%] | 0.0537 ms | 6.19 MB | `n_estimators=200, max_depth=None, max_features='sqrt', min_samples_split=2, min_samples_leaf=1, pca=PCA(0.75), scaler=None` |
| 4 | **Gaussian Naive Bayes (GNB)** | Dual-Domain (`Emotion ⊕ Face`) | 1,536 | **84.31%** | 0.8437 | 0.8431 | 0.8430 | [82.71%, 85.78%] | 0.0083 ms | 0.78 MB | `var_smoothing=0.005878, pca=PCA(0.75), scaler=MinMaxScaler` |

> [!NOTE]
> Untuk Gaussian Naive Bayes, konfigurasi Tri-Domain mencapai **83.61%** (Macro F1: 0.8364), sedangkan akurasi puncak tercapai pada Dual-Domain `Emotion ⊕ Face` (84.31%).

#### Papan Peringkat Global Definitif 28 Model Subject-Disjoint

| Peringkat | Classifier | Skema Fitur | Kategori | Dim | Test Accuracy | Precision | Recall | F1-Score | 95% CI (Wilson) | Latensi (ms) | Ukuran (MB) |
|:---:|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | **LR** | **`vit-face-emotion-age`** | **Tri** | **2,304** | **88.66%** | **0.8875** | **0.8866** | **0.8868** | **[87.25%, 89.93%]** | 0.0054 | 0.11 |
| 2 | **SVM** | **`vit-face-emotion-age`** | **Tri** | **2,304** | **88.61%** | **0.8871** | **0.8861** | **0.8863** | **[87.20%, 89.88%]** | 4.4481 | 36.60 |
| 3 | SVM | `vit-emotion-face` | Dual | 1,536 | 88.43% | 0.8850 | 0.8843 | 0.8844 | [87.01%, 89.71%] | 0.9707 | 15.27 |
| 4 | SVM | `vit-face-age` | Dual | 1,536 | 87.55% | 0.8766 | 0.8755 | 0.8757 | [86.09%, 88.87%] | 2.2581 | 23.48 |
| 5 | LR | `vit-emotion-face` | Dual | 1,536 | 87.45% | 0.8759 | 0.8745 | 0.8749 | [85.99%, 88.78%] | 0.0039 | 0.08 |
| 6 | LR | `vit-face-age` | Dual | 1,536 | 87.41% | 0.8744 | 0.8741 | 0.8740 | [85.94%, 88.74%] | 0.0090 | 0.11 |
| 7 | LR | `vit-emotion-age` | Dual | 1,536 | 86.67% | 0.8668 | 0.8667 | 0.8667 | [85.17%, 88.04%] | 0.0040 | 0.08 |
| 8 | LR | `vit-face` | Single | 768 | 86.39% | 0.8646 | 0.8639 | 0.8640 | [84.88%, 87.77%] | 0.0008 | 0.04 |
| 9 | SVM | `vit-emotion-age` | Dual | 1,536 | 86.25% | 0.8626 | 0.8625 | 0.8624 | [84.73%, 87.64%] | 3.1451 | 32.76 |
| 10 | SVM | `vit-face` | Single | 768 | 86.16% | 0.8624 | 0.8616 | 0.8619 | [84.64%, 87.55%] | 3.0653 | 7.56 |
| 11 | SVM | `vit-emotion` | Single | 768 | 85.79% | 0.8584 | 0.8579 | 0.8580 | [84.25%, 87.20%] | 1.8871 | 15.30 |
| 12 | LR | `vit-emotion` | Single | 768 | 85.23% | 0.8535 | 0.8523 | 0.8527 | [83.67%, 86.67%] | 0.0037 | 0.06 |
| 13 | RF | `vit-face-emotion-age` | Tri | 2,304 | 85.00% | 0.8506 | 0.8500 | 0.8493 | [83.43%, 86.44%] | 0.0537 | 6.19 |
| 14 | RF | `vit-emotion-face` | Dual | 1,536 | 84.86% | 0.8493 | 0.8486 | 0.8479 | [83.29%, 86.31%] | 0.0316 | 8.58 |
| 15 | RF | `vit-face-age` | Dual | 1,536 | 84.86% | 0.8488 | 0.8486 | 0.8478 | [83.29%, 86.31%] | 0.0310 | 6.19 |
| 16 | GNB | `vit-emotion-face` | Dual | 1,536 | 84.31% | 0.8437 | 0.8431 | 0.8430 | [82.71%, 85.78%] | 0.0083 | 0.78 |
| 17 | RF | `vit-face` | Single | 768 | 84.03% | 0.8413 | 0.8403 | 0.8403 | [82.42%, 85.51%] | 0.0314 | 5.99 |
| 18 | GNB | `vit-face-emotion-age` | Tri | 2,304 | 83.61% | 0.8379 | 0.8361 | 0.8364 | [81.99%, 85.11%] | 0.0081 | 1.36 |
| 19 | GNB | `vit-face-age` | Dual | 1,536 | 83.06% | 0.8347 | 0.8306 | 0.8310 | [81.42%, 84.58%] | 0.0080 | 0.75 |
| 20 | SVM | `vit-age` | Single | 768 | 82.55% | 0.8268 | 0.8255 | 0.8258 | [80.89%, 84.09%] | 2.0104 | 18.22 |
| 21 | GNB | `vit-face` | Single | 768 | 82.55% | 0.8268 | 0.8255 | 0.8250 | [80.89%, 84.09%] | 0.0031 | 0.19 |
| 22 | LR | `vit-age` | Single | 768 | 81.48% | 0.8145 | 0.8148 | 0.8146 | [79.79%, 83.06%] | 0.0028 | 0.06 |
| 23 | RF | `vit-emotion-age` | Dual | 1,536 | 77.31% | 0.7734 | 0.7731 | 0.7728 | [75.50%, 79.03%] | 0.0392 | 12.35 |
| 24 | RF | `vit-emotion` | Single | 768 | 76.11% | 0.7602 | 0.7611 | 0.7603 | [74.27%, 77.86%] | 0.0316 | 10.34 |
| 25 | GNB | `vit-emotion-age` | Dual | 1,536 | 75.88% | 0.7597 | 0.7588 | 0.7578 | [74.03%, 77.64%] | 0.0048 | 0.24 |
| 26 | GNB | `vit-emotion` | Single | 768 | 72.13% | 0.7251 | 0.7213 | 0.7199 | [70.20%, 73.98%] | 0.0031 | 0.13 |
| 27 | RF | `vit-age` | Single | 768 | 71.81% | 0.7176 | 0.7181 | 0.7170 | [69.87%, 73.66%] | 0.0327 | 11.21 |
| 28 | GNB | `vit-age` | Single | 768 | 67.08% | 0.6691 | 0.6708 | 0.6686 | [65.07%, 69.03%] | 0.0045 | 0.37 |

---

### 2. Benchmark Historis: Subject-Overlap Partitioning (Baseline Identity Leakage 100%)

Diarsipkan di bawah direktori [`experiment/code/archive/`](experiment/code/archive/) sebagai baseline ablasi untuk mengukur besaran efek inflasi akibat kebocoran identitas (identity leakage). Dievaluasi dengan skema random stratified split tingkat citra standar ($N = 8,640$ latih / $N = 2,160$ uji; seluruh 593 identitas pada data uji juga hadir di data latih pada foto berbeda):

| Peringkat | Classifier | Konfigurasi Fitur Terbaik | Dimensi Fitur | Best Accuracy | Precision | Recall | F1-Score | Hyperparameter Terbaik |
|:---:|---|---|:---:|:---:|:---:|:---:|:---:|---|
| 🥇 | **Support Vector Machine (SVM)** | **Tri-Domain (`Face ⊕ Emotion ⊕ Age`)** | **2,304** | **93.70%** | **0.9372** | **0.9370** | **0.9369** | `C=10, kernel='poly', degree=2, gamma='scale', pca=None, scaler=None` |
| 🥈 | **Logistic Regression (LR)** | Tri-Domain (`Face ⊕ Emotion ⊕ Age`) | 2,304 | **92.73%** | 0.9275 | 0.9273 | 0.9273 | `C=0.1, solver='newton-cg', max_iter=500, pca=None, scaler=None` |
| 🥉 | **Random Forest (RF)** | Dual-Domain (`Emotion ⊕ Face`) | 1,536 | **86.85%** | 0.8689 | 0.8685 | 0.8682 | `n_estimators=200, max_depth=None, max_features='sqrt', min_samples_split=5, min_samples_leaf=1, pca=PCA(0.75), scaler=None` |
| 4 | **Gaussian Naive Bayes (GNB)** | Tri-Domain (`Face ⊕ Emotion ⊕ Age`) | 2,304 | **85.05%** | 0.8512 | 0.8505 | 0.8505 | `var_smoothing=5.8780e-03, pca=PCA(0.75), scaler=None` |

---

### 3. Analisis Komparatif Ablasi Data Leakage & Generalisasi

Perbandingan antara kedua skema partisi mengungkap wawasan empiris fundamental terkait efek memorisasi identitas (identity memorization) vs representasi fitur multi-domain yang mampu digeneralisasikan:

#### (a) Selisih Performa Lintas Konfigurasi (Subject-Overlap vs. Subject-Disjoint)

| Classifier | Konfigurasi Fitur | Akurasi Subject-Overlap (Lama) | Akurasi Subject-Disjoint (Baru) | Penurunan Nominal ($\Delta\text{Akurasi}$) | 95% Wilson CI (Baru) | Kesimpulan Generalisasi |
|---|---|:---:|:---:|:---:|:---:|---|
| **SVM** | **Tri-Domain (`Face ⊕ Emotion ⊕ Age`)** | **93.70%** | **88.61%** | **-5.09 pp** | [87.20%, 89.88%] | Generalisasi out-of-subject tinggi |
| **SVM** | Dual-Domain (`Emotion ⊕ Face`) | 93.29% | 88.43% | -4.86 pp | [87.01%, 89.71%] | Batas keputusan lintas subjek kokoh |
| **SVM** | Single-Domain (`vit-face`) | 90.83% | 86.16% | -4.68 pp | [84.64%, 87.55%] | Rentan terhadap petunjuk identitas wajah |
| **LR** | **Tri-Domain (`Face ⊕ Emotion ⊕ Age`)** | **92.73%** | **88.66%** | **-4.07 pp** | [87.25%, 89.93%] | Generalisasi puncak & penurunan terendah |
| **LR** | Dual-Domain (`Emotion ⊕ Face`) | 92.41% | 87.45% | -4.95 pp | [85.99%, 88.78%] | Model linier terdorong oleh fitur Age |
| **LR** | Single-Domain (`vit-face`) | 90.60% | 86.39% | -4.21 pp | [84.88%, 87.77%] | Baseline Face tunggal |
| **RF** | Tri-Domain (`Face ⊕ Emotion ⊕ Age`) | 86.20% | 85.00% | -1.20 pp | [83.43%, 86.44%] | Stabilitas lintas subjek moderat |
| **GNB** | Tri-Domain (`Face ⊕ Emotion ⊕ Age`) | 85.05% | 83.61% | -1.44 pp | [81.99%, 85.11%] | Baseline Naive Bayes |

#### (b) Temuan Empiris Utama & Pembuktian Statistik

1. **Eliminasi Memorisasi Identitas Wajah:**  
   Penurunan akurasi nominal sebesar ~4.0% hingga 5.1% pada seluruh pengklasifikasi teratas membuktikan bahwa model yang dievaluasi dengan protokol subject-overlap tanpa sengaja menghafal ciri khas identitas wajah (facial identity signatures). Hasil subject-disjoint mencerminkan generalisasi atribut demografis sejati pada individu yang sebelumnya belum pernah dilihat.
2. **Keunggulan Multi-Domain Signifikan secara Statistik ($p < 0.001$):**  
   Kekhawatiran utama yang disampaikan Reviewer 2 adalah apakah peningkatan performa fusi multi-domain hanyalah artefak dari kebocoran data (data leakage). Pengujian hipotesis inferensial (**Paired McNemar Test dengan koreksi kontinuitas Edwards**) pada held-out test set subject-disjoint secara definitif membantah kekhawatiran tersebut:
   - **SVM:** Tri-Domain (88.61%) mengungguli Single Face Biometrics (86.16%) secara signifikan dengan $\Delta = +2.45\%$ (+53 citra benar bersih, $\chi^2 = 20.9612$, **$p = 3.46 \times 10^{-6} < 0.001$**).
   - **Logistic Regression:** Tri-Domain (88.66%) mengungguli Single Face Biometrics (86.39%) secara signifikan dengan $\Delta = +2.27\%$ (+49 citra benar bersih, $\chi^2 = 19.6923$, **$p = 6.78 \times 10^{-6} < 0.001$**).
   - Peningkatan fusi multi-domain terbukti kokoh secara statistik dan tidak bergantung pada kebocoran identitas.
3. **Saturasi Fitur Asimtotik vs. Komplementaritas Linier:**  
   - Pada **Logistic Regression**, Tri-Domain (88.66%) meningkat secara signifikan dibandingkan Dual-Domain `Emotion ⊕ Face` (87.45%) dengan penambahan bersih +26 citra (**$p = 0.0073 < 0.01$**), membuktikan bahwa morfologi usia biologis memberikan sinyal diskriminatif ortogonal bagi hyperplane linier.
   - Pada **SVM**, Tri-Domain (88.61%) dan Dual-Domain `Emotion ⊕ Face` (88.43%) menghasilkan selisih bersih +4 citra ($p = 0.7343 > 0.05$), mengonfirmasi terjadinya saturasi representasi asimtotik di bawah kernel RBF non-linier.
4. **Ekuivalensi Prediktif & Efisiensi Komputasi Ekstrem (LR vs. SVM):**  
   - Uji McNemar berpasangan antara LR Tri-Domain (88.66%) dan SVM Tri-Domain (88.61%) menunjukkan ekuivalensi prediktif persis ($p = 1.0000$, selisih bersih +1 citra).
   - Namun, **LR memberikan inferensi >800× lebih cepat** (**0.0054 ms** vs. 4.4481 ms per citra) dan **ukuran model >330× lebih ringkas** (**0.11 MB** vs. 36.60 MB), menetapkan Logistic Regression sebagai model optimal untuk implementasi Edge AI pada perangkat dengan keterbatasan sumber daya.

> [!NOTE]
> **Temuan Kunci mengenai Independensi Multi-Domain ($p < 0.001$):**  
> Uji McNemar berpasangan membuktikan bahwa peningkatan performa fusi fitur ViT multi-domain signifikan secara statistik dan sepenuhnya bertahan di bawah partisi ketat tanpa kebocoran data (zero data leakage).

---

### 4. Profil Disparitas Subkelompok Interseksional (Held-out Subject-Disjoint Test Set)

Dievaluasi pada 6 subkelompok demografis interseksional ($N = 360$ citra uji unseen per subkelompok):

#### (a) Logistic Regression Tri-Domain (Model Benchmark Teratas: 88.66%)

| Subkelompok Demografis | Ras Makro | Gender | Recall / TPR | Precision | F1-Score | Support |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **White_Males** | White | Male | **94.44%** | **95.24%** | **94.84%** | 360 |
| **White_Females** | White | Female | 90.56% | 91.32% | 90.93% | 360 |
| **Black_Males** | Black | Male | 87.78% | 91.59% | 89.65% | 360 |
| **Asian_Males** | Asian | Male | 87.78% | 82.72% | 85.18% | 360 |
| **Asian_Females** | Asian | Female | 86.67% | 86.43% | 86.55% | 360 |
| **Black_Females** | Black | Female | 84.72% | 85.20% | 84.96% | 360 |
| **Macro Average** | **Semua** | **Semua** | **88.66%** | **0.8875** | **0.8868** | **2,160** |

#### (b) Support Vector Machine Tri-Domain (88.61%)

| Subkelompok Demografis | Ras Makro | Gender | Recall / TPR | Precision | F1-Score | Support |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **White_Males** | White | Male | **94.44%** | 93.92% | **94.18%** | 360 |
| **White_Females** | White | Female | 91.11% | 90.11% | 90.61% | 360 |
| **Black_Males** | Black | Male | 87.22% | 92.35% | 89.71% | 360 |
| **Asian_Males** | Asian | Male | 88.06% | 82.34% | 85.10% | 360 |
| **Asian_Females** | Asian | Female | 86.11% | 85.87% | 85.99% | 360 |
| **Black_Females** | Black | Female | 84.72% | 87.64% | 86.16% | 360 |
| **Macro Average** | **Semua** | **Semua** | **88.61%** | **0.8871** | **0.8863** | **2,160** |

> [!NOTE]
> **Metrik Disparitas Equal Opportunity:**  
> Kedua model berperforma teratas menunjukkan Equal Opportunity Difference (Max − Min Recall) yang identik sebesar **9.72 percentage points** lintas subkelompok demografis (White_Males 94.44% vs. Black_Females 84.72%), menyoroti disparitas interseksional yang masih ada untuk mitigasi keadilan (fairness mitigation) di masa mendatang.

---

### 5. Perbandingan dengan Studi Terdahulu pada DemogPairs

| Studi | Protokol Partisi | Arsitektur | Accuracy | Precision | Recall | F1-Score |
|---|---|---|:---:|:---:|:---:|:---:|
| Putri et al. (*JIEET 2025*) | Random Stratified (Subject-Overlap) | MD-ViT (Face + Age) + XGBoost | 89.07% | 0.8912 | 0.8907 | 0.8901 |
| Putri et al. (*ICVEE 2025*) | Random Stratified (Subject-Overlap) | Dual-ViT (Face + Emotion) + SVM | 92.41% | 0.9248 | 0.9241 | 0.9238 |
| **Diusulkan (Baseline Historis)** | **Random Stratified (Subject-Overlap)** | **Tri-Domain ViT + SVM** | **93.70%** | **0.9372** | **0.9370** | **0.9369** |
| **Diusulkan (Milestone Revisi)** | **Subject-Disjoint (Zero Leakage)** | **Tri-Domain ViT + LR** | **88.66%** | **0.8875** | **0.8866** | **0.8868** |
| **Diusulkan (Milestone Revisi)** | **Subject-Disjoint (Zero Leakage)** | **Tri-Domain ViT + SVM** | **88.61%** | **0.8871** | **0.8861** | **0.8863** |

---

## Kerangka Metodologi

```
                          [ Input Facial Image: 224x224 RGB ]
                                           │
         ┌─────────────────────────────────┼─────────────────────────────────┐
         ▼                                 ▼                                 ▼
   [ ViT-Face ]                     [ ViT-Emotion ]                    [ ViT-Age ]
(skutaada/VIT-VGGFace)        (dima806/facial_emotions...)        (dima806/facial_age...)
   [CLS] Token 768-d                 [CLS] Token 768-d                 [CLS] Token 768-d
         │                                 │                                 │
         └─────────────────────────────────┼─────────────────────────────────┘
                                           ▼
                    [ Feature Concatenation: z_tri in R^2304 ]
                                           │
                                           ▼
                  [ Preprocessing Pipeline: Scaler + PCA (Fold-level) ]
                                           │
                                           ▼
                 [ 5-Fold Stratified Subject-Disjoint GridSearchCV ]
                   (Logistic Regression / SVM / Random Forest / GNB)
                                           │
                                           ▼
                 [ Intersectional 6-Class Classification on DemogPairs ]
           (Asian_Females, Asian_Males, Black_Females, Black_Males, White_Females, White_Males)
```

### 1. Ekstraktor Vision Transformer Multi-Domain (768-D per domain)
- **ViT-Face** (`skutaada/VIT-VGGFace`): Pretrained pada biometrik wajah; menangkap geometri kraniofasial statis dan proporsi identitas wajah.
- **ViT-Emotion** (`dima806/facial_emotions_image_detection`): Pretrained pada ekspresi emosi wajah; menangkap petunjuk afektif dinamis dan localized action units.
- **ViT-Age** (`dima806/facial_age_image_detection`): Pretrained pada estimasi usia wajah; menangkap morfologi penuaan biologis dan pola tekstur epidermal.

### 2. Pipeline Fusi Fitur & Optimasi Klasifikasi
- **Ekstraksi Representasi Offline:** Representasi tingkat tinggi diekstraksi dari token `[CLS]` ternormalisasi ($\mathbf{z}_L^0 \in \mathbb{R}^{768}$) pada lapisan enkoder terakhir dari setiap backbone ViT-Base yang dibekukan (frozen).
- **7 Skema Ablasi Sistematis:**
  - *Single-Domain (768-D):* `Face`, `Emotion`, `Age`
  - *Dual-Domain (1,536-D):* `Emotion ⊕ Face`, `Face ⊕ Age`, `Emotion ⊕ Age`
  - *Tri-Domain (2,304-D):* `Face ⊕ Emotion ⊕ Age`
- **Leakage-Free Cross-Validation:** Transformasi preprocessing (MinMaxScaler dan PCA) difitting secara ketat hanya pada training fold di dalam objek `scikit-learn.pipeline.Pipeline` untuk mencegah kebocoran data.
- **Ruang Penjelajahan Grid Search:** Mengevaluasi total 1.086 kombinasi parameter ($38,010$ total cross-validation fits di seluruh 7 konfigurasi fitur dan 4 famili classifier).

---

## Struktur Repositori

```
.
├── .agents/skills/                        # Kerangka kerja peer review mandiri & skill autonomous AI agent
│   ├── ar-paper-reviewer/                 # Skill simulasi peer review akademik independen
│   ├── ar-paper-revision/                 # Skill penerapan patch revisi presisi tingkat byte (byte-level patching)
│   └── ar-paper-revision-coach/           # Coach dekonstruksi review, peta jalan revisi, & ledger sanggahan
├── authors.txt                            # Profil lengkap penulis, afiliasi institusi, dan ORCID ID
├── experiment/                            # Log eksperimen, dokumentasi metodologi, dan kode sumber
│   ├── 00_overview.md - 05_results.md     # Log eksperimen komprehensif dan audit metodologi
│   ├── dataset_demogpairs.md              # Spesifikasi dataset dan ringkasan partisi data
│   └── code/
│       ├── 1.1_vit-*_demogpairs.ipynb     # Notebook ekstraksi fitur (Face, Emotion, Age)
│       ├── 2.1.* - 2.5.*.ipynb            # Notebook classifier aktif Subject-Disjoint (SVM, GNB, RF, LR)
│       ├── 3.0_compare.ipynb              # Notebook perbandingan global 28 model & benchmarking (Subject-Disjoint)
│       ├── 3.1_statistical_significance.ipynb # Uji McNemar berpasangan, 95% Wilson Score CI, & audit keadilan EOD
│       ├── 4.0_test.ipynb                 # Rutinitas pengujian dan evaluasi model pada held-out test set
│       ├── app.py                         # Aplikasi web demo inferensi interaktif berbasis Gradio
│       ├── archive/                       # Arsip Baseline Historis Subject-Overlap (Ablasi Data Leakage)
│       │   ├── audit_ledger.json          # Buku besar audit terpadu yang membandingkan 28 model Lama vs 28 model Baru
│       │   ├── md_old/                    # Log Markdown (35 berkas) & confusion matrix dari eksperimen warisan
│       │   ├── models_old/                # Bobot model terlatih ter-serialisasi (.pkl) dari 28 model warisan
│       │   ├── notebook_old/              # 35 Jupyter Notebook dari eksperimen warisan (subject-overlap)
│       │   ├── results_old/               # 28 berkas hasil JSON mentah dari model warisan subject-overlap
│       │   └── README.md                  # Dokumentasi mendalam tentang tujuan arsip dan protokol audit
│       ├── scripts/                       # Runner eksekusi otonom & skrip antrean otomatis
│       │   ├── auto_run_experiments.py    # Skrip runner batch otomatis utama untuk seluruh 28 pipeline eksperimen
│       │   ├── run_gnb_queue.py           # Skrip runner antrean khusus untuk rangkaian model Gaussian Naive Bayes
│       │   ├── run_remaining_queue.py     # Skrip runner antrean tangguh untuk sisa beban kerja model
│       │   ├── run_experiments.bat        # Berkas batch Windows peluncur auto_run_experiments.py
│       │   ├── run_gnb.bat                # Berkas batch Windows peluncur antrean GNB
│       │   └── README.md                  # Dokumentasi operasional runner dan perintah eksekusi
│       ├── utils/                         # Modul pustaka utilitas (konstanta, dataset, evaluasi, dll.)
│       ├── dataset/demogpairs/metadata/   # 6 berkas metadata .txt (masing-masing 1.800 baris)
│       ├── features/                      # Vektor embedding fitur 768-D ter-serialisasi (.pkl)
│       ├── md/                            # Ekspor Markdown dari seluruh notebook & laporan statistik
│       ├── models/                        # Bobot model terlatih ter-serialisasi (.pkl) dari 28 model aktif
│       ├── results/                       # 28 berkas hasil JSON mentah dari model aktif Subject-Disjoint
│       └── images/                        # Plot kurva, confusion matrix, dan visualisasi 95% Wilson Score CI
├── images/                                # Diagram arsitektur beresolusi tinggi dan gambar ilustrasi
├── paper/                                 # Draf naskah modular dalam format Markdown (gaya IEEE Access)
│   ├── 00_abstract.md - 05_conclusion.md  # Bagian-bagian utama naskah artikel ilmiah
│   ├── 06_references.md                   # Repositori daftar pustaka IEEE terstandarisasi (entri [1]-[51])
│   ├── 07_biographies.md                  # Bagian VII: Biografi penulis & aset foto potret
│   ├── acronyms.txt                       # Registri akronim sentral naskah
│   ├── ref_part_*.md                      # 10 log audit bibliografi modular (entri [1]-[51])
│   ├── references.txt                     # Registri pelacakan & verifikasi sitasi tingkat kalimat
│   └── references/                        # 51 berkas sumber bibliografi (.bib, .ris, .nbib, .bibtex)
├── paper_latex_en/                        # Paket LaTeX IEEE Access siap submit (Bahasa Inggris)
│   ├── access.tex                         # Entrypoint LaTeX master dengan perintah \input{} modular
│   ├── access.pdf                         # Berkas PDF naskah Bahasa Inggris hasil kompilasi dua kolom
│   ├── ieeeaccess.cls / IEEEtran.bst      # Kelas dokumen resmi IEEE Access dan format bibliografi
│   ├── references.bib                     # Basis data terpadu BibTeX
│   └── sections/                          # 21 berkas section LaTeX modular (00_title.tex s.d. 07_biographies.tex)
├── paper_latex_id/                        # Paket LaTeX IEEE Access versi referensi Bahasa Indonesia
│   ├── access.tex / access.pdf            # Berkas sumber LaTeX & hasil kompilasi PDF Bahasa Indonesia
│   └── sections/                          # Bagian-bagian naskah terjemahan Bahasa Indonesia
├── paper_outline_v1.0.md                  # Master outline naskah v1.0 (Arsip historis pra-revisi / Subject-Overlap)
├── paper_outline_v1.1.md                  # Master outline naskah v1.1 (Definitif revisi IEEE Access / Subject-Disjoint)
├── paper_reviews/                         # Sistem audit simulasi mock peer review internal multi-agent (Round 1 & 2)
├── paper_reviews_ieee/                    # Berkas resmi keputusan editorial IEEE Access & dokumen revisi
│   ├── Comments.md                        # Umpan balik reviewer yang didekonstruksi dan matriks tanggapan
│   ├── IEEE-Access_Decision-on-Manuscript-ID-Access-2026-50857.md # Keputusan resmi & komentar reviewer
│   ├── IEEE-Access_Response-to-Reviewers-template.md              # Templat tanggapan butir-per-butir
│   ├── Request-for-Byline-Change.md                               # Formulir resmi perubahan susunan kepengarangan
│   └── Resubmission-Checklist.md                                  # Daftar periksa kepatuhan 10 poin resubmission
├── paper_submission/                      # Berkas pengemasan submisi formal & laporan kepatuhan IEEE
├── prompts.txt                            # Catatan kronologis prompt dan instruksi rekayasa eksperimen
├── README.ai.md                           # Panduan operasional agen AI utama dan indeks ground-truth
├── README.md                              # Dokumentasi riset publik utama (BERKAS INI)
├── WORKFLOW.md                            # Standard Operating Procedure (SOP) siklus pengembangan naskah
└── upload/                                # Artefak paket pengajuan siap kirim (PDF dan arsip ZIP sumber)
```

---

## Panduan Memulai Cepat & Reproduksi Eksperimen

### 1. Penyiapan Lingkungan Komputasi (Environment Setup)

```bash
# Membuat dan mengaktifkan virtual environment conda
conda create -n torch-gpu python=3.11 -y
conda activate torch-gpu

# Memasang dependensi yang dibutuhkan
pip install torch torchvision transformers scikit-learn imbalanced-learn joblib pandas numpy pillow matplotlib seaborn tqdm gradio nbconvert
```

### 2. Alur Kerja Reproduksi Eksperimen

#### Opsi A: Eksekusi Batch Otomatis via Skrip ([`experiment/code/scripts/`](experiment/code/scripts/))

```bash
cd experiment/code
python scripts/auto_run_experiments.py
```

#### Opsi B: Eksekusi Interaktif Langkah-demi-Langkah

1. **Ekstraksi Fitur ViT (Feature Extraction):** Jalankan `1.1_vit-face_demogpairs.ipynb`, `1.1_vit-emotion_demogpairs.ipynb`, dan `1.1_vit-age_demogpairs.ipynb` untuk menghasilkan representasi fitur di direktori `features/`.
2. **Pelatihan Pengklasifikasi (Subject-Disjoint Classifier Training):** Jalankan notebook eksperimen:
   - Logistic Regression: `2.5.1` hingga `2.5.7`
   - Support Vector Machine: `2.1.1` hingga `2.1.7`
   - Random Forest: `2.4.1` hingga `2.4.7`
   - Gaussian Naive Bayes: `2.2.1` hingga `2.2.7`
3. **Agregasi & Perbandingan Hasil:** Jalankan `3.0_compare.ipynb` untuk menggabungkan ke-28 berkas hasil JSON ke dalam papan peringkat benchmark terpadu.
4. **Pengujian Signifikansi Statistik & Keadilan:** Jalankan `3.1_statistical_significance.ipynb` untuk menghitung uji McNemar berpasangan, 95% Wilson Score CI, dan audit keadilan algoritmik EOD (Equal Opportunity Difference).
5. **Demo Web Interaktif:** Jalankan `python app.py` untuk mengaktifkan antarmuka web inferensi secara real-time.

---

## Tim Peneliti

- **Dr. Ir. Ricky Eka Putra, S.Kom., M.Kom.** ([ORCID](https://orcid.org/0000-0002-5515-7967)) — Penulis Korespondensi (`rickyeka@unesa.ac.id`)
- **Rezky Arisanti Putri, S.Kom., M.Kom.** ([ORCID](https://orcid.org/0009-0000-8021-1833))
- **Dr. Yuni Yamasari, S.Kom., M.Kom.** ([ORCID](https://orcid.org/0000-0001-9719-3491))
- **Rafy Aulia Akbar, S.Kom., M.Kom.** ([ORCID](https://orcid.org/0009-0003-6991-0694))
- **Assoc. Prof. Dr. Shukor Sanim Mohd Fauzi** ([ORCID](https://orcid.org/0000-0003-4333-7853)) (`shukorsanim@uitm.edu.my`)

*Afiliasi Institusi:*
- **Departemen Informatika, Fakultas Informatika, Universitas Negeri Surabaya**, Surabaya, Jawa Timur, Indonesia (Putra, Putri, Yamasari, Akbar).
- **School of Computing Sciences, College of Computing, Informatics and Mathematics, Universiti Teknologi MARA**, Cawangan Perlis, Kampus Arau, 02600 Arau, Perlis, Malaysia (Mohd Fauzi).

---

## Sitasi

Jika Anda memanfaatkan penelitian atau basis kode ini dalam karya ilmiah Anda, silakan mensitasi publikasi berikut:

```bibtex
@article{putra2026multidomain,
  title={Multi-Domain Vision Transformer Fusion for Intersectional Demographic Classification from Facial Images},
  author={Putra, Ricky Eka and Putri, Rezky Arisanti and Yamasari, Yuni and Akbar, Rafy Aulia and Mohd Fauzi, Shukor Sanim},
  journal={IEEE Access},
  year={2026}
}

@inproceedings{hupont2019demogpairs,
  title={DemogPairs: Quantifying the Impact of Demographic Imbalance in Deep Face Recognition},
  author={Hupont, Isabelle and Fernandez, Carles},
  booktitle={2019 14th IEEE International Conference on Automatic Face & Gesture Recognition (FG 2019)},
  pages={1--7},
  year={2019},
  doi={10.1109/FG.2019.8756625}
}
```
