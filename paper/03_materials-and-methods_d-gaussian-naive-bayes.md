## D. Gaussian Naive Bayes

<a id="tab4"></a>
**Table IV. Hyperparameter Search Space for Gaussian Naive Bayes Classifier.**

| Component / Hyperparameter | Evaluated Values | Count |
|---|---|:---:|
| Feature Scaler | `None`, `MinMaxScaler` | 2 |
| Dimensionality Reduction (PCA) | `None`, `0.50`, `0.75` | 3 |
| Variance Smoothing | $\text{logspace}(-9, 2, 40)$ ($1.0 \times 10^{-9}$ to $1.0 \times 10^{2}$) | 40 |
| **Total Grid Combinations** | - | **240 (1,200 fits)** |

Berdasarkan Teorema Bayes, pengklasifikasi GNB mengestimasi probabilitas posterior kelas demografis interseksional dengan asumsi bahwa seluruh dimensi fitur kontinu bersifat independen secara bersyarat. Fungsi kerapatan probabilitas distribusi normal memodelkan likelihood fitur kontinu terhadap kelas target sesuai formulasi pada [(6)](#eq6), di mana $x_i$ menyatakan nilai fitur kontinu ke-$i$, $y$ adalah variabel label kelas, $c$ merupakan kategori kelas target, serta $\mu_{c,i}$ dan $\sigma_{c,i}^2$ masing-masing merepresentasikan rata-rata (mean) dan varians fitur ke-$i$ pada kelas $c$. Penambahan parameter penghalusan `var_smoothing` menjaga stabilitas komputasi terhadap risiko varians mendekati nol pada ruang representasi laten berdimensi tinggi. Prosedur penalaan hyperparameter melalui 5-Fold Stratified Cross-Validation mengevaluasi kombinasi penskalaan data, reduksi dimensionalitas PCA, serta 40 interval `var_smoothing` yang dieksplorasi secara logaritmik dari $1.0 \times 10^{-9}$ hingga $1.0 \times 10^{2}$, menghasilkan 240 kombinasi grid dengan total 1,200 proses fitting sebagaimana dipaparkan pada [Table IV](#tab4).

<a id="eq6"></a>
$$
P(x_i \mid y = c) = \frac{1}{\sqrt{2\pi\sigma_{c,i}^2}} \exp\left(-\frac{(x_i - \mu_{c,i})^2}{2\sigma_{c,i}^2}\right) \tag{6}
$$
