# Face Race & Gender Classification using Multi-Domain ViT

> Intersectional 6-class (3 Race × 2 Gender) classification from facial images using offline feature fusion across three domain-specific Vision Transformers (Identity, Emotion, Age) with GridSearchCV-optimized classical classifiers. **Best accuracy: 93.70%** (SVM Tri-Domain on DemogPairs benchmark).

---

## 🌟 Key Results

| Rank | Classifier | Best Feature Config | Dimensions | Best Accuracy | Macro F1 | Status |
|:---:|---|---|:---:|:---:|:---:|:---:|
| 🥇 | **SVM** | **Tri-Domain (Face + Emotion + Age)** | **2,304** | **93.70%** | **0.9369** | ✅ |
| 🥈 | **Logistic Regression** | Tri-Domain (Face + Emotion + Age) | 2,304 | 92.73% | 0.9273 | ✅ |
| 🥉 | **Random Forest** | Dual-Domain (Emotion + Face) | 1,536 | 86.85% | 0.8682 | ✅ |
| 4 | **Gaussian Naive Bayes** | Tri-Domain (Face + Emotion + Age) | 2,304 | 85.05% | 0.8505 | ✅ |

### Per-Class Performance (SVM Tri-Domain, $N=2,160$ Test)

| Demographic Subgroup | Race | Gender | OvR Accuracy | Precision | Recall | F1-Score |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **White_Males** | White | Male | 98.70% | 0.9536 | 0.9694 | 0.9614 |
| **Black_Males** | Black | Male | 98.29% | 0.9549 | 0.9417 | 0.9483 |
| **White_Females** | White | Female | 97.82% | 0.9241 | 0.9472 | 0.9355 |
| **Asian_Males** | Asian | Male | 97.78% | 0.9239 | 0.9444 | 0.9341 |
| **Asian_Females** | Asian | Female | 97.50% | 0.9250 | 0.9250 | 0.9250 |
| **Black_Females** | Black | Female | 97.31% | 0.9415 | 0.8944 | 0.9174 |
| **Macro Average** | — | — | **97.90%** | **0.9372** | **0.9370** | **0.9369** |

---

## 🔬 Methodology

### 1. Multi-Domain Feature Extractors (768-d each)
- **ViT-Face** (`skutaada/VIT-VGGFace`): Biometric geometry & craniofacial structure.
- **ViT-Emotion** (`dima806/facial_emotions_image_detection`): Facial micro-expressions & dynamic action units.
- **ViT-Age** (`dima806/facial_age_image_detection`): Biological aging morphology & skin textures.

### 2. Pipeline & Optimization
```
Image (224×224) ──► 3× ViT Extractors ──► Concatenation (2,304-d)
                       │
                       ▼
    Pipeline: Scaler ──► PCA ──► Classifier (5-Fold Stratified CV)
    (28 Experiments: 7 Feature Ablations × 4 Classical Classifiers)
```

### 3. Dataset: DemogPairs
- **10,800 images** (600 identities × 18 images), perfectly balanced (1,800/class).
- **Split:** 80/20 stratified split (8,640 train / 2,160 test held-out).
- **6 Classes:** `Asian_Females`, `Asian_Males`, `Black_Females`, `Black_Males`, `White_Females`, `White_Males`.

---

## 📁 Repository Structure

```
├── experiment/
│   ├── 00_overview.md - 05_results.md  # Detailed research documentation
│   └── code/
│       ├── 1.1_vit-*_demogpairs.ipynb  # Feature extraction notebooks
│       ├── 2.1 - 2.5_*.ipynb           # Classifier training (SVM, GNB, RF, LR)
│       ├── 3.0_compare.ipynb           # Comprehensive leaderboard
│       ├── 4.0_test.ipynb              # Final evaluation & test pipeline
│       ├── app.py                      # Interactive Gradio demo app
│       ├── utils/                      # Modular utility package (<200 lines/module)
│       ├── md/                         # Notebook markdown exports (nbconvert)
│       └── images/                     # Confusion matrix plots
├── related_works/                      # Literature review, matrix & gap analysis
└── references/                         # BibTeX citation sources
```

---

## 🚀 Quick Start

### 1. Installation
```bash
conda create -n torch-gpu python=3.11 -y
conda activate torch-gpu
pip install torch transformers scikit-learn imbalanced-learn joblib pandas numpy pillow matplotlib seaborn tqdm gradio nbconvert
```

### 2. Workflow
1. **Extract Features:** Run `experiment/code/1.1_vit-*.ipynb` to generate `.pkl` embeddings in `features/`.
2. **Train Classifiers:** Run `2.1.*` (SVM), `2.2.*` (GNB), `2.4.*` (RF), or `2.5.*` (LR) for 5-Fold GridSearchCV tuning.
3. **Compare Results:** Run `3.0_compare.ipynb` or view `experiment/code/md/3.0_compare.md`.
4. **Interactive Demo:** Launch `python experiment/code/app.py` for web inference.

---

## 📜 Citation

```bibtex
@inproceedings{hupont2019demogpairs,
  title={DemogPairs: Quantifying the Impact of Demographic Imbalance in Deep Face Recognition},
  author={Hupont, Isabelle and Fernandez, Carles},
  booktitle={2019 14th IEEE International Conference on Automatic Face & Gesture Recognition (FG 2019)},
  year={2019},
  doi={10.1109/FG.2019.8756625}
}
```
