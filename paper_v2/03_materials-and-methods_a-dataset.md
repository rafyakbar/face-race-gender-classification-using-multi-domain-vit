## A. Dataset

<a id="fig2"></a>
![Figure 2. Sample Images of the DemogPairs Dataset across Six Intersectional Demographic Subgroups: (a) Asian Females, (b) Asian Males, (c) Black Females, (d) Black Males, (e) White Females, and (f) White Males.](images/sample_demogpairs_v2.png)
<p align="center"><strong>Figure 2. Sample Images of the DemogPairs Dataset across Six Intersectional Demographic Subgroups: (a) Asian Females, (b) Asian Males, (c) Black Females, (d) Black Males, (e) White Females, and (f) White Males.</strong></p>

Eksperimen dalam penelitian ini memanfaatkan dataset DemogPairs [[25]](06_references.md#ref25) yang dirancang sebagai tolok ukur pengujian biometrik verifikasi wajah untuk mengevaluasi dampak ketimpangan demografis secara sistematis. Korpus ini memuat total 10.800 citra wajah yang terdistribusi seimbang ke dalam enam subkelompok demografis interseksional, mencakup persilangan antara tiga ras makro (Asian, Black, White) dan dua kategori gender biner (Female, Male). Struktur dataset mencakup 600 identitas unik, dengan alokasi seragam 100 individu per subkelompok di mana setiap identitas diwakili 18 citra terkontrol bervariasi pose, ekspresi, dan pencahayaan. Distribusi seimbang ini menyediakan lingkungan evaluasi terkontrol demi menganalisis disparitas performa antarsubkelompok secara objektif tanpa distorsi jumlah sampel. Sampel citra disajikan pada [Figure 2](#fig2).

<a id="tab1"></a>
**Table I. DemogPairs Dataset Partition and Subject-Disjoint Demographic Subgroup Distribution.**

| Demographic Subgroup | Train Subjects | Train Images | Test Subjects (Held-Out) | Test Images (Held-Out) | Total Subjects | Total Images |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Asian Females | 80 | 1,440 | 20 | 360 | 100 | 1,800 |
| Asian Males | 80 | 1,440 | 20 | 360 | 100 | 1,800 |
| Black Females | 80 | 1,440 | 20 | 360 | 100 | 1,800 |
| Black Males | 80 | 1,440 | 20 | 360 | 100 | 1,800 |
| White Females | 80 | 1,440 | 20 | 360 | 100 | 1,800 |
| White Males | 80 | 1,440 | 20 | 360 | 100 | 1,800 |
| **Total** | **480** | **8,640** | **120** | **2,160** | **600** | **10,800** |

Untuk menjamin integritas evaluasi dan mengeliminasi risiko kebocoran identitas secara mutlak (0% kebocoran), penelitian ini menerapkan protokol Strict Subject-Disjoint Partitioning. Sebanyak 600 identitas unik dipisahkan secara deterministik menjadi 480 subjek latih (8.640 citra) dan 120 subjek uji held-out (2.160 citra). Pembagian terstratifikasi ini menghasilkan alokasi seimbang berupa 80 subjek latih dan 20 subjek uji per subkelompok sebagaimana dirinci pada [Table I](#tab1). Subjek uji bersifat independen dan tidak pernah dilibatkan selama pelatihan maupun penalaan hyperparameter. Citra wajah terpusat dikonversi ke format 3-channel Red, Green, Blue (RGB) serta diubah resolusinya menjadi 224 × 224 piksel. Intensitas piksel dinormalisasi secara channel-wise mengikuti konfigurasi pra-latih masing-masing checkpoint ViT tanpa penambahan augmentasi sintetis.
