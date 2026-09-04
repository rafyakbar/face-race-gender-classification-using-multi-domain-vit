## F. Support Vector Classifier

Pengklasifikasi SVC diimplementasikan untuk membentuk batas keputusan margin optimal (maximum margin hyperplane) yang memisahkan enam kelas interseksional pada ruang fitur laten berdimensi tinggi. Untuk menangani kompleksitas distribusi nonlinier pada representasi gabungan multi-domain, pemetaan ruang fitur dilakukan melalui fungsi kernel, mencakup kernel linear, Radial Basis Function (RBF), dan polinomial. Formulasi kernel polinomial derajat dua dirumuskan pada [(8)](#eq8), di mana $\langle \mathbf{x}_i, \mathbf{x}_j \rangle$ menyatakan produk titik antarvektor fitur masukan, $\gamma$ adalah koefisien penskalaan kernel, $d = 2$ merupakan derajat polinomial, serta $\text{coef0} = 0.0$ adalah parameter intercept konstan bawaan scikit-learn. Pemetaan polinomial ini memungkinkan model menangkap interaksi kuadratik antardimensi representasi visual secara efektif. Ruang pencarian hyperparameter mengevaluasi kombinasi penskalaan fitur, reduksi dimensionalitas PCA, parameter penalti regularisasi $C \in \{0.01, 0.1, 1, 10\}$, fungsi kernel, derajat polinomial, dan nilai $\gamma$, yang menghasilkan 288 kombinasi konfigurasi atau 1.440 total fits pada prosedur 5-Fold Stratified Cross-Validation sesuai [Table VI](#tab6).

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
