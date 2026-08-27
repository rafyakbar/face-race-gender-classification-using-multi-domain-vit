# Hasil Eksperimen — Perbandingan, Ablation Study, dan Analisis Kesetaraan Demografis

## Ringkasan

Dokumen ini menyajikan hasil evaluasi komparatif dari **7 konfigurasi eksperimen** klasifikasi multi-atribut ras dan gender pada dataset DemogPairs. Eksperimen dirancang sebagai *Ablation Study* komprehensif untuk mengevaluasi kontribusi representasi fitur *Single-Domain*, *Dual-Domain Feature Fusion*, dan *Tri-Domain Feature Fusion* (usulan utama).

Seluruh model dievaluasi pada *held-out test set* independen berukuran **2.160 sampel citra** (360 citra per kelas demografis) menggunakan metrik global (*Accuracy, Macro Precision, Macro Recall, Macro F1-Score*), metrik *One-vs-Rest* per-kelas, matriks konfusi (*confusion matrix*), serta analisis kesetaraan demografis (*demographic parity & fairness*).

---

## Rekapitulasi Hasil 7 Konfigurasi Eksperimen

Tabel di bawah merangkum performa seluruh model eksperimen yang diurutkan dari akurasi terendah ke tertinggi:

| No | Konfigurasi Fitur | Tipe Fitur | Dimensi | Classifier | Parameter Terbaik (GridSearchCV) | Akurasi | Precision | Recall | F1-Score | Waktu Search (5-Fold CV) |
|:--:|-------------------|------------|:-------:|:----------:|----------------------------------|:-------:|:---------:|:------:|:--------:|:------------------------:|
| 1 | `vit-age` | Single | 768 | SVM | C=10, rbf, scale, deg=2, pca=None, scaler=None | **0,8764** | 0,8767 | 0,8764 | 0,8765 | 4 jam 15 menit (15.309 s) |
| 2 | `vit-emotion` | Single | 768 | SVM | C=10, rbf, scale, deg=2, pca=None, scaler=None | **0,9019** | 0,9020 | 0,9019 | 0,9017 | 3 jam 56 menit (14.209 s) |
| 3 | `vit-face` | Single | 768 | SVM | C=10, rbf, scale, deg=2, pca=None, scaler=None | **0,9083** | 0,9084 | 0,9083 | 0,9083 | 2 jam 51 menit (10.276 s) |
| 4 | `vit-emotion-age` | Dual | 1.536 | SVM | C=10, rbf, scale, deg=2, pca=None, scaler=None | **0,9208** | 0,9210 | 0,9208 | 0,9209 | 7 jam 22 menit (26.559 s) |
| 5 | `vit-face-age` | Dual | 1.536 | SVM | C=10, poly, scale, deg=2, pca=None, scaler=None | **0,9255** | 0,9254 | 0,9255 | 0,9254 | 6 jam 09 menit (22.197 s) |
| 6 | `vit-emotion-face` | Dual | 1.536 | SVM | C=10, rbf, scale, deg=2, pca=None, MinMaxScaler | **0,9329** | 0,9333 | 0,9329 | 0,9329 | 6 jam 14 menit (22.467 s) |
| 7 | **`vit-face-emotion-age`** | **Tri-Domain** | **2.304** | **SVM** | **C=10, poly, scale, deg=2, pca=None, scaler=None** | **0,9370** | **0,9372** | **0,9370** | **0,9369** | **11 jam 50 menit (42.626 s)** |

---

## 1. Analisis Performa Fitur Tunggal (*Single-Domain Baseline*)

Pada pengujian domain tunggal (768 dimensi):
* **ViT-Face (Identitas):** Menghasilkan performa tertinggi di antara model tunggal (**90,83%** akurasi). Hal ini membuktikan bahwa struktur biometrik wajah merupakan prediktor demografis paling dominan.
* **ViT-Emotion (Ekspresi):** Mencapai akurasi **90,19%**, hanya terpaut 0,64% dari fitur identitas. Hal ini menunjukkan bahwa representasi afek dan dinamika otot wajah juga menyematkan informasi bentuk wajah yang sangat kaya.
* **ViT-Age (Usia):** Mencapai akurasi **87,64%**. Meskipun fitur penuaan tetap mampu membedakan ras dan gender di atas peluang acak (16,67%), fitur ini memiliki keterbatasan terbesar bila berdiri sendiri.

---

## 2. Analisis Penggabungan 2 Fitur (*Dual-Domain Feature Fusion*)

Penggabungan dua domain fitur secara konsisten meningkatkan performa di atas model tunggal terbaik:
1. **`vit-emotion-age` (1.536-d):** Akurasi meningkat menjadi **92,08%** (+1,89% dibanding emosi tunggal, +4,44% dibanding usia tunggal).
2. **`vit-face-age` (1.536-d):** Akurasi meningkat menjadi **92,55%** (+1,72% dibanding wajah tunggal, +4,91% dibanding usia tunggal).
3. **`vit-emotion-face` (1.536-d):** Akurasi mencapai **93,29%** (+2,46% dibanding wajah tunggal, +3,10% dibanding emosi tunggal).

**Temuan Kunci:** Penggabungan fitur identitas dan emosi (`vit-emotion-face`) merupakan kombinasi dual-domain terbaik karena menyatukan struktur statis biometrik dengan artikulasi dinamis mikro-wajah.

---

## 3. Keunggulan Model Usulan (*Tri-Domain Cross-Domain Feature Fusion*)

Model usulan utama yang mengintegrasikan ketiga domain representasi (**ViT-Face + ViT-Emotion + ViT-Age**, 2.304 dimensi) menghasilkan performa tertinggi pada seluruh metrik evaluasi:

* **Akurasi Pengujian:** **93,70%** (2.024 dari 2.160 sampel diprediksi tepat).
* **Macro Precision:** **93,72%**.
* **Macro Recall:** **93,70%**.
* **Macro F1-Score:** **93,69%**.
* **5-Fold Cross-Validation Accuracy:** **92,65%** (± 0,83%) dengan skor per-fold: `[94,04%, 93,00%, 91,67%, 92,01%, 92,53%]`.
* **Area Under ROC Curve (ROC-AUC OvR):** **0,9948** (mendekati klasifikasi sempurna).

Peningkatan dari model tunggal terbaik (`vit-face`, 90,83%) ke model tripel (`vit-face-emotion-age`, 93,70%) adalah sebesar **+2,87%** (penurunan kesalahan relatif sebesar **31,29%**).

---

## 4. Evaluasi Rinci Per-Kelas Model Usulan (`vit-face-emotion-age`)

Tabel di bawah memperlihatkan metrik *One-vs-Rest* pada masing-masing dari 6 kelas demografis:

| Label Kelas | Indeks | Ras | Gender | Support | TP | FP | FN | TN | OvR Accuracy | Precision | Recall | F1-Score |
|-------------|:------:|-----|:------:|:-------:|:--:|:--:|:--:|:--:|:------------:|:---------:|:------:|:--------:|
| **Black_Males** | 0 | Black | Pria | 360 | 339 | 16 | 21 | 1.784 | **98,29%** | **0,9549** | **0,9417** | **0,9483** |
| **White_Females** | 1 | White | Wanita | 360 | 341 | 28 | 19 | 1.772 | **97,82%** | **0,9241** | **0,9472** | **0,9355** |
| **Asian_Males** | 2 | Asian | Pria | 360 | 340 | 28 | 20 | 1.772 | **97,78%** | **0,9239** | **0,9444** | **0,9341** |
| **White_Males** | 3 | White | Pria | 360 | 349 | 17 | 11 | 1.783 | **98,70%** | **0,9536** | **0,9694** | **0,9614** |
| **Black_Females** | 4 | Black | Wanita | 360 | 322 | 20 | 38 | 1.780 | **97,31%** | **0,9415** | **0,8944** | **0,9174** |
| **Asian_Females** | 5 | Asian | Wanita | 360 | 333 | 27 | 27 | 1.773 | **97,50%** | **0,9250** | **0,9250** | **0,9250** |
| **Rata-rata (Macro)** | — | — | — | **2.160** | — | — | — | — | **97,90%** | **0,9372** | **0,9370** | **0,9369** |

---

## 5. Matriks Konfusi (*Confusion Matrix*) Model Usulan

Matriks konfusi 6×6 pada data uji (Baris = *True Label*, Kolom = *Predicted Label*):

| True \ Pred | Black_Males (0) | White_Females (1) | Asian_Males (2) | White_Males (3) | Black_Females (4) | Asian_Females (5) | Total True |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Black_Males (0)** | **339** | 0 | 9 | 4 | 8 | 0 | 360 |
| **White_Females (1)** | 1 | **341** | 0 | 5 | 4 | 9 | 360 |
| **Asian_Males (2)** | 6 | 0 | **340** | 4 | 2 | 8 | 360 |
| **White_Males (3)** | 4 | 2 | 4 | **349** | 0 | 1 | 360 |
| **Black_Females (4)** | 5 | 16 | 6 | 2 | **322** | 9 | 360 |
| **Asian_Females (5)** | 0 | 10 | 9 | 2 | 6 | **333** | 360 |
| **Total Pred** | **355** | **369** | **368** | **366** | **342** | **360** | **2.160** |

---

## 6. Analisis Keadilan & Kesetaraan Demografis (*Fairness Insights*)

1. **Konsistensi Antar-Kelompok Demografis:**
   * Akurasi *One-vs-Rest* pada seluruh 6 kelompok berada dalam rentang yang sangat ketat dan konsisten, yaitu antara **97,31%** (Black Females) hingga **98,70%** (White Males).
   * Nilai F1-Score seluruh kelas berada di atas **0,91**, menunjukkan model tidak mengorbankan kelompok minoritas tertentu.
2. **Pola Kesalahan Interseksional (*Intersectional Misclassification*):**
   * Kesalahan prediksi gender di dalam ras yang sama sangat jarang terjadi (misal: pria berkulit putih hampir tidak pernah diprediksi sebagai wanita berkulit putih; hanya 2 dari 360).
   * Mayoritas kesalahan terjadi pada batas fenotipe ras pada gender yang sama (misalnya antara `Black_Females` dan `White_Females` sebanyak 16 kasus, atau `Asian_Females` dan `White_Females` sebanyak 10 kasus), yang umumnya dipengaruhi oleh variasi pencahayaan (*lighting*), sudut pose, dan riasan (*makeup*).
3. **Peningkatan Kesetaraan dari Single ke Tri-Domain:**
   * Pada model `vit-age`, recall untuk `Black_Females` hanya **83,61%** dan `Asian_Females` **86,94%**.
   * Pada model `vit-face-emotion-age`, recall `Black_Females` melonjak menjadi **89,44%** dan `Asian_Females` menjadi **92,50%**, membuktikan bahwa fusi fitur multi-domain secara signifikan mengurangi disparitas performa antar-subkelompok demografis.
