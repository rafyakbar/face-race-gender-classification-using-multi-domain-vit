## C. Intersectional Subgroup Performance

Profil performa klasifikasi granular OvR pada model tri-domain terbaik (LR dan SVM) dievaluasi melintasi enam subkelompok demografis ($N = 360$ citra uji per subkelompok) sebagaimana disajikan pada [Table XV](#tab15). Pada kedua model, subkelompok White Males mencatat performa tertinggi dengan Recall 94.44% (F1-Score 94.84% pada LR; F1-Score 94.18% pada SVM) dan False Negative Rate (FNR) terendah sebesar 5.56%. Sebaliknya, subkelompok Black Females mencatat Recall 84.72% (F1-Score 84.96% pada LR; F1-Score 86.16% pada SVM) dengan FNR sebesar 15.28%. Subkelompok Asian Females meraih Recall 86.67% pada LR dan 86.11% pada SVM. Seluruh kohort subkelompok mempertahankan F1-Score di atas 84.90%, mengonfirmasi keandalan fusi fitur tri-domain dalam memisahkan batas demografis interseksional.

<a id="tab15"></a>
**Table XV. Intersectional Subgroup Performance and Algorithmic Fairness Profile.**

| Classifier | Subgroup | Recall (TPR) | Precision | F1-Score | OvR Accuracy | FNR |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **Logistic Regression (Tri-Domain)** | `White_Males` | 94.44% | 95.24% | 94.84% | 98.29% | 5.56% |
| | `White_Females` | 90.56% | 91.32% | 90.93% | 96.99% | 9.44% |
| | `Black_Males` | 87.78% | 91.59% | 89.65% | 96.62% | 12.22% |
| | `Asian_Males` | 87.78% | 82.72% | 85.18% | 94.91% | 12.22% |
| | `Asian_Females` | 86.67% | 86.43% | 86.55% | 95.51% | 13.33% |
| | `Black_Females` | 84.72% | 85.20% | 84.96% | 95.00% | 15.28% |
| **Support Vector Machine (Tri-Domain)** | `White_Males` | 94.44% | 93.92% | 94.18% | 98.06% | 5.56% |
| | `White_Females` | 91.11% | 90.11% | 90.61% | 96.85% | 8.89% |
| | `Asian_Males` | 88.06% | 82.34% | 85.10% | 94.86% | 11.94% |
| | `Black_Males` | 87.22% | 92.35% | 89.71% | 96.67% | 12.78% |
| | `Asian_Females` | 86.11% | 85.87% | 85.99% | 95.32% | 13.89% |
| | `Black_Females` | 84.72% | 87.64% | 86.16% | 95.46% | 15.28% |

Evaluasi disparitas keadilan algoritmik antarsubkelompok dikuantifikasi melalui metrik EOD berdasarkan selisih TPR maksimum dan minimum ($\text{EOD} = \Delta \text{TPR} = \max \text{TPR} - \min \text{TPR} = 94.44\% - 84.72\% = \mathbf{9.72\text{ pp}}$), yang bernilai identik pada model LR dan SVM. Kesenjangan ini merefleksikan variasi distribusi frekuensi kesalahan empiris antarsubkelompok pada data uji held-out ($N = 2.160$), di mana Black Females mencatat FNR tertinggi (15.28%) dan White Males terendah (5.56%). Sebagai komitmen etika Artificial Intelligence (AI) dan delimitasi ruang lingkup (Responsible AI), disparitas ini secara tegas tidak diklaim sebagai jaminan tercapainya keadilan demografis universal (no overclaim of complete demographic fairness), melainkan sebagai audit transparansi performa subkelompok empiris.
