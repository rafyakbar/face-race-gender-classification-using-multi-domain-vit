## G. Classification Pipeline

Pipeline modular mengintegrasikan penskalaan fitur (None, MinMaxScaler), reduksi dimensi PCA (None, 50%, 75%), dan pengklasifikasi hilir ke dalam rantai pemrosesan terpadu. Rantai transformasi dimodelkan pada [(12)](#eq12), di mana vektor masukan $\mathbf{x}$ diskalakan menjadi $\tilde{\mathbf{x}}$, direduksi via proyeksi PCA menjadi $\hat{\mathbf{x}}$, lalu dipetakan ke estimasi label $\hat{y} \in \{0, \dots, K-1\}$ untuk $K = 6$ subkelompok interseksional. Untuk menjamin zero identity leakage dan zero statistical leakage, penskalaan dan PCA di-fit ketat hanya pada lipatan latih 5-Fold StratifiedGroupKFold GridSearchCV pada subset latih (480 subjek, 8.640 citra) dengan isolasi groups = subject_id. Penelusuran hyperparameter merekonsiliasi (SVM: 288 + LR: 96 + RF: 288 + GNB: 240) = 912 kombinasi hyperparameter per skema fitur × 5 folds = 4.560 fits per skema fitur × 7 skema fitur = 31.920 fits validasi silang + 28 refits akhir pada himpunan latih sebelum evaluasi held-out, sebagaimana dirinci pada [Algorithm 1](#alg1).

<a id="eq12"></a>
$$
\mathbf{x} \xrightarrow{\text{Scaler}} \tilde{\mathbf{x}} \xrightarrow{\text{PCA}} \hat{\mathbf{x}} \xrightarrow{\text{Classifier}} \hat{y} \in \{0, \dots, K-1\} \tag{12}
$$

<a id="alg1"></a>
**Algorithm 1. Pseudocode of Leakage-Free StratifiedGroupKFold Hyperparameter Optimization and Evaluation Procedure.**

```text
Input : Multi-domain feature matrix X in R^{N x D}, labels y in {0,...,5}^N, subject_ids g in {1,...,S}^N, hyperparameter grid Theta
Output: Best model M*, optimal hyperparameters theta*, evaluation metrics on held-out test set

1:  Partition dataset into D_train (480 subjects, 8.640 images) and D_test (120 subjects, 2.160 images) via subject-disjoint split
2:  Initialize cv = StratifiedGroupKFold(n_splits=5, shuffle=True, random_state=42) on D_train with groups = subject_ids
3:  For each configuration theta in Theta do:
4:      For fold k = 1 to 5 do:
5:          Split D_train into train_k and val_k with zero subject overlap
6:          Fit Scaler on train_k and transform train_k, val_k
7:          Fit PCA on train_k and transform train_k, val_k
8:          Train Classifier(theta) on transformed train_k
9:          Evaluate accuracy on transformed val_k
10:     End For
11:     Compute mean cross-validation score across 5 folds
12: End For
13: Select optimal theta* = argmax mean_cv_score
14: Refit Scaler, PCA, and Classifier(theta*) on entire D_train
15: Transform held-out D_test using fitted Scaler and PCA
16: Predict y_pred on transformed D_test and compute Accuracy, F1, McNemar, Wilson CI, EOD
```
