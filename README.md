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

- **Tri-Domain ViT Feature Fusion**: Identity + Emotion + Age representations from three HuggingFace models (ViT-Base, 768-d [CLS] each)
- **Ablation Study**: 7 configurations systematically (vit-face, vit-emotion, vit-age, 3 duals, 1 tri)
- **Multi-Classifier Comparison**: SVM (288 combos), Logistic Regression (270), Random Forest (288), Gaussian Naive Bayes (240) — total 28 experiments, 5-fold Stratified CV each
- **Hyperparameter Optimization**: GridSearchCV with `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)`, scoring `accuracy/f1_macro/precision_macro/recall_macro`, `refit='accuracy'`, `n_jobs=int(cpu_count*0.6)`
- **Intersectional Fairness Analysis**: Per-class OvR Accuracy, Precision/Recall/F1 per subgroup + confusion matrix (text array for AI + PNG image)
- **DemogPairs Benchmark**: 10,800 perfectly balanced face images (1,800 per class), 80/20 stratified split
- **Notebook-to-Markdown Exports**: 28 notebooks + `3.0_compare.ipynb` converted via `nbconvert` (`MarkdownExporter`) to `experiment/code/md/` for documentation without running Jupyter
- **Reproducible Utilities**: `utils/` package (constants, dataset, extraction, evaluation, display, serialization, time_helpers) — project-agnostic, threshold <200 lines per module

## Classifier Comparison (Tri-Domain, 2,304-d)

| Rank | Classifier | Best Accuracy | Best F1 | Combinations | Status |
|:---:|---|:---:|:---:|:---:|---|
| 1 | **SVM** | **93.70%** | **0.9369** | 288 | ✅ |
| 2 | **Logistic Regression** | **92.73%** | **0.9273** | 270 | ✅ |
| 3 | **Random Forest** | **86.85%** | **0.8682** | 288 | ✅ |
| 4 | **Gaussian Naive Bayes** | **85.05%** | **0.8505** | 240 | ✅ |

> [!NOTE]
> XGBoost was removed — `pip` build has no CUDA support (`No visible GPU is found`) and CPU training was ~70 hours estimated. CUDA ≥12.9 is required for GPU acceleration, while the environment provides CUDA 12.6 (RTX 4060 Laptop, `torch 2.10.0+cu126`).

**Key finding:** Tri-domain wins for SVM/LR/GNB; RF best is dual `vit-emotion-face` (86.85%) with tri close behind (86.20%).

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
│       ├── 3.0_compare.ipynb       # Comparative analysis (populated, 28 results)
│       ├── 4.0_test.ipynb          # Final evaluation (executed, CUDA)
│       ├── utils/                  # Utility package (project-agnostic, <200 lines/mod)
│       │   ├── __init__.py         # re-exports demogpairs_classes, evaluate_models, ...
│       │   ├── constants.py        # DemogPairs labels & mappings
│       │   ├── dataset.py          # load_demogpairs()
│       │   ├── evaluation.py       # evaluate_models() — OvR Accuracy, CM text array, HTML img
│       │   ├── extraction.py       # extract_vit_features()
│       │   ├── display.py          # printhtml, display_table, IS_NOTEBOOK
│       │   ├── serialization.py    # save/load object & JSON
│       │   └── time_helpers.py     # seconds_to_time()
│       ├── md/                     # Notebook Markdown exports (nbconvert, 29 files)
│       │   ├── svm/ (7)            # 2.1.1–2.1.7
│       │   ├── gnb/ (7)            # 2.2.1–2.2.7
│       │   ├── rf/ (7)             # 2.4.1–2.4.7
│       │   ├── lr/ (7)             # 2.5.1–2.5.7
│       │   └── 3.0_compare.md
│       ├── images/                 # Confusion matrices (cm_{clf}_{feat}_{model}.png, 28 images)
│       ├── dataset/demogpairs/     # Dataset (metadata + images, gitignored images/)
│       ├── features/               # Extracted feature .pkl files (768/1536/2304-d, gitignored)
│       ├── models/                 # Trained models .pkl (gitignored)
│       └── results/                # Evaluation results .json (28 files, best_params, metrics)
├── related_works/                  # Literature review
├── references/                     # BibTeX references
└── README.md
```

> `reports/` was removed — replaced by `md/` (nbconvert exports). See `experiment/code/md/` for Markdown without running Jupyter.

## Prerequisites

- **Python** 3.10+ (tested 3.11, conda `torch-gpu`)
- **GPU** with CUDA support (RTX 4060 Laptop or equivalent, CUDA 12.6, `torch 2.10.0+cu126` verified)

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
nbconvert>=7  # for notebook -> Markdown exports
```

> XGBoost intentionally omitted (GPU requires CUDA ≥12.9). `gradio` optional for `app.py`.

## Quick Start

1. **Clone the repository**

   ```bash
   git clone https://github.com/rafyakbar/face-race-gender-classification-using-multi-domain-vit.git
   cd face-race-gender-classification-using-multi-domain-vit
   ```

2. **Set up environment**

   ```bash
   conda create -n torch-gpu python=3.11
   conda activate torch-gpu
   pip install torch transformers scikit-learn imbalanced-learn joblib pandas numpy pillow matplotlib seaborn tqdm nbconvert
   ```

3. **Prepare dataset**

   Place the DemogPairs dataset under `experiment/code/dataset/demogpairs/` (see `dataset_demogpairs.md`).

4. **Extract features** (offline, one-time, ~2304-d)

   Run notebooks `1.1_vit-face_demogpairs.ipynb`, `1.1_vit-emotion_demogpairs.ipynb`, `1.1_vit-age_demogpairs.ipynb`. Each saves `features/demogpairs_vit-*.pkl`.

5. **Train classifiers** (GridSearchCV, 5-fold)

   Run notebooks `2.1.*` (SVM, 288 combos), `2.2.*` (GNB, 240), `2.4.*` (RF, 288), or `2.5.*` (LR, 270). Each saves `models/*.pkl`, `results/*.json` (best_params, accuracy, per-class), `images/*.png` (confusion matrix). For Markdown reports without Jupyter, see `md/` (nbconvert exports) or re-export:
   ```bash
   pip install nbconvert
   jupyter nbconvert --to markdown notebook.ipynb
   # or via Python:
   # from nbconvert import MarkdownExporter; import nbformat
   ```

6. **Compare**

   Run `3.0_compare.ipynb` (populated, 28 rows) or read `md/3.0_compare.md` for leaderboard.

## Feature Extractors

| Extractor | HuggingFace Model | Domain | Output | Size |
|---|---|---|:---:|:---:|
| ViT-Face | `skutaada/VIT-VGGFace` | Face Identity | 768-d [CLS] | 29.37 MB |
| ViT-Emotion | `dima806/facial_emotions_image_detection` | Facial Emotion | 768-d [CLS] | 29.36 MB |
| ViT-Age | `dima806/facial_age_image_detection` | Facial Age | 768-d [CLS] | 29.36 MB |

All models use ViT-Base architecture (12 layers, 12 heads, 768 hidden dim, patch 16×16). Features are concatenated per image in alfabet order. CM images without title, evaluation with explicit `labels` alignment.

## Classification Pipeline

```
Input Features (768 / 1,536 / 2,304-d)
    │
    ▼
┌─────────────────────────┐
│  Scaler (None / MinMax) │  ← GridSearchCV
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│  PCA (None / 50% / 75%) │  ← 0.5 / 0.75 variance retained
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────────────────────────┐
│  Classifier (GridSearchCV + 5-Fold CV)      │
│  • SVM: 288 combos (C, kernel, gamma, degree, tol, prob)│
│  • GNB: 240 combos (var_smoothing logspace -9..2)│
│  • Random Forest: 288 combos (n_estimators, max_depth, max_features, min_samples_split/leaf)│
│  • Logistic Regression: 270 combos (C, solver, max_iter)│
│  Scoring: accuracy, f1_macro, precision_macro, recall_macro; refit='accuracy'│
└───────────┬─────────────────────────────────┘
            │
            ▼
   Predicted Demographic Class (0-5)
   + per-class OvR Accuracy = (TP+TN)/total (one-vs-rest)
   + confusion matrix text array (AI-readable) + PNG image
```

**Scoring note:** `roc_auc_ovr` removed (GNB incompatible). Evaluation via `utils/evaluation.py`: `classification_report(target_names, digits=4)`, `_compute_class_metrics` (OvR), `confusion_matrix` with `target_names` labels, saved as `images/cm_{stem}.png` + printed text array.

## Dataset: DemogPairs

- **Paper**: Hupont & Fernandez (2019), FG 2019, DOI: `10.1109/FG.2019.8756625`
- **Total**: 10,800 face images (600 identities, 18 images each)
- **Balance**: Perfectly balanced across 6 intersectional classes
- **Split**: 80/20 stratified (8,640 train / 2,160 test, `random_state=42`, `stratify=y`)

| Class | Index | Race | Gender | Samples |
|---|:---:|---|:---:|:---:|
| Black_Males | 0 | Black | Male | 1,800 |
| White_Females | 1 | White | Female | 1,800 |
| Asian_Males | 2 | Asian | Male | 1,800 |
| White_Males | 3 | White | Male | 1,800 |
| Black_Females | 4 | Black | Female | 1,800 |
| Asian_Females | 5 | Asian | Female | 1,800 |

Supports `label` (string) and `label_idx` (int) as used in `utils/dataset.py`.

## Per-Class Performance (Best Model: SVM Tri-Domain, 93.70%, N=2160 test)

| Class | Precision | Recall | F1-Score | Support |
|---|:---:|:---:|:---:|:---:|
| Asian_Females | 0.9250 | 0.9250 | 0.9250 | 360 |
| Asian_Males | 0.9239 | 0.9444 | 0.9341 | 360 |
| Black_Females | 0.9415 | 0.8944 | 0.9174 | 360 |
| Black_Males | 0.9549 | 0.9417 | 0.9483 | 360 |
| White_Females | 0.9241 | 0.9472 | 0.9355 | 360 |
| White_Males | 0.9536 | 0.9694 | 0.9614 | 360 |
| **Macro Avg** | **0.9372** | **0.9370** | **0.9369** | **2160** |

Order alfabet `Asian_Females, Asian_Males, Black_Females, Black_Males, White_Females, White_Males` selaras `DEMOGPairs_CLASSES` dengan `labels` eksplisit di `evaluation.py`. OvR Accuracy per kelas lebih tinggi, CM tanpa title di `images/cm_*.png`. See `md/svm/2.1.7_svm_vit-face-emotion-age.md` atau `results/demogpairs_svm_vit-face-emotion-age_SVC.json`.

## Notebook-to-Markdown Exports

All 28 training notebooks + `3.0_compare.ipynb` are exported to Markdown for reading without Jupyter:

```bash
pip install nbconvert
jupyter nbconvert --to markdown notebook.ipynb          # CLI
# Python:
from nbconvert import MarkdownExporter
import nbformat
with open("notebook.ipynb") as f: nb = nbformat.read(f, as_version=4)
body, _ = MarkdownExporter().from_notebook_node(nb)
open("notebook.md", "w", encoding="utf-8").write(body)
```

Outputs: `experiment/code/md/svm|gnb|rf|lr/2.x_*.md` (29 files, ~27–30KB each). The former `reports/` folder (self-contained reports) was removed in favor of these direct exports.

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
