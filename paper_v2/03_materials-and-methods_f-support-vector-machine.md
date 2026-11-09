## F. Support Vector Machine

<a id="tab6"></a>
**Table VI. Hyperparameter Search Space for Support Vector Machine Classifier.**

| Component / Hyperparameter | Evaluated Values | Count |
|---|---|:---:|
| Feature Scaler | `None`, `MinMaxScaler` | 2 |
| Dimensionality Reduction (PCA) | `None`, `0.50`, `0.75` | 3 |
| Regularization Parameter | `0.01`, `0.1`, `1`, `10` | 4 |
| Kernel Function | `'linear'`, `'rbf'`, `'poly'` | 3 |
| Polynomial Degree | `2`, `3` | 2 |
| Kernel Coefficient | `'scale'`, `'auto'` | 2 |
| **Total Grid Combinations** | - | **288 (1,440 fits)** |

Pengklasifikasi Support Vector Machine (SVM) mengonstruksikan bidang pemisah berjarak terjauh (maximum margin hyperplane) untuk memisahkan enam kelas interseksional pada ruang representasi laten berdimensi tinggi [[40]](06_references.md#ref40). Fungsi kernel memproyeksikan distribusi data nonlinier dari fusi multi-domain ke ruang fitur berdimensi lebih tinggi, mencakup opsi kernel linear, Radial Basis Function (RBF), dan polinomial [[41]](06_references.md#ref41). Formulasi kernel polinomial pada [(11)](#eq11) menghitung produk titik $\langle \mathbf{x}_i, \mathbf{x}_j \rangle$ antara vektor fitur $\mathbf{x}_i$ dan $\mathbf{x}_j$, di mana $\gamma$ menyatakan parameter penskalaan kernel, $d \in \{2, 3\}$ menentukan derajat pemetaan, dan konstanta intercept $\text{coef0} = 0.0$ mengikuti nilai bawaan scikit-learn [[42]](06_references.md#ref42). Pemetaan polinomial ini memfasilitasi penangkapan interaksi nonlinier antardimensi visual secara efisien [[43]](06_references.md#ref43). Optimasi hyperparameter menelusuri parameter penalti $C \in \{0.01, 0.1, 1, 10\}$, ragam fungsi kernel, koefisien $\gamma$, derajat polinomial, serta opsi penskalaan dan PCA, menghasilkan 288 kombinasi grid Cartesian (108 konfigurasi unik efektif) atau 1.440 total fits pada prosedur 5-Fold StratifiedGroupKFold Cross-Validation sesuai [Table VI](#tab6).

<a id="eq11"></a>
$$
K(\mathbf{x}_i, \mathbf{x}_j) = (\gamma \langle \mathbf{x}_i, \mathbf{x}_j \rangle + \text{coef0})^d, \quad d \in \{2, 3\} \tag{11}
$$
