# Preprocessing Pipeline — Dua Tingkat Normalisasi untuk Multi-Domain ViT

## Ringkasan

Preprocessing dirancang dalam dua tingkat yang terpisah untuk menjaga konsistensi skala dan distribusi data:

| Tingkat | Tahap | Komponen | Sifat |
|---------|-------|----------|-------|
| **Tingkat 1 — Image-Level** | Normalisasi citra mentah | AutoImageProcessor (224×224, mean/std spesifik model) | Sekali, offline saat ekstraksi ViT (10.800 citra) |
| **Tingkat 2 — Feature-Level** | Transformasi vektor fitur | Scaler dan Principal Component Analysis (PCA) di dalam Pipeline | Di dalam Cross-Validation, fitting hanya pada data latih |

Pemisahan ini memastikan pipeline dirancang untuk mencegah kebocoran data, di mana penskalaan dan reduksi dimensi hanya dipelajari dari data latih pada setiap fold.

---

## 1. Tingkat Citra (Image-Level)

Setiap citra DemogPairs distandardisasi ke format identik **224×224 piksel, 3 channel RGB** agar sesuai dengan patch embedding Vision Transformer Base (196 patch 16×16 + 1 token khusus = 197 token).

Proses dilakukan oleh **AutoImageProcessor** dari Hugging Face Transformers, yang memuat konfigurasi mean dan standard deviation spesifik untuk setiap checkpoint secara otomatis tanpa nilai hard-coded. Tahapannya meliputi pemuatan citra, konversi ke RGB, resizing dengan interpolasi bicubic ke 224×224, rescaling piksel ke rentang [0,1], serta standardisasi channel-wise.

Tiga checkpoint yang digunakan masing-masing memiliki processor yang konsisten dengan modelnya:

- **ViT-Face** — identitas wajah
- **ViT-Emotion** — emosi wajah
- **ViT-Age** — estimasi usia wajah

Hasil akhir tingkat citra diteruskan ke Vision Transformer Encoder untuk menghasilkan vektor 768 dimensi dari token khusus. Vektor inilah yang disimpan sebagai arsip fitur dan menjadi input bagi tingkat selanjutnya.

---

## 2. Tingkat Vektor Fitur (Feature-Level)

Setelah ekstraksi offline, setiap citra direpresentasikan sebagai vektor numerik berdimensi 768 untuk single-domain, 1.536 untuk dual-domain, dan 2.304 untuk tri-domain. Sebelum klasifikasi, vektor melalui transformasi opsional yang dioptimasi melalui Grid Search with Cross-Validation (GridSearchCV) di dalam Pipeline.

Pipeline tersusun sebagai **Scaler → PCA → Classifier**, dengan urutan yang krusial: penskalaan harus mendahului reduksi dimensi karena PCA sensitif terhadap skala fitur.

**Penskalaan fitur** membandingkan dua opsi: tanpa penskalaan yang mempertahankan distribusi asli embedding, dan MinMaxScaler yang mentransformasi setiap dimensi ke rentang [0,1] berdasarkan min-max data latih pada fold tersebut.

**Reduksi dimensi** membandingkan tiga opsi berbasis rasio varians kumulatif: tanpa PCA yang mempertahankan seluruh dimensi, PCA 50% yang mempertahankan komponen hingga 50% total varians, dan PCA 75% yang mempertahankan hingga 75% total varians. Nilai tersebut adalah rasio varians, bukan jumlah komponen tetap.

**Temuan optimasi:** pada seluruh model terbaik, PCA tidak terpilih, yang menunjukkan reduksi linear menghilangkan detail halus yang relevan. Penskalaan juga tidak memberi keuntungan pada 6 dari 7 konfigurasi, karena embedding Vision Transformer telah memiliki skala yang teratur berkat Layer Normalization.

---

## 3. Scoring, Paralelisasi, dan Evaluasi

Seluruh 28 eksperimen menggunakan **empat metrik scoring yang identik** pada GridSearchCV: accuracy, F1-macro, precision-macro, dan recall-macro, dengan pemeringkatan berdasarkan accuracy. Metrik ROC-AUC One-vs-Rest sengaja tidak digunakan karena memerlukan probabilitas yang tidak konsisten lintas classifier dan memperlambat pencarian.

Paralelisasi menggunakan **60% CPU logis** dengan backend threading untuk kompatibilitas pada Windows.

Evaluasi akhir menghasilkan metrik global makro serta metrik per kelas berbasis **One-vs-Rest Accuracy** yang dihitung sebagai (TP+TN)/Total dari confusion matrix 6×6. Confusion matrix disajikan dalam dua bentuk: heatmap PNG dan text array berlabel untuk keterbacaan, dengan pemetaan label 0=Black_Males, 1=White_Females, 2=Asian_Males, 3=White_Males, 4=Black_Females, 5=Asian_Females yang selaras dengan urutan target.

---

## 4. Ringkasan Alur

```
DemogPairs 10.800 (6×1.800) → Normalisasi citra 224×224 → 3 Vision Transformer → vektor 768 dimensi → arsip fitur
  → Fusi fitur 768 / 1.536 / 2.304 dimensi (7 skema) → Split 8640/2160 → Pipeline penskalaan dan reduksi dimensi → Klasifikasi
  → Grid Search with 5-Fold Cross-Validation → evaluasi 2.160 uji → metrik global + per kelas + matriks konfusi
```

Alur ini menjamin seluruh transformasi dipelajari hanya dari data latih dan diterapkan ke data uji tanpa kebocoran, sehingga perbandingan antar konfigurasi fitur dan antar classifier bersifat adil.

---

## Referensi File

- `code/utils/extraction.py` — logika tingkat citra
- `code/utils/evaluation.py` — metrik One-vs-Rest, confusion matrix, dan penyimpanan hasil
- `code/utils/display.py` — helper tampilan tabel dan heading
