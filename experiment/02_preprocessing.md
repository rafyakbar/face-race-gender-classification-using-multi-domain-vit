# Preprocessing Pipeline — Normalisasi Citra, Ekstraksi Vektor [CLS], dan Transformasi Fitur

## Ringkasan

Pipeline *preprocessing* pada penelitian ini terbagi ke dalam dua tingkatan utama:
1. **Tingkat Citra (*Image-Level Preprocessing*):** Penyiapan dan standardisasi citra mentah sebelum diproses oleh arsitektur *Vision Transformer* (ViT) untuk ekstraksi fitur.
2. **Tingkat Vektor Fitur (*Feature-Level Preprocessing*):** Transformasi dan standardisasi vektor fitur numerik sebelum diinputkan ke dalam model klasifikasi *Support Vector Machine* (SVM), mencakup eksplorasi penskalaan (*feature scaling*) dan reduksi dimensi (*dimensionality reduction*).

---

## 1. Preprocessing Tingkat Citra (*Image-Level*)

Setiap citra wajah dari dataset DemogPairs diproses secara individual melalui pipeline `AutoImageProcessor` dari HuggingFace Transformers yang disesuaikan dengan arsitektur masing-masing model ViT pre-trained.

```
Citra Mentah (JPEG/RGB)
        │
        ▼
┌──────────────────────────────────────────────┐
│ 1. Verifikasi Format Warna                   │
│    - Konversi mode citra ke RGB 3-channel    │
└──────────────────────────────────────────────┘
        │
        ▼
┌──────────────────────────────────────────────┐
│ 2. Spatial Resizing                          │
│    - Interpolasi bicubic ke 224 × 224 piksel │
└──────────────────────────────────────────────┘
        │
        ▼
┌──────────────────────────────────────────────┐
│ 3. Tensor Normalization                      │
│    - Penskalaan nilai piksel ke [0, 1]       │
│    - Standardisasi: (x - mean) / std         │
└──────────────────────────────────────────────┘
        │
        ▼
┌──────────────────────────────────────────────┐
│ 4. Batch Formatting                          │
│    - Konversi ke PyTorch Tensor [1, 3, 224, 224]│
│    - Alokasi ke device (CUDA / CPU)          │
└──────────────────────────────────────────────┘
        │
        ▼
Input ke Vision Transformer Encoder
```

### Implementasi Ekstraksi Citra (`extract_vit_features`)

Fungsi inti preprocessing citra dalam `utils.py` / `utilsv2.py`:

```python
def extract_vit_features(img, model=None, model_path='...', device=None, feature_type='cls'):
    # 1. Pemuatan Processor & Konfigurasi Device
    if device is None:
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = model.to(device)
    processor = AutoImageProcessor.from_pretrained(model_path)

    # 2. Pemuatan dan Verifikasi Format Citra
    if isinstance(img, str):
        image = Image.open(img)
    elif isinstance(img, np.ndarray):
        image = Image.fromarray(img.astype('uint8'))
        
    if image.mode != 'RGB':
        image = image.convert('RGB')

    # 3. Preprocessing Standar ViT
    inputs = processor(images=image, return_tensors="pt").to(device)

    # 4. Inferensi Model & Ekstraksi Token
    with torch.no_grad():
        vit_outputs = model.vit(**inputs)
        hidden_states = vit_outputs.last_hidden_state  # [1, 197, 768]

    if feature_type == 'cls':
        features = hidden_states[:, 0, :]  # [CLS] token (vektor 768-d)
    elif feature_type == 'pool':
        features = hidden_states.mean(dim=1)  # Mean pooling

    return features.squeeze(0).cpu().numpy()
```

---

## 2. Representasi Token `[CLS]`

Arsitektur Vision Transformer membagi citra 224 × 224 menjadi 196 patch berukuran 16 × 16, ditambah satu token khusus `[CLS]` (*Classification Token*) di posisi awal urutan (196 + 1 = 197 token sequence). 

Melalui mekanisme *multi-head self-attention* berlapis, token `[CLS]` mengagregasi representasi global seluruh wajah. Output vektor 768-dimensi dari token `[CLS]` pada lapisan terakhir (*last hidden state*) digunakan sebagai deskriptor padat (*dense feature representation*) dari citra wajah.

---

## 3. Preprocessing Tingkat Vektor Fitur (*Feature-Level*)

Dalam pipeline pelatihan SVM, dilakukan eksplorasi sistematik terhadap dua komponen transformasi data menggunakan `GridSearchCV`:

### A. Penskalaan Fitur (*Feature Scaling*)
Eksperimen membandingkan dua opsi:
* **`None` (Tanpa Penskalaan):** Mempertahankan distribusi nilai embedding asli yang dihasilkan oleh ViT (rentang kontinu bertipe `float32`).
* **`MinMaxScaler()`:** Mentransformasi seluruh dimensi fitur ke dalam rentang terikat [0, 1] secara independen:
  `x_scaled = (x - x_min) / (x_max - x_min)`

### B. Reduksi Dimensi (*Principal Component Analysis — PCA*)
Eksperimen membandingkan tiga opsi PCA berbasis rasio varians kumulatif:
* **`None`:** Menggunakan seluruh dimensi fitur asli (768, 1.536, atau 2.304 dimensi).
* **`PCA(n_components=0.5)`:** Mempertahankan komponen utama hingga mencakup 50% total varians data.
* **`PCA(n_components=0.75)`:** Mempertahankan komponen utama hingga mencakup 75% total varians data.

### Temuan Preprocessing pada Tahap Optimasi
Dari 288 kombinasi parameter yang dievaluasi pada setiap model:
1. **PCA tidak terpilih pada seluruh model terbaik (`pca: None`).** Reduksi dimensi linear menggunakan PCA terbukti menghilangkan detail non-linear halus yang diekstrak oleh Vision Transformer, sehingga menurunkan akurasi klasifikasi secara signifikan.
2. **Penskalaan `scaler: None` menjadi pilihan optimal pada 6 dari 7 konfigurasi model.** Representasi embedding ViT telah memiliki skala yang teratur secara intrinsik berkat lapisan *Layer Normalization* pada transformer. Hanya konfigurasi gabungan `vit-emotion-face` yang menunjukkan sedikit peningkatan dengan `MinMaxScaler`.
