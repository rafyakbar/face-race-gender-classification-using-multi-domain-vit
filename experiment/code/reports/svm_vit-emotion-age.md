# SVM - vit-emotion-age

## Konfigurasi
- **Fitur:** vit-emotion-age (1536 dimensi)
- **Tipe:** Dual
- **Classifier:** SVM
- **Parameter Terbaik:** C=10, kernel=rbf, degree=2, gamma=scale
- **Scaler:** None
- **PCA:** None

## Hasil Global
| Metric | Value |
|---|:---:|
| Accuracy | 0.9208 |
| Precision | 0.9210 |
| Recall | 0.9208 |
| F1-Score | 0.9209 |

## Per-Kelas
| Class | Precision | Recall | F1-Score |
|---|:---:|:---:|:---:|
| Black_Males | 0.9552 | 0.9472 | 0.9512 |
| White_Females | 0.9101 | 0.9278 | 0.9188 |
| Asian_Males | 0.9014 | 0.9139 | 0.9076 |
| White_Males | 0.9524 | 0.9444 | 0.9484 |
| Black_Females | 0.9086 | 0.8833 | 0.8958 |
| Asian_Females | 0.8984 | 0.9083 | 0.9033 |
| **Macro Avg** | **0.9210** | **0.9208** | **0.9209** |

## Confusion Matrix
![CM](images/cm_svm_vit-emotion-age_SVC.png)
