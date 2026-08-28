# SVM - vit-age

## Konfigurasi
- **Fitur:** vit-age (768 dimensi)
- **Tipe:** Single
- **Classifier:** SVM
- **Parameter Terbaik:** C=10, kernel=rbf, degree=2, gamma=scale
- **Scaler:** None
- **PCA:** None

## Hasil Global
| Metric | Value |
|---|:---:|
| Accuracy | 0.8764 |
| Precision | 0.8767 |
| Recall | 0.8764 |
| F1-Score | 0.8765 |

## Per-Kelas
| Class | Precision | Recall | F1-Score |
|---|:---:|:---:|:---:|
| Black_Males | 0.8886 | 0.9083 | 0.8984 |
| White_Females | 0.8883 | 0.8611 | 0.8745 |
| Asian_Males | 0.8650 | 0.8722 | 0.8686 |
| White_Males | 0.9266 | 0.9111 | 0.9188 |
| Black_Females | 0.8247 | 0.8361 | 0.8303 |
| Asian_Females | 0.8670 | 0.8694 | 0.8682 |
| **Macro Avg** | **0.8767** | **0.8764** | **0.8765** |

## Confusion Matrix
![CM](images/cm_svm_vit-age_SVC.png)
