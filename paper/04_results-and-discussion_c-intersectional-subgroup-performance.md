## C. Intersectional Subgroup Performance

<a id="tab11"></a>
**Table XI. Subgroup-Level Performance for Tri-Domain Models.**

| Classifier | Subgroup | Recall (TPR) | Precision | F1-Score | OvR Accuracy | FNR |
|---|---|:---:|:---:|:---:|:---:|:---:|
| **SVM (Tri)** | `White_Males` | 96.94% | 95.36% | 96.14% | 98.70% | 3.06% |
| | `Black_Males` | 94.17% | 95.49% | 94.83% | 98.29% | 5.83% |
| | `White_Females` | 94.72% | 92.41% | 93.55% | 97.82% | 5.28% |
| | `Asian_Males` | 94.44% | 92.39% | 93.41% | 97.78% | 5.56% |
| | `Asian_Females` | 92.50% | 92.50% | 92.50% | 97.50% | 7.50% |
| | `Black_Females` | 89.44% | 94.15% | 91.74% | 97.31% | 10.56% |
| **LR (Tri)** | `White_Males` | 96.11% | 95.05% | 95.58% | 98.52% | 3.89% |
| | `Black_Males` | 93.06% | 95.71% | 94.37% | 98.15% | 6.94% |
| | `Asian_Males` | 92.78% | 90.76% | 91.76% | 97.22% | 7.22% |
| | `White_Females` | 92.22% | 91.21% | 91.71% | 97.22% | 7.78% |
| | `Black_Females` | 91.11% | 92.13% | 91.62% | 97.22% | 8.89% |
| | `Asian_Females` | 91.11% | 91.62% | 91.36% | 97.13% | 8.89% |

Profil kinerja klasifikasi granular pada model terbaik SVM tri-domain Face ⊕ Emotion ⊕ Age dievaluasi berdasarkan metrik pada [Table XI](#tab11). Seluruh subkelompok mencapai F1-Score melampaui 91.00%, dari 91.74% pada Black Females hingga 96.14% pada White Males. Namun demikian, analisis keadilan formal mencatat kesenjangan Equal Opportunity Difference (Delta TPR = 7.50%) akibat disparitas recall antara White Males (96.94%) dan Black Females (89.44% dengan FNR 10.56%). Meskipun presisi Black Females tetap tinggi sebesar 94.15%, sensitivitas deteksi yang lebih rendah merefleksikan tantangan representasi fenotipik interseksional yang belum terhapus sepenuhnya. Pelaporan metrik False Negative Rate ini menyeimbangkan evaluasi Akurasi OvR (97.31% hingga 98.70%) yang rentan terdistorsi oleh dominansi rasio sampel negatif 5:1.

Perbandingan profil kinerja subkelompok antara model SVM dan pengklasifikasi linier LR pada konfigurasi tri-domain disajikan pada [Table XI](#tab11). Model LR tri-domain memperlihatkan konsistensi performa tinggi dengan F1-Score melampaui 91.00% pada seluruh kelas demografis, merentang dari 91.36% pada Asian Females hingga 95.58% pada White Males. Evaluasi keadilan formal pada model LR menunjukkan kesenjangan Equal Opportunity Difference yang lebih rapat (Delta TPR = 5.00%), dengan recall White Males sebesar 96.11% berbanding 91.11% pada Asian Females dan Black Females (FNR 8.89%). Subkelompok White Males secara konsisten mencatatkan performa klasifikasi tertinggi pada kedua pengklasifikasi. Temuan empiris ini membuktikan bahwa fusi representasi tri-domain menghasilkan representasi visual yang stabil melintasi seluruh subkelompok demografis pada model linier maupun non-linier.
