# Preprocessing Citra — Resize dan Normalisasi untuk Vision Transformer

## Ringkasan

Tahap preprocessing citra menstandardisasi seluruh 10.800 citra DemogPairs ke format identik sebelum ekstraksi fitur Vision Transformer. Proses dilakukan sekali secara offline oleh AutoImageProcessor dan mencakup pemuatan citra, konversi warna, resizing, serta normalisasi.

---

## Preprocessing Citra

Setiap citra mentah memiliki variasi ukuran dan mode warna. Preprocessing menjamin setiap citra berada pada skala dan distribusi yang konsisten sehingga patch embedding Vision Transformer menerima input yang seragam.

Proses menggunakan **AutoImageProcessor** dari Hugging Face Transformers yang memuat konfigurasi spesifik untuk setiap checkpoint secara otomatis tanpa nilai hard-coded. Pipeline bersifat deterministik dan dijalankan untuk ketiga domain (Face, Emotion, Age) dengan processor yang konsisten dengan modelnya masing-masing.

Tahapan urut: pemuatan citra, verifikasi dan konversi ke 3 channel RGB (membuang alpha, grayscale, atau CMYK), resizing spasial ke 224×224, serta normalisasi tensor.

---

## Resize Citra 224×224

Seluruh citra di-resize ke **224×224 piksel** melalui interpolasi bicubic. Ukuran ini sesuai dengan ekspektasi Vision Transformer Base (vit-base-patch16-224) yang membagi citra menjadi 196 patch berukuran 16×16 ditambah 1 token khusus, menghasilkan total 197 token.

Konfigurasi ukuran diambil langsung dari processor config (height 224, width 224) dan menjaga konsistensi aspect ratio melalui mekanisme resize dan center crop bawaan processor Vision Transformer. Tidak ada resizing manual terpisah di luar processor.

---

## Normalisasi Citra

Setelah resizing, dilakukan dua langkah normalisasi oleh AutoImageProcessor:

1. **Rescaling** — piksel uint8 pada rentang [0,255] dibagi 255.0 menjadi float pada rentang [0,1].
2. **Standardisasi channel-wise** — setiap channel dinormalisasi dengan formula (x − mean) / std, di mana mean dan standard deviation adalah nilai spesifik untuk setiap checkpoint (misalnya konfigurasi VGGFace berbeda dengan Emotion dan Age).

Nilai mean dan standard deviation tidak ditulis manual, melainkan dimuat otomatis dari konfigurasi model. Hasil normalisasi kemudian diformat menjadi tensor dan dialokasikan ke device yang tersedia sebelum diteruskan ke Vision Transformer Encoder untuk ekstraksi fitur.

---

## Referensi File

- `code/utils/extraction.py` — implementasi preprocessing citra tingkat image-level
- `code/1.1_vit-*_demogpairs.ipynb` — eksekusi ekstraksi offline per domain
