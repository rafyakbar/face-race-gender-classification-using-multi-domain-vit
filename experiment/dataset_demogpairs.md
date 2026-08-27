# Dataset DemogPairs — Rangkuman & Spesifikasi

## 1. Informasi Paper Asli

* **Judul:** *DemogPairs: Quantifying the Impact of Demographic Imbalance in Deep Face Recognition*
* **Penulis:** Isabelle Hupont dan Carles Fernández
* **Publikasi:** 2019 14th IEEE International Conference on Automatic Face & Gesture Recognition (FG 2019)
* **DOI:** `10.1109/FG.2019.8756625`
* **Fokus Paper:** Menguantifikasi ketidakseimbangan demografis pada dataset wajah publik serta memperkenalkan dataset DemogPairs yang memiliki distribusi seimbang antar-kelompok etnis dan gender.

---

## 2. Masalah Ketidakseimbangan pada Dataset Publik

Sebagian besar dataset wajah publik populer mengalami bias etnis dan gender yang parah:

| Dataset | Female (%) | Male (%) | Asian (%) | Black (%) | White (%) |
|---------|:----------:|:--------:|:---------:|:---------:|:---------:|
| CWF | 41,1% | 58,9% | 2,3% | 8,6% | **89,1%** |
| LFW | 25,8% | 74,2% | 6,2% | 8,5% | **85,3%** |
| VGGFace | 49,4% | 50,6% | 2,2% | 9,4% | **88,4%** |
| VGGFace2 | 40,7% | 59,3% | 6,9% | 9,2% | **83,9%** |
| IJB-B | 46,2% | 53,8% | 15,6% | 10,3% | **74,1%** |
| **DemogPairs** | **50,0%** | **50,0%** | **33,3%** | **33,3%** | **33,3%** |

* Dominasi etnis White mencapai 74%–89% pada dataset publik.
* Ketidakseimbangan jumlah citra antar-identitas mencapai rasio hingga 500:1.

---

## 3. Komposisi Dataset DemogPairs

DemogPairs disusun dengan keseimbangan sempurna pada tingkat identitas, gender, dan etnis:

* **Total Citra:** 10.800 citra wajah bersih (telah disaring dari citra berkualitas buruk/rusak).
* **Total Subjek:** 600 identitas unik (18 citra per subjek).
* **6 Kelompok Demografis:**
  1. `Asian_Females`: 100 subjek (1.800 citra)
  2. `Asian_Males`: 100 subjek (1.800 citra)
  3. `Black_Females`: 100 subjek (1.800 citra)
  4. `Black_Males`: 100 subjek (1.800 citra)
  5. `White_Females`: 100 subjek (1.800 citra)
  6. `White_Males`: 100 subjek (1.800 citra)
* **Proporsi:** 50% Female / 50% Male | 33,3% Asian / 33,3% Black / 33,3% White.

---

## 4. Penggunaan Dataset dalam Penelitian Ini

Pada penelitian ini, dataset **DemogPairs** digunakan untuk tugas **klasifikasi multi-atribut ras dan gender secara terpadu (*6-class intersectional classification*)**:

* **Jumlah Data:** 10.800 citra wajah.
* **Target Kelas (6 Indeks):**
  * `0: Black_Males` (1.800 citra)
  * `1: White_Females` (1.800 citra)
  * `2: Asian_Males` (1.800 citra)
  * `3: White_Males` (1.800 citra)
  * `4: Black_Females` (1.800 citra)
  * `5: Asian_Females` (1.800 citra)
* **Pembagian Data:** Stratified Split 80/20 (8.640 Train / 2.160 Test).
* **Fokus Penelitian:** Menggabungkan representasi multi-domain dari Vision Transformer (Identitas, Emosi, Usia) untuk klasifikasi 6 kelas ras dan gender secara akurat dan seimbang.
