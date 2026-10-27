# Lingkungan Eksperimen & Eksekusi Klasifikasi Multi-Domain ViT (DemogPairs)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.10%2Bcu126-EE4C2C.svg)](https://pytorch.org/)
[![Transformers](https://img.shields.io/badge/Transformers-5.7.0-yellow.svg)](https://huggingface.co/transformers/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.8.0-F7931E.svg)](https://scikit-learn.org/)
[![Evaluation](https://img.shields.io/badge/Protocol-Subject--Disjoint%20(0%25%20Leakage)-brightgreen.svg)]()

Repositori ini memuat seluruh kode sumber, konfigurasi komputasi, skrip otomatisasi, bobot model terlatih, dan berkas analisis evaluasi untuk eksperimen klasifikasi interseksional ras dan gender citra wajah pada dataset **DemogPairs**. 

Kerangka kerja ini mengevaluasi integrasi representasi laten multi-domain berbasis arsitektur **Vision Transformer (ViT)**—menggabungkan domain fitur identitas wajah (*facial identity*), ekspresi emosi wajah (*facial emotion*), dan estimasi usia (*facial age*)—yang dipasangkan dengan empat keluarga algoritma klasifikasi tradisional melalui protokol partisi independen **Subject-Disjoint** (tanpa kebocoran identitas subjek).

---

## Daftar Isi

1. [Ringkasan Eksekutif & Temuan Kunci](#ringkasan-eksekutif--temuan-kunci)
2. [Protokol Partisi Data & Pembuktian 0% Kebocoran](#protokol-partisi-data--pembuktian-0-kebocoran)
3. [Ikhtisar 33 Notebook Eksperimen Aktif](#ikhtisar-33-notebook-eksperimen-aktif)
   - [3 Notebook Ekstraksi Fitur Laten (ViT)](#1-notebook-ekstraksi-fitur-laten-vit-3-berkas)
   - [28 Notebook Klasifikasi & Tuning Hiperparameter](#2-notebook-klasifikasi--tuning-hiperparameter-28-berkas)
   - [Standardisasi Arsitektur Tepat 16 Sel Notebook](#standardisasi-arsitektur-tepat-16-sel-notebook)
   - [2 Notebook Analisis Komparatif & Signifikansi Statistik](#3-notebook-analisis-komparatif--signifikansi-statistik-2-berkas)
4. [Peta Struktur Subfolder & Modul Kode](#peta-struktur-subfolder--modul-kode)
   - [Pustaka Modular Python (`utils/`)](#pustaka-modular-python-utils)
   - [Rincian Direktori Penyimpanan](#rincian-direktori-penyimpanan)
5. [Panduan Eksekusi & Alur Kerja](#panduan-eksekusi--alur-kerja)
   - [Evaluasi Cepat via Model Terlatih (Bypass Fit Ulang)](#opsi-a-evaluasi-cepat-via-model-terlatih-bypass-fit-ulang)
   - [Eksekusi Batch Otomatis (Headless Runner)](#opsi-b-eksekusi-batch-otomatis-headless-runner)
   - [Aplikasi Demo Web Interaktif (Gradio)](#opsi-c-aplikasi-demo-web-interaktif-gradio)
6. [Lingkungan Komputasi & Reprodusibilitas](#lingkungan-komputasi--reprodusibilitas)

---

## Ringkasan Eksekutif & Temuan Kunci

Eksperimen ini menginvestigasi hipotesis bahwa penggabungan representasi semantik laten dari model ViT yang dilatih pada domain komplementer (identitas wajah, emosi, dan usia) mampu menghasilkan pengklasifikasi ras-gender yang tangguh (*robust*) terhadap variasi pose, pencahayaan, dan demografi.

> [!IMPORTANT]
> Seluruh eksperimen pada direktori ini tunduk pada protokol **Subject-Disjoint murni (0.00% kebocoran identitas subjek)**. Sebanyak 120 subjek pada *held-out test set* (2.160 citra) sepenuhnya diisolasi dari tahap pelatihan dan penalaan hiperparameter, merefleksikan generalisasi dunia nyata yang sebenarnya (*true out-of-subject generalization*).

### Ringkasan Kinerja 28 Konfigurasi Model (Held-Out Test Set)

Berikut adalah ringkasan hasil evaluasi 28 model benchmark terurut berdasarkan akurasi klasifikasi:

| Peringkat | Algoritma Klasifikasi | Domain Fitur ViT | Dimensi Fitur | Akurasi Test | Macro F1 | Latensi Inferensi | Waktu Latih |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **1** | **Logistic Regression** | **Tri-Domain (Face + Emotion + Age)** | 2.304-D | **88.66%** | **0.8868** | **0.0046 ms** | 3.287,1 s |
| **2** | **Support Vector Machine (SVC)** | **Tri-Domain (Face + Emotion + Age)** | 2.304-D | **88.61%** | **0.8863** | 4.6785 ms | 30.666,0 s |
| **3** | Support Vector Machine (SVC) | Dual-Domain (Emotion + Face) | 1.536-D | 88.43% | 0.8844 | 0.9490 ms | 18.576,1 s |
| **4** | Support Vector Machine (SVC) | Dual-Domain (Face + Age) | 1.536-D | 87.55% | 0.8757 | 2.5468 ms | 29.541,1 s |
| **5** | Logistic Regression | Dual-Domain (Emotion + Face) | 1.536-D | 87.45% | 0.8749 | 0.0035 ms | 1.941,2 s |
| **6** | Logistic Regression | Dual-Domain (Face + Age) | 1.536-D | 87.41% | 0.8740 | 0.0056 ms | 1.825,3 s |
| **7** | Logistic Regression | Dual-Domain (Emotion + Age) | 1.536-D | 86.67% | 0.8667 | 0.0035 ms | 1.796,6 s |
| **8** | Logistic Regression | Single-Domain (Face) | 768-D | 86.39% | 0.8640 | 0.0008 ms | 833,9 s |
| **9** | Support Vector Machine (SVC) | Dual-Domain (Emotion + Age) | 1.536-D | 86.25% | 0.8624 | 3.7228 ms | 24.482,4 s |
| **10** | Support Vector Machine (SVC) | Single-Domain (Face) | 768-D | 86.16% | 0.8619 | 0.3638 ms | 9.997,4 s |
| ... | *18 Konfigurasi Lainnya (GNB, RF, LR, SVM)* | *Single / Dual / Tri* | *50-250 PC* | 67.08% - 85.79% | 0.6686 - 0.8580 | 0.0024 - 0.0334 ms | 548,6 s - 15.207,0 s |

> [!TIP]
> **Efisiensi Inferensi Pareto:** Walaupun SVM Tri-Domain dan Logistic Regression Tri-Domain memiliki performa akurasi yang sebanding (~88.6%, perbedaan tidak signifikan secara statistik via uji McNemar $p = 1.0$), **Logistic Regression Tri-Domain unggul telak dalam efisiensi komputasi** dengan latensi inferensi **~1.000× lebih cepat** (0.0046 ms vs 4.6785 ms per sampel) dan ukuran model yang jauh lebih kompak (0.11 MB vs 36.6 MB).

---

## Protokol Partisi Data & Pembuktian 0% Kebocoran

Dataset **DemogPairs** terdiri dari 10.800 citra wajah dengan resolusi terstandarisasi yang mencakup 6 kelas interseksional ras dan gender:
1. `Asian_Females` (1.800 citra / 100 subjek)
2. `Asian_Males` (1.800 citra / 100 subjek)
3. `Black_Females` (1.800 citra / 100 subjek)
4. `Black_Males` (1.800 citra / 100 subjek)
5. `White_Females` (1.800 citra / 100 subjek)
6. `White_Males` (1.800 citra / 100 subjek)

Total terdapat **600 identitas subjek unik**, di mana masing-masing subjek memiliki tepat 18 variasi citra wajah (pose, ekspresi, kondisi pencahayaan).

```
DemogPairs (10.800 Citra / 600 Subjek Unik)
│
├── Data Latih (Train Set: 80% Subjek)
│   ├── 480 Subjek Unik (80 subjek per kelas)
│   ├── 8.640 Citra (1.440 citra per kelas)
│   └── Validasi Internal: 5-Fold StratifiedGroupKFold (dikelompokkan per subject_id)
│
└── Data Uji Independen (Held-Out Test Set: 20% Subjek)
    ├── 120 Subjek Unik (20 subjek per kelas)
    ├── 2.160 Citra (360 citra per kelas)
    └── 0.00% Overlap Identitas (Zero-Leakage Guarantee)
```

Fungsi partisi [`split_demogpairs_subject_disjoint`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/utils/dataset.py#L36-L78) pada modul `utils/dataset.py` menjamin bahwa pembagian indeks dilakukan pada tingkat `subject_id`, bukan tingkat baris citra acak:

```python
# Ekstrak identitas subjek unik dan partisi tanpa tumpang tindih
train_idx, test_idx = u.split_demogpairs_subject_disjoint(
    data, 
    train_ratio=0.8, 
    random_state=42
)
```

> [!NOTE]
> Perbandingan mendalam antara partisi *Subject-Disjoint* ini dengan partisi *Subject-Overlap* terdahulu didokumentasikan di folder [`archive/`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/archive/README.md), di mana kebocoran 100% pada versi terdahulu memicu akurasi semu 93.70% (turun wajar menjadi 88.66% pada generalisasi out-of-subject riil).

---

## Ikhtisar 33 Notebook Eksperimen Aktif

Lingkungan `experiment/code/` mengelola **33 berkas Jupyter Notebook aktif** yang dirancang dengan alur komputasi modular, deterministik, dan dapat direproduksi secara mandiri.

```
experiment/code/
├── 1.1_vit-*.ipynb                   [3 Notebook Ekstraksi Fitur Laten]
├── 2.x.x_*_demogpairs.ipynb          [28 Notebook Klasifikasi & Tuning]
└── 3.x_*.ipynb                       [2 Notebook Komparasi & Signifikansi]
```

### 1. Notebook Ekstraksi Fitur Laten ViT (3 Berkas)

Notebook ekstraksi memproses seluruh 10.800 citra DemogPairs melalui model *foundation* Vision Transformer dari Hugging Face untuk mengekstrak vektor representasi laten token `[CLS]` 768 dimensi:

| File Notebook | Model Hugging Face | Domain Representasi | Dimensi Vektor | Berkas Cache Keluaran |
| :--- | :--- | :--- | :---: | :--- |
| [`1.1_vit-face_demogpairs.ipynb`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/1.1_vit-face_demogpairs.ipynb) | `skutaada/VIT-VGGFace` | Ciri Biometrik / Identitas Wajah | 768-D | `features/demogpairs_vit-face.pkl` (~30.8 MB) |
| [`1.1_vit-emotion_demogpairs.ipynb`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/1.1_vit-emotion_demogpairs.ipynb) | `dima806/facial_emotions_image_detection` | Morfologi Otot / Ekspresi Wajah | 768-D | `features/demogpairs_vit-emotion.pkl` (~30.8 MB) |
| [`1.1_vit-age_demogpairs.ipynb`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/1.1_vit-age_demogpairs.ipynb) | `dima806/facial_age_image_detection` | Tekstur Penuaan Wajah | 768-D | `features/demogpairs_vit-age.pkl` (~30.8 MB) |

### 2. Notebook Klasifikasi & Tuning Hiperparameter (28 Berkas)

Sebanyak 28 notebook mengimplementasikan 7 skema kombinasi domain fitur (3 *single-domain*, 3 *dual-domain*, 1 *tri-domain*) yang disilangkan dengan 4 keluarga pengklasifikasi:

```
4 Algoritma × 7 Konfigurasi Fitur = 28 Konfigurasi Model
```

#### Matriks Pemetaan 28 Notebook Klasifikasi

| No | File Notebook Klasifikasi | Algoritma | Konfigurasi Domain Fitur | Dimensi Asal | Komponen PCA ($k$) |
| :---: | :--- | :---: | :--- | :---: | :---: |
| 1 | [`2.1.1_svm_vit-face_demogpairs.ipynb`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/2.1.1_svm_vit-face_demogpairs.ipynb) | SVM | Single: Face | 768-D | [50, 100, 150, 200, 250] |
| 2 | [`2.1.2_svm_vit-emotion_demogpairs.ipynb`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/2.1.2_svm_vit-emotion_demogpairs.ipynb) | SVM | Single: Emotion | 768-D | [50, 100, 150, 200, 250] |
| 3 | [`2.1.3_svm_vit-age_demogpairs.ipynb`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/2.1.3_svm_vit-age_demogpairs.ipynb) | SVM | Single: Age | 768-D | [50, 100, 150, 200, 250] |
| 4 | [`2.1.4_svm_vit-face-age_demogpairs.ipynb`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/2.1.4_svm_vit-face-age_demogpairs.ipynb) | SVM | Dual: Face + Age | 1.536-D | [50, 100, 150, 200, 250] |
| 5 | [`2.1.5_svm_vit-emotion-age_demogpairs.ipynb`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/2.1.5_svm_vit-emotion-age_demogpairs.ipynb) | SVM | Dual: Emotion + Age | 1.536-D | [50, 100, 150, 200, 250] |
| 6 | [`2.1.6_svm_vit-emotion-face_demogpairs.ipynb`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/2.1.6_svm_vit-emotion-face_demogpairs.ipynb) | SVM | Dual: Emotion + Face | 1.536-D | [50, 100, 150, 200, 250] |
| 7 | [`2.1.7_svm_vit-face-emotion-age_demogpairs.ipynb`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/2.1.7_svm_vit-face-emotion-age_demogpairs.ipynb) | SVM | Tri: Face + Emotion + Age | 2.304-D | [50, 100, 150, 200, 250] |
| 8 | [`2.2.1_gnb_vit-face_demogpairs.ipynb`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/2.2.1_gnb_vit-face_demogpairs.ipynb) | GNB | Single: Face | 768-D | [50, 100, 150, 200, 250] |
| 9 | [`2.2.2_gnb_vit-emotion_demogpairs.ipynb`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/2.2.2_gnb_vit-emotion_demogpairs.ipynb) | GNB | Single: Emotion | 768-D | [50, 100, 150, 200, 250] |
| 10 | [`2.2.3_gnb_vit-age_demogpairs.ipynb`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/2.2.3_gnb_vit-age_demogpairs.ipynb) | GNB | Single: Age | 768-D | [50, 100, 150, 200, 250] |
| 11 | [`2.2.4_gnb_vit-face-age_demogpairs.ipynb`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/2.2.4_gnb_vit-face-age_demogpairs.ipynb) | GNB | Dual: Face + Age | 1.536-D | [50, 100, 150, 200, 250] |
| 12 | [`2.2.5_gnb_vit-emotion-age_demogpairs.ipynb`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/2.2.5_gnb_vit-emotion-age_demogpairs.ipynb) | GNB | Dual: Emotion + Age | 1.536-D | [50, 100, 150, 200, 250] |
| 13 | [`2.2.6_gnb_vit-emotion-face_demogpairs.ipynb`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/2.2.6_gnb_vit-emotion-face_demogpairs.ipynb) | GNB | Dual: Emotion + Face | 1.536-D | [50, 100, 150, 200, 250] |
| 14 | [`2.2.7_gnb_vit-face-emotion-age_demogpairs.ipynb`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/2.2.7_gnb_vit-face-emotion-age_demogpairs.ipynb) | GNB | Tri: Face + Emotion + Age | 2.304-D | [50, 100, 150, 200, 250] |
| 15 | [`2.4.1_rf_vit-face_demogpairs.ipynb`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/2.4.1_rf_vit-face_demogpairs.ipynb) | RF | Single: Face | 768-D | [50, 100, 150, 200, 250] |
| 16 | [`2.4.2_rf_vit-emotion_demogpairs.ipynb`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/2.4.2_rf_vit-emotion_demogpairs.ipynb) | RF | Single: Emotion | 768-D | [50, 100, 150, 200, 250] |
| 17 | [`2.4.3_rf_vit-age_demogpairs.ipynb`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/2.4.3_rf_vit-age_demogpairs.ipynb) | RF | Single: Age | 768-D | [50, 100, 150, 200, 250] |
| 18 | [`2.4.4_rf_vit-face-age_demogpairs.ipynb`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/2.4.4_rf_vit-face-age_demogpairs.ipynb) | RF | Dual: Face + Age | 1.536-D | [50, 100, 150, 200, 250] |
| 19 | [`2.4.5_rf_vit-emotion-age_demogpairs.ipynb`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/2.4.5_rf_vit-emotion-age_demogpairs.ipynb) | RF | Dual: Emotion + Age | 1.536-D | [50, 100, 150, 200, 250] |
| 20 | [`2.4.6_rf_vit-emotion-face_demogpairs.ipynb`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/2.4.6_rf_vit-emotion-face_demogpairs.ipynb) | RF | Dual: Emotion + Face | 1.536-D | [50, 100, 150, 200, 250] |
| 21 | [`2.4.7_rf_vit-face-emotion-age_demogpairs.ipynb`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/2.4.7_rf_vit-face-emotion-age_demogpairs.ipynb) | RF | Tri: Face + Emotion + Age | 2.304-D | [50, 100, 150, 200, 250] |
| 22 | [`2.5.1_lr_vit-face_demogpairs.ipynb`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/2.5.1_lr_vit-face_demogpairs.ipynb) | LR | Single: Face | 768-D | [50, 100, 150, 200, 250] |
| 23 | [`2.5.2_lr_vit-emotion_demogpairs.ipynb`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/2.5.2_lr_vit-emotion_demogpairs.ipynb) | LR | Single: Emotion | 768-D | [50, 100, 150, 200, 250] |
| 24 | [`2.5.3_lr_vit-age_demogpairs.ipynb`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/2.5.3_lr_vit-age_demogpairs.ipynb) | LR | Single: Age | 768-D | [50, 100, 150, 200, 250] |
| 25 | [`2.5.4_lr_vit-face-age_demogpairs.ipynb`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/2.5.4_lr_vit-face-age_demogpairs.ipynb) | LR | Dual: Face + Age | 1.536-D | [50, 100, 150, 200, 250] |
| 26 | [`2.5.5_lr_vit-emotion-age_demogpairs.ipynb`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/2.5.5_lr_vit-emotion-age_demogpairs.ipynb) | LR | Dual: Emotion + Age | 1.536-D | [50, 100, 150, 200, 250] |
| 27 | [`2.5.6_lr_vit-emotion-face_demogpairs.ipynb`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/2.5.6_lr_vit-emotion-face_demogpairs.ipynb) | LR | Dual: Emotion + Face | 1.536-D | [50, 100, 150, 200, 250] |
| 28 | [`2.5.7_lr_vit-face-emotion-age_demogpairs.ipynb`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/2.5.7_lr_vit-face-emotion-age_demogpairs.ipynb) | LR | Tri: Face + Emotion + Age | 2.304-D | [50, 100, 150, 200, 250] |

---

### Standardisasi Arsitektur Tepat 16 Sel Notebook

Seluruh 28 notebook klasifikasi dibangun dengan arsitektur standar **tepat 16 sel seragam** guna menjamin konsistensi eksekusi, kemudahan *debugging*, dan keandalan serialisasi otomatis:

```
[Cell 1: Markdown]  Judul & Metadata Eksperimen
[Cell 2: Code]      Inisialisasi Pustaka & Joblib Threading Backend
[Cell 3: Markdown]  Section Header: ## Load Dataset
[Cell 4: Code]      Pemuatan Metadata DemogPairs (u.load_demogpairs)
[Cell 5: Markdown]  Section Header: ## Load Fitur
[Cell 6: Code]      Pemuatan Cache Embedding (.pkl) & Konkatenasi Laten
[Cell 7: Markdown]  Section Header: ## Split Data
[Cell 8: Code]      Partisi Subject-Disjoint (u.split_demogpairs_subject_disjoint)
[Cell 9: Markdown]  Section Header: ## Kombinasi Parameter
[Cell 10: Code]     Definisi Pipeline PCA + Estimator & Ruang Hiperparameter GridSearchCV
[Cell 11: Markdown] Section Header: ## Klasifikasi
[Cell 12: Code]     Eksekusi GridSearchCV 5-Fold StratifiedGroupKFold (u.evaluate_models)
[Cell 13: Code]     Pemeriksaan Best Estimator & Muat Model Terpilih (models/clf_*.pkl)
[Cell 14: Code]     Visualisasi Durasi Waktu Pelatihan & Latensi Inferensi
[Cell 15: Code]     Tabel Metrik Klasifikasi Per-Kelas (Precision, Recall, F1, OvR Acc)
[Cell 16: Code]     Plotting Matriks Konfusi (Confusion Matrix) & Ekspor ke images/
```

---

### 3. Notebook Analisis Komparatif & Signifikansi Statistik (2 Berkas)

Kedua notebook ini mengonsolidasikan dan menguji seluruh hasil mentah dari ke-28 konfigurasi model:

* **[`3.0_compare.ipynb`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/3.0_compare.ipynb)** (19 Sel):
  - Memuat seluruh 28 berkas JSON hasil evaluasi dari direktori `results/`.
  - Menyusun tabel komparatif menyeluruh (Akurasi, Macro F1, Precision, Recall, Latensi, Ukuran Model).
  - Melakukan analisis ablasi fusi domain (*Single vs Dual vs Tri-Domain*).
  - Membangkitkan visualisasi kurva *trade-off* akurasi versus latensi inferensi ([`images/compare_accuracy_and_latency.png`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/images/compare_accuracy_and_latency.png)).

* **[`3.1_statistical_significance.ipynb`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/3.1_statistical_significance.ipynb)** (18 Sel):
  - **Uji McNemar Berpasangan (*Paired McNemar's Test*)**: Menghitung statistik $\chi^2$ dengan koreksi kontinuitas Edwards dan *Exact Two-Sided Binomial Test* untuk menguji signifikansi perbedaan performa antar-skema fusi dan antar-klasifier.
  - **Wilson Score 95% Confidence Interval (CI)**: Menghitung selang kepercayaan akurasi yang ketat dan bebas bias asimetris untuk seluruh 28 model benchmark.
  - **Audit Keadilan Algoritmik (*Intersectional Fairness Audit*)**: Menghitung *Equal Opportunity Difference* dan kesenjangan akurasi antar 6 subkelompok demografis.
  - **Pembuktian Kejenuhan Representasi (*Feature Saturation*)**: Memvisualisasikan batas ketidakpastian 95% CI ([`images/wilson_ci_top15.png`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/images/wilson_ci_top15.png)) untuk membuktikan secara empiris mengapa skema fusi *Dual-Domain* (`vit-emotion-face`) merupakan konfigurasi optimal sebelum kejenuhan representasi tri-domain terjadi.

---

## Peta Struktur Subfolder & Modul Kode

Struktur hierarki direktori pada `experiment/code/` dirancang dengan separasi peran yang terisolasi:

```
experiment/code/
│
├── 1.1_*.ipynb                      # 3 Notebook Ekstraksi Fitur ViT
├── 2.*.ipynb                        # 28 Notebook Klasifikasi & Tuning
├── 3.*.ipynb                        # 2 Notebook Komparasi & Signifikansi
├── app.py                           # Aplikasi Demo Web Interaktif (Gradio)
│
├── utils/                           # Pustaka Modular Inti Python
│   ├── __init__.py                  # P-Core affinity lock & eksposur fungsi
│   ├── constants.py                 # Mapping label kelas DemogPairs
│   ├── dataset.py                   # Ingesti metadata & partisi subject-disjoint
│   ├── display.py                   # Helper rendering notebook & CLI
│   ├── evaluation.py                # Evaluasi GridSearchCV, metrik, & CM
│   ├── extraction.py               # Ekstraksi token [CLS] ViT (Hugging Face)
│   ├── serialization.py             # Serialisasi joblib & JSON terkompresi
│   └── time_helpers.py              # Konversi detik ke format human-readable
│
├── dataset/                         # Dataset DemogPairs
│   └── demogpairs/
│       ├── images/                  # Direktori citra wajah per subjek
│       └── metadata/                # 6 file teks metadata interseksional
│
├── features/                        # Cache Embedding Representasi Laten (.pkl)
│   ├── demogpairs_vit-face.pkl      # 10.800 × 768-D Face Embeddings
│   ├── demogpairs_vit-emotion.pkl   # 10.800 × 768-D Emotion Embeddings
│   └── demogpairs_vit-age.pkl       # 10.800 × 768-D Age Embeddings
│
├── models/                          # Bobot Model Terlatih (28 file .pkl)
│   ├── clf_demogpairs_svm_*.pkl     # 7 Model Support Vector Machine
│   ├── clf_demogpairs_lr_*.pkl      # 7 Model Logistic Regression
│   ├── clf_demogpairs_rf_*.pkl      # 7 Model Random Forest
│   └── clf_demogpairs_gnb_*.pkl     # 7 Model Gaussian Naive Bayes
│
├── results/                         # Berkas Metrik Mentah JSON (28 file .json)
│   ├── demogpairs_svm_*.json        # Log metrik, prediksi y_pred, y_test
│   ├── demogpairs_lr_*.json         # Log metrik Logistic Regression
│   ├── demogpairs_rf_*.json         # Log metrik Random Forest
│   ├── demogpairs_gnb_*.json        # Log metrik Gaussian Naive Bayes
│   └── *_execution_log.txt          # Log pemantauan eksekusi runner background
│
├── images/                          # Visualisasi Metrik & Plot Publikasi
│   ├── cm_*.png                     # 28 Confusion Matrix heatmaps
│   ├── compare_accuracy_and_latency.png # Grafik komparasi performa vs latensi
│   └── wilson_ci_top15.png          # Plot forest selang kepercayaan Wilson 95%
│
├── md/                              # Ekspor Statis Markdown dari 33 Notebook
│   ├── svm/                         # Ekspor markdown 7 notebook SVM
│   ├── lr/                          # Ekspor markdown 7 notebook LR
│   ├── rf/                          # Ekspor markdown 7 notebook RF
│   ├── gnb/                         # Ekspor markdown 7 notebook GNB
│   ├── 1.1_*.md                     # Ekspor markdown 3 notebook ekstraksi
│   ├── 3.0_compare.md               # Ekspor markdown analisis komparasi
│   └── 3.1_statistical_significance.md # Ekspor markdown signifikansi statistik
│
├── scripts/                         # Orkestrator Eksekusi Otomatis Headless
│   ├── auto_run_experiments.py      # Runner antrean utama 28 notebook
│   ├── run_remaining_queue.py       # Runner antrean SVM komputasi berat
│   ├── run_gnb_queue.py             # Runner antrean cepat GNB
│   ├── run_experiments.bat          # Batch script aktivasi cepat Windows
│   ├── run_gnb.bat                  # Batch script GNB Windows
│   └── README.md                    # Dokumentasi teknis skrip otomatisasi
│
└── archive/                         # Arsip Eksperimen Historis (Subject-Overlap)
    ├── notebook_old/                # 35 Notebook lama (100% data leakage)
    ├── results_old/                 # 28 JSON metrik held-out versi lama
    ├── models_old/                  # 28 Bobot model terlatih versi lama
    ├── md_old/                      # Ekspor markdown lama
    ├── audit_ledger.json            # Matriks audit kebocoran data komparatif
    └── README.md                    # Dokumentasi metodologi komparasi arsip
```

---

### Pustaka Modular Python (`utils/`)

Seluruh logika inti komputasi dienkapsulasi dalam paket modular `utils` untuk mencegah duplikasi kode:

1. **`constants.py`**: Mendefinisikan konstanta nama kelas demografis (`DEMOGPairs_CLASSES`) dan kamus pemetaan dua arah antara label teks dengan indeks numerik (`DEMOGPairs_LABEL_TO_IDX`, `DEMOGPairs_IDX_TO_LABEL`).
2. **`dataset.py`**:
   - `load_demogpairs()`: Membaca metadata dari `dataset/demogpairs/metadata/*.txt`, memetakan path lengkap citra, dan mengekstrak ID folder subjek (`subject_id`).
   - `split_demogpairs_subject_disjoint()`: Menjalankan algoritma pemisahan subjek secara deterministik berbasis `random_state=42`, memastikan rasio 80/20 di setiap kelas tanpa ada subjek uji yang bocor ke data latih.
3. **`extraction.py`**:
   - `extract_vit_features()`: Menginisialisasi `AutoImageProcessor` dan `AutoModelForImageClassification` dari Hugging Face, mengubah citra ke tensor RGB, mengeksekusi inferensi pada kartu grafis CUDA tanpa gradien (`torch.no_grad()`), dan mengekstrak representasi laten token `[CLS]` (vektor 768 dimensi).
4. **`evaluation.py`**:
   - `evaluate_models()`: Mesin evaluasi utama. Menerima kamus estimator `GridSearchCV`, memeriksa apakah bobot model terlatih sudah ada di disk (`models/clf_*.pkl`), memuat model instan jika ditemukan, atau melatih model jika belum ada. Menghitung metrik klasifikasi multi-kelas, profil waktu inferensi per sampel, menyimpan hasil ke `results/*.json`, dan mengekspor visualisasi matriks konfusi ke `images/*.png`.
5. **`serialization.py`**:
   - `save_object()` & `load_object()`: Serialisasi objek Python kompleks (termasuk pipeline Scikit-Learn yang berisi estimator dan transformator PCA) menggunakan `joblib` dengan kompresi tingkat 9.
   - `save_json()` & `load_json()`: Serialisasi kamus metrik ke format JSON terstruktur dengan indentasi rapi.
6. **`display.py`**: Menyediakan abstraksi visual cerdas (`printhtml`, `h`, `display_table`) yang mampu mendeteksi lingkungan eksekusi secara dinamis (merender antarmuka HTML interaktif jika berada di Jupyter Notebook, atau teks polos terformat jika dieksekusi via CLI terminal).
7. **`time_helpers.py`**: Mengonversi durasi waktu dalam satuan detik ke format rincian hari, jam, menit, dan detik yang mudah dipahami manusia.
8. **`__init__.py`**: Mengotomatisasi pemanggilan fungsi `optimize_cpu_affinity(p_core_threads=12)` pada sistem operasi Windows setiap kali `utils` diimpor, mengunci thread eksekusi ke inti performa (*P-cores*) dan menaikkan prioritas proses untuk mengeliminasi pembatasan daya *EcoQoS*.

---

## Panduan Eksekusi & Alur Kerja

Terdapat tiga cara utama untuk berinteraksi dan mengeksekusi eksperimen ini:

### Opsi A: Evaluasi Cepat via Model Terlatih (Bypass Fit Ulang)

Seluruh 28 model hasil tuning telah dilatih dan disimpan di dalam folder `models/`. Jika Anda membuka salah satu dari 28 notebook klasifikasi (misalnya [`2.1.7_svm_vit-face-emotion-age_demogpairs.ipynb`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/2.1.7_svm_vit-face-emotion-age_demogpairs.ipynb)), fungsi `u.evaluate_models` secara otomatis mendeteksi keberadaan berkas model `.pkl`:

```python
# Cell 12 pada notebook klasifikasi
evaluation_results, fold_results = u.evaluate_models(
    grid_models,
    x_train, y_train,
    x_test, y_test,
    model_prefix="models/clf_demogpairs_svm_vit-face-emotion-age_",
    target_names=target_names,
    results_path="results/demogpairs_svm_vit-face-emotion-age_",
    groups_train=groups_train,
    groups_test=groups_test,
)
```

> [!NOTE]
> Karena berkas `models/clf_demogpairs_svm_vit-face-emotion-age_SVC.pkl` telah tersedia di disk, fungsi di atas akan **melewati proses fit ulang 5-fold cross-validation** yang memakan waktu ~8,5 jam, memuat model terlatih dalam **< 1 detik**, dan langsung menghitung seluruh metrik inferensi held-out test set secara akurat.

---

### Opsi B: Eksekusi Batch Otomatis (Headless Runner)

Untuk menjalankan kembali seluruh atau sebagian antrean notebook secara berurutan di latar belakang (*headless execution*) tanpa perlu membuka antarmuka grafis Jupyter satu per satu:

1. **Menggunakan Skrip Otomatisasi Python:**
   ```bash
   # Pastikan lingkungan conda torch-gpu telah aktif
   conda activate torch-gpu
   cd experiment/code

   # Jalankan runner antrean eksperimen
   python scripts/auto_run_experiments.py
   ```

2. **Menggunakan Skrip Batch Windows (Satu Klik):**
   Cukup klik ganda pada berkas [`scripts/run_experiments.bat`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/scripts/run_experiments.bat) atau jalankan dari terminal Windows:
   ```cmd
   scripts\run_experiments.bat
   ```

Skrip ini dilengkapi mekanisme *checkpointing*: jika suatu model sudah memiliki berkas hasil JSON di direktori `results/`, runner akan melewatinya secara otomatis dan melanjutkan ke antrean berikutnya.

---

### Opsi C: Aplikasi Demo Web Interaktif (Gradio)

Untuk mendemonstrasikan kemampuan inferensi model secara langsung menggunakan antarmuka grafis web interaktif:

```bash
conda activate torch-gpu
cd experiment/code
python app.py
```

Setelah aplikasi berjalan, buka peramban web pada alamat lokal:
```
http://127.0.0.1:7860
```

Pengguna dapat mengunggah sembarang citra wajah manusia (format JPG/PNG). Antarmuka akan mengekstraksi representasi laten melalui dua model Vision Transformer (`skutaada/VIT-VGGFace` dan `dima806/facial_emotions_image_detection`), menggabungkan fiturnya (1.536-D), dan memprediksi kelas interseksional ras dan gender menggunakan model Support Vector Machine secara instan beserta probabilitas distribusinya.

---

## Lingkungan Komputasi & Reprodusibilitas

Eksperimen ini dirancang dengan standar reproduktifitas penuh. Seluruh pembagian data, inisialisasi bobot komponen PCA, dan algoritma klasifikasi dikunci menggunakan benih acak seragam (`random_state = 42`).

### 1. Spesifikasi Perangkat Keras (Hardware)

Eksperimen dan pencatatan latensi inferensi dilakukan pada stasiun kerja komputasi dengan konfigurasi berikut:

* **Unit Pemroses Grafis (GPU):** NVIDIA GeForce RTX 4060 Laptop GPU (8 GB GDDR6 VRAM, Driver Version 560.94, CUDA 12.6)
* **Unit Pemroses Sentral (CPU):** Intel® Core™ i9-13900H (14 Cores / 20 Threads: 6 *Performance-cores* hingga 5,4 GHz dengan Hyper-Threading, 8 *Efficient-cores* hingga 4,1 GHz)
* **Memori Utama (RAM):** 32 GB DDR5 5200 MHz Dual-Channel
* **Penyimpanan:** NVMe PCIe Gen 4 SSD (Kecepatan Baca/Tulis > 5.000 MB/s)
* **Sistem Operasi:** Microsoft Windows 11 Home 64-bit

---

### 2. Konfigurasi Lingkungan Software (Conda Environment)

Eksperimen berjalan di atas lingkungan conda terisolasi bernama `torch-gpu`. Paket-paket utama beserta versinya adalah sebagai berikut:

```yaml
name: torch-gpu
channels:
  - pytorch
  - nvidia
  - conda-forge
  - defaults
dependencies:
  - python = 3.10
  - pytorch = 2.10.0+cu126
  - torchvision = 0.21.0+cu126
  - torchaudio = 2.10.0+cu126
  - cudatoolkit = 12.6
  - transformers = 5.7.0
  - scikit-learn = 1.8.0
  - imbalanced-learn = 0.12.0
  - pandas = 2.2.0
  - numpy = 1.26.4
  - matplotlib = 3.8.3
  - seaborn = 0.13.2
  - joblib = 1.3.2
  - tqdm = 4.66.2
  - gradio = 4.19.0
  - pillow = 10.2.0
```

Untuk mereplikasi lingkungan conda dari awal:
```bash
conda create -n torch-gpu python=3.10 -y
conda activate torch-gpu
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu126
pip install transformers scikit-learn imbalanced-learn pandas numpy matplotlib seaborn joblib tqdm gradio pillow
```

---

### 3. Optimasi Intel Hybrid P-Core Thread Affinity

Pada sistem operasi Windows modern dengan prosesor arsitektur Intel Hybrid (kombinasi P-Core dan E-Core), pustaka `joblib` dan `scikit-learn` kerap mengalami penurunan kecepatan drastis ketika beban komputasi multi-threading dialihkan secara agresif oleh Windows Scheduler ke *Efficient-cores* (status daya rendah *EcoQoS*).

Untuk mengatasi kendala ini, modul [`utils/__init__.py`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/utils/__init__.py#L15-L49) menyertakan optimasi tingkat kernel Windows API via `ctypes`:

```python
# utils/__init__.py: Mengunci proses ke 12 logical threads P-Cores
optimize_cpu_affinity(p_core_threads=12, verbose=False)
```

1. **`SetProcessAffinityMask(handle, 0x0FFF)`**: Mengunci thread komputasi Scikit-Learn dan PyTorch hanya pada thread 0 sampai 11 (6 Performance Cores berkecepatan tinggi).
2. **`SetPriorityClass(handle, ABOVE_NORMAL_PRIORITY_CLASS)`**: Menaikkan kelas prioritas proses menjadi `0x00008000` (*Above Normal*) guna mencegah sistem operasi menurunkan suplai daya saat eksperimen berjalan berjam-jam di latar belakang.

---

> [!NOTE]
> Jika Anda memiliki pertanyaan metodologi atau membutuhkan verifikasi metrik lebih lanjut, silakan merujuk pada berkas analisis inferensial di [`3.1_statistical_significance.ipynb`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/3.1_statistical_significance.ipynb) atau periksa dokumentasi audit kebocoran data di [`archive/README.md`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/archive/README.md).
