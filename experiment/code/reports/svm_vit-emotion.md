# SVM - vit-emotion

## Konfigurasi
- **Fitur:** vit-emotion (768 dimensi)
- **Tipe:** Single
- **Classifier:** SVM
- **Parameter Terbaik:** C=10, kernel=rbf, degree=2, gamma=scale
- **Scaler:** None
- **PCA:** None

## Hasil Global
| Metric | Value |
|---|:---:|
| Accuracy | 0.9019 |
| Precision | 0.9020 |
| Recall | 0.9019 |
| F1-Score | 0.9017 |

## Per-Kelas
| Class | Precision | Recall | F1-Score |
|---|:---:|:---:|:---:|
| Black_Males | 0.9290 | 0.9444 | 0.9366 |
| White_Females | 0.8952 | 0.9250 | 0.9098 |
| Asian_Males | 0.8733 | 0.9000 | 0.8865 |
| White_Males | 0.9244 | 0.9167 | 0.9205 |
| Black_Females | 0.9094 | 0.8639 | 0.8860 |
| Asian_Females | 0.8807 | 0.8611 | 0.8708 |
| **Macro Avg** | **0.9020** | **0.9019** | **0.9017** |

## Confusion Matrix
![CM](images/cm_svm_vit-emotion_SVC.png)
