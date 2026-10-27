# Master AI Agent Reference Guide: Intersectional Face Race & Gender Classification via Multi-Domain Vision Transformer Feature Fusion

> **Critical Notice to AI Agents:** This file (`README.ai.md`) is the authoritative, self-contained single source of truth and comprehensive operational manual for this research repository. Any AI agent entering this project should read this document to understand the full context, research background, model architecture, dataset, feature extraction protocols, dual 28-model experimental benchmark (Subject-Disjoint Primary Benchmark vs. Subject-Overlap Historical Baseline), official IEEE Access peer review dossier, submission compliance artifacts, codebase utilities, reproduction workflows, and scientific writing rules without needing to explore or reconstruct context from disparate files.

---

## 📑 Table of Contents

1. [Executive Summary & Manuscript Identity](#1-executive-summary--manuscript-identity)
2. [Current Publication Journey & Peer Review Dossier (`paper_reviews_ieee/`)](#2-current-publication-journey--peer-review-dossier-paper_reviews_ieee)
3. [Research Architecture & Methodological Pipeline](#3-research-architecture--methodological-pipeline)
4. [Dataset Specifications, Label Encodings & Dual Partitioning Protocol](#4-dataset-specifications-label-encodings--dual-partitioning-protocol)
5. [Feature Extraction & 7 Ablation Schemes](#5-feature-extraction--7-ablation-schemes)
6. [Classical Classifier Pipeline & Exhaustive GridSearchCV Optimization](#6-classical-classifier-pipeline--exhaustive-gridsearchcv-optimization)
7. [Comprehensive Dual Experimental Benchmark](#7-comprehensive-dual-experimental-benchmark)
   - 7.1 [Primary Benchmark: Subject-Disjoint Leaderboard (28 Models)](#71-primary-benchmark-subject-disjoint-leaderboard-28-models)
   - 7.2 [Historical Benchmark: Subject-Overlap Leaderboard (28 Models)](#72-historical-benchmark-subject-overlap-leaderboard-28-models)
   - 7.3 [Comparative Data Leakage Ablation & Generalization Analysis](#73-comparative-data-leakage-ablation--generalization-analysis)
   - 7.4 [Inferential Hypothesis Testing & Statistical Significance (Paired McNemar Tests)](#74-inferential-hypothesis-testing--statistical-significance-paired-mcnemar-tests)
8. [Intersectional Subgroup Performance, Confusion Matrix & Fairness Profile](#8-intersectional-subgroup-performance-confusion-matrix--fairness-profile)
9. [Comparison with Prior Studies on DemogPairs & Contextual Literature](#9-comparison-with-prior-studies-on-demogpairs--contextual-literature)
10. [Repository Architecture & File Inventory](#10-repository-architecture--file-inventory)
11. [Submission Compliance & Packaging (`paper_submission/` & `upload/`)](#11-submission-compliance--packaging-paper_submission--upload)
12. [Internal Mock Peer Review Suite (`paper_reviews/`) & Agent Skills (`.agents/skills/`)](#12-internal-mock-peer-review-suite-paper_reviews--agent-skills-agentsskills)
13. [Python Utilities Library Reference (`experiment/code/utils/`)](#13-python-utilities-library-reference-experimentcodeutils)
14. [Execution, Reproduction & Manuscript Compilation Workflows](#14-execution-reproduction--manuscript-compilation-workflows)
15. [Scientific Claim Boundaries & Academic Writing Constraints (28 Directives)](#15-scientific-claim-boundaries--academic-writing-constraints-28-directives)
16. [Key Authors, Academic Provenance & Citation Metadata](#16-key-authors-academic-provenance--citation-metadata)

---

## 1. Executive Summary & Manuscript Identity

### 1.1 Core Metadata
- **Repository Title / Working Directory:** `face-race-gender-multi-vit` (`D:\Research\face-race-gender-multi-vit`)
- **Primary Corpus Authors:** Dr. Ir. Ricky Eka Putra, S.Kom., M.Kom. (Corresponding Author, `rickyeka@unesa.ac.id`), Rezky Arisanti Putri, S.Kom., M.Kom., Dr. Yuni Yamasari, S.Kom., M.Kom., Rafy Aulia Akbar, S.Kom., M.Kom.
- **Affiliation:** Department of Informatics, Faculty of Informatics, Universitas Negeri Surabaya (UNESA), Surabaya, East Java, Indonesia.
- **Target Journal:** **IEEE Access** (Open Access, Q1, Impact Factor: 3.4).
- **Official Manuscript Tracking ID:** **`Access-2026-50857`**.
- **Manuscript Title:** *Multi-Domain Vision Transformer Fusion for Intersectional Demographic Classification from Facial Images*.
- **Current Milestone:** Editorial Decision Received on **October 20, 2026** (Binary Review Outcome: Reject & Resubmit with exactly 1 resubmission opportunity permitted).
- **Major Milestone Objective:** Complete resolution of Reviewer 2 Comment #2 regarding identity overlap and cross-subject generalization through a dual-benchmark architecture.

### 1.2 Core Research Paradigm
The study proposes an offline feature fusion framework for 6-class intersectional demographic classification (3 Races × 2 Genders: Asian/Black/White × Female/Male) from facial images. The system extracts task-associated latent representations from three frozen, specialized pre-trained Vision Transformer (ViT-Base) backbones:
1. **ViT-Face** (`skutaada/VIT-VGGFace`): Captures static craniofacial biometrics and identity-related spatial geometry.
2. **ViT-Emotion** (`dima806/facial_emotions_image_detection`): Captures dynamic affective expressions and localized facial action units.
3. **ViT-Age** (`dima806/facial_age_image_detection`): Captures biological aging morphology and epidermal texture patterns.

High-level `[CLS]` token vectors (768-d per domain) are concatenated into a **Tri-Domain representation** ($\mathbf{z}_{\text{tri}} \in \mathbb{R}^{2304}$) and fed into downstream classical classifiers optimized through exhaustive 5-Fold Stratified GridSearchCV (evaluating 1,086 hyperparameter combinations and 38,010 total cross-validation fits across 4 classifier families: SVM, Logistic Regression, Random Forest, and Gaussian Naive Bayes).

### 1.3 Dual Benchmark Architecture & Key Achievements

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                   DEMOGPAIRS DATASET                                   │
│                 10,800 Facial Images │ 600 Unique Subjects (18 images/subject)         │
│                 6 Intersectional Classes (1,800 images per demographic class)          │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │
                    ┌───────────────────────┴───────────────────────┐
                    ▼                                               ▼
┌───────────────────────────────────────┐       ┌───────────────────────────────────────┐
│       PRIMARY BENCHMARK REVISION      │       │     HISTORICAL BASELINE ARCHIVE       │
│      (Subject-Disjoint Partition)     │       │       (Subject-Overlap Split)         │
│ ───────────────────────────────────── │       │ ───────────────────────────────────── │
│ • 480 Train Subjects (8,640 images)   │       │ • Image-level 80/20 random partition  │
│ • 120 Held-Out Subjects (2,160 images)│       │ • 593/593 subjects overlap in test set│
│ • Identity Leakage: 0.00% (Zero)      │       │ • Identity Leakage: 100.00%           │
│ • Best: LR Tri (88.66%) / SVM (88.61%)│       │ • Best: SVM Tri (93.70%)              │
│ • Location: experiment/code/results/  │       │ • Location: experiment/code/archive/  │
└───────────────────────────────────────┘       └───────────────────────────────────────┘
```

1. **Primary Benchmark: Subject-Disjoint Partitioning (Zero Identity Leakage — IEEE Access Revision Milestone):**
   - **Top-Performing Model:** **Logistic Regression (LR) + Tri-Domain ViT Fusion** (`vit-face-emotion-age`, 2,304-d)
     - **Test Accuracy:** **88.66%** (1,915 correct out of 2,160 held-out test samples from 120 unseen subjects).
     - **Macro Precision:** **0.8875** | **Macro Recall:** **0.8866** | **Macro F1-Score:** **0.8868**
     - **95% Wilson Score CI:** **[87.25%, 89.93%]**
     - **Inference Latency:** **0.0054 ms/sample** (>800x faster than SVM)
     - **Model Storage:** **0.11 MB** (>330x smaller than SVM)
     - **Best Hyperparameters:** $C = 0.1$, solver = `'saga'`, max_iter = 500, Scaler = `'MinMaxScaler'`, PCA = `None`.
   - **Runner-Up Model:** **Support Vector Machine (SVM) + Tri-Domain ViT Fusion** (`vit-face-emotion-age`, 2,304-d)
     - **Test Accuracy:** **88.61%** (1,914 correct out of 2,160 test samples).
     - **Macro Precision:** **0.8871** | **Macro Recall:** **0.8861** | **Macro F1-Score:** **0.8863**
     - **95% Wilson Score CI:** **[87.20%, 89.88%]**
     - **Best Hyperparameters:** $C = 10$, kernel = `'rbf'`, gamma = `'scale'`, Scaler = `'MinMaxScaler'`, PCA = `None`.
   - **Statistical Equivalence (LR vs. SVM):** McNemar test confirms $p = 1.0000$ (net gain +1 image), showing exact performance parity while LR provides overwhelming edge computing advantages.
   - **Tri-Domain Dominance:** Tri-domain fusion achieves peak performance on **3 of the 4 classifiers** under subject-disjoint conditions (LR: 88.66%, SVM: 88.61%, RF: 85.00%). GNB peaks on dual-domain `Emotion ⊕ Face` (84.31%).

2. **Historical Benchmark: Subject-Overlap Baseline (100% Identity Leakage Baseline):**
   - **Top-Performing Configuration:** **Support Vector Machine (SVM) + Tri-Domain ViT Fusion**
     - **Test Accuracy:** **93.70%** (2,024 correct out of 2,160 held-out test samples).
     - **Macro Precision:** **0.9372** | **Macro Recall:** **0.9370** | **Macro F1-Score:** **0.9369**
     - **Best Hyperparameters:** $C = 10$, kernel = `'poly'`, degree = 2, gamma = `'scale'`, Scaler = `None`, PCA = `None`.
   - **Role in Revision:** Retained in full to provide an empirical basis for **Section IV: Data Leakage & Generalization Comparative Analysis**, directly satisfying IEEE Access Reviewer 2 Comment #2.

3. **Core Comparative Finding:**
   The nominal accuracy drop of ~4.0% to 5.1% on unseen subjects (93.70% $\to$ 88.61% on SVM; 92.73% $\to$ 88.66% on LR) empirically quantifies the removal of identity memorization. Crucially, **paired McNemar testing proves that multi-domain ViT fusion remains statistically significantly superior to single-domain face biometrics ($p = 3.46 \times 10^{-6} < 0.001$ on SVM; $p = 6.78 \times 10^{-6} < 0.001$ on LR)**, confirming that multi-domain gains are genuine and generalizable across unseen identities.

---

## 2. Current Publication Journey & Peer Review Dossier (`paper_reviews_ieee/`)

The manuscript was formally submitted to IEEE Access and received an official editorial decision letter on October 20, 2026. The peer review dossier is curated in [`paper_reviews_ieee/`](paper_reviews_ieee/).

### 2.1 Editorial Decision Overview
- **Associate Editor:** Dr. Vincenzo Conti (`vincenzo.conti@unikore.it`, `vinc.conti@gmail.com`).
- **Article Administrator:** Mr. Adesh Choudhary (`adesh.choudhary@ieee.org`).
- **Decision Date:** 20-10-2026.
- **Decision Type:** Rejected under IEEE Access's binary peer review model, with an explicit invitation to resubmit as a revised manuscript.
- **Resubmission Opportunity:** Exactly **ONE** opportunity to resubmit is permitted.
- **Resubmission Portal URL:** [IEEE Author Portal Resubmission Board](https://ieee.atyponrex.com/journal/ieee-access).

### 2.2 Curated Files in `paper_reviews_ieee/`
| File | Path | Role & Content |
|---|---|---|
| **Editorial Decision & Reviews** | [`IEEE-Access_Decision-on-Manuscript-ID-Access-2026-50857.md`](paper_reviews_ieee/IEEE-Access_Decision-on-Manuscript-ID-Access-2026-50857.md) | Official decision letter, submission link, required 3 files, Reviewer 1 (7 comments) & Reviewer 2 (10 comments) with questionnaires. |
| **Response to Reviewers Template** | [`IEEE-Access_Response-to-Reviewers-template.md`](paper_reviews_ieee/IEEE-Access_Response-to-Reviewers-template.md) | Standard IEEE Access response structure: point-by-point reviewer concerns, author responses, and author actions taken. |
| **Request for Byline Change** | [`Request-for-Byline-Change.md`](paper_reviews_ieee/Request-for-Byline-Change.md) | Official form and detailed justification required if the author list/order changes between original and revised submissions. |
| **Resubmission Checklist** | [`Resubmission-Checklist.md`](paper_reviews_ieee/Resubmission-Checklist.md) | 10-point compliance checklist: reviewer responses, grammar tools/discounts, math formulas, references, highlighted PDF, and main files. |

### 2.3 Detailed Deconstruction of Reviewer Comments

#### Reviewer 1 (Acceptable with Revisions; 7 Core Comments)
1. **Introduction Length:** Tighten Section I to improve focus.
2. **Related Works & Equations:** Structure Section II better and integrate formal mathematical formulations.
3. **Figure 3 Redesign:** Redesign ViT diagram in Figure 3 for clearer visual articulation of patch projection and feature extraction.
4. **Figure 4 Discussion:** Deepen empirical discussion around visual representations.
5. **Experimental Details & Time Cost:** Report execution times, detailed dataset specifications, and concrete contributions.
6. **Broader Method Comparisons:** Frame comparisons against contextual baselines rigorously.
7. **Conclusion Section:** Revise Section V to reflect actual contributions concisely.

#### Reviewer 2 (Substantial Methodological & Statistical Scrutiny; 10 Core Comments)
1. **Novelty & Methodological Contribution:** Clarify methodological contribution of tri-domain feature fusion over simple concatenation.
2. **Data Leakage & Subject-Disjoint Generalization:** **(CRITICAL CONCERN)** Inquire whether images of the same identity appear in both train and test partitions under random splitting; request evaluation under strict subject-disjoint conditions.
3. **Preprocessing & Reproducibility:** Specify exact HuggingFace checkpoint identifiers, image processor parameters, and normalization routines.
4. **Hyperparameter Search Space Consistency:** Reconcile reported search space metrics (1,086 combinations, 38,010 cross-validation fits, 28 final refits).
5. **Statistical Significance & McNemar Test:** Report inferential statistical hypothesis testing (McNemar test) to validate performance differences and qualify claims of tri-domain superiority.
6. **Fairness Analysis Scope:** Refine scope of fairness claims; note that EOD provides subgroup disparity insight but does not constitute an exhaustive algorithmic fairness audit.
7. **Baseline Benchmark Conditions:** Clarify whether prior methods evaluated on DemogPairs used identical partitions; treat them contextually.
8. **Computational Efficiency Profiling:** Report feature extraction latency, classifier training time, inference latency per sample, memory footprint, and model disk size.
9. **Phenotypic & Visual Overlap Interpretation:** Qualify statements regarding phenotypic and age-related overlap.
10. **Scope of Conclusions & Limitations:** Explicitly limit conclusions to DemogPairs demographic categories.

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
                    [ 5-Fold Stratified Subject-Disjoint GridSearchCV ]
                      (Logistic Regression / SVM / Random Forest / GNB)
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
- **Final Feature Extraction:** Backbones are frozen; feature vector is the normalized `[CLS]` token ($\mathbf{z}_L^0$) from the final layer $L = 12$:
  $$\mathbf{f}_{\text{domain}} = \text{LayerNorm}(\mathbf{z}_L^0) \in \mathbb{R}^{768}$$

### 3.2 ViT Backbone Specifications
| Backbone | HuggingFace Identifier | Pre-training Task & Domain | Representation Visual Cues |
|---|---|---|---|
| **ViT-Face** | `skutaada/VIT-VGGFace` | Facial Biometric Recognition (VGGFace) | Craniofacial bone structure, ocular distance, static facial proportions |
| **ViT-Emotion** | `dima806/facial_emotions_image_detection` | Affective State & Facial Expression | Micro-expressions, muscular activation around mouth, brows, and eyes |
| **ViT-Age** | `dima806/facial_age_image_detection` | Biological Age Estimation | Epidermal elasticity, nasolabial folds, periocular wrinkles, aging morphology |

---

## 4. Dataset Specifications, Label Encodings & Dual Partitioning Protocol

### 4.1 Benchmark Dataset: DemogPairs
- **Primary Citation:** I. Hupont and C. Fernández, "DemogPairs: Quantifying the Impact of Demographic Imbalance in Deep Face Recognition," *IEEE FG 2019*, DOI: `10.1109/FG.2019.8756625`.
- **Dataset Composition:** 10,800 facial images from 600 unique identities (100 subjects per demographic group, 18 high-resolution images per subject).
- **Class Balance:** Perfectly balanced across 6 intersectional demographic subgroups (1,800 images each).

### 4.2 Label Encodings
- **`DEMOGPairs_LABEL_TO_IDX` (in [`experiment/code/utils/constants.py`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/utils/constants.py)):**
  - `Black_Males`: `0` | `White_Females`: `1` | `Asian_Males`: `2` | `White_Males`: `3` | `Black_Females`: `4` | `Asian_Females`: `5`
- **Alphabetical Class Ordering (`DEMOGPairs_CLASSES`):**
  `['Asian_Females', 'Asian_Males', 'Black_Females', 'Black_Males', 'White_Females', 'White_Males']`
- **Evaluation Alignment:** In `utils/evaluation.py`, confusion matrices and classification reports explicitly use `labels=[DEMOGPairs_LABEL_TO_IDX[n] for n in target_names]` to prevent axis inversion.

### 4.3 Dual Partitioning Protocol Specification

#### Protocol A: Strict Subject-Disjoint Partitioning (Primary Benchmark — Revision Milestone)
- **Implementation:** `split_demogpairs_subject_disjoint` in `utils/dataset.py`.
- **Identity Split:** 600 unique subjects partitioned strictly by identity:
  - **Training Set:** 80 subjects per class $\times$ 6 classes = **480 unique subjects** ($N = 8,640$ images; 1,440 per class).
  - **Held-Out Test Set:** 20 subjects per class $\times$ 6 classes = **120 unique subjects** ($N = 2,160$ images; 360 per class).
- **Identity Overlap:** **0.00% (Zero)**. No subject identity present in the test partition ever appeared in training.
- **Cross-Validation:** 5-Fold Stratified Group K-Fold executed strictly within the 480 training subjects.
- **Location of Active Artifacts:** Notebooks at `experiment/code/`, models in `experiment/code/models/`, results in `experiment/code/results/`.

#### Protocol B: Subject-Overlap Partitioning (Historical Baseline — Data Leakage Ablation)
- **Implementation:** Image-level stratified split (`train_test_split(..., test_size=0.2, random_state=42, stratify=y)`).
- **Identity Overlap:** **100.00%**. All 593 test identities appeared in the training set under different poses/lighting.
- **Location of Archived Artifacts:** Entire legacy suite preserved under `experiment/code/archive/` (`notebook_old/`, `models_old/`, `results_old/`, `md_old/`, `audit_ledger.json`).

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
Serialized feature dictionaries mapping relative image paths to 768-d NumPy arrays (`float32`) stored in `experiment/code/features/`:
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

## 7. Comprehensive Dual Experimental Benchmark

### 7.1 Primary Benchmark: Subject-Disjoint Leaderboard (28 Models)
Evaluated on the held-out subject-disjoint test partition ($N = 2,160$ samples from 120 unseen subjects). Data extracted directly from active JSON files in `experiment/code/results/*.json`:

| Rank | Classifier | Feature Scheme | Category | Dim | Test Accuracy | Precision | Recall | F1-Score | 95% CI (Wilson) | Latency (ms) | Size (MB) | Best Hyperparameters |
|:---:|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 🥇 **1** | **LR** | **`vit-face-emotion-age`** | **Tri** | **2,304** | **88.66%** | **0.8875** | **0.8866** | **0.8868** | **[87.25%, 89.93%]** | **0.0054** | **0.11** | `C=0.1, solver='saga', max_iter=500, scaler=MinMaxScaler, pca=None` |
| 🥈 **2** | **SVM** | **`vit-face-emotion-age`** | **Tri** | **2,304** | **88.61%** | **0.8871** | **0.8861** | **0.8863** | **[87.20%, 89.88%]** | 4.4481 | 36.60 | `C=10, kernel='rbf', gamma='scale', scaler=MinMaxScaler, pca=None` |
| 🥉 **3** | SVM | `vit-emotion-face` | Dual | 1,536 | **88.43%** | 0.8850 | 0.8843 | 0.8844 | [87.01%, 89.71%] | 0.9707 | 15.27 | `C=10, kernel='rbf', gamma='scale', scaler=MinMaxScaler, pca=None` |
| 4 | SVM | `vit-face-age` | Dual | 1,536 | 87.55% | 0.8766 | 0.8755 | 0.8757 | [86.09%, 88.87%] | 2.2581 | 23.48 | `C=10, kernel='rbf', gamma='scale', scaler=MinMaxScaler, pca=None` |
| 5 | LR | `vit-emotion-face` | Dual | 1,536 | 87.45% | 0.8759 | 0.8745 | 0.8749 | [85.99%, 88.78%] | 0.0039 | 0.08 | `C=0.1, solver='saga', max_iter=500, scaler=MinMaxScaler, pca=None` |
| 6 | LR | `vit-face-age` | Dual | 1,536 | 87.41% | 0.8744 | 0.8741 | 0.8740 | [85.94%, 88.74%] | 0.0090 | 0.11 | `C=0.1, solver='saga', max_iter=500, scaler=MinMaxScaler, pca=None` |
| 7 | LR | `vit-emotion-age` | Dual | 1,536 | 86.67% | 0.8668 | 0.8667 | 0.8667 | [85.17%, 88.04%] | 0.0040 | 0.08 | `C=0.1, solver='saga', max_iter=500, scaler=MinMaxScaler, pca=None` |
| 8 | LR | `vit-face` | Single | 768 | 86.39% | 0.8646 | 0.8639 | 0.8640 | [84.88%, 87.77%] | 0.0008 | 0.04 | `C=1, solver='saga', max_iter=500, scaler=MinMaxScaler, pca=None` |
| 9 | SVM | `vit-emotion-age` | Dual | 1,536 | 86.25% | 0.8626 | 0.8625 | 0.8624 | [84.73%, 87.64%] | 3.1451 | 32.76 | `C=10, kernel='rbf', gamma='scale', scaler=MinMaxScaler, pca=None` |
| 10 | SVM | `vit-face` | Single | 768 | 86.16% | 0.8624 | 0.8616 | 0.8619 | [84.64%, 87.55%] | 3.0653 | 7.56 | `C=10, kernel='rbf', gamma='scale', scaler=MinMaxScaler, pca=None` |
| 11 | SVM | `vit-emotion` | Single | 768 | 85.79% | 0.8584 | 0.8579 | 0.8580 | [84.25%, 87.20%] | 1.8871 | 15.30 | `C=10, kernel='rbf', gamma='scale', scaler=MinMaxScaler, pca=None` |
| 12 | LR | `vit-emotion` | Single | 768 | 85.23% | 0.8535 | 0.8523 | 0.8527 | [83.67%, 86.67%] | 0.0037 | 0.06 | `C=0.1, solver='saga', max_iter=500, scaler=MinMaxScaler, pca=None` |
| 13 | RF | `vit-face-emotion-age` | Tri | 2,304 | 85.00% | 0.8506 | 0.8500 | 0.8493 | [83.43%, 86.44%] | 0.0537 | 6.19 | `n_estimators=200, max_depth=None, max_features='sqrt', min_samples_split=2, min_samples_leaf=1, pca=PCA(0.75), scaler=None` |
| 14 | RF | `vit-emotion-face` | Dual | 1,536 | 84.86% | 0.8493 | 0.8486 | 0.8479 | [83.29%, 86.31%] | 0.0316 | 8.58 | `n_estimators=200, max_depth=None, max_features='sqrt', min_samples_split=2, min_samples_leaf=1, pca=PCA(0.75), scaler=None` |
| 15 | RF | `vit-face-age` | Dual | 1,536 | 84.86% | 0.8488 | 0.8486 | 0.8478 | [83.29%, 86.31%] | 0.0310 | 6.19 | `n_estimators=200, max_depth=None, max_features='sqrt', min_samples_split=2, min_samples_leaf=1, pca=PCA(0.75), scaler=None` |
| 16 | GNB | `vit-emotion-face` | Dual | 1,536 | 84.31% | 0.8437 | 0.8431 | 0.8430 | [82.71%, 85.78%] | 0.0083 | 0.78 | `var_smoothing=0.005878, pca=PCA(0.75), scaler=MinMaxScaler` |
| 17 | RF | `vit-face` | Single | 768 | 84.03% | 0.8413 | 0.8403 | 0.8403 | [82.42%, 85.51%] | 0.0314 | 5.99 | `n_estimators=200, max_depth=None, max_features='sqrt', min_samples_split=2, min_samples_leaf=1, pca=PCA(0.75), scaler=None` |
| 18 | GNB | `vit-face-emotion-age` | Tri | 2,304 | 83.61% | 0.8379 | 0.8361 | 0.8364 | [81.99%, 85.11%] | 0.0081 | 1.36 | `var_smoothing=0.005878, pca=PCA(0.75), scaler=None` |
| 19 | GNB | `vit-face-age` | Dual | 1,536 | 83.06% | 0.8347 | 0.8306 | 0.8310 | [81.42%, 84.58%] | 0.0080 | 0.75 | `var_smoothing=0.011253, pca=PCA(0.75), scaler=MinMaxScaler` |
| 20 | SVM | `vit-age` | Single | 768 | 82.55% | 0.8268 | 0.8255 | 0.8258 | [80.89%, 84.09%] | 2.0104 | 18.22 | `C=10, kernel='rbf', gamma='scale', scaler=MinMaxScaler, pca=None` |
| 21 | GNB | `vit-face` | Single | 768 | 82.55% | 0.8268 | 0.8255 | 0.8250 | [80.89%, 84.09%] | 0.0031 | 0.19 | `var_smoothing=0.041246, pca=PCA(0.75), scaler=MinMaxScaler` |
| 22 | LR | `vit-age` | Single | 768 | 81.48% | 0.8145 | 0.8148 | 0.8146 | [79.79%, 83.06%] | 0.0028 | 0.06 | `C=0.1, solver='saga', max_iter=500, scaler=MinMaxScaler, pca=None` |
| 23 | RF | `vit-emotion-age` | Dual | 1,536 | 77.31% | 0.7734 | 0.7731 | 0.7728 | [75.50%, 79.03%] | 0.0392 | 12.35 | `n_estimators=200, max_depth=None, max_features='log2', min_samples_split=5, min_samples_leaf=2, pca=PCA(0.75), scaler=None` |
| 24 | RF | `vit-emotion` | Single | 768 | 76.11% | 0.7602 | 0.7611 | 0.7603 | [74.27%, 77.86%] | 0.0316 | 10.34 | `n_estimators=200, max_depth=None, max_features='log2', min_samples_split=5, min_samples_leaf=1, pca=PCA(0.75), scaler=None` |
| 25 | GNB | `vit-emotion-age` | Dual | 1,536 | 75.88% | 0.7597 | 0.7588 | 0.7578 | [74.03%, 77.64%] | 0.0048 | 0.24 | `var_smoothing=0.001604, pca=PCA(0.75), scaler=MinMaxScaler` |
| 26 | GNB | `vit-emotion` | Single | 768 | 72.13% | 0.7251 | 0.7213 | 0.7199 | [70.20%, 73.98%] | 0.0031 | 0.13 | `var_smoothing=0.003070, pca=PCA(0.75), scaler=None` |
| 27 | RF | `vit-age` | Single | 768 | 71.81% | 0.7176 | 0.7181 | 0.7170 | [69.87%, 73.66%] | 0.0327 | 11.21 | `n_estimators=200, max_depth=30, max_features='log2', min_samples_split=2, min_samples_leaf=1, pca=PCA(0.75), scaler=None` |
| 28 | GNB | `vit-age` | Single | 768 | 67.08% | 0.6691 | 0.6708 | 0.6686 | [65.07%, 69.03%] | 0.0045 | 0.37 | `var_smoothing=0.000438, pca=PCA(0.75), scaler=MinMaxScaler` |

### 7.2 Historical Benchmark: Subject-Overlap Leaderboard (28 Models)
Preserved in `experiment/code/archive/results_old/*.json` and `audit_ledger.json` as the comparative baseline:

| Rank | Classifier | Feature Scheme | Category | Dim | Test Accuracy | Precision | Recall | F1-Score | Best Hyperparameters |
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
| 16 | RF | `vit-face-emotion-age` | Tri | 2,304 | 0.8620 | 0.8620 | 0.8620 | 0.8613 | `n_estimators=200, max_depth=30, max_features='sqrt', min_samples_split=5, min_samples_leaf=1, pca=PCA(0.75), scaler=None` |
| 17 | RF | `vit-face-age` | Dual | 1,536 | 0.8579 | 0.8578 | 0.8579 | 0.8573 | `n_estimators=200, max_depth=None, max_features='sqrt', min_samples_split=2, min_samples_leaf=1, pca=PCA(0.75), scaler=None` |
| 18 | RF | `vit-face` | Single | 768 | 0.8546 | 0.8543 | 0.8546 | 0.8539 | `n_estimators=200, max_depth=30, max_features='log2', min_samples_split=2, min_samples_leaf=1, pca=PCA(0.75), scaler=MinMaxScaler` |
| 19 | GNB | `vit-face-emotion-age` | Tri | 2,304 | 0.8505 | 0.8512 | 0.8505 | 0.8505 | `var_smoothing=0.005878, pca=PCA(0.75), scaler=None` |
| 20 | GNB | `vit-emotion-face` | Dual | 1,536 | 0.8486 | 0.8490 | 0.8486 | 0.8481 | `var_smoothing=0.005878, pca=PCA(0.75), scaler=MinMaxScaler` |
| 21 | GNB | `vit-face-age` | Dual | 1,536 | 0.8315 | 0.8343 | 0.8315 | 0.8317 | `var_smoothing=0.011253, pca=PCA(0.75), scaler=MinMaxScaler` |
| 22 | GNB | `vit-face` | Single | 768 | 0.8269 | 0.8271 | 0.8269 | 0.8258 | `var_smoothing=0.041246, pca=PCA(0.75), scaler=MinMaxScaler` |
| 23 | RF | `vit-emotion-age` | Dual | 1,536 | 0.8111 | 0.8111 | 0.8111 | 0.8108 | `n_estimators=200, max_depth=None, max_features='log2', min_samples_split=5, min_samples_leaf=2, pca=PCA(0.75), scaler=None` |
| 24 | RF | `vit-emotion` | Single | 768 | 0.8060 | 0.8063 | 0.8060 | 0.8057 | `n_estimators=200, max_depth=None, max_features='log2', min_samples_split=5, min_samples_leaf=1, pca=PCA(0.75), scaler=None` |
| 25 | GNB | `vit-emotion-age` | Dual | 1,536 | 0.7681 | 0.7686 | 0.7681 | 0.7681 | `var_smoothing=0.001604, pca=PCA(0.75), scaler=MinMaxScaler` |
| 26 | RF | `vit-age` | Single | 768 | 0.7366 | 0.7363 | 0.7366 | 0.7354 | `n_estimators=200, max_depth=30, max_features='log2', min_samples_split=2, min_samples_leaf=1, pca=PCA(0.75), scaler=None` |
| 27 | GNB | `vit-emotion` | Single | 768 | 0.7338 | 0.7387 | 0.7338 | 0.7329 | `var_smoothing=0.003070, pca=PCA(0.75), scaler=None` |
| 28 | GNB | `vit-age` | Single | 768 | 0.6963 | 0.6979 | 0.6963 | 0.6952 | `var_smoothing=0.000438, pca=PCA(0.75), scaler=MinMaxScaler` |

### 7.3 Comparative Data Leakage Ablation & Generalization Analysis
Directly answering Reviewer 2 Comment #2, comparing the two benchmarks establishes the exact cost of identity memorization:

| Classifier | Scheme | Subject-Overlap Acc | Subject-Disjoint Acc | $\Delta\text{Acc}$ (Drop) | 95% Wilson Score CI |
|---|---|:---:|:---:|:---:|:---:|
| **SVM** | `vit-face-emotion-age` | 93.70% | 88.61% | -5.09 pp | [87.20%, 89.88%] |
| **SVM** | `vit-emotion-face` | 93.29% | 88.43% | -4.86 pp | [87.01%, 89.71%] |
| **SVM** | `vit-face` | 90.83% | 86.16% | -4.68 pp | [84.64%, 87.55%] |
| **LR** | `vit-face-emotion-age` | 92.73% | 88.66% | -4.07 pp | [87.25%, 89.93%] |
| **LR** | `vit-emotion-face` | 92.41% | 87.45% | -4.95 pp | [85.99%, 88.78%] |
| **LR** | `vit-face` | 90.60% | 86.39% | -4.21 pp | [84.88%, 87.77%] |
| **RF** | `vit-face-emotion-age` | 86.20% | 85.00% | -1.20 pp | [83.43%, 86.44%] |
| **GNB** | `vit-face-emotion-age` | 85.05% | 83.61% | -1.44 pp | [81.99%, 85.11%] |

### 7.4 Inferential Hypothesis Testing & Statistical Significance (Paired McNemar Tests)
Calculated from discordant pairs contingency tables ($N = 2,160$) with Edwards continuity correction:

1. **Tri-Domain vs. Single-Domain (`vit-face`):**
   - **SVM:** Tri-Domain (88.61%) vs. Face (86.16%) $\implies \Delta = +2.45\%$, Net Gain = $+53$ images ($b=91, c=38$), $\chi^2 = 20.9612$, **$p = 3.46 \times 10^{-6} < 0.001$ (Statistically Highly Significant)**.
   - **Logistic Regression:** Tri-Domain (88.66%) vs. Face (86.39%) $\implies \Delta = +2.27\%$, Net Gain = $+49$ images ($b=83, c=34$), $\chi^2 = 19.6923$, **$p = 6.78 \times 10^{-6} < 0.001$ (Statistically Highly Significant)**.
   - **Random Forest:** Tri-Domain (85.00%) vs. Face (84.03%) $\implies \Delta = +0.97\%$, Net Gain = $+21$ images ($b=50, c=29$), $\chi^2 = 5.0633$, **$p = 0.0238 < 0.05$ (Significant)**.
   - **Gaussian Naive Bayes:** Tri-Domain (83.61%) vs. Face (82.55%) $\implies \Delta = +1.06\%$, Net Gain = $+23$ images ($b=97, c=74$), $\chi^2 = 2.8304$, $p = 0.0922$ (Not significant).
2. **Tri-Domain vs. Dual-Domain (`vit-emotion-face`):**
   - **Logistic Regression:** Tri-Domain (88.66%) vs. Dual-Domain (87.45%) $\implies \Delta = +1.20\%$, Net Gain = $+26$ images ($b=57, c=31$), $\chi^2 = 7.1023$, **$p = 0.0073 < 0.01$ (Significant)**.
   - **SVM:** Tri-Domain (88.61%) vs. Dual-Domain (88.43%) $\implies \Delta = +0.19\%$, Net Gain = $+4$ images ($b=41, c=37$), $\chi^2 = 0.1154$, $p = 0.7343$ (Not significant; proves asymptotic feature saturation on RBF kernel).
3. **Pinnacle Architecture Comparison (LR Tri vs. SVM Tri):**
   - LR Tri (88.66%) vs. SVM Tri (88.61%) $\implies \Delta = +0.05\%$, Net Gain = $+1$ image ($b=36, c=35$), $\chi^2 = 0.0000$, **$p = 1.0000$ (Statistically Equivalent)**.
   - Efficiency Trade-off: LR is **>800x faster in inference** (0.0054 ms vs 4.4481 ms) and **>330x more compact** (0.11 MB vs 36.60 MB).

---

## 8. Intersectional Subgroup Performance, Confusion Matrix & Fairness Profile

### 8.1 Subgroup Performance on Subject-Disjoint Benchmark ($N = 2,160$)

#### (a) Logistic Regression Tri-Domain (Top Benchmark Model: 88.66%)
| Demographic Subgroup | Macro Race | Gender | Support | Recall / TPR | Precision | F1-Score |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **White_Males** | White | Male | 360 | **94.44%** | **95.24%** | **94.84%** |
| **White_Females** | White | Female | 360 | 90.56% | 91.32% | 90.93% |
| **Black_Males** | Black | Male | 360 | 87.78% | 91.59% | 89.65% |
| **Asian_Males** | Asian | Male | 360 | 87.78% | 82.72% | 85.18% |
| **Asian_Females** | Asian | Female | 360 | 86.67% | 86.43% | 86.55% |
| **Black_Females** | Black | Female | 360 | 84.72% | 85.20% | 84.96% |
| **Macro Average** | **All** | **All** | **2,160** | **88.66%** | **0.8875** | **0.8868** |

*Equal Opportunity Difference (Max - Min Recall): **9.72 percentage points** (94.44% - 84.72%).*

#### (b) Support Vector Machine Tri-Domain (88.61%)
| Demographic Subgroup | Macro Race | Gender | Support | Recall / TPR | Precision | F1-Score |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **White_Males** | White | Male | 360 | **94.44%** | 93.92% | **94.18%** |
| **White_Females** | White | Female | 360 | 91.11% | 90.11% | 90.61% |
| **Asian_Males** | Asian | Male | 360 | 88.06% | 82.34% | 85.10% |
| **Black_Males** | Black | Male | 360 | 87.22% | 92.35% | 89.71% |
| **Asian_Females** | Asian | Female | 360 | 86.11% | 85.87% | 85.99% |
| **Black_Females** | Black | Female | 360 | 84.72% | 87.64% | 86.16% |
| **Macro Average** | **All** | **All** | **2,160** | **88.61%** | **0.8871** | **0.8863** |

*Equal Opportunity Difference (Max - Min Recall): **9.72 percentage points**.*

### 8.2 Historical Subject-Overlap Subgroup Metrics (SVM Tri-Domain: 93.70%)
Preserved for comparative reference:
- `White_Males`: Recall 96.94%, Precision 95.36%, F1 96.14%
- `Black_Males`: Recall 94.17%, Precision 95.49%, F1 94.83%
- `White_Females`: Recall 94.72%, Precision 92.41%, F1 93.55%
- `Asian_Males`: Recall 94.44%, Precision 92.39%, F1 93.41%
- `Asian_Females`: Recall 92.50%, Precision 92.50%, F1 92.50%
- `Black_Females`: Recall 89.44%, Precision 94.15%, F1 91.74%
- Disparity: $\Delta\text{F1} = 0.0440$, $\Delta\text{Recall} = 0.0750$.

---

## 9. Comparison with Prior Studies on DemogPairs & Contextual Literature

### 9.1 Comparative Performance on DemogPairs Benchmark
| Reference | Partition Protocol | Architecture | Accuracy | Precision | Recall | F1-Score |
|---|---|---|:---:|:---:|:---:|:---:|
| Putri et al. (*JIEET 2025*) | Random Stratified (Subject-Overlap) | MD-ViT (Face + Age) + XGBoost | 89.07% | 0.8912 | 0.8907 | 0.8901 |
| Putri et al. (*IEEE ICVEE 2025*) | Random Stratified (Subject-Overlap) | Dual-ViT (Face + Emotion) + SVM | 92.41% | 0.9248 | 0.9241 | 0.9238 |
| **Proposed (Historical Baseline)** | **Random Stratified (Subject-Overlap)** | **Tri-Domain ViT + SVM** | **93.70%** | **0.9372** | **0.9370** | **0.9369** |
| **Proposed (Revision Milestone)** | **Subject-Disjoint (Zero Leakage)** | **Tri-Domain ViT + LR** | **88.66%** | **0.8875** | **0.8866** | **0.8868** |
| **Proposed (Revision Milestone)** | **Subject-Disjoint (Zero Leakage)** | **Tri-Domain ViT + SVM** | **88.61%** | **0.8871** | **0.8861** | **0.8863** |

*Important Contextual Distinction:* Prior works (Putri et al. 2025) evaluated under random image-level stratified splitting with identity overlap. On the strict subject-disjoint unseen partition, our tri-domain framework achieves 88.66% (LR) / 88.61% (SVM).

---

## 10. Repository Architecture & File Inventory

```
D:\Research\face-race-gender-multi-vit\
├── README.md                              # Public research documentation & summary
├── README.ai.md                           # Master AI agent reference manual (THIS FILE)
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
│       ├── 2.1.* - 2.5.*.ipynb            # Active Subject-Disjoint classifier notebooks (SVM, GNB, RF, LR)
│       ├── 3.0_compare.ipynb              # Global 28-model comparison and benchmarking (Subject-Disjoint)
│       ├── 3.1_statistical_significance.ipynb # Paired McNemar tests, Wilson Score CIs & EOD analysis
│       ├── 4.0_test.ipynb                 # Held-out evaluation and test routines
│       ├── app.py                         # Interactive Gradio demo web application
│       ├── archive/                       # Historical Subject-Overlap Baseline Archive (Data Leakage Ablation)
│       │   ├── audit_ledger.json          # Consolidated audit ledger comparing 28 Old vs 28 New models
│       │   ├── md_old/                    # Markdown logs (35 files) & confusion matrices of legacy experiments
│       │   ├── models_old/                # Serialized trained weights (.pkl) of 28 legacy models
│       │   ├── notebook_old/              # 35 Jupyter notebooks of legacy experiments
│       │   ├── results_old/               # 28 raw JSON result files of legacy subject-overlap models
│       │   └── README.md                  # Detailed documentation on archive purpose and audit protocol
│       ├── scripts/                       # Autonomous execution runners & automated queue scripts
│       │   ├── auto_run_experiments.py    # Main automated batch runner for all 28 experiment pipelines
│       │   ├── run_gnb_queue.py           # Dedicated queue runner for Gaussian Naive Bayes series
│       │   ├── run_remaining_queue.py     # Resilient queue runner for remaining model workloads
│       │   ├── run_experiments.bat        # Windows batch launcher for auto_run_experiments.py
│       │   ├── run_gnb.bat                # Windows batch launcher for GNB queue
│       │   └── README.md                  # Documentation on runner operations and execution commands
│       ├── utils/                         # Modular Python utility package (constants, dataset, evaluation, etc.)
│       ├── dataset/demogpairs/metadata/   # 6 metadata .txt files (1,800 rows each)
│       ├── features/                      # Serialized 768-d feature embeddings (.pkl)
│       ├── md/                            # Markdown exports of all notebooks & statistical reports
│       ├── models/                        # Serialized trained weights (.pkl) of 28 active models
│       ├── results/                       # 28 raw JSON result files of active Subject-Disjoint models
│       └── images/                        # Confusion matrices and Wilson Score 95% CI plots
│
├── images/                                # High-resolution architecture diagrams and sample figures
├── paper/                                 # Modular manuscript draft in Markdown (IEEE style)
│   ├── 00_abstract.md - 05_conclusion.md  # Core manuscript sections
│   ├── 06_references.md                   # Standardized IEEE bibliography registry (entries [1]-[51])
│   ├── 07_biographies.md                  # Section VII: Biographies & portrait assets
│   ├── acronyms.txt                       # Centralized acronym registry
│   ├── ref_part_*.md                      # 10 modular bibliographic audit logs (entries [1]-[51])
│   ├── references.txt                     # Sentence-level citation tracking & verification registry
│   └── references/                        # 51 bibliographic source files (.bib, .ris, .nbib, .bibtex)
│
├── paper_latex_en/                        # Submission-ready English IEEE Access LaTeX package
│   ├── access.tex / access.pdf            # Master LaTeX entrypoint & compiled PDF
│   ├── ieeeaccess.cls / IEEEtran.bst      # Official IEEE Access style files
│   ├── references.bib                     # Consolidated BibTeX database
│   ├── sections/                          # 21 modular LaTeX sections
│   └── images/                            # Figures and plots for compilation
│
├── paper_latex_id/                        # Reference Indonesian IEEE Access LaTeX package
├── paper_reviews/                         # Internal multi-agent mock peer review audit system (Round 1 & 2)
├── paper_reviews_ieee/                    # Official IEEE Access editorial decision & review dossier
├── paper_submission/                      # Formal submission packaging and IEEE compliance reports
├── template/                              # Raw IEEE Access LaTeX template distribution package
└── upload/                                # Packaged submission artifacts (PDF and source ZIP)
```

---

## 11. Submission Compliance & Packaging (`paper_submission/` & `upload/`)

### 11.1 Directory `paper_submission/`
- `checklist_report.md`: Systematic report auditing compliance with all IEEE Access submission requirements.
- `IEEE Reference Preparation Assistant Report.txt`: Output from the IEEE Reference Preparation Assistant verifying bibliographic metadata format consistency.
- `ieee_taxonomy.txt`: List of controlled vocabulary keywords matching official IEEE taxonomy categories.
- `IEEE-Access-Submission-Checklist.pdf` / `.txt` / `.ID.txt`: Official IEEE Access submission checklist.

### 11.2 Directory `upload/`
- `Multi-Domain Vision Transformer Fusion for Intersectional Demographic Classification from Facial Images.pdf`: The dual-column compiled PDF.
- `Multi-Domain Vision Transformer Fusion for Intersectional Demographic Classification from Facial Images.zip`: The zipped source package containing `access.tex`, `sections/*.tex`, `images/*`, `ieeeaccess.cls`, and `references.bib`.

---

## 12. Internal Mock Peer Review Suite (`paper_reviews/`) & Agent Skills (`.agents/skills/`)

### 12.1 Internal Mock Peer Review System (`paper_reviews/`)
- **`round-1/`**: Desk screening (`00_desk_screening.md`), 5 independent evaluator reviews (EIC, Methodology, Domain, Cross-Perspective, Devil's Advocate), findings matrix, editorial decision, and revision roadmap.
- **`round-2/`**: Verification of revisions, residual issues, response letter validation, rebuttal audit, re-review traceability matrix, and final EIC sign-off.
- **`REVIEW_LOG.md`**: Master audit trail tracking review milestones.

### 12.2 Specialized Autonomous Agent Skills (`.agents/skills/`)
- `ar-paper-reviewer`: Executes independent academic mock reviews across 5 specialized roles based on Contract Sprint Schema 13.
- `ar-paper-revision`: Implements byte-level precision patching (`<!--block:BNNNN-->`), fail-closed validation, and formal Response to Reviewers compilation (Schema 8).
- `ar-paper-revision-coach`: Parses reviewer comments, builds 4-tier issue taxonomies, prioritizes revisions (P1/P2/P3), and generates R&R Traceability Matrices (Schema 11).

---

## 13. Python Utilities Library Reference (`experiment/code/utils/`)

Located at `experiment/code/utils/`, providing unified shared logic across all pipelines:

- **`constants.py`**: Demographic classes (`DEMOGPairs_CLASSES`), index mappings (`DEMOGPairs_LABEL_TO_IDX`, `DEMOGPairs_IDX_TO_LABEL`), random seeds, and plot palettes.
- **`dataset.py`**:
  - `load_demogpairs(metadata_path, images_path) -> list[dict]`: Parses metadata text files.
  - `split_demogpairs_subject_disjoint(...)`: Implements strict subject-disjoint partitioning (480 train / 120 test subjects; 0.00% identity leakage).
- **`extraction.py`**: HuggingFace ViT feature extraction via normalized `[CLS]` token vectors (`(768,)`).
- **`evaluation.py`**: Unified evaluation routines, GridSearchCV pipeline fitting, One-vs-Rest metric generation, and JSON serialization.
- **`serialization.py`**: High-performance Joblib serialization (`save_object`, `load_object`) and formatted JSON serialization.
- **`display.py` & `time_helpers.py`**: Formatted tabular rendering and execution timer utilities.

---

## 14. Execution, Reproduction & Manuscript Compilation Workflows

### 14.1 Python Environment Setup
```bash
conda create -n torch-gpu python=3.11 -y
conda activate torch-gpu
pip install torch torchvision transformers scikit-learn imbalanced-learn joblib pandas numpy pillow matplotlib seaborn tqdm gradio nbconvert
```

### 14.2 Running the Active Pipeline (Subject-Disjoint)

#### Batch Execution via Automated Queue Scripts:
```bash
cd experiment/code
python scripts/auto_run_experiments.py
```

#### Step-by-Step Interactive Execution:
1. **Feature Extraction:** Run notebooks `1.1_vit-face_demogpairs.ipynb`, `1.1_vit-emotion_demogpairs.ipynb`, and `1.1_vit-age_demogpairs.ipynb` sequentially.
2. **Model Training & Optimization:** Execute active classifier notebooks:
   - Logistic Regression: `2.5.1` to `2.5.7`
   - Support Vector Machine: `2.1.1` to `2.1.7`
   - Random Forest: `2.4.1` to `2.4.7`
   - Gaussian Naive Bayes: `2.2.1` to `2.2.7`
3. **Cross-Model Comparison:** Run `3.0_compare.ipynb` to aggregate all 28 JSON result files into a consolidated benchmark leaderboard.
4. **Statistical Significance Testing:** Run `3.1_statistical_significance.ipynb` to generate paired McNemar test matrices, Wilson Score 95% CIs, and EOD fairness evaluations.
5. **Interactive Web Inference:**
   ```bash
   python experiment/code/app.py
   # Launches Gradio interface at http://127.0.0.1:7860
   ```

### 14.3 LaTeX Manuscript Compilation
```bash
# Compile English Submission Manuscript
cd paper_latex_en
pdflatex access.tex
bibtex access
pdflatex access.tex
pdflatex access.tex
```

---

## 15. Scientific Claim Boundaries & Academic Writing Constraints (28 Directives)

When writing, revising, or auditing manuscript drafts, outlining papers, or drafting responses to reviewer comments, any AI agent **MUST** adhere strictly to the following 28 directives:

1. **Dual Partitioning Clarity:** Explicitly differentiate between Subject-Disjoint Partitioning (Primary Benchmark, 0.00% leakage, 88.66% LR / 88.61% SVM) and Subject-Overlap Partitioning (Historical Baseline, 100% leakage, 93.70% SVM). Frame the historical results strictly as a comparative data leakage ablation study.
2. **Cautious Data Leakage Formulation:** State that "the subject-disjoint partitioning protocol isolates all 120 test identities from the training set, eliminating identity memorization leakage."
3. **Balanced Evaluation Setting:** A balanced dataset does not imply demographic bias has been eliminated; refer to it as a "balanced evaluation setting" or "balanced class distribution across subgroups."
4. **Statistical Significance Validation:** The claim that multi-domain ViT representations statistically outperform single face biometrics is formally validated by paired McNemar testing ($p = 3.46 \times 10^{-6} < 0.001$ for SVM; $p = 6.78 \times 10^{-6} < 0.001$ for LR). Always cite the exact p-value and test statistics when using "statistically significant".
5. **Accurate Tri-Domain Scope:** Tri-domain fusion achieves top accuracy on 3 of the 4 classifiers under subject-disjoint conditions (LR: 88.66%, SVM: 88.61%, RF: 85.00%). Gaussian Naive Bayes achieves peak accuracy on dual-domain `Emotion ⊕ Face` (84.31%).
6. **Complementary Age Features:** Refer to Age features as providing "complementary informational contribution" or "additional discriminative information", especially beneficial for linear classifiers ($p = 0.0073$ on LR), while non-linear SVM exhibits asymptotic feature saturation ($p = 0.7343$).
7. **LR vs. SVM Trade-off:** Emphasize that LR Tri-Domain and SVM Tri-Domain are statistically equivalent in predictive accuracy ($p = 1.0000$), but LR offers profound computational benefits (>800x faster inference, >330x smaller model size).
8. **Empirical vs Theoretical Separation:** Strictly separate empirical findings (actual experimental figures) from conceptual interpretations.
9. **No State-of-the-Art Hyperbole:** Use "highest performance among compared configurations on DemogPairs" - never unsupported "state-of-the-art".
10. **Demographic Generalization Scope:** Explicitly limit scope to the 3 macro-racial groups represented in DemogPairs (Asian, Black, White).
11. **AI Ethics Statement:** Formulated for academic benchmarking and algorithmic fairness research; public surveillance deployment requires human-in-the-loop oversight and ethical governance.
12. **Equation (4) CLS Token Definition:** $\mathbf{z}_L^0$ in $\mathbf{f}_{\text{domain}} = \text{LayerNorm}(\mathbf{z}_L^0)$ refers specifically to the CLS token representation from the **final encoder layer L** of the ViT backbone.
13. **ViT Embedding as Task-Associated Representations:** Use "task-associated representations" as the preferred framing.
14. **Exact Disparity Figures:**
    - Subject-Disjoint LR: Equal Opportunity Difference $\Delta\text{TPR} = \mathbf{9.72\text{ pp}}$ (White_Males 94.44% vs. Black_Females 84.72%).
    - Subject-Disjoint SVM: Equal Opportunity Difference $\Delta\text{TPR} = \mathbf{9.72\text{ pp}}$ (White_Males 94.44% vs. Black_Females 84.72%).
    - Subject-Overlap SVM: $\Delta\text{F1} = \mathbf{0.0440}$, $\Delta\text{Recall} = \mathbf{0.0750}$, $\Delta\text{Precision} = \mathbf{0.0310}$.
15. **Subgroup Performance Scope:** Subgroup evaluation reflects per-class performance across intersectional demographics and does not constitute an exhaustive algorithmic fairness audit.
16. **OvR Accuracy Context:** Note the 5:1 negative class ratio in 6-class OvR evaluation; do not present OvR Accuracy as a primary fairness indicator.
17. **Full Numerical Consistency Check:** All tables, confusion matrices, per-subgroup metrics, and narrative text must be numerically consistent with `experiment/code/results/*.json` and `experiment/code/archive/audit_ledger.json`.
18. **Novelty Statement:** Novelty lies in combining: (a) tri-domain ViT feature fusion, (b) comparative 4-classifier evaluation under unified GridSearchCV, (c) empirical data leakage ablation (subject-disjoint vs subject-overlap), and (d) inferential statistical validation.
19. **RQ Alignment:** Every research conclusion must be backed by an evidential anchor.
20. **Final Terminology/Notation/Number Consistency:** Verify consistent notation ($\oplus$ symbol, equations, metric values) throughout.
21. **Hupont & Fernández (IEEE FG 2019):** Seminal DemogPairs paper; cited when introducing the dataset, not as a direct performance competitor.
22. **Universal Manuscript Pipeline SOP (`WORKFLOW.md`):** All drafting, translation, and publication workflows must follow `WORKFLOW.md`.
23. **Sentence-Level Citation Audit Protocol (`paper/references.txt`):** Factual claims must trace to registered citations.
24. **Interactive In-Text Citation Standards (`paper/*.md`):** Markdown in-text citations use `[[N]](06_references.md#refN)`.
25. **Preservation of Archive Directory:** Never delete or alter `experiment/code/archive/` or `audit_ledger.json`.
26. **Scripts Directory Maintenance:** Keep execution runner scripts cleanly inside `experiment/code/scripts/`.
27. **Notebook Location Standard:** All 33 active Jupyter notebooks remain directly at `experiment/code/` root.
28. **Response to Reviewers Alignment:** When drafting rebuttal text for Reviewer 2 Comment #2, leverage the data leakage comparison table and McNemar p-values directly from Section 7 of this manual.

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
