# Archive / Legacy Experiments (Subject-Overlap & Data Leakage Baseline)

Direktori ini berisi seluruh artefak eksperimen versi awal (sebelum revisi naskah IEEE Access `Access-2026-50857`).

---

## 📌 Tujuan Penyimpanan Arsip

Arsip ini sengaja dipertahankan dan didokumentasikan secara transparan untuk mendukung **analisis komparatif ablasi kebocoran data (*Data Leakage and Generalization Comparative Analysis*)** dalam naskah revisi IEEE Access (khususnya menanggapi masukan **Reviewer 2 Comment #2**).

1. **Eksperimen Legacy (Arsip Ini):**
   - Menggunakan partisi acak biasa (`train_test_split(..., random_state=42)`).
   - Memiliki **kebocoran identitas subjek sebesar 100%** (seluruh 593/593 subjek uji dan 2.160 citra uji hadir dalam data latih dengan pose/kondisi berbeda).
   - Menghasilkan akurasi semu yang sangat tinggi (*over-optimistic performance*), dipimpin oleh SVM Tri-Domain (**93.70%** / Macro F1: **0.9369**).
2. **Eksperimen Baru (Di Direktori Induk `experiment/code/`):**
   - Menggunakan partisi **Subject-Disjoint** murni (`split_demogpairs_subject_disjoint`).
   - Memiliki **0.00% kebocoran identitas** (120 subjek uji held-out sepenuhnya terisolasi dan belum pernah dilihat oleh model selama pelatihan).
   - Menghasilkan akurasi generalisasi sejati (*true out-of-subject generalization*):
     - Logistic Regression Tri-Domain: **88.66%** (Macro F1: **0.8868**)
     - SVM Tri-Domain: **88.61%** (Macro F1: **0.8863**)

---

## 📂 Struktur Direktori Arsip

- **`notebook_old/`**: Salinan 35 file Jupyter Notebook versi lama (termasuk [`0.0_data_leakage_audit.ipynb`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/archive/notebook_old/0.0_data_leakage_audit.ipynb) yang membuktikan secara empiris perbedaan kebocoran data antara partisi lama dan baru).
- **`md_old/`**: Salinan 35 hasil ekspor Markdown dari notebook lama beserta grafik confusion matrix historis.
- **`results_old/`**: File metrik format JSON (28 file) hasil evaluasi held-out test set versi lama.
- **`models_old/`**: Bobot model terlatih (`.pkl`) dari 28 konfigurasi model versi lama.
