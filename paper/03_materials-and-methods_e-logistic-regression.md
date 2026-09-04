## E. Logistic Regression

Pengklasifikasi LR diimplementasikan menggunakan formulasi regresi multinomial (Softmax regression) untuk memetakan probabilitas posterior ke dalam enam kelas demografis interseksional secara terpadu. Probabilitas kondisional sampel fitur $\mathbf{x}$ terhadap kelas target $y = c$ dihitung melalui fungsi Softmax ter-normalisasi sebagaimana dirumuskan pada [(7)](#eq7), di mana $\mathbf{w}_c$ dan $b_c$ masing-masing menyatakan vektor bobot dan bias kelas $c$, serta $K = 6$ merepresentasikan total kelas interseksional. Proses pembelajaran model meminimalkan fungsi kerugian cross-entropy dengan regularisasi $L_2$ untuk mengontrol kompleksitas bobot pada ruang representasi laten. Ruang pencarian hyperparameter mengevaluasi kombinasi penskalaan fitur, reduksi dimensionalitas PCA, parameter penalti regularisasi $C$, algoritma solver optimasi numerik (`lbfgs`, `saga`, `newton-cg`), dan batas iterasi konvergensi `max_iter`, yang menghasilkan 270 kombinasi konfigurasi atau 1.350 total fits pada prosedur 5-Fold Stratified Cross-Validation sesuai [Table V](#tab5).

<a id="eq7"></a>
$$
P(y = c \mid \mathbf{x}) = \frac{e^{\mathbf{w}_c^T \mathbf{x} + b_c}}{\sum_{j=1}^K e^{\mathbf{w}_j^T \mathbf{x} + b_j}} \tag{7}
$$

<a id="tab5"></a>
**Table V. Hyperparameter Search Space for Logistic Regression Classifier.**

| Component / Hyperparameter | Evaluated Values | Count |
|---|---|:---:|
| Feature Scaler | `None`, `MinMaxScaler` | 2 |
| Dimensionality Reduction (PCA) | `None`, `0.50`, `0.75` | 3 |
| Regularization Strength ($C$) | `0.01`, `0.1`, `1`, `10`, `100` | 5 |
| Optimization Solver | `'lbfgs'`, `'saga'`, `'newton-cg'` | 3 |
| Maximum Iterations (`max_iter`) | `500`, `1000`, `2000` | 3 |
| **Total Grid Combinations** | **2 × 3 × 5 × 3 × 3** | **270 (1,350 fits)** |
