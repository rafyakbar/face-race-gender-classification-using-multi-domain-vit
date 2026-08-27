# Ekstraksi Fitur — Multi-Domain Vision Transformers & Feature Fusion

## Ringkasan

Penelitian ini mengusulkan kerangka kerja **Multi-Domain Feature Extraction** yang memanfaatkan representasi transfer dari tiga model *Vision Transformer* (ViT-Base) yang telah dilatih sebelumnya (*pre-trained*) pada domain spesifik wajah manusia. Ketiga domain tersebut mencakup:
1. **Identitas Wajah (*Face Identity / Biometrics*)**
2. **Ekspresi Wajah (*Facial Emotion / Affect*)**
3. **Estimasi Usia (*Facial Age / Biological Aging*)**

Proses ekstraksi dilakukan secara *offline* (sekali jalan) pada seluruh 10.800 citra dataset DemogPairs. Vektor fitur yang dihasilkan disimpan dalam format terkompresi (`.pkl`), kemudian digabungkan secara sistematis (*feature concatenation*) untuk membentuk varian fitur berdimensi tunggal (768-d), ganda (1.536-d), dan tripel (2.304-d).

---

## Alur Ekstraksi & Penggabungan Fitur

```
                            Citra DemogPairs (10.800)
                                       │
        ┌──────────────────────────────┼──────────────────────────────┐
        │                              │                              │
        ▼                              ▼                              ▼
┌──────────────────┐          ┌──────────────────┐          ┌──────────────────┐
│     ViT-Face     │          │   ViT-Emotion    │          │     ViT-Age      │
│ skutaada/        │          │ dima806/facial_  │          │ dima806/facial_  │
│ VIT-VGGFace      │          │ emotions_...     │          │ age_...          │
│ (Identity)       │          │ (Emotion)        │          │ (Age)            │
└────────┬─────────┘          └────────┬─────────┘          └────────┬─────────┘
         │                             │                             │
         ▼                             ▼                             ▼
   Vektor [CLS]                  Vektor [CLS]                  Vektor [CLS]
     (768-d)                       (768-d)                       (768-d)
         │                             │                             │
         ├─────────────────────────────┼─────────────────────────────┤
         │                             │                             │
         ▼                             ▼                             ▼
 demogpairs_vit-face.pkl      demogpairs_vit-emotion.pkl   demogpairs_vit-age.pkl
   (29,37 MB)                    (29,36 MB)                    (29,36 MB)
         │                             │                             │
         └─────────────────────────────┼─────────────────────────────┘
                                       │
                                       ▼
                       ┌───────────────────────────────┐
                       │ Cross-Domain Feature Fusion   │
                       │ (Concatenation)               │
                       ├───────────────────────────────┤
                       │ • Single-Domain: 768-d        │
                       │ • Dual-Domain  : 1.536-d      │
                       │ • Tri-Domain   : 2.304-d      │
                       └───────────────────────────────┘
```

---

## Rincian Ekstraktor 1: ViT-Face (Identitas Wajah)

### 1. Karakteristik Model
* **Model Checkpoint:** `skutaada/VIT-VGGFace` (HuggingFace)
* **Arsitektur:** Vision Transformer Base (`vit-base-patch16-224`)
* **Konfigurasi Arsitektur:** 12 Transformer Encoder Layers, 12 Attention Heads, Hidden Dimension 768, MLP Dimension 3.072.
* **Domain Pre-training:** Pengenalan identitas wajah (*Face Recognition / Biometrics*) yang dilatih pada dataset benchmark VGGFace.
* **Karakteristik Representasi:** Menangkap karakteristik anatomi dan biometrik statis wajah, konfigurasi spasial fitur wajah (jarak antar mata, bentuk hidung, garis rahang), serta representasi unik individu yang invarian terhadap variasi pencahayaan.

### 2. Statistik Ekstraksi
* **Dimensi Output:** 768 float32
* **Total Sampel Diekstrak:** 10.800 citra
* **Kecepatan Ekstraksi:** ~2,14 iterasi/detik
* **Total Durasi Ekstraksi:** **1 jam 24 menit 04 detik**
* **Berkas Penyimpanan:** `features/demogpairs_vit-face.pkl` (29,37 MB)

---

## Rincian Ekstraktor 2: ViT-Emotion (Ekspresi & Afek Wajah)

### 1. Karakteristik Model
* **Model Checkpoint:** `dima806/facial_emotions_image_detection` (HuggingFace)
* **Arsitektur:** Vision Transformer Base (`vit-base-patch16-224`)
* **Konfigurasi Arsitektur:** 12 Transformer Encoder Layers, 12 Attention Heads, Hidden Dimension 768.
* **Domain Pre-training:** Klasifikasi ekspresi emosi wajah (*Facial Emotion Recognition*).
* **Karakteristik Representasi:** Menangkap dinamika lokal wajah (*facial dynamics*), deformasi mikro-otot wajah (*Action Units*), kerutan senyum, kontraksi dahi, dan pola afektif yang melintasi berbagai struktur wajah.

### 2. Statistik Ekstraksi
* **Dimensi Output:** 768 float32
* **Total Sampel Diekstrak:** 10.800 citra
* **Kecepatan Ekstraksi:** ~2,10 iterasi/detik
* **Total Durasi Ekstraksi:** **1 jam 25 menit 48 detik**
* **Berkas Penyimpanan:** `features/demogpairs_vit-emotion.pkl` (29,36 MB)

---

## Rincian Ekstraktor 3: ViT-Age (Usia & Penuaan Biologis)

### 1. Karakteristik Model
* **Model Checkpoint:** `dima806/facial_age_image_detection` (HuggingFace)
* **Arsitektur:** Vision Transformer Base (`vit-base-patch16-224`)
* **Konfigurasi Arsitektur:** 12 Transformer Encoder Layers, 12 Attention Heads, Hidden Dimension 768.
* **Domain Pre-training:** Estimasi usia wajah (*Facial Age Estimation*).
* **Karakteristik Representasi:** Menangkap perubahan tekstur kulit, kerapatan kerutan, elastisitas epidermis, serta perubahan morfologi kraniofasial yang terjadi sepanjang proses penuaan biologis manusia.

### 2. Statistik Ekstraksi
* **Dimensi Output:** 768 float32
* **Total Sampel Diekstrak:** 10.800 citra
* **Kecepatan Ekstraksi:** ~1,84 iterasi/detik
* **Total Durasi Ekstraksi:** **1 jam 37 menit 45 detik**
* **Berkas Penyimpanan:** `features/demogpairs_vit-age.pkl` (29,36 MB)

> **Total Waktu Ekstraksi Offline:** Keseluruhan ekstraksi 3 fitur pada 10.800 citra memerlukan waktu komputasi akumulatif sekitar **4 jam 27 menit 37 detik** pada perangkat GPU/CPU.

---

## Rasional & Strategi Cross-Domain Feature Fusion

### Mengapa Pendekatan Multi-Domain Diperlukan?
Klasifikasi ras dan gender pada citra wajah sering kali rentan terhadap bias visual apabila hanya mengandalkan satu domain fitur:
1. **Fitur Identitas (ViT-Face)** sangat kuat dalam membedakan bentuk biometrik global, tetapi dapat terdistorsi oleh variasi usia atau ekspresi ekstrem.
2. **Fitur Emosi (ViT-Emotion)** menyediakan konteks dinamika mikro wajah yang membantu memisahkan atribut gender melalui pola kontraksi otot wajah.
3. **Fitur Usia (ViT-Age)** menyediakan informasi tekstur mikro kulit dan struktur penuaan yang memiliki manifestasi berbeda antar-kelompok ras dan gender.

Penggabungan ketiga representasi saling melengkapi (*complementary representations*), memungkinkan ruang fitur menangkap perbedaan interseksional yang halus dan kuat terhadap variasi intra-kelas.

---

## 7 Konfigurasi Fitur yang Dievaluasi (Ablation Study)

### 1. Single-Domain Configurations (768 Dimensi)
* **`vit-age`:** Vektor fitur usia tunggal (768-d).
* **`vit-emotion`:** Vektor fitur emosi tunggal (768-d).
* **`vit-face`:** Vektor fitur identitas wajah tunggal (768-d).

### 2. Dual-Domain Configurations (1.536 Dimensi)
* **`vit-emotion-age`:** Penggabungan fitur emosi dan usia (768 + 768 = 1.536-d).
* **`vit-face-age`:** Penggabungan fitur wajah dan usia (768 + 768 = 1.536-d).
* **`vit-emotion-face`:** Penggabungan fitur emosi dan wajah (768 + 768 = 1.536-d).

### 3. Tri-Domain Configuration (2.304 Dimensi — Usulan Utama)
* **`vit-face-emotion-age`:** Penggabungan simultan ketiga domain representasi (768 + 768 + 768 = 2.304-d).

```python
# Implementasi Penggabungan 3 Fitur (Notebook 2.1.7)
vggface_features = joblib.load('features/demogpairs_vit-face.pkl')
emotion_features = joblib.load('features/demogpairs_vit-emotion.pkl')
age_features     = joblib.load('features/demogpairs_vit-age.pkl')

features = {}
for d in tqdm(data):
    key = d['image_path']
    features[key] = np.array(
        list(vggface_features[key]) + 
        list(emotion_features[key]) + 
        list(age_features[key])
    )
```
