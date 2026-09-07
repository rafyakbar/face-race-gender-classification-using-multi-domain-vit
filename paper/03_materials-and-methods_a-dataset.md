## A. Dataset

<a id="fig2"></a>
**Figure 2. Sample Images of the DemogPairs Dataset across Six Intersectional Demographic Subgroups: (a) Asian Females, (b) Asian Males, (c) Black Females, (d) Black Males, (e) White Females, and (f) White Males.**

- (a) Asian Females:
  ![Figure 2(a). Sample Image of Asian Females](images/sample_Asian_Females.jpg)
- (b) Asian Males:
  ![Figure 2(b). Sample Image of Asian Males](images/sample_Asian_Males.jpg)
- (c) Black Females:
  ![Figure 2(c). Sample Image of Black Females](images/sample_Black_Females.jpg)
- (d) Black Males:
  ![Figure 2(d). Sample Image of Black Males](images/sample_Black_Males.jpg)
- (e) White Females:
  ![Figure 2(e). Sample Image of White Females](images/sample_White_Females.jpg)
- (f) White Males:
  ![Figure 2(f). Sample Image of White Males](images/sample_White_Males.jpg)

Dataset yang digunakan dalam penelitian ini adalah DemogPairs, sebuah dataset yang dirancang khusus untuk pengenalan wajah lintas kelompok demografis. Dataset ini memuat total 10,800 citra wajah yang terdistribusi secara seimbang ke dalam enam kelas interseksional. Keenam subkelompok tersebut mencakup kombinasi persilangan dari tiga kelompok ras makro dan dua kelompok gender, yaitu Asian Females, Asian Males, Black Females, Black Males, White Females, dan White Males, dengan kuota tepat 1,800 citra per kelas. Distribusi yang seimbang ini menyediakan kondisi evaluasi yang lebih terkontrol untuk membandingkan performa antarsubkelompok dengan mengurangi pengaruh ketimpangan jumlah sampel. Sampel visual dari keenam subkelompok demografis diilustrasikan pada [Figure 2](#fig2).

<a id="tab1"></a>
**Table I. Dataset Partition and Demographic Subgroup Distribution.**

| Subgroup | Train Set (80%) | Test Set (20%) | Total |
|---|:---:|:---:|:---:|
| **Black_Males** | 1,440 | 360 | 1,800 |
| **White_Females** | 1,440 | 360 | 1,800 |
| **Asian_Males** | 1,440 | 360 | 1,800 |
| **White_Males** | 1,440 | 360 | 1,800 |
| **Black_Females** | 1,440 | 360 | 1,800 |
| **Asian_Females** | 1,440 | 360 | 1,800 |
| **Total** | **8,640** | **2,160** | **10,800** |

Untuk memastikan integritas pengujian empiris, dataset dibagi menggunakan prosedur stratified split 80/20 (80% data latih dan 20% data uji). Pembagian tersebut menghasilkan 8,640 citra latih dengan 1,440 sampel per kelas serta 2,160 citra uji independen dengan 360 sampel per kelas, sebagaimana dirinci pada [Table I](#tab1). Subset uji tersebut diisolasi secara ketat, tidak pernah dilibatkan selama proses pencarian hyperparameter, dan hanya digunakan untuk evaluasi akhir. Pada tahapan standardisasi citra, setiap citra wajah dikonversi ke dalam format 3-channel Red, Green, Blue (RGB), diubah ukurannya ke resolusi 224 × 224 piksel, dan diskalakan intensitas pikselnya dari rentang [0, 255] menjadi [0, 1] agar selaras dengan masukan model transformer.
