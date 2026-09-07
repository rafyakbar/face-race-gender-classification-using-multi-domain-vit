## F. Support Vector Machine

<a id="tab6"></a>
**Table VI. Hyperparameter Search Space for Support Vector Machine.**

| Component / Hyperparameter | Evaluated Values | Count |
|---|---|:---:|
| Feature Scaler | `None`, `MinMaxScaler` | 2 |
| Dimensionality Reduction (PCA) | `None`, `0.50`, `0.75` | 3 |
| Regularization Parameter | `0.01`, `0.1`, `1`, `10` | 4 |
| Kernel Function | `'linear'`, `'rbf'`, `'poly'` | 3 |
| Polynomial Degree | `2`, `3` | 2 |
| Kernel Coefficient | `'scale'`, `'auto'` | 2 |
| **Total Grid Combinations** | - | **288 (1,440 fits)** |

Pengklasifikasi SVM mengonstruksikan bidang pemisah berjarak terjauh (maximum margin hyperplane) untuk memisahkan enam kelas interseksional pada ruang representasi laten berdimensi tinggi. Fungsi kernel memproyeksikan distribusi data nonlinier dari fusi multi-domain ke ruang fitur berdimensi lebih tinggi, mencakup opsi kernel linear, Radial Basis Function (RBF), dan polinomial. Formulasi kernel polinomial derajat dua pada [(8)](#eq8) menghitung produk titik $\langle \mathbf{x}_i, \mathbf{x}_j \rangle$ antara pasangan vektor fitur $\mathbf{x}_i$ dan $\mathbf{x}_j$, di mana $\gamma$ menyatakan parameter penskalaan kernel, $d = 2$ menentukan derajat pemetaan, dan konstanta intercept $\text{coef0} = 0.0$ mengikuti nilai bawaan scikit-learn. Pemetaan kuadratik ini memfasilitasi penangkapan interaksi nonlinier antardimensi visual secara efisien. Optimasi hyperparameter menelusuri rentang parameter penalti $C \in \{0.01, 0.1, 1, 10\}$, ragam fungsi kernel, koefisien $\gamma$, derajat polinomial, serta opsi penskalaan dan PCA, menghasilkan 288 kombinasi konfigurasi atau 1,440 total fits pada prosedur 5-Fold Stratified Cross-Validation sesuai [Table VI](#tab6).

<a id="eq8"></a>
$$
K(\mathbf{x}_i, \mathbf{x}_j) = (\gamma \langle \mathbf{x}_i, \mathbf{x}_j \rangle + \text{coef0})^d, \quad d = 2 \tag{8}
$$
