# Intersectional Face Race and Gender Classification via Tri-Domain Vision Transformer Feature Fusion

> **Abstract:** An empirical framework for intersectional 6-class (3 Race × 2 Gender) demographic classification from facial images using offline feature fusion across three domain-specific Vision Transformers (**Face Identity**, **Facial Emotion**, and **Facial Age**) combined with GridSearchCV-optimized classical machine learning pipelines. Achieving state-of-the-art **93.70% Test Accuracy** and **0.9369 Macro F1** on the balanced DemogPairs benchmark.

---

## 🌟 Key Experimental Results

### 1. Global Leaderboard Across Classifiers

| Rank | Classifier | Best Feature Configuration | Feature Dim | Best Accuracy | Macro Precision | Macro Recall | Macro F1 | Best Hyperparameters |
|:---:|---|---|:---:|:---:|:---:|:---:|:---:|---|
| 🥇 | **SVM** | **Tri-Domain (Face + Emotion + Age)** | **2,304** | **93.70%** | **0.9372** | **0.9370** | **0.9369** | C=10, kernel='poly', degree=2, gamma='scale', No Scaler, No PCA |
| 🥈 | **Logistic Regression** | Tri-Domain (Face + Emotion + Age) | 2,304 | **92.73%** | 0.9274 | 0.9273 | 0.9273 | C=10, solver='lbfgs', max_iter=200, No Scaler, No PCA |
| 🥉 | **Random Forest** | Dual-Domain (Emotion + Face) | 1,536 | **86.85%** | 0.8690 | 0.8685 | 0.8682 | n_estimators=200, max_depth=None, max_features='sqrt', No Scaler, No PCA |
| 4 | **Gaussian Naive Bayes** | Tri-Domain (Face + Emotion + Age) | 2,304 | **85.05%** | 0.8523 | 0.8505 | 0.8505 | var_smoothing=0.007017, MinMax Scaler, No PCA |

### 2. Intersectional Fairness Audit (SVM Tri-Domain, N = 2,160 Test Set)

| Demographic Subgroup | Race | Gender | OvR Accuracy | Precision | Recall | F1-Score | Support |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **White_Males** | White | Male | 98.70% | 0.9536 | 0.9694 | 0.9614 | 360 |
| **Black_Males** | Black | Male | 98.29% | 0.9549 | 0.9417 | 0.9483 | 360 |
| **White_Females** | White | Female | 97.82% | 0.9241 | 0.9472 | 0.9355 | 360 |
| **Asian_Males** | Asian | Male | 97.78% | 0.9239 | 0.9444 | 0.9341 | 360 |
| **Asian_Females** | Asian | Female | 97.50% | 0.9250 | 0.9250 | 0.9250 | 360 |
| **Black_Females** | Black | Female | 97.31% | 0.9415 | 0.8944 | 0.9174 | 360 |
| **Macro Average** | All | All | **97.90%** | **0.9372** | **0.9370** | **0.9369** | **2,160** |

> **Fairness Highlights:** The F1-Score across all 6 demographic subgroups is tightly bounded within **0.9174 to 0.9614** (disparity gap of only 0.0441), with One-vs-Rest accuracy reaching **97.31% to 98.70%**, proving that multi-domain fusion effectively mitigates demographic classification bias without performance trade-offs.

---

## 🔬 Methodology Framework

![Methodology Framework](images/method.png)

### 1. Multi-Domain Vision Transformer Extractors (768-d per domain)
- **ViT-Face** (`skutaada/VIT-VGGFace`): Captures static biometric geometry and craniofacial proportions.
- **ViT-Emotion** (`dima806/facial_emotions_image_detection`): Captures dynamic affective micro-expressions and facial action units.
- **ViT-Age** (`dima806/facial_age_image_detection`): Captures biological aging morphology and skin texture patterns.

### 2. Feature Fusion & Optimization Pipeline
- **One-Pass Offline Extraction:** High-level representations are extracted from the `[CLS]` token (768-d) of each frozen ViT-Base backbone.
- **7 Feature Ablation Schemes:** 3 Single-domain (768-d), 3 Dual-domain (1,536-d), and 1 Tri-domain (2,304-d).
- **GridSearchCV Tuning:** 5-Fold Stratified Cross-Validation evaluating 1,086 hyperparameter combinations (38,010 total fits) across 4 classical classifiers with modular Scaler and PCA preprocessing stages.

### 3. Benchmark Dataset: DemogPairs
- **Total Images:** 10,800 high-resolution facial images (600 unique identities × 18 images per subject).
- **Balance:** Perfectly balanced across 6 intersectional classes (1,800 images per class).
- **Partition:** 80/20 Stratified Split (8,640 train / 2,160 held-out test; `random_state=42`, `stratify=y`).
- **Classes (Alphabetical):** `Asian_Females`, `Asian_Males`, `Black_Females`, `Black_Males`, `White_Females`, `White_Males`.

---

## 📁 Repository Structure

```
.
├── experiment/
│   ├── 00_overview.md - 05_results.md  # Detailed experimental documentation & audit
│   └── code/
│       ├── 1.1_vit-*_demogpairs.ipynb  # Feature extraction notebooks
│       ├── 2.1 - 2.5_*.ipynb           # Classifier training (SVM, GNB, RF, LR)
│       ├── 3.0_compare.ipynb           # Comprehensive 28-experiment leaderboard
│       ├── 4.0_test.ipynb              # Final evaluation & test pipeline
│       ├── app.py                      # Interactive Gradio demo web application
│       ├── utils/                      # Modular utility package (<200 lines/module)
│       ├── md/                         # Notebook markdown exports (nbconvert)
│       └── images/                     # Confusion matrix plots
├── images/
│   ├── method.png                      # Methodology framework architecture diagram
│   └── method.pptx                     # Editable presentation source
├── paper_outline.md                    # Detailed paper outline for IEEE Access publication
├── rules/                              # Standardized Markdown, LaTeX, and IEEE citation rules
├── related_works/                      # Literature review, matrix & gap analysis (10 papers)
└── references/                         # BibTeX citation sources
```

---

## 🚀 Quick Start

### 1. Environment Setup
```bash
conda create -n torch-gpu python=3.11 -y
conda activate torch-gpu
pip install torch transformers scikit-learn imbalanced-learn joblib pandas numpy pillow matplotlib seaborn tqdm gradio nbconvert
```

### 2. Experimental Workflow
1. **Extract Embeddings:** Run `experiment/code/1.1_vit-*.ipynb` to generate `.pkl` latent embeddings in `features/`.
2. **Train Classifiers:** Run `2.1.*` (SVM), `2.2.*` (GNB), `2.4.*` (RF), or `2.5.*` (LR) for 5-Fold GridSearchCV tuning.
3. **Compare Results:** Run `3.0_compare.ipynb` or view `experiment/code/md/3.0_compare.md`.
4. **Interactive Demo:** Launch `python experiment/code/app.py` for real-time web inference.

---

## 👥 Research Team

- **Dr. Ir. Ricky Eka Putra, S.Kom., M.Kom.** ([ORCID](https://orcid.org/0000-0002-5515-7967)) - Corresponding Author (`rickyeka@unesa.ac.id`)
- **Rezky Arisanti Putri, S.Kom., M.Kom.** ([ORCID](https://orcid.org/0009-0000-8021-1833))
- **Dr. Yuni Yamasari, S.Kom., M.Kom.** ([ORCID](https://orcid.org/0000-0001-9719-3491))
- **Rafy Aulia Akbar, S.Kom., M.Kom.** ([ORCID](https://orcid.org/0009-0003-6991-0694))

*Department of Informatics, Faculty of Informatics, Universitas Negeri Surabaya, Surabaya, East Java, Indonesia.*

---

## 📜 Citation

If you find this research or codebase useful in your work, please cite:

```bibtex
@article{putra2026multidomain,
  title={Intersectional Face Race and Gender Classification via Tri-Domain Vision Transformer Feature Fusion and Optimized Support Vector Classifier},
  author={Putra, Ricky Eka and Putri, Rezky Arisanti and Yamasari, Yuni and Akbar, Rafy Aulia},
  journal={IEEE Access},
  year={2026}
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
