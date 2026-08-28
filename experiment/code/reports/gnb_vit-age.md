# GNB - vit-age

## Konfigurasi
- **Fitur:** vit-age (768 dimensi)
- **Tipe:** Single
- **Classifier:** GNB
- **Parameter Terbaik:** var_smoothing=0.000437547937507418
- **Scaler:** MinMaxScaler
- **PCA:** PCA

## Hasil Global
| Metric | Value |
|---|:---:|
| Accuracy | 0.6963 |
| Precision | 0.6979 |
| Recall | 0.6963 |
| F1-Score | 0.6952 |

## Per-Kelas
| Class | Precision | Recall | F1-Score |
|---|:---:|:---:|:---:|
| Black_Males | 0.6512 | 0.7000 | 0.6747 |
| White_Females | 0.6941 | 0.7500 | 0.7210 |
| Asian_Males | 0.6921 | 0.6056 | 0.6459 |
| White_Males | 0.6983 | 0.7778 | 0.7359 |
| Black_Females | 0.7418 | 0.6306 | 0.6817 |
| Asian_Females | 0.7099 | 0.7139 | 0.7119 |
| **Macro Avg** | **0.6979** | **0.6963** | **0.6952** |

## Confusion Matrix
![CM](images/cm_gnb_vit-age_GaussianNB.png)
