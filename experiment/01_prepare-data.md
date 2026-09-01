# Persiapan Data DemogPairs (Race × Gender Classification)

## Ringkasan

Penelitian menggunakan **DemogPairs** (Hupont & Fernández, FG 2019) sebagai satu-satunya sumber citra untuk klasifikasi interseksional **6 kelas** (3 ras × 2 gender). Seluruh pipeline bertumpu pada **satu pembagian data yang identik** untuk 28 eksperimen, sehingga perbandingan antar konfigurasi fitur dan antar classifier bersifat adil dan dapat direproduksi.

| Atribut | Nilai |
|---------|-------|
| **Dataset** | DemogPairs - DOI `10.1109/FG.2019.8756625` |
| **Total citra** | **10.800** (600 identitas × 18 citra) |
| **Kelas** | **6 interseksional**, 1.800 per kelas - seimbang sempurna |
| **Rasio** | 50% Female/Male, 33,3% Asian/Black/White |
| **Split** | Stratified 80/20 → **8.640 Train / 2.160 Test** |
| **Cakupan** | Satu split yang sama untuk 28 eksperimen (7 fitur × 4 classifier) |
| **Lokasi** | `experiment/code/dataset/demogpairs/` |

---

## Komposisi Dataset

Setiap kelas terdiri dari **100 subjek × 18 citra = 1.800 citra**, dengan pemetaan indeks:

| Kelas | Ras | Gender | Subjek | Citra | Indeks |
|---|:---:|:---:|:---:|:---:|:---:|
| Black_Males | Black | Male | 100 | 1.800 | 0 |
| White_Females | White | Female | 100 | 1.800 | 1 |
| Asian_Males | Asian | Male | 100 | 1.800 | 2 |
| White_Males | White | Male | 100 | 1.800 | 3 |
| Black_Females | Black | Female | 100 | 1.800 | 4 |
| Asian_Females | Asian | Female | 100 | 1.800 | 5 |
| **Total** | 3 ras | 2 gender | **600** | **10.800** | 0–5 |

Pemetaan didefinisikan di `utils/constants.py` dan tidak diubah - seluruh notebook, fitur, dan confusion matrix mengacu pada urutan ini.

---

## Struktur Direktori & Metadata

`metadata/` berisi 6 berkas teks (satu per kelas, masing-masing 1.800 baris data + 1 header), `images/` berisi 600 folder identitas dengan 18 JPEG tiap folder (total 10.800).

Setiap berkas metadata berformat whitespace-separated dengan header `db_code image_path`. Kolom `db_code` mencatat provenance (CWF, VGGFace atau VGGFace2 - varian tanpa '2' adalah legacy dan diperlakukan identik) dan tidak dipakai sebagai fitur. Kolom `image_path` menjadi kunci utama untuk mencocokkan citra dengan vektor fitur pada `features/demogpairs_vit-*.pkl`.

---

## Pembagian Dataset - Stratified 80/20

Pembagian menggunakan **Stratified Split** 80/20 dengan seed `42` untuk menjaga proporsi 16,67% per kelas secara eksak di kedua subset. Hasil pembagian:

| Kelas | Total | Train (80%) | Test (20%) |
|---|:---:|:---:|:---:|
| Tiap kelas | 1.800 | 1.440 | 360 |
| **Total** | **10.800** | **8.640** | **2.160** |

Tidak ada validation set terpisah. Validasi dilakukan di dalam subset latih (8.640) melalui 5-Fold Stratified Cross-Validation pada tahap Grid Search with Cross-Validation (GridSearchCV). Subset uji (2.160) bersifat held-out murni dan hanya dipakai sekali pada evaluasi akhir.

Peran subset: **Training (8.640)** untuk pelatihan dan pencarian hyperparameter, **Testing (2.160)** untuk evaluasi akhir (accuracy, macro precision/recall/F1, per-class One-vs-Rest, confusion matrix).

---

## Konsistensi untuk 28 Eksperimen

Penelitian menjalankan **28 eksperimen** dari kombinasi **7 skema fitur** (vit-face, vit-emotion, vit-age, vit-face-age, vit-emotion-age, vit-emotion-face, vit-face-emotion-age) dan **4 classifier** (SVM, Gaussian Naive Bayes, Random Forest, Logistic Regression).

Ke-28 notebook menggunakan pembagian yang identik tanpa re-splitting. Setiap model melihat 8.640 sampel latih yang sama dan dievaluasi pada 2.160 sampel uji yang sama, sehingga perbedaan performa hanya berasal dari representasi fitur atau classifier.

---

## Validasi & Posisi dalam Alur

Pemeriksaan meliputi kelengkapan metadata dan citra, keseimbangan kelas, keselarasan kunci fitur, stratifikasi split, serta determinisme. Tahap persiapan data merupakan fondasi yang menjamin seluruh hasil berasal dari partisi yang identik dan tidak bias.

```
[01] Persiapan Data → 10.800 records → Split 8640/2160 (dipakai ulang di 28 eksperimen)
  → [02] Preprocessing → [03] Feature Extraction (768/1536/2304-d) → [04] Methods → [05] Results
```

---

## Referensi Silang

- `dataset_demogpairs.md` - spesifikasi DemogPairs
- `00_overview.md` - framework & 7 skema fitur
- `03_feature-extraction.md` - ekstraksi ViT
- `04_methods.md` - Grid Search & pipeline
- `utils/dataset.py` dan `utils/constants.py` - implementasi pemuatan dan pemetaan label
