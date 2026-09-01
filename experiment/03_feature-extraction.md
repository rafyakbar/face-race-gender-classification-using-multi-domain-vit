# Ekstraksi Fitur Multi-Domain Vision Transformer & Feature Fusion

## Ringkasan

Penelitian menerapkan strategi ekstraksi **offline (one-pass)**: 10.800 citra DemogPairs dilewatkan sekali melalui tiga Vision Transformer pre-trained yang berbeda domain, vektor 768 dimensi diambil dari token khusus, disimpan sebagai arsip fitur, dan dipakai ulang untuk seluruh 28 eksperimen. Pendekatan ini menjamin reproduksibilitas, efisiensi, dan isolasi variabel antar classifier.

| Aspek | Spesifikasi |
|---|---|
| Ekstraktor | 3 Vision Transformer Base (12 layer, 768 dimensi) |
| Output per ekstraktor | 768 dimensi, float32, token khusus |
| Penyimpanan | `features/demogpairs_vit-{face,emotion,age}.pkl` (≈30 MB per berkas) |
| Dimensi gabungan | 768 (single), 1.536 (dual), 2.304 (tri) |
| Konfigurasi ablation | 7 (3 single + 3 dual + 1 tri) |

---

## Arsitektur Vision Transformer Base

Ketiga model berbagi arsitektur Vision Transformer Base patch16-224: citra 224×224 dibagi menjadi 196 patch 16×16 ditambah 1 token khusus di posisi awal, menghasilkan sequence 197 token yang melewati 12 layer Transformer. Token khusus mengagregasi informasi global seluruh patch dan diambil sebagai deskriptor padat 768 dimensi.

---

## Tiga Ekstraktor Multi-Domain

Ketiga Vision Transformer dipilih karena pre-training pada tugas yang saling melengkapi:

- **ViT-Face** — identitas wajah, menangkap geometri biometrik statis (struktur kraniofasial, proporsi wajah)
- **ViT-Emotion** — emosi wajah, menangkap dinamika mikro otot dan pola afektif
- **ViT-Age** — usia wajah, menangkap tekstur penuaan dan morfologi terkait usia

Ketiga domain bersifat komplementer untuk membedakan ras dan gender. Masing-masing menghasilkan arsip fitur 768 dimensi untuk 10.800 citra yang sama, dengan kunci berupa jalur relatif citra sehingga mudah digabungkan.

---

## Pipeline Ekstraksi Offline

```
Citra DemogPairs 10.800 → AutoImageProcessor 224×224 → 3 Vision Transformer → token khusus 768 dimensi → arsip fitur .pkl → Feature Fusion → matriks fitur [10800, D]
```

Setiap citra diproses secara sekuensial, vektor 768 dimensi disimpan dalam dictionary dengan kunci jalur relatif, dan diserialisasi dengan kompresi. Format arsip memungkinkan pemuatan ulang tanpa inferensi Vision Transformer berulang, sehingga eksperimen klasifikasi dapat berjalan tanpa GPU.

---

## Feature Fusion — Concatenation

Fusi dilakukan dengan concatenation vektor secara berurutan tanpa penjumlahan atau proyeksi, sehingga seluruh informasi asli tiap domain dipertahankan.

| Kategori | Dimensi | Konfigurasi |
|---|:---:|---|
| Single-Domain | 768 | `vit-face`, `vit-emotion`, `vit-age` |
| Dual-Domain | 1.536 | `vit-face-age`, `vit-emotion-age`, `vit-emotion-face` |
| Tri-Domain | 2.304 | `vit-face-emotion-age` (usulan utama) |

Total 7 konfigurasi. Single-domain mengukur kekuatan tiap domain secara terisolasi, dual-domain menguji sinergi dua domain, dan tri-domain menggabungkan ketiganya untuk representasi paling kaya (geometri + dinamika + tekstur).

Setelah fusi, matriks fitur [10800, D] dan label [10800] dibagi menjadi train 8640 dan test 2160 melalui Stratified Split untuk tahap klasifikasi.

---

## Ablation Study

Setiap dari 7 konfigurasi diuji pada 4 classifier (SVM, Gaussian Naive Bayes, Random Forest, Logistic Regression) dengan Grid Search with Cross-Validation yang identik, sehingga perbedaan performa merefleksikan kualitas representasi fitur.

Matriks ablation:

```
              Face  Emotion  Age   Dimensi
vit-face        ●      ○      ○      768
vit-emotion     ○      ●      ○      768
vit-age         ○      ○      ●      768
vit-face-age    ●      ○      ●     1536
vit-emotion-age ○      ●      ●     1536
vit-emotion-face●      ●      ○     1536
vit-face-emotion-age ● ●      ●     2304 ← usulan utama
```

---

## Referensi File

- `code/utils/extraction.py` — implementasi ekstraksi token khusus
- `code/1.1_vit-*_demogpairs.ipynb` — eksekusi ekstraksi per domain
- `code/features/demogpairs_vit-*.pkl` — arsip fitur terkompresi
