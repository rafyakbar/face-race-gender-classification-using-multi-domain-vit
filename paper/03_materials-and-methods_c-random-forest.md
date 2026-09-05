## C. Random Forest

Sebagai representasi kelompok model ensemble, RF memanfaatkan agregasi sekumpulan pohon keputusan independen yang dibangun melalui prinsip bootstrap aggregating (bagging) dan random subspace method. Mekanisme ini mereduksi varians prediksi dengan membangun sebanyak $B$ pohon dari sampel acak berulang data latih. Pada setiap percabangan node, pemilihan fitur dibatasi pada subset acak berukuran `max_features` $\in \{\text{'sqrt'}, \text{'log2'}\}$ untuk menekan korelasi antarpohon, sementara pembagian partisi dioptimalkan menggunakan indeks Gini impurity hingga mencapai batas kedalaman `max_depth` atau ukuran daun minimum `min_samples_leaf`. Keputusan akhir sampel citra diagregasikan melalui majority voting melintasi seluruh pohon. Eksplorasi parameter penalaan model ini mencakup variasi penskalaan, dekomposisi PCA, jumlah pohon `n_estimators`, kedalaman, dan pembagian sampel, yang secara keseluruhan merangkum 288 konfigurasi grid dengan 1.440 total fits pada validasi silang 5-Fold Stratified Cross-Validation, sebagaimana dirangkum pada [Table III](#tab3).

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
