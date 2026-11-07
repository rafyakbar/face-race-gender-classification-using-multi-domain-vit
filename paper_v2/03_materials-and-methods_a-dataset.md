## A. Dataset

Eksperimen dalam penelitian ini memanfaatkan dataset DemogPairs yang dikembangkan oleh Hupont dan Fernández [[25]](06_references.md#ref25). Korpus ini memuat total 10.800 citra wajah yang terdistribusi secara seimbang sempurna ke dalam enam subkelompok demografis interseksional (Asian Females, Asian Males, Black Females, Black Males, White Females, dan White Males). Struktur dataset mencakup 600 identitas unik dengan alokasi seragam tepat 100 subjek per subkelompok, di mana setiap subjek diwakili oleh 18 citra wajah yang mencakup variasi pose, ekspresi, dan pencahayaan, menghasilkan 1.800 citra per kelas. Distribusi seimbang ini menyediakan lingkungan evaluasi terkontrol untuk menganalisis disparitas performa klasifikasi antarsubkelompok secara objektif tanpa bias jumlah sampel. Sampel citra disajikan pada [Figure 2](#fig2).

<a id="fig2"></a>
<p align="center">
  <img src="images/sample_Asian_Females.jpg" width="16%" alt="(a) Asian Females" />
  <img src="images/sample_Asian_Males.jpg" width="16%" alt="(b) Asian Males" />
  <img src="images/sample_Black_Females.jpg" width="16%" alt="(c) Black Females" />
  <img src="images/sample_Black_Males.jpg" width="16%" alt="(d) Black Males" />
  <img src="images/sample_White_Females.jpg" width="16%" alt="(e) White Females" />
  <img src="images/sample_White_Males.jpg" width="16%" alt="(f) White Males" />
</p>
<p align="center"><strong>Figure 2. Sample Images of the DemogPairs Dataset across Six Intersectional Demographic Subgroups: (a) Asian Females, (b) Asian Males, (c) Black Females, (d) Black Males, (e) White Females, and (f) White Males.</strong></p>

Untuk menjamin integritas evaluasi dan mencegah kebocoran identitas (0% identity leakage), penelitian ini menerapkan protokol Strict Subject-Disjoint Partitioning. Sebanyak 600 identitas unik dipisahkan secara deterministik menjadi 480 subjek latih (8.640 citra, 80%) dan 120 subjek uji held-out (2.160 citra, 20%) yang terbagi rata atas 80 subjek latih dan 20 subjek uji per subkelompok, sebagaimana dirinci pada [Table I](#tab1). Subjek uji terisolasi penuh dari pelatihan dan validasi silang 5-Fold StratifiedGroupKFold. Karena citra DemogPairs telah berformat pangkasan wajah terpusat (pre-cropped), prapemrosesan tidak memerlukan deteksi wajah tambahan, melainkan langsung dikonversi ke format 3-channel Red, Green, Blue (RGB), diubah resolusinya menjadi 224 × 224 piksel, dan dinormalisasi kanal dengan mean serta deviasi standar [0.5, 0.5, 0.5].

<a id="tab1"></a>
**Table I. DemogPairs Dataset Partition and Subject-Disjoint Demographic Subgroup Distribution.**

| Subkelompok Demografis | Subjek Latih | Citra Latih | Subjek Uji (Held-Out) | Citra Uji (Held-Out) | Total Subjek | Total Citra |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Asian Females | 80 | 1.440 | 20 | 360 | 100 | 1.800 |
| Asian Males | 80 | 1.440 | 20 | 360 | 100 | 1.800 |
| Black Females | 80 | 1.440 | 20 | 360 | 100 | 1.800 |
| Black Males | 80 | 1.440 | 20 | 360 | 100 | 1.800 |
| White Females | 80 | 1.440 | 20 | 360 | 100 | 1.800 |
| White Males | 80 | 1.440 | 20 | 360 | 100 | 1.800 |
| **Total** | **480** | **8.640** | **120** | **2.160** | **600** | **10.800** |
