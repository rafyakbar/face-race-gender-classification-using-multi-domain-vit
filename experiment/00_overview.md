# Framework Penelitian — Multi-Domain ViT + 4 Classifier untuk Klasifikasi Ras & Gender

## Ringkasan

Penelitian mengklasifikasikan **6 kelas interseksional** (3 Ras × 2 Gender: Asian/Black/White × Female/Male) pada citra wajah dengan **Cross-Domain Feature Fusion**. Tiga ViT-Base (12 layer, 768-d `[CLS]`) sebagai *feature extractor offline*:

- **ViT-Face** `skutaada/VIT-VGGFace` → 768-d
- **ViT-Emotion** `dima806/facial_emotions_image_detection` → 768-d
- **ViT-Age** `dima806/facial_age_image_detection` → 768-d

Konkatenasi tri-domain = **2.304-d** (`768+768+768`). Dataset **DemogPairs** (Hupont & Fernández FG 2019, DOI `10.1109/FG.2019.8756625`) — **10.800 citra** (600 identitas ×18, 1.800/kelas, seimbang), split **80/20 stratified** (`random_state=42`): **8.640 train / 2.160 test** (360/kelas).

**28 eksperimen** = 7 konfigurasi fitur × 4 classifier (GridSearchCV 5-Fold, `refit='accuracy'`):

| Classifier | Kombinasi | Tri-domain Akurasi | F1 |
|:---|:---:|:---:|:---:|
| **SVM** | 288 | **93,70%** | 0,9369 |
| **Logistic Regression** | 270 | **92,73%** | 0,9273 |
| **Random Forest** | 288 | 86,20% (best dual 86,85%) | 0,8682 |
| **Gaussian NB** | 240 | **85,05%** | 0,8505 |

> RF terbaik dual `vit-emotion-face` (86,85%), tri 86,20%. XGBoost dihapus (butuh CUDA ≥12.9, env 12.6).

---

## Alur Penelitian

```
DemogPairs 10.800 (6×1.800) → AutoImageProcessor 224×224 → 3 ViT [CLS] 768-d → .pkl
  → Fusion 768 / 1.536 / 2.304-d (7 skema) → Split 8640/2160 → Pipeline Scaler/PCA/Classifier
  → GridSearchCV 5-Fold (1.086 kombinasi, 5.430 fits/fitur) → best_params → evaluasi 2.160 test
  → metrik global + OvR per kelas + CM (PNG + text array)
```

7 skema: `vit-face`, `vit-emotion`, `vit-age` (768), `vit-face-age`, `vit-emotion-age`, `vit-emotion-face` (1.536), `vit-face-emotion-age` (2.304, usulan utama).

---

## Arsitektur & Fusi Fitur

- ViT-Base: 224×224 → 196 patch 16×16 + 1 `[CLS]` = 197 token, 12 layer/heads, 768 hidden.
- Ekstraksi offline: `extract_vit_features()` via `model.vit(**inputs)` → `[CLS]` 768-d, `joblib.dump(compress=9)` → `features/demogpairs_vit-*.pkl` (~29 MB).
- Fusi: `np.array(list(face)+list(emotion)+list(age))` per `image_path` (kunci `load_demogpairs()`).

---

## Pipeline Klasifikasi

```
768/1.536/2.304-d → Scaler [None|MinMaxScaler] → PCA [None|0.5|0.75] → Classifier → Kelas 0..5
```
`imblearn.pipeline.Pipeline` (anti-leakage, fit hanya di fold latih), `scoring={accuracy,f1_macro,precision_macro,recall_macro}`, `n_jobs=60%`.

Evaluasi di `utils/evaluation.py`: `labels=[LABEL_TO_IDX[c] for c in CLASSES]` selaras `target_names`, OvR Accuracy `(TP+TN)/N`, CM text array + `images/cm_*.png`.

---

## Hasil & Artefak

- Best: **SVM tri-domain 93,70%** (SVC C=10, poly d2, scale, no PCA/scaler); LR 92,73%, RF 86,85%, GNB 85,05%.
- Leaderboard 28 baris di `code/3.0_compare.ipynb` (populated) & `code/md/3.0_compare.md`.
- Artefak per eksperimen: `models/*.pkl`, `results/*.json`, `images/*.png`; Markdown via `nbconvert` di `code/md/svm|gnb|rf|lr/` (29 file).
- Final test: `code/4.0_test.ipynb` (executed, CUDA).

---

## Struktur Dokumen

- `00_overview.md` — ringkasan ini
- `01_prepare-data.md` — dataset & split
- `02_preprocessing.md` — 2-level preprocessing
- `03_feature-extraction.md` — ViT & fusi
- `04_methods.md` — 4 classifier & GridSearch
- `05_results.md` — 28 eksperimen & fairness
- `dataset_demogpairs.md` — spesifikasi DemogPairs
- `code/` — notebook, `utils/`, `md/`, `images/`, `results/`

---

## Referensi

Hupont & Fernández, *DemogPairs: Quantifying the Impact of Demographic Imbalance in Deep Face Recognition*, FG 2019, DOI `10.1109/FG.2019.8756625`.
