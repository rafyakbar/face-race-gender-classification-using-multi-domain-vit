# GNB - vit-emotion-face

## Konfigurasi
- **Fitur:** vit-emotion-face (1536 dimensi)
- **Tipe:** Dual
- **Classifier:** GNB
- **Parameter Terbaik:** var_smoothing=0.0058780160722749115
- **Scaler:** MinMaxScaler
- **PCA:** PCA

## Hasil Global
| Metric | Value |
|---|:---:|
| Accuracy | 0.8486 |
| Precision | 0.8490 |
| Recall | 0.8486 |
| F1-Score | 0.8481 |

## Per-Kelas
| Class | Precision | Recall | F1-Score |
|---|:---:|:---:|:---:|
| Black_Males | 0.8842 | 0.8694 | 0.8768 |
| White_Females | 0.8636 | 0.8972 | 0.8801 |
| Asian_Males | 0.8338 | 0.7944 | 0.8137 |
| White_Males | 0.8557 | 0.9222 | 0.8877 |
| Black_Females | 0.8659 | 0.7889 | 0.8256 |
| Asian_Females | 0.7909 | 0.8194 | 0.8049 |
| **Macro Avg** | **0.8490** | **0.8486** | **0.8481** |

## Confusion Matrix
![CM](images/cm_gnb_vit-emotion-face_GaussianNB.png)
