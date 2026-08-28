# GNB - vit-face

## Konfigurasi
- **Fitur:** vit-face (768 dimensi)
- **Tipe:** Single
- **Classifier:** GNB
- **Parameter Terbaik:** var_smoothing=0.04124626382901348
- **Scaler:** MinMaxScaler
- **PCA:** PCA

## Hasil Global
| Metric | Value |
|---|:---:|
| Accuracy | 0.8269 |
| Precision | 0.8271 |
| Recall | 0.8269 |
| F1-Score | 0.8258 |

## Per-Kelas
| Class | Precision | Recall | F1-Score |
|---|:---:|:---:|:---:|
| Black_Males | 0.8280 | 0.8556 | 0.8415 |
| White_Females | 0.8819 | 0.8917 | 0.8867 |
| Asian_Males | 0.7745 | 0.7917 | 0.7830 |
| White_Males | 0.8621 | 0.9028 | 0.8820 |
| Black_Females | 0.8311 | 0.6972 | 0.7583 |
| Asian_Females | 0.7851 | 0.8222 | 0.8033 |
| **Macro Avg** | **0.8271** | **0.8269** | **0.8258** |

## Confusion Matrix
![CM](images/cm_gnb_vit-face_GaussianNB.png)
