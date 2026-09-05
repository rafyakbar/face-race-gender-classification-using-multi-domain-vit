## C. Random Forest

Model ensemble RF mengagregasikan prediksi sekumpulan pohon keputusan independen untuk mengklasifikasikan fitur wajah berdasarkan prinsip bootstrap aggregating (bagging) dan random subspace method. Pendekatan ini mereduksi varians prediksi dengan membangun sebanyak $B$ pohon klasifikasi dari sampel acak data latih. Setiap percabangan node membatasi pemilihan fitur pada subset acak berukuran `max_features` $\in \{\text{'sqrt'}, \text{'log2'}\}$ untuk menekan korelasi antarpohon. Kriteria pemotongan cabang mengoptimalkan indeks Gini impurity hingga mencapai batas kedalaman `max_depth` atau batas minimum daun `min_samples_leaf`. Mekanisme majority voting menentukan keputusan akhir sampel citra melintasi seluruh pohon keputusan. Prosedur penalaan hyperparameter mengevaluasi kombinasi penskalaan fitur, reduksi dimensionalitas PCA, variasi jumlah pohon `n_estimators`, batas kedalaman, dan kriteria pemisahan sampel, menghasilkan 288 konfigurasi grid dengan 1.440 total fits melalui 5-Fold Stratified Cross-Validation sebagaimana dirangkum pada [Table III](#tab3).

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
