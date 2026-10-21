# Master AI Agent Reference Guide: Intersectional Face Race & Gender Classification via Multi-Domain Vision Transformer Feature Fusion

> **Critical Notice to AI Agents:** This file (`README.AI.md`) is the authoritative, self-contained single source of truth and comprehensive operational manual for this research repository. Any AI agent entering this project should read this document to understand the full context, research background, model architecture, dataset, feature extraction protocols, 28-model experimental benchmark, official IEEE Access peer review dossier, submission compliance artifacts, codebase utilities, reproduction workflows, and scientific writing rules without needing to explore or reconstruct context from disparate files.

---

## 📑 Table of Contents

1. [Executive Summary & Manuscript Identity](#1-executive-summary--manuscript-identity)
2. [Current Publication Journey & Peer Review Dossier (`paper_reviews_ieee/`)](#2-current-publication-journey--peer-review-dossier-paper_reviews_ieee)
3. [Research Architecture & Methodological Pipeline](#3-research-architecture--methodological-pipeline)
4. [Dataset Specifications, Label Encodings & Partitioning Protocol](#4-dataset-specifications-label-encodings--partitioning-protocol)
5. [Feature Extraction & 7 Ablation Schemes](#5-feature-extraction--7-ablation-schemes)
6. [Classical Classifier Pipeline & Exhaustive GridSearchCV Optimization](#6-classical-classifier-pipeline--exhaustive-gridsearchcv-optimization)
7. [Comprehensive Experimental Benchmark (Definitive 28-Model Leaderboard)](#7-comprehensive-experimental-benchmark-definitive-28-model-leaderboard)
8. [Intersectional Subgroup Performance, Confusion Matrix & Error Dynamics](#8-intersectional-subgroup-performance-confusion-matrix--error-dynamics)
9. [Comparison with Prior Studies on DemogPairs & Contextual Literature](#9-comparison-with-prior-studies-on-demogpairs--contextual-literature)
10. [Repository Architecture & File Inventory](#10-repository-architecture--file-inventory)
11. [Submission Compliance & Packaging (`paper_submission/` & `upload/`)](#11-submission-compliance--packaging-paper_submission--upload)
12. [Internal Mock Peer Review Suite (`paper_reviews/`) & Agent Skills (`.agents/skills/`)](#12-internal-mock-peer-review-suite-paper_reviews--agent-skills-agentsskills)
13. [Python Utilities Library Reference (`experiment/code/utils/`)](#13-python-utilities-library-reference-experimentcodeutils)
14. [Execution, Reproduction & Manuscript Compilation Workflows](#14-execution-reproduction--manuscript-compilation-workflows)
15. [Scientific Claim Boundaries & Academic Writing Constraints (27 Directives)](#15-scientific-claim-boundaries--academic-writing-constraints-27-directives)
16. [Key Authors, Academic Provenance & Citation Metadata](#16-key-authors-academic-provenance--citation-metadata)

---

## 1. Executive Summary & Manuscript Identity

### 1.1 Core Metadata
- **Repository Title / Working Directory:** `face-race-gender-classification-using-multi-domain-vit` (`D:\Research\face-race-gender-classification-using-multi-domain-vit`)
- **Primary Corpus Authors:** Dr. Ir. Ricky Eka Putra, S.Kom., M.Kom. (Corresponding Author, `rickyeka@unesa.ac.id`), Rezky Arisanti Putri, S.Kom., M.Kom., Dr. Yuni Yamasari, S.Kom., M.Kom., Rafy Aulia Akbar, S.Kom., M.Kom.
- **Affiliation:** Department of Informatics, Faculty of Informatics, Universitas Negeri Surabaya (UNESA), Surabaya, East Java, Indonesia.
- **Target Journal:** **IEEE Access** (Open Access, Q1, Impact Factor: 3.4).
- **Official Manuscript Tracking ID:** **`Access-2026-50857`**.
- **Manuscript Title:** *Multi-Domain Vision Transformer Fusion for Intersectional Demographic Classification from Facial Images*.
- **Current Milestone:** Editorial Decision Received on **October 20, 2026** (Binary Review Outcome: Reject & Resubmit with 1 resubmission opportunity allowed).

### 1.2 Core Research Paradigm
The study proposes an offline feature fusion framework for 6-class intersectional demographic classification (3 Races × 2 Genders: Asian/Black/White × Female/Male) from facial images. The system extracts task-associated latent representations from three frozen, specialized pre-trained Vision Transformer (ViT-Base) backbones:
1. **ViT-Face** (`skutaada/VIT-VGGFace`): Captures static craniofacial biometrics and identity-related spatial geometry.
2. **ViT-Emotion** (`dima806/facial_emotions_image_detection`): Captures dynamic affective expressions and localized facial action units.
3. **ViT-Age** (`dima806/facial_age_image_detection`): Captures biological aging morphology and epidermal texture patterns.

High-level `[CLS]` token vectors (768-d per domain) are concatenated into a **Tri-Domain representation** ($\mathbf{z}_{\text{tri}} \in \mathbb{R}^{2304}$) and fed into downstream classical classifiers optimized through exhaustive 5-Fold Stratified GridSearchCV (evaluating 1,086 hyperparameter combinations and 38,010 total cross-validation fits across 4 classifier families: SVM, Logistic Regression, Random Forest, and Gaussian Naive Bayes).

### 1.3 Key Benchmark Achievements
- **Top-Performing Configuration:** **Support Vector Machine (SVM) + Tri-Domain ViT Fusion** (`vit-face-emotion-age`, 2,304-d)
  - **Test Accuracy:** **93.70%** (2,024 correct out of 2,160 held-out test samples).
  - **Macro Precision:** **0.9372**
  - **Macro Recall:** **0.9370**
  - **Macro F1-Score:** **0.9369**
  - **Best Hyperparameters:** $C = 10$, kernel = `'poly'`, degree = 2, gamma = `'scale'`, Scaler = `None`, PCA = `None`.
- **Global Classifier Hierarchy (Average Accuracy across all 7 feature schemes):**
  $$\text{SVM } (91.47\%) > \text{Logistic Regression } (90.40\%) > \text{Random Forest } (82.81\%) > \text{Gaussian Naive Bayes } (79.37\%)$$
- **Ablation Trend:** Tri-domain fusion yields peak accuracy on 3 of the 4 classifiers (SVM: 93.70%, LR: 92.73%, GNB: 85.05%). Random Forest peaks on dual-domain `Emotion ⊕ Face` (86.85% vs. 86.20% on tri-domain).
- **Subgroup Fairness Profile:** Subgroup F1-scores range from **0.9174 to 0.9614** ($\Delta_{\text{F1}} = 0.0440$), with OvR Accuracy from **97.31% to 98.70%**.

---

## 2. Current Publication Journey & Peer Review Dossier (`paper_reviews_ieee/`)

The manuscript was formally submitted to IEEE Access and received an official editorial decision letter on October 20, 2026. The peer review dossier is curated in [`paper_reviews_ieee/`](paper_reviews_ieee/).

### 2.1 Editorial Decision Overview
- **Associate Editor:** Dr. Vincenzo Conti (`vincenzo.conti@unikore.it`, `vinc.conti@gmail.com`).
- **Article Administrator:** Mr. Adesh Choudhary (`adesh.choudhary@ieee.org`).
- **Decision Date:** 20-10-2026.
- **Decision Type:** Rejected under IEEE Access's binary peer review model, with an explicit invitation to resubmit as a revised manuscript.
- **Resubmission Opportunity:** Exactly **ONE** opportunity to resubmit is permitted. If unresolved concerns remain, the manuscript is definitively rejected.
- **Resubmission Portal URL:** [IEEE Author Portal Resubmission Board](https://ieee.atyponrex.com/journal/ieee-access).

### 2.2 Curated Files in `paper_reviews_ieee/`
All relevant files have been converted into clean, standardized Markdown:

| File | Path | Role & Content |
|---|---|---|
| **Editorial Decision & Reviews** | [`IEEE-Access_Decision-on-Manuscript-ID-Access-2026-50857.md`](paper_reviews_ieee/IEEE-Access_Decision-on-Manuscript-ID-Access-2026-50857.md) | Official decision letter, submission link, required 3 files, Reviewer 1 (7 comments) & Reviewer 2 (10 comments) with questionnaires. |
| **Response to Reviewers Template** | [`IEEE-Access_Response-to-Reviewers-template.md`](paper_reviews_ieee/IEEE-Access_Response-to-Reviewers-template.md) | Standard IEEE Access response structure: point-by-point reviewer concerns, author responses, and author actions taken. |
| **Request for Byline Change** | [`Request-for-Byline-Change.md`](paper_reviews_ieee/Request-for-Byline-Change.md) | Official form and detailed justification required if the author list/order changes between original and revised submissions. |
| **Resubmission Checklist** | [`Resubmission-Checklist.md`](paper_reviews_ieee/Resubmission-Checklist.md) | 10-point compliance checklist: reviewer responses, grammar tools/discounts, math formulas, references, highlighted PDF, and main files. |

### 2.3 Detailed Deconstruction of Reviewer Comments

#### Reviewer 1 (Acceptable with Revisions; 7 Core Comments)
1. **Introduction Length:** Section I is overly lengthy; needs to be tightened and summarized.
2. **Related Works & Equations:** Section II requires better structuring and inclusion of formal mathematical formulations/equations.
3. **Figure 3 Redesign:** ViT diagram in Figure 3 needs redesigning and clearer explanation to show methodological novelty and enhance visual clarity.
4. **Figure 4 Discussion:** Visual data graph in Figure 4 needs deeper and more rigorous discussion in the narrative.
5. **Experimental & Dataset Details + Time Cost:** Provide more granular detail on the dataset, articulate specific contributions, and report execution time costs.
6. **Broader Method Comparisons:** Compare proposed framework against additional baseline methods to validate empirical contributions.
7. **Conclusion Section:** Revise Section V to reflect the actual contributions more effectively and concisely.
- *Questionnaire Answers:* Reviewed all files (Yes), Contributes to knowledge (Yes), Technically sound (Yes), Comprehensive presentation (Yes), References applicable (Yes), Inappropriate references (No).

#### Reviewer 2 (Substantial Methodological & Statistical Scrutiny; 10 Core Comments)
1. **Novelty & Methodological Contribution:** Clarify methodological novelty beyond simple concatenation of 3 pre-trained ViT feature vectors followed by off-the-shelf classifiers, relative to existing dual-domain and multi-domain techniques.
2. **Data Leakage & Subject-Disjoint Generalization:** Inquire whether the image-level stratified split (10,800 images across 600 unique identities, 18 images/identity) permits images of the same identity to appear in both training and test partitions. Request clarification on identity overlap and evaluation under subject-disjoint conditions.
3. **Preprocessing & Reproducibility:** Specify exact HuggingFace checkpoint versions, image processors, normalization parameters, and feature extraction procedures for all three ViT backbones.
4. **Hyperparameter Search Space Consistency:** Reconcile reported search space metrics (1,086 combinations, 38,010 cross-validation fits, 28 final refits) with individual parameter tables in the methodology.
5. **Statistical Significance & McNemar Test:** Point out that SVM accuracy gain from dual-domain (93.29%) to tri-domain (93.70%) is not statistically significant based on the reported McNemar test ($p = 0.3057$). Consequently, claims of tri-domain superiority and feature saturation must be appropriately qualified.
6. **Fairness Analysis Scope:** Clarify that Equal Opportunity Difference (EOD) metrics provide useful subgroup data but do not constitute comprehensive demographic fairness. Refine the scope of fairness claims.
7. **Baseline Benchmark Conditions:** Clarify whether prior methods compared in Table 12 used identical data partitions, preprocessing, and evaluation protocols; otherwise present them as contextual rather than controlled benchmarks.
8. **Computational Efficiency Profiling:** Report empirical feature extraction time, classifier training time, inference latency, memory consumption, and model storage requirements.
9. **Phenotypic & Visual Overlap Interpretation:** Qualify statements regarding phenotypic overlap, age-related feature contributions, and inter-racial error reductions, as they cannot be fully substantiated by confusion matrices alone.
10. **Scope of Conclusions & Limitations:** Restrict conclusions strictly to the evaluated DemogPairs benchmark unless cross-identity or external dataset validation is provided.
- *Questionnaire Answers:* Reviewed all files (Yes), Contributes to knowledge (Yes), Technically sound (Yes), Comprehensive presentation (Yes), References applicable (Yes), Inappropriate references (No).

### 2.4 Resubmission Deliverables Required by IEEE Access
To execute a successful resubmission through the IEEE Author Portal, the following three manuscript files are mandatory:
1. **`Author's Response Files`:** Completed `IEEE-Access_Response-to-Reviewers-template.md` addressing every reviewer comment in a point-by-point format (`Concern`, `Author response`, `Author action`).
2. **`Highlighted PDF`:** Revised manuscript PDF with all individual textual, mathematical, and tabular modifications highlighted in yellow.
3. **`Main Manuscript`:** Clean version of the final manuscript without highlights, provided in both LaTeX source (`.tex` / `.zip`) and compiled double-column PDF (`.pdf`).
4. **Additional Forms (if applicable):** `Request-for-Byline-Change.md` (if authorship order or members changed) and `Resubmission-Checklist.md`.

---

## 3. Research Architecture & Methodological Pipeline

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
                         (SVM / Logistic Regression / Random Forest / GNB)
                                               │
                                               ▼
                     [ Intersectional 6-Class Classification on DemogPairs ]
               (Asian_Females, Asian_Males, Black_Females, Black_Males, White_Females, White_Males)
```

### 3.1 Vision Transformer Feature Extraction Mechanics
All three models are built on the **ViT-Base (`vit-base-patch16-224`)** architecture:
- **Input Processing:** $224 \times 224 \times 3$ RGB image partitioned into $N = 196$ non-overlapping patches ($P = 16 \times 16$).
- **Linear Patch Projection:** Patches are flattened ($\mathbf{x}_p^i \in \mathbb{R}^{768}$) and projected via matrix $\mathbf{E} \in \mathbb{R}^{(P^2C) \times D}$ to dimension $D = 768$.
- **Prepend CLS Token & Position Embedding:**
  $$\mathbf{z}_0 = [\mathbf{x}_{\text{class}}; \, \mathbf{x}_p^1\mathbf{E}; \, \mathbf{x}_p^2\mathbf{E}; \, \dots; \, \mathbf{x}_p^{196}\mathbf{E}] + \mathbf{E}_{\text{pos}}, \quad \mathbf{E}_{\text{pos}} \in \mathbb{R}^{(N+1) \times D}$$
- **Encoder Blocks (12 Layers):** Each layer comprises Multi-Head Self-Attention (MHSA, 12 heads) and Multi-Layer Perceptron (MLP) with Layer Normalization (LN):
  $$\mathbf{z}'_\ell = \text{MHSA}(\text{LN}(\mathbf{z}_{\ell-1})) + \mathbf{z}_{\ell-1}$$
  $$\mathbf{z}_\ell = \text{MLP}(\text{LN}(\mathbf{z}'_\ell)) + \mathbf{z}'_\ell, \quad \ell = 1, \dots, 12$$
- **Final Feature Extraction:** Models are frozen; feature vector is the normalized `[CLS]` token ($\mathbf{z}_L^0$) from the final layer $L = 12$:
  $$\mathbf{f}_{\text{domain}} = \text{LayerNorm}(\mathbf{z}_L^0) \in \mathbb{R}^{768}$$

### 3.2 ViT Backbone Specifications
| Backbone | HuggingFace Repository Identifier | Pre-training Task & Domain | Representation Visual Cues |
|---|---|---|---|
| **ViT-Face** | `skutaada/VIT-VGGFace` | Facial Biometric Recognition (VGGFace) | Craniofacial bone structure, ocular distance, static facial proportions |
| **ViT-Emotion** | `dima806/facial_emotions_image_detection` | Affective State & Facial Expression | Micro-expressions, muscular activation around mouth, brows, and eyes |
| **ViT-Age** | `dima806/facial_age_image_detection` | Biological Age Estimation | Epidermal elasticity, nasolabial folds, periocular wrinkles, aging morphology |

---

## 4. Dataset Specifications, Label Encodings & Partitioning Protocol

### 4.1 Benchmark Dataset: DemogPairs
- **Primary Citation:** I. Hupont and C. Fernández, "DemogPairs: Quantifying the Impact of Demographic Imbalance in Deep Face Recognition," *IEEE FG 2019*, DOI: `10.1109/FG.2019.8756625`.
- **Dataset Composition:** 10,800 facial images from 600 unique identities (100 subjects per demographic group, 18 high-resolution images per subject).
- **Class Balance:** Perfectly balanced across 6 intersectional demographic subgroups (1,800 images each).

### 4.2 Critical Label Encoding Map
An AI agent modifying or evaluating code must note the distinction between internal array indices and alphabetical class listings:
- **`DEMOGPairs_LABEL_TO_IDX` (in `experiment/code/utils/constants.py`):**
  - `Black_Males`: `0`
  - `White_Females`: `1`
  - `Asian_Males`: `2`
  - `White_Males`: `3`
  - `Black_Females`: `4`
  - `Asian_Females`: `5`
- **Alphabetical Class Ordering (`DEMOGPairs_CLASSES`):**
  `['Asian_Females', 'Asian_Males', 'Black_Females', 'Black_Males', 'White_Females', 'White_Males']`
- **Confusion Matrix Alignment:** In `utils/evaluation.py`, classification reports and confusion matrices explicitly use `labels=[DEMOGPairs_LABEL_TO_IDX[n] for n in target_names]` to prevent axis misalignment.

### 4.3 Partitioning & Leakage Prevention Protocol
- **Partition Ratio:** 80% Train ($N = 8,640$, exactly 1,440 per class) / 20% Held-Out Test ($N = 2,160$, exactly 360 per class).
- **Splitting Parameters:** `sklearn.model_selection.train_test_split(..., test_size=0.2, random_state=42, stratify=y)`.
- **Cross-Validation:** 5-Fold Stratified K-Fold (`shuffle=True, random_state=42`) executed strictly within training folds.
- **Data Leakage Safeguard:** Preprocessing transformations (`MinMaxScaler` and `PCA`) are encapsulated within `sklearn.pipeline.Pipeline` objects and fitted only on training folds.

---

## 5. Feature Extraction & 7 Ablation Schemes

### 5.1 Ablation Taxonomy
| Scheme Index | Feature Scheme Name | Category | Dimensionality | Concatenation Formulation |
|:---:|---|:---:|:---:|---|
| 1 | `vit-age` | Single-Domain | 768 | $\mathbf{z} = \mathbf{f}_{\text{age}} \in \mathbb{R}^{768}$ |
| 2 | `vit-emotion` | Single-Domain | 768 | $\mathbf{z} = \mathbf{f}_{\text{emotion}} \in \mathbb{R}^{768}$ |
| 3 | `vit-face` | Single-Domain | 768 | $\mathbf{z} = \mathbf{f}_{\text{face}} \in \mathbb{R}^{768}$ |
| 4 | `vit-emotion-age` | Dual-Domain | 1,536 | $\mathbf{z} = [\mathbf{f}_{\text{emotion}} \,\|\, \mathbf{f}_{\text{age}}] \in \mathbb{R}^{1536}$ |
| 5 | `vit-face-age` | Dual-Domain | 1,536 | $\mathbf{z} = [\mathbf{f}_{\text{face}} \,\|\, \mathbf{f}_{\text{age}}] \in \mathbb{R}^{1536}$ |
| 6 | `vit-emotion-face` | Dual-Domain | 1,536 | $\mathbf{z} = [\mathbf{f}_{\text{emotion}} \,\|\, \mathbf{f}_{\text{face}}] \in \mathbb{R}^{1536}$ |
| 7 | **`vit-face-emotion-age`** | **Tri-Domain (Proposed)** | **2,304** | $\mathbf{z} = [\mathbf{f}_{\text{face}} \,\|\, \mathbf{f}_{\text{emotion}} \,\|\, \mathbf{f}_{\text{age}}] \in \mathbb{R}^{2304}$ |

### 5.2 Offline Cache Files
Serialized feature dictionaries mapping relative image paths to 768-d NumPy arrays (`float32`) are stored in `experiment/code/features/`:
- `demogpairs_vit-face.pkl` (30.8 MB)
- `demogpairs_vit-emotion.pkl` (30.8 MB)
- `demogpairs_vit-age.pkl` (30.8 MB)

---

## 6. Classical Classifier Pipeline & Exhaustive GridSearchCV Optimization

### 6.1 End-to-End Pipeline Formulation
$$\mathbf{x} \xrightarrow{\text{Scaler}} \tilde{\mathbf{x}} \xrightarrow{\text{PCA}} \hat{\mathbf{x}} \xrightarrow{\text{Classifier}} \hat{y} \in \{0, 1, 2, 3, 4, 5\}$$

### 6.2 Search Spaces per Classifier
- **Support Vector Machine (SVM) – 288 configurations per scheme:**
  - `scaler`: `[None, MinMaxScaler()]`
  - `pca`: `[None, PCA(n_components=0.50), PCA(n_components=0.75)]`
  - `classifier__C`: `[0.1, 1, 10, 100]`
  - `classifier__kernel`: `['linear', 'rbf', 'poly']`
  - `classifier__degree`: `[2, 3]`
  - `classifier__gamma`: `['scale', 'auto']`
- **Logistic Regression (LR) – 270 configurations per scheme:**
  - `scaler`: `[None, MinMaxScaler()]`
  - `pca`: `[None, PCA(n_components=0.50), PCA(n_components=0.75)]`
  - `classifier__C`: `[0.01, 0.1, 1, 10, 100]`
  - `classifier__solver`: `['lbfgs', 'saga', 'newton-cg']`
  - `classifier__max_iter`: `[200, 500, 2000]`
- **Random Forest (RF) – 288 configurations per scheme:**
  - `scaler`: `[None, MinMaxScaler()]`
  - `pca`: `[None, PCA(n_components=0.50), PCA(n_components=0.75)]`
  - `classifier__n_estimators`: `[100, 200]`
  - `classifier__max_depth`: `[None, 10, 30]`
  - `classifier__max_features`: `['sqrt', 'log2']`
  - `classifier__min_samples_split`: `[2, 5]`
  - `classifier__min_samples_leaf`: `[1, 2]`
- **Gaussian Naive Bayes (GNB) – 240 configurations per scheme:**
  - `scaler`: `[None, MinMaxScaler()]`
  - `pca`: `[None, PCA(n_components=0.50), PCA(n_components=0.75)]`
  - `classifier__var_smoothing`: 40 log-spaced values from $10^{-9}$ to $10^{2}$ (`np.logspace(-9, 2, 40)`)

### 6.3 Optimization Scale Summary
- Total combinations per scheme: $288 + 270 + 288 + 240 = \mathbf{1,086}$ combinations.
- Total 5-Fold cross-validation fits per scheme: $1,086 \times 5 = \mathbf{5,430}$ fits.
- Total for all 7 feature schemes: $5,430 \times 7 = \mathbf{38,010}$ cross-validation fits + 28 final refit models.

---

## 7. Comprehensive Experimental Benchmark (Definitive 28-Model Leaderboard)

Evaluated on the held-out test partition ($N = 2,160$). All figures are extracted directly from `experiment/code/results/*.json`:

| Rank | Classifier | Feature Scheme | Category | Dim | Test Accuracy | Precision (Macro) | Recall (Macro) | F1-Score (Macro) | Best Hyperparameters |
|:---:|---|---|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 🥇 **1** | **SVM** | **`vit-face-emotion-age`** | **Tri** | **2,304** | **0.9370** | **0.9372** | **0.9370** | **0.9369** | `C=10, kernel='poly', degree=2, gamma='scale', scaler=None, pca=None` |
| 🥈 **2** | **SVM** | `vit-emotion-face` | Dual | 1,536 | **0.9329** | 0.9333 | 0.9329 | 0.9329 | `C=10, kernel='rbf', degree=2, gamma='scale', scaler=MinMaxScaler, pca=None` |
| 🥉 **3** | **LR** | **`vit-face-emotion-age`** | **Tri** | **2,304** | **0.9273** | 0.9275 | 0.9273 | 0.9273 | `C=0.1, solver='newton-cg', max_iter=500, scaler=None, pca=None` |
| 4 | SVM | `vit-face-age` | Dual | 1,536 | 0.9255 | 0.9254 | 0.9255 | 0.9254 | `C=10, kernel='poly', degree=2, gamma='scale', scaler=None, pca=None` |
| 5 | LR | `vit-emotion-face` | Dual | 1,536 | 0.9241 | 0.9241 | 0.9241 | 0.9240 | `C=0.1, solver='lbfgs', max_iter=500, scaler=None, pca=None` |
| 6 | SVM | `vit-emotion-age` | Dual | 1,536 | 0.9208 | 0.9210 | 0.9208 | 0.9209 | `C=10, kernel='rbf', degree=2, gamma='scale', scaler=None, pca=None` |
| 7 | LR | `vit-face-age` | Dual | 1,536 | 0.9162 | 0.9162 | 0.9162 | 0.9162 | `C=0.1, solver='newton-cg', max_iter=500, scaler=None, pca=None` |
| 8 | SVM | `vit-face` | Single | 768 | 0.9083 | 0.9084 | 0.9083 | 0.9083 | `C=10, kernel='rbf', degree=2, gamma='scale', scaler=None, pca=None` |
| 9 | LR | `vit-face` | Single | 768 | 0.9060 | 0.9060 | 0.9060 | 0.9059 | `C=1, solver='newton-cg', max_iter=500, scaler=MinMaxScaler, pca=None` |
| 10 | LR | `vit-emotion-age` | Dual | 1,536 | 0.9051 | 0.9052 | 0.9051 | 0.9051 | `C=0.1, solver='lbfgs', max_iter=500, scaler=None, pca=None` |
| 11 | SVM | `vit-emotion` | Single | 768 | 0.9019 | 0.9020 | 0.9019 | 0.9017 | `C=10, kernel='rbf', degree=2, gamma='scale', scaler=None, pca=None` |
| 12 | LR | `vit-emotion` | Single | 768 | 0.8847 | 0.8850 | 0.8847 | 0.8846 | `C=1, solver='saga', max_iter=500, scaler=MinMaxScaler, pca=None` |
| 13 | SVM | `vit-age` | Single | 768 | 0.8764 | 0.8767 | 0.8764 | 0.8765 | `C=10, kernel='rbf', degree=2, gamma='scale', scaler=None, pca=None` |
| 14 | RF | `vit-emotion-face` | Dual | 1,536 | 0.8685 | 0.8689 | 0.8685 | 0.8682 | `n_estimators=200, max_depth=None, max_features='sqrt', min_samples_split=5, min_samples_leaf=1, pca=PCA(0.75), scaler=None` |
| 15 | LR | `vit-age` | Single | 768 | 0.8648 | 0.8649 | 0.8648 | 0.8648 | `C=0.1, solver='lbfgs', max_iter=500, scaler=None, pca=None` |
| 16 | RF | **`vit-face-emotion-age`** | **Tri** | **2,304** | 0.8620 | 0.8620 | 0.8620 | 0.8613 | `n_estimators=200, max_depth=30, max_features='sqrt', min_samples_split=5, min_samples_leaf=1, pca=PCA(0.75), scaler=None` |
| 17 | RF | `vit-face-age` | Dual | 1,536 | 0.8579 | 0.8578 | 0.8579 | 0.8573 | `n_estimators=200, max_depth=None, max_features='sqrt', min_samples_split=2, min_samples_leaf=1, pca=PCA(0.75), scaler=None` |
| 18 | RF | `vit-face` | Single | 768 | 0.8546 | 0.8543 | 0.8546 | 0.8539 | `n_estimators=200, max_depth=30, max_features='log2', min_samples_split=2, min_samples_leaf=1, pca=PCA(0.75), scaler=MinMaxScaler` |
| 19 | GNB | **`vit-face-emotion-age`** | **Tri** | **2,304** | 0.8505 | 0.8512 | 0.8505 | 0.8505 | `var_smoothing=0.005878, pca=PCA(0.75), scaler=None` |
| 20 | GNB | `vit-emotion-face` | Dual | 1,536 | 0.8486 | 0.8490 | 0.8486 | 0.8481 | `var_smoothing=0.005878, pca=PCA(0.75), scaler=MinMaxScaler` |
| 21 | GNB | `vit-face-age` | Dual | 1,536 | 0.8315 | 0.8343 | 0.8315 | 0.8317 | `var_smoothing=0.011253, pca=PCA(0.75), scaler=MinMaxScaler` |
| 22 | GNB | `vit-face` | Single | 768 | 0.8269 | 0.8271 | 0.8269 | 0.8258 | `var_smoothing=0.041246, pca=PCA(0.75), scaler=MinMaxScaler` |
| 23 | RF | `vit-emotion-age` | Dual | 1,536 | 0.8111 | 0.8111 | 0.8111 | 0.8108 | `n_estimators=200, max_depth=None, max_features='log2', min_samples_split=5, min_samples_leaf=2, pca=PCA(0.75), scaler=None` |
| 24 | RF | `vit-emotion` | Single | 768 | 0.8060 | 0.8063 | 0.8060 | 0.8057 | `n_estimators=200, max_depth=None, max_features='log2', min_samples_split=5, min_samples_leaf=1, pca=PCA(0.75), scaler=None` |
| 25 | GNB | `vit-emotion-age` | Dual | 1,536 | 0.7681 | 0.7686 | 0.7681 | 0.7681 | `var_smoothing=0.001604, pca=PCA(0.75), scaler=MinMaxScaler` |
| 26 | RF | `vit-age` | Single | 768 | 0.7366 | 0.7363 | 0.7366 | 0.7354 | `n_estimators=200, max_depth=30, max_features='log2', min_samples_split=2, min_samples_leaf=1, pca=PCA(0.75), scaler=None` |
| 27 | GNB | `vit-emotion` | Single | 768 | 0.7338 | 0.7387 | 0.7338 | 0.7329 | `var_smoothing=0.003070, pca=PCA(0.75), scaler=None` |
| 28 | GNB | `vit-age` | Single | 768 | 0.6963 | 0.6979 | 0.6963 | 0.6952 | `var_smoothing=0.000438, pca=PCA(0.75), scaler=MinMaxScaler` |

### 7.2 Empirical Ablation Analysis
1. **Single to Dual:** Adding emotion features to face biometrics (`vit-face` 0.9083 $\to$ `vit-emotion-face` 0.9329 on SVM) yields a **+0.0245 gain (+2.70%, 26.77% relative error reduction)**.
2. **Dual to Tri-Domain:** Adding biological age morphology (`vit-emotion-face` 0.9329 $\to$ `vit-face-emotion-age` 0.9370 on SVM) adds **+0.0042 (+0.45%, 6.11% error reduction)**. While modest and not statistically significant under McNemar test ($p = 0.3057$), it establishes consistency across SVM, LR, and GNB.
3. **Cumulative Impact:** Single face to tri-domain (`0.9083` to `0.9370`) achieves **+0.0287 (+3.16%, 31.31% total error reduction)**.
4. **Dimensionality & PCA Selection:** SVM and LR models consistently select `pca=None` (preserving all 2,304 features). In contrast, Random Forest and Gaussian Naive Bayes universally select `pca=PCA(0.75)` to prevent severe overfitting.

---

## 8. Intersectional Subgroup Performance, Confusion Matrix & Error Dynamics

### 8.1 Subgroup Metrics for Top-Performing SVM Tri-Domain ($N = 2,160$)
| Subgroup | Race | Gender | Support | TP | FP | FN | TN | OvR Accuracy | Precision | Recall | F1-Score |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **White_Males** | White | Male | 360 | 349 | 17 | 11 | 1,783 | **98.70%** | 0.9536 | **0.9694** | **0.9614** |
| **Black_Males** | Black | Male | 360 | 339 | 16 | 21 | 1,784 | **98.29%** | 0.9549 | 0.9417 | 0.9483 |
| **White_Females** | White | Female | 360 | 341 | 28 | 19 | 1,772 | **97.82%** | 0.9241 | 0.9472 | 0.9355 |
| **Asian_Males** | Asian | Male | 360 | 340 | 28 | 20 | 1,772 | **97.78%** | 0.9239 | 0.9444 | 0.9341 |
| **Asian_Females** | Asian | Female | 360 | 333 | 27 | 27 | 1,773 | **97.50%** | 0.9250 | 0.9250 | 0.9250 |
| **Black_Females** | Black | Female | 360 | 322 | 20 | 38 | 1,780 | **97.31%** | 0.9415 | 0.8944 | 0.9174 |
| **Macro Average** | **All** | **All** | **2,160** | **-** | **-** | **-** | **-** | **97.90%** | **0.9372** | **0.9370** | **0.9369** |

### 8.2 Actual 6 × 6 Confusion Matrix (Held-Out Test Set)
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

### 8.3 Error Dynamics & Disparity Summary
- **Primary Error Source:** Cross-race same-gender misclassifications (e.g., 16 `Black_Females` misclassified as `White_Females`, 10 `Asian_Females` as `White_Females`).
- **Near-Zero Gender Confusion:** Intra-race and cross-race gender confusion is <1%, indicating that multi-domain ViT representations establish distinct gender boundaries.
- **Disparity Metrics:**
  - $\Delta_{\text{F1}} = \max(\text{F1}) - \min(\text{F1}) = 0.9614 - 0.9174 = \mathbf{0.0440}$.
  - $\Delta_{\text{Recall}} = \max(\text{Recall}) - \min(\text{Recall}) = 0.9694 - 0.8944 = \mathbf{0.0750}$.
  - $\Delta_{\text{Precision}} = 0.9549 - 0.9239 = \mathbf{0.0310}$.
  - $\Delta_{\text{OvR Acc}} = 98.70\% - 97.31\% = \mathbf{1.39\text{ pp}}$.

---

## 9. Comparison with Prior Studies on DemogPairs & Contextual Literature

### 9.1 Controlled Comparison on DemogPairs Benchmark
| Reference | Architecture / Method | Evaluated Classes | Accuracy | Precision | Recall | F1-Score |
|---|---|:---:|:---:|:---:|:---:|:---:|
| Putri et al. (*JIEET 2025*) | MD-ViT (Face + Age) + XGBoost | 6 Intersectional | 89.07% | 0.8912 | 0.8907 | 0.8901 |
| Putri et al. (*IEEE ICVEE 2025*) | Dual-ViT (Face + Emotion) + SVM | 6 Intersectional | 92.41% | 0.9248 | 0.9241 | 0.9238 |
| **Proposed Framework (2026)** | **Tri-Domain ViT (Face ⊕ Emotion ⊕ Age) + Optimized SVM** | **6 Intersectional** | **93.70%** | **0.9372** | **0.9370** | **0.9369** |

### 9.2 Contextual Literature (Studies 1–8)
Studies evaluating outside DemogPairs (e.g., Belcar et al. 2022 on custom dataset: 61.74%; Sunitha et al. 2022 on FairFace: 88.50%; Tahyudin et al. 2024 on AFAD: 81.74%; Kalkatawi & Saeed 2024 on FairFace: 77.20%) are cited strictly as contextual background. In scientific writing, do not describe them as a direct controlled baseline.

---

## 10. Repository Architecture & File Inventory

```
D:\Research\face-race-gender-classification-using-multi-domain-vit\
├── README.md                              # Public research documentation & summary
├── README.AI.md                           # Master AI agent reference manual (THIS FILE)
├── WORKFLOW.md                            # Standard Operating Procedure (SOP) for manuscript pipeline
├── paper_outline.md                       # Comprehensive paper outline & paragraph targets
├── folder_structure.txt                   # Complete directory tree and detailed file glossary
├── authors.txt                            # Academic author profiles, affiliations & ORCIDs
├── prompts.txt                            # Chronological prompt tracking log
├── scopus_query.txt                       # Scopus literature search queries
│
├── .agents/skills/                        # Autonomous AI agent skills & peer review frameworks
│   ├── ar-paper-reviewer/                 # Independent academic peer review simulation skill
│   ├── ar-paper-revision/                 # Byte-level precision patching and revision application skill
│   └── ar-paper-revision-coach/           # Review deconstruction, roadmap & rebuttal ledger coach
│
├── experiment/                            # Experimental documentation, datasets & source code
│   ├── 00_overview.md - 05_results.md     # Structured experimental logs & audits
│   ├── dataset_demogpairs.md              # Dataset specification and partition summary
│   └── code/
│       ├── 1.1_vit-*_demogpairs.ipynb     # Feature extraction notebooks (Face, Emotion, Age)
│       ├── 2.1.* - 2.5.*.ipynb            # Classifier training notebooks (SVM, GNB, RF, LR)
│       ├── 3.0_compare.ipynb              # Global 28-model comparison and benchmarking
│       ├── 4.0_test.ipynb                 # Held-out evaluation and test routines
│       ├── app.py                         # Interactive Gradio demo web application
│       ├── utils/                         # Modular Python utility package (constants, dataset, evaluation, etc.)
│       ├── dataset/demogpairs/metadata/   # 6 metadata .txt files (1,800 rows each)
│       ├── md/                            # Markdown exports of all Jupyter notebooks
│       ├── results/                       # 28 raw JSON evaluation result files
│       └── images/                        # 28 confusion matrix diagrams (.png)
│
├── images/                                # High-resolution architecture diagrams and sample figures
│   ├── method.png / method.pptx           # Architecture & methodology framework diagram (Figure 1)
│   ├── sample_*.jpg / demogpairs.png      # Sample demographic face images (Figure 2)
│   ├── vit.png / vit.pptx                 # ViT backbone & patch projection diagram (Figure 3)
│   └── confusion_matrix_*.png             # Selected confusion matrix plots
│
├── paper/                                 # Modular manuscript draft in Markdown (IEEE style)
│   ├── 00_abstract.md                     # Title, authors, abstract, and IEEE keywords
│   ├── 01_introduction.md                 # Section I: Introduction
│   ├── 02_related-works.md                # Section II: Related Works
│   ├── 03_materials-and-methods_*.md      # Section III: Methodology modular subsections
│   ├── 04_results-and-discussion_*.md     # Section IV: Results and Discussion modular subsections
│   ├── 05_conclusion.md                   # Section V: Conclusion, limitations & future work
│   ├── 06_references.md                   # Section VI: References (IEEE formatted, entries [1]-[51])
│   ├── 07_biographies.md                  # Section VII: Biographies & portrait assets
│   ├── acronyms.txt                       # Centralized acronym registry (Rule 1.3)
│   ├── ref_part_*.md                      # 10 modular bibliographic audit logs (entries [1]-[51])
│   ├── references.txt                     # Sentence-level citation tracking & verification registry
│   ├── references/                        # 51 bibliographic source files (.bib, .ris, .nbib, .bibtex)
│   └── images/                            # Self-contained local image assets for paper compilation
│
├── paper_latex_en/                        # Submission-ready English IEEE Access LaTeX package
│   ├── access.tex                         # Master LaTeX entrypoint with \input{} sections
│   ├── access.pdf                         # Compiled dual-column English manuscript PDF
│   ├── ieeeaccess.cls / IEEEtran.bst      # Official IEEE Access style class and bibliography style
│   ├── references.bib                     # Consolidated BibTeX database
│   ├── sections/                          # 21 modular LaTeX sections (00_title.tex s.d. 07_biographies.tex)
│   └── images/                            # Figures and high-resolution plots for LaTeX compilation
│
├── paper_latex_id/                        # Reference Indonesian IEEE Access LaTeX package
│   ├── access.tex                         # Master LaTeX entrypoint with \input{} sections
│   ├── access.pdf                         # Compiled dual-column Indonesian manuscript PDF
│   ├── ieeeaccess.cls / IEEEtran.bst      # Official IEEE Access style class and bibliography style
│   ├── references.bib                     # Consolidated BibTeX database
│   ├── sections/                          # 21 modular LaTeX sections (00_title.tex s.d. 07_biographies.tex)
│   └── images/                            # Figures and high-resolution plots for LaTeX compilation
│
├── paper_reviews/                         # Internal multi-agent mock peer review audit system
│   ├── round-1/                           # Round 1: Desk screening, 5 independent reviews & roadmap
│   ├── round-2/                           # Round 2: Residual issue audit, re-review verification & EIC sign-off
│   └── REVIEW_LOG.md                      # Audit trail of internal peer review cycles
│
├── paper_reviews_ieee/                    # Official IEEE Access editorial decision & review dossier
│   ├── IEEE-Access_Decision-on-Manuscript-ID-Access-2026-50857.md # Official decision letter & reviewer comments
│   ├── IEEE-Access_Response-to-Reviewers-template.md              # IEEE Access response to reviewers template
│   ├── Request-for-Byline-Change.md                               # Formal author byline change form
│   └── Resubmission-Checklist.md                                  # Resubmission 10-point compliance checklist
│
├── paper_submission/                      # Formal submission packaging and IEEE compliance reports
│   ├── checklist_report.md                # Submission readiness audit report
│   ├── IEEE Reference Preparation Assistant Report.txt # IEEE reference tool compliance report
│   ├── ieee_taxonomy.txt                  # Selected IEEE controlled vocabulary taxonomy terms
│   ├── IEEE-Access-Submission-Checklist.pdf # IEEE Access official checklist form (PDF)
│   └── IEEE-Access-Submission-Checklist.txt # IEEE Access submission checklist (English & Indonesian)
│
├── references/                            # BibTeX citation sources (DemogPairs)
├── related_works/                         # Literature reviews, summary matrices, and gap analysis
│   ├── bib/                               # BibTeX files for 10 mandatory literature papers
│   ├── pdf/                               # Full-text PDFs of related studies
│   ├── summaries/                         # Structured analytical summaries per paper
│   ├── gap_analysis.md                    # Research gap identification
│   ├── literature_matrix.md               # Comparative literature matrix
│   ├── sintesis_literatur.md              # Thematic literature synthesis
│   └── tren_analisis.md                   # Chronological and methodological trend analysis
│
├── rules/                                 # Standardized rules for formatting, LaTeX, and citations
│   ├── IEEE_citation_guidelines.md        # IEEE citation and bibliography guidelines
│   ├── latex_rules.txt                    # LaTeX conversion rules and templates
│   └── md_rules.txt                       # Strict Markdown drafting rules and checklist
│
├── sessions/                              # Chronological AGY development and audit session records
│   └── session_*.md                       # Comprehensive session logs (pattern: session_YYYY-MM-DD_agent_title)
│
├── template/                              # Raw IEEE Access LaTeX template distribution package
└── upload/                                # Packaged submission artifacts (PDF and source ZIP)
```

---

## 11. Submission Compliance & Packaging (`paper_submission/` & `upload/`)

### 11.1 Directory `paper_submission/`
Contains documents validating alignment with IEEE Access author guidelines:
- `checklist_report.md`: Systematic report auditing compliance with all IEEE Access submission requirements.
- `IEEE Reference Preparation Assistant Report.txt`: Output from the IEEE Reference Preparation Assistant verifying bibliographic metadata format consistency.
- `ieee_taxonomy.txt`: List of controlled vocabulary keywords matching official IEEE taxonomy categories.
- `IEEE-Access-Submission-Checklist.pdf` / `.txt` / `.ID.txt`: Official IEEE Access submission checklist completed and translated for dual-language tracking.

### 11.2 Directory `upload/`
Contains the submission package submitted to the IEEE Author Portal:
- `Multi-Domain Vision Transformer Fusion for Intersectional Demographic Classification from Facial Images.pdf`: The dual-column compiled PDF.
- `Multi-Domain Vision Transformer Fusion for Intersectional Demographic Classification from Facial Images.zip`: The zipped source package containing `access.tex`, `sections/*.tex`, `images/*`, `ieeeaccess.cls`, and `references.bib`.

---

## 12. Internal Mock Peer Review Suite (`paper_reviews/`) & Agent Skills (`.agents/skills/`)

### 12.1 Internal Mock Peer Review System (`paper_reviews/`)
Before formal journal submission, the manuscript underwent an internal multi-agent mock peer review simulation:
- **`round-1/`**:
  - `00_desk_screening.md`: Desk screening audit assessing scope, formatting, and structural compliance.
  - `01_eic_report.md`: Editor-in-Chief summary assessment.
  - `02_methodology_reviewer.md`: In-depth methodological examination.
  - `03_domain_reviewer.md`: Computer vision and facial biometrics domain review.
  - `04_cross_perspective_analyst.md`: Intersectional fairness and demographic disparity evaluation.
  - `05_devils_advocate.md`: Critical scrutiny challenging assumptions, claims, and baselines.
  - `06_findings_matrix.md`: Consolidated issue tracking matrix.
  - `07_editorial_decision.md`: Synthesized Round 1 editorial decision.
  - `08_revision_roadmap.md`: Action plan for resolving identified issues.
- **`round-2/`**:
  - `07_editorial_decision.md`: Verification of revisions.
  - `08_residual_issues.md`: Tracking of any remaining minor items.
  - `09_response_letter_validation.md`: Rebuttal response validation.
  - `10_rebuttal_audit.md`: Quality assurance audit of response arguments.
  - `11_re_review_verification.md`: Traceability matrix mapping reviewer comments to manuscript lines.
  - `12_eic_re_review_decision.md`: Final mock acceptance sign-off.
- **`REVIEW_LOG.md`**: Master audit trail tracking timelines and reviewer identities.

### 12.2 Specialized Autonomous Agent Skills (`.agents/skills/`)
- `ar-paper-reviewer`: Executes independent academic mock reviews across 5 specialized roles (EIC, Methodology, Domain, Cross-Perspective, Devil's Advocate) based on Contract Sprint Schema 13.
- `ar-paper-revision`: Implements byte-level precision patching (`<!--block:BNNNN-->`), fail-closed validation, and formal Response to Reviewers compilation (Schema 8).
- `ar-paper-revision-coach`: Parses raw reviewer comments, builds 4-tier issue taxonomies, prioritizes revisions (P1 must-fix, P2 should-fix, P3 consider), and generates R&R Traceability Matrices (Schema 11).

---

## 13. Python Utilities Library Reference (`experiment/code/utils/`)

Located at `experiment/code/utils/`, this modular library provides common functionality across experiments:

### 13.1 `constants.py`
Defines demographic classes, index mappings, random seeds, and color palettes:
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

### 13.2 `dataset.py`
- `load_demogpairs(metadata_path, images_path) -> list[dict]`: Parses 6 metadata `.txt` files in `dataset/demogpairs/metadata/` to produce 10,800 dictionary records with keys `db_code`, `image_path`, `full_path`, `label`, and `label_idx`.

### 13.3 `extraction.py`
- `extract_vit_features(img, model=None, model_path=None, device=None, feature_type='cls') -> np.ndarray`: Takes an image path or array, runs HuggingFace `AutoImageProcessor` to format tensors to $224 \times 224$, queries the Vision Transformer backbone, and returns a 1D NumPy vector of shape `(768,)` corresponding to the normalized `[CLS]` token.

### 13.4 `evaluation.py`
- `evaluate_models(grid_models, x_train, y_train, x_test, y_test, model_prefix, target_names, results_path) -> tuple`: Fits GridSearchCV pipelines (or loads them if serialized `.pkl` exists), performs inference on test sets, generates classification reports, calculates One-vs-Rest (OvR) per-class metrics, creates confusion matrix heatmap figures (`images/`), and serializes evaluation artifacts to JSON (`results/`).

### 13.5 `serialization.py`
- `save_object(obj, filename, compress=9)`: Serializes binary objects using Joblib with level-9 compression.
- `load_object(filename)`: Loads Joblib-serialized objects.
- `save_json(data, json_file)`: Formats and writes Python dictionaries to indented JSON.
- `load_json(file_path)`: Safely parses JSON files into dictionaries.

### 13.6 `display.py` & `time_helpers.py`
- `display.py`: Provides tabular formatting utilities for CLI and HTML notebook environments.
- `time_helpers.py`: Tracks and formats elapsed execution time across long-running cross-validation loops.

---

## 14. Execution, Reproduction & Manuscript Compilation Workflows

### 14.1 Python Environment Setup
```bash
conda create -n torch-gpu python=3.11 -y
conda activate torch-gpu
pip install torch torchvision transformers scikit-learn imbalanced-learn joblib pandas numpy pillow matplotlib seaborn tqdm gradio nbconvert
```

### 14.2 Running the Machine Learning Pipeline
1. **Feature Extraction:** Execute notebooks `1.1_vit-face_demogpairs.ipynb`, `1.1_vit-emotion_demogpairs.ipynb`, and `1.1_vit-age_demogpairs.ipynb` sequentially. Feature vectors will be saved in `experiment/code/features/`.
2. **Model Training & Optimization:** Execute classifier notebooks:
   - SVM: `2.1.1` to `2.1.7`
   - GNB: `2.2.1` to `2.2.7`
   - RF: `2.4.1` to `2.4.7`
   - LR: `2.5.1` to `2.5.7`
3. **Cross-Model Comparison:** Run `3.0_compare.ipynb` to aggregate all 28 JSON result files into a consolidated benchmark leaderboard.
4. **Interactive Web Inference:**
   ```bash
   python experiment/code/app.py
   # Launches local Gradio interface at http://127.0.0.1:7860
   ```

### 14.3 LaTeX Manuscript Compilation
To recompile either manuscript from source:
```bash
# 1. Compile English Submission Manuscript (IEEE Access dual-column)
cd paper_latex_en
pdflatex access.tex
bibtex access
pdflatex access.tex
pdflatex access.tex

# 2. Compile Indonesian Reference Manuscript
cd ../paper_latex_id
pdflatex access.tex
bibtex access
pdflatex access.tex
pdflatex access.tex
```
Compilation produces the submission-ready dual-column PDF `access.pdf` in each respective folder.

---

## 15. Scientific Claim Boundaries & Academic Writing Constraints (27 Directives)

When writing, revising, or auditing manuscript drafts, outlining papers, or drafting responses to reviewer comments, any AI agent **MUST** adhere strictly to the following 27 directives:

1. **No Subject Identity Discussion:** Do not discuss identity-level split, identity leakage, subject identity, or identity-aware split. Focus strictly on intersectional race and gender classification.
2. **Cautious Data Leakage Formulation:** Do not claim absolute "zero data leakage"; use "the preprocessing and cross-validation pipeline was designed to prevent information leakage."
3. **Balanced Evaluation Setting:** A balanced dataset does not imply demographic bias has been eliminated; refer to it as a "balanced evaluation setting" or "balanced class distribution across subgroups."
4. **No "Significantly" Without Statistical Tests:** Do not use the word "significantly" in the absence of formal hypothesis testing; use "substantially", "considerably", "notably", or "achieved higher performance."
5. **Accurate Tri-Domain Scope:** Tri-domain fusion was top-performing on 3 of the 4 classifiers (SVM, LR, GNB); Random Forest achieved its highest performance on dual-domain `Emotion ⊕ Face`.
6. **Complementary Age Features:** Refer to Age features as providing "complementary informational contribution" or "additional discriminative information", not "orthogonal contribution".
7. **Hypothesis-Driven RF Drop Interpretation:** Present the drop in RF performance on 2,304 dimensions as a potential interpretation ("may reflect the difficulty of partitioning a higher-dimensional feature space using randomized splits").
8. **Empirical vs Theoretical Separation:** Strictly separate empirical findings (actual experimental figures) from conceptual interpretations.
9. **No State-of-the-Art Hyperbole:** Use "highest performance among the compared studies" or "outperformed the compared baselines on DemogPairs" - never "state-of-the-art".
10. **Demographic Generalization Scope:** Explicitly limit scope to the 3 macro-racial groups represented in DemogPairs (Asian, Black, White).
11. **AI Ethics Statement:** Formulated for academic benchmarking and algorithmic fairness research; public surveillance deployment requires human-in-the-loop oversight and ethical governance.
12. **Equation (4) CLS Token Definition:** $\mathbf{z}_L^0$ in $\mathbf{f}_{\text{domain}} = \text{LayerNorm}(\mathbf{z}_L^0)$ refers specifically to the CLS token representation from the **final encoder layer L** of the ViT backbone. This must be stated explicitly.
13. **ViT Embedding as Task-Associated Representations:** Do not claim that ViT embeddings are exclusive or universal feature characterizations. Use "task-associated representations" as the preferred framing.
14. **Exact Disparity Figures:** Report confirmed disparity values from source JSON results:
    - SVM: $\Delta\text{F1} = \mathbf{0.0440}$ (0.9614 - 0.9174), $\Delta\text{Precision} = \mathbf{0.0310}$, $\Delta\text{Recall} = \mathbf{0.0750}$, $\Delta\text{OvR Acc} = \mathbf{1.39\text{ pp}}$.
    - LR: $\Delta\text{F1} = \mathbf{0.0422}$ (0.9558 - 0.9136), $\Delta\text{Precision} = \mathbf{0.0495}$, $\Delta\text{Recall} = \mathbf{0.0500}$, $\Delta\text{OvR Acc} = \mathbf{1.39\text{ pp}}$.
15. **Table XI Structure:** Table XI (Subgroup-Level Performance) reports per-subgroup classification metrics (Recall, Precision, F1-Score, OvR Accuracy) for SVM and LR on the tri-domain configuration.
16. **Subgroup Performance Scope:** Note that subgroup evaluation reflects per-class performance across intersectional demographics and does not constitute a comprehensive fairness audit.
17. **OvR Accuracy Context:** High OvR accuracy values are partially attributable to the 5:1 negative sample ratio in binary one-vs-rest evaluation; do not present OvR Accuracy as a sole or primary fairness indicator.
18. **No "State-of-the-Art" Without Benchmark:** Do not claim state-of-the-art without a comprehensive benchmark; the proposed framework was evaluated only on DemogPairs.
19. **Conclusion Must Reflect Actual Results:** Conclusions must state that tri-domain fusion achieved the highest performance on 3 of 4 classifiers. No "universal improvement" or "fairness fully resolved" claims are permitted.
20. **Full Numerical Consistency Check:** All tables, confusion matrices, per-subgroup metrics, and narrative text must be numerically consistent with source JSON result files in `experiment/code/results/`.
21. **Novelty Statement:** The novelty of this work is the combination of (a) tri-domain ViT feature fusion, (b) comparative 4-classifier evaluation under unified GridSearchCV, (c) SVM hyperparameter optimization, and (d) subgroup disparity analysis on an intersectional benchmark.
22. **RQ Alignment:** Every research conclusion must be backed by a table, figure, or experiment result. Do not assert findings without an explicit evidential anchor.
23. **Final Terminology/Notation/Number Consistency:** Before finalizing any section, verify that all acronyms, configuration names (using $\oplus$ symbol), equation references (Eq. 1-19), and numerical values are consistent throughout the entire document.
24. **Hupont & Fernández (IEEE FG 2019):** This is the seminal DemogPairs paper and serves as the baseline dataset citation. It is NOT included in the main direct-comparison performance table (Table XII), but should be cited when introducing the DemogPairs dataset.
25. **Universal Manuscript Pipeline SOP (`WORKFLOW.md`):** All drafting, translation, and publication workflows must strictly follow `WORKFLOW.md` as the official standard operating procedure for generating modular Markdown drafts (`paper/`), Indonesian LaTeX (`paper_latex_id/`), and English submission-ready LaTeX manuscripts (`paper_latex_en/`) from `paper_outline.md`. Both LaTeX packages use `access.tex` as the master document entrypoint and compile directly to `access.pdf`. Each stage must strictly maintain 100% numerical consistency, exact formula definitions, and 1-to-1 modular mapping across all target formats.
26. **Sentence-Level Citation Audit Protocol (`paper/references.txt`):** Every factual claim or external literature reference in `paper/*.md` must be registered with exact quote matching in `paper/references.txt` pointing to source files in `paper/references/`. During manuscript evolution, temporary inline citation markers (`[(N)]`) are strictly tracked and converted into validated bibliography entries before final LaTeX synchronization (`references.bib`).
27. **Interactive In-Text Citation Standards (`paper/*.md`):** All in-text citations in modular Markdown manuscript files use double-bracketed interactive hyperlinks `[[N]](06_references.md#refN)` directly connecting to target `<a id="refN"></a>` anchors in Section VI (`paper/06_references.md`). Multi-citations within a single sentence must be comma-separated with spaces (e.g., `[[1]](06_references.md#ref1), [[2]](06_references.md#ref2)`), placed strictly before terminal punctuation marks (`.` or ` |`) without preceding whitespace, and ordered monotonically increasing by first appearance in the manuscript following IEEE guidelines. Identical literature sources must reuse the same reference number without duplicate assignment.

---

## 16. Key Authors, Academic Provenance & Citation Metadata

### 16.1 Research Team
All authors are affiliated with the **Department of Informatics, Faculty of Informatics, Universitas Negeri Surabaya (UNESA), Surabaya, East Java, Indonesia**:
1. **Dr. Ir. Ricky Eka Putra, S.Kom., M.Kom.** ([ORCID: 0000-0002-5515-7967](https://orcid.org/0000-0002-5515-7967)) - Corresponding Author (`rickyeka@unesa.ac.id`)
2. **Rezky Arisanti Putri, S.Kom., M.Kom.** ([ORCID: 0009-0000-8021-1833](https://orcid.org/0009-0000-8021-1833))
3. **Dr. Yuni Yamasari, S.Kom., M.Kom.** ([ORCID: 0000-0001-9719-3491](https://orcid.org/0000-0001-9719-3491))
4. **Rafy Aulia Akbar, S.Kom., M.Kom.** ([ORCID: 0009-0003-6991-0694](https://orcid.org/0009-0003-6991-0694))

### 16.2 Citation Entries
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
