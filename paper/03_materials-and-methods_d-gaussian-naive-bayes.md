## D. Gaussian Naive Bayes

Model probabilistik GNB mengestimasi probabilitas posterior kelas demografis interseksional berdasarkan Teorema Bayes dengan asumsi bahwa seluruh dimensi fitur kontinu bersifat independen secara bersyarat. Fungsi kerapatan probabilitas distribusi normal (Gaussian) memodelkan likelihood dimensi fitur kontinu $x_i$ terhadap kelas target $y = c$ sesuai formulasi pada [(6)](#eq6), di mana parameter $\mu_{c,i}$ dan $\sigma_{c,i}^2$ masing-masing menyatakan rata-rata (mean) serta varians fitur ke-$i$ pada kelas target $c$. Penambahan parameter penghalusan `var_smoothing` menjaga stabilitas komputasi terhadap risiko varians mendekati nol pada ruang representasi laten berdimensi tinggi. Skema validasi silang 5-Fold Stratified Cross-Validation menguji interaksi penskalaan data, reduksi dimensionalitas PCA, serta 40 interval `var_smoothing` berskala logaritmik ($1.0 \times 10^{-9}$ hingga $1.0 \times 10^{2}$), menghasilkan 240 kombinasi grid dengan total 1.200 kali proses fitting seperti dipaparkan pada [Table IV](#tab4).

<a id="eq6"></a>
$$
P(x_i \mid y = c) = \frac{1}{\sqrt{2\pi\sigma_{c,i}^2}} \exp\left(-\frac{(x_i - \mu_{c,i})^2}{2\sigma_{c,i}^2}\right) \tag{6}
$$

<a id="tab4"></a>
**Table IV. Hyperparameter Search Space for Gaussian Naive Bayes Classifier.**

| Component / Hyperparameter | Evaluated Values | Count |
|---|---|:---:|
| Feature Scaler | `None`, `MinMaxScaler` | 2 |
| Dimensionality Reduction (PCA) | `None`, `0.50`, `0.75` | 3 |
| Variance Smoothing (`var_smoothing`) | $\text{logspace}(-9, 2, 40)$ ($1.0 \times 10^{-9}$ to $1.0 \times 10^{2}$) | 40 |
| **Total Grid Combinations** | **2 × 3 × 40** | **240 (1,200 fits)** |
