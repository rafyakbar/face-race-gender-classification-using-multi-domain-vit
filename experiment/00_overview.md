# Framework Penelitian - Multi-Domain ViT + 4 Classifier untuk Klasifikasi Ras & Gender

## Ringkasan

Penelitian ini mengklasifikasikan **6 kelas interseksional** (3 Ras $\times$ 2 Gender: Asian/Black/White $\times$ Female/Male) pada citra wajah dengan pendekatan **Cross-Domain Feature Fusion**. Tiga arsitektur Vision Transformer (ViT-Base) digunakan sebagai ekstraktor fitur representasi tugas (*task-associated representation*):

- **ViT-Face** — 768 dimensi (morfologi identitas & geometri wajah)
- **ViT-Emotion** — 768 dimensi (ekspresi wajah & dinamika afektif)
- **ViT-Age** — 768 dimensi (tekstur penuaan & estimasi usia biologis)

Konkatenasi tri-domain menghasilkan vektor fitur gabungan **2.304 dimensi**. Penelitian menggunakan dataset terstandarisasi **DemogPairs** dengan total **10.800 citra wajah seimbang** (600 identitas subjek unik $\times$ 18 foto per subjek, 1.800 citra per kelas demografi).

---

## Dua Protokol Eksperimen: Subject-Disjoint (Utama) vs. Subject-Overlap (Historis)

Untuk menjamin kepatuhan metodologis tertinggi sesuai telaah pakar jurnal **IEEE Access** (menanggapi secara tuntas **Reviewer 2 Comment #2 mengenai Data Leakage and Generalization**), penelitian ini mendokumentasikan dan membandingkan **dua protokol evaluasi secara transparan**:

1. **Protokol Utama Revisi IEEE Access (Subject-Disjoint Split — Zero Data Leakage):**
   - Pembagian data dilakukan murni pada level identitas individu (`subject_id`): **480 subjek latih (8.640 citra)** dan **120 subjek uji held-out independen (2.160 citra, 20 subjek/kelas)**.
   - Kebocoran data identitas subjek bernilai **0.00% (bebas kebocoran identitas secara mutlak)**.
   - Optimasi hyperparameter menggunakan 5-Fold *StratifiedGroupKFold* pada set pelatihan (memastikan tidak ada subjek yang muncul bersamaan di fold latih dan validasi).
   - Menghasilkan evaluasi generalisasi sejati (*true out-of-subject generalization*).

2. **Tolok Ukur Historis Baseline (Subject-Overlap Split — 100% Identity Leakage):**
   - Pembagian data awal menggunakan metode acak berstrata tingkat citra (*image-level stratified random split* 80/20, `random_state=42`).
   - Memiliki kebocoran identitas **100%** (seluruh 593 subjek uji hadir di set pelatihan dengan foto pose/kondisi berbeda).
   - Dipertahankan secara utuh sebagai dasar **Studi Ablasi Kebocoran Data (*Data Leakage Ablation Study*)** untuk membuktikan fenomena *shortcut learning*.

### Perbandingan Ringkasan Performa Puncak 4 Klasifikator pada Kedua Protokol:

| Classifier | Kombinasi Parameter | Subject-Disjoint (Revisi Utama - Zero Leakage) | 95% Wilson CI (Disjoint) | Subject-Overlap (Historis - 100% Leakage) | Drop Generalisasi ($\Delta \text{Acc}$) | Latensi Inferensi | Ukuran Model | Konfigurasi Terbaik (Subject-Disjoint) |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **Logistic Regression (LR)** | 270 | **88,66%** (F1: **0,8868**) | **[87,25%, 89,93%]** | 92,73% (F1: 0,9273) | -4,07 pp | **0,0054 ms** | **0,11 MB** | **Tri-Domain (`Face ⊕ Emotion ⊕ Age`)** |
| **Support Vector Machine (SVM)** | 288 | **88,61%** (F1: **0,8863**) | **[87,20%, 89,88%]** | **93,70%** (F1: **0,9369**) | -5,09 pp | 4,4481 ms | 36,60 MB | **Tri-Domain (`Face ⊕ Emotion ⊕ Age`)** |
| **Random Forest (RF)** | 288 | 85,00% (F1: 0,8493) | [83,43%, 86,44%] | 86,85% (F1: 0,8682) | -1,85 pp | 0,0537 ms | 6,19 MB | Tri-Domain (`Face ⊕ Emotion ⊕ Age`) |
| **Gaussian Naive Bayes (GNB)** | 240 | 84,31% (F1: 0,8430) | [82,71%, 85,78%] | 85,05% (F1: 0,8505) | -0,74 pp | 0,0081 ms | 0,78 MB | Dual-Domain (`Emotion ⊕ Face`) |

> **Temuan Signifikansi Inferensial:** Pada protokol Subject-Disjoint, **LR Tri-Domain (88,66%) dan SVM Tri-Domain (88,61%) terbukti ekuivalen secara statistik** berdasarkan Uji McNemar berpasangan ($p = 1,0000$, selisih bersih hanya +1 citra). Namun, LR menawarkan keunggulan komputasi luar biasa (>820$\times$ lebih cepat dan >330$\times$ lebih hemat memori), menjadikannya pilihan optimal untuk *Edge AI*.

---

## Alur Penelitian

```
DemogPairs 10.800 Citra (600 Subjek × 18 Foto)
  │
  ├── Normalisasi Citra 224×224 → 3 Vision Transformers (Face, Emotion, Age)
  │     └── Ekstraksi Offline Token [CLS] (768 dimensi per domain)
  │
  ├── Fusi Fitur Lintas Domain: 7 Skema (Single: 768-d | Dual: 1.536-d | Tri: 2.304-d)
  │
  ├── Partisi Data Komparatif:
  │     ├─ [Protokol Utama] Subject-Disjoint: 480 subjek latih (8.640) / 120 subjek uji (2.160) — Zero Leakage
  │     └─ [Baseline Historis] Subject-Overlap: 8.640 latih / 2.160 uji (image-level) — 100% Identity Overlap
  │
  ├── Pipeline Klasifikasi Terenkapsulasi (Mencegah Kebocoran Informasi):
  │     └── MinMaxScaler → PCA (opsional) → Klasifikator (SVM, LR, RF, GNB)
  │
  ├── Optimasi Hyperparameter:
  │     ├─ Subject-Disjoint: 5-Fold StratifiedGroupKFold (groups = subject_id, 38.010 fits)
  │     └─ Subject-Overlap: 5-Fold StratifiedKFold (38.010 fits)
  │
  └── Evaluasi Holistik pada 2.160 Citra Uji Independen:
        ├─ Metrik Global (Akurasi, Presisi, Recall, Macro F1)
        ├─ Interval Kepercayaan 95% Wilson Score
        ├─ Uji Signifikansi Statistik Inferensial (McNemar & Exact Binomial)
        ├─ Evaluasi Profil Efisiensi Komputasi (Latensi & Ukuran Memori)
        ├─ Analisis Keadilan Algoritmik (One-vs-Rest & Equal Opportunity Disparity)
        └─ Studi Komparatif Ablasi Kebocoran Data (Tanggapan Reviewer 2)
```

---

## Skema Konfigurasi Fitur ViT (7 Varian)

| # | Konfigurasi Fitur | Tipe Domain | Dimensi | Komposisi Ekstraktor |
|:---:|:---|:---:|:---:|:---|
| 1 | `vit-age` | Single-Domain | 768 | ViT-Age murni |
| 2 | `vit-emotion` | Single-Domain | 768 | ViT-Emotion murni |
| 3 | `vit-face` | Single-Domain | 768 | ViT-Face murni |
| 4 | `vit-emotion-age` | Dual-Domain | 1.536 | Emotion $\oplus$ Age |
| 5 | `vit-face-age` | Dual-Domain | 1.536 | Face $\oplus$ Age |
| 6 | `vit-emotion-face` | Dual-Domain | 1.536 | Emotion $\oplus$ Face |
| 7 | `vit-face-emotion-age` | **Tri-Domain (Usulan Utama)** | **2.304** | **Face $\oplus$ Emotion $\oplus$ Age** |

---

## Pipeline Klasifikasi Bebas Kebocoran

```
Fitur ViT (768 / 1.536 / 2.304-d) ──> Penskalaan (MinMaxScaler) ──> Reduksi Dimensi (PCA) ──> Klasifikasi ──> Prediksi Kelas (0–5)
```

Pipeline dirancang dengan prinsip enkapsulasi ketat (*strict encapsulation*):
- Penskalaan fitur (`MinMaxScaler`) dan reduksi dimensi (`PCA`) dipelajari **hanya dari fold pelatihan** pada setiap iterasi validasi silang (*cross-validation*), mencegah kebocoran informasi (*information leakage*).
- Pada protokol Subject-Disjoint, seluruh proses *grid search* menggunakan `StratifiedGroupKFold` dengan pengelompokan berdasarkan `subject_id`, memastikan model tidak pernah mengevaluasi citra dari individu yang ada di set pelatihan fold tersebut.

---

## Temuan Saintifik Utama

1. **Keunggulan Konsisten Fusi Multi-Domain Lintas Individu Baru:**
   - Penambahan representasi ekspresi emosi dan usia biologis terhadap representasi fitur wajah murni (`vit-face`) memberikan lonjakan akurasi signifikan: **+2.45 pp pada SVM** ($p = 3.46 \times 10^{-6}$) dan **+2.27 pp pada LR** ($p = 6.78 \times 10^{-6}$). Hal ini membuktikan bahwa fusi multi-domain ViT menghasilkan representasi yang kaya dan dapat digeneralisasi pada subjek yang belum pernah dilihat sebelumnya.
2. **Kejenuhan Representasi Asimtotik (*Asymptotic Feature Saturation*):**
   - Pada SVM, penambahan domain usia dari Dual `vit-emotion-face` (88,43%) ke Tri-Domain (88,61%) hanya menghasilkan kenaikan +0,19 pp (+4 citra) yang tidak signifikan secara statistik ($p = 0.7343$). Namun, pada LR, kenaikan ini bernilai +1,20 pp (+26 citra) dan signifikan ($p = 0.0073$).
3. **Ekuivalensi Prediktif & Efisiensi Ekstrim:**
   - LR Tri-Domain (88,66%) dan SVM Tri-Domain (88,61%) ekuivalen secara statistik ($p = 1.0000$), namun LR mengeksekusi inferensi dalam **0,0054 ms** (vs 4,4481 ms pada SVM) dengan ukuran bobot hanya **110 KB** (vs 36,6 MB pada SVM).
4. **Analisis Disparitas Kesetaraan Demografis (Fairness):**
   - Evaluasi interseksional menunjukkan *Equal Opportunity Disparity* terkecil pada LR dan SVM ($\Delta \text{TPR} = 9.72$ pp), dengan recall tertinggi pada kelompok *White Males* (94,44%) dan terendah pada *Black Females* (84,72%). Kesalahan klasifikasi dominan terjadi antar-ras dengan gender yang sama, bukan lintas-gender.
5. **Dampak Kebocoran Data terhadap Karakteristik Klasifikator:**
   - Perbandingan langsung antara protokol Subject-Overlap (93,70%) dan Subject-Disjoint (88,66%) membuktikan bahwa model non-linier kompleks (SVM) lebih rentan menghafal ciri khas identitas individu (drop $-5.09$ pp), sedangkan model batas keputusan linier teregularisasi (LR) lebih tangguh mempertahankan performa generalisasi (drop $-4.07$ pp).

---

## Struktur Dokumen Penelitian

- **`00_overview.md`** — Ikhtisar komprehensif ini (kerangka riset, kedua protokol, dan hasil utama)
- **`01_prepare-data.md`** — Spesifikasi dataset DemogPairs dan prosedur pemisahan data
- **`02_preprocessing.md`** — Preprocessing citra dua tingkat (ekstraksi token ViT & pipeline normalisasi)
- **`03_feature-extraction.md`** — Arsitektur 3 Vision Transformer (Face, Emotion, Age) dan fusi offline
- **`04_methods.md`** — Formulasi 4 algoritma klasifikasi dan protokol GridSearchCV
- **`05_results.md`** — Laporan hasil eksperimen lengkap 3 Bagian:
  - *Bagian 1:* Hasil 28 Model Subject-Disjoint (95% Wilson CI, Uji McNemar, Profil Latensi/Memori, Fairness OvR)
  - *Bagian 2:* Hasil 28 Model Historis Subject-Overlap (100% Identity Leakage Baseline)
  - *Bagian 3:* Analisis Komparatif Ablasi Kebocoran Data (Tanggapan Komprehensif IEEE Access Reviewer 2)
- **`dataset_demogpairs.md`** — Rincian teknis distribusi subjek dan citra DemogPairs
- **`code/`** — Kode sumber eksperimen:
  - `code/results/`: 28 berkas JSON hasil evaluasi Subject-Disjoint
  - `code/archive/`: Berkas historis Subject-Overlap (`audit_ledger.json`, `results_old/`, `models_old/`, `notebook_old/`)
  - `code/md/`: Laporan analitis mendalam (`3.0_compare.md`, `3.1_statistical_significance.md`)

---

## Referensi Akademik

1. Hupont, I., & Fernández, C. (2019). *DemogPairs: Quantifying the Impact of Demographic Imbalance in Deep Face Recognition*. IEEE International Conference on Automatic Face and Gesture Recognition (FG 2019), DOI: `10.1109/FG.2019.8756625`.
2. Dosovitskiy, A., et al. (2021). *An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale*. International Conference on Learning Representations (ICLR 2021).
3. Buolamwini, J., & Gebru, T. (2018). *Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification*. Conference on Fairness, Accountability and Transparency (FAT* 2018).
4. Edwards, A. L. (1948). *Note on the "correction for continuity" in test of significance for the 2x2 table*. Journal of the American Statistical Association, 43(244), 384-387.
5. Wilson, E. B. (1927). *Probable inference, the law of population, and the golden mean*. Proceedings of the National Academy of Sciences, 13(8), 649-655.
