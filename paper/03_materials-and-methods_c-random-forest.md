## C. Random Forest

Pengklasifikasi RF diimplementasikan sebagai model ensemble berbasis pohon keputusan yang menggabungkan prinsip bootstrap aggregating (bagging) dan random subspace method untuk mereduksi varians prediksi. Pada arsitektur ini, sebanyak $B$ pohon klasifikasi independen dibangun menggunakan sampel bootstrap dari data latih, di mana percabangan setiap node mengevaluasi subset fitur acak berukuran `max_features` $\in \{\text{'sqrt'}, \text{'log2'}\}$ untuk meminimalkan korelasi antarpohon. Kriteria pemotongan node dioptimalkan berdasarkan indeks Gini impurity hingga mencapai kedalaman maksimum `max_depth` atau batas minimum sampel daun `min_samples_leaf`. Prediksi akhir untuk setiap sampel citra wajah ditentukan melalui mekanisme majority voting melintasi seluruh pohon keputusan. Ruang pencarian hyperparameter yang dievaluasi pada penelitian ini mencakup kombinasi penskalaan fitur, reduksi dimensionalitas PCA, variasi jumlah pohon `n_estimators`, kedalaman pohon, serta kriteria pembagian sampel, yang menghasilkan total 288 kombinasi konfigurasi atau 1.440 total fits pada prosedur 5-Fold Stratified Cross-Validation, sebagaimana dirincikan pada [Table III](#tab3).

<a id="tab3"></a>
**Table III. Hyperparameter Search Space for Random Forest Classifier.**

| Component / Hyperparameter | Evaluated Values | Count |
|---|---|:---:|
| Feature Scaler | `None`, `MinMaxScaler` | 2 |
| Dimensionality Reduction (PCA) | `None`, `0.50`, `0.75` | 3 |
| Number of Estimators (`n_estimators`) | `100`, `200` | 2 |
| Maximum Tree Depth (`max_depth`) | `None`, `20`, `30` | 3 |
| Feature Subspace (`max_features`) | `'sqrt'`, `'log2'` | 2 |
| Minimum Samples Split (`min_samples_split`) | `2`, `5` | 2 |
| Minimum Samples Leaf (`min_samples_leaf`) | `1`, `2` | 2 |
| **Total Grid Combinations** | **2 × 3 × 2 × 3 × 2 × 2 × 2** | **288 (1,440 fits)** |
