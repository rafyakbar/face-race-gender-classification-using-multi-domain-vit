# GNB - vit-emotion

## Konfigurasi
- **Fitur:** vit-emotion (768 dimensi)
- **Tipe:** Single
- **Classifier:** GNB
- **Parameter Terbaik:** var_smoothing=0.00307029062975785
- **Scaler:** None
- **PCA:** PCA

## Hasil Global
| Metric | Value |
|---|:---:|
| Accuracy | 0.7338 |
| Precision | 0.7387 |
| Recall | 0.7338 |
| F1-Score | 0.7329 |

## Per-Kelas
| Class | Precision | Recall | F1-Score |
|---|:---:|:---:|:---:|
| Black_Males | 0.8306 | 0.6944 | 0.7564 |
| White_Females | 0.6929 | 0.8083 | 0.7462 |
| Asian_Males | 0.6694 | 0.6806 | 0.6749 |
| White_Males | 0.7324 | 0.8361 | 0.7808 |
| Black_Females | 0.7410 | 0.7472 | 0.7441 |
| Asian_Females | 0.7659 | 0.6361 | 0.6950 |
| **Macro Avg** | **0.7387** | **0.7338** | **0.7329** |

## Confusion Matrix
![CM](images/cm_gnb_vit-emotion_GaussianNB.png)
