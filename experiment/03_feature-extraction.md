# Ekstraksi Fitur Multi-Domain Vision Transformer & Feature Fusion

## Ringkasan

Penelitian menerapkan strategi ekstraksi fitur **offline (one-pass)**: seluruh 10.800 citra wajah DemogPairs dilewatkan tepat satu kali melalui tiga model Vision Transformer (ViT-Base) pra-latih yang berspesialisasi pada domain saling melengkapi. Vektor representasi 768 dimensi diekstraksi langsung dari token khusus `[CLS]` (*Classification Token*), disimpan sebagai arsip terkompresi (`joblib`), dan dipakai ulang di seluruh rangkaian eksperimen.

Sesuai arahan penelaahan **IEEE Access Reviewer 2 (Comment #2 & #3)**, ekstraksi fitur ini menjamin **paritas fitur absolut (*absolute feature parity*)**: arsip fitur yang sama persis digunakan untuk kedua protokol evaluasi (**Subject-Disjoint** bebas kebocoran dan **Subject-Overlap** tolok ukur historis). Hal ini memastikan bahwa seluruh disparitas kinerja antar-protokol murni diakibatkan oleh kemampuan generalisasi model terhadap identitas subjek baru (*unseen subjects*), bukan variasi representasi fitur.

| Aspek Teknis | Spesifikasi Ekstraksi | Keterangan Metodologis |
|---|---|---|
| **Backbone Ekstraktor** | 3 Arsitektur ViT-Base (`patch16-224`, 12 layer, 12 attention heads) | Pra-latih pada tugas spesifik domain |
| **Output per Ekstraktor** | Vektor 768 dimensi, `float32` | Diambil dari token khusus `[CLS]` |
| **Penyimpanan Fitur** | `features/demogpairs_vit-{face,emotion,age}.pkl` | ≈30 MB per berkas (kompresi `joblib` level 9) |
| **Dimensi Gabungan** | **768-D** (Single), **1.536-D** (Dual), **2.304-D** (Tri-Domain) | Concatenation vektor fitur secara langsung |
| **Konfigurasi Fitur** | **7 varian** (3 Single-Domain + 3 Dual-Domain + 1 Tri-Domain) | Digunakan untuk studi ablasi komparatif |
| **Paritas Fitur** | **100% Identik & Fixed** untuk kedua protokol | Menjamin isolasi variabel yang ketat |

---

## Arsitektur Vision Transformer Base & Formulasi Token `[CLS]`

Ketiga model ekstraktor mengadopsi arsitektur standar Vision Transformer Base (`vit-base-patch16-224`):

1. **Pemotongan Patch & Linear Projection:** Citra input ternormalisasi $\mathbf{x} \in \mathbb{R}^{3 \times 224 \times 224}$ dipotong menjadi $N = 196$ *non-overlapping patches* $\mathbf{x}_p \in \mathbb{R}^{196 \times (16^2 \cdot 3)}$, kemudian diproyeksikan secara linier ke dimensi laten $D = 768$.
2. **Penambahan Token `[CLS]` & Positional Embedding:** Token khusus $\mathbf{x}_{\text{class}} \in \mathbb{R}^{1 \times D}$ diposisikan pada awal urutan patch, diikuti penambahan *1D learnable position embeddings* $\mathbf{E}_{\text{pos}} \in \mathbb{R}^{(N+1) \times D}$:
   $$\mathbf{z}_0 = [\mathbf{x}_{\text{class}}; \, \mathbf{x}_p^1 \mathbf{E}; \, \mathbf{x}_p^2 \mathbf{E}; \, \dots; \, \mathbf{x}_p^N \mathbf{E}] + \mathbf{E}_{\text{pos}}, \quad \mathbf{z}_0 \in \mathbb{R}^{197 \times 768}$$
3. **Transformer Encoder:** Sequence melewati 12 blok Transformer yang terdiri dari *Multi-Head Self-Attention* (MSA) dan *Multi-Layer Perceptron* (MLP) dengan normalisasi *LayerNorm* (LN):
   $$\mathbf{z}'_\ell = \text{MSA}(\text{LN}(\mathbf{z}_{\ell-1})) + \mathbf{z}_{\ell-1}, \quad \ell = 1, \dots, 12$$
   $$\mathbf{z}_\ell = \text{MLP}(\text{LN}(\mathbf{z}'_\ell)) + \mathbf{z}'_\ell, \quad \ell = 1, \dots, 12$$
4. **Ekstraksi Representasi Global:** Vektor representasi pada indeks ke-0 dari lapisan terakhir (`last_hidden_state[:, 0, :]`) diambil sebagai representasi ringkas seluruh citra:
   $$\mathbf{f}_{\text{ViT}} = \mathbf{z}_{12}^0 \in \mathbb{R}^{768}$$

---

## Tiga Ekstraktor Multi-Domain

Ketiga model Vision Transformer dipilih secara cermat untuk menghasilkan representasi fitur yang saling melengkapi (*complementary task-associated representations*):

| Ekstraktor | Checkpoint Hugging Face | Domain Representasi | Karakteristik Fitur yang Ditangkap |
|---|---|---|---|
| **ViT-Face** | `skutaada/VIT-VGGFace` | Geometri Biometrik Wajah | Menangkap struktur kraniofasial, jarak inter-okular, bentuk rahang, dan geometri statis identitas wajah. |
| **ViT-Emotion** | `dima806/facial_emotions_image_detection` | Dinamika Afektif Wajah | Menangkap kontraksi mikro otot wajah, pola ekspresi, serta kurvatur bibir dan alis. |
| **ViT-Age** | `dima806/facial_age_image_detection` | Morfologi Penuaan Wajah | Menangkap tekstur elastisitas kulit, kerutan periorbital, lipatan nasolabial, dan tanda biologis usia. |

Masing-masing ekstraktor menghasilkan berkas arsip fitur `features/demogpairs_vit-{face,emotion,age}.pkl` berukuran ~30 MB yang memetakan `image_path` (string) ke vektor `np.ndarray` berdimensi `(768,)` tipe `float32`.

---

## Pipeline Ekstraksi Fitur Offline

```
Dataset DemogPairs (10.800 Citra)
  │
  ├── Preprocessing Citra: 224×224 Bicubic, RGB, Rescale [0, 1], Standardisasi Channel (AutoImageProcessor)
  │
  ├── Ekstraksi ViT Offline (One-Pass Forward Pass, torch.no_grad()):
  │     ├─ ViT-Face    (skutaada/VIT-VGGFace)                   ──> Token [CLS] ──> demogpairs_vit-face.pkl (768-D)
  │     ├─ ViT-Emotion (dima806/facial_emotions_image_detection) ──> Token [CLS] ──> demogpairs_vit-emotion.pkl (768-D)
  │     └─ ViT-Age     (dima806/facial_age_image_detection)     ──> Token [CLS] ──> demogpairs_vit-age.pkl (768-D)
  │
  ├── Feature Fusion: Penggabungan Vektor (Concatenation) Menghasilkan 7 Skema Fitur
  │
  └── Paritas Fitur Absolut Digunakan Bersama oleh Kedua Protokol Evaluasi:
        ├─ [Protokol Utama Revisi IEEE Access] Subject-Disjoint (0% Leakage)
        └─ [Tolok Ukur Historis Ablasi] Subject-Overlap (100% Leakage)
```

Karena ekstraksi dilakukan secara *offline* sekali untuk seluruh dataset, tahap klasifikasi hilir (*downstream classification*) dapat dieksekusi secara efisien tanpa memerlukan inferensi ViT berulang pada GPU.

---

## Skema Fusi Fitur Multi-Domain (Concatenation)

Fusi fitur dilakukan melalui metode konkatenasi langsung (*direct concatenation*) pada ruang vektor laten tanpa proyeksi linier awal atau operasi rata-rata, menjaga integritas dimensionalitas informasi asli:

$$\mathbf{f}_{\text{Dual}} = [\mathbf{f}_{\text{Domain 1}} \,\|\, \mathbf{f}_{\text{Domain 2}}] \in \mathbb{R}^{1.536}$$
$$\mathbf{f}_{\text{Tri}} = [\mathbf{f}_{\text{Face}} \,\|\, \mathbf{f}_{\text{Emotion}} \,\|\, \mathbf{f}_{\text{Age}}] \in \mathbb{R}^{2.304}$$

Berikut adalah 7 varian skema fusi yang dievaluasi secara sistematis:

| # | Konfigurasi Fitur | Kategori Domain | Dimensi ($D$) | Komposisi Vektor |
|:---:|:---|:---:|:---:|:---|
| 1 | `vit-face` | Single-Domain | 768 | $\mathbf{f}_{\text{Face}}$ murni |
| 2 | `vit-emotion` | Single-Domain | 768 | $\mathbf{f}_{\text{Emotion}}$ murni |
| 3 | `vit-age` | Single-Domain | 768 | $\mathbf{f}_{\text{Age}}$ murni |
| 4 | `vit-face-age` | Dual-Domain | 1.536 | $\mathbf{f}_{\text{Face}} \,\|\, \mathbf{f}_{\text{Age}}$ |
| 5 | `vit-emotion-age` | Dual-Domain | 1.536 | $\mathbf{f}_{\text{Emotion}} \,\|\, \mathbf{f}_{\text{Age}}$ |
| 6 | `vit-emotion-face` | Dual-Domain | 1.536 | $\mathbf{f}_{\text{Emotion}} \,\|\, \mathbf{f}_{\text{Face}}$ |
| 7 | `vit-face-emotion-age` | **Tri-Domain (Usulan Utama)** | **2.304** | $\mathbf{f}_{\text{Face}} \,\|\, \mathbf{f}_{\text{Emotion}} \,\|\, \mathbf{f}_{\text{Age}}$ |

---

## Paritas Fitur Absolut Antara Kedua Protokol Benchmark

Penerapan sistem *dual-benchmark* pada penelitian ini dirancang dengan prinsip kontrol eksperimen yang sangat ketat:

1. **Vektor Fitur Bersifat Statis dan Tak Berubah:** Vektor fitur `[CLS]` 768-D untuk setiap citra dari 10.800 sampel adalah identik dan diambil dari berkas `.pkl` yang sama pada kedua protokol.
2. **Isolasi Variabel Penelitian:** Dengan menjaga ekstraksi fitur dan arsitektur ViT tetap sama persis:
   - Protokol **Subject-Disjoint** mengevaluasi 8.640 sampel latih (480 subjek) dan 2.160 sampel uji (120 subjek independen).
   - Protokol **Subject-Overlap** mengevaluasi 8.640 sampel latih dan 2.160 sampel uji dengan partisi tingkat citra acak (593 subjek uji tumpang tindih).
3. **Pembuktian Hipotesis Kebocoran Data:** Karena fitur yang diumpankan adalah identik, penurunan akurasi puncak dari 93,70% (SVM pada Subject-Overlap) menjadi 88,66% (LR pada Subject-Disjoint) atau 88,61% (SVM pada Subject-Disjoint) membuktikan secara murni dan ilmiah pengaruh *identity leakage* terhadap pembelajaran mesin, sekaligus menjawab tuntas keraguan Reviewer 2 IEEE Access.

---

## Referensi File & Implementasi

- `experiment/code/utils/extraction.py` — Fungsi `extract_vit_features()` (implementasi PyTorch forward pass dan ekstraksi `[CLS]`).
- `experiment/code/features/demogpairs_vit-face.pkl` — Arsip fitur representasi Wajah (768-D).
- `experiment/code/features/demogpairs_vit-emotion.pkl` — Arsip fitur representasi Emosi (768-D).
- `experiment/code/features/demogpairs_vit-age.pkl` — Arsip fitur representasi Usia (768-D).
- `experiment/01_prepare-data.md` — Rincian pembagian data komparatif.
- `experiment/04_methods.md` — Pipeline penskalaan, PCA, dan optimasi GridSearchCV.
- `experiment/05_results.md` — Analisis hasil ablasi fitur dan perbandingan komparatif model.
