# SVM - vit-face

## Konfigurasi
- **Fitur:** vit-face (768 dimensi)
- **Tipe:** Single
- **Classifier:** SVM
- **Parameter Terbaik:** C=10, kernel=rbf, degree=2, gamma=scale
- **Scaler:** None
- **PCA:** None

## Hasil Global
| Metric | Value |
|---|:---:|
| Accuracy | 0.9083 |
| Precision | 0.9084 |
| Recall | 0.9083 |
| F1-Score | 0.9083 |

## Per-Kelas
| Class | Precision | Recall | F1-Score |
|---|:---:|:---:|:---:|
| Black_Males | 0.9407 | 0.9250 | 0.9328 |
| White_Females | 0.8978 | 0.9028 | 0.9003 |
| Asian_Males | 0.8919 | 0.9167 | 0.9041 |
| White_Males | 0.9290 | 0.9444 | 0.9366 |
| Black_Females | 0.8964 | 0.8889 | 0.8926 |
| Asian_Females | 0.8946 | 0.8722 | 0.8833 |
| **Macro Avg** | **0.9084** | **0.9083** | **0.9083** |

## Confusion Matrix
![CM](images/cm_svm_vit-face_SVC.png)
