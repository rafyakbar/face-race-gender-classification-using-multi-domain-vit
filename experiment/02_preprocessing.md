# Preprocessing Citra - Standarisasi, Resize, dan Normalisasi untuk Vision Transformer

## Ringkasan

Tahap prapemrosesan citra (*image preprocessing*) bertujuan menstandardisasi seluruh **10.800 citra wajah** dari dataset DemogPairs ke format tensor yang seragam sebelum diumpankan ke tiga model Vision Transformer (ViT-Base). Proses ini dilakukan tepat **satu kali secara *offline*** menggunakan konfigurasi resmi dari `AutoImageProcessor` (Hugging Face Transformers) untuk menjamin reproduksibilitas absolut.

Untuk menjawab catatan kritis **IEEE Access Reviewer 2 (Comment #3: Preprocessing and Reproducibility)**, dokumen ini merinci secara eksplisit versi checkpoint, pustaka pemroses citra, interpolasi spasial, serta parameter normalisasi per kanal warna (*channel-wise mean & standard deviation*).

Pipa prapemrosesan ini bersifat **invarian dan dipakai bersama secara identik** oleh kedua protokol pengujian (**Subject-Disjoint** maupun **Subject-Overlap**), memastikan bahwa perbedaan performa antar-protokol murni disebabkan oleh sifat partisi identitas data, bukan variabilitas prapemrosesan.

| Parameter Preprocessing | Spesifikasi Teknis | Keterangan & Rujukan |
|---|---|---|
| **Pustaka Pemroses** | `transformers.AutoImageProcessor` | Memuat konfigurasi resmi checkpoint |
| **Resolusi Target** | **224 × 224 piksel** | Standar ViT-Base (`patch16-224`) |
| **Metode Interpolasi** | **Bicubic Interpolation** (`PIL.Image.BICUBIC`) | Menjaga kehalusan tekstur mikro wajah |
| **Format Warna** | **RGB 3-Channel** | Konversi otomatis mode RGBA / Grayscale |
| **Penskalaan Nilai Piksel** | Rescale $[0, 255] \to [0, 1]$ (faktor $1/255.0$) | Konversi awal sebelum standardisasi |
| **Ekstraksi Token** | Token khusus `[CLS]` (posisi indeks 0) | Representasi global 768 dimensi |
| **Paritas Antar-Benchmark** | 100% Identik untuk kedua protokol | Menghilangkan variabel perancu |

---

## Alur Prapemrosesan Citra

Setiap citra mentah dari folder `dataset/demogpairs/images/` diproses dengan alur deterministik sebagai berikut:

```
Citra Mentah (.jpg) ──> Verifikasi Mode & Konversi ke RGB ──> Resizing Bicubic ke 224×224 
  ──> Rescaling [0, 1] ──> Standardisasi Channel (Mean/Std) ──> Tensor PyTorch [1, 3, 224, 224] 
  ──> Feed-forward ke ViT Backbone ──> Ekstraksi Token [CLS] (768-D)
```

1. **Pemuatan dan Verifikasi Format Citra:**
   - Citra dimuat menggunakan pustaka `PIL.Image`.
   - Pemeriksaan mode warna dilakukan secara ketat: jika citra memiliki channel alfa (RGBA) atau monokrom (Grayscale/L), citra secara otomatis dikonversi menjadi format 3-channel RGB murni (`image.convert("RGB")`). Hal ini mencegah diskrepansi dimensionalitas tensor pada lapisan *patch embedding*.

2. **Penyesuaian Resolusi Spasial (Resize 224×224):**
   - Citra diubah ukurannya menjadi resolusi presisi **224 × 224 piksel** melalui interpolasi *bicubic*.
   - Resolusi ini dipilih sesuai dengan spesifikasi arsitektur ViT-Base (`vit-base-patch16-224`) yang membagi citra input menjadi $14 \times 14 = 196$ *non-overlapping patches* berukuran $16 \times 16$ piksel.
   - Bersama dengan 1 token `[CLS]` di awal sequence, terbentuk representasi urutan (*sequence*) berukuran $197 \times 768$ token.

3. **Normalisasi Dua Tahap (*Rescaling & Channel Standardization*):**
   - **Tahap 1 (Rescaling):** Nilai intensitas piksel bilangan bulat tak bertanda (*uint8*) pada rentang $[0, 255]$ diskalakan ke rentang floating-point $[0.0, 1.0]$.
   - **Tahap 2 (Standardisasi):** Setiap channel warna dinormalisasi secara independen dengan formula:
     $$x_{\text{norm}}^{(c)} = \frac{x^{(c)} - \mu^{(c)}}{\sigma^{(c)}}$$
     di mana $\mu^{(c)}$ dan $\sigma^{(c)}$ adalah nilai rerata (*mean*) dan simpangan baku (*standard deviation*) per channel $c \in \{R, G, B\}$.

---

## Rincian Konfigurasi Pemroses per Checkpoint ViT

Tiga model Vision Transformer pra-latih yang digunakan memiliki parameter pemroses spesifik yang dimuat secara otomatis dari Hugging Face Hub untuk menjamin reproduksibilitas:

| Model ViT | Domain Fitur | Checkpoint Hugging Face | Nilai Rerata Channel ($\mu_{R}, \mu_{G}, \mu_{B}$) | Simpangan Baku ($\sigma_{R}, \sigma_{G}, \sigma_{B}$) | Dimensi Output Token `[CLS]` |
|---|---|---|:---:|:---:|:---:|
| **ViT-Face** | Geometri & Identitas Wajah | `skutaada/VIT-VGGFace` | `[0.485, 0.456, 0.406]` | `[0.229, 0.224, 0.225]` | **768-D** |
| **ViT-Emotion** | Ekspresi & Afektif Wajah | `dima806/facial_emotions_image_detection` | `[0.500, 0.500, 0.500]` | `[0.500, 0.500, 0.500]` | **768-D** |
| **ViT-Age** | Tekstur Penuaan & Usia | `dima806/facial_age_image_detection` | `[0.500, 0.500, 0.500]` | `[0.500, 0.500, 0.500]` | **768-D** |

- Parameter normalisasi untuk `skutaada/VIT-VGGFace` mengadopsi standar ImageNet/VGGFace yang lazim pada tugas biometrik wajah.
- Parameter normalisasi untuk `dima806/*` mengadopsi rentang simetris $[-1.0, 1.0]$ yang optimal untuk pemodelan ekspresi afektif dan penuaan wajah.
- Semua nilai parameter diekstraksi langsung dari berkas konfigurasi `preprocessor_config.json` pada masing-masing repositori model tanpa intervensi manual (*no hardcoding*).

---

## Paritas Fitur pada Sistem Dual-Benchmark

Salah satu aspek metodologis krusial dalam penelitian ini adalah **paritas fitur absolut (*absolute feature parity*)**:

- Ekstraksi fitur ViT dilakukan sekali secara *offline* untuk seluruh 10.800 citra DemogPairs.
- Vektor fitur `[CLS]` 768-D yang dihasilkan disimpan dalam format terkompresi `joblib` (`features/demogpairs_vit-*.pkl`).
- **Kedua protokol evaluasi**—baik **Subject-Disjoint** (480 subjek latih / 120 subjek uji, 0% leakage) maupun **Subject-Overlap** (image-level split lama, 100% leakage)—mengakses **arsip vektor fitur yang persis sama**.
- Tidak ada ekstraksi ulang (*re-extraction*) atau modifikasi prapemrosesan antar-protokol.
- Dengan demikian, perbedaan akurasi antara Subject-Overlap (93,70%) dan Subject-Disjoint (88,66% LR / 88,61% SVM) membuktikan secara murni besaran *shortcut learning* akibat kebocoran data identitas subjek, sekaligus memenuhi standar pembuktian empiris yang diminta oleh Reviewer 2 IEEE Access.

---

## Referensi File & Implementasi

- `experiment/code/utils/extraction.py` — Implementasi fungsi `extract_vit_features()` (konversi RGB, `AutoImageProcessor`, dan ekstraksi tensor `[CLS]`).
- `experiment/code/1.1_vit-face_demogpairs.ipynb` — Eksekusi prapemrosesan dan ekstraksi domain Wajah.
- `experiment/code/1.1_vit-emotion_demogpairs.ipynb` — Eksekusi prapemrosesan dan ekstraksi domain Emosi.
- `experiment/code/1.1_vit-age_demogpairs.ipynb` — Eksekusi prapemrosesan dan ekstraksi domain Usia.
- `experiment/01_prepare-data.md` — Spesifikasi partisi dan pembagian data subjek.
- `experiment/03_feature-extraction.md` — Rincian fusi multi-domain dan arsitektur ViT.
