# SVM - vit-emotion-face

## Konfigurasi
- **Fitur:** vit-emotion-face (1536 dimensi)
- **Tipe:** Dual
- **Classifier:** SVM
- **Parameter Terbaik:** C=10, kernel=rbf, degree=2, gamma=scale
- **Scaler:** MinMaxScaler
- **PCA:** None

## Hasil Global
| Metric | Value |
|---|:---:|
| Accuracy | 0.9329 |
| Precision | 0.9333 |
| Recall | 0.9329 |
| F1-Score | 0.9329 |

## Per-Kelas
| Class | Precision | Recall | F1-Score |
|---|:---:|:---:|:---:|
| Black_Males | 0.9768 | 0.9361 | 0.9560 |
| White_Females | 0.9227 | 0.9278 | 0.9252 |
| Asian_Males | 0.9111 | 0.9389 | 0.9248 |
| White_Males | 0.9508 | 0.9667 | 0.9587 |
| Black_Females | 0.9348 | 0.9167 | 0.9257 |
| Asian_Females | 0.9036 | 0.9111 | 0.9073 |
| **Macro Avg** | **0.9333** | **0.9329** | **0.9329** |

## Confusion Matrix
![CM](images/cm_svm_vit-emotion-face_SVC.png)
