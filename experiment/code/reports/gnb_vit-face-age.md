# GNB - vit-face-age

## Konfigurasi
- **Fitur:** vit-face-age (1536 dimensi)
- **Tipe:** Dual
- **Classifier:** GNB
- **Parameter Terbaik:** var_smoothing=0.011253355826007646
- **Scaler:** MinMaxScaler
- **PCA:** PCA

## Hasil Global
| Metric | Value |
|---|:---:|
| Accuracy | 0.8315 |
| Precision | 0.8343 |
| Recall | 0.8315 |
| F1-Score | 0.8317 |

## Per-Kelas
| Class | Precision | Recall | F1-Score |
|---|:---:|:---:|:---:|
| Black_Males | 0.8177 | 0.8972 | 0.8556 |
| White_Females | 0.9112 | 0.8556 | 0.8825 |
| Asian_Males | 0.7855 | 0.7833 | 0.7844 |
| White_Males | 0.8966 | 0.8667 | 0.8814 |
| Black_Females | 0.8385 | 0.7500 | 0.7918 |
| Asian_Females | 0.7563 | 0.8361 | 0.7942 |
| **Macro Avg** | **0.8343** | **0.8315** | **0.8317** |

## Confusion Matrix
![CM](images/cm_gnb_vit-face-age_GaussianNB.png)
