# IEEE Access - Decision on Manuscript ID Access-2026-50857

---

## Metadata Email

- **Subjek:** IEEE Access - Decision on Manuscript ID Access-2026-50857
- **Tanggal:** 20 Oktober 2026 pukul 23.14
- **Pengirim:** IEEE Access `<onbehalfof@manuscriptcentral.com>`
- **Balas Ke:** <vincenzo.conti@unikore.it>
- **Kepada:** <rickyeka@unesa.ac.id>, <24051905008@mhs.unesa.ac.id>, <yuniyamasari@unesa.ac.id>, <24051905007@mhs.unesa.ac.id>, <shukorsanim@uitm.edu.my>
- **Cc:** <vincenzo.conti@unikore.it>, <vinc.conti@gmail.com>

---

## Isi Keputusan Editorial

20-10-2026

Dear Dr. PUTRA:

I am writing to you regarding manuscript # Access-2026-50857 entitled "Multi-Domain Vision Transformer Fusion for Intersectional Demographic Classification from Facial Images" which you submitted to IEEE *Access*.

Your article was peer reviewed with interest but has not been recommended for publication in its current form. We strongly encourage you to address the reviewers’ concerns, which can be found at the bottom of this letter, and resubmit your article to IEEE *Access* once you have updated it accordingly.

Please note that IEEE *Access* has a binary peer review process. Therefore, to uphold quality to IEEE standards, an article is rejected even if it requires minor edits.

When updating your manuscript, you should elaborate on your points and clarify with references, examples, data, etc. If you disagree with any technical points the reviewers have made, please include your counterarguments in your response to the reviewers (more information detailed below) and work this into the updated manuscript.

Also, note that if a reviewer suggested references, you should only add those that are relevant to your work if you feel they strengthen your article. Recommending references to specific publications is not appropriate for reviewers and you should report excessive cases to [ieeeaccessEIC@ieee.org](mailto:ieeeaccessEIC@ieee.org). Authors are not obligated to cite articles that are recommended by the reviewers, and the final decision on the article will not be influenced by whether or not authors cite these suggested references.

IEEE *Access* allows one opportunity to resubmit. If the updated manuscript is determined not to have addressed all of the previous reviewers’ concerns, or if the Associate Editor still has substantial technical concerns, the article will be rejected and no further resubmissions will be allowed.

**When you are ready to resubmit your updated article, you can do so in the [IEEE Author Portal](https://ieee.atyponrex.com/journal/ieee-access). When you log into the IEEE Author Portal you will see the title of the rejected article and the option to ‘Start Resubmission’.**

Tautan Pengajuan: [https://ieee.atyponrex.com/submission/submissionBoard/REX-PROD-2-E9361D66-0B0C-43F4-BE88-698DEEEF7BBB-49863DA0-9FE4-4717-A447-42173D59A943-26563/current?idtype=external](https://ieee.atyponrex.com/submission/submissionBoard/REX-PROD-2-E9361D66-0B0C-43F4-BE88-698DEEEF7BBB-49863DA0-9FE4-4717-A447-42173D59A943-26563/current?idtype=external)

Upon resubmission you will be asked to upload the following 3 files:

1. A document containing your response to reviewers from the previous peer review. The ‘response to reviewers’ document (template attached) should have the following regarding each comment: a) Reviewer’s concern, b) your response to the concern, c) your action to remedy the concern. **The document should be uploaded with your manuscript files under "*Author's Response Files*."**
2. Your updated manuscript with all your individual changes highlighted, including grammatical changes (e.g. preferably with the yellow highlight tool within the pdf file). This file should be uploaded with your manuscript files as *‘Highlighted PDF.’*
3. A clean copy of the final manuscript (without highlighted changes) submitted as a Word or LaTeX file, and as a PDF, both submitted as the *‘Main Manuscript.’*

**\*\*IMPORTANT:** Please see the attached Resubmission Checklist that details all the items listed above. Please utilize this checklist to ensure you have made the necessary edits to your manuscript, and to ensure you have all the necessary files prepared prior to resubmission.

**\*\*\* AUTHOR LIST CHANGES:** If your revised manuscript has an updated author list, you will need to submit a formal request to the Editor by completing the attachment labelled ‘Request for Byline Change,’ and uploading it as *'Request for byline change form.'* This should include a DETAILED justification explaining each author’s contribution(s) to the work. You will also need to provide the justification for the author change during the submission process. Change in the author list is considered rare and exceptional, and the decision to allow such changes rests with the Editor. Once the list and order of authors has been established, the list and order of authors should not be altered without permission of all living authors of that article.

We sincerely hope you will update your manuscript and resubmit soon. Please contact me if you have any questions.

Thank you for your interest in IEEE *Access*.

Sincerely,

Dr. Vincenzo Conti  
Associate Editor, IEEE *Access*  
<vincenzo.conti@unikore.it>, <vinc.conti@gmail.com>

---

## Reviewers' Comments to Author

### Reviewer: 1

#### Comments
Dear authors, thanks for your valuable work, this manuscript can be acceptable for publication after reviewing it according to the following comments:

1. the introduction is too long need to be summarized.
2. The related works needs to be modified in better way and add equations.
3. The figure 3 needs to be redesigned and explained in better way to show the novelty of the proposed method and also not clear.
4. Graph in figure 4 needs to be discussed in better way.
5. Experimental works need to mention the dataset used in more detail and show the contribution of your proposed method and also to consider the time cost in the evaluation.
6. the authors need to compare their proposed method with more methods to validate their contribution.
7. conclusion part does not show the contribution in good way.

#### Additional Questions
- **Please confirm that you have reviewed all relevant files, including supplementary files and any author response files, which can be found in the "View Author's Response" link above (author responses will only appear for resubmissions):**  
  Yes, all files have been reviewed
- **1) Does the paper contribute to the body of knowledge?:**  
  Yes
- **2) Is the paper technically sound?:**  
  Yes
- **3) Is the subject matter presented in a comprehensive manner?:**  
  Yes
- **4) Are the references provided applicable and sufficient?:**  
  Yes
- **5) Are there references that are not appropriate for the topic being discussed?:**  
  No
- **5a) If yes, then please indicate which references should be removed.:**  
  *(None)*

---

### Reviewer: 2

#### Comments
1. **Novelty and contribution:** The methodological novelty beyond concatenating three pretrained feature representations and applying conventional classifiers should be more clearly established relative to existing dual-domain and multidomain approaches.
2. **Data leakage and generalization:** The image-level stratified split may allow images of the same identity to occur in both training and test sets. Please clarify whether identity overlap exists and provide subject-disjoint evaluation to establish genuine generalization.
3. **Preprocessing and reproducibility:** Please specify the exact checkpoint versions, image processors, normalization parameters, and feature extraction procedures used for all three pretrained ViT models.
4. **Hyperparameter search consistency:** The reported totals of 1,086 configurations, 38,010 cross-validation fits, and 28 final refits should be reconciled with the individual search spaces reported in Tables 3–6.
5. **Statistical interpretation:** The SVM accuracy improvement from 93.29% to 93.70% is not statistically significant according to the reported McNemar test (p = 0.3057). Consequently, claims of tri-domain superiority and feature saturation should be appropriately qualified.
6. **Fairness analysis:** The reported Equal Opportunity Difference values provide useful subgroup information but do not establish comprehensive demographic fairness. Please clarify the scope and limitations of the fairness claims.
7. **Baseline comparison:** Please clarify whether the prior methods in Table 12 used comparable data partitions, preprocessing, and evaluation protocols. Otherwise, the comparison should be presented as contextual rather than a controlled benchmark.
8. **Computational efficiency:** Please report feature extraction time, classifier training time, inference latency, memory consumption, and model storage requirements to substantiate the efficiency claims.
9. **Results and discussion:** Several interpretations concerning phenotypic overlap, the contribution of age-related features, and reductions in inter-racial errors remain insufficiently supported by confusion matrices alone. These statements should be qualified or supported by additional analyses.
10. **Conclusion and limitations:** The conclusions should be restricted to the evaluated DemogPairs benchmark unless additional cross-identity or external-dataset validation is provided.

#### Additional Questions
- **Please confirm that you have reviewed all relevant files, including supplementary files and any author response files, which can be found in the "View Author's Response" link above (author responses will only appear for resubmissions):**  
  Yes, all files have been reviewed
- **1) Does the paper contribute to the body of knowledge?:**  
  Yes
- **2) Is the paper technically sound?:**  
  Yes
- **3) Is the subject matter presented in a comprehensive manner?:**  
  Yes
- **4) Are the references provided applicable and sufficient?:**  
  Yes
- **5) Are there references that are not appropriate for the topic being discussed?:**  
  No
- **5a) If yes, then please indicate which references should be removed.:**  
  *(None)*

---

## Kontak Administrator

If you have any questions, please contact article administrator:  
Mr. Adesh Choudhary (<adesh.choudhary@ieee.org>)

---

## Lampiran (Attachments)

1. `* IEEE-Access-Response-to-Reviewers-template-6.26.23.docx` (18K)
2. `* Request-for-Byline-Change--2-.docx` (16K)
3. `* Resubmission-Checklist-6.26.23.docx` (130K)
