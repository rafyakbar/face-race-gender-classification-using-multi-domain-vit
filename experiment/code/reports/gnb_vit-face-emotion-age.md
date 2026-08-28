# GNB - vit-face-emotion-age

## Konfigurasi
- **Fitur:** vit-face-emotion-age (2304 dimensi)
- **Tipe:** Tri-Domain
- **Classifier:** GNB
- **Parameter Terbaik:** var_smoothing=0.0058780160722749115
- **Scaler:** None
- **PCA:** PCA

## Hasil Global
| Metric | Value |
|---|:---:|
| Accuracy | 0.8505 |
| Precision | 0.8512 |
| Recall | 0.8505 |
| F1-Score | 0.8505 |

## Per-Kelas
| Class | Precision | Recall | F1-Score |
|---|:---:|:---:|:---:|
| Black_Males | 0.8781 | 0.8806 | 0.8793 |
| White_Females | 0.8641 | 0.8833 | 0.8736 |
| Asian_Males | 0.8272 | 0.8111 | 0.8191 |
| White_Males | 0.8936 | 0.8861 | 0.8898 |
| Black_Females | 0.8576 | 0.8028 | 0.8293 |
| Asian_Females | 0.7865 | 0.8389 | 0.8118 |
| **Macro Avg** | **0.8512** | **0.8505** | **0.8505** |

## Confusion Matrix
![CM](images/cm_gnb_vit-face-emotion-age_GaussianNB.png)
