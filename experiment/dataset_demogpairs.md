# Dataset DemogPairs - Rangkuman & Spesifikasi Lengkap

> Dokumen ini merangkum dataset **DemogPairs** yang digunakan dalam penelitian klasifikasi ras–gender multi-kelas berbasis Vision Transformer (ViT) multi-domain. Semua angka telah diverifikasi langsung terhadap file metadata (`dataset/demogpairs/metadata/*.txt`), folder citra (`dataset/demogpairs/images/`), dan artefak fitur (`.pkl`) di `experiment/code/`.

---

## 1. Informasi Paper Asli

| Atribut | Detail |
|---------|--------|
| **Judul** | *DemogPairs: Quantifying the Impact of Demographic Imbalance in Deep Face Recognition* |
| **Penulis** | Isabelle Hupont & Carles Fernández |
| **Konferensi** | 2019 14th IEEE International Conference on Automatic Face & Gesture Recognition (FG 2019) |
| **Bulan / Tahun** | Mei 2019 |
| **Halaman** | 1–7 |
| **Penerbit** | IEEE |
| **DOI** | [`10.1109/FG.2019.8756625`](https://doi.org/10.1109/FG.2019.8756625) |
| **ID IEEE** | `8756625` |
| **Kata Kunci** | *Face recognition; Training; Annotations; Benchmark testing; Manuals; Databases* |
| **Sitiran BibTeX** | `references/2019_DemogPairs Quantifying the Impact of Demographic Imbalance in Deep Face Recognition.bib` |

### Fokus & Kontribusi Paper

1. **Kuantifikasi bias demografis** - untuk pertama kalinya mengukur ketidakseimbangan identitas, gender, dan etnis pada dataset wajah publik populer (LFW, VGGFace, VGGFace2, IJB-B, CWF, dll.).
2. **Merilis DemogPairs** - *validation set* baru berisi **10.800 citra wajah** (*10.8K*) dan **58,3 juta pasangan verifikasi identitas** (*58.3M identity verification pairs*), yang didistribusikan dalam *fold* seimbang secara demografis: *Asian, Black, White × Female, Male*.
3. **Benchmark model SOTA** - evaluasi perilaku lintas-demografis pada model *deep face recognition* ternama (SphereFace, FaceNet, ResNet50) dan menunjukkan bahwa model-model tersebut menderita bias demografis yang sangat terstruktur dan merugikan.
4. **Protokol pengujian baru** - mengusulkan protokol validasi yang lebih tepat untuk menguji kemampuan generalisasi model pengenalan wajah lintas kelompok demografis.

### Abstrak (terjemahan ringkas)

> Meskipun pengenalan wajah berbasis *deep learning* telah mencapai hasil mengesankan, kontroversi muncul terkait bias ras dan gender yang mempertanyakan penerapannya pada skenario sensitif. Karya ini mengukur ketidakseimbangan demografis pada dataset wajah publik populer dan merilis DemogPairs - *validation set* seimbang yang memungkinkan benchmark yang adil antar kelompok demografis. Hasil eksperimen menunjukkan bias demografis yang sistematis pada model SOTA dan perlunya protokol evaluasi yang memperhatikan keseimbangan demografis.

---

## 2. Masalah Ketidakseimbangan pada Dataset Publik

Temuan utama Hupont & Fernández (2019) adalah dominasi etnis **White** dan ketidakseimbangan gender yang ekstrem pada dataset publik. Rasio jumlah citra antar-identitas bahkan mencapai **500:1** pada beberapa dataset.

| Dataset | Female (%) | Male (%) | Asian (%) | Black (%) | White (%) |
|---------|:----------:|:--------:|:---------:|:---------:|:---------:|
| CWF | 41,1% | 58,9% | 2,3% | 8,6% | **89,1%** |
| LFW | 25,8% | 74,2% | 6,2% | 8,5% | **85,3%** |
| VGGFace | 49,4% | 50,6% | 2,2% | 9,4% | **88,4%** |
| VGGFace2 | 40,7% | 59,3% | 6,9% | 9,2% | **83,9%** |
| IJB-B | 46,2% | 53,8% | 15,6% | 10,3% | **74,1%** |
| **DemogPairs** | **50,0%** | **50,0%** | **33,3%** | **33,3%** | **33,3%** |

**Interpretasi:**

* Pada CWF, VGGFace, dan LFW, lebih dari **83–89%** citra adalah etnis White - Asian dan Black sangat direpresentasikan rendah (< 10%).
* Gender pada LFW sangat timpang (74,2% Male), sedangkan CWF dan VGGFace2 juga condong ke Male.
* **DemogPairs** satu-satunya yang **seimbang sempurna**: 50% Female / 50% Male dan 33,3% untuk masing-masing ras (Asian / Black / White), sehingga ideal untuk evaluasi *fairness* dan generalisasi lintas-demografis.
* Ketidakseimbangan identitas (beberapa selebriti memiliki ratusan citra, lainnya hanya sedikit) memperparah bias pelatihan - DemogPairs mengatasinya dengan jumlah citra seragam per subjek.

---

## 3. Komposisi Dataset DemogPairs

### 3.1 Statistik Inti (terverifikasi)

| Statistik | Nilai |
|-----------|-------|
| **Total citra** | **10.800** citra wajah bersih (telah disaring dari citra rusak/berkualitas buruk) |
| **Total subjek (identitas unik)** | **600** identitas |
| **Citra per subjek** | **18** citra / subjek (seragam) |
| **Jumlah kelompok demografis** | **6** kelas interseksional (3 ras × 2 gender) |
| **Citra per kelas** | **1.800** citra / kelas |
| **Subjek per kelas** | **100** subjek / kelas |
| **Keseimbangan gender** | **50,0%** Female (5.400 citra) / **50,0%** Male (5.400 citra) |
| **Keseimbangan ras** | **33,3%** Asian (3.600 citra) / **33,3%** Black (3.600 citra) / **33,3%** White (3.600 citra) |
| **Pasangan verifikasi** | **58,3 juta** pasangan verifikasi identitas (sesuai paper asli - untuk protokol verifikasi; tidak dipakai pada klasifikasi 6-kelas) |
| **Sumber citra** | Agregasi dari dataset publik (CWF, VGGFace2, dll. - kolom `db_code` pada metadata, mis. `CWF`, `VGGFace2`) |

> Verifikasi: `metadata/*.txt` masing-masing 1.800 baris × 6 file = 10.800; `images/**/*.jpg` = 10.800 file; tiap kelas memiliki tepat 100 folder subjek unik dengan 18 citra/subjek.

### 3.2 Enam Kelompok Demografis

| No. | Label Kelas (`label`) | Subjek | Citra | Proporsi Dataset |
|-----|-----------------------|--------|-------|-----------------|
| 1 | `Asian_Females` | 100 | 1.800 | 16,67% |
| 2 | `Asian_Males` | 100 | 1.800 | 16,67% |
| 3 | `Black_Females` | 100 | 1.800 | 16,67% |
| 4 | `Black_Males` | 100 | 1.800 | 16,67% |
| 5 | `White_Females` | 100 | 1.800 | 16,67% |
| 6 | `White_Males` | 100 | 1.800 | 16,67% |
| **Total** | **6 kelas** | **600** | **10.800** | **100%** |

Pembagian ini menjamin setiap kombinasi ras–gender mendapat representasi identik, sehingga metrik *accuracy*, *precision*, *recall*, dan *F1* tidak terdistorsi oleh dominasi kelas mayoritas.

### 3.3 Struktur Penyimpanan di Repositori

```
experiment/code/dataset/demogpairs/
├── metadata/
│   ├── Asian_Females.txt   (1.800 baris)
│   ├── Asian_Males.txt     (1.800 baris)
│   ├── Black_Females.txt   (1.800 baris)
│   ├── Black_Males.txt     (1.800 baris)
│   ├── White_Females.txt   (1.800 baris)
│   └── White_Males.txt     (1.800 baris)
└── images/
    ├── able_wanamakok/     (contoh subjek Asian_Females, 18 .jpg)
    ├── 14th_dalai_lama/    (contoh subjek Asian_Males)
    ├── aisha_tyler/        (contoh subjek Black_Females)
    ├── 50_cent/            (contoh subjek Black_Males)
    ├── abigail_spencer/    (contoh subjek White_Females)
    ├── amir_arison/        (contoh subjek White_Males)
    └── ... (600 folder subjek, total 10.800 .jpg)
```

**Format metadata** (TSV/whitespace-separated, tanpa header eksplisit di file mentah, dibaca dengan `pd.read_csv(..., sep=r"\s+")`):

| Kolom | Contoh | Keterangan |
|-------|--------|------------|
| `db_code` | `CWF`, `VGGFace2` | Kode dataset sumber citra |
| `image_path` | `able_wanamakok/002.jpg` | Path relatif terhadap `images/` |

Saat dimuat melalui `utils.dataset.load_demogpairs()`, setiap baris diperkaya menjadi:

```python
{
  "db_code":    "CWF",
  "image_path": "able_wanamakok/002.jpg",
  "full_path":  "dataset/demogpairs/images/able_wanamakok/002.jpg",
  "label":      "Asian_Females",   # nama kelas kanonik
  "label_idx":  5                  # indeks integer sesuai mapping
}
```

---

## 4. Pemetaan Label (`label_idx`) - Standar Penelitian Ini

### 4.1 Urutan Kanonik Kelas

Urutan alfabetis/kanonik yang didefinisikan di `utils/constants.py` (`DEMOGPairs_CLASSES`):

```python
DEMOGPairs_CLASSES = [
    "Asian_Females",   # indeks kanonik 0 (urutan list)
    "Asian_Males",     # indeks kanonik 1
    "Black_Females",   # indeks kanonik 2
    "Black_Males",     # indeks kanonik 3
    "White_Females",   # indeks kanonik 4
    "White_Males",     # indeks kanonik 5
]
```

### 4.2 Mapping `label → label_idx` yang Digunakan untuk Training

> **Penting:** Untuk kompatibilitas historis, mapping integer yang dipakai pada *training* dan evaluasi (`DEMOGPairs_LABEL_TO_IDX`) **tidak** mengikuti urutan list di atas, melainkan sebagai berikut (didefinisikan eksplisit di `utils/constants.py`):

| `label_idx` | `label` (kelas) | Jumlah Citra | Jumlah Subjek |
|:-----------:|-----------------|:------------:|:-------------:|
| `0` | `Black_Males` | 1.800 | 100 |
| `1` | `White_Females` | 1.800 | 100 |
| `2` | `Asian_Males` | 1.800 | 100 |
| `3` | `White_Males` | 1.800 | 100 |
| `4` | `Black_Females` | 1.800 | 100 |
| `5` | `Asian_Females` | 1.800 | 100 |

```python
DEMOGPairs_LABEL_TO_IDX = {
    "Black_Males":   0,
    "White_Females": 1,
    "Asian_Males":   2,
    "White_Males":   3,
    "Black_Females": 4,
    "Asian_Females": 5,
}
DEMOGPairs_IDX_TO_LABEL = {v: k for k, v in DEMOGPairs_LABEL_TO_IDX.items()}
```

Alias kompatibel: `demogpairs_classes`, `demogpairs_label_to_idx`, `demogpairs_idx_to_label`.

Semua notebook (`1.1_*`, `2.*_*`) dan fungsi `load_demogpairs()` menggunakan mapping ini, sehingga `y = np.array([d['label_idx'] for d in data])` selalu menghasilkan label 0–5 sesuai tabel di atas.

---

## 5. Pembagian Data (Train / Test Split)

| Atribut | Detail |
|---------|--------|
| **Metode** | *Stratified Split* - `sklearn.model_selection.train_test_split(..., stratify=y)` |
| **Rasio** | **80% Train / 20% Test** |
| **Jumlah Train** | **8.640** citra (1.440 per kelas) |
| **Jumlah Test** | **2.160** citra (360 per kelas) |
| **`random_state`** | `42` (reproducible) |
| **`test_size`** | `0.2` |
| **Validasi silang** | `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)` pada fase *GridSearchCV* |

Kode (dari `2.1.7_svm_vit-face-emotion-age_demogpairs.ipynb`):

```python
from sklearn.model_selection import train_test_split
X = np.array([features[d['image_path']] for d in data])
y = np.array([d['label_idx'] for d in data])
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)
# len(X_train)==8640, len(X_test)==2160; tiap kelas 360 di test
```

Stratifikasi menjamin proporsi 16,67% per kelas tetap terjaga di kedua himpunan, sehingga evaluasi tidak bias terhadap kelas tertentu.

---

## 6. Fitur Vision Transformer (768-D)

### 6.1 Tiga Domain ViT

Penelitian ini mengekstrak representasi wajah menggunakan **tiga model ViT pra-latih** yang masing-masing berspesialisasi pada domain berbeda. Fitur diambil dari token `[CLS]` (*last_hidden_state[:, 0, :]*) sehingga setiap citra menghasilkan vektor **768 dimensi** (`hidden_dim = 768`).

| Domain | Model HuggingFace (`model_path`) | File Fitur (`.pkl`) | Dimensi | Jumlah Vektor |
|--------|----------------------------------|----------------------|---------|---------------|
| **Wajah / Identitas** | `skutaada/VIT-VGGFace` | `features/demogpairs_vit-face.pkl` | **768-D** (`float32`) | 10.800 |
| **Emosi** | `dima806/facial_emotions_image_detection` | `features/demogpairs_vit-emotion.pkl` | **768-D** (`float32`) | 10.800 |
| **Usia** | `dima806/facial_age_image_detection` | `features/demogpairs_vit-age.pkl` | **768-D** (`float32`) | 10.800 |

* Verifikasi: `joblib.load(...)[key].shape == (768,)` untuk ketiga file; `len(dict) == 10.800`; *keys* berupa `image_path` (mis. `able_wanamakok/002.jpg`).
* Ekstraksi dilakukan di notebook `1.1_vit-face_demogpairs.ipynb`, `1.1_vit-emotion_demogpairs.ipynb`, `1.1_vit-age_demogpairs.ipynb` via `utils.extraction.extract_vit_features(..., feature_type="cls")`.

### 6.2 Varian Gabungan Fitur

Untuk eksperimen klasifikasi, vektor 768-D dapat digabungkan (konkatenasi) menjadi representasi multi-domain:

| Varian | Dimensi Gabungan | Notebook |
|--------|:----------------:|----------|
| `vit-face` saja | 768-D | `2.1.1`, `2.2.1`, `2.4.1`, `2.5.1` |
| `vit-emotion` saja | 768-D | `2.1.2`, dst. |
| `vit-age` saja | 768-D | `2.1.3`, dst. |
| `vit-face + vit-age` | 1.536-D | `2.1.4`, dst. |
| `vit-emotion + vit-age` | 1.536-D | `2.1.5`, dst. |
| `vit-emotion + vit-face` | 1.536-D | `2.1.6`, dst. |
| `vit-face + vit-emotion + vit-age` (tri-domain) | **2.304-D** | `2.1.7`, `2.2.7`, `2.4.7`, `2.5.7` - **terbaik 93,70% accuracy (SVM)** |

Semua fitur disimpan sebagai `dict[str, np.ndarray]` terkompresi (`joblib.dump(..., compress=9)`) dengan *key* = `image_path`.

---

## 7. Penggunaan Dataset dalam Penelitian Ini

### Tugas

**Klasifikasi interseksional 6-kelas (3 ras × 2 gender)** secara terpadu - memprediksi kombinasi ras dan gender sekaligus dalam satu model, bukan dua tugas terpisah.

### Alur Eksperimen

1. **Ekstraksi fitur** - setiap citra DemogPairs diproses oleh ketiga ViT untuk menghasilkan vektor 768-D per domain (total 10.800 × 768 per file `.pkl`).
2. **Split** - 8.640 train / 2.160 test (stratified, `random_state=42`).
3. **Klasifikasi** - empat keluarga *classifier* dievaluasi dengan *GridSearchCV* + *StratifiedKFold* (5 lipatan):
   * **SVM** (`SVC` - `2.1.*`, terbaik tri-domain 93,70%),
   * **Gaussian Naive Bayes** (`2.2.*`),
   * **Random Forest** (`2.4.*`),
   * **Logistic Regression** (`2.5.*`).
   * Pipeline opsional: `MinMaxScaler` → `PCA(n_components=0.5/0.75)` → *classifier*.
4. **Evaluasi** - *accuracy*, *macro F1/precision/recall*, *classification report* per kelas, *confusion matrix*, dan **OvR Accuracy** per kelas (mis. Black_Males ~98,7% OvR) - lihat `md/` dan `results/demogpairs_*.json`.

### Fokus Penelitian

Menggabungkan representasi multi-domain dari Vision Transformer (Identitas, Emosi, Usia) untuk klasifikasi 6 kelas ras–gender yang **akurat dan seimbang** - memanfaatkan keseimbangan demografis DemogPairs agar model tidak bias terhadap kelompok mayoritas.

---

## 8. Catatan Rekonstruksi & Reproduksibilitas

* **Dependensi utama:** `transformers` (`AutoImageProcessor`, `AutoModelForImageClassification`), `torch`, `scikit-learn`, `imblearn`, `joblib`, `pandas`.
* **Perangkat:** `torch.device("cuda" if torch.cuda.is_available() else "cpu")` - ekstraksi ViT otomatis memakai GPU jika tersedia.
* **Reproduksibilitas split:** selalu gunakan `stratify=y` dan `random_state=42` agar pembagian 8640/2160 identik antar eksekusi.
* **Mapping label:** jangan mengasumsikan urutan alfabetis - selalu impor `DEMOGPairs_LABEL_TO_IDX` dari `utils/constants.py`.
* **Lokasi dataset:** `experiment/code/dataset/demogpairs/` (folder `images/` di-*gitignore* untuk citra; `metadata/` tetap ter-*track*).
* **Sitiran:** jika memakai DemogPairs, sitir Hupont & Fernández (FG 2019), DOI 10.1109/FG.2019.8756625.

---

*Dokumen diperbarui: 31 Agustus 2026 - diverifikasi terhadap `metadata/*.txt` (10.800 baris), `images/**/*.jpg` (10.800 file), `features/*.pkl` (768-D, 10.800 entri), dan `utils/constants.py`.*
