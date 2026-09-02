# Framework Penelitian - Multi-Domain ViT + 4 Classifier untuk Klasifikasi Ras & Gender

## Ringkasan

Penelitian mengklasifikasikan **6 kelas interseksional** (3 Ras × 2 Gender: Asian/Black/White × Female/Male) pada citra wajah dengan **Cross-Domain Feature Fusion**. Tiga Vision Transformer sebagai ekstraktor fitur offline:

- **ViT-Face** - 768 dimensi
- **ViT-Emotion** - 768 dimensi
- **ViT-Age** - 768 dimensi

Konkatenasi tri-domain = **2.304 dimensi**. Dataset **DemogPairs** - **10.800 citra** (600 identitas ×18, 1.800 per kelas, seimbang), split **80/20 stratified** (8.640 latih / 2.160 uji, 360 per kelas).

**28 eksperimen** = 7 konfigurasi fitur × 4 classifier - hyperparameter optimization using Grid Search with Cross-Validation (GridSearchCV):

| Classifier | Kombinasi | Tri-domain Akurasi | Macro F1 | Konfigurasi Terbaik (Puncak) |
|:---|:---:|:---:|:---:|:---|
| **Support Vector Classifier (SVC)** | 288 | **93,70%** | **0,9369** | Tri-Domain (`Face ⊕ Emotion ⊕ Age`) |
| **Logistic Regression (LR)** | 270 | **92,73%** | 0,9273 | Tri-Domain (`Face ⊕ Emotion ⊕ Age`) |
| **Random Forest (RF)** | 288 | 86,20% | 0,8613 | Dual-Domain (`Emotion ⊕ Face`: **86,85%** / F1 **0,8682**) |
| **Gaussian Naive Bayes (GNB)** | 240 | **85,05%** | 0,8505 | Tri-Domain (`Face ⊕ Emotion ⊕ Age`) |

---

## Alur Penelitian

```
DemogPairs 10.800 (6×1.800) → Normalisasi citra 224×224 → 3 ViT (Face, Emotion, Age) → fitur 768 dimensi → arsip fitur
  → Fusi fitur 768 / 1.536 / 2.304 dimensi (7 skema) → Split 8640/2160 → Pipeline penskalaan dan reduksi dimensi → Klasifikasi
  → Grid Search with 5-Fold Stratified Cross-Validation (GridSearchCV, 1.086 kombinasi per skema, 38.010 total CV fits) → evaluasi 2.160 uji → metrik global + per kelas + disparitas subkelompok
```

7 skema konfigurasi fitur:
- `vit-face` - 768 dimensi (single-domain)
- `vit-emotion` - 768 dimensi (single-domain)
- `vit-age` - 768 dimensi (single-domain)
- `vit-face-age` - 1.536 dimensi (dual-domain)
- `vit-emotion-age` - 1.536 dimensi (dual-domain)
- `vit-emotion-face` - 1.536 dimensi (dual-domain)
- `vit-face-emotion-age` - 2.304 dimensi (tri-domain, usulan utama)

---

## Arsitektur & Fusi Fitur

- Vision Transformer Base: citra 224×224 → 196 patch 16×16 + 1 token khusus = 197 token, 12 layer.
- Ekstraksi offline: setiap citra menghasilkan vektor 768 dimensi dari token khusus (`[CLS]` token $\mathbf{z}_L^0$), disimpan sebagai arsip fitur task-associated representation.
- Fusi: penggabungan vektor per citra berdasarkan kunci jalur gambar, menghasilkan varian 768, 1.536, dan 2.304 dimensi sesuai skema.

---

## Pipeline Klasifikasi

```
Fitur 768/1.536/2.304 dimensi → Penskalaan → Reduksi dimensi → Klasifikasi → Kelas 0–5
```

Pipeline dirancang untuk mencegah kebocoran data (*information leakage*), di mana penskalaan (MinMaxScaler) dan reduksi dimensi (PCA) hanya dipelajari dari data latih pada setiap fold di dalam pipeline cross-validation. Evaluasi dilakukan dengan 5-Fold Stratified Cross-Validation (total 38.010 model fits + 28 refits) dan evaluasi akhir dilakukan pada subset uji held-out independen ($N=2.160$).

---

## Hasil

- Fusi tri-domain menghasilkan performa tertinggi pada **3 dari 4 classifier** yang dievaluasi: **SVC Tri-Domain (93,70% Akurasi, 0,9369 F1)**, Logistic Regression (92,73% Akurasi, 0,9273 F1), dan Gaussian Naive Bayes (85,05% Akurasi, 0,8505 F1).
- Pada Random Forest, performa puncak dicapai oleh skema dual-domain `Emotion ⊕ Face` (86,85% Akurasi, 0,8682 F1 vs 86,20% pada tri-domain).
- Seluruh 6 subkelompok demografis pada SVC Tri-Domain mencapai F1-Score di atas 0,91 (rentang 0,9174 hingga 0,9614, $\Delta_{\text{F1}} = 0,0440$).
- Papan peringkat lengkap 28 model tersedia pada analisis komparatif (`3.0_compare.md`).

---

## Struktur Dokumen

- `00_overview.md` - ringkasan ini
- `01_prepare-data.md` - dataset & split
- `02_preprocessing.md` - dua tingkat preprocessing
- `03_feature-extraction.md` - ekstraksi ViT & fusi
- `04_methods.md` - empat classifier & optimasi
- `05_results.md` - 28 eksperimen & fairness
- `dataset_demogpairs.md` - spesifikasi DemogPairs
- `code/` - notebook, utilitas, arsip markdown, gambar, dan hasil

---

## Referensi

Hupont & Fernández, *DemogPairs: Quantifying the Impact of Demographic Imbalance in Deep Face Recognition*, FG 2019, DOI `10.1109/FG.2019.8756625`.
