# Skrip Eksekusi & Runner Otomatisasi Eksperimen

Direktori ini berisi skrip-skrip otomatisasi untuk mengeksekusi antrean notebook eksperimen klasifikasi Multi-ViT secara *headless* (menggunakan `jupyter nbconvert` atau `papermill`) di lingkungan conda `torch-gpu`.

---

## 📜 Daftar Skrip

1. **`auto_run_experiments.py`**:
   - Skrip orkestrator antrean utama untuk menjalankan 28 notebook eksperimen secara berurutan.
   - Mengelola pemantauan log berkala, pencatatan (*logging*) durasi eksekusi per model, dan *graceful fallback*.
2. **`run_remaining_queue.py`**:
   - Skrip antrean khusus untuk menyelesaikan model SVM komputasi berat (2.1.5, 2.1.6, 2.1.7).
   - Dilengkapi *Intel P-core CPU Affinity lock* dan *priority elevation* untuk mencegah pelambatan daya (EcoQoS) pada CPU Intel Hybrid.
3. **`run_gnb_queue.py`**:
   - Skrip antrean cepat untuk kelompok model Gaussian Naive Bayes (2.2.1 s.d. 2.2.7).
4. **`run_experiments.bat`** & **`run_gnb.bat`**:
   - Berkas batch Windows untuk aktivasi lingkungan conda `torch-gpu` secara instan dan memulai antrean eksekusi dengan klik ganda.

---

## 🚀 Cara Menjalankan

Dari direktori `experiment/code/` atau dari direktori `experiment/code/scripts/`:

```bash
# Menggunakan python langsung (pastikan lingkungan torch-gpu aktif)
python scripts/auto_run_experiments.py

# Atau menggunakan skrip batch di Windows
scripts\run_experiments.bat
```
