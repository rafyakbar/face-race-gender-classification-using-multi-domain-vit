# Multi-Domain Vision Transformer Fusion for Intersectional Demographic Classification from Facial Images

> **Abstract:** An empirical framework for intersectional 6-class (3 Race × 2 Gender) demographic classification from facial images using offline feature fusion across three task-associated Vision Transformer (ViT) representations (**Face Biometrics**, **Facial Emotion**, and **Facial Age**) combined with GridSearchCV-optimized classical machine learning pipelines. The proposed Tri-Domain ViT + Support Vector Classifier (SVC) achieves **93.70% Test Accuracy** and **0.9369 F1-Score** on the balanced DemogPairs benchmark ($N = 2,160$ held-out test samples), outperforming single-domain and dual-domain baselines.

---

## 🌟 Key Experimental Results

### 1. Global Benchmark Leaderboard across Classifiers

Evaluated on the held-out test set ($N = 2,160$) following 5-Fold Stratified Cross-Validation tuning ($N = 8,640$ train set):

| Rank | Classifier | Best Feature Configuration | Feature Dim | Best Accuracy | Precision | Recall | F1-Score | Best Hyperparameters |
|:---:|---|---|:---:|:---:|:---:|:---:|:---:|---|
| 🥇 | **Support Vector Classifier (SVC)** | **Tri-Domain (`Face ⊕ Emotion ⊕ Age`)** | **2,304** | **93.70%** | **0.9372** | **0.9370** | **0.9369** | `C=10, kernel='poly', degree=2, gamma='scale', pca=None, scaler=None` |
| 🥈 | **Logistic Regression (LR)** | Tri-Domain (`Face ⊕ Emotion ⊕ Age`) | 2,304 | **92.73%** | 0.9275 | 0.9273 | 0.9273 | `C=0.1, solver='newton-cg', max_iter=500, pca=None, scaler=None` |
| 🥉 | **Random Forest (RF)** | Dual-Domain (`Emotion ⊕ Face`) | 1,536 | **86.85%** | 0.8689 | 0.8685 | 0.8682 | `n_estimators=200, max_depth=None, max_features='sqrt', min_samples_split=5, min_samples_leaf=1, pca=PCA(0.75), scaler=None` |
| 4 | **Gaussian Naive Bayes (GNB)** | Tri-Domain (`Face ⊕ Emotion ⊕ Age`) | 2,304 | **85.05%** | 0.8512 | 0.8505 | 0.8505 | `var_smoothing=5.8780e-03, pca=PCA(0.75), scaler=None` |

> **Key Takeaway:** Tri-domain feature fusion yields the highest performance across **3 of the 4 evaluated classifiers** (SVC, LR, GNB). Random Forest achieves its empirical peak on the dual-domain `Emotion ⊕ Face` configuration (86.85% vs. 86.20% on tri-domain).

---

### 2. Intersectional Subgroup Performance & Disparity Profile

#### (a) Subgroup-Level Metrics for Best-Performing Model: SVC Tri-Domain (`Face ⊕ Emotion ⊕ Age`)

| Demographic Subgroup | Race | Gender | OvR Accuracy | Precision | Recall | F1-Score | Support |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **White_Males** | White | Male | 98.70% | 0.9536 | 0.9694 | 0.9614 | 360 |
| **Black_Males** | Black | Male | 98.29% | 0.9549 | 0.9417 | 0.9483 | 360 |
| **White_Females** | White | Female | 97.82% | 0.9241 | 0.9472 | 0.9355 | 360 |
| **Asian_Males** | Asian | Male | 97.78% | 0.9239 | 0.9444 | 0.9341 | 360 |
| **Asian_Females** | Asian | Female | 97.50% | 0.9250 | 0.9250 | 0.9250 | 360 |
| **Black_Females** | Black | Female | 97.31% | 0.9415 | 0.8944 | 0.9174 | 360 |
| **Macro Average** | All | All | **97.90%** | **0.9372** | **0.9370** | **0.9369** | **2,160** |

#### (b) Subgroup Disparity Summary ($\max - \min$) across Tri-Domain Classifiers

| Classifier | $\Delta_{\text{Recall}}$ | $\Delta_{\text{Precision}}$ | $\Delta_{\text{F1}}$ | $\Delta_{\text{OvR Acc}}$ |
|---|:---:|:---:|:---:|:---:|
| **SVC (Tri-Domain: `Face ⊕ Emotion ⊕ Age`)** | 0.0750 | 0.0310 | 0.0440 | 1.39 pp |
| **LR (Tri-Domain: `Face ⊕ Emotion ⊕ Age`)** | 0.0500 | 0.0495 | 0.0422 | 1.39 pp |

> **Audit Note:** All 6 demographic subgroups achieve an F1-Score above **0.91** on the proposed SVC Tri-Domain model (range: **0.9174 to 0.9614**; $\Delta\text{F1} = 0.0440$). Range-based disparity ($\max - \min$) is reported as a descriptive indicator of cross-subgroup performance variation and does not replace a comprehensive algorithmic fairness audit.

---

### 3. Comparison with Prior Studies on the DemogPairs Dataset

| Study | Model Architecture | Accuracy | Precision | Recall | F1-Score |
|---|---|:---:|:---:|:---:|:---:|
| Putri et al. (JIEET 2025) | MD-ViT + XGBoost | 89.07% | 0.8912 | 0.8907 | 0.8901 |
| Putri et al. (ICVEE 2025) | Dual-ViT + SVM | 92.41% | 0.9248 | 0.9241 | 0.9238 |
| **Proposed Framework** | **Tri-Domain ViT + SVC** | **93.70%** | **0.9372** | **0.9370** | **0.9369** |

---

## 🔬 Methodology Framework

```
                          [ Input Facial Image: 224x224 RGB ]
                                           │
         ┌─────────────────────────────────┼─────────────────────────────────┐
         ▼                                 ▼                                 ▼
   [ ViT-Face ]                     [ ViT-Emotion ]                    [ ViT-Age ]
(skutaada/VIT-VGGFace)        (dima806/facial_emotions...)        (dima806/facial_age...)
   [CLS] Token 768-d                 [CLS] Token 768-d                 [CLS] Token 768-d
         │                                 │                                 │
         └─────────────────────────────────┼─────────────────────────────────┘
                                           ▼
                    [ Feature Concatenation: z_tri in R^2304 ]
                                           │
                                           ▼
                  [ Preprocessing Pipeline: Scaler + PCA (Fold-level) ]
                                           │
                                           ▼
                   [ 5-Fold Stratified Cross-Validation GridSearchCV ]
                     (SVC / Logistic Regression / Random Forest / GNB)
                                           │
                                           ▼
                 [ Intersectional 6-Class Classification on DemogPairs ]
           (Asian_Females, Asian_Males, Black_Females, Black_Males, White_Females, White_Males)
```

### 1. Multi-Domain Vision Transformer Extractors (768-d per domain)
- **ViT-Face** (`skutaada/VIT-VGGFace`): Pretrained on facial biometrics; captures static craniofacial geometry and facial identity proportions.
- **ViT-Emotion** (`dima806/facial_emotions_image_detection`): Pretrained on facial affect; captures dynamic expression cues and localized action units.
- **ViT-Age** (`dima806/facial_age_image_detection`): Pretrained on facial age estimation; captures biological aging morphology and skin texture variations.

### 2. Feature Fusion & Optimization Pipeline
- **Offline Representation Extraction:** High-level representations are extracted from the normalized `[CLS]` token ($\mathbf{z}_L^0 \in \mathbb{R}^{768}$) of the final encoder layer of each frozen ViT-Base backbone.
- **7 Systematic Ablation Schemes:**
  - *Single-Domain (768-d):* `Face`, `Emotion`, `Age`
  - *Dual-Domain (1,536-d):* `Emotion ⊕ Face`, `Face ⊕ Age`, `Emotion ⊕ Age`
  - *Tri-Domain (2,304-d):* `Face ⊕ Emotion ⊕ Age`
- **Leakage-Free Cross-Validation:** Preprocessing transformations (MinMaxScaler and PCA) are fitted strictly on training folds within `scikit-learn.pipeline.Pipeline` objects to prevent data leakage.
- **Grid Search Space:** Evaluated a total of 1,086 parameter combinations ($38,010$ total cross-validation fits across 7 feature configurations and 4 classifier families).

### 3. Benchmark Dataset: DemogPairs
- **Total Images:** 10,800 facial images (600 unique identities × 18 images per subject).
- **Subgroup Balance:** Perfectly balanced across 6 intersectional classes (1,800 images per class).
- **Partition:** 80/20 Stratified Split (8,640 train / 2,160 held-out test; `random_state=42`, `stratify=y`).
- **Demographic Subgroups:** `Asian_Females`, `Asian_Males`, `Black_Females`, `Black_Males`, `White_Females`, `White_Males`.

---

## 📁 Repository Structure

```
.
├── experiment/                            # Experimental logs, documentation, and source code
│   ├── 00_overview.md - 05_results.md     # Comprehensive experimental logs and methodology audits
│   ├── dataset_demogpairs.md              # Dataset specification and partition summary
│   └── code/
│       ├── 1.1_vit-*_demogpairs.ipynb     # Feature extraction scripts (Face, Emotion, Age)
│       ├── 2.1.* - 2.5.*.ipynb            # Classifier training notebooks (SVC, GNB, RF, LR)
│       ├── 3.0_compare.ipynb              # Global 28-model comparison and benchmarking
│       ├── 4.0_test.ipynb                 # Held-out evaluation and test routines
│       ├── app.py                         # Interactive Gradio demo web application
│       ├── utils/                         # Modular utility library
│       │   ├── constants.py               # Class names, mappings, and seed definitions
│       │   ├── dataset.py                 # Dataset loaders and metadata processors
│       │   ├── display.py                 # Visual display and tabular helpers
│       │   ├── evaluation.py              # Cross-validation, metrics, and disparity calculations
│       │   ├── extraction.py              # ViT [CLS] feature extractor
│       │   ├── serialization.py           # Joblib & JSON loaders/savers
│       │   └── time_helpers.py            # Execution duration trackers
│       ├── dataset/demogpairs/metadata/   # 6 metadata .txt files (1,800 rows each)
│       ├── md/                            # Markdown exports of all Jupyter notebooks
│       ├── results/                       # Raw JSON result files (28 experiment artifacts)
│       └── images/                        # Confusion matrix plots (28 models)
├── images/                                # High-resolution architecture diagrams and sample figures
├── paper/                                 # Modular manuscript draft in Markdown (IEEE style)
│   ├── 00_abstract.md                  # Title, authors, abstract, and IEEE keywords
│   ├── 01_introduction.md              # Section I: Introduction
│   ├── 02_related-works.md              # Section II: Related Works
│   ├── 03_materials-and-methods_*.md   # Section III: Methodology (0-overview, a-dataset s.d. i-ethical)
│   ├── 04_results-and-discussion_*.md  # Section IV: Results and Discussion (a-global s.d. f-prior-studies)
│   ├── 05_conclusion.md                # Section V: Conclusion
│   ├── 06_references.md                # Section VI: References
│   ├── 07_biographies.md               # Section VII: Biographies
│   ├── acronyms.txt                    # Centralized acronym registry (Rule 1.3)
│   └── images/                         # Self-contained local image assets for paper compilation
├── references/                            # BibTeX citation sources (DemogPairs)
├── related_works/                         # Literature reviews, summary matrices, and gap analysis
│   ├── bib/                               # BibTeX files for 10 mandatory literature papers
│   ├── pdf/                               # Full-text PDFs of related studies
│   ├── summaries/                         # Structured analytical summaries per paper
│   ├── gap_analysis.md                    # Research gap identification
│   ├── literature_matrix.md               # Comparative literature matrix
│   ├── sintesis_literatur.md              # Thematic literature synthesis
│   └── tren_analisis.md                   # Chronological and methodological trend analysis
├── rules/                                 # Standardized rules for formatting, LaTeX, and citations
│   ├── IEEE_citation_guidelines.md        # IEEE citation and bibliography guidelines
│   ├── latex_rules.txt                    # LaTeX conversion rules and templates
│   └── md_rules.txt                       # Strict Markdown drafting rules and checklist
├── folder_structure.txt                   # Complete project directory tree and file glossary
├── paper_outline.md                       # Complete publication outline & paragraph targets
├── prompts.txt                            # Chronological log of experimental prompts and instructions
├── README.AI.md                           # Master AI agent operational guide and ground-truth index
├── README.md                              # Public research documentation
├── scopus_query.txt                       # Scopus literature search query strings
└── WORKFLOW.md                            # Standard Operating Procedure (SOP) for manuscript pipeline
```

### Overview of Core Documentation & Manuscript Pipeline

| Document | Description & Role |
|---|---|
| [`WORKFLOW.md`](WORKFLOW.md) | **Standard Operating Procedure (SOP):** Universal 4-stage research manuscript pipeline (`Outline` &rarr; `paper/` &rarr; `paper_latex_id/` &rarr; `paper_latex_en/`) |
| [`README.AI.md`](README.AI.md) | Master AI agent operational guide, ground-truth audit index, and academic writing rules |
| [`paper_outline.md`](paper_outline.md) | Master architectural blueprint for IEEE Access publication, word limits, and notation definitions |
| [`folder_structure.txt`](folder_structure.txt) | Complete directory tree diagram and comprehensive functional glossary of all folders/files |
| [`paper/`](paper/) | Modular publication draft in Markdown conforming strictly to IEEE publication standards |
| [`rules/md_rules.txt`](rules/md_rules.txt) | Strict Markdown drafting rules (word count bounds, acronym tracking, interactive links, no forbidden words) |
| [`experiment/00_overview.md`](experiment/00_overview.md) | Comprehensive experimental logs, 28-model leaderboard audit, and dataset partition details |

---

## 🚀 Quick Start

### 1. Environment Setup
```bash
conda create -n torch-gpu python=3.11 -y
conda activate torch-gpu
pip install torch torchvision transformers scikit-learn imbalanced-learn joblib pandas numpy pillow matplotlib seaborn tqdm gradio nbconvert
```

### 2. Experimental Execution Workflow
1. **Extract Embeddings:** Run `experiment/code/1.1_vit-*.ipynb` to generate `.pkl` latent embeddings in `features/`.
2. **Train Classifiers:** Run `2.1.*` (SVC), `2.2.*` (GNB), `2.4.*` (RF), or `2.5.*` (LR) for 5-Fold GridSearchCV tuning.
3. **Compare Results:** Run `3.0_compare.ipynb` or review [`experiment/code/md/3.0_compare.md`](experiment/code/md/3.0_compare.md).
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
  title={Multi-Domain Vision Transformer Fusion for Intersectional Demographic Classification from Facial Images},
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

