## F. Support Vector Classifier

Prinsip maksimisasi margin geometris antarsubkelompok diwujudkan menggunakan SVC untuk membentuk bidang pemisah optimal (maximum margin hyperplane) pada ruang representasi laten berdimensi tinggi. Distribusi data nonlinier dari fusi multi-domain ditangani melalui fungsi kernel, mencakup kernel linear, Radial Basis Function (RBF), dan polinomial. Formulasi kernel polinomial derajat dua dinyatakan pada [(8)](#eq8), di mana $\langle \mathbf{x}_i, \mathbf{x}_j \rangle$ merupakan produk titik antardua vektor fitur, $\gamma$ adalah parameter penskalaan kernel, $d = 2$ menentukan derajat pemetaan, dan konstanta intercept $\text{coef0} = 0.0$ mengikuti nilai bawaan scikit-learn. Pemetaan ini memfasilitasi penangkapan interaksi kuadratik antardimensi fitur secara efisien. Ruang pencarian hyperparameter mengevaluasi parameter penalti $C \in \{0.01, 0.1, 1, 10\}$, jenis fungsi kernel, koefisien $\gamma$, derajat polinomial, serta kombinasi penskalaan dan PCA, menghasilkan 288 kombinasi konfigurasi atau 1.440 total fits pada prosedur 5-Fold Stratified Cross-Validation sesuai [Table VI](#tab6).

<a id="eq8"></a>
$$
K(\mathbf{x}_i, \mathbf{x}_j) = (\gamma \langle \mathbf{x}_i, \mathbf{x}_j \rangle + \text{coef0})^d, \quad d = 2 \tag{8}
$$

<a id="tab6"></a>
**Table VI. Hyperparameter Search Space for Support Vector Classifier.**

| Component / Hyperparameter | Evaluated Values | Count |
|---|---|:---:|
| Feature Scaler | `None`, `MinMaxScaler` | 2 |
| Dimensionality Reduction (PCA) | `None`, `0.50`, `0.75` | 3 |
| Regularization Parameter ($C$) | `0.01`, `0.1`, `1`, `10` | 4 |
| Kernel Function | `'linear'`, `'rbf'`, `'poly'` | 3 |
| Polynomial Degree (`degree`) | `2`, `3` | 2 |
| Kernel Coefficient (`gamma`) | `'scale'`, `'auto'` | 2 |
| **Total Grid Combinations** | **2 × 3 × 4 × 3 × 2 × 2** | **288 (1,440 fits)** |
