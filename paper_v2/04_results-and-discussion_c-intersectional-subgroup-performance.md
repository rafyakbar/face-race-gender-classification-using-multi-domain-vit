## C. Intersectional Subgroup Performance

Profil performa klasifikasi granular One-vs-Rest (OvR) pada model tri-domain terbaik (Logistic Regression dan Support Vector Machine) dievaluasi melintasi enam subkelompok demografis ($N = 360$ citra uji per subkelompok) sebagaimana disajikan pada [Table XV](#tab15). Pada kedua model, subkelompok White Males mencatat performa tertinggi dengan Recall 94.44% (F1 94.84% pada LR; F1 94.18% pada SVM) dan False Negative Rate (FNR) terendah sebesar 5.56%. Sebaliknya, subkelompok Black Females mencatat Recall 84.72% (F1 84.96% pada LR; F1 86.16% pada SVM) dengan FNR sebesar 15.28%. Subkelompok Asian Females meraih Recall 86.67% pada LR dan 86.11% pada SVM. Seluruh kohort subkelompok mempertahankan F1-Score di atas 84.90%, mengonfirmasi keandalan fusi fitur tri-domain dalam memisahkan batas demografis interseksional.

<a id="tab15"></a>
**Table XV. Intersectional Subgroup Performance and Algorithmic Fairness Profile ($N = 2,160$).**

| Classifier | Subgroup | Support | Precision | Recall (TPR) | F1-Score | FNR |
|---|---|:---:|:---:|:---:|:---:|:---:|
| **Logistic Regression (Tri)** | `White_Males` | 360 | 95.24% | 94.44% | 94.84% | 5.56% |
| | `White_Females` | 360 | 91.32% | 90.56% | 90.93% | 9.44% |
| | `Black_Males` | 360 | 91.59% | 87.78% | 89.65% | 12.22% |
| | `Asian_Males` | 360 | 82.72% | 87.78% | 85.18% | 12.22% |
| | `Asian_Females` | 360 | 86.43% | 86.67% | 86.55% | 13.33% |
| | `Black_Females` | 360 | 85.20% | 84.72% | 84.96% | 15.28% |
| **Support Vector Machine (Tri)** | `White_Males` | 360 | 93.92% | 94.44% | 94.18% | 5.56% |
| | `White_Females` | 360 | 90.11% | 91.11% | 90.61% | 8.89% |
| | `Asian_Males` | 360 | 82.34% | 88.06% | 85.10% | 11.94% |
| | `Black_Males` | 360 | 92.35% | 87.22% | 89.71% | 12.78% |
| | `Asian_Females` | 360 | 85.87% | 86.11% | 85.99% | 13.89% |
| | `Black_Females` | 360 | 87.64% | 84.72% | 86.16% | 15.28% |

Evaluasi disparitas keadilan algoritmik antarsubkelompok dikuantifikasi melalui metrik Equal Opportunity Difference (EOD) berdasarkan selisih True Positive Rate maksimum dan minimum ($\text{EOD} = \Delta \text{TPR} = \max \text{TPR} - \min \text{TPR} = 94.44\% - 84.72\% = \mathbf{9.72\text{ pp}}$), yang bernilai identik pada model LR dan SVM. Kesenjangan ini merefleksikan variasi distribusi frekuensi kesalahan empiris antarsubkelompok pada data uji held-out ($N = 2.160$), di mana Black Females mencatat FNR tertinggi (15.28%) dan White Males terendah (5.56%). Sebagai komitmen etika kecerdasan buatan dan delimitasi ruang lingkup (Responsible AI), disparitas ini secara tegas tidak diklaim sebagai jaminan tercapainya keadilan demografis universal (no overclaim of complete demographic fairness), melainkan sebagai audit transparansi performa subkelompok empiris.
