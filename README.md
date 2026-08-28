# Face Race & Gender Classification using Multi-Domain ViT

> [!TIP]
> Intersectional 6-class (3 Race x 2 Gender) classification on face images using feature concatenation from three domain-specific Vision Transformers (Identity, Emotion, Age) with multiple optimized classifiers. Best result: **93.70% accuracy** (SVM) on DemogPairs benchmark.

## Overview

This research implements a **Cross-Domain Multi-Feature Fusion** framework for classifying race and gender simultaneously (intersectional classification) from face images. Instead of training a single end-to-end model, we leverage three pre-trained ViT-Base models as **offline feature extractors** from complementary facial domains, concatenate their representations, and compare multiple classifiers.

### Why Multi-Domain Fusion?

Single-domain features have inherent limitations:

- **ViT-Face** captures biometric structure (jaw, nose, eye spacing) but is sensitive to age and expression variations.
- **ViT-Emotion** captures facial micro-dynamics (action units, muscle contractions) useful for gender cues but can be noisy.
- **ViT-Age** captures skin texture and aging morphology but lacks strong identity discriminators alone.

Concatenating all three (768 + 768 + 768 = **2,304 dimensions**) creates a complementary representation that outperforms any individual or dual combination.

## Features

- **Tri-Domain ViT Feature Fusion**: Identity + Emotion + Age representations from three HuggingFace models
- **Ablation Study**: Systematic evaluation of 7 configurations (3 single-domain, 3 dual-domain, 1 tri-domain)
- **Multi-Classifier Comparison**: SVM, Gaussian Naive Bayes, XGBoost, Random Forest
- **Hyperparameter Optimization**: GridSearchCV with 5-fold stratified cross-validation per classifier
- **Intersectional Fairness Analysis**: Per-class metrics across all 6 demographic subgroups
- **DemogPairs Benchmark**: 10,800 perfectly balanced face images (1,800 per class)

## Classifier Comparison

| Classifier | Best Accuracy | Best F1 | Kombinasi | Status |
|---|:---:|:---:|:---:|---|
| **SVM** | **93.70%** | **0.9369** | 288 | ✅ Selesai |
| GNB | 85.05% | 0.8505 | 240 | ✅ Selesai |
| XGBoost | - | - | 288 | ⏳ Menunggu |
| Random Forest | - | - | 288 | ⏳ Sedang berjalan |

## Results Summary: SVM

| Configuration | Dimensions | Accuracy | F1-Score |
|---|:---:|:---:|:---:|
| vit-age (single) | 768 | 87.64% | 0.8765 |
| vit-emotion (single) | 768 | 90.19% | 0.9017 |
| vit-face (single) | 768 | 90.83% | 0.9083 |
| vit-emotion-age (dual) | 1,536 | 92.08% | 0.9209 |
| vit-face-age (dual) | 1,536 | 92.55% | 0.9254 |
| vit-emotion-face (dual) | 1,536 | 93.29% | 0.9329 |
| **vit-face-emotion-age (tri)** | **2,304** | **93.70%** | **0.9369** |

> [!IMPORTANT]
> **Best SVM Model**: Tri-Domain (vit-face-emotion-age) with SVC (kernel=`poly`, degree=2, C=10, gamma=`scale`), no PCA, no scaling.

## Results Summary: GNB

| Configuration | Dimensions | Accuracy | F1-Score |
|---|:---:|:---:|:---:|
| vit-age (single) | 768 | 81.44% | 0.8127 |
| vit-emotion (single) | 768 | 83.80% | 0.8373 |
| vit-face (single) | 768 | 82.69% | 0.8258 |
| vit-emotion-age (dual) | 1,536 | 83.84% | 0.8379 |
| vit-face-age (dual) | 1,536 | 83.47% | 0.8340 |
| vit-emotion-face (dual) | 1,536 | 84.86% | 0.8481 |
| **vit-face-emotion-age (tri)** | **2,304** | **85.05%** | **0.8505** |

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
│       ├── 1.0_ftvit-age_*.ipynb   # Fine-tuned ViT extraction (age)
│       ├── 1.1_vit-*_*.ipynb       # ViT feature extraction (face/emotion/age)
│       ├── 2.1.*_svm_vit-*_*.ipynb # SVM training (7 notebooks)
│       ├── 2.2.*_gnb_vit-*_*.ipynb # GNB training (7 notebooks)
│       ├── 2.3.*_xgb_vit-*_*.ipynb # XGBoost training (7 notebooks)
│       ├── 2.4.*_rf_vit-*_*.ipynb  # Random Forest training (7 notebooks)
│       ├── 3.0_compare.ipynb       # Comparative analysis
│       ├── 4.1_test.ipynb          # Final evaluation
│       ├── app.py                  # Gradio demo app
│       ├── utils/                  # Utility package
│       │   ├── __init__.py
│       │   ├── constants.py
│       │   ├── dataset.py
│       │   ├── evaluation.py
│       │   ├── extraction.py
│       │   ├── display.py
│       │   ├── serialization.py
│       │   └── time_helpers.py
│       ├── reports/                # Experiment results (markdown)
│       ├── images/                 # Confusion matrices
│       ├── dataset/demogpairs/     # Dataset (metadata + images)
│       ├── features/               # Extracted feature .pkl files
│       ├── models/                 # Trained models .pkl
│       └── results/                # Evaluation results .json
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
xgboost
joblib
pandas
numpy
pillow
matplotlib
seaborn
gradio
tqdm
```

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
   pip install torch transformers scikit-learn imbalanced-learn xgboost joblib pandas numpy pillow matplotlib seaborn gradio tqdm
   ```

3. **Prepare dataset**

   Place the DemogPairs dataset under `experiment/code/dataset/demogpairs/`.

4. **Extract features** (offline, one-time)

   Run notebooks `1.1_vit-face_demogpairs.ipynb`, `1.1_vit-emotion_demogpairs.ipynb`, and `1.1_vit-age_demogpairs.ipynb`.

5. **Train classifiers**

   Run notebooks `2.1.*` (SVM), `2.2.*` (GNB), `2.3.*` (XGBoost), or `2.4.*` (RF).

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
│  • SVM: 288 combos                          │
│  • GNB: 240 combos                          │
│  • XGBoost: 288 combos                      │
│  • Random Forest: 288 combos                 │
└───────────┬─────────────────────────────────┘
            │
            ▼
   Predicted Demographic Class (0-5)
```

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

## Per-Class Performance (Best SVM Model)

| Class | Precision | Recall | F1-Score |
|---|:---:|:---:|:---:|
| Black_Males | 0.9549 | 0.9417 | 0.9483 |
| White_Females | 0.9241 | 0.9472 | 0.9355 |
| Asian_Males | 0.9239 | 0.9444 | 0.9341 |
| White_Males | 0.9536 | 0.9694 | 0.9614 |
| Black_Females | 0.9415 | 0.8944 | 0.9174 |
| Asian_Females | 0.9250 | 0.9250 | 0.9250 |
| **Macro Avg** | **0.9372** | **0.9370** | **0.9369** |

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
