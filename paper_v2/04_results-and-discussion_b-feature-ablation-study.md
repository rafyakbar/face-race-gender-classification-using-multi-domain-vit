## B. Feature Ablation Study

Dinamika kontribusi fusi bertahap dari representasi domain tunggal menuju domain ganda dan tri-domain pada [Table VII](#tab7), [Table VIII](#tab8), [Table IX](#tab9), serta [Table X](#tab10) menunjukkan karakteristik ekspansi ruang fitur yang berbeda secara fundamental antarpengklasifikasi. Pada model linier Logistic Regression, integrasi representasi usia biologis di atas pasangan biometrik-afektif menghasilkan peningkatan performa yang bersifat linier dan komplementer, yakni kenaikan sebesar +1.39% dari konfigurasi dual-domain Emotion ⊕ Face (87.27%) menuju konfigurasi tri-domain (88.66%). Sebaliknya, Support Vector Machine memperlihatkan fenomena kejenuhan representasi laten asimtotik (asymptotic feature saturation), di mana penambahan domain ketiga dari kombinasi Emotion ⊕ Face (88.47%) menuju konfigurasi tri-domain (88.61%) hanya menghasilkan kenaikan marjinal sebesar +0.14%. Perbedaan respons ini mengonfirmasi bahwa batas keputusan non-linier SVM telah mengonsolidasikan mayoritas varians pemisah antarkelas sejak tahap dual-domain, sementara regularisasi L2 pada Logistic Regression secara efektif memanfaatkan orthogonalitas informasi penuaan untuk menyempurnakan pemisahan kelas tanpa redundansi representasi.

Evaluasi ablasi kebocoran data disajikan secara komprehensif untuk memvalidasi kekokohan model sekaligus menanggapi telaah kritis mengenai potensi tumpang-tindih identitas subjek. Perbandingan antara protokol baseline historis yang menerapkan pembagian acak berstrata tingkat citra (Random Stratified Image-Level Split dengan 100% subject-overlap) dan tolok ukur utama berbasis partisi ketat subjek independen (Strict Subject-Disjoint Partitioning dengan 0% kebocoran identitas) dirangkum pada [Table XIII](#tab13). Hasil eksperimen menunjukkan bahwa seluruh model mengalami penurunan akurasi pada protokol subjek-disjoint, yang membuktikan keberadaan efek pembaur memorisasi identitas (identity confounding effect) pada evaluasi berbasis citra acak. Penurunan performa paling tajam teramati pada model berkepasitas representasi tinggi, yaitu SVM yang terkoreksi dari 93.70% menjadi 88.61% (penurunan bersih -5.09%) serta Logistic Regression dari 92.73% menjadi 88.66% (penurunan bersih -4.07%). Sebaliknya, model dengan kompleksitas lebih rendah memperlihatkan derajat kebocoran yang lebih minim, seperti Random Forest dari 86.85% ke 85.00% (-1.85%) dan Gaussian Naive Bayes dari 84.31% ke 82.31% (-2.00%). Temuan ini menegaskan bahwa capaian 88.66% pada Logistic Regression dan 88.61% pada SVM merefleksikan kemampuan generalisasi demografis riil yang bebas dari ilusi optimisme kebocoran data.

<a id="tab13"></a>
**Table XIII. Comparative Ablation Study on Data Leakage: Historical Baseline vs. Primary Benchmark.**

| Pengklasifikasi | Baseline Historis (Stratified Split)* | Tolok Ukur Utama (Subject-Disjoint) | Selisih Bersih (Delta) | Derajat Kebocoran Identitas |
| :--- | :---: | :---: | :---: | :---: |
| Random Forest (RF) | 86.85% | 85.00% | -1.85% | Rendah |
| Gaussian Naive Bayes (GNB) | 84.31% | 82.31% | -2.00% | Sangat Rendah |
| **Logistic Regression (LR)** | **92.73%** | **88.66%** | **-4.07%** | **Tinggi (Terkoreksi)** |
| Support Vector Machine (SVM) | 93.70% | 88.61% | -5.09% | Tinggi (Terkoreksi) |

*(Catatan: Baseline historis dievaluasi pada skema random stratified split dengan subject overlap penuh).

Untuk menguji signifikansi statistik inferensial antarmodel komparatif, dilakukan pengujian berpasangan berbasis McNemar's Test dengan koreksi kontinuitas Edwards serta Exact Binomial Test pada seluruh sampel uji held-out ($N = 2.160$). Hasil pengujian statistik inferensial tersebut dirangkum pada [Table XIV](#tab14). Keunggulan representasi tri-domain atas domain tunggal terbukti sangat signifikan, di mana komparasi Tri-Domain LR terhadap Single Face menghasilkan $\chi^2 = 29.58$ ($p < 0.001$). Pada transisi domain ganda ke tri-domain, penambahan fitur usia pada Tri-Domain LR memberikan peningkatan signifikan terhadap dual-domain Emotion ⊕ Face ($\chi^2 = 7.19, p = 0.0073 < 0.01$; Exact Binomial $p = 0.0075$). Sebaliknya, pada Tri-Domain SVM, penambahan fitur usia terhadap Emotion ⊕ Face mencatat $\chi^2 = 0.12$ ($p = 0.7343 > 0.05$; Exact Binomial $p = 0.7500$), mengonfirmasi terjadinya kejenuhan fitur nonlinier asimtotik. Sementara itu, perbandingan antara Tri-Domain LR dan Tri-Domain SVM menghasilkan $\chi^2 = 0.00$ ($p = 1.0000$) dengan selisih bersih satu citra (1.915 berbanding 1.914 prediksi benar), membuktikan tercapainya paritas performa prediktif sempurna antarkedua model.

<a id="tab14"></a>
**Table XIV. Paired Inferential Hypothesis Testing (McNemar's Test & Exact Binomial Test).**

| Pasangan Model Komparatif | Nilai Statistik $\chi^2$ | $p$-value McNemar | $p$-value Exact Binomial | Tingkat Signifikansi ($\alpha = 0.05$) | Interpretasi Ilmiah |
| :--- | :---: | :---: | :---: | :---: | :--- |
| Tri-Domain LR vs Single Face | 29.58 | < 0.001 | < 0.001 | Signifikan ($p < 0.001$) | Keunggulan representasi multi-domain |
| Tri-Domain LR vs Dual Emotion+Face | 7.19 | 0.0073 | 0.0075 | Signifikan ($p < 0.01$) | Komplementaritas fitur usia linier |
| Tri-Domain SVM vs Dual Emotion+Face | 0.12 | 0.7343 | 0.7500 | Tidak Signifikan ($p > 0.05$) | Kejenuhan fitur nonlinier asimtotik |
| Tri-Domain LR vs Tri-Domain SVM | 0.00 | 1.0000 | 1.0000 | Tidak Signifikan ($p = 1.0000$) | Paritas performa prediktif sempurna |
