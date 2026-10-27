# Multi-Domain Vision Transformer Fusion for Intersectional Demographic Classification from Facial Images

> **Abstract:** An empirical machine learning framework for intersectional 6-class (3 Race × 2 Gender) demographic classification from facial images using offline multi-representation feature fusion across three task-specialized Vision Transformer (ViT) backbones (**Face Biometrics**, **Facial Emotion**, and **Facial Age**) combined with exhaustive 5-Fold Stratified GridSearchCV-optimized classical classifiers. Under strict **Subject-Disjoint Partitioning** (Zero Identity Leakage — IEEE Access Revision Milestone), the proposed Tri-Domain ViT representation achieves **88.66% Test Accuracy** (Logistic Regression, Macro F1: **0.8868**) and **88.61% Test Accuracy** (Support Vector Machine, Macro F1: **0.8863**) on held-out unseen subjects ($N = 2,160$ test samples from 120 isolated identities). Concurrently, this repository preserves the historical **Subject-Overlap Benchmark** (**93.70%** SVM Tri-Domain) to provide a rigorous empirical baseline for data leakage ablation and out-of-subject generalization analysis (answering IEEE Access Reviewer 2 Comment #2).

---

## 📌 Publication & Review Status

- **Target Journal:** [IEEE Access](https://ieeeaccess.ieee.org/) (Open Access, Q1 / Impact Factor: 3.4)
- **Manuscript ID:** `Access-2026-50857`
- **Current Milestone:** Editorial Decision Received (20-10-2026) – Binary Peer Review (Reject & Resubmit with 1 Resubmission Opportunity).
- **Revision Core Objective:** Resolving Reviewer 2 Comment #2 regarding identity overlap and cross-subject generalization through strict subject-disjoint re-benchmarking, paired inferential hypothesis testing (McNemar tests & 95% Wilson Score CIs), and computational profiling.
- **Peer Review Dossier:** Managed under [`paper_reviews_ieee/`](paper_reviews_ieee/) (Decision letter, Reviewer 1 & 2 feedback, response template, and 10-point resubmission checklist).

---

## 🌟 Dual Benchmark System

To ensure complete scientific transparency and directly answer IEEE Access Reviewer 2 Comment #2, this repository establishes a **Dual Benchmark Architecture**:
1. **Primary Benchmark (Subject-Disjoint):** Zero identity leakage ($0.00\%$); evaluates true generalizability on completely unseen identities.
2. **Historical Benchmark (Subject-Overlap):** Image-level stratified split ($100.00\%$ identity presence); serves as the comparative baseline for quantifying facial identity memorization.

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

---

### 1. Primary Benchmark: Subject-Disjoint Partitioning (Zero Data Leakage — IEEE Access Revision)

Evaluated on the held-out subject-disjoint test partition ($N = 2,160$ images from 120 unseen subjects; exactly 360 images per intersectional class) following 5-fold stratified cross-validation on 480 training subjects ($N = 8,640$).

#### Top-Performing Configuration per Classifier Family

| Rank | Classifier | Best Feature Scheme | Feature Dim | Test Accuracy | Precision (Macro) | Recall (Macro) | F1-Score (Macro) | 95% Wilson Score CI | Latency (ms/sample) | Model Size (MB) | Best Hyperparameters |
|:---:|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 🥇 | **Logistic Regression (LR)** | **Tri-Domain (`Face ⊕ Emotion ⊕ Age`)** | **2,304** | **88.66%** | **0.8875** | **0.8866** | **0.8868** | **[87.25%, 89.93%]** | **0.0054 ms** | **0.11 MB** | `C=0.1, solver='saga', max_iter=500, scaler=MinMaxScaler, pca=None` |
| 🥈 | **Support Vector Machine (SVM)** | **Tri-Domain (`Face ⊕ Emotion ⊕ Age`)** | **2,304** | **88.61%** | **0.8871** | **0.8861** | **0.8863** | **[87.20%, 89.88%]** | 4.4481 ms | 36.60 MB | `C=10, kernel='rbf', gamma='scale', scaler=MinMaxScaler, pca=None` |
| 🥉 | **Random Forest (RF)** | **Tri-Domain (`Face ⊕ Emotion ⊕ Age`)** | **2,304** | **85.00%** | 0.8506 | 0.8500 | 0.8493 | [83.43%, 86.44%] | 0.0537 ms | 6.19 MB | `n_estimators=200, max_depth=None, max_features='sqrt', min_samples_split=2, min_samples_leaf=1, pca=PCA(0.75), scaler=None` |
| 4 | **Gaussian Naive Bayes (GNB)** | Dual-Domain (`Emotion ⊕ Face`) | 1,536 | **84.31%** | 0.8437 | 0.8431 | 0.8430 | [82.71%, 85.78%] | 0.0083 ms | 0.78 MB | `var_smoothing=0.005878, pca=PCA(0.75), scaler=MinMaxScaler` |

*Note: For Gaussian Naive Bayes, Tri-Domain achieves **83.61%** (Macro F1: 0.8364), while peak accuracy occurs on Dual-Domain `Emotion ⊕ Face` (84.31%).*

#### Definitive 28-Model Subject-Disjoint Global Leaderboard

| Rank | Classifier | Feature Scheme | Category | Dim | Test Accuracy | Precision | Recall | F1-Score | 95% CI (Wilson) | Latency (ms) | Size (MB) |
|:---:|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | **LR** | **`vit-face-emotion-age`** | **Tri** | **2,304** | **88.66%** | **0.8875** | **0.8866** | **0.8868** | **[87.25%, 89.93%]** | 0.0054 | 0.11 |
| 2 | **SVM** | **`vit-face-emotion-age`** | **Tri** | **2,304** | **88.61%** | **0.8871** | **0.8861** | **0.8863** | **[87.20%, 89.88%]** | 4.4481 | 36.60 |
| 3 | SVM | `vit-emotion-face` | Dual | 1,536 | 88.43% | 0.8850 | 0.8843 | 0.8844 | [87.01%, 89.71%] | 0.9707 | 15.27 |
| 4 | SVM | `vit-face-age` | Dual | 1,536 | 87.55% | 0.8766 | 0.8755 | 0.8757 | [86.09%, 88.87%] | 2.2581 | 23.48 |
| 5 | LR | `vit-emotion-face` | Dual | 1,536 | 87.45% | 0.8759 | 0.8745 | 0.8749 | [85.99%, 88.78%] | 0.0039 | 0.08 |
| 6 | LR | `vit-face-age` | Dual | 1,536 | 87.41% | 0.8744 | 0.8741 | 0.8740 | [85.94%, 88.74%] | 0.0090 | 0.11 |
| 7 | LR | `vit-emotion-age` | Dual | 1,536 | 86.67% | 0.8668 | 0.8667 | 0.8667 | [85.17%, 88.04%] | 0.0040 | 0.08 |
| 8 | LR | `vit-face` | Single | 768 | 86.39% | 0.8646 | 0.8639 | 0.8640 | [84.88%, 87.77%] | 0.0008 | 0.04 |
| 9 | SVM | `vit-emotion-age` | Dual | 1,536 | 86.25% | 0.8626 | 0.8625 | 0.8624 | [84.73%, 87.64%] | 3.1451 | 32.76 |
| 10 | SVM | `vit-face` | Single | 768 | 86.16% | 0.8624 | 0.8616 | 0.8619 | [84.64%, 87.55%] | 3.0653 | 7.56 |
| 11 | SVM | `vit-emotion` | Single | 768 | 85.79% | 0.8584 | 0.8579 | 0.8580 | [84.25%, 87.20%] | 1.8871 | 15.30 |
| 12 | LR | `vit-emotion` | Single | 768 | 85.23% | 0.8535 | 0.8523 | 0.8527 | [83.67%, 86.67%] | 0.0037 | 0.06 |
| 13 | RF | `vit-face-emotion-age` | Tri | 2,304 | 85.00% | 0.8506 | 0.8500 | 0.8493 | [83.43%, 86.44%] | 0.0537 | 6.19 |
| 14 | RF | `vit-emotion-face` | Dual | 1,536 | 84.86% | 0.8493 | 0.8486 | 0.8479 | [83.29%, 86.31%] | 0.0316 | 8.58 |
| 15 | RF | `vit-face-age` | Dual | 1,536 | 84.86% | 0.8488 | 0.8486 | 0.8478 | [83.29%, 86.31%] | 0.0310 | 6.19 |
| 16 | GNB | `vit-emotion-face` | Dual | 1,536 | 84.31% | 0.8437 | 0.8431 | 0.8430 | [82.71%, 85.78%] | 0.0083 | 0.78 |
| 17 | RF | `vit-face` | Single | 768 | 84.03% | 0.8413 | 0.8403 | 0.8403 | [82.42%, 85.51%] | 0.0314 | 5.99 |
| 18 | GNB | `vit-face-emotion-age` | Tri | 2,304 | 83.61% | 0.8379 | 0.8361 | 0.8364 | [81.99%, 85.11%] | 0.0081 | 1.36 |
| 19 | GNB | `vit-face-age` | Dual | 1,536 | 83.06% | 0.8347 | 0.8306 | 0.8310 | [81.42%, 84.58%] | 0.0080 | 0.75 |
| 20 | SVM | `vit-age` | Single | 768 | 82.55% | 0.8268 | 0.8255 | 0.8258 | [80.89%, 84.09%] | 2.0104 | 18.22 |
| 21 | GNB | `vit-face` | Single | 768 | 82.55% | 0.8268 | 0.8255 | 0.8250 | [80.89%, 84.09%] | 0.0031 | 0.19 |
| 22 | LR | `vit-age` | Single | 768 | 81.48% | 0.8145 | 0.8148 | 0.8146 | [79.79%, 83.06%] | 0.0028 | 0.06 |
| 23 | RF | `vit-emotion-age` | Dual | 1,536 | 77.31% | 0.7734 | 0.7731 | 0.7728 | [75.50%, 79.03%] | 0.0392 | 12.35 |
| 24 | RF | `vit-emotion` | Single | 768 | 76.11% | 0.7602 | 0.7611 | 0.7603 | [74.27%, 77.86%] | 0.0316 | 10.34 |
| 25 | GNB | `vit-emotion-age` | Dual | 1,536 | 75.88% | 0.7597 | 0.7588 | 0.7578 | [74.03%, 77.64%] | 0.0048 | 0.24 |
| 26 | GNB | `vit-emotion` | Single | 768 | 72.13% | 0.7251 | 0.7213 | 0.7199 | [70.20%, 73.98%] | 0.0031 | 0.13 |
| 27 | RF | `vit-age` | Single | 768 | 71.81% | 0.7176 | 0.7181 | 0.7170 | [69.87%, 73.66%] | 0.0327 | 11.21 |
| 28 | GNB | `vit-age` | Single | 768 | 67.08% | 0.6691 | 0.6708 | 0.6686 | [65.07%, 69.03%] | 0.0045 | 0.37 |

---

### 2. Historical Benchmark: Subject-Overlap Partitioning (100% Identity Leakage Baseline)

Preserved under [`experiment/code/archive/`](experiment/code/archive/) as an ablation baseline to quantify the inflation effect of identity leakage. Evaluated under standard image-level stratified splitting ($N = 8,640$ train / $N = 2,160$ test; all 593 test identities appeared in the training set under different photos):

| Rank | Classifier | Best Feature Configuration | Feature Dim | Best Accuracy | Precision | Recall | F1-Score | Best Hyperparameters |
|:---:|---|---|:---:|:---:|:---:|:---:|:---:|---|
| 🥇 | **Support Vector Machine (SVM)** | **Tri-Domain (`Face ⊕ Emotion ⊕ Age`)** | **2,304** | **93.70%** | **0.9372** | **0.9370** | **0.9369** | `C=10, kernel='poly', degree=2, gamma='scale', pca=None, scaler=None` |
| 🥈 | **Logistic Regression (LR)** | Tri-Domain (`Face ⊕ Emotion ⊕ Age`) | 2,304 | **92.73%** | 0.9275 | 0.9273 | 0.9273 | `C=0.1, solver='newton-cg', max_iter=500, pca=None, scaler=None` |
| 🥉 | **Random Forest (RF)** | Dual-Domain (`Emotion ⊕ Face`) | 1,536 | **86.85%** | 0.8689 | 0.8685 | 0.8682 | `n_estimators=200, max_depth=None, max_features='sqrt', min_samples_split=5, min_samples_leaf=1, pca=PCA(0.75), scaler=None` |
| 4 | **Gaussian Naive Bayes (GNB)** | Tri-Domain (`Face ⊕ Emotion ⊕ Age`) | 2,304 | **85.05%** | 0.8512 | 0.8505 | 0.8505 | `var_smoothing=5.8780e-03, pca=PCA(0.75), scaler=None` |

---

### 3. Comparative Data Leakage Ablation & Generalization Analysis

Comparing the two partitioning schemes reveals critical empirical insights regarding identity memorization versus generalizable multi-domain feature representations:

#### (a) Performance Delta across Configurations (Subject-Overlap vs. Subject-Disjoint)

| Classifier | Feature Configuration | Subject-Overlap Acc (Old) | Subject-Disjoint Acc (New) | Nominal Drop ($\Delta\text{Acc}$) | 95% Wilson CI (New) | Generalization Verdict |
|---|---|:---:|:---:|:---:|:---:|---|
| **SVM** | **Tri-Domain (`Face ⊕ Emotion ⊕ Age`)** | **93.70%** | **88.61%** | **-5.09 pp** | [87.20%, 89.88%] | High out-of-subject generalization |
| **SVM** | Dual-Domain (`Emotion ⊕ Face`) | 93.29% | 88.43% | -4.86 pp | [87.01%, 89.71%] | Robust cross-subject boundaries |
| **SVM** | Single-Domain (`vit-face`) | 90.83% | 86.16% | -4.68 pp | [84.64%, 87.55%] | Susceptible to facial identity cues |
| **LR** | **Tri-Domain (`Face ⊕ Emotion ⊕ Age`)** | **92.73%** | **88.66%** | **-4.07 pp** | [87.25%, 89.93%] | Peak generalizability & lowest drop |
| **LR** | Dual-Domain (`Emotion ⊕ Face`) | 92.41% | 87.45% | -4.95 pp | [85.99%, 88.78%] | Linear model benefits from Age |
| **LR** | Single-Domain (`vit-face`) | 90.60% | 86.39% | -4.21 pp | [84.88%, 87.77%] | Face-alone baseline |
| **RF** | Tri-Domain (`Face ⊕ Emotion ⊕ Age`) | 86.20% | 85.00% | -1.20 pp | [83.43%, 86.44%] | Moderate cross-subject stability |
| **GNB** | Tri-Domain (`Face ⊕ Emotion ⊕ Age`) | 85.05% | 83.61% | -1.44 pp | [81.99%, 85.11%] | Naive Bayes baseline |

#### (b) Key Empirical Takeaways & Statistical Proofs

1. **Elimination of Facial Identity Memorization:**
   The nominal accuracy drop of ~4.0% to 5.1% across top classifiers proves that models evaluated under subject-overlap protocols inadvertently memorize facial identity signatures. The subject-disjoint results reflect genuine demographic attribute generalization on previously unseen individuals.
2. **Statistically Significant Multi-Domain Superiority ($p < 0.001$):**
   A common concern raised by Reviewer 2 was whether multi-domain fusion gains could be an artifact of data leakage. Inferential hypothesis testing (**Paired McNemar Test with Edwards continuity correction**) on the subject-disjoint test set definitively refutes this:
   - **SVM:** Tri-Domain (88.61%) significantly outperforms Single Face Biometrics (86.16%) with $\Delta = +2.45\%$ (+53 net correct images, $\chi^2 = 20.9612$, **$p = 3.46 \times 10^{-6} < 0.001$**).
   - **Logistic Regression:** Tri-Domain (88.66%) significantly outperforms Single Face Biometrics (86.39%) with $\Delta = +2.27\%$ (+49 net correct images, $\chi^2 = 19.6923$, **$p = 6.78 \times 10^{-6} < 0.001$**).
   - Multi-domain fusion gains are statistically robust and independent of identity leakage.
3. **Asymptotic Feature Saturation vs. Linear Complementarity:**
   - In **Logistic Regression**, Tri-Domain (88.66%) significantly improves over Dual-Domain `Emotion ⊕ Face` (87.45%) with net gain +26 images (**$p = 0.0073 < 0.01$**), demonstrating that biological age morphology provides orthogonal discriminative signal for linear hyperplanes.
   - In **SVM**, Tri-Domain (88.61%) and Dual-Domain `Emotion ⊕ Face` (88.43%) exhibit net gain +4 images ($p = 0.7343 > 0.05$), confirming asymptotic representation saturation under non-linear RBF kernels.
4. **Predictive Equivalence & Extreme Computational Efficiency (LR vs. SVM):**
   - Paired McNemar testing between LR Tri-Domain (88.66%) and SVM Tri-Domain (88.61%) shows exact equivalence ($p = 1.0000$, net gain +1 image).
   - However, **LR delivers >800x faster inference** (**0.0054 ms** vs. 4.4481 ms per image) and **>330x smaller model footprint** (**0.11 MB** vs. 36.60 MB), establishing Logistic Regression as the optimal engine for resource-constrained edge AI.

---

### 4. Intersectional Subgroup Disparity Profile (Subject-Disjoint Test Set)

Evaluated on the 6 intersectional demographic subgroups ($N = 360$ unseen test images per subgroup):

#### (a) Logistic Regression Tri-Domain (Top Benchmark Model: 88.66%)

| Demographic Subgroup | Macro Race | Gender | Recall / TPR | Precision | F1-Score | Support |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **White_Males** | White | Male | **94.44%** | **95.24%** | **94.84%** | 360 |
| **White_Females** | White | Female | 90.56% | 91.32% | 90.93% | 360 |
| **Black_Males** | Black | Male | 87.78% | 91.59% | 89.65% | 360 |
| **Asian_Males** | Asian | Male | 87.78% | 82.72% | 85.18% | 360 |
| **Asian_Females** | Asian | Female | 86.67% | 86.43% | 86.55% | 360 |
| **Black_Females** | Black | Female | 84.72% | 85.20% | 84.96% | 360 |
| **Macro Average** | **All** | **All** | **88.66%** | **0.8875** | **0.8868** | **2,160** |

*Equal Opportunity Difference (Max - Min Recall): **9.72 percentage points** (White_Males 94.44% vs. Black_Females 84.72%).*

#### (b) Support Vector Machine Tri-Domain (88.61%)

| Demographic Subgroup | Macro Race | Gender | Recall / TPR | Precision | F1-Score | Support |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **White_Males** | White | Male | **94.44%** | 93.92% | **94.18%** | 360 |
| **White_Females** | White | Female | 91.11% | 90.11% | 90.61% | 360 |
| **Black_Males** | Black | Male | 87.22% | 92.35% | 89.71% | 360 |
| **Asian_Males** | Asian | Male | 88.06% | 82.34% | 85.10% | 360 |
| **Asian_Females** | Asian | Female | 86.11% | 85.87% | 85.99% | 360 |
| **Black_Females** | Black | Female | 84.72% | 87.64% | 86.16% | 360 |
| **Macro Average** | **All** | **All** | **88.61%** | **0.8871** | **0.8863** | **2,160** |

*Equal Opportunity Difference (Max - Min Recall): **9.72 percentage points**.*

---

### 5. Comparison with Prior Studies on DemogPairs

| Study | Partitioning Protocol | Architecture | Accuracy | Precision | Recall | F1-Score |
|---|---|---|:---:|:---:|:---:|:---:|
| Putri et al. (*JIEET 2025*) | Random Stratified (Subject-Overlap) | MD-ViT (Face + Age) + XGBoost | 89.07% | 0.8912 | 0.8907 | 0.8901 |
| Putri et al. (*ICVEE 2025*) | Random Stratified (Subject-Overlap) | Dual-ViT (Face + Emotion) + SVM | 92.41% | 0.9248 | 0.9241 | 0.9238 |
| **Proposed (Historical Baseline)** | **Random Stratified (Subject-Overlap)** | **Tri-Domain ViT + SVM** | **93.70%** | **0.9372** | **0.9370** | **0.9369** |
| **Proposed (Revision Milestone)** | **Subject-Disjoint (Zero Leakage)** | **Tri-Domain ViT + LR** | **88.66%** | **0.8875** | **0.8866** | **0.8868** |
| **Proposed (Revision Milestone)** | **Subject-Disjoint (Zero Leakage)** | **Tri-Domain ViT + SVM** | **88.61%** | **0.8871** | **0.8861** | **0.8863** |

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
                 [ 5-Fold Stratified Subject-Disjoint GridSearchCV ]
                   (Logistic Regression / SVM / Random Forest / GNB)
                                           │
                                           ▼
                 [ Intersectional 6-Class Classification on DemogPairs ]
           (Asian_Females, Asian_Males, Black_Females, Black_Males, White_Females, White_Males)
```

### 1. Multi-Domain Vision Transformer Extractors (768-d per domain)
- **ViT-Face** (`skutaada/VIT-VGGFace`): Pretrained on facial biometrics; captures static craniofacial geometry and facial identity proportions.
- **ViT-Emotion** (`dima806/facial_emotions_image_detection`): Pretrained on facial affect; captures dynamic expression cues and localized action units.
- **ViT-Age** (`dima806/facial_age_image_detection`): Pretrained on facial age estimation; captures biological aging morphology and epidermal texture patterns.

### 2. Feature Fusion & Optimization Pipeline
- **Offline Representation Extraction:** High-level representations are extracted from the normalized `[CLS]` token ($\mathbf{z}_L^0 \in \mathbb{R}^{768}$) of the final encoder layer of each frozen ViT-Base backbone.
- **7 Systematic Ablation Schemes:**
  - *Single-Domain (768-d):* `Face`, `Emotion`, `Age`
  - *Dual-Domain (1,536-d):* `Emotion ⊕ Face`, `Face ⊕ Age`, `Emotion ⊕ Age`
  - *Tri-Domain (2,304-d):* `Face ⊕ Emotion ⊕ Age`
- **Leakage-Free Cross-Validation:** Preprocessing transformations (MinMaxScaler and PCA) are fitted strictly on training folds within `scikit-learn.pipeline.Pipeline` objects to prevent data leakage.
- **Grid Search Space:** Evaluated a total of 1,086 parameter combinations ($38,010$ total cross-validation fits across 7 feature configurations and 4 classifier families).

---

## 📁 Repository Structure

```
.
├── .agents/skills/                        # Autonomous AI agent skills & peer review frameworks
│   ├── ar-paper-reviewer/                 # Independent academic peer review simulation skill
│   ├── ar-paper-revision/                 # Byte-level precision patching and revision application skill
│   └── ar-paper-revision-coach/           # Review deconstruction, roadmap & rebuttal ledger coach
├── authors.txt                            # Complete author profiles, affiliations, and ORCID IDs
├── experiment/                            # Experimental logs, documentation, and source code
│   ├── 00_overview.md - 05_results.md     # Comprehensive experimental logs and methodology audits
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
│       │   ├── md_old/                    # Markdown logs & confusion matrices of legacy experiments
│       │   ├── models_old/                # Serialized trained weights (.pkl) of 28 legacy models
│       │   ├── notebook_old/              # 33 Jupyter notebooks of legacy experiments
│       │   ├── results_old/               # 28 raw JSON result files of legacy subject-overlap models
│       │   └── README.md                  # Detailed documentation on archive purpose and audit protocol
│       ├── scripts/                       # Autonomous execution runners & automated queue scripts
│       │   ├── auto_run_experiments.py    # Main automated batch runner for all 28 experiment pipelines
│       │   ├── run_gnb_queue.py           # Dedicated queue runner for Gaussian Naive Bayes series
│       │   ├── run_remaining_queue.py     # Resilient queue runner for remaining model workloads
│       │   ├── run_experiments.bat        # Windows batch launcher for auto_run_experiments.py
│       │   ├── run_gnb.bat                # Windows batch launcher for GNB queue
│       │   └── README.md                  # Documentation on runner operations and execution commands
│       ├── utils/                         # Modular utility library (constants, dataset, evaluation, etc.)
│       ├── dataset/demogpairs/metadata/   # 6 metadata .txt files (1,800 rows each)
│       ├── features/                      # Serialized 768-d feature embeddings (.pkl)
│       ├── md/                            # Markdown exports of all notebooks & statistical reports
│       ├── models/                        # Serialized trained weights (.pkl) of 28 active models
│       ├── results/                       # 28 raw JSON result files of active Subject-Disjoint models
│       └── images/                        # Confusion matrices and Wilson Score 95% CI plots
├── images/                                # High-resolution architecture diagrams and sample figures
├── paper/                                 # Modular manuscript draft in Markdown (IEEE style)
│   ├── 00_abstract.md - 05_conclusion.md  # Core manuscript sections
│   ├── 06_references.md                   # Standardized IEEE bibliography registry (entries [1]-[51])
│   ├── 07_biographies.md                  # Section VII: Biographies & portrait assets
│   ├── acronyms.txt                       # Centralized acronym registry
│   ├── ref_part_*.md                      # 10 modular bibliographic audit logs (entries [1]-[51])
│   ├── references.txt                     # Sentence-level citation tracking & verification registry
│   └── references/                        # 51 bibliographic source files (.bib, .ris, .nbib, .bibtex)
├── paper_latex_en/                        # Submission-ready English IEEE Access LaTeX package
│   ├── access.tex                         # Master LaTeX entrypoint with \input{} sections
│   ├── access.pdf                         # Compiled dual-column English manuscript PDF
│   ├── ieeeaccess.cls / IEEEtran.bst      # Official IEEE Access style class and bibliography style
│   ├── references.bib                     # Consolidated BibTeX database
│   └── sections/                          # 21 modular LaTeX sections (00_title.tex s.d. 07_biographies.tex)
├── paper_latex_id/                        # Reference Indonesian IEEE Access LaTeX package
│   ├── access.tex / access.pdf            # Indonesian LaTeX source & compiled PDF
│   └── sections/                          # Indonesian translation sections
├── paper_outline.md                       # Complete publication outline & paragraph targets
├── paper_reviews/                         # Internal multi-agent mock peer review audit system (Round 1 & 2)
├── paper_reviews_ieee/                    # Official IEEE Access editorial decision & review dossier
│   ├── IEEE-Access_Decision-on-Manuscript-ID-Access-2026-50857.md # Official decision & reviewer comments
│   ├── IEEE-Access_Response-to-Reviewers-template.md              # Point-by-point response template
│   ├── Request-for-Byline-Change.md                               # Formal author byline change form
│   └── Resubmission-Checklist.md                                  # Resubmission 10-point compliance checklist
├── paper_submission/                      # Formal submission packaging and IEEE compliance reports
├── prompts.txt                            # Chronological log of experimental prompts and instructions
├── README.AI.md                           # Master AI agent operational guide and ground-truth index
├── README.md                              # Public research documentation (THIS FILE)
├── WORKFLOW.md                            # Standard Operating Procedure (SOP) for manuscript pipeline
└── upload/                                # Packaged submission artifacts (PDF and source ZIP)
```

---

## 🚀 Quick Start

### 1. Environment Setup
```bash
conda create -n torch-gpu python=3.11 -y
conda activate torch-gpu
pip install torch torchvision transformers scikit-learn imbalanced-learn joblib pandas numpy pillow matplotlib seaborn tqdm gradio nbconvert
```

### 2. Experimental Reproduction Workflow

#### Option A: Automated Batch Execution via Scripts (`experiment/code/scripts/`)
```bash
# Execute automated batch execution across all models
cd experiment/code
python scripts/auto_run_experiments.py
```

#### Option B: Step-by-Step Interactive Execution
1. **Extract ViT Embeddings:** Run `1.1_vit-face_demogpairs.ipynb`, `1.1_vit-emotion_demogpairs.ipynb`, and `1.1_vit-age_demogpairs.ipynb` to generate embeddings in `features/`.
2. **Train Classifiers (Subject-Disjoint):** Run notebooks:
   - Logistic Regression: `2.5.1` to `2.5.7`
   - Support Vector Machine: `2.1.1` to `2.1.7`
   - Random Forest: `2.4.1` to `2.4.7`
   - Gaussian Naive Bayes: `2.2.1` to `2.2.7`
3. **Compare Results:** Run `3.0_compare.ipynb` to aggregate all 28 JSON result files into a consolidated benchmark leaderboard.
4. **Statistical Significance Testing:** Run `3.1_statistical_significance.ipynb` for paired McNemar tests, Wilson Score 95% CIs, and EOD algorithmic fairness audits.
5. **Interactive Web Demo:** Launch `python app.py` for real-time web inference.

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
