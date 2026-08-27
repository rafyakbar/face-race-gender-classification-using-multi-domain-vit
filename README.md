# Tri-Domain ViT + SVM: Face Race & Gender Classification via Cross-Domain Feature Fusion

> [!TIP]
> Intersectional 6-class (3 Race x 2 Gender) classification on face images using feature concatenation from three domain-specific Vision Transformers (Identity, Emotion, Age) with optimized SVM classifier. Achieves **93.70% accuracy** on DemogPairs benchmark.

## Overview

This research implements a **Cross-Domain Multi-Feature Fusion** framework for classifying race and gender simultaneously (intersectional classification) from face images. Instead of training a single end-to-end model, we leverage three pre-trained ViT-Base models as **offline feature extractors** from complementary facial domains, concatenate their representations, and classify with an optimally tuned Support Vector Machine.

### Why Multi-Domain Fusion?

Single-domain features have inherent limitations:

- **ViT-Face** captures biometric structure (jaw, nose, eye spacing) but is sensitive to age and expression variations.
- **ViT-Emotion** captures facial micro-dynamics (action units, muscle contractions) useful for gender cues but can be noisy.
- **ViT-Age** captures skin texture and aging morphology but lacks strong identity discriminators alone.

Concatenating all three (768 + 768 + 768 = **2,304 dimensions**) creates a complementary representation that outperforms any individual or dual combination.

## Features

- **Tri-Domain ViT Feature Fusion**: Identity + Emotion + Age representations from three HuggingFace models
- **Ablation Study**: Systematic evaluation of 7 configurations (3 single-domain, 3 dual-domain, 1 tri-domain)
- **SVM Hyperparameter Optimization**: 288 combinations via GridSearchCV with 5-fold stratified cross-validation
- **Intersectional Fairness Analysis**: Per-class metrics across all 6 demographic subgroups
- **DemogPairs Benchmark**: 10,800 perfectly balanced face images (1,800 per class)
- **Gradio Demo App**: Interactive web interface for real-time prediction

## Results Summary

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
> **Best Model**: Tri-Domain (vit-face-emotion-age) with SVC (kernel=`poly`, degree=2, C=10, gamma=`scale`), no PCA, no scaling. CV ROC-AUC: 0.9948.

## Project Structure

```
face-race-gender-multi-vit/
├── experiment/
│   ├── 00_overview.md              # Research framework overview
│   ├── 01_prepare-data.md          # Dataset preparation & splitting
│   ├── 02_preprocessing.md         # Image & feature-level preprocessing
│   ├── 03_feature-extraction.md    # Multi-domain ViT feature extraction
│   ├── 04_methods.md               # SVM classification & GridSearch
│   ├── 05_results.md               # Comparative analysis & fairness
│   ├── dataset_demogpairs.md       # DemogPairs dataset specification
│   └── code/
│       ├── 1.0_ftvit-age_*.ipynb   # Fine-tuned ViT extraction (age)
│       ├── 1.1_vit-*_*.ipynb       # ViT feature extraction (face/emotion/age)
│       ├── 2.1.*_svm_vit-*_*.ipynb # SVM training per configuration (7 notebooks)
│       ├── 3.0_compare.ipynb       # Comparative analysis across models
│       ├── 4.1_test.ipynb          # Final evaluation & confusion matrix
│       ├── app.py                  # Gradio demo application
│       ├── utils.py / utilsv2.py   # Shared utility functions
│       ├── dataset/demogpairs/     # Dataset (metadata + images)
│       ├── features/               # Extracted feature .pkl files
│       ├── models/                 # Trained SVM .pkl models
│       └── results/                # Evaluation results (.json)
├── related_works/
│   ├── literature_matrix.md        # Structured matrix of 10 related papers
│   ├── gap_analysis.md             # 8 research gaps (G1-G8) & 4 priorities (P1-P4)
│   ├── sintesis_literatur.md       # Literature synthesis hub
│   ├── tren_analisis.md            # Knowledge mapping & trend analysis
│   ├── summaries/                  # Per-paper summaries
│   ├── pdf/                        # Paper PDFs
│   └── bib/                        # BibTeX references
├── references/                     # Primary reference (DemogPairs paper)
├── prompts.txt                     # Research prompts/workflow log
└── scopus_query.txt                # Scopus search query for literature
```

## Prerequisites

- **Python** 3.10+
- **GPU** with CUDA support (RTX 4060 or equivalent recommended)
- **Conda** environment (recommended)

### Required Packages

```
torch>=2.0
transformers>=4.30
scikit-learn>=1.3
imbalanced-learn>=0.11
huggingface-hub
joblib
pandas
numpy
opencv-python
pillow
matplotlib
seaborn
gradio
umap-learn
jupyter
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
   pip install torch transformers scikit-learn imbalanced-learn joblib pandas numpy opencv-python pillow matplotlib seaborn gradio
   ```

3. **Prepare dataset**

   Place the DemogPairs dataset under `experiment/code/dataset/demogpairs/` with the following structure:

   ```
   dataset/demogpairs/
   ├── metadata/
   │   ├── Asian_Females.txt
   │   ├── Asian_Males.txt
   │   ├── Black_Females.txt
   │   ├── Black_Males.txt
   │   ├── White_Females.txt
   │   └── White_Males.txt
   └── images/
       └── <identity_folders>/
   ```

4. **Extract features** (offline, one-time)

   Run notebooks `1.1_vit-face_demogpairs.ipynb`, `1.1_vit-emotion_demogpairs.ipynb`, and `1.1_vit-age_demogpairs.ipynb` to generate `.pkl` feature files (~4.5 hours total on GPU).

5. **Train classifier**

   Run notebooks `2.1.1` through `2.1.7` for each feature configuration. Each performs GridSearchCV (288 combinations x 5-fold CV) and saves the best model.

6. **Compare and evaluate**

   Run `3.0_compare.ipynb` for comparative analysis, then `4.1_test.ipynb` for detailed evaluation on the held-out test set.

## Feature Extractors

| Extractor | HuggingFace Model | Domain | Output | Size |
|---|---|---|:---:|:---:|
| ViT-Face | `skutaada/VIT-VGGFace` | Face Identity | 768-d [CLS] | 29.37 MB |
| ViT-Emotion | `dima806/facial_emotions_image_detection` | Facial Emotion | 768-d [CLS] | 29.36 MB |
| ViT-Age | `dima806/facial_age_image_detection` | Facial Age | 768-d [CLS] | 29.36 MB |

All models use ViT-Base architecture (12 layers, 12 heads, 768 hidden dim, patch 16x16).

## Classification Pipeline

```
Input Features (2,304-d)
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
│  SVC (C=10, poly, degree=2, gamma=scale)    │
│  GridSearchCV: 288 combos x 5-fold CV       │
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

## Interactive Demo

A Gradio web app is included for real-time prediction:

```bash
cd experiment/code
python app.py
```

Upload a face image and the model will predict the intersectional race-gender class with confidence scores across all 6 categories.

## Per-Class Performance (Best Model)

| Class | Precision | Recall | F1-Score | OvR Accuracy |
|---|:---:|:---:|:---:|:---:|
| Black_Males | 0.9549 | 0.9417 | 0.9483 | 98.29% |
| White_Females | 0.9241 | 0.9472 | 0.9355 | 97.82% |
| Asian_Males | 0.9239 | 0.9444 | 0.9341 | 97.78% |
| White_Males | 0.9536 | 0.9694 | 0.9614 | 98.70% |
| Black_Females | 0.9415 | 0.8944 | 0.9174 | 97.31% |
| Asian_Females | 0.9250 | 0.9250 | 0.9250 | 97.50% |
| **Macro Avg** | **0.9372** | **0.9370** | **0.9369** | **97.90%** |

## Related Work

This project builds upon and extends two precursor studies by the same research group:

1. **Dual-ViT (Face + Emotion) + SVM** - Putri et al., IEEE ICVEE 2025 (92.41%)
2. **MD-ViT (Face + Age) + XGBoost** - Putri et al., JIEET 2025 (89.07%)

The full literature synthesis covers 10 papers (2022-2025) across the fields of face race/gender classification, Vision Transformer fairness, and multi-domain feature fusion. See `related_works/` for the complete literature matrix, gap analysis, and trend analysis.

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

## License

This research project is for academic purposes. The DemogPairs dataset is subject to its original license terms.
