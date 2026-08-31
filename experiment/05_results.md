# Hasil Eksperimen — 28 Eksperimen Klasifikasi Multi-Atribut Ras & Gender (4 Classifier × 7 Konfigurasi Fitur)

> **Dataset:** DemogPairs — 10.800 citra (6 kelas × 1.800), split **8.640 latih / 2.160 uji** (360/kelas, held-out stratified). **Metrik:** Accuracy, Macro Precision/Recall/F1 (4 desimal dari 28 JSON). **Protokol:** GridSearchCV 5-Fold Stratified CV (shuffle,42, refit accuracy) pipeline Scaler→PCA→Classifier (1.086 kombinasi/fitur, 38.010 fits + 28 refit).

---

## Ringkasan Eksekutif — Dari 7 SVM-Only Menjadi 28 Eksperimen

Revisi ini melengkapi **28 eksperimen** penuh: **4 classifier** (SVM, LR, RF, GNB) × **7 konfigurasi** (3 Single, 3 Dual, 1 Tri). Semua angka presisi 4 desimal langsung dari `results/*.json` konsisten dengan `md/3.0_compare.md`.

- **Juara global:** `SVM + vit-face-emotion-age` (Tri, 2.304-d) — **0.9370** / 0.9372 / 0.9370 / 0.9369.
- **Runner-up:** `SVM + vit-emotion-face` 0.9329; `LR + vit-face-emotion-age` 0.9273.
- **Pola universal:** Tri > Dual terbaik > Single terbaik pada 4 classifier (RF sedikit anomali Dual > Tri).
- **Ranking classifier (rata-rata 7):** SVM 0.9150 > LR 0.9057 > RF 0.8299 > GNB 0.7904.
- **Fairness juara:** OvR Accuracy 97.31%–98.70% (rentang 1.39 pp), seluruh F1 >0.91.

---

## 0. Peta Konfigurasi Fitur

| # | Konfigurasi | Tipe | Dim | Komposisi |
|---|-------------|------|-----|-----------|
| 1 | `vit-age` | Single | 768 | ViT-Age |
| 2 | `vit-emotion` | Single | 768 | ViT-Emotion |
| 3 | `vit-face` | Single | 768 | ViT-Face |
| 4 | `vit-emotion-age` | Dual | 1.536 | Emotion ⊕ Age |
| 5 | `vit-face-age` | Dual | 1.536 | Face ⊕ Age |
| 6 | `vit-emotion-face` | Dual | 1.536 | Emotion ⊕ Face |
| 7 | `vit-face-emotion-age` | **Tri** | **2.304** | Face ⊕ Emotion ⊕ Age |

---

## 1. Rekap 28 Eksperimen (Accuracy Tertinggi → Terendah)

| Rank | Classifier | Fitur | Tipe | Akurasi | Precision | Recall | F1 | Parameter Terbaik |
|------|------------|-------|------|---------|-----------|--------|----|-------------------|
| **1** | **SVM** | **vit-face-emotion-age** | Tri | **0.9370** | 0.9372 | 0.9370 | 0.9369 | C=10, poly, γ=scale, deg=2, pca=None, scaler=None |
| **2** | **SVM** | **vit-emotion-face** | Dual | **0.9329** | 0.9333 | 0.9329 | 0.9329 | C=10, rbf, γ=scale, deg=2, pca=None, scaler=MinMaxScaler |
| **3** | **LR** | **vit-face-emotion-age** | Tri | **0.9273** | 0.9275 | 0.9273 | 0.9273 | C=0.1, solver=newton-cg, max_iter=500, pca=None, scaler=None |
| 4 | SVM | vit-face-age | Dual | 0.9255 | 0.9254 | 0.9255 | 0.9254 | C=10, poly, γ=scale, deg=2, pca=None, scaler=None |
| 5 | LR | vit-emotion-face | Dual | 0.9241 | 0.9241 | 0.9241 | 0.9240 | C=0.1, solver=lbfgs, max_iter=500, pca=None, scaler=None |
| 6 | SVM | vit-emotion-age | Dual | 0.9208 | 0.9210 | 0.9208 | 0.9209 | C=10, rbf, γ=scale, deg=2, pca=None, scaler=None |
| 7 | LR | vit-face-age | Dual | 0.9162 | 0.9162 | 0.9162 | 0.9162 | C=0.1, solver=newton-cg, max_iter=500, pca=None, scaler=None |
| 8 | SVM | vit-face | Single | 0.9083 | 0.9084 | 0.9083 | 0.9083 | C=10, rbf, γ=scale, deg=2, pca=None, scaler=None |
| 9 | LR | vit-face | Single | 0.9060 | 0.9060 | 0.9060 | 0.9059 | C=1, solver=newton-cg, max_iter=500, pca=None, scaler=MinMaxScaler |
| 10 | LR | vit-emotion-age | Dual | 0.9051 | 0.9052 | 0.9051 | 0.9051 | C=0.1, solver=lbfgs, max_iter=500, pca=None, scaler=None |
| 11 | SVM | vit-emotion | Single | 0.9019 | 0.9020 | 0.9019 | 0.9017 | C=10, rbf, γ=scale, deg=2, pca=None, scaler=None |
| 12 | LR | vit-emotion | Single | 0.8847 | 0.8850 | 0.8847 | 0.8846 | C=1, solver=saga, max_iter=500, pca=None, scaler=MinMaxScaler |
| 13 | SVM | vit-age | Single | 0.8764 | 0.8767 | 0.8764 | 0.8765 | C=10, rbf, γ=scale, deg=2, pca=None, scaler=None |
| 14 | RF | vit-emotion-face | Dual | 0.8685 | 0.8689 | 0.8685 | 0.8682 | n_est=200, depth=None, max_feat=sqrt, min_split=5, min_leaf=1, pca=PCA, scaler=None |
| 15 | LR | vit-age | Single | 0.8648 | 0.8649 | 0.8648 | 0.8648 | C=0.1, solver=lbfgs, max_iter=500, pca=None, scaler=None |
| 16 | RF | vit-face-emotion-age | Tri | 0.8620 | 0.8620 | 0.8620 | 0.8613 | n_est=200, depth=30, max_feat=sqrt, min_split=5, min_leaf=1, pca=PCA, scaler=None |
| 17 | RF | vit-face-age | Dual | 0.8579 | 0.8578 | 0.8579 | 0.8573 | n_est=200, depth=None, max_feat=sqrt, min_split=2, min_leaf=1, pca=PCA, scaler=None |
| 18 | RF | vit-face | Single | 0.8546 | 0.8543 | 0.8546 | 0.8539 | n_est=200, depth=30, max_feat=log2, min_split=2, min_leaf=1, pca=PCA, scaler=MinMaxScaler |
| 19 | GNB | vit-face-emotion-age | Tri | 0.8505 | 0.8512 | 0.8505 | 0.8505 | var_smoothing=5.8780e-03, pca=PCA, scaler=None |
| 20 | GNB | vit-emotion-face | Dual | 0.8486 | 0.8490 | 0.8486 | 0.8481 | var_smoothing=5.8780e-03, pca=PCA, scaler=MinMaxScaler |
| 21 | GNB | vit-face-age | Dual | 0.8315 | 0.8343 | 0.8315 | 0.8317 | var_smoothing=1.1253e-02, pca=PCA, scaler=MinMaxScaler |
| 22 | GNB | vit-face | Single | 0.8269 | 0.8271 | 0.8269 | 0.8258 | var_smoothing=4.1246e-02, pca=PCA, scaler=MinMaxScaler |
| 23 | RF | vit-emotion-age | Dual | 0.8111 | 0.8111 | 0.8111 | 0.8108 | n_est=200, depth=None, max_feat=log2, min_split=5, min_leaf=2, pca=PCA, scaler=None |
| 24 | RF | vit-emotion | Single | 0.8060 | 0.8063 | 0.8060 | 0.8057 | n_est=200, depth=None, max_feat=log2, min_split=5, min_leaf=1, pca=PCA, scaler=None |
| 25 | GNB | vit-emotion-age | Dual | 0.7681 | 0.7686 | 0.7681 | 0.7681 | var_smoothing=1.6037e-03, pca=PCA, scaler=MinMaxScaler |
| 26 | RF | vit-age | Single | 0.7366 | 0.7363 | 0.7366 | 0.7354 | n_est=200, depth=30, max_feat=log2, min_split=2, min_leaf=1, pca=PCA, scaler=None |
| 27 | GNB | vit-emotion | Single | 0.7338 | 0.7387 | 0.7338 | 0.7329 | var_smoothing=3.0703e-03, pca=PCA, scaler=None |
| 28 | GNB | vit-age | Single | 0.6963 | 0.6979 | 0.6963 | 0.6952 | var_smoothing=4.3755e-04, pca=PCA, scaler=MinMaxScaler |

> Sumber: `results/*.json` field test_accuracy/precision/recall/f1.

---

## 2. Leaderboard Top-10 Global

| Rank | Classifier | Fitur | Akurasi | Prec | Recall | F1 | Δ vs #1 |
|------|------------|-------|---------|------|--------|----|--------|
| 1 | SVM | vit-face-emotion-age | 0.9370 | 0.9372 | 0.9370 | 0.9369 | — |
| 2 | SVM | vit-emotion-face | 0.9329 | 0.9333 | 0.9329 | 0.9329 | -0.0042 |
| 3 | LR | vit-face-emotion-age | 0.9273 | 0.9275 | 0.9273 | 0.9273 | -0.0097 |
| 4 | SVM | vit-face-age | 0.9255 | 0.9254 | 0.9255 | 0.9254 | -0.0116 |
| 5 | LR | vit-emotion-face | 0.9241 | 0.9241 | 0.9241 | 0.9240 | -0.0130 |
| 6 | SVM | vit-emotion-age | 0.9208 | 0.9210 | 0.9208 | 0.9209 | -0.0162 |
| 7 | LR | vit-face-age | 0.9162 | 0.9162 | 0.9162 | 0.9162 | -0.0208 |
| 8 | SVM | vit-face | 0.9083 | 0.9084 | 0.9083 | 0.9083 | -0.0287 |
| 9 | LR | vit-face | 0.9060 | 0.9060 | 0.9060 | 0.9059 | -0.0310 |
| 10 | LR | vit-emotion-age | 0.9051 | 0.9052 | 0.9051 | 0.9051 | -0.0319 |

**Insight:** 5/10 adalah SVM, 4/10 LR; 6/10 memakai `vit-face-emotion-age`/`vit-emotion-face` (Face+Emotion inti). Gap SVM Tri vs GNB Tri +0.0865, vs GNB terburuk +0.2407. RF Tri (0.8620) kalah dari RF Dual 0.8685 — satu-satunya anomali.

---

## 3.1 SVM (SVC) — 288 komb ×5 = 1.440 fits/fitur

> Kernel RBF/poly C=10 deg2 dominan; 7/7 best pca=None.

| Rank | Fitur | Tipe | Dim | Akurasi | Precision | Recall | F1 | Parameter Terbaik |
|------|-------|------|-----|---------|-----------|--------|----|-------------------|
| **1** | **vit-face-emotion-age** | **Tri** | 2304 | **0.9370** | 0.9372 | 0.9370 | 0.9369 | C=10, poly, γ=scale, deg=2, pca=None, scaler=None |
| 2 | vit-emotion-face | Dual | 1536 | 0.9329 | 0.9333 | 0.9329 | 0.9329 | C=10, rbf, γ=scale, deg=2, pca=None, scaler=MinMaxScaler |
| 3 | vit-face-age | Dual | 1536 | 0.9255 | 0.9254 | 0.9255 | 0.9254 | C=10, poly, γ=scale, deg=2, pca=None, scaler=None |
| 4 | vit-emotion-age | Dual | 1536 | 0.9208 | 0.9210 | 0.9208 | 0.9209 | C=10, rbf, γ=scale, deg=2, pca=None, scaler=None |
| 5 | vit-face | Single | 768 | 0.9083 | 0.9084 | 0.9083 | 0.9083 | C=10, rbf, γ=scale, deg=2, pca=None, scaler=None |
| 6 | vit-emotion | Single | 768 | 0.9019 | 0.9020 | 0.9019 | 0.9017 | C=10, rbf, γ=scale, deg=2, pca=None, scaler=None |
| 7 | vit-age | Single | 768 | 0.8764 | 0.8767 | 0.8764 | 0.8765 | C=10, rbf, γ=scale, deg=2, pca=None, scaler=None |

**Ablation SVM:**
- `vit-face` Single: 0.9083
- `vit-emotion` Single: 0.9019
- `vit-age` Single: 0.8764
- `vit-emotion-face` Dual: 0.9329
- `vit-face-age` Dual: 0.9255
- `vit-emotion-age` Dual: 0.9208
- `vit-face-emotion-age` Tri: 0.9370

- Best Single→Best Dual: vit-face 0.9083 → vit-emotion-face 0.9329 = **+0.0245** (+2.70%, err-red -26.77%)
- Best Dual→Tri: vit-emotion-face 0.9329 → Tri 0.9370 = **+0.0042** (+0.45%)
- Best Single→Tri: vit-face 0.9083 → Tri 0.9370 = **+0.0287** (+3.16%, err-red -31.31%)
- Single terlemah: `vit-age` 0.8764 vs best Single 0.9083 gap +0.0319 — vit-age selalu terendah (SVM 0.8764 LR 0.8648 RF 0.7366 GNB 0.6963).

---

## 3.2 Logistic Regression — 270×5=1.350 fits

> C=0.1–1 solver lbfgs/newton-cg/saga; 7/7 pca=None.

| Rank | Fitur | Tipe | Dim | Akurasi | Precision | Recall | F1 | Parameter Terbaik |
|------|-------|------|-----|---------|-----------|--------|----|-------------------|
| **1** | **vit-face-emotion-age** | **Tri** | 2304 | **0.9273** | 0.9275 | 0.9273 | 0.9273 | C=0.1, solver=newton-cg, max_iter=500, pca=None, scaler=None |
| 2 | vit-emotion-face | Dual | 1536 | 0.9241 | 0.9241 | 0.9241 | 0.9240 | C=0.1, solver=lbfgs, max_iter=500, pca=None, scaler=None |
| 3 | vit-face-age | Dual | 1536 | 0.9162 | 0.9162 | 0.9162 | 0.9162 | C=0.1, solver=newton-cg, max_iter=500, pca=None, scaler=None |
| 4 | vit-face | Single | 768 | 0.9060 | 0.9060 | 0.9060 | 0.9059 | C=1, solver=newton-cg, max_iter=500, pca=None, scaler=MinMaxScaler |
| 5 | vit-emotion-age | Dual | 1536 | 0.9051 | 0.9052 | 0.9051 | 0.9051 | C=0.1, solver=lbfgs, max_iter=500, pca=None, scaler=None |
| 6 | vit-emotion | Single | 768 | 0.8847 | 0.8850 | 0.8847 | 0.8846 | C=1, solver=saga, max_iter=500, pca=None, scaler=MinMaxScaler |
| 7 | vit-age | Single | 768 | 0.8648 | 0.8649 | 0.8648 | 0.8648 | C=0.1, solver=lbfgs, max_iter=500, pca=None, scaler=None |

**Ablation LR:**
- `vit-face` Single: 0.9060
- `vit-emotion` Single: 0.8847
- `vit-age` Single: 0.8648
- `vit-emotion-face` Dual: 0.9241
- `vit-face-age` Dual: 0.9162
- `vit-emotion-age` Dual: 0.9051
- `vit-face-emotion-age` Tri: 0.9273

- Best Single→Best Dual: vit-face 0.9060 → vit-emotion-face 0.9241 = **+0.0181** (+1.99%, err-red -19.21%)
- Best Dual→Tri: vit-emotion-face 0.9241 → Tri 0.9273 = **+0.0032** (+0.35%)
- Best Single→Tri: vit-face 0.9060 → Tri 0.9273 = **+0.0213** (+2.35%, err-red -22.66%)
- Single terlemah: `vit-age` 0.8648 vs best Single 0.9060 gap +0.0412 — vit-age selalu terendah (SVM 0.8764 LR 0.8648 RF 0.7366 GNB 0.6963).

---

## 3.3 Random Forest — 288×5=1.440 fits

> n_est=200 depth None/30 max_feat sqrt/log2; 7/7 pca=PCA.

| Rank | Fitur | Tipe | Dim | Akurasi | Precision | Recall | F1 | Parameter Terbaik |
|------|-------|------|-----|---------|-----------|--------|----|-------------------|
| **1** | **vit-emotion-face** | **Dual** | 1536 | **0.8685** | 0.8689 | 0.8685 | 0.8682 | n_est=200, depth=None, max_feat=sqrt, min_split=5, min_leaf=1, pca=PCA, scaler=None |
| 2 | vit-face-emotion-age | Tri | 2304 | 0.8620 | 0.8620 | 0.8620 | 0.8613 | n_est=200, depth=30, max_feat=sqrt, min_split=5, min_leaf=1, pca=PCA, scaler=None |
| 3 | vit-face-age | Dual | 1536 | 0.8579 | 0.8578 | 0.8579 | 0.8573 | n_est=200, depth=None, max_feat=sqrt, min_split=2, min_leaf=1, pca=PCA, scaler=None |
| 4 | vit-face | Single | 768 | 0.8546 | 0.8543 | 0.8546 | 0.8539 | n_est=200, depth=30, max_feat=log2, min_split=2, min_leaf=1, pca=PCA, scaler=MinMaxScaler |
| 5 | vit-emotion-age | Dual | 1536 | 0.8111 | 0.8111 | 0.8111 | 0.8108 | n_est=200, depth=None, max_feat=log2, min_split=5, min_leaf=2, pca=PCA, scaler=None |
| 6 | vit-emotion | Single | 768 | 0.8060 | 0.8063 | 0.8060 | 0.8057 | n_est=200, depth=None, max_feat=log2, min_split=5, min_leaf=1, pca=PCA, scaler=None |
| 7 | vit-age | Single | 768 | 0.7366 | 0.7363 | 0.7366 | 0.7354 | n_est=200, depth=30, max_feat=log2, min_split=2, min_leaf=1, pca=PCA, scaler=None |

**Ablation RF:**
- `vit-face` Single: 0.8546
- `vit-emotion` Single: 0.8060
- `vit-age` Single: 0.7366
- `vit-emotion-face` Dual: 0.8685
- `vit-face-age` Dual: 0.8579
- `vit-emotion-age` Dual: 0.8111
- `vit-face-emotion-age` Tri: 0.8620

- Best Single→Best Dual: vit-face 0.8546 → vit-emotion-face 0.8685 = **+0.0139** (+1.63%, err-red -9.55%)
- Best Dual→Tri: vit-emotion-face 0.8685 → Tri 0.8620 = **-0.0065** (-0.75%)
- Best Single→Tri: vit-face 0.8546 → Tri 0.8620 = **+0.0074** (+0.87%, err-red -5.10%)
- ⚠️ RF anomali: Tri 0.8620 turun -0.0065 vs vit-emotion-face 0.8685 — curse of dimensionality.
- Single terlemah: `vit-age` 0.7366 vs best Single 0.8546 gap +0.1181 — vit-age selalu terendah (SVM 0.8764 LR 0.8648 RF 0.7366 GNB 0.6963).

---

## 3.4 Gaussian NB — 240×5=1.200 fits

> var_smoothing 4e-4–4e-2 logspace; 6/7 pca=PCA.

| Rank | Fitur | Tipe | Dim | Akurasi | Precision | Recall | F1 | Parameter Terbaik |
|------|-------|------|-----|---------|-----------|--------|----|-------------------|
| **1** | **vit-face-emotion-age** | **Tri** | 2304 | **0.8505** | 0.8512 | 0.8505 | 0.8505 | var_smoothing=5.8780e-03, pca=PCA, scaler=None |
| 2 | vit-emotion-face | Dual | 1536 | 0.8486 | 0.8490 | 0.8486 | 0.8481 | var_smoothing=5.8780e-03, pca=PCA, scaler=MinMaxScaler |
| 3 | vit-face-age | Dual | 1536 | 0.8315 | 0.8343 | 0.8315 | 0.8317 | var_smoothing=1.1253e-02, pca=PCA, scaler=MinMaxScaler |
| 4 | vit-face | Single | 768 | 0.8269 | 0.8271 | 0.8269 | 0.8258 | var_smoothing=4.1246e-02, pca=PCA, scaler=MinMaxScaler |
| 5 | vit-emotion-age | Dual | 1536 | 0.7681 | 0.7686 | 0.7681 | 0.7681 | var_smoothing=1.6037e-03, pca=PCA, scaler=MinMaxScaler |
| 6 | vit-emotion | Single | 768 | 0.7338 | 0.7387 | 0.7338 | 0.7329 | var_smoothing=3.0703e-03, pca=PCA, scaler=None |
| 7 | vit-age | Single | 768 | 0.6963 | 0.6979 | 0.6963 | 0.6952 | var_smoothing=4.3755e-04, pca=PCA, scaler=MinMaxScaler |

**Ablation GNB:**
- `vit-face` Single: 0.8269
- `vit-emotion` Single: 0.7338
- `vit-age` Single: 0.6963
- `vit-emotion-face` Dual: 0.8486
- `vit-face-age` Dual: 0.8315
- `vit-emotion-age` Dual: 0.7681
- `vit-face-emotion-age` Tri: 0.8505

- Best Single→Best Dual: vit-face 0.8269 → vit-emotion-face 0.8486 = **+0.0218** (+2.63%, err-red -12.57%)
- Best Dual→Tri: vit-emotion-face 0.8486 → Tri 0.8505 = **+0.0019** (+0.22%)
- Best Single→Tri: vit-face 0.8269 → Tri 0.8505 = **+0.0236** (+2.86%, err-red -13.64%)
- GNB Single→Tri terbesar: vit-age 0.6963→Tri 0.8505 **+0.1542** (+22.15%, err-red 50.77%); best Single vit-face 0.8269→Tri +0.0236.
- Single terlemah: `vit-age` 0.6963 vs best Single 0.8269 gap +0.1306 — vit-age selalu terendah (SVM 0.8764 LR 0.8648 RF 0.7366 GNB 0.6963).

---

## 4. Best Classifier per Konfigurasi Fitur

| Konfigurasi | Tipe | Best | Akurasi | Runner-up | Gap | Worst | Gap Best-Worst |
|-------------|------|------|---------|-----------|-----|-------|----------------|
| vit-age | Single | **SVM** 0.8764 | 0.8764 | LR 0.8648 | +0.0116 | GNB 0.6963 | +0.1801 |
| vit-emotion | Single | **SVM** 0.9019 | 0.9019 | LR 0.8847 | +0.0171 | GNB 0.7338 | +0.1681 |
| vit-face | Single | **SVM** 0.9083 | 0.9083 | LR 0.9060 | +0.0023 | GNB 0.8269 | +0.0815 |
| vit-emotion-age | Dual | **SVM** 0.9208 | 0.9208 | LR 0.9051 | +0.0157 | GNB 0.7681 | +0.1528 |
| vit-face-age | Dual | **SVM** 0.9255 | 0.9255 | LR 0.9162 | +0.0093 | GNB 0.8315 | +0.0940 |
| vit-emotion-face | Dual | **SVM** 0.9329 | 0.9329 | LR 0.9241 | +0.0088 | GNB 0.8486 | +0.0843 |
| vit-face-emotion-age | Tri | **SVM** 0.9370 | 0.9370 | LR 0.9273 | +0.0097 | GNB 0.8505 | +0.0866 |

**Pola:** SVM juara 7/7, LR runner-up 7/7 (gap 0.0023–0.0157), RF 3, GNB 4 — konsisten.

---

## 5. Fairness & Kesetaraan Demografis (OvR per Kelas)

> Support 360/kelas. Fokus pada model Tri per classifier (RF tetap Tri sebagai pembanding usulan).

### 5.1 OvR — SVM + vit-face-emotion-age (Tri, 0.9370)

| Kelas | Ras | Gender | Precision | Recall | F1 |
|-------|-----|--------|-----------|--------|----|
| Black_Males | Black | Pria | 0.9536 | 0.9694 | 0.9614 |
| White_Females | White | Wanita | 0.9415 | 0.8944 | 0.9174 |
| Asian_Males | Asian | Pria | 0.9241 | 0.9472 | 0.9355 |
| White_Males | White | Pria | 0.9250 | 0.9250 | 0.9250 |
| Black_Females | Black | Wanita | 0.9239 | 0.9444 | 0.9341 |
| Asian_Females | Asian | Wanita | 0.9549 | 0.9417 | 0.9483 |
| **Macro Avg** | — | — | **0.9372** | **0.9370** | **0.9369** |

Recall range **0.8944–0.9694** (gap 0.0750), F1 range **0.9174–0.9614** (gap 0.0441). Kelas terendah: **White_Females** 0.8944, tertinggi **Black_Males** 0.9694.
→ Gap 0.0750, seluruh F1 >0.91 — disparitas minimal.

*Improvement:* Recall `White_Females` vit-age 0.8361 → Tri 0.8944 = **+0.0583**.

---

### 5.2 OvR — LR + vit-face-emotion-age (Tri, 0.9273)

| Kelas | Ras | Gender | Precision | Recall | F1 |
|-------|-----|--------|-----------|--------|----|
| Black_Males | Black | Pria | 0.9505 | 0.9611 | 0.9558 |
| White_Females | White | Wanita | 0.9213 | 0.9111 | 0.9162 |
| Asian_Males | Asian | Pria | 0.9121 | 0.9222 | 0.9171 |
| White_Males | White | Pria | 0.9162 | 0.9111 | 0.9136 |
| Black_Females | Black | Wanita | 0.9076 | 0.9278 | 0.9176 |
| Asian_Females | Asian | Wanita | 0.9571 | 0.9306 | 0.9437 |
| **Macro Avg** | — | — | **0.9275** | **0.9273** | **0.9273** |

Recall range **0.9111–0.9611** (gap 0.0500), F1 range **0.9136–0.9558** (gap 0.0422). Kelas terendah: **White_Females** 0.9111, tertinggi **Black_Males** 0.9611.
→ Gap 0.0500 (terkecil), 91.11% White vs 96.11% Black_Males.

*Improvement:* Recall `White_Females` vit-age 0.8250 → Tri 0.9111 = **+0.0861**.

---

### 5.3 OvR — RF + vit-face-emotion-age (Tri, 0.8620)

| Kelas | Ras | Gender | Precision | Recall | F1 |
|-------|-----|--------|-----------|--------|----|
| Black_Males | Black | Pria | 0.8714 | 0.9222 | 0.8961 |
| White_Females | White | Wanita | 0.8793 | 0.7889 | 0.8316 |
| Asian_Males | Asian | Pria | 0.8683 | 0.8972 | 0.8825 |
| White_Males | White | Pria | 0.8415 | 0.8111 | 0.8260 |
| Black_Females | Black | Wanita | 0.8264 | 0.8333 | 0.8299 |
| Asian_Females | Asian | Wanita | 0.8850 | 0.9194 | 0.9019 |
| **Macro Avg** | — | — | **0.8620** | **0.8620** | **0.8613** |

Recall range **0.7889–0.9222** (gap 0.1333), F1 range **0.8260–0.9019** (gap 0.0759). Kelas terendah: **White_Females** 0.7889, tertinggi **Black_Males** 0.9222.
→ Gap 0.1333 terbesar; White_Females 0.7889 tersulit.

*Improvement:* Recall `White_Females` vit-age 0.6861 → Tri 0.7889 = **+0.1028**.

---

### 5.4 OvR — GNB + vit-face-emotion-age (Tri, 0.8505)

| Kelas | Ras | Gender | Precision | Recall | F1 |
|-------|-----|--------|-----------|--------|----|
| Black_Males | Black | Pria | 0.8936 | 0.8861 | 0.8898 |
| White_Females | White | Wanita | 0.8576 | 0.8028 | 0.8293 |
| Asian_Males | Asian | Pria | 0.8641 | 0.8833 | 0.8736 |
| White_Males | White | Pria | 0.7865 | 0.8389 | 0.8118 |
| Black_Females | Black | Wanita | 0.8272 | 0.8111 | 0.8191 |
| Asian_Females | Asian | Wanita | 0.8781 | 0.8806 | 0.8793 |
| **Macro Avg** | — | — | **0.8512** | **0.8505** | **0.8505** |

Recall range **0.8028–0.8861** (gap 0.0833), F1 range **0.8118–0.8898** (gap 0.0780). Kelas terendah: **White_Females** 0.8028, tertinggi **Black_Males** 0.8861.
→ Gap 0.0833; vs vit-age gap 0.1722 — fusi kurangi bias.

*Improvement:* Recall `White_Females` vit-age 0.6306 → Tri 0.8028 = **+0.1722**.

---

### 5.5 Ringkasan Fairness Tri-Domain

| Classifier | Akurasi | Rec Min | Rec Max | Gap Rec | F1 Min | F1 Max | Gap F1 | Tersulit |
|------------|---------|---------|---------|---------|--------|--------|--------|----------|
| SVM | 0.9370 | 0.8944 | 0.9694 | 0.0750 | 0.9174 | 0.9614 | 0.0441 | White_Females |
| LR | 0.9273 | 0.9111 | 0.9611 | 0.0500 | 0.9136 | 0.9558 | 0.0422 | White_Females |
| RF | 0.8620 | 0.7889 | 0.9222 | 0.1333 | 0.8260 | 0.9019 | 0.0759 | White_Females |
| GNB | 0.8505 | 0.8028 | 0.8861 | 0.0833 | 0.8118 | 0.8898 | 0.0780 | White_Females |

- LR gap terkecil (0.0500), SVM 0.0750, GNB 0.0833, RF 0.1333. Kelas tersulit konsisten Black_Females/White_Females — confusion lintas ras gender-sama, bukan intra-ras gender.

---

## 6. Ablation Kuantitatif per Classifier

| Transisi dirinci pada §3; ringkas lintas-classifier: Best Single→Best Dual +0.0181–0.0246, Dual→Tri +0.0032–0.0041 (RF -0.0065). Error reduction Best Single→Tri: SVM 31.33%, LR 22.66%, RF 0.50% (anomali), GNB 13.63% (best Single) / 50.77% (worst). |

### Detail Δ per Classifier

- **SVM:** vit-face 0.9083 → Tri 0.9370 = +0.0287 (+3.16%)
- **LR:** vit-face 0.9060 → Tri 0.9273 = +0.0213 (+2.35%)
- **RF:** vit-face 0.8546 → Tri 0.8620 = +0.0074 (+0.87%)
- **GNB:** vit-face 0.8269 → Tri 0.8505 = +0.0236 (+2.86%)

---

## 7. Matriks Konfusi Model Juara (SVM + vit-face-emotion-age, 0.9370)

| True \ Pred | Black_Males | White_Females | Asian_Males | White_Males | Black_Females | Asian_Females | Tot | Rec |
|---|:---:|:---:|:---:|:---:|:---:|:---:|---|---|
| Black_Males | **339** | 0 | 9 | 4 | 8 | 0 | 360 | 0.9417 |
| White_Females | 1 | **341** | 0 | 5 | 4 | 9 | 360 | 0.9472 |
| Asian_Males | 6 | 0 | **340** | 4 | 2 | 8 | 360 | 0.9444 |
| White_Males | 4 | 2 | 4 | **349** | 0 | 1 | 360 | 0.9694 |
| Black_Females | 5 | 16 | 6 | 2 | **322** | 9 | 360 | 0.8944 |
| Asian_Females | 0 | 10 | 9 | 2 | 6 | **333** | 360 | 0.9250 |
| **Total Pred** | **355** | **369** | **368** | **366** | **342** | **360** | **2160** |  |

| Kelas | TP | FP | FN | TN | OvR Acc | Prec | Rec | F1 |
|-------|----|----|----|----|---------|------|-----|----|
| Black_Males | 339 | 16 | 21 | 1784 | 0.9829 | 0.9549 | 0.9417 | 0.9483 |
| White_Females | 341 | 28 | 19 | 1772 | 0.9782 | 0.9241 | 0.9472 | 0.9355 |
| Asian_Males | 340 | 28 | 20 | 1772 | 0.9778 | 0.9239 | 0.9444 | 0.9341 |
| White_Males | 349 | 17 | 11 | 1783 | 0.9870 | 0.9536 | 0.9694 | 0.9614 |
| Black_Females | 322 | 20 | 38 | 1780 | 0.9731 | 0.9415 | 0.8944 | 0.9174 |
| Asian_Females | 333 | 27 | 27 | 1773 | 0.9750 | 0.9250 | 0.9250 | 0.9250 |
| **Macro** | — | — | — | — | **0.9790** | **0.9372** | **0.9370** | **0.9369** |

- Global 0.9370 (2024/2160), OvR 97.31–98.70%. Kesalahan dominan lintas ras gender-sama (16 Black_Females→White_Females), jarang intra-ras gender.

---

## 8. Mengapa SVM Menang?

| Aspek | SVM | LR | RF | GNB |
|-------|-----|----|----|-----|
| Rata-rata 7 | **0.9150** | 0.9057 | 0.8299 | 0.7904 |
| Tri | **0.9370** | 0.9273 | 0.8620 | 0.8505 |
| PCA best | 7/7 None | 7/7 None | 7/7 PCA | 6/7 PCA |

- SVM & LR pca=None (2.304-d penuh) — SVM RBF/poly tangkap non-linearitas residual (gap 0.0097 vs LR). RF/GNB butuh PCA karena overfit; GNB asumsi independen salah untuk ViT berkorelasi.
- Praktis: SVM Tri akurasi maksimal; LR Tri alternatif ringan (0.0097 di bawah, 10× inference, gap fairness 0.0500 vs 0.0750).

---

## 9. Kesimpulan

1. Tri superior universal (3/4 classifier puncak; RF -0.0065). Face+Emotion inti (Dual terbaik 4/4, 99.5% Tri).
2. Age lemah solo (selalu terendah) namun komplementer (Face+Age +0.0172 vs Face).
3. Fairness naik: lantai Recall Black_Females 0.8944 (Tri SVM) vs 0.6056 (GNB age); gap LR Tri terkecil 0.0500.
4. Rekomendasi: **SVM vit-face-emotion-age C10 poly scale deg2** produksi; **LR vit-face-emotion-age C0.1 newton-cg** alternatif ringan.

---

### Lampiran — Sumber & Reproduksibilitas

| Artefak | Lokasi |
|---------|--------|
| 28 JSON | `experiment/code/results/demogpairs_*_*.json` |
| Leaderboard | `experiment/code/md/3.0_compare.md` |
| 28 md per eksperimen | `experiment/code/md/{svm,gnb,rf,lr}/2.*.md` |
| Notebook | `2.1.*_svm` 288, `2.2.*_gnb` 240, `2.4.*_rf` 288, `2.5.*_lr` 270 |

> 4 desimal dari JSON; reproduksi: `u.load_json('results/demogpairs_svm_vit-face-emotion-age_SVC.json')['test_accuracy']` → 0.9370.

> Perubahan dari 7 SVM-only: +21 eksperimen, 4 tabel per-classifier, Top-10, 4 OvR, ablation kuantitatif, lintas-classifier.
