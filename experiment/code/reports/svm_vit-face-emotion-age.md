# SVM - vit-face-emotion-age

## Konfigurasi
- **Fitur:** vit-face-emotion-age (2304 dimensi)
- **Tipe:** Tri-Domain
- **Classifier:** SVM
- **Parameter Terbaik:** C=10, kernel=poly, degree=2, gamma=scale
- **Scaler:** None
- **PCA:** None

## Hasil Global
| Metric | Value |
|---|:---:|
| Accuracy | 0.9370 |
| Precision | 0.9372 |
| Recall | 0.9370 |
| F1-Score | 0.9369 |

## Per-Kelas
| Class | Precision | Recall | F1-Score |
|---|:---:|:---:|:---:|
| Black_Males | 0.9549 | 0.9417 | 0.9483 |
| White_Females | 0.9241 | 0.9472 | 0.9355 |
| Asian_Males | 0.9239 | 0.9444 | 0.9341 |
| White_Males | 0.9536 | 0.9694 | 0.9614 |
| Black_Females | 0.9415 | 0.8944 | 0.9174 |
| Asian_Females | 0.9250 | 0.9250 | 0.9250 |
| **Macro Avg** | **0.9372** | **0.9370** | **0.9369** |

## Confusion Matrix
![CM](images/cm_svm_vit-face-emotion-age_SVC.png)
