# Master AI Agent Reference Guide: Intersectional Face Race & Gender Classification via Multi-Domain Vision Transformer Feature Fusion

> **Notice to AI Agents:** This file (`README.AI.md`) is the single source of truth and comprehensive operational manual for this research repository. Any AI agent working on this codebase should read this document to understand the full context, architecture, dataset, feature extraction protocols, experimental results, code structure, evaluation metrics, and scientific writing rules without needing to reconstruct context from multiple disparate files.

---

## 📑 Table of Contents

1. [Executive Summary & Project Identity](#1-executive-summary--project-identity)
2. [Research Architecture & Methodology](#2-research-architecture--methodology)
3. [Dataset Specifications & Partitioning Protocol](#3-dataset-specifications--partitioning-protocol)
4. [Feature Extraction & Fusion Engineering](#4-feature-extraction--fusion-engineering)
5. [Classical Classifier Pipeline & GridSearchCV Optimization](#5-classical-classifier-pipeline--gridsearchcv-optimization)
6. [Comprehensive Experimental Benchmark (28 Experiments)](#6-comprehensive-experimental-benchmark-28-experiments)
7. [Intersectional Subgroup Performance & Disparity Analysis](#7-intersectional-subgroup-performance--disparity-analysis)
8. [Comparison with Prior Studies](#8-comparison-with-prior-studies)
9. [Repository & Codebase Architecture](#9-repository--codebase-architecture)
10. [Utilities Package Reference (`utils/`)](#10-utilities-package-reference-utils)
11. [Execution & Reproduction Workflow](#11-execution--reproduction-workflow)
12. [Scientific Claim Boundaries & Academic Writing Rules](#12-scientific-claim-boundaries--academic-writing-rules)
13. [Key Authors, Provenance & Citation Metadata](#13-key-authors-provenance--citation-metadata)

---

## 1. Executive Summary & Project Identity

### 1.1 Project Overview
- **Repository Name / Corpus:** `rafyakbar/face-race-gender-classification-using-multi-domain-vit`
- **Working Directory:** `D:\Research\face-race-gender-multi-vit`
- **Target Publication:** High-tier Q1 International Journal (IEEE Access / Pattern Recognition / Image and Vision Computing)
- **Paper Title:** *Multi-Domain Vision Transformer Fusion for Intersectional Demographic Classification from Facial Images*
- **Primary Goal:** Classify facial images into **6 intersectional demographic subgroups** (3 Races × 2 Genders: Asian/Black/White × Female/Male) by combining task-associated latent representations from three domain-specialized pre-trained Vision Transformers (**Face**, **Facial Emotion**, and **Facial Age**) and optimizing downstream classical machine learning pipelines via exhaustive 5-Fold Stratified GridSearchCV.

### 1.2 Key Research Findings & Benchmarks
- **Top Performing Model (Highest Performance Among Compared Studies):** **Support Vector Classifier (SVC) + Tri-Domain ViT Fusion** (`vit-face-emotion-age`, 2,304-d)
  - **Test Accuracy:** **93.70%** (2,024 / 2,160 correct on held-out test set)
  - **Macro Precision:** **0.9372**
  - **Macro Recall:** **0.9370**
  - **Macro F1-Score:** **0.9369**
  - **Best Hyperparameters:** $C = 10$, kernel = `'poly'`, degree = 2, gamma = `'scale'`, Scaler = `None`, PCA = `None`
- **Global Classifier Hierarchy (Average Accuracy across all 7 Feature Configurations):**
  $$\text{SVC } (0.9147) > \text{Logistic Regression } (0.9040) > \text{Random Forest } (0.8281) > \text{Gaussian Naive Bayes } (0.7937)$$
- **Ablation Insight:** Tri-Domain (2,304-d) outperforms Dual-Domain (1,536-d) and Single-Domain (768-d) across **3 of 4 classifiers** (SVC, LR, GNB). Random Forest achieved its best performance on dual-domain `Emotion ⊕ Face` (0.8685). Biological Age (`ViT-Age`), while weaker individually, provides additional discriminative morphology information that contributes to improved accuracy and reduced subgroup error.
- **Subgroup Disparity:** Subgroup F1-scores range from **0.9174 to 0.9614** (disparity gap $\Delta_{\text{F1}} = 0.0440$), with One-vs-Rest (OvR) Accuracy ranging from **97.31% to 98.70%**, showing a lower disparity across demographic subgroups compared to single- and dual-domain configurations.

---

## 2. Research Architecture & Methodology

### 2.1 End-to-End Methodological Framework

```
+---------------------------------------------------------------------------------------------------+
|                                  DEMOGPAIRS DATASET (10,800 Images)                                |
|                        6 Intersectional Classes (1,800 images/class - Perfectly Balanced)          |
+---------------------------------------------------------------------------------------------------+
                                                  │
                                                  ▼
+---------------------------------------------------------------------------------------------------+
|                                       IMAGE PREPROCESSING                                         |
|    RGB Conversion -> Bicubic Resizing to 224 x 224 -> Rescaling [0, 1] -> Channel Standardization  |
+---------------------------------------------------------------------------------------------------+
                                                  │
                ┌─────────────────────────────────┼─────────────────────────────────┐
                ▼                                 ▼                                 ▼
+-------------------------------+ +-------------------------------+ +-------------------------------+
|       ViT-Face Backbone       | |      ViT-Emotion Backbone     | |       ViT-Age Backbone        |
|     `skutaada/VIT-VGGFace`    | | `dima806/facial_emotions...`  | |  `dima806/facial_age_image...`|
| (Static Biometric Geometry)   | | (Dynamic Affective Micro-Exp) | | (Biological Aging Morphology) |
|   Extract [CLS] Token (768-d) | |   Extract [CLS] Token (768-d) | |   Extract [CLS] Token (768-d) |
+-------------------------------+ +-------------------------------+ +-------------------------------+
                │                                 │                                 │
                └─────────────────────────────────┼─────────────────────────────────┘
                                                  ▼
+---------------------------------------------------------------------------------------------------+
|                                      OFFLINE FEATURE ARCHIVE                                      |
|    features/demogpairs_vit-face.pkl (30.8MB) | vit-emotion.pkl (30.8MB) | vit-age.pkl (30.8MB)     |
+---------------------------------------------------------------------------------------------------+
                                                  │
                                                  ▼
+---------------------------------------------------------------------------------------------------+
|                                7 FEATURE ABLATION SCHEMES (Fusion)                                |
|  Single (768-d): face, emotion, age | Dual (1,536-d): face+age, emotion+age, emotion+face         |
|                             Tri-Domain (2,304-d): face + emotion + age                            |
+---------------------------------------------------------------------------------------------------+
                                                  │
                                                  ▼
+---------------------------------------------------------------------------------------------------+
|                                   DATA SPLIT & INFORMATION LEAKAGE PREVENTION                    |
|          Stratified 80/20 Split (seed=42): 8,640 Training Set  |  2,160 Held-Out Test Set         |
+---------------------------------------------------------------------------------------------------+
                                                  │
                                                  ▼
+---------------------------------------------------------------------------------------------------+
|                               MODULAR CLASSIFIER PIPELINE (GridSearchCV)                          |
|         Scaler [None | MinMaxScaler] -> PCA [None | 0.50 | 0.75] -> Classifier [SVC|LR|RF|GNB]    |
|                5-Fold Stratified Cross-Validation (1,086 combinations, 38,010 total fits)         |
+---------------------------------------------------------------------------------------------------+
                                                  │
                                                  ▼
+---------------------------------------------------------------------------------------------------+
|                                     FINAL EVALUATION & AUDIT                                      |
|    Macro Accuracy, Precision, Recall, F1 | One-vs-Rest Per-Class Metrics | Confusion Matrix 6 x 6 |
+---------------------------------------------------------------------------------------------------+
```

### 2.2 Three Domain-Specific Vision Transformer Extractors
All three extractors share the standard **ViT-Base (`vit-base-patch16-224`)** architecture:
- **Input:** $224 \times 224 \times 3$ RGB image divided into 196 non-overlapping patches of $16 \times 16$ pixels + 1 learnable `[CLS]` token = 197 total tokens.
- **Layers & Depth:** 12 Transformer Encoder layers, 12 multi-head self-attention heads, hidden dimension $D = 768$.
- **Offline One-Pass Extraction:** The model backbones remain frozen. Each image is processed once to extract the 768-d `[CLS]` embedding from the final hidden state:
  $$\mathbf{z}_0 = [\mathbf{x}_{\text{class}}; \, \mathbf{x}_p^1\mathbf{E}; \, \dots; \, \mathbf{x}_p^{196}\mathbf{E}] + \mathbf{E}_{\text{pos}}$$
  $$\mathbf{f}_{\text{domain}} = \text{LayerNorm}(\mathbf{z}_L^0) \in \mathbb{R}^{768}$$
  where $\mathbf{z}_L^0$ is the CLS token representation from the final encoder layer $L$.

| Model Label | HuggingFace Checkpoint Path | Specialized Representation Domain | Task-Associated Visual Cues |
|---|---|---|---|
| **ViT-Face** | `skutaada/VIT-VGGFace` | Facial Biometric Geometry | Task-associated representations of craniofacial biometric geometry |
| **ViT-Emotion** | `dima806/facial_emotions_image_detection` | Affective & Emotional Expressions | Task-associated representations of dynamic affective expressions |
| **ViT-Age** | `dima806/facial_age_image_detection` | Biological Age & Life Stages | Task-associated representations of biological aging morphology |

---

## 3. Dataset Specifications & Partitioning Protocol

### 3.1 Benchmark Dataset: DemogPairs
- **Primary Citation:** I. Hupont and C. Fernández, "DemogPairs: Quantifying the Impact of Demographic Imbalance in Deep Face Recognition," in *2019 14th IEEE International Conference on Automatic Face & Gesture Recognition (FG 2019)*, pp. 1-7, DOI: `10.1109/FG.2019.8756625`.
- **Dataset Composition:** 10,800 high-resolution facial images representing 600 individual faces (100 per intersectional demographic subgroup, 18 images each).
- **Intersectional Classes (6-Class Balanced Distribution):**

| Label Index | Class Name | Race | Gender | Total Images | Train Set (80%) | Test Set (20%) |
|:---:|---|:---:|:---:|:---:|:---:|:---:|
| `0` | `Black_Males` | Black | Male | 1,800 | 1,440 | 360 |
| `1` | `White_Females` | White | Female | 1,800 | 1,440 | 360 |
| `2` | `Asian_Males` | Asian | Male | 1,800 | 1,440 | 360 |
| `3` | `White_Males` | White | Male | 1,800 | 1,440 | 360 |
| `4` | `Black_Females` | Black | Female | 1,800 | 1,440 | 360 |
| `5` | `Asian_Females` | Asian | Female | 1,800 | 1,440 | 360 |
| **Total** | **6 Intersectional Classes** | **3 Races** | **2 Genders** | **10,800** | **8,640** | **2,160** |

> **Critical Note on Label Encodings:**
> 1. `DEMOGPairs_LABEL_TO_IDX` (in `utils/constants.py`) maps indices as: `Black_Males: 0`, `White_Females: 1`, `Asian_Males: 2`, `White_Males: 3`, `Black_Females: 4`, `Asian_Females: 5`.
> 2. `DEMOGPairs_CLASSES` (alphabetical list) is ordered as: `['Asian_Females', 'Asian_Males', 'Black_Females', 'Black_Males', 'White_Females', 'White_Males']`.
> 3. Classification reports and confusion matrix calculations in `utils/evaluation.py` explicitly use `labels=[DEMOGPairs_LABEL_TO_IDX[n] for n in target_names]` to align matrix axes perfectly.

### 3.2 Partitioning & Information Leakage Prevention Protocol
- **Split Ratio:** Stratified 80/20 train/test partition using `sklearn.model_selection.train_test_split(..., test_size=0.2, random_state=42, stratify=y)`.
- **Training Subset:** 8,640 samples (1,440 per class).
- **Held-Out Test Subset:** 2,160 samples (360 per class).
- **Cross-Validation on Train Split:** 5-Fold Stratified K-Fold Cross-Validation (`shuffle=True, random_state=42`) used within GridSearchCV.
- **Information Leakage Prevention:** The pipeline is designed to prevent information leakage: feature scaling (e.g., `MinMaxScaler`) and dimensionality reduction (`PCA`) are fitted exclusively on training folds within GridSearchCV and applied as transforms only on validation and held-out test data.

---

## 4. Feature Extraction & Fusion Engineering

### 4.1 Seven Feature Ablation Schemes

| # | Feature Scheme Name | Category | Dimensionality | Vector Concatenation Formulation |
|:---:|---|:---:|:---:|---|
| 1 | `vit-age` | Single-Domain | 768 | $\mathbf{z} = \mathbf{f}_{\text{age}} \in \mathbb{R}^{768}$ |
| 2 | `vit-emotion` | Single-Domain | 768 | $\mathbf{z} = \mathbf{f}_{\text{emotion}} \in \mathbb{R}^{768}$ |
| 3 | `vit-face` | Single-Domain | 768 | $\mathbf{z} = \mathbf{f}_{\text{face}} \in \mathbb{R}^{768}$ |
| 4 | `vit-emotion-age` | Dual-Domain | 1,536 | $\mathbf{z} = [\mathbf{f}_{\text{emotion}} \,\|\, \mathbf{f}_{\text{age}}] \in \mathbb{R}^{1536}$ |
| 5 | `vit-face-age` | Dual-Domain | 1,536 | $\mathbf{z} = [\mathbf{f}_{\text{face}} \,\|\, \mathbf{f}_{\text{age}}] \in \mathbb{R}^{1536}$ |
| 6 | `vit-emotion-face` | Dual-Domain | 1,536 | $\mathbf{z} = [\mathbf{f}_{\text{emotion}} \,\|\, \mathbf{f}_{\text{face}}] \in \mathbb{R}^{1536}$ |
| 7 | `vit-face-emotion-age` | **Tri-Domain (Usulan)** | **2,304** | $\mathbf{z} = [\mathbf{f}_{\text{face}} \,\|\, \mathbf{f}_{\text{emotion}} \,\|\, \mathbf{f}_{\text{age}}] \in \mathbb{R}^{2304}$ |

### 4.2 Feature File Storage
Latent features are cached in `experiment/code/features/` as serialized dictionaries mapping relative image paths to 768-d numpy arrays:
- `demogpairs_vit-face.pkl` (30.8 MB)
- `demogpairs_vit-emotion.pkl` (30.8 MB)
- `demogpairs_vit-age.pkl` (30.8 MB)

---

## 5. Classical Classifier Pipeline & GridSearchCV Optimization

### 5.1 Pipeline Structure
Each experimental configuration executes an end-to-end `sklearn.pipeline.Pipeline`:
$$\mathbf{x} \xrightarrow{\text{Scaler}} \tilde{\mathbf{x}} \xrightarrow{\text{PCA}} \hat{\mathbf{x}} \xrightarrow{\text{Classifier}} \hat{y} \in \{0, 1, 2, 3, 4, 5\}$$

### 5.2 Hyperparameter Search Spaces

```python
# 1. Support Vector Classifier (288 combinations per feature scheme)
param_grid_svm = {
    'scaler': [None, MinMaxScaler()],
    'pca': [None, PCA(n_components=0.50), PCA(n_components=0.75)],
    'classifier__C': [0.1, 1, 10, 100],
    'classifier__kernel': ['linear', 'rbf', 'poly'],
    'classifier__degree': [2, 3],
    'classifier__gamma': ['scale', 'auto'],
}

# 2. Logistic Regression (270 combinations per feature scheme)
param_grid_lr = {
    'scaler': [None, MinMaxScaler()],
    'pca': [None, PCA(n_components=0.50), PCA(n_components=0.75)],
    'classifier__C': [0.01, 0.1, 1, 10, 100],
    'classifier__solver': ['lbfgs', 'saga', 'newton-cg'],
    'classifier__max_iter': [200, 500, 2000],
}

# 3. Random Forest (288 combinations per feature scheme)
param_grid_rf = {
    'scaler': [None, MinMaxScaler()],
    'pca': [None, PCA(n_components=0.50), PCA(n_components=0.75)],
    'classifier__n_estimators': [100, 200],
    'classifier__max_depth': [None, 10, 30],
    'classifier__max_features': ['sqrt', 'log2'],
    'classifier__min_samples_split': [2, 5],
    'classifier__min_samples_leaf': [1, 2],
}

# 4. Gaussian Naive Bayes (240 combinations per feature scheme)
param_grid_gnb = {
    'scaler': [None, MinMaxScaler()],
    'pca': [None, PCA(n_components=0.50), PCA(n_components=0.75)],
    'classifier__var_smoothing': np.logspace(-9, 2, 40),
}
```

### 5.3 Optimization Scale
- **Combinations per Feature Scheme:** 1,086 combinations ($288 + 270 + 288 + 240$).
- **Fits per Feature Scheme (5-Fold CV):** 5,430 fits.
- **Total Cross-Validation Fits (7 Schemes × 4 Classifiers):** **38,010 fits** + 28 refit models.
- **Scoring & Refit:** Scored with `accuracy`, `precision_macro`, `recall_macro`, `f1_macro`; `refit='accuracy'`.

---

## 6. Comprehensive Experimental Benchmark (28 Experiments)

Below is the complete, definitive leaderboard of all 28 experiments evaluated on the held-out test set ($N = 2,160$). All figures are direct 4-decimal values extracted from `experiment/code/results/*.json`.

### 6.1 Complete 28-Experiment Leaderboard

| Rank | Classifier | Feature Scheme | Type | Dim | Test Accuracy | Macro Precision | Macro Recall | Macro F1 | Best Hyperparameters |
|:---:|---|---|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 🥇 **1** | **SVM** | **vit-face-emotion-age** | **Tri** | **2,304** | **0.9370** | **0.9372** | **0.9370** | **0.9369** | `C=10, kernel='poly', degree=2, gamma='scale', scaler=None, pca=None` |
| 🥈 **2** | **SVM** | **vit-emotion-face** | **Dual** | 1,536 | **0.9329** | 0.9333 | 0.9329 | 0.9329 | `C=10, kernel='rbf', degree=2, gamma='scale', scaler=MinMaxScaler, pca=None` |
| 🥉 **3** | **LR** | **vit-face-emotion-age** | **Tri** | **2,304** | **0.9273** | 0.9275 | 0.9273 | 0.9273 | `C=0.1, solver='newton-cg', max_iter=500, scaler=None, pca=None` |
| 4 | SVM | vit-face-age | Dual | 1,536 | 0.9255 | 0.9254 | 0.9255 | 0.9254 | `C=10, kernel='poly', degree=2, gamma='scale', scaler=None, pca=None` |
| 5 | LR | vit-emotion-face | Dual | 1,536 | 0.9241 | 0.9241 | 0.9241 | 0.9240 | `C=0.1, solver='lbfgs', max_iter=500, scaler=None, pca=None` |
| 6 | SVM | vit-emotion-age | Dual | 1,536 | 0.9208 | 0.9210 | 0.9208 | 0.9209 | `C=10, kernel='rbf', degree=2, gamma='scale', scaler=None, pca=None` |
| 7 | LR | vit-face-age | Dual | 1,536 | 0.9162 | 0.9162 | 0.9162 | 0.9162 | `C=0.1, solver='newton-cg', max_iter=500, scaler=None, pca=None` |
| 8 | SVM | vit-face | Single | 768 | 0.9083 | 0.9084 | 0.9083 | 0.9083 | `C=10, kernel='rbf', degree=2, gamma='scale', scaler=None, pca=None` |
| 9 | LR | vit-face | Single | 768 | 0.9060 | 0.9060 | 0.9060 | 0.9059 | `C=1, solver='newton-cg', max_iter=500, scaler=MinMaxScaler, pca=None` |
| 10 | LR | vit-emotion-age | Dual | 1,536 | 0.9051 | 0.9052 | 0.9051 | 0.9051 | `C=0.1, solver='lbfgs', max_iter=500, scaler=None, pca=None` |
| 11 | SVM | vit-emotion | Single | 768 | 0.9019 | 0.9020 | 0.9019 | 0.9017 | `C=10, kernel='rbf', degree=2, gamma='scale', scaler=None, pca=None` |
| 12 | LR | vit-emotion | Single | 768 | 0.8847 | 0.8850 | 0.8847 | 0.8846 | `C=1, solver='saga', max_iter=500, scaler=MinMaxScaler, pca=None` |
| 13 | SVM | vit-age | Single | 768 | 0.8764 | 0.8767 | 0.8764 | 0.8765 | `C=10, kernel='rbf', degree=2, gamma='scale', scaler=None, pca=None` |
| 14 | RF | vit-emotion-face | Dual | 1,536 | 0.8685 | 0.8689 | 0.8685 | 0.8682 | `n_estimators=200, max_depth=None, max_features='sqrt', min_samples_split=5, min_samples_leaf=1, pca=PCA(0.75), scaler=None` |
| 15 | LR | vit-age | Single | 768 | 0.8648 | 0.8649 | 0.8648 | 0.8648 | `C=0.1, solver='lbfgs', max_iter=500, scaler=None, pca=None` |
| 16 | RF | vit-face-emotion-age | Tri | 2,304 | 0.8620 | 0.8620 | 0.8620 | 0.8613 | `n_estimators=200, max_depth=30, max_features='sqrt', min_samples_split=5, min_samples_leaf=1, pca=PCA(0.75), scaler=None` |
| 17 | RF | vit-face-age | Dual | 1,536 | 0.8579 | 0.8578 | 0.8579 | 0.8573 | `n_estimators=200, max_depth=None, max_features='sqrt', min_samples_split=2, min_samples_leaf=1, pca=PCA(0.75), scaler=None` |
| 18 | RF | vit-face | Single | 768 | 0.8546 | 0.8543 | 0.8546 | 0.8539 | `n_estimators=200, max_depth=30, max_features='log2', min_samples_split=2, min_samples_leaf=1, pca=PCA(0.75), scaler=MinMaxScaler` |
| 19 | GNB | vit-face-emotion-age | Tri | 2,304 | 0.8505 | 0.8512 | 0.8505 | 0.8505 | `var_smoothing=0.005878, pca=PCA(0.75), scaler=None` |
| 20 | GNB | vit-emotion-face | Dual | 1,536 | 0.8486 | 0.8490 | 0.8486 | 0.8481 | `var_smoothing=0.005878, pca=PCA(0.75), scaler=MinMaxScaler` |
| 21 | GNB | vit-face-age | Dual | 1,536 | 0.8315 | 0.8343 | 0.8315 | 0.8317 | `var_smoothing=0.011253, pca=PCA(0.75), scaler=MinMaxScaler` |
| 22 | GNB | vit-face | Single | 768 | 0.8269 | 0.8271 | 0.8269 | 0.8258 | `var_smoothing=0.041246, pca=PCA(0.75), scaler=MinMaxScaler` |
| 23 | RF | vit-emotion-age | Dual | 1,536 | 0.8111 | 0.8111 | 0.8111 | 0.8108 | `n_estimators=200, max_depth=None, max_features='log2', min_samples_split=5, min_samples_leaf=2, pca=PCA(0.75), scaler=None` |
| 24 | RF | vit-emotion | Single | 768 | 0.8060 | 0.8063 | 0.8060 | 0.8057 | `n_estimators=200, max_depth=None, max_features='log2', min_samples_split=5, min_samples_leaf=1, pca=PCA(0.75), scaler=None` |
| 25 | GNB | vit-emotion-age | Dual | 1,536 | 0.7681 | 0.7686 | 0.7681 | 0.7681 | `var_smoothing=0.001604, pca=PCA(0.75), scaler=MinMaxScaler` |
| 26 | RF | vit-age | Single | 768 | 0.7366 | 0.7363 | 0.7366 | 0.7354 | `n_estimators=200, max_depth=30, max_features='log2', min_samples_split=2, min_samples_leaf=1, pca=PCA(0.75), scaler=None` |
| 27 | GNB | vit-emotion | Single | 768 | 0.7338 | 0.7387 | 0.7338 | 0.7329 | `var_smoothing=0.003070, pca=PCA(0.75), scaler=None` |
| 28 | GNB | vit-age | Single | 768 | 0.6963 | 0.6979 | 0.6963 | 0.6952 | `var_smoothing=0.000438, pca=PCA(0.75), scaler=MinMaxScaler` |

### 6.2 Key Ablation Analysis
1. **Single $\to$ Dual Fusion Progression:**
   - SVM: `vit-face` (0.9083) $\to$ `vit-emotion-face` (0.9329) = **+0.0245 (+2.70% gain, 26.77% error reduction)**.
   - LR: `vit-face` (0.9060) $\to$ `vit-emotion-face` (0.9241) = **+0.0181 (+1.99% gain, 19.21% error reduction)**.
2. **Dual $\to$ Tri-Domain Fusion Progression:**
   - SVM: `vit-emotion-face` (0.9329) $\to$ `vit-face-emotion-age` (0.9370) = **+0.0042 (+0.45% gain, 6.11% error reduction)**.
   - LR: `vit-emotion-face` (0.9241) $\to$ `vit-face-emotion-age` (0.9273) = **+0.0032 (+0.35% gain, 4.22% error reduction)**.
3. **Cumulative Single $\to$ Tri-Domain Impact:**
   - SVM: `vit-face` (0.9083) $\to$ `vit-face-emotion-age` (0.9370) = **+0.0287 (+3.16% gain, 31.31% total error reduction)**.
4. **Behavior of Preprocessing Transformations:**
   - **SVC & LR:** 7 out of 7 configurations perform best with `pca=None` (retaining full raw 2,304-d latent space). The degree-2 polynomial kernel selected by SVC may capture nonlinear interactions among latent feature dimensions, which could contribute to its strong performance on high-dimensional fused representations.
   - **RF & GNB:** 7 out of 7 configurations select `pca=PCA(n_components=0.75)` to prevent severe overfitting on sparse high-dimensional data. Note: The drop in RF performance at tri-domain dimensionality (2,304-d) may reflect the increased difficulty of partitioning a higher-dimensional feature space using randomized decision splits.

---

## 7. Intersectional Subgroup Performance & Disparity Analysis

### 7.1 Subgroup Performance for the Top-Performing Model (SVC Tri-Domain, $N = 2,160$)

| Intersectional Subgroup | Race | Gender | Support | TP | FP | FN | TN | OvR Accuracy | Precision | Recall | F1-Score |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **White_Males** | White | Male | 360 | 349 | 17 | 11 | 1,783 | **98.70%** | 0.9536 | **0.9694** | **0.9614** |
| **Black_Males** | Black | Male | 360 | 339 | 16 | 21 | 1,784 | **98.29%** | 0.9549 | 0.9417 | 0.9483 |
| **White_Females** | White | Female | 360 | 341 | 28 | 19 | 1,772 | **97.82%** | 0.9241 | 0.9472 | 0.9355 |
| **Asian_Males** | Asian | Male | 360 | 340 | 28 | 20 | 1,772 | **97.78%** | 0.9239 | 0.9444 | 0.9341 |
| **Asian_Females** | Asian | Female | 360 | 333 | 27 | 27 | 1,773 | **97.50%** | 0.9250 | 0.9250 | 0.9250 |
| **Black_Females** | Black | Female | 360 | 322 | 20 | 38 | 1,780 | **97.31%** | 0.9415 | 0.8944 | 0.9174 |
| **Macro Average** | **All** | **All** | **2,160** | **-** | **-** | **-** | **-** | **97.90%** | **0.9372** | **0.9370** | **0.9369** |

### 7.2 Confusion Matrix (Actual 2,160 Held-Out Samples)

```
                       Predicted Class
True Class        AF    AM    BF    BM    WF    WM  │ Total │ Recall
─────────────────────────────────────────────────────┼───────┼───────
Asian_Females    333     9     6     0    10     2  │   360 │ 0.9250
Asian_Males        8   340     2     6     0     4  │   360 │ 0.9444
Black_Females      9     6   322     5    16     2  │   360 │ 0.8944
Black_Males        0     9     8   339     0     4  │   360 │ 0.9417
White_Females      9     0     4     1   341     5  │   360 │ 0.9472
White_Males        1     4     0     4     2   349  │   360 │ 0.9694
─────────────────────────────────────────────────────┼───────┼───────
Predicted Total  360   368   342   355   369   366  │ 2,160 │
```

### 7.3 Critical Error Insights
1. **Cross-Race Same-Gender Misclassifications:** The dominant error pattern occurs between subjects of different races sharing the *same gender* (e.g., 16 `Black_Females` misclassified as `White_Females`, 10 `Asian_Females` as `White_Females`).
2. **Near-Zero Gender Confusion:** Intra-race or cross-race gender confusion is virtually non-existent (<1% error rate), indicating that the multi-domain representation separates gender boundaries effectively.
3. **Disparity Metrics:**
   - F1-Score Disparity: $\Delta_{\text{F1}} = \max(\text{F1}) - \min(\text{F1}) = 0.9614 - 0.9174 = \mathbf{0.0440}$.
   - Recall Disparity: $\Delta_{\text{Recall}} = \max(\text{Recall}) - \min(\text{Recall}) = 0.9694 - 0.8944 = \mathbf{0.0750}$.
   - Logistic Regression Tri-Domain achieves a narrower F1 gap ($\Delta_{\text{F1}} = 0.0422$, $\Delta_{\text{Recall}} = 0.0500$).
   - **Note:** OvR Accuracy values appear high due to the dominance of negative samples (5:1 ratio in binary one-vs-rest evaluation). Range-based disparity (max - min) is used as a simple indicator of subgroup performance variation, not a comprehensive fairness measure.

---

## 8. Comparison with Prior Studies

| # | Study / Publication | Method / Architecture | Benchmark Dataset | Evaluated Classes | Reported Accuracy | Macro F1 | Intersectional Audit? |
|:---:|---|---|---|:---:|:---:|:---:|:---:|
| 1 | Belcar et al. (Sensors 2022) | Middle-Face CNN (ResNet) | Custom | 4 Ethnicity | 61.74% | - | No |
| 2 | Sunitha et al. (IVC 2022) | Deep CNN + Hybrid Metaheuristics | FairFace / UTKFace | Ethnicity | 88.50% | - | No |
| 3 | Liao et al. (Appl. Sci. 2022) | Multi-Task Multi-Scale CNN | Multi-task Face | Gender & Age | ~89.20% | - | No |
| 4 | Brinkmann et al. (ICCV 2023) | Social Bias in ViT Encoders | FairFace | Gender / Race | 88.30% | - | Partial |
| 5 | Ramachandran & Rattani (2023) | StyleGAN2 Generative Debiasing | CelebA / UTKFace | Gender | 87.10% | 0.8690 | Partial |
| 6 | Chen et al. (JVCI 2023) | Parallel Attention Sharing Net | CelebA / LFWA | 40 Attributes | 91.80% | - | No |
| 7 | Tahyudin et al. (JOIV 2024) | Vision Transformer Base | AFAD (Asian Only) | Gender | 81.74% (Cross) | 0.8170 | No (Domain Shift) |
| 8 | Kalkatawi & Saeed (IJACSA 2024)| MaxViT Multi-Axis Transformer | FairFace | 6 Ethnicity | 77.20% | 0.7680 | No |
| 9 | Putri et al. (IEEE ICVEE 2025) | Dual-ViT (Face+Emotion) + SVM | DemogPairs | 6 Intersectional | 92.41% | 0.9240 | Yes |
| 10| Putri et al. (JIEET 2025) | MD-ViT (Face+Age) + XGBoost | DemogPairs | 6 Intersectional | 89.07% | 0.8905 | Yes |
| ⭐ | **Proposed Framework (2026)** | **Tri-Domain ViT (Face+Emotion+Age) + Optimized SVC** | **DemogPairs (10,800)** | **6 Intersectional** | **93.70%** | **0.9369** | **Yes (Full Audit)** |

> **Note:** Direct comparison in paper (Table XII) includes only studies evaluated on DemogPairs (rows 9, 10, and the Proposed Framework). Studies 1-8 evaluated on different datasets and class definitions and are cited for contextual positioning only. Use "highest performance among the compared studies on DemogPairs" - not "state-of-the-art."

---

## 9. Repository & Codebase Architecture

```
D:\Research\face-race-gender-multi-vit\
├── README.md                           # Public GitHub repository landing page
├── README.AI.md                        # Master AI Agent reference guide (This file)
├── WORKFLOW.md                         # Universal Research Manuscript Pipeline SOP (Outline -> paper/ -> paper_latex_id/ -> paper_latex_en/)
├── paper_outline.md                    # Detailed paper outline (IEEE Access / Q1 target)
├── prompts.txt                         # Experimental instructions and agent logs
├── scopus_query.txt                    # Scopus literature search query strings
│
├── images/
│   ├── method.png                      # Architecture & methodology framework diagram
│   └── method.pptx                     # Editable presentation source diagram
│
├── rules/
│   ├── md_rules.txt                    # Mandatory Markdown writing rules & constraints
│   ├── latex_rules.txt                 # Mandatory LaTeX conversion & formatting rules
│   └── IEEE_citation_guidelines.md     # IEEE referencing style and citation guidelines
│
├── references/
│   └── 2019_DemogPairs...bib           # BibTeX entry for DemogPairs benchmark
│
├── related_works/                      # Literature review corpus (10 core papers)
│   ├── literature_matrix.md            # Comparative matrix across all 10 papers
│   ├── gap_analysis.md                 # Formalization of gaps G1-G8 and priorities P1-P4
│   ├── tren_analisis.md                # Knowledge mapping and evolutionary trends
│   ├── sintesis_literatur.md           # Master hub for literature review
│   ├── bib/                            # BibTeX files for all 10 papers
│   ├── pdf/                            # Full-text PDF papers
│   └── summaries/                      # Detailed markdown summaries per paper
│
└── experiment/
    ├── 00_overview.md                  # High-level experimental framework overview
    ├── 01_prepare-data.md              # Dataset preparation, composition & split
    ├── 02_preprocessing.md             # Image normalization and bicubic resizing
    ├── 03_feature-extraction.md        # ViT feature extraction & concatenation fusion
    ├── 04_methods.md                   # 4 Classifiers, pipeline & GridSearchCV protocol
    ├── 05_results.md                   # 28-experiment leaderboard & fairness audit
    │
    └── code/
        ├── app.py                      # Interactive Gradio demo web application
        ├── 1.1_vit-face_demogpairs.ipynb       # ViT-Face feature extraction notebook
        ├── 1.1_vit-emotion_demogpairs.ipynb    # ViT-Emotion feature extraction notebook
        ├── 1.1_vit-age_demogpairs.ipynb        # ViT-Age feature extraction notebook
        ├── 2.1.1_svm_vit-face_demogpairs.ipynb ... 2.1.7_svm_vit-face-emotion-age_demogpairs.ipynb (7 SVM)
        ├── 2.2.1_gnb_vit-face_demogpairs.ipynb ... 2.2.7_gnb_vit-face-emotion-age_demogpairs.ipynb (7 GNB)
        ├── 2.4.1_rf_vit-face_demogpairs.ipynb  ... 2.4.7_rf_vit-face-emotion-age_demogpairs.ipynb  (7 RF)
        ├── 2.5.1_lr_vit-face_demogpairs.ipynb  ... 2.5.7_lr_vit-face-emotion-age_demogpairs.ipynb  (7 LR)
        ├── 3.0_compare.ipynb           # Global comparative analysis & leaderboard
        ├── 4.0_test.ipynb              # Final pipeline testing & interactive inference
        │
        ├── utils/                      # Modular Python utility package
        │   ├── __init__.py             # Exposes core APIs
        │   ├── constants.py            # Label dictionaries & class lists
        │   ├── dataset.py              # Metadata parsing & dataset loader
        │   ├── display.py              # HTML / CLI tabular formatting
        │   ├── evaluation.py           # GridSearchCV orchestration & metrics
        │   ├── extraction.py           # ViT [CLS] feature extractor
        │   ├── serialization.py        # Joblib & JSON loaders/savers
        │   └── time_helpers.py         # Formats elapsed execution time
        │
        ├── dataset/
        │   └── demogpairs/
        │       ├── metadata/           # 6 metadata .txt files (1,800 rows each)
        │       └── images/             # 600 subject directories (18 JPEGs each)
        │
        ├── features/                   # Serialized feature archives (.pkl)
        │   ├── demogpairs_vit-face.pkl
        │   ├── demogpairs_vit-emotion.pkl
        │   └── demogpairs_vit-age.pkl
        │
        ├── models/                     # 28 trained joblib models (.pkl)
        ├── results/                    # 28 evaluation result JSON files (.json)
        ├── images/                     # 28 confusion matrix diagrams (.png)
        └── md/                         # Exported markdown versions of notebooks
```

---

## 10. Utilities Package Reference (`utils/`)

Located at `experiment/code/utils/`:

### 10.1 `constants.py`
```python
DEMOGPairs_CLASSES = [
    "Asian_Females", "Asian_Males", "Black_Females",
    "Black_Males", "White_Females", "White_Males"
]
DEMOGPairs_LABEL_TO_IDX = {
    "Black_Males": 0, "White_Females": 1, "Asian_Males": 2,
    "White_Males": 3, "Black_Females": 4, "Asian_Females": 5
}
DEMOGPairs_IDX_TO_LABEL = {v: k for k, v in DEMOGPairs_LABEL_TO_IDX.items()}
```

### 10.2 `dataset.py`
- `load_demogpairs(metadata_path, images_path) -> list[dict]`: Parses the 6 metadata `.txt` files in `dataset/demogpairs/metadata/` and produces a list of 10,800 structured dictionary records with keys `db_code`, `image_path`, `full_path`, `label`, and `label_idx`.

### 10.3 `extraction.py`
- `extract_vit_features(img, model=None, model_path=None, device=None, feature_type='cls') -> np.ndarray`: Takes an image filepath or NumPy array, runs HuggingFace `AutoImageProcessor` to format tensors to 224 × 224, queries the Vision Transformer backbone, and returns a 1D NumPy array of shape `(768,)` corresponding to the `[CLS]` token (or mean pool).

### 10.4 `evaluation.py`
- `evaluate_models(grid_models, x_train, y_train, x_test, y_test, model_prefix, target_names, results_path) -> tuple`: Fits GridSearchCV models (or loads them if `.pkl` already exists), performs prediction on test data, generates classification reports, computes One-vs-Rest (OvR) per-class metrics, creates confusion matrix heatmaps (saved to `images/`), and serializes all metadata to JSON in `results/`.

### 10.5 `serialization.py`
- `save_object(obj, filename, compress=9)`: Saves binary objects using joblib with compression level 9.
- `load_object(filename)`: Loads joblib-serialized binary objects.
- `save_json(data, json_file)`: Formats and writes dictionaries to indented JSON.
- `load_json(file_path)`: Safely parses JSON files into Python dictionaries.

---

## 11. Execution & Reproduction Workflow

### 11.1 Python Environment Setup
```bash
# Recommended Python 3.11 with CUDA-enabled PyTorch
conda create -n torch-gpu python=3.11 -y
conda activate torch-gpu

# Core dependencies
pip install torch torchvision transformers scikit-learn imbalanced-learn joblib pandas numpy pillow matplotlib seaborn tqdm gradio nbconvert
```

### 11.2 End-to-End Execution Sequence
1. **Feature Extraction:**
   Run `experiment/code/1.1_vit-face_demogpairs.ipynb`, `1.1_vit-emotion_demogpairs.ipynb`, and `1.1_vit-age_demogpairs.ipynb` sequentially. This saves `demogpairs_vit-*.pkl` files in `features/`.
2. **Model Training & GridSearch:**
   Run the desired classifier notebooks:
   - SVM: `2.1.1` through `2.1.7`
   - Gaussian NB: `2.2.1` through `2.2.7`
   - Random Forest: `2.4.1` through `2.4.7`
   - Logistic Regression: `2.5.1` through `2.5.7`
   Each notebook automatically saves the best fitted model to `models/` and metrics to `results/`.
3. **Cross-Model Comparison & Leaderboard:**
   Run `3.0_compare.ipynb` to aggregate all 28 JSON result files into a sorted master leaderboard.
4. **Interactive Web Demo:**
   Execute `python experiment/code/app.py` to start the Gradio interface at `http://127.0.0.1:7860`.

### 11.3 Quick Code Snippet: Loading and Running SOTA SVM Model
```python
import sys
import numpy as np
import joblib
sys.path.append('experiment/code')
import utils as u

# 1. Load Pre-extracted Features
face_feats = u.load_object('experiment/code/features/demogpairs_vit-face.pkl')
emotion_feats = u.load_object('experiment/code/features/demogpairs_vit-emotion.pkl')
age_feats = u.load_object('experiment/code/features/demogpairs_vit-age.pkl')

# 2. Concatenate Tri-Domain Feature for a sample image path
sample_path = '14th_dalai_lama/0043_01.jpg'
f_face = face_feats[sample_path]
f_emotion = emotion_feats[sample_path]
f_age = age_feats[sample_path]
tri_feature = np.concatenate([f_face, f_emotion, f_age]).reshape(1, -1)  # Shape: (1, 2304)

# 3. Load Trained SOTA Model
model, elapsed_time = u.load_object('experiment/code/models/clf_demogpairs_svm_vit-face-emotion-age_SVC.pkl')

# 4. Predict
pred_idx = model.predict(tri_feature)[0]
pred_label = u.DEMOGPairs_IDX_TO_LABEL[pred_idx]
print(f'Predicted Class Index: {pred_idx} -> Label: {pred_label}')
```

---

## 12. Scientific Claim Boundaries & Academic Writing Rules

When writing, editing, or evaluating paper drafts, outlines, or reports related to this project, any AI agent **MUST** strictly adhere to the following rules:

### 12.1 Language & Heading Rules
- **Headings & Subheadings:** Must be strictly in **English Title Case** (e.g., `# I. Introduction`, `## A. Dataset`, `## B. Vision Transformer`).
- **Narrative Body Text:** Written in formal **Bahasa Indonesia**, while preserving standard international academic and technical terms in **English** (e.g., *feature extraction*, *cross-validation*, *grid search*, *held-out test set*, *one-vs-rest*, *support vector classifier*).
- **Classifier Terminology Standardization:** Standardize on **Support Vector Classifier (SVC)** (consistent with scikit-learn `sklearn.svm.SVC`) throughout the manuscript.
- **First-Mention Acronym Rule:** Technical terms with standard acronyms (e.g., *Vision Transformer* (ViT), *Support Vector Classifier* (SVC), *Random Forest* (RF), *Gaussian Naive Bayes* (GNB), *Logistic Regression* (LR), *Principal Component Analysis* (PCA), *Multi-Head Self-Attention* (MHSA)) **MUST** be written in full with their acronym on first mention in the abstract or introduction. Subsequently, use only the acronym (ViT, SVC, RF, GNB, LR, PCA, MHSA).
- **Paragraph Length Discipline:** Standard paragraphs should be calibrated to **100-150 words** (with Related Works specifically at **100-115 words**) as specified in `paper_outline.md`, except for designated special paragraphs (Intro P3 [150-275 words], Intro P5 [150-250 words], Intro P6 [200-250 words], Intro P7 [75-100 words], and Abstract [150-200 words]).
- **Citation Density:** Maximum of 3 citations per sentence to prevent citation dumping.

### 12.2 Mathematical & Typographical Constraints
- **NO Em Dash Characters:** The long em dash (`—`) is **strictly forbidden**. Use a standard hyphen (`-`), parentheses `( )`, or commas `,`.
- **Plain Text for Simple Arithmetic:** Do not use LaTeX math mode for basic numbers, dimensions, arithmetic, and ranges:
  - Use `224 × 224` (NOT `$224 \times 224$`)
  - Use `768 + 768 + 768 = 2304` (NOT `$768+768+768=2304$`)
  - Use `80/20 split` (NOT `$80/20$`)
  - Use `±5%` (NOT `$\pm 5\%$`)
- **Math Mode Exclusivity:** Reserve LaTeX formulas (`$...$` and `$$...$$`) strictly for symbolic algebra, vectors, matrices, and formal mathematical definitions.
- **No Orphan Elements:** Every figure, table, equation, algorithm, and reference cited must be explicitly introduced and elaborated in the accompanying narrative text.

### 12.3 Scientific Claim Boundaries & Academic Rigor (25 Directives)
1. **No Subject Identity Discussion:** Do not discuss identity-level split, identity leakage, subject identity, or identity-aware split. Focus strictly on intersectional race and gender classification.
2. **Cautious Data Leakage Formulation:** Do not claim absolute "zero data leakage"; use "the preprocessing and cross-validation pipeline was designed to prevent information leakage."
3. **Balanced Evaluation Setting:** A balanced dataset does not imply demographic bias has been eliminated; refer to it as a "balanced evaluation setting" or "balanced class distribution across subgroups."
4. **No "Significantly" Without Statistical Tests:** Do not use the word "significantly" in the absence of statistical hypothesis testing; use "substantially", "considerably", "notably", or "achieved higher performance."
5. **Accurate Tri-Domain Scope:** Tri-domain fusion was top-performing on 3 of the 4 classifiers (SVC, LR, GNB); Random Forest achieved its highest performance on dual-domain `Emotion ⊕ Face`.
6. **Complementary Age Features:** Refer to Age features as providing "complementary informational contribution" or "additional discriminative information", not "orthogonal contribution".
7. **Hypothesis-Driven RF Drop Interpretation:** Present the drop in RF performance on 2,304 dimensions as a potential interpretation ("may reflect the difficulty of partitioning a higher-dimensional feature space using randomized splits").
8. **Empirical vs Theoretical Separation:** Strictly separate empirical findings (actual experimental figures) from conceptual interpretations.
9. **No State-of-the-Art Hyperbole:** Use "highest performance among the compared studies" or "outperformed the compared baselines on DemogPairs".
10. **Demographic Generalization Scope:** Explicitly limit scope to the 3 macro-racial groups represented in DemogPairs (Asian, Black, White).
11. **AI Ethics Statement:** Formulated for academic benchmarking and algorithmic fairness research; public surveillance deployment requires human-in-the-loop oversight and ethical governance.
12. **Equation (4) CLS Token Definition:** `z_L^0` in `f_domain = LN(z_L^0)` refers specifically to the CLS token representation from the **final encoder layer L** of the ViT backbone. This must be stated explicitly when first introducing Eq. (4).
13. **ViT Embedding as Task-Associated Representations:** Do not claim that ViT embeddings are exclusive or universal feature characterizations. Use "task-associated representations" as the preferred framing.
14. **Corrected Disparity Values:** The confirmed disparity values from the experiment logs are: SVC ΔF1 = **0.0440** (0.9614 - 0.9174), SVC ΔPrecision = **0.0310**, SVC ΔRecall = **0.0750**, SVC ΔOvR Acc = **1.39 pp**; LR ΔF1 = **0.0422** (0.9558 - 0.9136), LR ΔPrecision = **0.0495** (0.9571 - 0.9076), LR ΔRecall = **0.0500** (0.9611 - 0.9111), LR ΔOvR Acc = **1.39 pp**.
15. **Table XI Restructured (Two Parts):** Table XI (Subgroup Performance) must be presented in two blocks: (a) subgroup-level performance per classifier on tri-domain configuration, and (b) disparity summary comparing ΔRecall, ΔPrecision, ΔF1, ΔOvR across classifiers.
16. **Range-Based Disparity Scope:** Explicitly note that range-based disparity (max - min) is a simple, interpretable indicator and does not constitute a comprehensive fairness audit.
17. **OvR Accuracy Context:** High OvR accuracy values are partially attributable to the 5:1 negative sample ratio in binary one-vs-rest evaluation; do not present OvR Accuracy as a sole or primary fairness indicator.
18. **No "State-of-the-Art" Without Benchmark:** Do not claim state-of-the-art without a comprehensive benchmark; the proposed framework was evaluated only on DemogPairs.
19. **Conclusion Must Reflect Actual Results:** Conclusions must state that tri-domain fusion achieved the highest performance on 3 of 4 classifiers. No "universal improvement" or "fairness fully resolved" claims are permitted.
20. **Full Numerical Consistency Check:** All tables, confusion matrices, per-subgroup metrics, and narrative text must be numerically consistent with source JSON result files in `experiment/code/results/`.
21. **Novelty Statement:** The novelty of this work is the combination of (a) tri-domain ViT feature fusion, (b) comparative 4-classifier evaluation under unified GridSearchCV, (c) SVC hyperparameter optimization, and (d) subgroup disparity analysis on an intersectional benchmark.
22. **RQ Alignment:** Every research conclusion must be backed by a table, figure, or experiment result. Do not assert findings without an explicit evidential anchor.
23. **Final Terminology/Notation/Number Consistency:** Before finalizing any section, verify that all acronyms, configuration names (using ⊕ symbol), equation references (Eq. 1-19), and numerical values are consistent throughout the entire document.
24. **Hupont & Fernández (IEEE FG 2019):** This is the seminal DemogPairs paper and serves as the baseline dataset citation. It is NOT included in the main direct-comparison performance table (Table XII), but should be cited when introducing the DemogPairs dataset.
25. **Universal Manuscript Pipeline SOP (`WORKFLOW.md`):** All drafting, translation, and publication workflows must strictly follow `WORKFLOW.md` as the official standard operating procedure for generating modular Markdown drafts (`paper/`), Indonesian LaTeX (`paper_latex_id/`), and English submission-ready LaTeX manuscripts (`paper_latex_en/`) from `paper_outline.md`. Each stage must strictly maintain 100% numerical consistency, exact formula definitions, and 1-to-1 modular mapping across all target formats.

---

## 13. Key Authors, Provenance & Citation Metadata

### 13.1 Research Team & Affiliations
All authors are affiliated with the **Department of Informatics, Faculty of Informatics, Universitas Negeri Surabaya (UNESA), Surabaya, East Java, Indonesia**:

1. **Dr. Ir. Ricky Eka Putra, S.Kom., M.Kom.** ([ORCID: 0000-0002-5515-7967](https://orcid.org/0000-0002-5515-7967)) - Corresponding Author (`rickyeka@unesa.ac.id`)
2. **Rezky Arisanti Putri, S.Kom., M.Kom.** ([ORCID: 0009-0000-8021-1833](https://orcid.org/0009-0000-8021-1833))
3. **Dr. Yuni Yamasari, S.Kom., M.Kom.** ([ORCID: 0000-0001-9719-3491](https://orcid.org/0000-0001-9719-3491))
4. **Rafy Aulia Akbar, S.Kom., M.Kom.** ([ORCID: 0009-0003-6991-0694](https://orcid.org/0009-0003-6991-0694))

### 13.2 BibTeX Citations

```bibtex
@article{putra2026multidomain,
  title={Multi-Domain Vision Transformer Fusion for Intersectional Demographic Classification from Facial Images},
  author={Putra, Ricky Eka and Putri, Rezky Arisanti and Yamasari, Yuni and Akbar, Rafy Aulia},
  journal={IEEE Access},
  year={2026}
}

@inproceedings{putri2025dual,
  title={Dual Vision Transformer Integration for Race and Gender Recognition Based on Facial Images},
  author={Putri, Rezky Arisanti and Anifah, Lilik and Putra, Ricky Eka and Yamasari, Yuni and Akbar, Rafy Aulia},
  booktitle={2025 8th International Conference on Vocational Education and Electrical Engineering (ICVEE)},
  pages={1--6},
  year={2025},
  organization={IEEE}
}

@article{putri2025mdvit,
  title={MD-ViT: Multidomain Vision Transformer Fusion for Fair Demographic Attribute Recognition},
  author={Putri, Rezky Arisanti and Putra, Ricky Eka and Yamasari, Yuni},
  journal={Journal of Information Engineering and Educational Technology (JIEET)},
  volume={9},
  number={2},
  pages={64--79},
  year={2025}
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
