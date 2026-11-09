## E. Comparison with Prior Studies

Perbandingan empiris kerangka kerja usulan terhadap model terdahulu dan baseline internal pada dataset DemogPairs disajikan pada [Table XVI](#tab16). Evaluasi distrukturkan ke dalam dua kelompok protokol partisi data, yaitu kelompok protokol Stratified dan kelompok protokol Subject-Disjoint. Studi seminal oleh Hupont dan Fernández (2019) [[25]](06_references.md#ref25) menguji verifikasi pasangan identitas berbasis kurva Receiver Operating Characteristic (ROC) dan Area Under the Curve (AUC), serta tidak mengevaluasi klasifikasi 6-kelas interseksional. Pada kelompok protokol Stratified yang merepresentasikan komparasi kontekstual, Proposed Tri-Domain + SVM (Historical Baseline) mencatat performa tertinggi dengan Akurasi 93.70%, Presisi 93.72%, Recall 93.70%, dan F1-Score 93.69%. Capaian tersebut melampaui model terdahulu Putri et al. (2025) [[19]](06_references.md#ref19) (Akurasi 91.15%) dan Putri et al. (2025) [[20]](06_references.md#ref20) (90.85%). Selain itu, hasil ini juga mengungguli baseline komparasi ViT-Base [[17]](06_references.md#ref17) (85.40%) dan ResNet-50 [[13]](06_references.md#ref13) (81.25%). Pada kelompok protokol Subject-Disjoint yang mengevaluasi generalisasi tanpa kebocoran identitas, Proposed Tri-Domain + LR memimpin tolok ukur dengan Akurasi 88.66%, Presisi 88.75%, Recall 88.66%, dan F1-Score 88.68%, disusul oleh Proposed Tri-Domain + SVM (88.61%). Fusi tri-domain secara konsisten mengungguli konfigurasi single-domain dan dual-domain.

<a id="tab16"></a>
**Table XVI. Contextual and Controlled Comparison of the Proposed Framework on the DemogPairs Dataset.**

| Model | Feature Domain | Data Split Protocol | Accuracy (%) | Precision (%) | Recall (%) | F1-Score (%) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| Hupont & Fernández (2019) [[25]](06_references.md#ref25)* | Single (Face Verification) | Pairwise ROC Verification | - | - | - | - |
| Baseline ResNet-50 [[13]](06_references.md#ref13) | Single (Face) | Stratified | 81.25 | 81.30 | 81.25 | 81.20 |
| Baseline ViT-Base [[17]](06_references.md#ref17) | Single (Face) | Stratified | 85.40 | 85.45 | 85.40 | 85.38 |
| Putri et al. (2025) [[19]](06_references.md#ref19) | Dual (Face + Emotion) | Stratified | 91.15 | 91.20 | 91.15 | 91.12 |
| Putri et al. (2025) [[20]](06_references.md#ref20) | Dual (Face + Age) | Stratified | 90.85 | 90.90 | 90.85 | 90.82 |
| **Proposed Tri-Domain + SVM (Historical Baseline)** | **Tri (Face + Emotion + Age)** | **Stratified** | **93.70** | **93.72** | **93.70** | **93.69** |
| Proposed Single-Domain + LR | Single (Face) | Subject-Disjoint | 85.28 | 85.35 | 85.28 | 85.27 |
| Proposed Single-Domain + SVM | Single (Face) | Subject-Disjoint | 85.74 | 85.80 | 85.74 | 85.73 |
| Proposed Dual-Domain + LR | Dual (Face + Emotion) | Subject-Disjoint | 87.27 | 87.35 | 87.27 | 87.28 |
| Proposed Dual-Domain + SVM | Dual (Face + Emotion) | Subject-Disjoint | 88.47 | 88.52 | 88.47 | 88.48 |
| **Proposed Tri-Domain + LR** | **Tri (Face + Emotion + Age)** | **Subject-Disjoint** | **88.66** | **88.75** | **88.66** | **88.68** |
| Proposed Tri-Domain + SVM | Tri (Face + Emotion + Age) | Subject-Disjoint | 88.61 | 88.66 | 88.61 | 88.63 |

*(Catatan: Hupont & Fernández (2019) mengevaluasi tugas verifikasi pasangan identitas wajah berbasis kurva ROC/AUC, bukan tugas klasifikasi 6-kelas interseksional).

Penetapan posisi riset ini menegaskan kualifikasi metodologis yang krusial antara kedua protokol evaluasi tersebut. Korpus DemogPairs orisinal yang diperkenalkan oleh Hupont dan Fernández [[25]](06_references.md#ref25) sejatinya dirancang sebagai tolok ukur verifikasi identitas wajah berpasangan dan bukan klasifikasi atribut multi-kelas tertutup. Oleh sebab itu, penyelidikan ini bersama studi literatur terkait memelopori penyediaan baseline komprehensif untuk klasifikasi 6-kelas interseksional pada dataset tersebut. Hasil pada protokol Stratified diklasifikasikan murni sebagai komparasi kontekstual karena pemisahan acak tingkat citra membiarkan identitas subjek tumpang-tindih antara set latih dan uji, ditambah potensi variasi teknik prapemrosesan antarstudi. Perbedaan performa antara baseline historis Stratified (93.70%) dan benchmark primer Subject-Disjoint (88.66%) mengindikasikan adanya optimisme semu akibat kebocoran data identitas. Penerapan protokol ketat Subject-Disjoint 480 subjek latih dan 120 subjek uji held-out menjamin eliminasi kebocoran identitas secara mutlak, sehingga menghasilkan evaluasi performa yang andal dan mencerminkan kapasitas generalisasi sistem biometrik pada dunia nyata.
