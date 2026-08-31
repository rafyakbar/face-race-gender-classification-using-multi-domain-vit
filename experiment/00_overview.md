# Framework Penelitian — Multi-Domain ViT + 4 Classifier untuk Klasifikasi Ras & Gender

## Ringkasan

Penelitian mengklasifikasikan **6 kelas interseksional** (3 Ras × 2 Gender: Asian/Black/White × Female/Male) pada citra wajah dengan **Cross-Domain Feature Fusion**. Tiga Vision Transformer sebagai ekstraktor fitur offline:

- **ViT-Face** — 768 dimensi
- **ViT-Emotion** — 768 dimensi
- **ViT-Age** — 768 dimensi

Konkatenasi tri-domain = **2.304 dimensi**. Dataset **DemogPairs** — **10.800 citra** (600 identitas ×18, 1.800 per kelas, seimbang), split **80/20 stratified** (8.640 latih / 2.160 uji, 360 per kelas).

**28 eksperimen** = 7 konfigurasi fitur × 4 classifier (GridSearchCV 5-Fold):

| Classifier | Kombinasi | Tri-domain Akurasi | F1 |
|:---|:---:|:---:|:---:|
| **SVM** | 288 | **93,70%** | 0,9369 |
| **Logistic Regression** | 270 | **92,73%** | 0,9273 |
| **Random Forest** | 288 | 86,20% | 0,8682 |
| **Gaussian NB** | 240 | **85,05%** | 0,8505 |

---

## Alur Penelitian

```
DemogPairs 10.800 (6×1.800) → Normalisasi citra 224×224 → 3 ViT → fitur 768 dimensi → arsip fitur
  → Fusi fitur 768 / 1.536 / 2.304 dimensi (7 skema) → Split 8640/2160 → Pipeline penskalaan dan reduksi dimensi → Klasifikasi
  → GridSearchCV 5-Fold (1.086 kombinasi, 5.430 fitting per fitur) → evaluasi 2.160 uji → metrik global + per kelas + matriks konfusi
```

7 skema konfigurasi fitur:
- `vit-face` — 768 dimensi (single-domain)
- `vit-emotion` — 768 dimensi (single-domain)
- `vit-age` — 768 dimensi (single-domain)
- `vit-face-age` — 1.536 dimensi (dual-domain)
- `vit-emotion-age` — 1.536 dimensi (dual-domain)
- `vit-emotion-face` — 1.536 dimensi (dual-domain)
- `vit-face-emotion-age` — 2.304 dimensi (tri-domain, usulan utama)

---

## Arsitektur & Fusi Fitur

- Vision Transformer Base: citra 224×224 → 196 patch 16×16 + 1 token khusus = 197 token, 12 layer.
- Ekstraksi offline: setiap citra menghasilkan vektor 768 dimensi dari token khusus, disimpan sebagai arsip fitur.
- Fusi: penggabungan vektor per citra berdasarkan kunci jalur gambar, menghasilkan varian 768, 1.536, dan 2.304 dimensi sesuai skema.

---

## Pipeline Klasifikasi

```
Fitur 768/1.536/2.304 dimensi → Penskalaan → Reduksi dimensi → Klasifikasi → Kelas 0–5
```

Pipeline anti-kebocoran data (penskalaan dan reduksi hanya dipelajari dari data latih tiap fold), evaluasi dengan validasi silang 5-Fold dan pemeringkatan berdasarkan akurasi. Evaluasi per kelas memakai akurasi One-vs-Rest dan matriks konfusi.

---

## Hasil

- Terbaik: **SVM tri-domain 93,70%**, disusul Logistic Regression 92,73%, Random Forest 86,20%, Gaussian NB 85,05%.
- Papan peringkat 28 baris tersedia pada analisis komparatif.

---

## Struktur Dokumen

- `00_overview.md` — ringkasan ini
- `01_prepare-data.md` — dataset & split
- `02_preprocessing.md` — dua tingkat preprocessing
- `03_feature-extraction.md` — ekstraksi ViT & fusi
- `04_methods.md` — empat classifier & optimasi
- `05_results.md` — 28 eksperimen & fairness
- `dataset_demogpairs.md` — spesifikasi DemogPairs
- `code/` — notebook, utilitas, arsip markdown, gambar, dan hasil

---

## Referensi

Hupont & Fernández, *DemogPairs: Quantifying the Impact of Demographic Imbalance in Deep Face Recognition*, FG 2019, DOI `10.1109/FG.2019.8756625`.
