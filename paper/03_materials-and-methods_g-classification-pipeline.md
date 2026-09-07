## G. Classification Pipeline

Kerangka kerja pipeline modular menyatukan penskalaan fitur, reduksi dimensi representasi, dan estimasi model hilir ke dalam rantai transformasi terpadu. Rantai pemrosesan tersebut dirumuskan pada [(9)](#eq9), di mana vektor fitur input $\mathbf{x}$ ditransformasikan oleh modul penskalaan menjadi $\tilde{\mathbf{x}}$, direduksi dimensinya melalui PCA menjadi $\hat{\mathbf{x}}$, dan dipetakan oleh pengklasifikasi menuju prediksi label $\hat{y} \in \{0, 1, 2, 3, 4, 5\}$ untuk enam subkelompok demografis. Protokol validasi silang menerapkan skema 5-Fold Stratified Cross-Validation dengan pengacakan terkontrol untuk mempertahankan proporsi seimbang ~16.67% per kelas di setiap fold. Untuk mencegah kebocoran informasi, Scaler dan PCA di-fit secara eksklusif hanya pada data latih di dalam GridSearchCV sebelum diterapkan ke data validasi. Penelusuran terhadap 1,086 kombinasi hyperparameter menghasilkan 5,430 fits per skema fitur atau 38,010 total fits untuk tujuh konfigurasi representasi, serta 28 refit final sebelum pengujian pada data uji held-out independen.

<a id="eq9"></a>
$$
\mathbf{x} \xrightarrow{\text{Scaler}} \tilde{\mathbf{x}} \xrightarrow{\text{PCA}} \hat{\mathbf{x}} \xrightarrow{\text{Classifier}} \hat{y} \in \{0, 1, 2, 3, 4, 5\} \tag{9}
$$
