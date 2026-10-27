# Persiapan Data DemogPairs (Race × Gender Classification)

## Ringkasan

Penelitian menggunakan **DemogPairs** (Hupont & Fernández, FG 2019) sebagai satu-satunya sumber citra untuk klasifikasi interseksional **6 kelas** (3 ras × 2 gender: *Asian, Black, White* × *Female, Male*). Repositori ini mengimplementasikan **Sistem Dual-Benchmark Komparatif** untuk mengevaluasi performa model secara transparan dan menanggapi secara tuntas catatan penelaah **IEEE Access** (khususnya **Reviewer 2 Comment #2: Data Leakage and Generalization**):

1. **Protokol Utama Revisi IEEE Access (Subject-Disjoint Split — Zero Data Leakage):**
   - Partisi terstratifikasi murni pada level identitas individu (`subject_id`): **480 subjek latih (8.640 citra)** dan **120 subjek uji held-out independen (2.160 citra)**.
   - Kebocoran data identitas subjek bernilai **0.00% (bebas kebocoran identitas secara mutlak)**.
   - Menghasilkan evaluasi generalisasi sejati (*true out-of-subject generalization*).
2. **Tolok Ukur Historis Baseline (Subject-Overlap Split — 100% Identity Leakage):**
   - Partisi acak terstratifikasi pada level citra (*image-level stratified random split* 80/20, 8.640 latih / 2.160 uji).
   - Memiliki kebocoran identitas **100%** (seluruh 593 subjek uji hadir di set pelatihan dengan foto kondisi/pose berbeda).
   - Dipertahankan sebagai studi ablasi empiris untuk membuktikan dampak *shortcut learning* akibat kebocoran data.

| Atribut | Detail Protokol Utama (Subject-Disjoint) | Detail Baseline Historis (Subject-Overlap) |
|---|---|---|
| **Dataset** | DemogPairs — DOI `10.1109/FG.2019.8756625` | DemogPairs — DOI `10.1109/FG.2019.8756625` |
| **Total Citra** | **10.800** (600 subjek unik × 18 citra) | **10.800** (600 subjek unik × 18 citra) |
| **Kelas** | **6 interseksional**, 1.800 citra per kelas (seimbang sempurna) | **6 interseksional**, 1.800 citra per kelas (seimbang sempurna) |
| **Metode Split** | Subject-Level Stratified (`u.split_demogpairs_subject_disjoint`) | Image-Level Stratified (`train_test_split(stratify=y)`) |
| **Partisi Subjek** | **480 Subjek Latih / 120 Subjek Uji** (80:20 per kelas) | 600 Subjek tersebar acak (593 subjek hadir di kedua set) |
| **Partisi Citra** | **8.640 Latih / 2.160 Uji** (1.440 : 360 per kelas) | **8.640 Latih / 2.160 Uji** (1.440 : 360 per kelas) |
| **Tingkat Kebocoran Identitas** | **0,00% (0 subjek uji bocor di set latih)** | **100,00% (593 dari 593 subjek uji bocor di set latih)** |
| **Validasi Silang (CV)** | 5-Fold `StratifiedGroupKFold(groups=subject_id)` | 5-Fold `StratifiedKFold()` |
| **Cakupan Model** | 28 Konfigurasi Model (7 skema fitur × 4 klasifikator) | 28 Konfigurasi Model (7 skema fitur × 4 klasifikator) |
| **Lokasi File** | `experiment/code/dataset/demogpairs/` | `experiment/code/dataset/demogpairs/` |

---

## Komposisi Dataset

Setiap kelas terdiri dari **100 subjek × 18 citra = 1.800 citra**, dengan pemetaan indeks:

| Kelas | Ras | Gender | Subjek | Citra | Indeks (`label_idx`) |
|---|:---:|:---:|:---:|:---:|:---:|
| Black_Males | Black | Male | 100 | 1.800 | 0 |
| White_Females | White | Female | 100 | 1.800 | 1 |
| Asian_Males | Asian | Male | 100 | 1.800 | 2 |
| White_Males | White | Male | 100 | 1.800 | 3 |
| Black_Females | Black | Female | 100 | 1.800 | 4 |
| Asian_Females | Asian | Female | 100 | 1.800 | 5 |
| **Total** | 3 ras | 2 gender | **600** | **10.800** | 0–5 |

Pemetaan didefinisikan di `utils/constants.py` dan konsisten digunakan di seluruh notebook, fitur, evaluasi matriks konfusi, dan pelaporan metrik.

---

## Struktur Direktori & Metadata

`metadata/` berisi 6 berkas teks (satu per kelas, masing-masing 1.800 baris data + 1 header), sedangkan `images/` berisi 600 folder identitas dengan 18 citra JPEG tiap folder (total 10.800 citra).

Setiap berkas metadata berformat whitespace-separated dengan header `db_code image_path`.
- Kolom `db_code` mencatat provenance (CWF, VGGFace, atau VGGFace2) dan tidak dipakai sebagai fitur klasifikasi.
- Kolom `image_path` menjadi kunci utama untuk mencocokkan citra dengan vektor fitur pada `features/demogpairs_vit-*.pkl`.
- `subject_id` diekstrak dari segmen pertama `image_path` (nama subfolder identitas, mis. `able_wanamakok`), berfungsi sebagai pengelompokan grup identitas (*grouping key*) untuk partisi *subject-disjoint* dan *StratifiedGroupKFold*.

---

## Pembagian Dataset: Subject-Disjoint vs. Subject-Overlap

### 1. Kaitan Eksplisit dengan Telaah Kritis Reviewer 2 IEEE Access

Pada proses telaah naskah IEEE Access (`Access-2026-50857`), Reviewer 2 menyampaikan komentar kunci No. 2:
> *"2. Data leakage and generalization: The image-level stratified split may allow images of the same identity to occur in both training and test sets. Please clarify whether identity overlap exists and provide subject-disjoint evaluation to establish genuine generalization."*

Komentar ini mengidentifikasi kelemahan metodologis fundamental pada *image-level split*: jika citra dari subjek yang sama hadir di set pelatihan dan pengujian, model berkapasitas tinggi dapat menghafal fitur visual spesifik individu (*identity shortcuts*) alih-alih mempelajari batas demografis umum. Untuk menjawab tantangan tersebut secara tuntas, penelitian membangun sistem pengujian ganda (*dual-benchmark*).

### 2. Protokol Utama: Subject-Disjoint Stratified Partitioning (Zero Data Leakage)

Pemisahan data dilakukan pada level subjek (`subject_id`) menggunakan fungsi `split_demogpairs_subject_disjoint` pada `utils/dataset.py`:
- Dari 100 subjek per kelas, **80 subjek dialokasikan untuk pelatihan** dan **20 subjek dialokasikan untuk pengujian held-out independen** (`train_size=0.8, random_state=42`).
- **Data Latih:** 480 subjek × 18 citra = **8.640 citra** (1.440 citra per kelas).
- **Data Uji:** 120 subjek × 18 citra = **2.160 citra** (360 citra per kelas).
- **Tingkat Tumpang Tindih Identitas (*Identity Overlap*):** Tepat **0 subjek (0,00%)**. Tidak ada satu pun citra dari 120 subjek uji yang pernah dilihat oleh model selama proses pelatihan atau pencarian hyperparameter.
- **Validasi Silang Terisolasi:** Di dalam data latih (8.640 citra), validasi silang dilakukan menggunakan `StratifiedGroupKFold(n_splits=5, shuffle=True, random_state=42)` dengan `groups=groups_train`. Setiap fold validasi berisi tepat 16 subjek per kelas (96 subjek = 1.728 citra), sehingga isolasi identitas subjek terjaga 100% pada setiap iterasi cross-validation.

### 3. Protokol Baseline Historis: Subject-Overlap Image-Level Split (100% Identity Leakage)

Sebelum revisi IEEE Access, partisi dilakukan secara acak pada tingkat citra menggunakan `train_test_split(..., stratify=y, test_size=0.2, random_state=42)`:
- Menghasilkan 8.640 citra latih dan 2.160 citra uji (proporsi citra 80:20 per kelas).
- Namun, audit empiris membuktikan bahwa **593 dari 593 subjek unik pada set uji (100,00%) juga hadir pada set pelatihan**.
- Protokol ini dipertahankan sebagai tolok ukur historis untuk studi ablasi kebocoran data (*data leakage ablation study*), memberikan bukti empiris kuantitatif mengenai besaran inflasi performa (*shortcut learning effect*) yang terjadi akibat kebocoran identitas.

### Perbandingan Komparatif Struktur Partisi:

| Parameter Partisi | Protokol Utama (Subject-Disjoint) | Protokol Historis (Subject-Overlap) | Status Metodologis |
|---|:---:|:---:|---|
| **Fungsi Partisi** | `split_demogpairs_subject_disjoint` | `train_test_split(stratify=y)` | Protokol Utama memenuhi standar ketat biometrik |
| **Unit Pemisahan** | Identitas Subjek (`subject_id`) | Citra individual (`image_path`) | Pemisahan subjek mencegah *identity shortcut* |
| **Subjek Latih** | **480 subjek** (80 per kelas) | 600 subjek (tersebar) | 100% subjek latih terisolasi |
| **Subjek Uji Held-out** | **120 subjek** (20 per kelas) | 593 subjek (tumpang tindih) | 120 subjek uji benar-benar baru (*unseen*) |
| **Overlap Subjek Uji di Train** | **0 subjek (0,00%)** | **593 subjek (100,00%)** | **Bebas kebocoran data secara mutlak** |
| **Citra Latih** | 8.640 citra (1.440 per kelas) | 8.640 citra (1.440 per kelas) | Ukuran data latih identik |
| **Citra Uji** | 2.160 citra (360 per kelas) | 2.160 citra (360 per kelas) | Ukuran data uji identik |
| **Skema CV Latih** | `StratifiedGroupKFold(n_splits=5)` | `StratifiedKFold(n_splits=5)` | CV bebas kontaminasi identitas |
| **Subjek Overlap per Fold CV** | **0 subjek (0,00%)** | **~572 - 581 subjek (~99%)** | Pencegahan kebocoran antar-lipatan |

---

## Konsistensi untuk 28 Eksperimen

Penelitian menjalankan **28 konfigurasi eksperimen** dari kombinasi **7 skema fitur ViT** (`vit-face`, `vit-emotion`, `vit-age`, `vit-face-age`, `vit-emotion-age`, `vit-emotion-face`, `vit-face-emotion-age`) dan **4 keluarga klasifikator** (Support Vector Machine, Logistic Regression, Random Forest, Gaussian Naive Bayes).

Untuk masing-masing protokol:
- Seluruh 28 model melihat indeks latih yang identik (8.640 sampel) dan dievaluasi pada indeks uji held-out yang identik (2.160 sampel).
- Paritas ini menjamin bahwa variasi performa antar-model murni bersumber dari representasi fitur laten atau algoritma klasifikasi, bukan fluktuasi partisi data.
- Pada protokol Subject-Disjoint, model terbaik dicapai oleh **Logistic Regression (LR) Tri-Domain** (Akurasi **88,66%**, Macro F1 **0,8868**) dan **SVM Tri-Domain** (Akurasi **88,61%**, Macro F1 **0,8863**) yang terbukti ekuivalen secara statistik ($p = 1,0000$), di mana LR unggul mutlak dalam efisiensi komputasi (>820× lebih cepat, >330× lebih hemat memori).

---

## Validasi & Posisi dalam Alur Riset

Pemeriksaan integritas data mencakup: verifikasi kelengkapan 10.800 berkas citra, keselarasan metadata terhadap nama folder identitas, keseimbangan kelas sempurna (1.800 citra/kelas), determinisme indeks partisi dengan seed 42, dan verifikasi zero-overlap identitas subjek.

```
DemogPairs (10.800 Citra, 600 Subjek)
  │
  ├── [01] Persiapan Data & Partisi Dual-Benchmark:
  │     ├─ [Protokol Utama Revisi IEEE Access] Subject-Disjoint: 480 Train (8.640) / 120 Test (2.160) — 0% Leakage
  │     └─ [Baseline Historis Ablasi] Subject-Overlap: 8.640 Train / 2.160 Test — 100% Identity Overlap
  │
  ├── [02] Preprocessing: Standarisasi 224×224, konversi RGB, normalisasi AutoImageProcessor
  │
  ├── [03] Ekstraksi Fitur ViT: Ekstraksi offline token [CLS] 768-D per domain (Face, Emotion, Age)
  │
  ├── [04] Metode Klasifikasi: Pipeline MinMaxScaler → PCA → Classifier (SVM, LR, RF, GNB)
  │     ├─ Subject-Disjoint: 5-Fold StratifiedGroupKFold (groups=subject_id)
  │     └─ Subject-Overlap: 5-Fold StratifiedKFold
  │
  └── [05] Hasil & Analisis: Evaluasi 28 model per protokol, 95% Wilson CI, McNemar Test, Efisiensi, Fairness, & Ablasi Kebocoran
```

---

## Referensi Silang

- `dataset_demogpairs.md` — Rincian teknis distribusi subjek, citra, dan struktur DemogPairs
- `00_overview.md` — Ikhtisar komprehensif kerangka riset dan dual-benchmark
- `02_preprocessing.md` — Pipeline normalisasi dan prapemrosesan citra
- `03_feature-extraction.md` — Ekstraksi token [CLS] 768-D ViT multi-domain
- `04_methods.md` — Formulasi 4 klasifikator, ruang hyperparameter, dan protokol GridSearchCV
- `05_results.md` — Laporan lengkap hasil eksperimen 56 model (28 Subject-Disjoint + 28 Subject-Overlap)
- `paper_reviews_ieee/Comments.md` — Rincian komentar Associate Editor dan Reviewer IEEE Access
- `utils/dataset.py` dan `utils/constants.py` — Implementasi fungsi pemisahan data dan konstanta kelas
