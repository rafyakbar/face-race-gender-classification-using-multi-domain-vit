## D. Gaussian Naive Bayes

Klasifikasi berbasis probabilitas pada penelitian ini diwujudkan melalui algoritma GNB, yang memanfaatkan Teorema Bayes dengan asumsi bahwa seluruh dimensi fitur kontinu bersifat independen secara bersyarat. Kerapatan probabilitas kontinu $x_i$ untuk suatu kelas interseksional $y = c$ diestimasi melalui fungsi distribusi normal (Gaussian) yang dirumuskan pada [(6)](#eq6), di mana parameter $\mu_{c,i}$ dan $\sigma_{c,i}^2$ melambangkan rata-rata (mean) serta varians fitur ke-$i$ pada subkelompok target $c$. Mengingat ruang fitur gabungan memiliki dimensionalitas tinggi dengan risiko singularitas varians numerik mendekati nol, stabilitas komputasi dijaga melalui penambahan koefisien penghalusan `var_smoothing` pada varians empiris. Skema validasi silang 5-Fold Stratified Cross-Validation menguji interaksi penskalaan data, reduksi dimensi PCA, serta pemindaian 40 interval `var_smoothing` berskala logaritmik ($1.0 \times 10^{-9}$ hingga $1.0 \times 10^{2}$), menghasilkan 240 kombinasi pengujian dengan total 1.200 kali proses fitting seperti dipaparkan pada [Table IV](#tab4).

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
