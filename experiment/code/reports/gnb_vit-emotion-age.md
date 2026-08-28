# GNB - vit-emotion-age

## Konfigurasi
- **Fitur:** vit-emotion-age (1536 dimensi)
- **Tipe:** Dual
- **Classifier:** GNB
- **Parameter Terbaik:** var_smoothing=0.001603718743751331
- **Scaler:** MinMaxScaler
- **PCA:** PCA

## Hasil Global
| Metric | Value |
|---|:---:|
| Accuracy | 0.7681 |
| Precision | 0.7686 |
| Recall | 0.7681 |
| F1-Score | 0.7681 |

## Per-Kelas
| Class | Precision | Recall | F1-Score |
|---|:---:|:---:|:---:|
| Black_Males | 0.8092 | 0.7778 | 0.7932 |
| White_Females | 0.7874 | 0.7611 | 0.7740 |
| Asian_Males | 0.7253 | 0.7333 | 0.7293 |
| White_Males | 0.7591 | 0.8139 | 0.7855 |
| Black_Females | 0.7762 | 0.7806 | 0.7784 |
| Asian_Females | 0.7542 | 0.7417 | 0.7479 |
| **Macro Avg** | **0.7686** | **0.7681** | **0.7681** |

## Confusion Matrix
![CM](images/cm_gnb_vit-emotion-age_GaussianNB.png)
