# Face Race & Gender Classification using Multi-Domain ViT

> [!TIP]
> Intersectional 6-class (3 Race × 2 Gender) classification on face images using feature concatenation from three domain-specific Vision Transformers (Identity, Emotion, Age) with multiple optimized classifiers. Best result: **93.70% accuracy** (SVM, tri-domain) on DemogPairs benchmark.

## Overview

This research implements a **Cross-Domain Multi-Feature Fusion** framework for classifying race and gender simultaneously (intersectional classification) from face images. Instead of training a single end-to-end model, we leverage three pre-trained ViT-Base models as **offline feature extractors** from complementary facial domains, concatenate their representations, and compare multiple classical classifiers.

### Why Multi-Domain Fusion?

Single-domain features have inherent limitations:

- **ViT-Face** captures biometric structure (jaw, nose, eye spacing) but is sensitive to age and expression variations.
- **ViT-Emotion** captures facial micro-dynamics (action units, muscle contractions) useful for gender cues but can be noisy.
- **ViT-Age** captures skin texture and aging morphology but lacks strong identity discriminators alone.

Concatenating all three (768 + 768 + 768 = **2,304 dimensions**) creates a complementary representation that outperforms any individual or dual combination across all classifiers.

## Features

- **Tri-Domain ViT Feature Fusion**: Identity + Emotion + Age representations from three HuggingFace models
- **Ablation Study**: Systematic evaluation of 7 configurations (3 single-domain, 3 dual-domain, 1 tri-domain)
- **Multi-Classifier Comparison**: SVM, Logistic Regression, Random Forest, Gaussian Naive Bayes
- **Hyperparameter Optimization**: GridSearchCV with 5-fold stratified cross-validation per classifier
- **Intersectional Fairness Analysis**: Per-class OvR metrics across all 6 demographic subgroups (with confusion matrix as text array + image)
- **DemogPairs Benchmark**: 10,800 perfectly balanced face images (1,800 per class)
- **Self-Contained Reports**: 28 Markdown reports under `experiment/code/reports/` for AI-agent readability

## Classifier Comparison (Tri-Domain, 2,304-d)

| Rank | Classifier | Best Accuracy | Best F1 | Combinations | Status |
|:---:|---|:---:|:---:|:---:|---|
| 1 | **SVM** | **93.70%** | **0.9369** | 288 | ✅ |
| 2 | **Logistic Regression** | **92.73%** | **0.9273** | 270 | ✅ |
| 3 | **Random Forest** | **86.85%** | **0.8682** | 288 | ✅ |
| 4 | **Gaussian Naive Bayes** | **85.05%** | **0.8505** | 240 | ✅ |

> [!NOTE]
> XGBoost was removed — `pip` build has no CUDA support (`No visible GPU is found`) and CPU training was ~70 hours estimated. CUDA ≥12.9 is required for GPU acceleration, while the environment provides CUDA 12.6.

## Results Summary: SVM (288 combos)

| Configuration | Dimensions | Accuracy | F1-Score |
|---|:---:|:---:|:---:|
| vit-age (single) | 768 | 87.64% | 0.8765 |
| vit-emotion (single) | 768 | 90.19% | 0.9017 |
| vit-face (single) | 768 | 90.83% | 0.9083 |
| vit-emotion-age (dual) | 1,536 | 92.08% | 0.9209 |
| vit-face-age (dual) | 1,536 | 92.55% | 0.9254 |
| vit-emotion-face (dual) | 1,536 | 93.29% | 0.9329 |
| **vit-face-emotion-age (tri)** | **2,304** | **93.70%** | **0.9369** |

> **Best SVM**: Tri-Domain with `SVC(C=10, kernel=poly, degree=2, gamma=scale, tol=0.001, probability=True)`, no PCA, no scaler.

## Results Summary: Logistic Regression (270 combos)

| Configuration | Dimensions | Accuracy | F1-Score |
|---|:---:|:---:|:---:|
| vit-age (single) | 768 | 86.48% | 0.8648 |
| vit-emotion (single) | 768 | 88.47% | 0.8846 |
| vit-face (single) | 768 | 90.60% | 0.9059 |
| vit-emotion-age (dual) | 1,536 | 90.51% | 0.9051 |
| vit-face-age (dual) | 1,536 | 91.62% | 0.9162 |
| vit-emotion-face (dual) | 1,536 | 92.41% | 0.9240 |
| **vit-face-emotion-age (tri)** | **2,304** | **92.73%** | **0.9273** |

> **Best LR**: Tri-Domain with `LogisticRegression(C=0.1, solver=newton-cg, max_iter=500)`, no PCA, no scaler.

## Results Summary: Random Forest (288 combos)

| Configuration | Dimensions | Accuracy | F1-Score |
|---|:---:|:---:|:---:|
| vit-age (single) | 768 | 73.66% | 0.7354 |
| vit-emotion (single) | 768 | 80.60% | 0.8057 |
| vit-face (single) | 768 | 85.46% | 0.8539 |
| vit-emotion-age (dual) | 1,536 | 81.11% | 0.8108 |
| vit-face-age (dual) | 1,536 | 85.79% | 0.8573 |
| vit-emotion-face (dual) | 1,536 | 86.85% | 0.8682 |
| **vit-face-emotion-age (tri)** | **2,304** | **86.20%** | **0.8613** |

> **Best RF**: `vit-emotion-face` with `RandomForestClassifier(n_estimators=200, max_depth=None, max_features=sqrt, min_samples_leaf=1, min_samples_split=5)` + PCA, no scaler — 86.85% (tri-domain follows at 86.20%).

## Results Summary: Gaussian Naive Bayes (240 combos)

| Configuration | Dimensions | Accuracy | F1-Score |
|---|:---:|:---:|:---:|
| vit-age (single) | 768 | 69.63% | 0.6952 |
| vit-emotion (single) | 768 | 73.38% | 0.7329 |
| vit-face (single) | 768 | 82.69% | 0.8258 |
| vit-emotion-age (dual) | 1,536 | 76.81% | 0.7681 |
| vit-face-age (dual) | 1,536 | 83.15% | 0.8317 |
| vit-emotion-face (dual) | 1,536 | 84.86% | 0.8481 |
| **vit-face-emotion-age (tri)** | **2,304** | **85.05%** | **0.8505** |

## Full Leaderboard (28 Experiments)

| Rank | Classifier | Features | Accuracy | F1 |
|:---:|---|---|:---:|:---:|
| 1 | SVM | vit-face-emotion-age | 93.70% | 0.9369 |
| 2 | SVM | vit-emotion-face | 93.29% | 0.9329 |
| 3 | LR | vit-face-emotion-age | 92.73% | 0.9273 |
| 4 | SVM | vit-face-age | 92.55% | 0.9254 |
| 5 | LR | vit-emotion-face | 92.41% | 0.9240 |
| 6 | SVM | vit-emotion-age | 92.08% | 0.9209 |
| 7 | LR | vit-face-age | 91.62% | 0.9162 |
| 8 | SVM | vit-face | 90.83% | 0.9083 |
| 9 | LR | vit-face | 90.60% | 0.9059 |
| 10 | LR | vit-emotion-age | 90.51% | 0.9051 |

See `experiment/code/reports/` for all 28 self-contained Markdown reports.

## Project Structure

```
face-race-gender-multi-vit/
├── experiment/
│   ├── 00_overview.md              # Research framework overview
│   ├── 01_prepare-data.md          # Dataset preparation & splitting
│   ├── 02_preprocessing.md         # Image & feature-level preprocessing
│   ├── 03_feature-extraction.md    # Multi-domain ViT feature extraction
│   ├── 04_methods.md               # Classification methods & GridSearch
│   ├── 05_results.md               # Comparative analysis & fairness
│   ├── dataset_demogpairs.md       # DemogPairs dataset specification
│   └── code/
│       ├── 1.1_vit-*_*.ipynb       # ViT feature extraction (face/emotion/age)
│       ├── 2.1.*_svm_vit-*_*.ipynb # SVM training (7 notebooks, 288 combos)
│       ├── 2.2.*_gnb_vit-*_*.ipynb # GNB training (7 notebooks, 240 combos)
│       ├── 2.4.*_rf_vit-*_*.ipynb  # Random Forest training (7 notebooks, 288 combos)
│       ├── 2.5.*_lr_vit-*_*.ipynb  # Logistic Regression training (7 notebooks, 270 combos)
│       ├── 3.0_compare.ipynb       # Comparative analysis (4 classifiers × 7 configs)
│       ├── 4.1_test.ipynb          # Final evaluation
│       ├── utils/                  # Utility package (project-agnostic)
│       │   ├── __init__.py         # re-exports
│       │   ├── constants.py        # DemogPairs labels
│       │   ├── dataset.py          # load_demogpairs()
│       │   ├── evaluation.py       # evaluate_models() — OvR Accuracy, CM text array
│       │   ├── extraction.py       # extract_vit_features()
│       │   ├── display.py          # Jupyter/terminal display helpers
│       │   ├── serialization.py    # save/load object & JSON
│       │   └── time_helpers.py     # seconds_to_time()
│       ├── reports/                # Self-contained Markdown reports (28 files)
│       │   ├── 2.1/ (SVM)
│       │   ├── 2.2/ (GNB)
│       │   ├── 2.4/ (RF)
│       │   └── 2.5/ (LR)
│       ├── images/                 # Confusion matrices (cm_{clf}_{feat}_{model}.png)
│       ├── dataset/demogpairs/     # Dataset (metadata + images)
│       ├── features/               # Extracted feature .pkl files
│       ├── models/                 # Trained models .pkl
│       └── results/                # Evaluation results .json (28 files)
├── related_works/                  # Literature review
├── references/                     # BibTeX references
└── README.md
```

## Prerequisites

- **Python** 3.10+
- **GPU** with CUDA support (RTX 4060 or equivalent recommended)

### Required Packages

```
torch>=2.0
transformers>=4.30
scikit-learn>=1.3
imbalanced-learn>=0.11
joblib
pandas
numpy
pillow
matplotlib
seaborn
tqdm
```

> XGBoost is intentionally omitted — GPU build requires CUDA ≥12.9.

## Quick Start

1. **Clone the repository**

   ```bash
   git clone https://github.com/rafyakbar/face-race-gender-classification-using-multi-domain-vit.git
   cd face-race-gender-classification-using-multi-domain-vit
   ```

2. **Set up environment**

   ```bash
   conda create -n facevit python=3.11
   conda activate facevit
   pip install torch transformers scikit-learn imbalanced-learn joblib pandas numpy pillow matplotlib seaborn tqdm
   ```

3. **Prepare dataset**

   Place the DemogPairs dataset under `experiment/code/dataset/demogpairs/`.

4. **Extract features** (offline, one-time)

   Run notebooks `1.1_vit-face_demogpairs.ipynb`, `1.1_vit-emotion_demogpairs.ipynb`, and `1.1_vit-age_demogpairs.ipynb`.

5. **Train classifiers**

   Run notebooks `2.1.*` (SVM, 288 combos), `2.2.*` (GNB, 240 combos), `2.4.*` (RF, 288 combos), or `2.5.*` (LR, 270 combos). Each saves `models/*.pkl`, `results/*.json`, `images/*.png`, and validation is via self-contained `reports/*.md`.

## Feature Extractors

| Extractor | HuggingFace Model | Domain | Output | Size |
|---|---|---|:---:|:---:|
| ViT-Face | `skutaada/VIT-VGGFace` | Face Identity | 768-d [CLS] | 29.37 MB |
| ViT-Emotion | `dima806/facial_emotions_image_detection` | Facial Emotion | 768-d [CLS] | 29.36 MB |
| ViT-Age | `dima806/facial_age_image_detection` | Facial Age | 768-d [CLS] | 29.36 MB |

All models use ViT-Base architecture (12 layers, 12 heads, 768 hidden dim, patch 16x16).

## Classification Pipeline

```
Input Features (768 / 1,536 / 2,304-d)
    │
    ▼
┌─────────────────────────┐
│  Scaler (None / MinMax) │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│  PCA (None / 50% / 75%) │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────────────────────────┐
│  Classifier (GridSearchCV + 5-Fold CV)      │
│  • SVM: 288 combos (C, kernel, gamma, degree)│
│  • GNB: 240 combos (var_smoothing)          │
│  • Random Forest: 288 combos (n_estimators, max_depth, max_features, ...)│
│  • Logistic Regression: 270 combos (C, solver, max_iter)│
└───────────┬─────────────────────────────────┘
            │
            ▼
   Predicted Demographic Class (0-5)
```

Per-class evaluation uses **One-vs-Rest (OvR) Accuracy** = `(TP+TN)/total` alongside Precision/Recall/F1, plus a confusion matrix text array for AI-agent readability.

## Dataset: DemogPairs

- **Paper**: Hupont & Fernandez (2019), FG 2019, DOI: `10.1109/FG.2019.8756625`
- **Total**: 10,800 face images (600 identities, 18 images each)
- **Balance**: Perfectly balanced across 6 intersectional classes
- **Split**: 80/20 stratified (8,640 train / 2,160 test, `random_state=42`)

| Class | Index | Race | Gender | Samples |
|---|:---:|---|:---:|:---:|
| Black_Males | 0 | Black | Male | 1,800 |
| White_Females | 1 | White | Female | 1,800 |
| Asian_Males | 2 | Asian | Male | 1,800 |
| White_Males | 3 | White | Male | 1,800 |
| Black_Females | 4 | Black | Female | 1,800 |
| Asian_Females | 5 | Asian | Female | 1,800 |

## Per-Class Performance (Best Model: SVM Tri-Domain, 93.70%)

| Class | Precision | Recall | F1-Score |
|---|:---:|:---:|:---:|
| Black_Males | 0.9549 | 0.9417 | 0.9483 |
| White_Females | 0.9241 | 0.9472 | 0.9355 |
| Asian_Males | 0.9239 | 0.9444 | 0.9341 |
| White_Males | 0.9536 | 0.9694 | 0.9614 |
| Black_Females | 0.9415 | 0.8944 | 0.9174 |
| Asian_Females | 0.9250 | 0.9250 | 0.9250 |
| **Macro Avg** | **0.9372** | **0.9370** | **0.9369** |

See `experiment/code/reports/2.1/2.1.7_svm_vit-face-emotion-age.md` for full details (confusion matrix, OvR Accuracy, CV folds).

## Citation

If you use this work, please cite the DemogPairs dataset:

```bibtex
@inproceedings{hupont2019demogpairs,
  title={DemogPairs: Quantifying the Impact of Demographic Imbalance in Deep Face Recognition},
  author={Hupont, Isabelle and Fernandez, Carles},
  booktitle={2019 14th IEEE International Conference on Automatic Face \& Gesture Recognition (FG 2019)},
  year={2019},
  doi={10.1109/FG.2019.8756625}
}
```
