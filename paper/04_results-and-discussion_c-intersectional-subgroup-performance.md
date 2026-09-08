## C. Intersectional Subgroup Performance

<a id="tab11"></a>
**Table XI. Subgroup-Level Performance for Tri-Domain Models.**

| Classifier | Subgroup | Recall | Precision | F1-Score | OvR Accuracy |
|---|---|---|:---:|:---:|:---:|
| **SVM (Tri)** | `White_Males` | 96.94% | 95.36% | 96.14% | 98.70% |
| | `Black_Males` | 94.17% | 95.49% | 94.83% | 98.29% |
| | `White_Females` | 94.72% | 92.41% | 93.55% | 97.82% |
| | `Asian_Males` | 94.44% | 92.39% | 93.41% | 97.78% |
| | `Asian_Females` | 92.50% | 92.50% | 92.50% | 97.50% |
| | `Black_Females` | 89.44% | 94.15% | 91.74% | 97.31% |
| **LR (Tri)** | `White_Males` | 96.11% | 95.05% | 95.58% | 98.52% |
| | `Black_Males` | 93.06% | 95.71% | 94.37% | 98.15% |
| | `White_Females` | 92.22% | 91.21% | 91.71% | 97.22% |
| | `Asian_Males` | 92.78% | 90.76% | 91.76% | 97.22% |
| | `Asian_Females` | 91.11% | 91.62% | 91.36% | 97.13% |
| | `Black_Females` | 91.11% | 92.13% | 91.62% | 97.22% |

Profil kinerja klasifikasi granular pada model terbaik SVM berbasis fusi tri-domain Face ⊕ Emotion ⊕ Age dievaluasi secara mendalam berdasarkan metrik OvR sebagaimana disajikan pada [Table XI](#tab11). Seluruh subkelompok demografis berhasil mencapai F1-Score melampaui 91.00%, dengan rentang capaian bergerak dari 91.74% pada Black_Females hingga 96.14% pada White_Males, sehingga menghasilkan selisih disparitas rentang sebesar 4.40%. Sementara itu, nilai Akurasi OvR berada pada rentang 97.31% hingga 98.70% dengan disparitas sebesar 1.39 pp. Perlu dicatat secara metodologis bahwa tingginya nilai Akurasi OvR tersebut turut dipengaruhi oleh rasio dominansi sampel negatif sebesar 5:1 pada evaluasi biner OvR, sehingga metrik ini tidak diposisikan sebagai indikator tunggal disparitas kinerja.

Perbandingan profil kinerja subkelompok antara model SVM dan pengklasifikasi linier LR pada konfigurasi tri-domain disajikan pada [Table XI](#tab11). Model LR tri-domain turut memperlihatkan konsistensi performa yang tinggi dengan capaian F1-Score melampaui 91.00% pada seluruh kelas demografis, yang merentang dari 91.36% pada Asian_Females hingga 95.58% pada White_Males dengan selisih disparitas rentang sebesar 4.22%. Subkelompok White_Males secara konsisten mencatatkan performa klasifikasi tertinggi pada kedua pengklasifikasi tersebut. Temuan empiris ini membuktikan bahwa fusi representasi tri-domain menghasilkan representasi visual yang tangguh dan terdistribusi stabil melintasi seluruh subkelompok demografis, baik pada model linier maupun model non-linier. Meskipun demikian, evaluasi subkelompok ini mencerminkan kinerja granular per kelas dan bukan audit keadilan algoritmik komprehensif.
