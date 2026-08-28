# SVM - vit-face-age

## Konfigurasi
- **Fitur:** vit-face-age (1536 dimensi)
- **Tipe:** Dual
- **Classifier:** SVM
- **Parameter Terbaik:** C=10, kernel=poly, degree=2, gamma=scale
- **Scaler:** None
- **PCA:** None

## Hasil Global
| Metric | Value |
|---|:---:|
| Accuracy | 0.9255 |
| Precision | 0.9254 |
| Recall | 0.9255 |
| F1-Score | 0.9254 |

## Per-Kelas
| Class | Precision | Recall | F1-Score |
|---|:---:|:---:|:---:|
| Black_Males | 0.9389 | 0.9389 | 0.9389 |
| White_Females | 0.9190 | 0.9139 | 0.9164 |
| Asian_Males | 0.9258 | 0.9361 | 0.9309 |
| White_Males | 0.9449 | 0.9528 | 0.9488 |
| Black_Females | 0.9148 | 0.8944 | 0.9045 |
| Asian_Females | 0.9091 | 0.9167 | 0.9129 |
| **Macro Avg** | **0.9254** | **0.9255** | **0.9254** |

## Confusion Matrix
![CM](images/cm_svm_vit-face-age_SVC.png)
