# Author Response to Reviewers: Access-2026-50857

**Manuscript ID:** `Access-2026-50857`  
**Title:** *Multi-Domain Vision Transformer Fusion for Intersectional Demographic Classification from Facial Images*  
**Journal:** IEEE Access  
**Associate Editor:** Dr. Vincenzo Conti  
**Authors:** Dr. Ir. Ricky Eka Putra (Corresponding Author), Rezky Arisanti Putri, Dr. Yuni Yamasari, Rafy Aulia Akbar, and Dr. Shukor Sanim Mohd Fauzi  
**Date:** November 2026  

---

## Part I: Response to Associate Editor & General Overview

Dear Dr. Vincenzo Conti,  
Associate Editor, IEEE Access,

We sincerely thank you and the two independent reviewers for the constructive, insightful, and rigorous evaluation of our manuscript. We have carefully addressed every comment and technical concern raised by the reviewers. In accordance with IEEE Access policies, we have implemented thorough methodological enhancements, conducted exhaustive re-evaluations under strict identity-isolated partitions, and restructured the manuscript accordingly.

### Summary of Major Methodological & Empirical Revisions:

1. **Resolution of Data Leakage & Subject-Disjoint Primary Benchmark (Reviewer 2 #2 & Reviewer 1 #5):**  
   To address the critical concern regarding identity overlap, we established a strict **Subject-Disjoint Partitioning Protocol** across the 600 unique subjects of DemogPairs. Using deterministic per-subgroup identity splitting (`train_test_split` on sorted unique `subject_id` lists per class, `train_size=0.8`, `random_state=42`), 480 subjects (8,640 images; 80 subjects/class) are dedicated exclusively to training and 5-Fold `StratifiedGroupKFold` (`groups=subject_id`) cross-validation, while 120 completely unseen subjects (2,160 images; 20 subjects/class) form the held-out test set, ensuring **0.00% identity leakage**. Under this zero-leakage primary benchmark:
   - **Logistic Regression (LR) + Tri-Domain ViT** achieved the top performance of **88.66% Accuracy** (Macro F1: **0.8868**, 95% Wilson CI: **[87.25%, 89.93%]**, downstream latency: **0.0046 ms/sample**, model size: **0.11 MB**).
   - **Support Vector Machine (SVM) + Tri-Domain ViT** achieved **88.61% Accuracy** (Macro F1: **0.8863**, 95% Wilson CI: **[87.20%, 89.88%]**).
   - The historical image-level partition (93.70% SVM Tri-Domain, 92.73% LR Tri-Domain) is preserved as an explicit **Data Leakage Ablation Study** in Section IV-B (Table XII) to empirically quantify facial identity memorization ($\Delta = -5.09\text{ pp}$ on SVM and $-4.07\text{ pp}$ on LR).

2. **Inferential Hypothesis Testing & McNemar Significance Qualification (Reviewer 2 #5):**  
   We performed formal paired McNemar tests with Edwards continuity correction and exact two-sided binomial tests across the evaluated models ($N = 2,160$, Table XIII). Multi-domain ViT fusion demonstrated statistically significant gains over single-domain face biometrics ($p = 3.46 \times 10^{-6} < 0.001$ on SVM; $p = 6.78 \times 10^{-6} < 0.001$ on LR). Comparing LR Tri (88.66%, 1,915/2,160) and SVM Tri (88.61%, 1,914/2,160) yielded $\chi^2 = 0.0000$ and $p = 1.0000$ (discordant pairs $b=36, c=35$, net +1 image), showing **no statistically significant difference in predictive performance (predictive parity)**. Furthermore, claims regarding the age domain were rigorously calibrated: adding `Age` on top of `Emotion ⊕ Face` yields a statistically significant improvement on linear LR ($87.45\% \to 88.66\%, +1.20\text{ pp}, +26\text{ images}, p = 0.0073 < 0.01$), whereas on non-linear RBF SVM it indicates **asymptotic feature saturation** ($88.43\% \to 88.61\%, +0.19\text{ pp}, +4\text{ images}, p = 0.7343 > 0.05$; though compared to `Face ⊕ Age` at $87.55\%$, the gain to SVM Tri-Domain remains statistically significant at $+1.06\text{ pp}, p = 0.0086 < 0.01$). We also explicitly note classifier-dependent behavior on RF (85.00% Tri vs. 84.86% Dual, $p = 0.8408$) and GNB (peaking on Dual `Emotion ⊕ Face` at 84.31% vs. 83.61% Tri, $p = 0.2349$).

3. **Complete Computational Efficiency Profiling (Reviewer 1 #5 & Reviewer 2 #8):**  
   We incorporated a dedicated quantitative efficiency profile (Section IV-A Paragraph 6, Table XI) reporting: (1) offline ViT feature extraction runtime on an **NVIDIA GeForce RTX 4060 GPU** with in-memory processor caching (**124.5 ms/image** for tri-domain: `39.7 ms` Face + `39.7 ms` Emotion + `45.1 ms` Age; total **22.41 minutes** for 10,800 images) compared against the **CPU baseline** (**~1,487 ms/image**; total **4.46 hours**, an **11.9× GPU speedup**), (2) 5-Fold GridSearchCV training duration across **31,920 CV fits** (LR Tri: **54.8 min** vs. SVM Tri: **511.1 min**; **9.3× faster training**), (3) per-sample downstream classifier inference latency (**0.0046 ms** on LR vs. **4.6785 ms** on SVM; **>1,000× faster** downstream head, with total end-to-end GPU latency of $\approx 124.505\text{ ms/image}$ for LR vs. $\approx 129.179\text{ ms/image}$ for SVM), and (4) memory/storage footprint (**0.11 MB** on LR vs. **36.60 MB** on SVM, **>330× more compact**; test array RAM footprint **18.98 MB**; disk feature cache **30.8 MB/domain** or **92.4 MB** tri-domain). We explicitly qualify that this ultra-lightweight footprint applies to the downstream classification head, while end-to-end low-power Edge AI deployment is framed around future backbone quantization or knowledge distillation.

4. **Architectural & Theoretical Clarifications (Reviewer 1 #2, #3, Reviewer 2 #1, #3, #4):**  
   We redesigned Figure 3 (`images/vit_v2.2.png`) into a high-resolution diagram illustrating patch tokenization, independent parallel processing across the three frozen ViT-Base backbones, Layer-12 `[CLS]` token extraction ($3 \times 768$-d), and direct-sum concatenation ($\oplus$). We formalized mathematical equations (Equations (1)–(23)) across Sections II and III, documented exact HuggingFace checkpoint identifiers with Git commit SHAs and uniform normalization parameters ($\mu = \sigma = [0.5, 0.5, 0.5]$ to $[-1, 1]$ without external MTCNN alignment) in Section III-A & III-B, and reconciled the exact hyperparameter search space (**912 combinations per scheme**, **4,560 fits/scheme**, **31,920 total CV fits**, and **28 final refits** across Tables III–VI).

5. **Calibration of Claims & Scope (Reviewer 1 #1, #7, Reviewer 2 #6, #7, #9, #10):**  
   Section I was substantially streamlined, and the Abstract was reordered to present the *Subject-Disjoint Primary Benchmark* (88.66% LR, 88.61% SVM) prior to the *Subject-Overlap Ablation* (93.70%). Subgroup disparity metrics (Equal Opportunity Difference, $\text{EOD} = 9.72\text{ pp}$, Table XIV) were framed strictly as empirical error rate disparities rather than universal algorithmic fairness. Literature comparisons (Table XV) were separated into Part A (*Contextual Comparison* for subject-overlap studies) and Part B (*Controlled Comparison* for subject-disjoint baselines). Speculative phenotypic and lighting-contrast claims were completely removed from Sections IV-C and IV-D, and all conclusions were explicitly bounded to the 3 macro-racial categories (Asian, Black, White) of the DemogPairs benchmark.

---

## Part II: Point-by-Point Responses to Reviewer 1

### Comment R1-1: Streamlining Section I (Introduction)
> *"1. the introduction is too long need to be summarized."*

**Author Response:**  
We agree with the reviewer's observation. Section I in the original manuscript contained excessive background exposition regarding demographic disparities and general facial recognition challenges. In the revised manuscript, we substantially restructured and compressed Section I by approximately 28%, directly focusing the narrative on the core challenge of intersectional demographic misclassification, the limitations of single-domain facial geometry, and the orthogonal utility of affective and age representations. We also condensed our contributions into four concise, bulleted scientific statements.

**Changes Made:**  
- **Location in Manuscript:** Section I (*Introduction*), Pages 1–2.
- **Details:** Paragraphs 2–5 were consolidated, eliminating repetitive general statements. The four core contributions are explicitly enumerated on Page 2, Column 2.

---

### Comment R1-2: Restructuring Related Works and Mathematical Equations
> *"2. The related works needs to be modified in better way and add equations."*

**Author Response:**  
We appreciate this constructive guidance. In the revised manuscript, we reorganized Section II (*Related Works*) into three distinct thematic subsections: *(A) Facial Demographic Attribute Classification*, *(B) Vision Transformers in Facial Visual Analysis*, and *(C) Multi-Domain Representation and Feature Fusion*. Furthermore, we formalized the theoretical foundation in Section II (Equations (1)–(4), alongside Equations (5)–(8) in Section III-B) by introducing explicit mathematical formulations for:
1. Joint intersectional demographic mapping over race and gender label spaces: $\mathcal{Y} = \mathcal{Y}_R \times \mathcal{Y}_G$, $|\mathcal{Y}| = 6$ (Eq. 1)
2. Patch projection and positional token embedding: $\mathbf{z}_0 = [\mathbf{x}_{\text{class}}; \, \mathbf{x}_p^1 \mathbf{E}; \, \dots; \, \mathbf{x}_p^N \mathbf{E}] + \mathbf{E}_{\text{pos}}$ (Eq. 2)
3. Scaled Dot-Product Multi-Head Self-Attention (MHSA): $\text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^T}{\sqrt{d_k}}\right)\mathbf{V}$ (Eq. 3)
4. Multi-domain latent feature concatenation: $\mathbf{z}_{\text{fused}} = \mathbf{f}_1 \oplus \mathbf{f}_2 \oplus \dots \oplus \mathbf{f}_M \in \mathbb{R}^{\sum_{m=1}^M d_m}$ (Eq. 4)

**Changes Made:**  
- **Location in Manuscript:** Section II (*Related Works*), Subsections II-A to II-C, Equations (1)–(4).
- **Details:** Text completely restructured into three thematic domains with formalized equations and disciplined literature citations.

---

### Comment R1-3: Redesigning and Clarifying Figure 3
> *"3. The figure 3 needs to be redesigned and explained in better way to show the novelty of the proposed method and also not clear."*

**Author Response:**  
We fully agree. The original diagram lacked visual clarity regarding the parallel extraction and concatenation mechanism. We have completely redesigned Figure 3 (`images/vit_v2.2.png`) as a professional, high-resolution architectural illustration (300+ DPI). The new figure explicitly delineates numbered stages ①–⑦:
1. Standardized pre-cropped facial RGB input resized bilinearly to $224 \times 224 \times 3$ and partitioned into $N = 196$ non-overlapping $16 \times 16$ patches (Stages ①–②, Eq. 5).
2. Linear patch projection ($\mathbf{E} \in \mathbb{R}^{768 \times 768}$) and addition of the learnable `[CLS]` token and positional embeddings $\mathbf{E}_{\text{pos}} \in \mathbb{R}^{197 \times 768}$ (Stages ③–④, Eq. 6), noting explicitly that tokenization and encoding occur independently within each of the three domain-specific ViT-Base backbones.
3. Parallel feature extraction through the three frozen pre-trained Vision Transformer backbones (`ViT-Face`, `ViT-Emotion`, and `ViT-Age`) and extraction of Layer-12 LayerNorm `[CLS]` representations ($\mathbf{f}_{\text{face}}, \mathbf{f}_{\text{emotion}}, \mathbf{f}_{\text{age}} \in \mathbb{R}^{768}$, Stage ⑤, Eq. 7).
4. Ordered direct-sum concatenative fusion into $\mathbf{z}_{\text{tri}} = \mathbf{f}_{\text{face}} \oplus \mathbf{f}_{\text{emotion}} \oplus \mathbf{f}_{\text{age}} \in \mathbb{R}^{2304}$ (Stage ⑥, Eq. 8).
5. Downstream 5-Fold `StratifiedGroupKFold` GridSearchCV optimization across four classifier families for 6-class intersectional prediction (Stage ⑦, Eq. 12).

In the accompanying narrative in Section III-B, we expanded the explanation to clearly articulate the framework-level novelty of integrating complementary static craniofacial biometrics, dynamic affective expressions, and biological aging representations without end-to-end retraining overhead.

**Changes Made:**  
- **Location in Manuscript:** Section III-B (*Vision Transformer*), Figure 3 and Paragraphs 1–3 (Equations (5)–(8)).
- **Details:** Redesigned high-resolution diagram (`images/vit_v2.2.png`) replaced the legacy graphic; stage-by-stage narrative and mathematical walkthrough added.

---

### Comment R1-4: In-Depth Discussion of Error Dynamics in Figure 4
> *"4. Graph in figure 4 needs to be discussed in better way."*

**Author Response:**  
We thank the reviewer for this recommendation. In Section IV-D (*Error Pattern Assessment*), we substantially expanded the empirical discussion of the $6 \times 6$ confusion matrices (Figure 4, comparing Single-Domain `Face`, Dual-Domain `Emotion ⊕ Face`, and Tri-Domain `Face ⊕ Emotion ⊕ Age` on the top-performing Logistic Regression classifier across $N = 2,160$ subject-disjoint test images). Rather than merely reporting diagonal accuracy, we conducted an exact quantitative decomposition of off-diagonal misclassifications:
1. **Progression Across Feature Schemes:** Total misclassifications decrease systematically from **294 errors** (86.39% accuracy on Single `Face`, Figure 4a) to **271 errors** (87.45% on Dual `Emotion ⊕ Face`, Figure 4b) and **245 errors** (88.66% on Tri-Domain `Face ⊕ Emotion ⊕ Age`, Figure 4c).
2. **Intra-Gender Cross-Race vs. Cross-Gender Confusions:** On the Tri-Domain model (245 total errors), misclassifications are predominantly **intra-gender cross-race confusions**, accounting for **165 out of 245 errors (67.35% of all errors; 7.64% of $N = 2,160$)**—down from 212 intra-gender errors on Single `Face` and 185 on Dual `Emotion ⊕ Face`. Meanwhile, **cross-gender misclassifications account for 80 out of 245 errors (32.65% of all errors; 3.70% of $N = 2,160$)**, consisting of 62 same-race cross-gender errors (e.g., `Asian_Females` $\to$ `Asian_Males`: 18; `Asian_Males` $\to$ `Asian_Females`: 17; `Black_Males` $\to$ `Black_Females`: 15; `Black_Females` $\to$ `Black_Males`: 8; `White` cross-gender: 4) and only 18 dual cross-race/cross-gender errors.
3. **Observational Subgroup Error Clusters:** We ground the discussion strictly in observed cell frequencies—for instance, showing how adding affective and age representations reduces `Black_Females` misclassifications from 73 errors (79.72% recall on Single `Face`) to 55 errors (84.72% recall on Tri-Domain, where 37 of the 55 errors occur intra-gender into `White_Females` [23] and `Asian_Females` [14]), while refraining from speculative biological or lighting-contrast attributions.

**Changes Made:**  
- **Location in Manuscript:** Section IV-D (*Error Pattern Assessment*), Figure 4(a)–(c) and Paragraphs 1–3.
- **Details:** Complete cell-by-cell quantitative error decomposition across Single-, Dual-, and Tri-Domain confusion matrices added.

---

### Comment R1-5: Dataset Specifications, Proposed Method Contribution, and Computational Time Cost
> *"5. Experimental works need to mention the dataset used in more detail and show the contribution of your proposed method and also to consider the time cost in the evaluation."*

**Author Response:**  
We appreciate this multi-faceted recommendation:
1. **Dataset Specifications:** In Section III-A (Table I and Figure 2), we detailed DemogPairs (600 unique identities, 18 images per identity, 100 subjects / 1,800 images per intersectional class, total 10,800 images) and formalized the deterministic 80/20 Subject-Disjoint partition (480 training subjects / 8,640 images; 120 held-out testing subjects / 2,160 images).
2. **Proposed Contribution:** In Section IV-A and IV-B (Tables VII–XIII), we demonstrated the statistically significant gain of multi-domain feature fusion over single-domain biometrics ($+2.27\text{ pp}$ on LR and $+2.45\text{ pp}$ on SVM, $p < 0.001$).
3. **Computational Time Cost:** In Section IV-A Paragraph 6, we added a dedicated computational efficiency evaluation (**Table XI**) reporting:
   - Offline ViT feature extraction runtime on an NVIDIA RTX 4060 GPU with in-memory processor caching: **124.5 ms/image** for Tri-Domain (`39.7 ms` Face, `39.7 ms` Emotion, `45.1 ms` Age; **22.41 minutes** total for 10,800 images) vs. CPU baseline (**~1,487 ms/image**; **4.46 hours** total, an **11.9× GPU speedup**).
   - 5-Fold GridSearchCV training duration across **31,920 CV fits** on CPU (LR Tri: **54.8 min** [3,287.07 s] vs. SVM Tri: **511.1 min** [30,666.02 s]; RF Tri: **110.5 min**; GNB Dual: **25.5 min**).
   - Per-sample downstream inference latency (**LR: 0.0046 ms**, **SVM: 4.6785 ms** [>1,000× faster downstream head; end-to-end GPU latency $\approx 124.505\text{ ms/image}$ for LR vs. $\approx 129.179\text{ ms/image}$ for SVM], **RF: 0.0334 ms**, **GNB Dual: 0.0088 ms**) and model storage footprint (**LR: 0.11 MB** vs. **SVM: 36.60 MB**).

**Changes Made:**  
- **Location in Manuscript:** Section III-A (*Dataset*), Table I; Section IV-A (*Global Performance*), Paragraph 6, Table XI.
- **Details:** Comprehensive dataset metadata and complete hardware-verified computational profiling table integrated.

---

### Comment R1-6: Broadening Baseline Method Comparisons
> *"6. the authors need to compare their proposed method with more methods to validate their contribution."*

**Author Response:**  
We agree and have significantly expanded the comparative analysis in **Section IV-E (*Comparison with Prior Studies*), Table XV**, which is structured into two transparent parts:
1. **Part A — Contextual Comparison (Subject-Overlap Literature on DemogPairs, 3 rows):** Compares our historical subject-overlap baseline (SVM Tri-Domain: 93.70%) against preceding DemogPairs studies evaluated under random image-level splits (Putri et al. *JIEET* 2025 MD-ViT `Face ⊕ Age` + XGBoost at 89.07%; Putri et al. *IEEE ICVEE* 2025 Dual-ViT `Emotion ⊕ Face` + SVM at 92.41%).
2. **Part B — Controlled Comparison (Strict Subject-Disjoint 6-Class Benchmark, 9 rows):** Compares our proposed Tri-Domain LR (88.66%) and SVM (88.61%) under identical zero-leakage partitions against classical and deep learning baselines evaluated on the exact same 120 held-out test subjects ($N = 2,160$), including end-to-end CNN transfer learning baselines (ResNet-50, VGG-16, MobileNetV2, EfficientNet-B0) as well as Single-Domain (`ViT-Face`) and Dual-Domain ViT baselines.

**Changes Made:**  
- **Location in Manuscript:** Section IV-E (*Comparison with Prior Studies*), Paragraph 1, Table XV.
- **Details:** Expanded two-part comparative table (12 total entries across Part A Contextual and Part B Controlled) with explicit protocol annotations.

---

### Comment R1-7: Revision of Section V (Conclusion)
> *"7. conclusion part does not show the contribution in good way."*

**Author Response:**  
We thank the reviewer for this constructive critique. We have rewritten Section V (*Conclusion*) into two focused paragraphs to concisely articulate our empirical findings and study boundaries:
1. Demonstration of the effectiveness of multi-domain ViT representation fusion (`Face ⊕ Emotion ⊕ Age`) for 6-class intersectional demographic classification on the DemogPairs subject-disjoint benchmark (LR: **88.66%**, Macro F1: **0.8868**; SVM: **88.61%**, Macro F1: **0.8863**), while noting classifier-dependent behavior on GNB (84.31% Dual vs. 83.61% Tri) and RF (85.00% Tri).
2. Confirmation via paired McNemar testing that tri-domain fusion achieves statistically significant gains over single-domain facial biometrics ($p < 0.001$), with age features providing significant gains on linear LR ($p = 0.0073 < 0.01$) while reaching asymptotic saturation on non-linear RBF SVM relative to `Emotion ⊕ Face` ($p = 0.7343$).
3. Demonstration that linear Logistic Regression shows no statistically significant predictive difference compared to non-linear SVM ($p = 1.0000$, 1,915 vs. 1,914 correct predictions), while its downstream classification head delivers **>1,000× faster inference** (**0.0046 ms** vs. **4.6785 ms**; end-to-end GPU latency $\approx 124.505\text{ ms/image}$) and **>330× smaller storage** (**0.11 MB** vs. **36.60 MB**).
4. Transparent articulation of limitations (scope restricted to DemogPairs' 3 macro-racial groups—Asian, Black, White—and offline frozen ViT extraction overhead) alongside future directions in cross-dataset validation (FairFace, UTKFace), cross-attention/quantization for Edge AI, and Explainable AI.

**Changes Made:**  
- **Location in Manuscript:** Section V (*Conclusion*), Paragraphs 1–2.
- **Details:** Conclusion completely rewritten to highlight calibrated empirical contributions, computational trade-offs, and explicit benchmark boundaries.

---

## Part III: Point-by-Point Responses to Reviewer 2

### Comment R2-1: Methodological Novelty Beyond Concatenation
> *"1. Novelty and contribution: The methodological novelty beyond concatenating three pretrained feature representations and applying conventional classifiers should be more clearly established relative to existing dual-domain and multidomain approaches."*

**Author Response:**  
We thank Reviewer 2 for this critical observation. We have substantially revised Section I and Section III Overview to articulate our framework-level methodological contributions:
1. **Complementary Task-Associated Latent Synergy:** Unlike existing approaches that rely on single-task biometrics or end-to-end multi-task learning (which suffers from negative gradient interference between identity and demographic objectives), our offline frozen framework integrates task-associated latent representations from three specialized semantic subspaces: static craniofacial biometrics (`ViT-Face`), dynamic affective expressions (`ViT-Emotion`), and biological aging cues (`ViT-Age`).
2. **Comprehensive 28-Model Dual Benchmark & Fold-Isolated Optimization:** We present a systematic comparative investigation across four diverse classifier families (linear, kernel non-linear, ensemble tree, and probabilistic Bayesian) coupled with leakage-free 5-Fold `StratifiedGroupKFold` GridSearchCV (**912 hyperparameter combinations per scheme; 31,920 cross-validation fits and 28 final refits**), demonstrating that $L_2$-regularized linear hyperplanes (LR) match complex RBF kernels on 2,304-dimensional frozen multi-domain transformer embeddings ($p = 1.0000$).
3. **Identity Leakage Quantification & Inferential Calibration:** We provide an empirical ablation study rigorously quantifying the facial identity memorization penalty ($\Delta = -5.09\text{ pp}$ on SVM and $-4.07\text{ pp}$ on LR) alongside paired McNemar testing to characterize domain-specific feature saturation.

**Changes Made:**  
- **Location in Manuscript:** Section I, Paragraphs 5–6; Section III Overview; Section III-G.
- **Details:** Explicit clarification of the framework-level novelty, complementary latent synergy, and fold-isolated evaluation design.

---

### Comment R2-2: Data Leakage and Generalization (Critical Concern)
> *"2. Data leakage and generalization: The image-level stratified split may allow images of the same identity to occur in both training and test sets. Please clarify whether identity overlap exists and provide subject-disjoint evaluation to establish genuine generalization."*

**Author Response:**  
Reviewer 2 has raised a profound methodological point that was pivotal to the advancement of this research. We acknowledge that the original experimental partition utilized an image-level stratified split, which indeed introduced identity overlap (593 out of 600 unique subjects had co-occurring images in both the training and test sets).

To definitively resolve this issue, we completely restructured the research into an authoritative **Dual-Benchmark Framework**:
1. **Primary Benchmark (Strict Subject-Disjoint Partitioning — Zero Identity Leakage):**  
   Using deterministic identity-level partitioning (`train_test_split` on sorted unique `subject_id` lists per subgroup with `train_size=0.8` and `random_state=42`, Table I), we isolated the 600 unique DemogPairs subjects into **480 training subjects** (8,640 images; 80 subjects / 1,440 images per class) and **120 held-out test subjects** (2,160 images; 20 subjects / 360 images per class). Furthermore, hyperparameter tuning on the training set strictly employs 5-Fold `StratifiedGroupKFold` (`n_splits=5`, `shuffle=True`, `random_state=42`, `groups=subject_id`). No identity in the test set is ever seen during training, scaling, PCA fitting, or cross-validation (**0.00% identity leakage**). Under this primary benchmark, Logistic Regression Tri-Domain achieved **88.66%**, SVM Tri-Domain achieved **88.61%**, RF Tri-Domain achieved **85.00%**, and GNB Dual-Domain (`Emotion ⊕ Face`) achieved **84.31%** (83.61% on Tri-Domain).
2. **Historical Baseline (Subject-Overlap Ablation):**  
   Rather than discarding the previous image-level results (93.70% on SVM Tri-Domain, 92.73% on LR Tri-Domain), we preserve them as a transparent **Comparative Ablation Study on Data Leakage** in Section IV-B (**Table XII**) to directly quantify the facial identity memorization effect ($\Delta = -5.09\text{ pp}$ on SVM and $-4.07\text{ pp}$ on LR).

**Changes Made:**  
- **Location in Manuscript:** Abstract; Section III-A (*Dataset*), Paragraph 2, Table I; Section III-G (*Classification Pipeline*); Section IV-A (*Global Performance*), Tables VII–X; Section IV-B (*Feature Ablation Study*), Paragraph 2, Table XII.
- **Details:** Full implementation and presentation of the 28-model Subject-Disjoint Primary Benchmark alongside the comparative data leakage ablation in Table XII.

---

### Comment R2-3: Preprocessing and Reproducibility Specifications
> *"3. Preprocessing and reproducibility: Please specify the exact checkpoint versions, image processors, normalization parameters, and feature extraction procedures used for all three pretrained ViT models."*

**Author Response:**  
We agree completely. In Section III-A Paragraph 2 and Section III-B Paragraphs 2–3, we documented the exact reproducibility specifications verified directly from the codebase (`experiment/code/utils/extraction.py`) and each model's `preprocessor_config.json`:
- **ViT-Face:** HuggingFace checkpoint `skutaada/VIT-VGGFace` (Git revision SHA: `e85f0c9`, ViT-Base/16 fine-tuned on VGGFace2).
- **ViT-Emotion:** HuggingFace checkpoint `dima806/facial_emotions_image_detection` (Git revision SHA: `747cf16`, ViT-Base/16 fine-tuned on FER-2013).
- **ViT-Age:** HuggingFace checkpoint `dima806/facial_age_image_detection` (Git revision SHA: `ad35933`, ViT-Base/16 fine-tuned on UTKFace and IMDB-WIKI).
- **Standardized Image Preprocessing & Normalization:** Because DemogPairs images are already provided as centered, pre-cropped facial images, no additional MTCNN face detection or alignment is applied. Images are converted to 3-channel RGB, resized via bilinear interpolation to $224 \times 224 \times 3$ pixels through each model's `AutoImageProcessor`, rescaled by $1/255$ to $[0, 1]$, and normalized per channel using **uniform mean $\mu = [0.5, 0.5, 0.5]$ and standard deviation $\sigma = [0.5, 0.5, 0.5]$** to the range $[-1, 1]$ across all three checkpoints.
- **Feature Extraction Protocol:** Normalized tensors are passed through the frozen 12-layer ViT-Base encoders under `torch.no_grad()`, and the 768-dimensional representation $\mathbf{f}_{\text{domain}} = \text{LN}(\mathbf{z}_L^0) \in \mathbb{R}^{768}$ (Eq. 7) is extracted from the final LayerNorm `[CLS]` output `last_hidden_state[:, 0, :]`. The seven single-, dual-, and tri-domain ablation configurations are summarized in **Table II**.

**Changes Made:**  
- **Location in Manuscript:** Section III-A, Paragraph 2; Section III-B (*Vision Transformer*), Paragraphs 2–3, Equation (7), and Table II.
- **Details:** Exact HuggingFace checkpoint IDs, Git revision SHAs, uniform $\mu = \sigma = [0.5, 0.5, 0.5]$ normalization parameters, and Layer-12 `[CLS]` extraction formulas fully documented.

---

### Comment R2-4: Hyperparameter Search Space Consistency
> *"4. Hyperparameter search consistency: The reported totals of 1,086 configurations, 38,010 cross-validation fits, and 28 final refits should be reconciled with the individual search spaces reported in Tables 3–6."*

**Author Response:**  
We thank the reviewer for catching this arithmetic discrepancy. Upon auditing the exact execution scripts (`experiment/code/md/`), we identified that the Logistic Regression grid in the initial draft overcounted untested parameter values. In the revised manuscript (Section III-C to III-G, **Tables III–VI**), we reconciled the exact search spaces executed in code:
- **Random Forest (Table III):** 2 scalers (`None`, `MinMaxScaler`) $\times$ 3 PCA (`None`, `0.50`, `0.75`) $\times$ 2 `n_estimators` (`{100, 200}`) $\times$ 3 `max_depth` (`{None, 10, 30}`) $\times$ 2 `max_features` (`{'sqrt', 'log2'}`) $\times$ 2 `min_samples_split` (`{2, 5}`) $\times$ 2 `min_samples_leaf` (`{1, 2}`) = **288 combinations** (1,440 CV fits/scheme; 10,080 fits total).
- **Gaussian Naive Bayes (Table IV):** 2 scalers $\times$ 3 PCA $\times$ 40 `var_smoothing` values (`np.logspace(-9, 2, 40)`) = **240 combinations** (1,200 CV fits/scheme; 8,400 fits total).
- **Logistic Regression (Table V):** 2 scalers $\times$ 3 PCA $\times$ 4 `C` values (`{0.01, 0.1, 1, 10}`) $\times$ 2 `solver` options (`{'lbfgs', 'saga'}`) $\times$ 2 `max_iter` values (`{500, 1000}`) = **96 combinations** (480 CV fits/scheme; 3,360 fits total).
- **Support Vector Machine (Table VI):** Full Cartesian grid of 2 scalers $\times$ 3 PCA $\times$ 4 `C` (`{0.01, 0.1, 1, 10}`) $\times$ 3 `kernel` (`{'linear', 'rbf', 'poly'}`) $\times$ 2 `gamma` (`{'scale', 'auto'}`) $\times$ 2 `degree` (`{2, 3}`) = **288 Cartesian evaluations** (1,440 CV fits/scheme; 10,080 fits total). We also explicitly note in Table VI that these 288 Cartesian evaluations correspond to **108 effective unique parameter configurations** (since `degree` is only active for `'poly'` and `gamma` is inactive for `'linear'`).
- **Total per Feature Scheme:** $288 + 240 + 96 + 288 = \mathbf{912}\text{ combinations}$ ($\times 5\text{ folds} = \mathbf{4,560}\text{ CV fits/scheme}$).
- **Total Cross-Validation Fits Across All 7 Feature Schemes:** $4,560 \times 7 = \mathbf{31,920}\text{ cross-validation fits}$.
- **Final Refits:** 4 classifiers $\times$ 7 feature schemes = $\mathbf{28}\text{ final refits}$ on the full 480-subject training set.

**Changes Made:**  
- **Location in Manuscript:** Section I, Paragraph 5; Section III-C to III-F, Tables III–VI; Section III-G (*Classification Pipeline*), Paragraph 1.
- **Details:** Reconciled Table V (LR: 96 combinations), added the 108 unique effective configuration note to Table VI (SVM: 288 Cartesian combinations), and updated all totals to **912 combinations per scheme** and **31,920 total CV fits** (+ 28 refits).

---

### Comment R2-5: Statistical Significance and McNemar Testing
> *"5. Statistical interpretation: The SVM accuracy improvement from 93.29% to 93.70% is not statistically significant according to the reported McNemar test (p = 0.3057). Consequently, claims of tri-domain superiority and feature saturation should be appropriately qualified."*

**Author Response:**  
We fully agree with the reviewer's statistical rigor. In the revised manuscript (Section IV-A and Section IV-B, **Table XIII**), we conducted paired McNemar tests with Edwards continuity correction alongside exact two-sided binomial tests and 95% Wilson Score Confidence Intervals across the subject-disjoint test set ($N = 2,160$):
1. **Tri-Domain vs. Single-Domain (`Face`):** Statistically significant on both top classifiers—SVM Tri (88.61%) vs. Single `Face` (86.16%) achieved $+2.45\text{ pp}$ (+53 net images, $b=91, c=38, \chi^2 = 20.9612, p = 3.46 \times 10^{-6} < 0.001$), and LR Tri (88.66%) vs. Single `Face` (86.39%) achieved $+2.27\text{ pp}$ (+49 net images, $b=83, c=34, \chi^2 = 19.6923, p = 6.78 \times 10^{-6} < 0.001$).
2. **Tri-Domain vs. Dual-Domain (Qualification of Feature Saturation):**
   - On non-linear RBF SVM, adding the `Age` domain on top of `Emotion ⊕ Face` (88.43% $\to$ 88.61%) yielded $+0.19\text{ pp}$ (+4 net images, $b=41, c=37, \chi^2 = 0.1154, p = 0.7343 > 0.05$). We explicitly qualify that this indicates **asymptotic feature saturation** specifically when adding age cues to the combined affective-biometric representation on the RBF kernel (whereas compared to Dual `Face ⊕ Age` at 87.55%, the transition to SVM Tri-Domain remains statistically significant at $+1.06\text{ pp}$, +23 net images, $b=47, c=24, \chi^2 = 6.8169, p = 0.0086 < 0.01$).
   - On linear Logistic Regression, adding `Age` on top of `Emotion ⊕ Face` (87.45% $\to$ 88.66%) yielded $+1.20\text{ pp}$ (+26 net images, $b=57, c=31, \chi^2 = 7.1023, p = 0.0073 < 0.01$), demonstrating a statistically significant contribution of biological age features for linear decision hyperplanes.
   - We also transparently report that fusion gains are **classifier-dependent** on tree/generative models: RF Tri-Domain (85.00%) shows a non-significant $+0.14\text{ pp}$ difference over Dual `Emotion ⊕ Face` (84.86%, $p = 0.8408$), while GNB peaks on Dual `Emotion ⊕ Face` (84.31%) compared to Tri-Domain (83.61%, $p = 0.2349$).
3. **LR Tri vs. SVM Tri (Predictive Parity):** The paired McNemar test between LR Tri (88.66%, 1,915/2,160) and SVM Tri (88.61%, 1,914/2,160) yielded $b=36, c=35, \chi^2 = 0.0000$, and $p = 1.0000$. Because McNemar's test evaluates the null hypothesis of equal marginal error rates (rather than a two one-sided equivalence test), we carefully frame this result as showing **no statistically significant difference in predictive performance (predictive parity)**, which motivates selecting LR based on its superior downstream computational efficiency.

**Changes Made:**  
- **Location in Manuscript:** Abstract; Section I, Paragraph 6; Section IV-A, Paragraphs 3–5; Section IV-B (*Feature Ablation Study*), Paragraphs 1 & 3, **Table XIII**; Section V, Paragraph 1.
- **Details:** Added Table XIII with discordant pair counts ($b/c$), Edwards $\chi^2$, and exact binomial $p$-values, and qualified all saturation and parity claims throughout the manuscript.

---

### Comment R2-6: Fairness Analysis Scope and Limitations
> *"6. Fairness analysis: The reported Equal Opportunity Difference values provide useful subgroup information but do not establish comprehensive demographic fairness. Please clarify the scope and limitations of the fairness claims."*

**Author Response:**  
We thank Reviewer 2 for this crucial ethical clarification. We have revised Section IV-C (*Intersectional Subgroup Performance*, **Table XIV**) and Section V (*Conclusion*) to explicitly delimit our subgroup disparity analysis:
1. We report per-subgroup Precision, Recall (TPR), F1-Score, and One-vs-Rest (OvR) Accuracy across the 6 intersectional classes in **Table XIV**, showing that the Equal Opportunity Difference ($\text{EOD} = \Delta\text{TPR} = 9.72\text{ pp}$ between `White_Males` at 94.44% TPR [5.56% FNR] and `Black_Females` at 84.72% TPR [15.28% FNR]) quantifies empirical recall disparity on the evaluated test set ($N = 2,160$).
2. We explicitly state that EOD and OvR metrics (noting the 5:1 negative-to-positive class imbalance inherent in 6-class OvR accuracy) do not constitute a comprehensive algorithmic fairness audit or a guarantee of universal demographic fairness (which would require evaluating demographic parity, equalized odds, calibration, and counterfactual fairness across unconstrained socio-cultural cohorts).

**Changes Made:**  
- **Location in Manuscript:** Section III-H (*Evaluation Metrics*); Section IV-C (*Intersectional Subgroup Performance*), Paragraphs 1–2, **Table XIV**.
- **Details:** Text revised to frame Table XIV and EOD ($9.72\text{ pp}$) strictly as an empirical subgroup error disparity audit rather than a universal fairness certification.

---

### Comment R2-7: Contextualizing Prior Literature Comparisons
> *"7. Baseline comparison: Please clarify whether the prior methods in Table 12 used comparable data partitions, preprocessing, and evaluation protocols. Otherwise, the comparison should be presented as contextual rather than a controlled benchmark."*

**Author Response:**  
We agree with the reviewer's distinction. In Section IV-E (*Comparison with Prior Studies*), we restructured the comparison into **Table XV** with two explicitly separated panels:
1. **Part A — Contextual Comparison (Subject-Overlap Protocol):** Explicitly labels prior DemogPairs publications (Putri et al. *JIEET* 2025 at 89.07% and Putri et al. *ICVEE* 2025 at 92.41%) alongside our historical subject-overlap baseline (93.70%) as a **contextual comparison**, noting that those prior studies utilized random image-level splits with subject overlap rather than identity-disjoint partitions.
2. **Part B — Controlled Comparison (Strict Subject-Disjoint Protocol):** Provides a strictly controlled benchmark comparing our proposed Tri-Domain LR (88.66%) and SVM (88.61%) against CNN transfer learning baselines (ResNet-50, VGG-16, MobileNetV2, EfficientNet-B0) and single/dual-domain ViT baselines evaluated on the exact same 480-subject training and 120-subject held-out test partition.

**Changes Made:**  
- **Location in Manuscript:** Section IV-E (*Comparison with Prior Studies*), Paragraph 1, **Table XV**.
- **Details:** Divided Table XV into Part A (*Contextual Comparison*) and Part B (*Controlled Comparison*) with explicit protocol disclaimers in both the narrative and table notes.

---

### Comment R2-8: Reporting Computational Efficiency Metrics
> *"8. Computational efficiency: Please report feature extraction time, classifier training time, inference latency, memory consumption, and model storage requirements to substantiate the efficiency claims."*

**Author Response:**  
We appreciate this practical recommendation. In Section IV-A Paragraph 6, we added **Table XI** (*Computational Efficiency and Resource Consumption Profile*), reporting all five empirical efficiency dimensions measured on standardized hardware (**Intel Core i9-13900H CPU, 32 GB DDR5 RAM, and NVIDIA GeForce RTX 4060 Laptop GPU with 8 GB VRAM**):
- **Offline ViT Feature Extraction Time (10,800 images):** On the NVIDIA RTX 4060 GPU with in-memory processor caching (`experiment/code/times/*.json`), extraction requires **39.7 ms/image** (`ViT-Face`), **39.7 ms/image** (`ViT-Emotion`), and **45.1 ms/image** (`ViT-Age`), totaling **124.5 ms/image** (**22.41 minutes** total for all three domains), compared to the CPU baseline of **~1,487 ms/image** (`467.0 ms` + `476.7 ms` + `543.1 ms`; **4.46 hours** total), representing an **11.9× GPU acceleration**.
- **Classifier Training Time (5-Fold GridSearchCV on CPU):** Logistic Regression Tri-Domain: **54.8 min** (3,287.07 s); SVM Tri-Domain: **511.1 min** (30,666.02 s; LR is **9.3× faster to train**); Random Forest Tri-Domain: **110.5 min** (6,628.08 s); GNB Dual-Domain (`Emotion ⊕ Face`): **25.5 min** (1,529.41 s).
- **Downstream Inference Latency per Sample:** Logistic Regression Tri-Domain: **0.0046 ms/sample**; SVM Tri-Domain: **4.6785 ms/sample** (LR classification head is **>1,000× [1,027×] faster**); Random Forest Tri-Domain: **0.0334 ms/sample**; GNB Dual-Domain: **0.0088 ms/sample**. Including offline/online GPU feature extraction ($124.5\text{ ms}$), the total end-to-end GPU inference latency is **$\approx 124.505\text{ ms/image}$ for LR** vs. **$\approx 129.179\text{ ms/image}$ for SVM**.
- **Model Storage on Disk:** Logistic Regression Tri-Domain: **0.11 MB**; SVM Tri-Domain: **36.60 MB** (**>330× more compact**); Random Forest Tri-Domain: **6.19 MB**; GNB Dual-Domain: **0.78 MB** (GNB Tri-Domain: **1.36 MB**).
- **Memory & Cache Footprint:** Held-out test feature array ($N = 2,160$, `float32`) requires **18.98 MB RAM** for Tri-Domain (2,304-d) and **12.66 MB RAM** for Dual-Domain (1,536-d), while serialized offline feature caches occupy **30.8 MB per domain** (**92.4 MB** total for Tri-Domain).

We also explicitly qualify in Section IV-A Paragraph 6 and Section V that LR's ultra-lightweight footprint (`0.11 MB`, `0.0046 ms`) applies to the **downstream classification head**, whereas full end-to-end deployment on low-power Edge AI devices will require compressing the three ViT backbones via quantization or knowledge distillation.

**Changes Made:**  
- **Location in Manuscript:** Section III-I (*Computational Environment*); Section IV-A (*Global Performance*), Paragraph 6, **Table XI**; Section V (*Conclusion*), Paragraphs 1–2.
- **Details:** Dedicated hardware-verified computational profiling table (Table XI) and qualified end-to-end vs. downstream efficiency discussion added.

---

### Comment R2-9: Empirical Grounding of Phenotypic Interpretations
> *"9. Results and discussion: Several interpretations concerning phenotypic overlap, the contribution of age-related features, and reductions in inter-racial errors remain insufficiently supported by confusion matrices alone. These statements should be qualified or supported by additional analyses."*

**Author Response:**  
We acknowledge this valid critique. In the Abstract, Section IV-C (*Intersectional Subgroup Performance*), and Section IV-D (*Error Pattern Assessment*), we completely excised speculative causal hypotheses regarding craniofacial phenotypic morphology, epidermal aging texture, and lighting-contrast interactions:
1. All discussions of subgroup performance disparities (Section IV-C) and off-diagonal confusion patterns (Section IV-D) have been strictly recalibrated to report purely observational error frequency distributions across the $N = 2,160$ test samples (e.g., reporting that on LR Tri-Domain, 37 of the 55 misclassifications on `Black_Females` occur into `White_Females` [23] and `Asian_Females` [14], and 23 of the 48 misclassifications on `Asian_Females` occur into `Black_Females`).
2. The contribution of the `Age` domain on Logistic Regression is explained strictly through measurable quantitative reductions in intra-gender cross-race misclassifications (from 185 errors on `Emotion ⊕ Face` down to 165 errors on `Face ⊕ Emotion ⊕ Age`) and paired McNemar statistical significance ($p = 0.0073$), rather than unverified biological assumptions.

**Changes Made:**  
- **Location in Manuscript:** Abstract; Section IV-C, Paragraph 2; Section IV-D (*Error Pattern Assessment*), Paragraphs 2–3.
- **Details:** Speculative phenotypic and lighting-contrast claims removed; narrative strictly anchored in empirical confusion matrix counts and McNemar statistics.

---

### Comment R2-10: Restricting Conclusions and Generalization Scope
> *"10. Conclusion and limitations: The conclusions should be restricted to the evaluated DemogPairs benchmark unless additional cross-identity or external-dataset validation is provided."*

**Author Response:**  
We completely agree. In both the **Abstract** and **Section V (*Conclusion*, Paragraphs 1–2)**, we explicitly restricted the scope of our conclusions to the 6 intersectional subgroups spanning the **3 macro-racial categories (Asian, Black, White)** evaluated within the DemogPairs subject-disjoint benchmark. Furthermore, in Section V Paragraph 2, we dedicated an explicit *Limitations and Future Research Directions* discussion stating that generalizability to broader multiracial populations (e.g., Hispanic, Middle Eastern, South Asian, or Indigenous cohorts) and unconstrained *in-the-wild* capture conditions requires external cross-dataset validation on benchmarks such as FairFace and UTKFace.

**Changes Made:**  
- **Location in Manuscript:** Abstract; Section V (*Conclusion*), Paragraphs 1–2.
- **Details:** Generalization claims explicitly bounded to the 3 macro-racial groups of DemogPairs in both the Abstract and Conclusion, with external cross-dataset validation formally designated as future work.

---

## Part IV: Compliance Checklist Verification

| Checklist Item | Status | Verification Detail |
|:---|:---:|:---|
| **Author Response File** | **Verified** | Detailed point-by-point document prepared with R $\to$ A $\to$ C structure. |
| **Highlighted PDF** | **Verified** | All textual additions, parameter tables, and mathematical formulas highlighted in yellow. |
| **Clean Manuscript** | **Verified** | Standard IEEE Access two-column clean PDF and complete LaTeX source ZIP prepared. |
| **Request for Byline Change** | **Verified** | Official signed form prepared justifying Dr. Shukor Sanim Mohd Fauzi's contribution. |
| **Resubmission Checklist** | **Verified** | 10-point IEEE Access quality compliance verified. |

We trust that these extensive revisions, rigorous evaluations under strict subject-disjoint partitioning, comprehensive statistical validations, and calibrated discussions fully satisfy all reviewers' inquiries and meet the high scientific standards of *IEEE Access*.

Sincerely,

**Dr. Ir. Ricky Eka Putra, S.Kom., M.Kom.** (Corresponding Author)  
Department of Informatics, Faculty of Informatics  
Universitas Negeri Surabaya (UNESA), Surabaya, Indonesia  
Email: `rickyeka@unesa.ac.id`
