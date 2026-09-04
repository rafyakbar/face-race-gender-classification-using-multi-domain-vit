## D. Gaussian Naive Bayes

Pengklasifikasi GNB diimplementasikan sebagai model probabilistik multi-kelas berbasis Teorema Bayes yang mengasumsikan independensi bersyarat antarlapisan fitur kontinu. Likelihood dari dimensi fitur kontinu $x_i$ terhadap kelas target interseksional $y = c$ dimodelkan mengikuti fungsi kerapatan probabilitas distribusi normal (Gaussian), sebagaimana dirumuskan pada [(6)](#eq6), di mana $\mu_{c,i}$ dan $\sigma_{c,i}^2$ masing-masing menyatakan nilai rata-rata (mean) dan varians dari fitur ke-$i$ pada kelas $c$. Untuk mencegah instabilitas numerik akibat varians yang mendekati nol pada ruang representasi laten berdimensi tinggi, parameter penghalusan `var_smoothing` ditambahkan ke dalam perhitungan varians empiris. Ruang pencarian hyperparameter pada penelitian ini mengevaluasi interaksi penskalaan fitur, reduksi dimensionalitas PCA, serta 40 nilai `var_smoothing` yang dieksplorasi secara logaritmik dalam rentang $1.0 \times 10^{-9}$ hingga $1.0 \times 10^{2}$, menghasilkan total 240 kombinasi grid atau 1.200 total fits melalui 5-Fold Stratified Cross-Validation sesuai rincian pada [Table IV](#tab4).

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
