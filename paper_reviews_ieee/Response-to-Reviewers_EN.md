# IEEE Access - Response to Reviewers

**Original Manuscript ID:** Access-2026-50857  
**Original Article Title:** "Multi-Domain Vision Transformer Fusion for Intersectional Demographic Classification from Facial Images"  
**To:** IEEE Access Editor  
**Re:** Response to reviewers  

---

Dear Editor,

Thank you for allowing a resubmission of our manuscript, with an opportunity to address the reviewers' comments.

We are uploading:
- **(a)** our point-by-point response to the comments (below) (response to reviewers, under "Author's Response Files"),
- **(b)** an updated manuscript with yellow highlighting indicating changes (as "Highlighted PDF"), and
- **(c)** a clean updated manuscript without highlights ("Main Manuscript").

Through this resubmission, we also kindly request the Editor to assign the same reviewers if possible.

Best regards,  
Dr. Ricky Eka Putra et al.

---

## Reviewer #1

### Reviewer #1, Concern #1:
> *"1. the introduction is too long need to be summarized."*

**Author response:**  
We agree with the reviewer regarding the need to condense Section I (*Introduction*). The background narrative has been summarized and restructured into seven focused paragraphs with a strict discipline of at most two citations per sentence to improve readability, while explicitly articulating our four primary scientific contributions.

**Author action:**  
We updated Section I (*Introduction*, Pages 1–2) by condensing the introductory paragraphs and adding the explicit summary of four scientific contributions on Page 2:

> The primary scientific contributions of this study are summarized in four essential aspects as follows:
> 1. Formulation of a seven-feature-scheme ablation framework integrating frozen pre-trained ViT backbones with leakage-free fold-level preprocessing and hyperparameter optimization across four classifier families for intersectional demographic classification.
> 2. Establishment of an identity-leakage-free evaluation benchmark on the DemogPairs dataset and a comparative data leakage ablation study to quantify the effects of facial identity memorization.
> 3. Paired inferential statistical significance evaluation validating the significant superiority of multi-domain representations over single-domain baselines, demonstrating predictive parity between the top-performing linear and non-linear models, and uncovering linear age feature complementarity versus non-linear asymptotic representation saturation.
> 4. Presentation of a comprehensive computational efficiency profile encompassing ViT extraction time, training cost, inference latency, and memory footprint, realizing ultra-lightweight downstream classification heads for practical deployment.

---

### Reviewer #1, Concern #2:
> *"2. The related works needs to be modified in better way and add equations."*

**Author response:**  
We thank the reviewer for this constructive suggestion. Section II (*Related Works*) has been reorganized into three coherent thematic subsections—*(II-A) Demographic Face Recognition*, *(II-B) Vision Transformers in Face Analysis*, and *(II-C) Multi-Domain Feature Fusion*—accompanied by formal mathematical formulations to strengthen the theoretical foundation.

**Author action:**  
We updated Section II (*Related Works*, Pages 2–4) by restructuring the literature review into Subsections II-A through II-C and adding four formal equations with complete variable definitions on Page 3: the Kernel Extreme Learning Machine (KELM) decision function [Eq. (1)], linear patch projection [Eq. (2)], Scaled Dot-Product Attention within Multi-Head Self-Attention [Eq. (3)], and multi-domain concatenation fusion [Eq. (4)], followed by an explicit positioning of our research novelty at the end of Subsection II-C (Pages 3–4).

---

### Reviewer #1, Concern #3:
> *"3. The figure 3 needs to be redesigned and explained in better way to show the novelty of the proposed method and also not clear."*

**Author response:**  
We fully agree that the previous architecture diagram lacked clarity. We redesigned **Figure 3** into a high-resolution architecture diagram illustrating seven sequential integrated stages: (1) 224 × 224 RGB image preprocessing, (2) partitioning into 196 patches of 16 × 16 pixels, (3) linear projection into a 768-dimensional latent space, (4) prepending the `[CLS]` token and adding positional embeddings (Stages 1–4 operate independently on each ViT backbone), (5) parallel extraction of the 12th-layer `[CLS]` token from three frozen pre-trained ViT backbones (`ViT-Face`, `ViT-Emotion`, `ViT-Age`), (6) direct concatenation ⊕ into a 2,304-dimensional feature vector, and (7) downstream six-class classification using four classical classifiers.

**Author action:**  
We replaced **Figure 3** (Page 6) with the redesigned architecture diagram and expanded the explanation of the seven-stage pipeline in Section III-B (Pages 4–5, Eq. (5)–(8)) to clearly highlight the novelty of our frozen multi-domain fusion framework without end-to-end fine-tuning.

---

### Reviewer #1, Concern #4:
> *"4. Graph in figure 4 needs to be discussed in better way."*

**Author response:**  
We thank the reviewer for this feedback. In Section IV-D (*Error Pattern Assessment*), we deepened the discussion of the 6 × 6 Logistic Regression confusion matrices on the 2,160 held-out test images across the three representation stages in **Figure 4(a)–(c)** by quantitatively decomposing the off-diagonal error cells.

**Author action:**  
We updated **Figure 4(a)–(c)** (Page 12) and expanded Section IV-D (Pages 11 and 13) by adding the following quantitative error decomposition analysis on Page 13:

> Quantitative decomposition of the off-diagonal cells in the confusion matrices reveals that the classification error pattern is dominated by same-gender cross-race misclassifications. In the tri-domain model (245 errors), intra-gender cross-race confusion accounts for 165 images (67.35% of total errors or 7.64% of all test samples), declining significantly from 194 cases in the single-domain model. The largest confusion cells are observed for Black Males to Asian Males (23 images), Black Females to White Females (23 images), and Asian Females to Black Females (23 images). Conversely, cross-gender errors amount to only 80 images (32.65% of total errors or 3.70% of all test samples). This pattern aligns with the recall profile of Black Females (84.72%), where 37 of their 55 errors occur intra-gender toward White Females (23) and Asian Females (14).

---

### Reviewer #1, Concern #5:
> *"5. Experimental works need to mention the dataset used in more detail and show the contribution of your proposed method and also to consider the time cost in the evaluation."*

**Author response:**  
We addressed all three aspects: (1) detailing the 600-subject DemogPairs structure (10,800 balanced images across 6 classes; 18 images/subject) and the 80/20 subject-disjoint partition, (2) establishing the inferential significance of tri-domain fusion over single-domain baselines ($p < 0.001$), and (3) reporting comprehensive time cost and computational efficiency profiles.

**Author action:**  
We updated Section III-A (Page 4), **Figure 2** (Page 5), and **Table 1** (Page 6) for detailed dataset specifications, Section III-I (Page 8) for experimental hardware specifications, and Section IV-B and **Table 14** (Pages 11–12) for inferential statistical validation of our method's contribution ($p < 0.001$). Additionally, we added **Table 11** (Page 10), **Table 12** (Page 12), and Paragraph 6 of Section IV-A (Pages 9 and 11), reporting that offline ViT extraction on an RTX 4060 GPU requires **124.50 ms/image** (22.41 minutes total for 10,800 images), 5-fold CV training of Tri-Domain LR (**54.78 minutes**) is **9.3× faster** than SVM (**511.10 minutes**), and downstream LR inference (**0.0046 ms/sample**) is **1,027× (>1,000×) faster** than SVM (**4.6785 ms/sample**).

---

### Reviewer #1, Concern #6:
> *"6. the authors need to compare their proposed method with more methods to validate their contribution."*

**Author response:**  
We agree and have substantially expanded the empirical comparison by clearly separating prior studies that used image-level partitioning (*Stratified*) from our controlled evaluations under the leakage-free partition (*Subject-Disjoint*).

**Author action:**  
We updated Section IV-E and **Table 16** (Page 13) to 12 empirical comparison entries, comprising three models under the *Stratified* protocol (Putri et al. *JIEET* 2025: 89.07%; Putri et al. *IEEE ICVEE* 2025: 92.41%; and our historical baseline: 93.70%) and nine controlled configurations under the *Subject-Disjoint* protocol (four single-domain configurations [`Face` on LR and SVM, `Emotion` on SVM, and `Age` on SVM], two dual-domain configurations `Emotion` ⊕ `Face` [on SVM at 88.43% and GNB at 84.31%], and three tri-domain configurations across RF [85.00%], SVM [88.61%], and LR [88.66%]).

---

### Reviewer #1, Concern #7:
> *"7. conclusion part does not show the contribution in good way."*

**Author response:**  
We thank the reviewer for this feedback and have rewritten Section V (*Conclusion*) into two structured paragraphs that summarize the key empirical contributions, predictive parity and computational efficiency, research limitations, and future research directions.

**Author action:**  
We updated Section V (*Conclusion*, Page 14) into two structured paragraphs; the first paragraph summarizing our main conclusions and contributions is quoted verbatim below (while the research limitations in Paragraph 2 are quoted verbatim in our response to Reviewer #2, Concern #10):

> This study demonstrates the effectiveness of multi-domain ViT representation fusion (Face ⊕ Emotion ⊕ Age) for the classification of six intersectional classes from three macro-racial groups (Asian, Black, White) on the DemogPairs dataset. Under the Strict Subject-Disjoint Partitioning protocol with 0% identity leakage (480 training subjects and 120 held-out testing subjects), the LR classifier achieved peak performance with an accuracy of 88.66%, macro precision of 88.75%, macro recall of 88.66%, and macro F1-score of 88.68%, followed by the SVM classifier with an accuracy of 88.61%, macro precision of 88.71%, macro recall of 88.61%, and macro F1-score of 88.63%. Paired inferential statistical significance testing of McNemar demonstrated the significance of tri-domain fusion over the single-domain Face representation (p < 0.001) and confirmed predictive parity between LR and SVM (p = 1.0000, with a net difference of one sample out of 2,160 images). Algorithmic fairness evaluation across subgroups demonstrated prediction stability with a recall range from 84.72% to 94.44% and an EOD gap of 9.72 pp across both top-performing models. From the aspect of computational efficiency, the downstream LR classifier proved to be the most optimal with an inference latency of 0.0046 ms per sample and a model size of 0.11 MB, realizing an ultra-lightweight classification head for practical deployment.

---

## Reviewer #2

### Reviewer #2, Concern #1:
> *"1. Novelty and contribution: The methodological novelty beyond concatenating three pretrained feature representations and applying conventional classifiers should be more clearly established relative to existing dual-domain and multidomain approaches."*

**Author response:**  
We clarified our framework-level novelty beyond simple feature concatenation across three dimensions: (1) offline synergy of three complementary latent spaces (`ViT-Face`, `ViT-Emotion`, `ViT-Age`) extracted from frozen pre-trained backbones to preserve computational efficiency without retraining or fine-tuning, (2) systematic investigation of seven feature schemes across four classifier families under fully isolated *5-Fold StratifiedGroupKFold* cross-validation, demonstrating predictive parity between a linear LR separator and a non-linear RBF kernel ($p = 1.0000$), and (3) empirical characterization of the facial identity memorization effect (5.09 pp) alongside the distinction between linear age-feature complementarity and non-linear asymptotic representation saturation.

**Author action:**  
We updated the conceptual novelty positioning in Section I Paragraphs 5–6 (Page 2), Section II-C Paragraph 2 (Pages 3–4), and Section III Overview (Page 4), and presented the empirical proof of predictive parity ($p = 1.0000$) and the identity memorization effect (5.09 pp) in Section IV-B (Pages 11–12).

---

### Reviewer #2, Concern #2:
> *"2. Data leakage and generalization: The image-level stratified split may allow images of the same identity to occur in both training and test sets. Please clarify whether identity overlap exists and provide subject-disjoint evaluation to establish genuine generalization."*

**Author response:**  
We confirm that the image-level random split in the initial manuscript induced extensive identity overlap: based on our internal historical partition audit, 593 of the 600 subjects appeared simultaneously in both the training and test sets, which is summarized in Section IV-B (Page 11) and **Table 13** (Page 12) as full subject-overlap evaluation. To resolve this rigorously, we established **Strict Subject-Disjoint Partitioning** as our primary benchmark (480 training subjects / 8,640 images; 120 held-out testing subjects / 2,160 images; **0% identity leakage**), employing *5-Fold StratifiedGroupKFold* (`groups = subject_id`) for all hyperparameter tuning, feature scaling, and PCA fitting. The legacy partition results are transparently retained as a data leakage ablation study to quantify facial identity memorization (a 5.09 pp drop on SVM from 93.70% to 88.61%, and a 4.07 pp drop on LR from 92.73% to 88.66%).

**Author action:**  
We updated the Abstract (Page 1), Section III Overview (Page 4), **Figure 1** (Page 5, labeled *"80:20 Subject-Disjoint Split"* and *"5-Fold StratifiedGroupKFold Cross-Validation"*), Section III-A and **Table 1** (Pages 4 and 6), Section III-G (Page 7), all primary benchmarks in **Table 7–10** (Pages 9–10), and the data leakage ablation study in Section IV-B and **Table 13** (Pages 11–12).

---

### Reviewer #2, Concern #3:
> *"3. Preprocessing and reproducibility: Please specify the exact checkpoint versions, image processors, normalization parameters, and feature extraction procedures used for all three pretrained ViT models."*

**Author response:**  
We documented the full technical reproducibility specifications in Sections III-A and III-B, supplemented by the image processor configuration details below:
1. **Checkpoint Versions:** As detailed in Section III-B Paragraph 2 (Page 4), all three models adopt the ViT-Base/16 architecture (12 encoder layers, latent dimension $D = 768$, and 12 attention heads per layer per the standard ViT-Base configuration) derived from `google/vit-base-patch16-224-in21k`: `ViT-Face` (`skutaada/VIT-VGGFace`, version `e85f0c9`, fine-tuned on VGGFace2), `ViT-Emotion` (`dima806/facial_emotions_image_detection`, version `747cf16`, fine-tuned on FER-2013), and `ViT-Age` (`dima806/facial_age_image_detection`, version `ad35933`, fine-tuned on UTKFace + IMDB-WIKI).
2. **Preprocessing & Normalization:** As described in Section III-A Paragraph 2 (Page 4) and Section III-B Paragraph 2 (Page 4), centered DemogPairs facial images are converted to 3-channel RGB, resized to 224 × 224 pixels, and processed via `AutoImageProcessor` with uniform channel normalization $\mu = \sigma = [0.5, 0.5, 0.5]$ without synthetic data augmentation. As an additional technical detail from the processor configuration (`preprocessor_config.json`), the DemogPairs corpus is pre-cropped and requires no external face detector (such as MTCNN), while `AutoImageProcessor` applies bilinear interpolation and intensity rescaling by $1/255$ prior to normalization into $[-1, 1]$.
3. **`[CLS]` Extraction & Fusion:** As formulated in Section III-B Paragraph 3 (Pages 4–5) and **Table 2** (Page 6), all three backbones remain frozen (no gradient updates), and the 12th-layer `[CLS]` token after Layer Normalization [Eq. (7)] is concatenated into a 2,304-dimensional vector [Eq. (8)].

**Author action:**  
We added the exact checkpoint identifiers and commit versions, `AutoImageProcessor` normalization parameters, **Eq. (7)–(8)**, and the seven-scheme ablation summary in Section III-A Paragraph 2 (Page 4), Section III-B Paragraphs 2–3 (Pages 4–5), and **Table 2** (Page 6).

---

### Reviewer #2, Concern #4:
> *"4. Hyperparameter search consistency: The reported totals of 1,086 configurations, 38,010 cross-validation fits, and 28 final refits should be reconciled with the individual search spaces reported in Tables 3–6."*

**Author response:**  
We thank the reviewer for this arithmetic audit. A source-code audit revealed that the initial draft figures (1,086 configurations and 38,010 fits) resulted from listing unexecuted Logistic Regression parameters in **Table 5** ($C=100$, `'newton-cg'`, and `max_iter=2000`), inflating LR to 270 combinations whereas the executed grid contained **96 combinations** ($2 \text{ scalers} \times 3 \text{ PCA} \times 4 \ C \times 2 \text{ solvers} \times 2 \text{ max\_iter}$). Furthermore, in **Table 6** (SVM), out of the 288 Cartesian grid combinations ($2 \text{ scalers} \times 3 \text{ PCA} \times 4 \ C \times 3 \text{ kernels} \times 2 \text{ degrees} \times 2 \ \gamma$), there are **168 effective unique configurations** ($24 \text{ [linear]} + 48 \text{ [rbf]} + 96 \text{ [poly]} = 168$). The complete reconciliation is presented below:

| Classifier & Table | Initial Draft | Actual Revision | Fits/Scheme ($\times 5$ Folds) | Total CV Fits ($\times 7$ Schemes) | Notes |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Random Forest (Table 3)** | 288 | **288** | 1,440 | 10,080 | $2 \times 3 \times 2 \times 3 \times 2 \times 2 \times 2$ |
| **Gaussian Naive Bayes (Table 4)** | 240 | **240** | 1,200 | 8,400 | $2 \text{ scalers} \times 3 \text{ PCA} \times 40 \text{ var\_smoothing}$ |
| **Logistic Regression (Table 5)** | 270 | **96** | **480** | **3,360** | Corrected: removed $C=100$, `'newton-cg'`, `2000` |
| **Support Vector Machine (Table 6)** | 288 | **288** | 1,440 | 10,080 | 288 Cartesian (**168 effective unique**) |
| **Total per Scheme / Global** | **1,086 / 38,010** | **912 / 31,920** | **4,560** | **31,920 CV fits + 28 refits** | Reconciled across all sections |

**Author action:**  
We reconciled the search space specifications in **Table 3–6** (Page 7), the narrative in Section III-F (Pages 6–7, noting 288 Cartesian grid combinations or **168 effective unique configurations** for SVM and 1,440 fits), and Section III-G (Page 7, `912 combinations × 5 folds = 4,560 fits × 7 feature schemes + 28 final refits`, totaling **31,920** cross-validation fits).

---

### Reviewer #2, Concern #5:
> *"5. Statistical interpretation: The SVM accuracy improvement from 93.29% to 93.70% is not statistically significant according to the reported McNemar test (p = 0.3057). Consequently, claims of tri-domain superiority and feature saturation should be appropriately qualified."*

**Author response:**  
We fully agree and have applied paired McNemar's test with Edwards' continuity correction [Eq. (21)], two-sided Exact Binomial testing, and 95% Wilson Score confidence intervals [Eq. (22)] on the subject-disjoint benchmark ($N = 2,160$):
1. **Tri-Domain vs. Single `Face`:** Statistically significant for both SVM (88.61% vs. 86.16%; $+2.45\text{ pp}$, $\chi^2 = 20.96$, McNemar $p < 0.001$, Exact Binomial $p < 0.001$) and LR (88.66% vs. 86.39%; $+2.27\text{ pp}$, $\chi^2 = 19.69$, McNemar $p < 0.001$, Exact Binomial $p < 0.001$).
2. **Feature Saturation Qualification (*Tri-Domain* vs. `Emotion` ⊕ `Face`):** For RBF SVM, adding age features yields a non-significant difference ($88.43\% \to 88.61\%$, $+0.18\text{ pp}$, $\chi^2 = 0.12$, McNemar $p = 0.7341$, Exact Binomial $p = 0.7343$), which is qualified as **asymptotic latent feature saturation**. As an additional verification from our prediction logs, comparing Tri-Domain SVM against `Face` ⊕ `Age` (87.55%, $\chi^2 = 6.82$, Exact Binomial $p = 0.0086 < 0.01$) still confirms the statistical significance of emotion features. Conversely, for linear LR, adding age features on top of `Emotion` ⊕ `Face` yields a statistically significant gain ($87.45\% \to 88.66\%$, $+1.21\text{ pp}$, $\chi^2 = 7.10$, McNemar $p = 0.0077$, Exact Binomial $p = 0.0073 < 0.01$).
3. **Predictive Parity (LR vs. SVM):** Comparing Tri-Domain LR (1,915 correct) against Tri-Domain SVM (1,914 correct) yields $\chi^2 = 0.00$, McNemar $p = 1.0000$, and Exact Binomial $p = 1.0000$ (+1 net image), which is explicitly framed as **predictive parity**.

**Author action:**  
We added **Table 14** (Page 12) reporting verified McNemar $\chi^2$ $p$-values and Exact Binomial $p$-values, and consistently qualified all statistical claims across the Abstract (Page 1), Sections IV-A and IV-B (Pages 8–12), and Section V (Page 14).

---

### Reviewer #2, Concern #6:
> *"6. Fairness analysis: The reported Equal Opportunity Difference values provide useful subgroup information but do not establish comprehensive demographic fairness. Please clarify the scope and limitations of the fairness claims."*

**Author response:**  
We agree that Equal Opportunity Difference (EOD) does not establish comprehensive demographic fairness. We explicitly qualify EOD ($9.72\text{ pp}$ between White Males TPR of 94.44% and Black Females TPR of 84.72%) strictly as an empirical subgroup performance disparity indicator on the DemogPairs test set.

**Author action:**  
We added the formal EOD boundary definition in Section III-H (Page 8, Eq. (23)), reported full subgroup metrics in **Table 15** (Page 12), and included the following qualification statement in Section IV-C (Page 11):

> As a commitment to Artificial Intelligence (AI) ethics and scope delimitation (Responsible AI), this disparity is explicitly not claimed as a guarantee of achieving universal demographic fairness (no overclaim of complete demographic fairness), but rather as an empirical subgroup performance transparency audit.

---

### Reviewer #2, Concern #7:
> *"7. Baseline comparison: Please clarify whether the prior methods in Table 12 used comparable data partitions, preprocessing, and evaluation protocols. Otherwise, the comparison should be presented as contextual rather than a controlled benchmark."*

**Author response:**  
We agree and have clarified the differences in data partitioning, preprocessing, and evaluation protocols between prior literature and our primary benchmark. Accordingly, we explicitly partition the literature comparison table into contextual comparisons (*Stratified*, for prior DemogPairs studies using image-level splits with subject identity overlap and potential cross-study preprocessing variations) and controlled benchmarks (*Subject-Disjoint*, for internal evaluations using uniform preprocessing and identical leakage-free protocols).

**Author action:**  
We updated **Table 16** (Page 13) and the methodological qualification narrative in Section IV-E (Page 13) to clearly separate these two evaluation protocol groups.

---

### Reviewer #2, Concern #8:
> *"8. Computational efficiency: Please report feature extraction time, classifier training time, inference latency, memory consumption, and model storage requirements to substantiate the efficiency claims."*

**Author response:**  
We measured and reported all five computational efficiency dimensions on an Intel Core i9-13900H CPU, 32 GB DDR5 RAM, and NVIDIA RTX 4060 GPU (8 GB VRAM):
1. **ViT Feature Extraction (10,800 images):** 39.74 ms (`Face`), 39.65 ms (`Emotion`), and 45.11 ms (`Age`), totaling **124.50 ms/image** for tri-domain extraction (22.41 minutes total on GPU).
2. **5-Fold CV Training Time:** Tri-Domain LR **3,287.07 seconds (54.78 minutes)** vs. Tri-Domain SVM **30,666.02 seconds (511.10 minutes)** (**9.3× faster**).
3. **Downstream Classifier Inference Latency:** LR **0.0046 ms/sample** vs. SVM **4.6785 ms/sample** (**1,027× (>1,000×) faster**; combining the extraction time in **Table 11** and inference time in **Table 12**, total end-to-end GPU latency is $\approx 124.505\text{ ms}$ for LR vs. $\approx 129.179\text{ ms}$ for SVM).
4. **RAM & Cache Footprint:** The held-out test array ($N = 2,160$, `float32`) consumes **18.98 MB RAM** (tri-domain) and **12.66 MB RAM** (dual-domain); on-disk feature caches occupy 30.8 MB/domain (92.4 MB total).
5. **Model Storage Size:** LR **0.11 MB** vs. SVM **36.60 MB** (**>330× more compact**).

**Author action:**  
We added Section III-I (*Experimental Setup*, Page 8), **Table 11** (Page 10), **Table 12** (Page 12), the efficiency analysis in Section IV-A Paragraph 6 (Pages 9 and 11), and Section V (Page 14), clarifying that the 0.11 MB footprint and 0.0046 ms latency apply specifically to the downstream classification head, while future work in Section V Paragraph 2 (Page 14) notes applying quantization or knowledge distillation to the ViT backbones.

---

### Reviewer #2, Concern #9:
> *"9. Results and discussion: Several interpretations concerning phenotypic overlap, the contribution of age-related features, and reductions in inter-racial errors remain insufficiently supported by confusion matrices alone. These statements should be qualified or supported by additional analyses."*

**Author response:**  
We fully accept this correction and have removed all unsupported speculations regarding craniofacial morphology, epidermal wrinkle textures, and illumination contrasts from the Abstract, Section IV-C, and Section IV-D.

**Author action:**  
We updated the Abstract (Page 1), Section IV-C (Page 11), and Section IV-D (Pages 11 and 13), including adding the following four-sentence qualification paragraph in Section IV-D (Page 13):

> The cross-race visual overlap phenomenon underlying this misclassification pattern is examined objectively based purely on the distribution of image visual variations, without introducing untested biological causal assumptions. Empirical evaluation shows that the confusion matrices reflect the observational data distribution characteristics within the evaluated corpus. The addition of biological aging representations provides a measurable contribution in suppressing intra-gender cross-race confusion from 185 to 165 cases, consistent with the statistical significance of McNemar's test (p = 0.0073). This qualification affirms that the superiority of multi-domain fusion originates from complementary latent feature covariate enrichment, thereby resolving visual ambiguities in the representation space without relying on phenotypic speculations or lighting conditions.

---

### Reviewer #2, Concern #10:
> *"10. Conclusion and limitations: The conclusions should be restricted to the evaluated DemogPairs benchmark unless additional cross-identity or external-dataset validation is provided."*

**Author response:**  
We fully agree. The scope of our claims and conclusions is explicitly restricted to the six intersectional classes across three macro-racial groups (**Asian, Black, White**) within the subject-disjoint DemogPairs benchmark.

**Author action:**  
We bounded the scope of claims in the Abstract (Page 1) and added an explicit statement of research limitations in Paragraph 2 of Section V (*Conclusion*, Page 14) as follows:

> Despite offering significant empirical contributions, this study has two primary limitations that warrant attention. First, the demographic scope of this investigation is limited to three macro-racial groups within the DemogPairs dataset (Asian, Black, White); thus, generalizing classification performance to multiracial groups and other ethnic populations still requires additional empirical testing. Second, the multi-domain representation extraction process is still conducted separately (offline) utilizing three frozen ViT-Base backbone models without unified end-to-end fine-tuning, thereby requiring a dedicated feature processing stage prior to downstream classification.

---

*\*Note: References suggested by reviewers should only be added if it is relevant to the article and makes it more complete. Excessive cases of recommending non-relevant articles should be reported to ieeeaccesseic@ieee.org\**
