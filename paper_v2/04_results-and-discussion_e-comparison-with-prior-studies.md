## E. Comparison with Prior Studies

Perbandingan empiris kerangka kerja usulan terhadap studi terdahulu dan baseline internal pada dataset DemogPairs disajikan pada [Table XVI](#tab16). Evaluasi distrukturkan ke dalam dua kelompok protokol partisi data, yaitu kelompok protokol Stratified dan kelompok protokol Subject-Disjoint. Pada kelompok protokol Stratified yang merepresentasikan komparasi kontekstual, Proposed Tri-Domain + SVM mencatat performa tertinggi dengan Akurasi 93.70%, Presisi 93.72%, Recall 93.70%, dan F1-Score 93.69%. Capaian tersebut melampaui model terdahulu Dual-ViT + SVM dengan Akurasi 92.41% [[19]](06_references.md#ref19) dan MD-ViT + XGBoost dengan Akurasi 89.07% [[20]](06_references.md#ref20). Pada kelompok protokol Subject-Disjoint yang mengevaluasi generalisasi tanpa kebocoran identitas, Proposed Tri-Domain + LR memimpin tolok ukur dengan Akurasi 88.66%, disusul oleh Proposed Tri-Domain + SVM (88.61%). Fusi tri-domain secara konsisten mengungguli konfigurasi single-domain dan dual-domain.

<a id="tab16"></a>
**Table XVI. Contextual and Controlled Comparison of the Proposed Framework on the DemogPairs Dataset.**

| Model | Data Split Protocol | Accuracy (%) | Precision (%) | Recall (%) | F1-Score (%) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| MD-ViT + XGBoost [[20]](06_references.md#ref20) | Stratified | 89.07 | 89.12 | 89.07 | 89.01 |
| Dual-ViT + SVM [[19]](06_references.md#ref19) | Stratified | 92.41 | 92.48 | 92.41 | 92.38 |
| **Proposed Tri-Domain + SVM** | **Stratified** | **93.70** | **93.72** | **93.70** | **93.69** |
| Single-Domain `Face` + LR | Subject-Disjoint | 86.39 | 86.46 | 86.39 | 86.40 |
| Single-Domain `Face` + SVM | Subject-Disjoint | 86.16 | 86.24 | 86.16 | 86.19 |
| Single-Domain `Emotion` + SVM | Subject-Disjoint | 85.79 | 85.84 | 85.79 | 85.80 |
| Single-Domain `Age` + SVM | Subject-Disjoint | 82.55 | 82.68 | 82.55 | 82.58 |
| Dual-Domain `Emotion ⊕ Face` + SVM | Subject-Disjoint | 88.43 | 88.50 | 88.43 | 88.44 |
| Tri-Domain + RF | Subject-Disjoint | 85.00 | 85.06 | 85.00 | 84.93 |
| Dual-Domain `Emotion ⊕ Face` + GNB | Subject-Disjoint | 84.31 | 84.37 | 84.31 | 84.30 |
| Proposed Tri-Domain + SVM | Subject-Disjoint | 88.61 | 88.71 | 88.61 | 88.63 |
| **Proposed Tri-Domain + LR** | **Subject-Disjoint** | **88.66** | **88.75** | **88.66** | **88.68** |

Penetapan posisi riset ini menegaskan kualifikasi metodologis yang krusial antara kedua protokol evaluasi tersebut. Hasil pada protokol Stratified diklasifikasikan murni sebagai komparasi kontekstual karena pemisahan acak tingkat citra membiarkan identitas subjek tumpang-tindih antara set latih dan uji, ditambah potensi variasi prapemrosesan antarstudi. Perbedaan performa antara evaluasi protokol Stratified (93.70%) dan benchmark primer Subject-Disjoint (88.66%) mengindikasikan adanya optimisme semu akibat kebocoran data identitas sebesar 5.09 pp. Penerapan protokol ketat Subject-Disjoint pada 480 subjek latih dan 120 subjek uji held-out pada korpus DemogPairs [[25]](06_references.md#ref25) yang sejatinya dirancang untuk verifikasi pasangan identitas wajah menjamin eliminasi kebocoran identitas secara mutlak, sehingga menghasilkan evaluasi klasifikasi 6-kelas interseksional yang andal di dunia nyata.
