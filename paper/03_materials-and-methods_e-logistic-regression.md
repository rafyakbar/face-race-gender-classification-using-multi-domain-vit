## E. Logistic Regression

<a id="tab5"></a>
**Table V. Hyperparameter Search Space for Logistic Regression Classifier.**

| Component / Hyperparameter | Evaluated Values | Count |
|---|---|:---:|
| Feature Scaler | `None`, `MinMaxScaler` | 2 |
| Dimensionality Reduction (PCA) | `None`, `0.50`, `0.75` | 3 |
| Regularization Strength | `0.01`, `0.1`, `1`, `10`, `100` | 5 |
| Optimization Solver | `'lbfgs'`, `'saga'`, `'newton-cg'` | 3 |
| Maximum Iterations | `500`, `1000`, `2000` | 3 |
| **Total Grid Combinations** | - | **270 (1,350 fits)** |

Pendekatan regresi multinomial (Softmax regression) pada LR memetakan representasi fitur laten ke dalam enam kategori demografis interseksional melalui estimasi probabilitas linier terpadu [[37]](06_references.md#ref37). Fungsi probabilitas Softmax menghitung peluang bersyarat sampel terhadap kategori target sebagaimana didefinisikan pada [(7)](#eq7), di mana $\mathbf{x}$ merepresentasikan vektor fitur masukan, $y$ adalah variabel label kelas, $c$ menyatakan kategori kelas target, $\mathbf{w}_c$ dan $b_c$ masing-masing merupakan vektor bobot serta bias kelas $c$, sedangkan konstanta $K = 6$ menunjukkan jumlah total kelas interseksional [[38]](06_references.md#ref38). Proses pembelajaran model meminimalkan fungsi kerugian cross-entropy dengan menyertakan penalti regularisasi $L_2$ untuk mengendalikan kompleksitas bobot pada ruang representasi berdimensi tinggi [[39]](06_references.md#ref39). Pencarian hyperparameter terstruktur mengevaluasi variasi kekuatan regularisasi $C$, algoritma solver optimasi (`lbfgs`, `saga`, `newton-cg`), batas iterasi `max_iter`, serta integrasi penskalaan dan PCA, menghasilkan 270 kombinasi evaluasi atau 1,350 total fits pada protokol 5-Fold Stratified Cross-Validation yang disajikan pada [Table V](#tab5).

<a id="eq7"></a>
$$
P(y = c \mid \mathbf{x}) = \frac{e^{\mathbf{w}_c^T \mathbf{x} + b_c}}{\sum_{j=1}^K e^{\mathbf{w}_j^T \mathbf{x} + b_j}} \tag{7}
$$

