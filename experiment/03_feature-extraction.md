# 03 — Ekstraksi Fitur Multi-Domain Vision Transformer & Feature Fusion

## Ringkasan Eksekutif

Tahap ekstraksi fitur merupakan fondasi metodologis penelitian ini. Berbeda dengan pendekatan *end-to-end* yang melatih *backbone* dan *classifier* secara bersamaan, penelitian ini menerapkan **strategi ekstraksi *offline* (sekali jalan, *one-pass*)**: seluruh 10.800 citra DemogPairs dilewatkan melalui tiga *Vision Transformer* (ViT) *pre-trained* yang berbeda domain, vektor fitur padat (*dense embedding*) diambil, disimpan permanen dalam berkas `.pkl` terkompresi, dan baru kemudian digunakan untuk seluruh eksperimen klasifikasi (28 notebook `2.x`). Strategi ini memberikan tiga keuntungan: (1) reproduksibilitas — fitur identik untuk setiap *classifier*, (2) efisiensi — tidak ada inferensi ViT berulang saat *GridSearchCV* 1.440 *fits*, dan (3) isolasi variabel — performa *classifier* merefleksikan kualitas representasi, bukan stokastisitas *backbone*.

Tiga ekstraktor yang digunakan seluruhnya berbasis **ViT-Base *patch16-224* (12 *layers*, 12 *heads*, *hidden dim* 768, *MLP dim* 3072)** dan menghasilkan **vektor token `[CLS]` 768-dimensi bertipe `float32`** per citra. Melalui operasi *concatenation* vektor, dibentuk **7 konfigurasi fitur *ablation*** dengan dimensi **768-d** (*single-domain*), **1.536-d** (*dual-domain*), dan **2.304-d** (*tri-domain*) untuk menjawab pertanyaan riset: kombinasi domain mana yang paling diskriminatif untuk klasifikasi ras–gender.

| Aspek | Spesifikasi |
|---|---|
| **Dataset sumber** | DemogPairs — 10.800 citra (6 kelas: Asian/Black/White × Female/Male) |
| **Jumlah ekstraktor** | 3 ViT-Base independen |
| **Dimensi per ekstraktor** | 768-d (`float32`, token `[CLS]`) |
| **Mode ekstraksi** | *Offline*, *one-pass*, `torch.no_grad()` |
| **Penyimpanan** | `features/demogpairs_vit-{face,emotion,age}.pkl` (`joblib.dump(..., compress=9)`, ±30 MB/berkas) |
| **Dimensi gabungan** | 768 (×1), 1.536 (×2), 2.304 (×3) |
| **Total waktu ekstraksi** | ±4 jam 27 menit 37 detik (CPU, ~2 it/s) |
| **Konfigurasi *ablation*** | 7 (3 tunggal + 3 ganda + 1 tripel) |

---

## 1. Landasan Arsitektur: Vision Transformer Base (ViT-Base)

Ketiga model berbagi arsitektur identik — **ViT-Base *patch16-224*** yang diperkenalkan Dosovitskiy *et al.* (2020). Pemahaman arsitektur ini penting karena menentukan dimensi output dan mekanisme ekstraksi `[CLS]`.

### 1.1 Spesifikasi Arsitektur ViT-Base

| Komponen | Nilai | Keterangan |
|---|---|---|
| **Input citra** | 224 × 224 × 3 (RGB) | Setelah *resizing* oleh `AutoImageProcessor` |
| **Ukuran *patch*** | 16 × 16 piksel | Citra dibagi menjadi grid 14 × 14 |
| **Jumlah *patch*** | 196 | (224/16)² = 196 *patch* spasial |
| **Token `[CLS]`** | 1 | Token klasifikasi yang dipelajari (*learnable*) di posisi 0 |
| **Panjang *sequence*** | 197 | 196 *patch* + 1 `[CLS]` → `last_hidden_state` berukuran `[1, 197, 768]` |
| ***Transformer layers*** | 12 | *Encoder blocks* berurutan |
| ***Attention heads*** | 12 | *Multi-head self-attention* per *layer* |
| ***Hidden dimension*** | 768 | Dimensi setiap token (juga dimensi output `[CLS]`) |
| ***MLP dimension*** | 3.072 | Dimensi *feed-forward* di dalam tiap *encoder* (4× *hidden*) |
| **Parameter total** | ±86 juta | Standar ViT-Base |
| **Normalisasi** | *LayerNorm* | Di setiap *residual block*; membuat skala *embedding* sudah ternormalisasi |
| ***Positional embedding*** | *Learnable 1D* | 197 posisi (196 *patch* + `[CLS]`) |

### 1.2 Mekanisme Token `[CLS]` sebagai Deskriptor Wajah

1. Citra 224×224 dipecah menjadi 196 *patch* 16×16, masing-masing diproyeksikan linear menjadi vektor 768-d (*patch embedding*).
2. Vektor `[CLS]` (768-d, diinisialisasi acak dan dipelajari selama *pre-training*) ditempel di awal *sequence*.
3. *Positional embedding* ditambahkan ke seluruh 197 token.
4. *Sequence* melewati 12 *layers self-attention*: setiap token dapat memperhatikan seluruh token lain. Secara progresif, token `[CLS]` mengagregasi informasi global — anatomi, tekstur, dan konteks spasial wajah.
5. Pada `last_hidden_state` lapis ke-12, **baris ke-0 (`hidden_states[:, 0, :]`)** — yaitu representasi `[CLS]` — diambil sebagai **deskriptor padat citra**. Vektor inilah yang disimpan sebagai fitur 768-d.

> **Mengapa `[CLS]` dan bukan *mean pooling*?** Fungsi `extract_vit_features(..., feature_type='cls')` secara eksplisit menggunakan `hidden_states[:, 0, :]`. Alternatif `feature_type='pool'` (*mean* 197 token) tersedia di kode tetapi **tidak digunakan** dalam eksperimen ini, karena `[CLS]` terbukti lebih diskriminatif untuk tugas klasifikasi wajah pada ViT *pre-trained*.

---

## 2. Tiga Ekstraktor Multi-Domain

Ketiga ViT dipilih karena *pre-training* pada tugas wajah yang **saling ortogonal** — identitas, emosi, dan usia — sehingga representasinya saling melengkapi (*complementary*), bukan redundan.

### 2.1 Tabel Perbandingan Ketiga Ekstraktor

| Atribut | ViT-Face (Identitas) | ViT-Emotion (Emosi) | ViT-Age (Usia) |
|---|---|---|---|
| **Checkpoint HuggingFace** | `skutaada/VIT-VGGFace` | `dima806/facial_emotions_image_detection` | `dima806/facial_age_image_detection` |
| **Arsitektur *backbone*** | `vit-base-patch16-224` | `vit-base-patch16-224` | `vit-base-patch16-224` |
| **Konfigurasi** | 12 *layers* / 12 *heads* / 768-d / MLP 3072 | Identik | Identik |
| **Domain *pre-training*** | Pengenalan identitas wajah (*Face Recognition / Biometrics*) pada **VGGFace** | Klasifikasi ekspresi emosi wajah (*Facial Emotion Recognition*) | Estimasi usia wajah (*Facial Age Estimation*) |
| **Label *pre-training*** | Identitas individu (ribuan kelas identitas) | Kategori emosi (mis. *happy, sad, angry, fear, disgust, surprise, neutral*) | Kelompok/ regresi usia |
| **Karakteristik representasi** | Geometri biometrik statis: jarak antar-mata, bentuk hidung, garis rahang, struktur kraniofasial; invarian terhadap iluminasi & pose moderat | Dinamika mikro-otot wajah: *Action Units* (AU), kerutan senyum, kontraksi dahi, deformasi bibir & mata; pola afektif lintas struktur | Tekstur penuaan: kerapatan kerutan, elastisitas epidermis, pigmentasi, perubahan morfologi kraniofasial terkait usia biologis |
| **Relevansi untuk ras–gender** | Ras dan gender memiliki korelat biometrik global yang kuat | Ekspresi dan *display rules* emosi bervariasi antar gender & budaya | Penuaan kulit dan morfologi bermanifestasi berbeda antar ras & gender |
| **Dimensi output** | 768-d `float32` (`[CLS]`) | 768-d `float32` (`[CLS]`) | 768-d `float32` (`[CLS]`) |
| **Berkas `.pkl`** | `features/demogpairs_vit-face.pkl` | `features/demogpairs_vit-emotion.pkl` | `features/demogpairs_vit-age.pkl` |
| **Ukuran berkas (compress=9)** | 30.795.213 bytes (±29,37 MB) | 30.789.736 bytes (±29,36 MB) | 30.781.253 bytes (±29,36 MB) |
| **Total sampel** | 10.800 citra | 10.800 citra | 10.800 citra |
| **Kecepatan (CPU)** | ~2,14 it/s | ~2,10 it/s | ~1,84 it/s |
| **Durasi ekstraksi** | **1 jam 24 menit 04 detik** (5.044 dtk) | **1 jam 25 menit 48 detik** (5.148 dtk) | **1 jam 37 menit 45 detik** (5.865 dtk) |
| **Notebook sumber** | `code/1.1_vit-face_demogpairs.ipynb` | `code/1.1_vit-emotion_demogpairs.ipynb` | `code/1.1_vit-age_demogpairs.ipynb` |
| **Struktur loop** | `for d in tqdm(data): features[d['image_path']] = u.extract_vit_features(d['full_path'], model, model_path, device)` | Identik | Identik |
| **Output loop** | `((768,), ['features/demogpairs_vit-face.pkl'])` | `((768,), ['features/demogpairs_vit-emotion.pkl'])` | `((768,), ['features/demogpairs_vit-age.pkl'])` |

### 2.2 Rincian Per Ekstraktor

#### Ekstraktor 1 — ViT-Face (`skutaada/VIT-VGGFace`)

- **Tugas *pre-training*:** Klasifikasi identitas pada VGGFace/VGGFace2 (ribuan identitas selebritas). Model belajar memisahkan individu, sehingga fitur yang dihasilkan sangat sensitif terhadap **struktur anatomi wajah yang unik per individu** dan relatif robust terhadap variasi iluminasi, ekspresi moderat, dan *background*.
- **Apa yang ditangkap untuk ras–gender:** Perbedaan biometrik antar-kelompok demografis (mis. proporsi kraniofasial, morfologi hidung-bibir) termanifestasi sebagai pergeseran sistematis di ruang 768-d. Fitur ini menjadi *backbone* terkuat untuk klasifikasi demografis, tetapi rentan bias jika hanya mengandalkan *ancestral features* tanpa kompensasi tekstur/ekspresi.

#### Ekstraktor 2 — ViT-Emotion (`dima806/facial_emotions_image_detection`)

- **Tugas *pre-training*:** Klasifikasi 7 emosi dasar pada dataset ekspresi wajah. Model belajar mendeteksi **deformasi lokal** — kerutan *nasolabial*, kontraksi *corrugator supercilii* (dahi), pembukaan kelopak mata, dan ketegangan otot bibir.
- **Apa yang ditangkap untuk ras–gender:** Pola ekspresi memiliki korelat gender (mis. intensitas senyum, *facial display rules*) dan ras (morfologi otot wajah & kerutan). Fitur emosi berfungsi sebagai **sinyal komplementer** yang membantu memisahkan kelas ketika fitur biometrik global ambigu.
- **Catatan teknis:** Saat ekstraksi, *processor* model ini memicu peringatan `Using a slow image processor as use_fast is unset` — tidak memengaruhi nilai fitur, hanya mengindikasikan *legacy processor* masih dipakai. Ekstraksi tetap berjalan penuh 10.800 citra dalam 1 jam 25 menit 48 detik.

#### Ekstraktor 3 — ViT-Age (`dima806/facial_age_image_detection`)

- **Tugas *pre-training*:** Estimasi usia (regresi/klasifikasi kelompok usia). Model belajar mengasosiasikan **tekstur kulit, kerapatan kerutan, kekenduran jaringan, dan perubahan proporsi kraniofasial** dengan usia kronologis.
- **Apa yang ditangkap untuk ras–gender:** Proses penuaan bermanifestasi berbeda: tingkat *photoaging*, distribusi melanin, ketebalan epidermis, dan pola kerutan bervariasi antar ras; sementara ketebalan kulit dan distribusi lemak wajah bervariasi antar gender. Fitur usia menyediakan **sinyal tekstur mikro** yang ortogonal terhadap geometri biometrik.
- **Catatan performa:** ViT-Age paling lambat (~1,84 it/s vs ~2,14 it/s pada ViT-Face), kemungkinan karena ukuran *checkpoint* atau kompleksitas *head* yang sedikit berbeda, tetapi tetap menyelesaikan 10.800 citra dalam 1 jam 37 menit 45 detik.

---

## 3. Pipeline Ekstraksi *Offline* — Dari Citra Mentah ke `.pkl`

### 3.1 Diagram Alur End-to-End

```
                        Citra Mentah DemogPairs (10.800 JPEG)
                        dataset/demogpairs/images/*/*.jpg
                                     │
                                     ▼
                    ┌─────────────────────────────────┐
                    │  AutoImageProcessor (per model)  │
                    │  1. Konversi RGB (3-channel)     │
                    │  2. Resize bicubic 224×224       │
                    │  3. Normalisasi (x-mean)/std     │
                    │  4. To Tensor [1,3,224,224]      │
                    │  5. Pindah ke device (CPU/CUDA)  │
                    └──────────────┬──────────────────┘
                                   │
              ┌────────────────────┼────────────────────┐
              │                    │                    │
              ▼                    ▼                    ▼
     ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
     │   ViT-Face      │  │  ViT-Emotion    │  │    ViT-Age      │
     │ skutaada/       │  │ dima806/facial_ │  │ dima806/facial_ │
     │ VIT-VGGFace     │  │ emotions_...    │  │ age_...         │
     │ (Identity)      │  │ (Emotion)       │  │ (Age)           │
     │ 12 layers       │  │ 12 layers       │  │ 12 layers       │
     │ 768-d hidden    │  │ 768-d hidden    │  │ 768-d hidden    │
     └────────┬────────┘  └────────┬────────┘  └────────┬────────┘
              │                    │                    │
              ▼                    ▼                    ▼
        model.vit(**inputs)  model.vit(**inputs)  model.vit(**inputs)
        last_hidden_state    last_hidden_state    last_hidden_state
          [1,197,768]          [1,197,768]          [1,197,768]
              │                    │                    │
              ▼                    ▼                    ▼
       hidden_states[:,0,:]  hidden_states[:,0,:] hidden_states[:,0,:]
         Token [CLS] 768-d    Token [CLS] 768-d   Token [CLS] 768-d
         float32              float32              float32
              │                    │                    │
              ▼                    ▼                    ▼
   features/demogpairs_  features/demogpairs_  features/demogpairs_
     vit-face.pkl          vit-emotion.pkl       vit-age.pkl
    (30,79 MB, 10800)     (30,78 MB, 10800)     (30,78 MB, 10800)
    joblib.dump(c=9)      joblib.dump(c=9)      joblib.dump(c=9)
              │                    │                    │
              └────────────────────┼────────────────────┘
                                   │
                                   ▼
                  ┌─────────────────────────────────┐
                  │  Cross-Domain Feature Fusion     │
                  │  Concatenation (np.concatenate)  │
                  │  • Single: 768-d                 │
                  │  • Dual  : 1.536-d (768+768)     │
                  │  • Tri   : 2.304-d (768×3)       │
                  └──────────────┬──────────────────┘
                                   │
                                   ▼
                     Matriks Fitur X [10800, D]
                     D ∈ {768, 1536, 2304}
                     + Label y [10800] (0..5)
                                   │
                                   ▼
                    train_test_split (80/20, stratify, seed 42)
                     X_train [8640,D] / X_test [2160,D]
                                   │
                                   ▼
                        GridSearchCV (SVM/RF/LR/GNB)
```

### 3.2 Fungsi Inti: `utils/extraction.py :: extract_vit_features`

Seluruh notebook `1.1_*` memanggil **satu fungsi yang sama** — `u.extract_vit_features` — yang didefinisikan di `code/utils/extraction.py`. Berikut anatomi lengkapnya:

```python
def extract_vit_features(
    img: str | np.ndarray,
    model: Optional[AutoModelForImageClassification] = None,
    model_path: str = "models/codewithdark/vit-chest-xray",
    device: Optional[torch.device] = None,
    feature_type: str = "cls",
) -> np.ndarray:
    """
    Extract features from a ViT model using [CLS] token or mean pooling.
    Returns: 1D NumPy array shape (hidden_dim,) — yaitu (768,).
    """
    if device is None:
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    if model is None:
        model = AutoModelForImageClassification.from_pretrained(model_path)
    model = model.to(device)
    model.eval()  # nonaktifkan dropout/batchnorm update

    processor = AutoImageProcessor.from_pretrained(model_path)

    # 1. Muat citra
    if isinstance(img, str):
        image = Image.open(img)          # path file JPEG
    elif isinstance(img, np.ndarray):
        image = Image.fromarray(img.astype("uint8"))
    else:
        raise ValueError("img must be a file path or NumPy array.")

    if image.mode != "RGB":
        image = image.convert("RGB")     # paksa 3-channel

    # 2. Preprocessing ViT standar
    inputs = processor(images=image, return_tensors="pt").to(device)
    # → pixel_values: [1, 3, 224, 224], sudah dinormalisasi

    # 3. Forward pass tanpa gradien (hemat memori & cepat)
    with torch.no_grad():
        vit_outputs = model.vit(**inputs)
        hidden_states = vit_outputs.last_hidden_state  # [1, 197, 768]

    # 4. Ambil token [CLS]
    if feature_type == "cls":
        features = hidden_states[:, 0, :]   # [1, 768] — baris CLS
    elif feature_type == "pool":
        features = hidden_states.mean(dim=1) # [1, 768] — rata-rata 197 token
    else:
        raise ValueError("feature_type must be 'cls' or 'pool'.")

    return features.squeeze(0).cpu().numpy()  # (768,) float32
```

**Langkah demi langkah (sesuai eksekusi aktual di notebook):**

| Langkah | Kode | Penjelasan |
|---|---|---|
| **0. Inisialisasi *device*** | `torch.device('cuda' if torch.cuda.is_available() else 'cpu')` | Pada eksperimen tercatat `device(type='cpu')` — seluruh ekstraksi 10.800 citra berjalan di CPU |
| **1. Muat model** | `AutoModelForImageClassification.from_pretrained(model_path).to(device)` | Model dipindahkan ke *device* sekali di awal, lalu dipakai berulang untuk 10.800 iterasi tanpa *reload* |
| **2. Muat dataset** | `data = u.load_demogpairs()` | Membaca 6 berkas `dataset/demogpairs/metadata/{class}.txt`, menghasilkan `list[dict]` dengan kunci `image_path`, `full_path`, `label`, `label_idx` (10.800 entri) |
| **3. Loop ekstraksi** | `for d in tqdm(data): features[d['image_path']] = u.extract_vit_features(...)` | Iterasi satu-per-satu; `tqdm` menampilkan progres & kecepatan it/s |
| **4. Simpan** | `joblib.dump(features, 'features/demogpairs_vit-*.pkl', compress=9)` | Kompresi level 9 (maksimal) — rasio ±30 MB untuk 10.800 × 768 × 4 byte (~33 MB mentah) |

### 3.3 Detail *Preprocessing* Tingkat Citra

`AutoImageProcessor` di dalam `extract_vit_features` melakukan pipeline identik untuk ketiga model (hanya nilai *mean/std* yang dapat berbeda per *checkpoint*):

1. **Verifikasi warna** — `image.convert("RGB")` jika *grayscale* atau *RGBA*.
2. ***Resizing* spasial** — interpolasi *bicubic* ke 224×224 piksel (input tetap ViT).
3. ***Rescaling* & normalisasi** — piksel [0,255] → [0,1] → `(x - mean) / std` dengan *mean/std* bawaan *processor* masing-masing model.
4. ***Batch formatting*** — konversi ke `torch.Tensor` bentuk `[1, 3, 224, 224]` dan pemindahan ke *device*.

Output `processor(images=image, return_tensors="pt")` adalah *dict* dengan kunci `pixel_values` yang langsung diumpankan ke `model.vit(**inputs)`.

---

## 4. Penyimpanan Fitur: Format `.pkl` Terkompresi

### 4.1 Struktur Berkas

Setiap berkas `.pkl` adalah **satu objek Python *dict*** yang diserialisasi dengan `joblib`:

```python
# Struktur logis (ditampilkan untuk satu berkas, mis. vit-face)
features: dict[str, np.ndarray]
# Contoh isi:
# {
#   "able_wanamakok/002.jpg": np.ndarray(shape=(768,), dtype=float32),
#   "able_wanamakok/004.jpg": np.ndarray(shape=(768,), dtype=float32),
#   ...
#   "zachary_quinto/226.jpg": np.ndarray(shape=(768,), dtype=float32),
# }
# Total: 10.800 kunci (satu per citra)
```

- **Kunci (*key*):** `image_path` relatif (mis. `"able_wanamakok/002.jpg"`), **bukan** `full_path`. Hal ini disengaja agar *key* konsisten lintas ekstraktor dan memudahkan *concatenation* berbasis *key* yang sama.
- **Nilai (*value*):** `np.ndarray` 1-D bentuk `(768,)` bertipe `float32` — vektor `[CLS]` mentah tanpa normalisasi tambahan.
- **Jumlah entri:** Selalu 10.800 (validasi: `len(features) == len(data) == 10800`).
- **Tipe data:** `float32` (4 byte/elemen) → 768 × 4 = 3.072 byte per citra; total mentah ~33 MB, terkompresi menjadi ±30 MB dengan `compress=9`.

### 4.2 Cara Memuat & Memvalidasi

```python
import joblib
import numpy as np

# Muat satu domain
face = joblib.load("features/demogpairs_vit-face.pkl")
print(len(face))                          # 10800
print(face["able_wanamakok/002.jpg"].shape) # (768,)
print(face["able_wanamakok/002.jpg"].dtype) # float32

# Validasi lintas domain — key harus identik
emotion = joblib.load("features/demogpairs_vit-emotion.pkl")
age     = joblib.load("features/demogpairs_vit-age.pkl")
assert set(face.keys()) == set(emotion.keys()) == set(age.keys())
```

### 4.3 Mengapa *Offline* & Terkompresi?

| Keputusan | Alasan |
|---|---|
| ***Offline* (ekstraksi sekali, simpan, pakai ulang)** | (1) Inferensi ViT mahal (±4,5 jam CPU); tanpanya, setiap `GridSearchCV` 288 kombinasi akan mengulang inferensi 10.800 citra — tidak praktis. (2) Memastikan **fitur identik** untuk seluruh *classifier* (SVM, GNB, RF, LR) sehingga perbandingan adil. (3) Memungkinkan eksperimen klasifikasi dijalankan tanpa GPU. |
| **`joblib.dump(..., compress=9)`** | Kompresi `zlib` level 9 mengurangi ukuran ~10% tanpa kehilangan presisi (lossless). Level 9 dipilih karena ekstraksi hanya sekali — waktu kompresi tidak kritis, tetapi penghematan penyimpanan & I/O signifikan. |
| **Kunci `image_path` relatif** | Memungkinkan *join* via `d['image_path']` tanpa bergantung pada *absolute path* yang berbeda antar mesin. |

### 4.4 Lokasi Berkas & `.gitignore`

```
code/
├── features/
│   ├── demogpairs_vit-face.pkl      # 30.795.213 bytes — gitignored
│   ├── demogpairs_vit-emotion.pkl   # 30.789.736 bytes — gitignored
│   └── demogpairs_vit-age.pkl       # 30.781.253 bytes — gitignored
├── 1.1_vit-face_demogpairs.ipynb
├── 1.1_vit-emotion_demogpairs.ipynb
└── 1.1_vit-age_demogpairs.ipynb
```

Direktori `features/` di-*gitignore* karena ukurannya besar (±90 MB total) dan dapat diregenerasi kapan saja dengan menjalankan ulang tiga notebook `1.1_*`. Notebook ekstraksi sendiri tetap di-*track* sebagai bukti reproduksibilitas.

---

## 5. Strategi *Cross-Domain Feature Fusion* — *Concatenation*

### 5.1 Prinsip Dasar

*Fusion* dilakukan dengan **operasi *concatenation* vektor** — yaitu penyambungan (*append*) elemen-elemen vektor secara berurutan, **tanpa** penjumlahan, perkalian, atau proyeksi. Jika `a` berdimensi *m* dan `b` berdimensi *n*, maka `concat(a,b)` berdimensi *m+n* dan mempertahankan seluruh informasi asli kedua domain.

```
vit-face    : [ f1, f2, ..., f768 ]                          →  768-d
vit-emotion : [ e1, e2, ..., e768 ]                          →  768-d
vit-age     : [ a1, a2, ..., a768 ]                          →  768-d

Dual (face+emotion): [ f1..f768, e1..e768 ]                  → 1.536-d
Dual (face+age)    : [ f1..f768, a1..a768 ]                  → 1.536-d
Dual (emotion+age) : [ e1..e768, a1..a768 ]                  → 1.536-d

Tri (face+emotion+age): [ f1..f768, e1..e768, a1..a768 ]     → 2.304-d
```

Urutan *concatenation* konsisten dengan penamaan: `vit-emotion-face` berarti `[emotion | face]` (emosi dahulu, wajah kemudian), sesuai implementasi `list(emotion_features[key]) + list(face_features[key])`.

### 5.2 Dimensi Hasil Gabungan

| Kategori | Rumus Dimensi | Dimensi Akhir | Jumlah Kombinasi |
|---|---|---|---|
| **Single-Domain** | 768 | **768** | 3 |
| **Dual-Domain** | 768 + 768 | **1.536** | 3 |
| **Tri-Domain** | 768 + 768 + 768 | **2.304** | 1 |
| **Total** | — | — | **7** |

Dimensi ini diverifikasi di setiap notebook klasifikasi dengan:

```python
print('Jumlah fitur per gambar:', np.array(features[list(features.keys())[0]]).shape[0])
# Output: 768  (single), 1536 (dual), atau 2304 (tri)
```

### 5.3 Implementasi Kode (Disalin dari Notebook Aktual)

#### a) Single-Domain — Langsung pakai satu `.pkl`

```python
# Contoh: vit-face (notebook 2.x.1)
import joblib

features = joblib.load("features/demogpairs_vit-face.pkl")
print("Jumlah fitur per gambar:", np.array(features[list(features.keys())[0]]).shape[0])
# → 768

# Alternatif: vit-emotion (2.x.2), vit-age (2.x.3) — hanya ganti nama berkas
# features = joblib.load("features/demogpairs_vit-emotion.pkl")  # 768-d
# features = joblib.load("features/demogpairs_vit-age.pkl")      # 768-d
```

#### b) Dual-Domain — *Concatenation* dua `.pkl`

```python
# Contoh: vit-face-age (notebook 2.4.4 / 2.1.4)
import joblib, numpy as np
from tqdm import tqdm

face_features = joblib.load("features/demogpairs_vit-face.pkl")   # 768-d
age_features  = joblib.load("features/demogpairs_vit-age.pkl")    # 768-d

features = {}
for d in tqdm(data):
    key = d["image_path"]
    features[key] = np.array(list(face_features[key]) + list(age_features[key]))

print("Jumlah fitur per gambar:", np.array(features[list(features.keys())[0]]).shape[0])
# → 1536  (768 + 768)

# Varian lain (hanya ubah pasangan):
# vit-emotion-age  (2.x.5): list(emotion_features[key]) + list(age_features[key])     → 1536
# vit-emotion-face (2.x.6): list(emotion_features[key]) + list(face_features[key])    → 1536
```

#### c) Tri-Domain — *Concatenation* tiga `.pkl` (Usulan Utama)

```python
# Contoh: vit-face-emotion-age (notebook 2.1.7 / 2.4.7 — usulan utama 2304-d)
import joblib, numpy as np
from tqdm import tqdm
import utils as u

data = u.load_demogpairs()  # 10800 entri

face_features    = joblib.load("features/demogpairs_vit-face.pkl")      # 768-d
emotion_features = joblib.load("features/demogpairs_vit-emotion.pkl")   # 768-d
age_features     = joblib.load("features/demogpairs_vit-age.pkl")       # 768-d

features = {}
for d in tqdm(data):
    key = d["image_path"]
    features[key] = np.array(
        list(face_features[key]) +
        list(emotion_features[key]) +
        list(age_features[key])
    )

print("Jumlah fitur per gambar:", np.array(features[list(features.keys())[0]]).shape[0])
# → 2304  (768 + 768 + 768)
```

> **Catatan variasi nama variabel:** Notebook `2.1.7` (SVM tri-domain) menggunakan `vggface_features` sebagai nama variabel untuk `demogpairs_vit-face.pkl`; notebook GNB/RF/LR tri-domain menggunakan `face_features`. Keduanya merujuk pada berkas yang identik — perbedaan hanya gaya penamaan, bukan isi.

### 5.4 Rekonstruksi Matriks Fitur untuk Klasifikasi

Setelah `features` (dict) terbentuk, seluruh notebook klasifikasi membangun matriks `X` dan label `y` dengan pola identik:

```python
import numpy as np
from sklearn.model_selection import train_test_split

X = np.array([features[d["image_path"]] for d in data])  # [10800, D]
y = np.array([d["label_idx"] for d in data])              # [10800], nilai 0..5

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,       # 8640 latih / 2160 uji
    stratify=y,          # jaga proporsi 6 kelas
    random_state=42
)
# X_train.shape → (8640, 768) atau (8640, 1536) atau (8640, 2304)
# X_test.shape  → (2160, 768) atau (2160, 1536) atau (2160, 2304)
```

---

## 6. *Ablation Study* — 7 Konfigurasi Fitur yang Dievaluasi

Untuk mengukur kontribusi masing-masing domain dan kombinasinya, penelitian mengevaluasi **7 konfigurasi fitur** secara sistematis. Setiap konfigurasi diuji pada **4 keluarga *classifier*** (SVM, GNB, Random Forest, Logistic Regression) dengan *GridSearchCV* yang identik, sehingga perbedaan performa murni merefleksikan kualitas representasi fitur.

### 6.1 Tabel Lengkap 7 Konfigurasi

| # | Kode Konfigurasi | Domain Penyusun | Dimensi | Kategori | Berkas Sumber | Notebook Klasifikasi |
|---|---|---|---|---|---|---|
| 1 | `vit-face` | Face saja | **768** | Single | `vit-face.pkl` | `2.1.1`, `2.2.1`, `2.4.1`, `2.5.1` |
| 2 | `vit-emotion` | Emotion saja | **768** | Single | `vit-emotion.pkl` | `2.1.2`, `2.2.2`, `2.4.2`, `2.5.2` |
| 3 | `vit-age` | Age saja | **768** | Single | `vit-age.pkl` | `2.1.3`, `2.2.3`, `2.4.3`, `2.5.3` |
| 4 | `vit-face-age` | Face + Age | **1.536** | Dual | `vit-face.pkl` + `vit-age.pkl` | `2.1.4`, `2.2.4`, `2.4.4`, `2.5.4` |
| 5 | `vit-emotion-age` | Emotion + Age | **1.536** | Dual | `vit-emotion.pkl` + `vit-age.pkl` | `2.1.5`, `2.2.5`, `2.4.5`, `2.5.5` |
| 6 | `vit-emotion-face` | Emotion + Face | **1.536** | Dual | `vit-emotion.pkl` + `vit-face.pkl` | `2.1.6`, `2.2.6`, `2.4.6`, `2.5.6` |
| 7 | **`vit-face-emotion-age`** | **Face + Emotion + Age** | **2.304** | **Tri (Usulan Utama)** | **Ketiga `.pkl`** | **`2.1.7`, `2.2.7`, `2.4.7`, `2.5.7`** |

### 6.2 Pengelompokan Kategori

#### Kategori A — *Single-Domain* (768-d): *Baseline* per Domain

Bertujuan mengukur kekuatan diskriminatif masing-masing ViT secara terisolasi. Dari eksperimen, `vit-face` secara konsisten unggul di kategori ini (wajar — biometrik adalah sinyal terkuat untuk ras–gender), tetapi masih meninggalkan *gap* yang ditutup oleh kombinasi multi-domain.

- **`vit-face` (768-d):** Biometrik murni. Kuat pada struktur global, lemah pada variasi tekstur halus.
- **`vit-emotion` (768-d):** Dinamika ekspresi murni. Paling lemah sebagai *single* (emosi bukan prediktor utama ras), tetapi bernilai sebagai pelengkap.
- **`vit-age` (768-d):** Tekstur penuaan murni. Menengah — menangkap variasi kulit yang berkorelasi dengan ras/gender.

#### Kategori B — *Dual-Domain* (1.536-d): Sinergi Dua Domain

Menguji apakah dua domain saling melengkapi. Setiap pasangan menghilangkan satu domain untuk melihat penurunannya (*leave-one-out* implisit):

- **`vit-face-age` (1.536-d):** Geometri + tekstur. Mengkompensasi kelemahan `vit-face` pada variasi usia/kulit.
- **`vit-emotion-age` (1.536-d):** Dinamika + tekstur. Tanpa biometrik — konfigurasi terlemah di kategori dual, membuktikan biometrik tetap esensial.
- **`vit-emotion-face` (1.536-d):** Dinamika + biometrik. Kombinasi dual terbaik di banyak *classifier* (mis. RF terbaik pada `vit-emotion-face`), menunjukkan emosi memperkuat biometrik.

#### Kategori C — *Tri-Domain* (2.304-d): Usulan Utama

- **`vit-face-emotion-age` (2.304-d):** Penggabungan simultan ketiga domain. Secara teori, ruang fitur menangkap **geometri + dinamika + tekstur** sekaligus, sehingga paling kaya dan paling tahan terhadap variasi intra-kelas (mis. wajah tersenyum, wajah menua, variasi iluminasi). Konfigurasi ini menjadi **usulan utama** penelitian dan diuji sebagai `2.x.7` pada setiap keluarga *classifier*.

### 6.3 Matriks *Ablation* (Visual)

```
                    Face (768)   Emotion (768)   Age (768)
                    ──────────   ─────────────   ─────────
vit-face               ●              ○             ○         768
vit-emotion            ○              ●             ○         768
vit-age                ○              ○             ●         768
vit-face-age           ●              ○             ●        1536
vit-emotion-age        ○              ●             ●        1536
vit-emotion-face       ●              ●             ○        1536
vit-face-emotion-age   ●              ●             ●        2304  ← usulan utama
```

### 6.4 Pemetaan Notebook per Konfigurasi

Setiap konfigurasi dieksekusi pada 4 *classifier* — total **28 notebook klasifikasi** (`2.1` SVM, `2.2` GNB, `2.4` RF, `2.5` LR):

| Konfigurasi | SVM (`2.1.*`) | GNB (`2.2.*`) | RF (`2.4.*`) | LR (`2.5.*`) |
|---|---|---|---|---|
| `vit-face` | `2.1.1` | `2.2.1` | `2.4.1` | `2.5.1` |
| `vit-emotion` | `2.1.2` | `2.2.2` | `2.4.2` | `2.5.2` |
| `vit-age` | `2.1.3` | `2.2.3` | `2.4.3` | `2.5.3` |
| `vit-face-age` | `2.1.4` | `2.2.4` | `2.4.4` | `2.5.4` |
| `vit-emotion-age` | `2.1.5` | `2.2.5` | `2.4.5` | `2.5.5` |
| `vit-emotion-face` | `2.1.6` | `2.2.6` | `2.4.6` | `2.5.6` |
| `vit-face-emotion-age` | `2.1.7` | `2.2.7` | `2.4.7` | `2.5.7` |

Seluruh notebook *comparison* (`3.0_compare.ipynb`) dan *testing* (`4.0_test.ipynb`) kemudian membandingkan ke-7 konfigurasi secara *head-to-head* untuk menentukan pemenang global.

---

## 7. Rasional Multi-Domain: Mengapa Satu Domain Tidak Cukup?

Klasifikasi ras dan gender pada citra wajah rentan terhadap **bias visual** apabila hanya mengandalkan satu domain:

1. **Keterbatasan `vit-face` saja:** Fitur identitas sangat kuat membedakan bentuk biometrik global (mis. struktur rahang, jarak mata), tetapi dapat terdistorsi oleh variasi usia ekstrem (wajah anak vs lansia), ekspresi intens (tertawa lebar mengubah geometri bibir), atau iluminasi yang mengubah kontras. Tanpa kompensasi tekstur/emosi, model menjadi rapuh terhadap variasi intra-kelas.

2. **Nilai tambah `vit-emotion`:** Dinamika mikro wajah (*Action Units*, kerutan senyum, kontraksi dahi) memiliki pola yang **berkorelasi dengan gender** (mis. studi psikologi menunjukkan perbedaan *display rules* emosi antar gender) dan membantu memisahkan kelas ketika geometri biometrik ambigu. Emosi bukan prediktor utama ras, tetapi sebagai **fitur sekunder** ia menambah dimensi pemisah.

3. **Nilai tambah `vit-age`:** Tekstur kulit (kerapatan kerutan, elastisitas, pigmentasi, *photoaging*) bermanifestasi **berbeda antar ras** (mis. perbedaan ketebalan epidermis dan distribusi melanin) dan **antar gender** (mis. ketebalan kulit, kepadatan kolagen). Fitur usia menangkap sinyal mikro yang tidak terlihat oleh ViT-Face yang fokus pada geometri makro.

**Hipotesis sentral:** Ketiga representasi bersifat ***complementary* (saling melengkapi)**, bukan redundan. Penggabungan ketiganya memungkinkan ruang fitur menangkap **perbedaan interseksional yang halus** (*fine-grained intersectional differences*) — mis. membedakan *Asian Females* vs *White Females* tidak hanya dari bentuk mata, tetapi juga dari tekstur kulit dan pola ekspresi — sekaligus lebih **robust terhadap variasi intra-kelas** (usia, ekspresi, iluminasi) karena setiap variasi dikompensasi oleh domain lain.

---

## 8. Ringkasan Statistik Komputasi

| Metrik | ViT-Face | ViT-Emotion | ViT-Age | **Total** |
|---|---|---|---|---|
| **Citra diproses** | 10.800 | 10.800 | 10.800 | **32.400** (3×) |
| **Vektor dihasilkan** | 10.800 × 768 | 10.800 × 768 | 10.800 × 768 | **32.400 × 768** |
| **Kecepatan (it/s)** | 2,14 | 2,10 | 1,84 | — |
| **Durasi** | 1j 24m 04d (5.044 dtk) | 1j 25m 48d (5.148 dtk) | 1j 37m 45d (5.865 dtk) | **4j 27m 37d (16.057 dtk)** |
| **Berkas output** | `vit-face.pkl` | `vit-emotion.pkl` | `vit-age.pkl` | 3 berkas |
| **Ukuran berkas** | 30,79 MB | 30,78 MB | 30,78 MB | **±92,36 MB** |
| **Tipe data** | `float32` | `float32` | `float32` | — |
| ***Device*** | CPU | CPU | CPU | CPU |
| ***Batch size*** | 1 (per citra) | 1 (per citra) | 1 (per citra) | — |

> **Catatan reproduksibilitas:** Durasi di atas tercatat pada *device* CPU (`device(type='cpu')`) dengan *batch size* 1 (satu citra per *forward pass*). Pada GPU, kecepatan dapat meningkat 5–10×. Karena ekstraksi bersifat *offline*, durasi ini hanya dibayar sekali — seluruh 28 eksperimen klasifikasi berikutnya tidak lagi memerlukan inferensi ViT.

---

## 9. Dependensi & Reproduksibilitas

### 9.1 Dependensi Utama

```
torch
transformers (AutoModelForImageClassification, AutoImageProcessor)
Pillow (PIL.Image)
numpy
joblib
tqdm
pandas        # untuk load_demogpairs()
```

### 9.2 Langkah Reproduksi Lengkap

```bash
# 1. Instal dependensi (dari root repo)
pip install torch transformers Pillow numpy joblib tqdm pandas scikit-learn imbalanced-learn

# 2. Ekstraksi fitur (sekali jalan — menghasilkan 3 berkas .pkl)
# Jalankan berurutan (atau paralel di 3 proses berbeda):
jupyter nbconvert --to notebook --execute code/1.1_vit-face_demogpairs.ipynb
jupyter nbconvert --to notebook --execute code/1.1_vit-emotion_demogpairs.ipynb
jupyter nbconvert --to notebook --execute code/1.1_vit-age_demogpairs.ipynb
# Output: code/features/demogpairs_vit-{face,emotion,age}.pkl

# 3. Verifikasi
python -c "import joblib; print({k: len(v) for k,v in {'face': joblib.load('code/features/demogpairs_vit-face.pkl'), 'emotion': joblib.load('code/features/demogpairs_vit-emotion.pkl'), 'age': joblib.load('code/features/demogpairs_vit-age.pkl')}.items()})"
# → {'face': 10800, 'emotion': 10800, 'age': 10800}

# 4. Lanjut ke klasifikasi (tanpa perlu GPU/ViT lagi)
jupyter nbconvert --to notebook --execute code/2.1.7_svm_vit-face-emotion-age_demogpairs.ipynb
```

### 9.3 Invarian yang Dijaga

- **Determinisme fitur:** `model.eval()` + `torch.no_grad()` memastikan output identik setiap *run* (tidak ada *dropout* stokastik).
- **Konsistensi *key*:** Selalu `d['image_path']` relatif — tidak pernah `full_path` absolut.
- **Tipe data:** Selalu `float32` — tidak ada kuantisasi atau *half-precision*.
- **Token:** Selalu `[CLS]` (`feature_type='cls'`) — bukan *mean pooling*.

---

## 10. Referensi Silang Dokumen

- **Preprocessing citra & token `[CLS]`:** `experiment/02_preprocessing.md`
- **Metode klasifikasi & *GridSearchCV* 288 kombinasi:** `experiment/04_methods.md`
- **Hasil perbandingan 7 konfigurasi:** `experiment/05_results.md` & `code/3.0_compare.ipynb`
- **Implementasi ekstraksi:** `code/utils/extraction.py`, `code/utils/dataset.py`
- **Notebook ekstraksi:** `code/1.1_vit-face_demogpairs.ipynb`, `code/1.1_vit-emotion_demogpairs.ipynb`, `code/1.1_vit-age_demogpairs.ipynb`
- **Notebook klasifikasi (28):** `code/2.1.*` (SVM), `2.2.*` (GNB), `2.4.*` (RF), `2.5.*` (LR)

---

*Dokumen ini mendeskripsikan tahap ekstraksi fitur secara lengkap dan siap direplikasi. Seluruh angka durasi, ukuran berkas, dan dimensi diverifikasi langsung dari output notebook dan berkas `.pkl` aktual.*
