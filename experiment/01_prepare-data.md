# 01 — Persiapan Data DemogPairs (Race × Gender Classification)

> **Tujuan dokumen:** Mendokumentasikan secara rinci tahap inventarisasi, validasi, pemuatan metadata, dan pembagian dataset DemogPairs yang digunakan pada seluruh 28 eksperimen penelitian ini. Dokumen ini adalah sumber kebenaran tunggal (*single source of truth*) untuk spesifikasi data.

---

## 1. Ringkasan Eksekutif

Penelitian ini menggunakan dataset **DemogPairs** (Hupont & Fernández, FG 2019) sebagai satu-satunya sumber citra wajah untuk tugas klasifikasi interseksional **6 kelas** (3 ras × 2 gender). Seluruh pipeline — mulai dari ekstraksi fitur ViT offline hingga evaluasi 28 model klasifikasi — bertumpu pada **satu pembagian data yang identik**, sehingga perbandingan antar-konfigurasi fitur dan antar-classifier bersifat adil (*apple-to-apple*) dan dapat direproduksi sepenuhnya.

| Atribut | Nilai |
|---------|-------|
| **Dataset** | DemogPairs — *Quantifying the Impact of Demographic Imbalance in Deep Face Recognition* (DOI: `10.1109/FG.2019.8756625`) |
| **Total citra** | **10.800** citra wajah bersih (terkurasi, bebas citra rusak/berkualitas buruk) |
| **Total identitas** | **600 subjek** unik — masing-masing **18 citra** per subjek |
| **Jumlah kelas** | **6 kelas interseksional** (3 ras × 2 gender), **1.800 citra per kelas** — seimbang sempurna, tanpa *class imbalance* |
| **Rasio gender** | 50% Female (5.400) / 50% Male (5.400) |
| **Rasio ras** | 33,3% Asian (3.600) / 33,3% Black (3.600) / 33,3% White (3.600) |
| **Pembagian data** | **Stratified 80/20** → **8.640 Train / 2.160 Test**, `stratify=y`, `random_state=42` |
| **Cakupan split** | **Satu split yang sama dipakai untuk semua 28 eksperimen** (7 skema fitur × 4 classifier) |
| **Lokasi fisik** | `experiment/code/dataset/demogpairs/` |

---

## 2. Latar Belakang Dataset & Motivasi Pemilihan

### 2.1 Masalah bias pada dataset publik

Mayoritas dataset wajah publik mengalami dominasi ras White (74–89%) dan ketidakseimbangan gender yang parah. DemogPairs dirancang untuk mengoreksi bias tersebut dengan distribusi yang seimbang sempurna pada tingkat identitas, gender, dan etnis:

| Dataset | Female | Male | Asian | Black | White |
|---------|:------:|:----:|:-----:|:-----:|:-----:|
| CWF | 41,1% | 58,9% | 2,3% | 8,6% | **89,1%** |
| LFW | 25,8% | 74,2% | 6,2% | 8,5% | **85,3%** |
| VGGFace | 49,4% | 50,6% | 2,2% | 9,4% | **88,4%** |
| VGGFace2 | 40,7% | 59,3% | 6,9% | 9,2% | **83,9%** |
| IJB-B | 46,2% | 53,8% | 15,6% | 10,3% | **74,1%** |
| **DemogPairs** | **50,0%** | **50,0%** | **33,3%** | **33,3%** | **33,3%** |

Rasio jumlah citra antar-identitas pada dataset publik juga timpang hingga 500:1; DemogPairs meratakan menjadi tepat **18 citra per identitas** untuk seluruh 600 subjek.

### 2.2 Fokus penggunaan dalam penelitian ini

Tidak seperti paper asli yang memakai DemogPairs untuk audit bias *face recognition*, penelitian ini memformulasikan ulang dataset sebagai tugas **klasifikasi 6 kelas (*single-label, 6-way intersectional classification*)** — satu label per citra yang mengkodekan kombinasi ras dan gender secara bersamaan. Detail lengkap profil demografis dataset tersedia di [`dataset_demogpairs.md`](./dataset_demogpairs.md).

---

## 3. Komposisi Dataset — 10.800 Citra, 6 Kelas @ 1.800

DemogPairs disusun dengan keseimbangan sempurna pada tiga level: **kelas, gender, dan ras**. Setiap kelas demografis terdiri dari **100 subjek x 18 citra = 1.800 citra**.

| No | Kelas (`label`) | Ras | Gender | Subjek | Citra | Proporsi | Indeks (`label_idx`) |
|:--:|-----------------|-----|:------:|:------:|:-----:|:--------:|:--------------------:|
| 1 | `Black_Males` | Black | Pria (Male) | 100 | **1.800** | 16,67% | **0** |
| 2 | `White_Females` | White | Wanita (Female) | 100 | **1.800** | 16,67% | **1** |
| 3 | `Asian_Males` | Asian | Pria (Male) | 100 | **1.800** | 16,67% | **2** |
| 4 | `White_Males` | White | Pria (Male) | 100 | **1.800** | 16,67% | **3** |
| 5 | `Black_Females` | Black | Wanita (Female) | 100 | **1.800** | 16,67% | **4** |
| 6 | `Asian_Females` | Asian | Wanita (Female) | 100 | **1.800** | 16,67% | **5** |
| | **Total** | **3 ras** | **2 gender** | **600** | **10.800** | **100%** | **0-5** |

> **Pemetaan indeks** di atas didefinisikan di `experiment/code/utils/constants.py` (`DEMOGPairs_CLASSES`, `DEMOGPairs_LABEL_TO_IDX`, `DEMOGPairs_IDX_TO_LABEL`) dan **tidak boleh diubah** — seluruh notebook, fitur `.pkl`, model, dan laporan confusion matrix mengacu pada urutan ini secara konsisten. Alias kompatibel `demogpairs_classes` / `demogpairs_label_to_idx` / `demogpairs_idx_to_label` juga tersedia via `utils/__init__.py`.

```python
# experiment/code/utils/constants.py
DEMOGPairs_CLASSES = [
    "Asian_Females",
    "Asian_Males",
    "Black_Females",
    "Black_Males",
    "White_Females",
    "White_Males",
]

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

Urutan `DEMOGPairs_CLASSES` (alfabetis) digunakan untuk iterasi pemuatan metadata, sedangkan `DEMOGPairs_LABEL_TO_IDX` menentukan urutan baris/kolom pada *confusion matrix* dan laporan klasifikasi.

---

## 4. Struktur Direktori & Format Metadata

### 4.1 Struktur fisik

```
experiment/code/dataset/demogpairs/
├── metadata/
│   ├── Asian_Females.txt   # 1.800 baris data + 1 baris header = 1.801 baris total
│   ├── Asian_Males.txt     # 1.800 baris data + 1 baris header
│   ├── Black_Females.txt   # 1.800 baris data + 1 baris header
│   ├── Black_Males.txt     # 1.800 baris data + 1 baris header
│   ├── White_Females.txt   # 1.800 baris data + 1 baris header
│   └── White_Males.txt     # 1.800 baris data + 1 baris header
└── images/
    ├── 14th_dalai_lama/
    ├── 50_cent/
    ├── aaron_yoo/
    ├── abigail_spencer/
    ├── able_wanamakok/
    └── ... (600 subdirektori identitas, masing-masing berisi 18 berkas .jpg)
            # Total: 10.800 berkas JPEG
```

* `metadata/` berisi 6 berkas teks (satu per kelas) — **tidak ada file gabungan**.
* `images/` berisi **600 folder identitas** (nama folder = nama orang, *lowercase* dengan underscore), masing-masing memuat 18 citra `.jpg` berukuran bervariasi (akan di-*resize* ke 224x224 pada tahap preprocessing ViT).

### 4.2 Format berkas metadata

Setiap berkas `*.txt` adalah **TSV/whitespace-separated** dengan **1 baris header** diikuti 1.800 baris data:

```
db_code image_path
CWF     able_wanamakok/002.jpg
CWF     able_wanamakok/004.jpg
CWF     able_wanamakok/007.jpg
VGGFace2 zachary_quinto/177.jpg
...
```

| Kolom | Tipe | Deskripsi |
|-------|------|-----------|
| `db_code` | `string` | Kode basis data asal citra: `CWF` (*Celebrities in the Wild Faces*) atau `VGGFace2`. Digunakan untuk audit provenance, **tidak dipakai sebagai fitur**. |
| `image_path` | `string` | Jalur relatif terhadap `images/` (format `{identitas}/{nomor}.jpg`). Menjadi **kunci utama** untuk mencocokkan citra dengan vektor fitur pada `features/demogpairs_vit-*.pkl`. |

Pemuatan memakai `pd.read_csv(meta_file, sep=r"\s+")` sehingga spasi/tab ganda tetap ditangani dengan benar. Baris header `db_code image_path` otomatis menjadi nama kolom DataFrame.

### 4.3 Kunci pencocokan fitur

Pada tahap ekstraksi fitur (`1.1_vit-*.ipynb`), setiap citra dipetakan ke vektor 768-d dengan kunci `image_path` yang identik dengan entri metadata. Dengan demikian `load_demogpairs()` dan `features/*.pkl` selalu selaras tanpa perlu *re-indexing*.

---

## 5. Prosedur Pemuatan Data (`load_demogpairs`)

### 5.1 Fungsi resmi

Seluruh notebook memakai fungsi tunggal `load_demogpairs()` dari `experiment/code/utils/dataset.py` (di-*re-export* via `utils/__init__.py`):

```python
# experiment/code/utils/dataset.py
import os
import pandas as pd
from .constants import DEMOGPairs_CLASSES, DEMOGPairs_LABEL_TO_IDX

def load_demogpairs(
    metadata_path: str = "dataset/demogpairs/metadata",
    images_path: str = "dataset/demogpairs/images",
) -> list[dict]:
    """Load DemogPairs dataset metadata and map to structured records."""
    data = []
    for class_name in DEMOGPairs_CLASSES:
        meta_file = os.path.join(metadata_path, f"{class_name}.txt")
        df = pd.read_csv(meta_file, sep=r"\s+")
        for row in df.to_dict("records"):
            row["full_path"] = os.path.join(images_path, row["image_path"])
            row["label"] = class_name
            row["label_idx"] = DEMOGPairs_LABEL_TO_IDX[class_name]
            data.append(row)
    return data
```

### 5.2 Struktur *record* yang dihasilkan

Fungsi mengembalikan `list[dict]` dengan panjang **10.800** elemen (urutan: iterasi per kelas sesuai `DEMOGPairs_CLASSES`). Setiap elemen memiliki 5 kunci:

| Kunci | Tipe | Contoh | Keterangan |
|-------|------|--------|------------|
| `db_code` | `str` | `"CWF"` | Asal dataset citra |
| `image_path` | `str` | `"able_wanamakok/002.jpg"` | Jalur relatif (kunci fitur) |
| `full_path` | `str` | `"dataset/demogpairs/images/able_wanamakok/002.jpg"` | Jalur lengkap untuk `Image.open()` |
| `label` | `str` | `"Asian_Females"` | Label string kelas |
| `label_idx` | `int` | `5` | Label numerik 0-5 sesuai `DEMOGPairs_LABEL_TO_IDX` |

### 5.3 Penggunaan di notebook

```python
import utils as u

data = u.load_demogpairs(
    metadata_path="dataset/demogpairs/metadata",
    images_path="dataset/demogpairs/images"
)
# len(data) == 10.800 — validasi pertama setelah pemuatan
assert len(data) == 10800

# Contoh akses
data[0]
# {'db_code': 'CWF', 'image_path': 'able_wanamakok/002.jpg',
#  'full_path': 'dataset/demogpairs/images/able_wanamakok/002.jpg',
#  'label': 'Asian_Females', 'label_idx': 5}
```

---

## 6. Pembagian Dataset — Stratified 80/20 (`random_state=42`)

### 6.1 Prinsip & motivasi

Karena setiap kelas memiliki jumlah sampel yang identik (1.800), pembagian **stratified** menjamin bahwa proporsi 16,67% per kelas dipertahankan persis di subset latih maupun uji. Tanpa stratifikasi, *random split* biasa berisiko menghasilkan fluktuasi kecil yang dapat mengganggu perbandingan *fairness* antar-kelompok demografis.

Parameter **`random_state=42`** mengunci generator bilangan acak, sehingga urutan pengacakan **deterministik dan dapat direproduksi** di semua lingkungan dan semua waktu eksekusi.

### 6.2 Kode pembagian (identik di seluruh 28 notebook)

```python
import numpy as np
from sklearn.model_selection import train_test_split

# features: dict {image_path: np.ndarray(768,)} dimuat dari features/demogpairs_vit-*.pkl
# data:     list[dict] dari load_demogpairs() — panjang 10.800

X = np.array([features[d['image_path']] for d in data])
y = np.array([d['label_idx'] for d in data])

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,      # 20% untuk test -> 2.160 sampel
    stratify=y,         # menjaga proporsi 6 kelas tetap identik
    random_state=42     # seed tetap untuk reproduktibilitas penuh
)

print(len(X_train), len(X_test))  # (8640, 2160)
```

* `test_size=0.2` -> 2.160 sampel uji, 8.640 sampel latih.
* `stratify=y` -> setiap kelas terbelah **1.440 / 360** secara eksak (80/20 per kelas).
* `random_state=42` -> partisi identik di setiap eksekusi ulang, tanpa perlu menyimpan indeks terpisah.
* `shuffle=True` adalah *default* `train_test_split`; dengan `random_state` yang terkunci, pengacakan tetap deterministik.

> **Catatan:** Tidak ada *validation set* terpisah. Validasi dilakukan di dalam subset latih (8.640) melalui **5-Fold Stratified Cross-Validation** pada tahap `GridSearchCV`. Subset uji (2.160) bersifat *held-out* murni — hanya dipakai sekali pada evaluasi akhir, tanpa pernah tersentuh selama *tuning* hyperparameter.

### 6.3 Rincian kuantitatif hasil pembagian

| Kelas (`label`) | Indeks | Total | Train (80%) | Test (20%) | Persentase per Subset |
|-----------------|:------:|:-----:|:-----------:|:----------:|:---------------------:|
| `Black_Males` | 0 | 1.800 | **1.440** | **360** | 16,67% |
| `White_Females` | 1 | 1.800 | **1.440** | **360** | 16,67% |
| `Asian_Males` | 2 | 1.800 | **1.440** | **360** | 16,67% |
| `White_Males` | 3 | 1.800 | **1.440** | **360** | 16,67% |
| `Black_Females` | 4 | 1.800 | **1.440** | **360** | 16,67% |
| `Asian_Females` | 5 | 1.800 | **1.440** | **360** | 16,67% |
| **Total** | - | **10.800** | **8.640** | **2.160** | **100%** |

Validasi stratifikasi (dapat dijalankan di notebook mana pun):

```python
from collections import Counter
print("Train:", Counter(y_train))  # Counter({0: 1440, 1: 1440, 2: 1440, 3: 1440, 4: 1440, 5: 1440})
print("Test: ", Counter(y_test))   # Counter({0: 360,  1: 360,  2: 360,  3: 360,  4: 360,  5: 360})
```

### 6.4 Peran masing-masing subset

| Subset | Ukuran | Peran |
|--------|--------|-------|
| **Training (8.640)** | 1.440 x 6 kelas | Pelatihan model + pencarian hyperparameter via **5-Fold Stratified CV** (`StratifiedKFold(n_splits=5, shuffle=True, random_state=42)`, `refit='accuracy'`). Seluruh *Grid Search* hanya melihat data ini. |
| **Testing (2.160)** | 360 x 6 kelas | **Held-out test set** — dipakai **hanya sekali** untuk evaluasi akhir (accuracy, macro precision/recall/F1, per-class OvR metrics, confusion matrix). Tidak pernah dipakai untuk *tuning* atau seleksi model. |

---

## 7. Konsistensi Split untuk Seluruh 28 Eksperimen — Jaminan Perbandingan yang Adil

### 7.1 Satu split, 28 eksperimen

Penelitian ini menjalankan **28 eksperimen** yang merupakan kombinasi lengkap dari:

* **7 skema konfigurasi fitur** (ablation study):
  1. `vit-face` (768-d, single-domain)
  2. `vit-emotion` (768-d, single-domain)
  3. `vit-age` (768-d, single-domain)
  4. `vit-face-age` (1.536-d, dual-domain)
  5. `vit-emotion-age` (1.536-d, dual-domain)
  6. `vit-emotion-face` (1.536-d, dual-domain)
  7. `vit-face-emotion-age` (2.304-d, tri-domain — usulan utama)

* **4 keluarga classifier**:
  1. **SVM** (`SVC`, 2.1.x — 288 kombinasi hyperparameter)
  2. **Gaussian Naive Bayes** (`GaussianNB`, 2.2.x)
  3. **Random Forest** (`RandomForestClassifier`, 2.4.x)
  4. **Logistic Regression** (`LogisticRegression`, 2.5.x)

> **Jaminan metodologis:** Ke-28 notebook (`2.1.1`-`2.5.7`) menggunakan **potongan kode `train_test_split` yang identik** — parameter `test_size=0.2`, `stratify=y`, dan `random_state=42` yang sama persis, tanpa modifikasi apa pun. Tidak ada *re-splitting* atau *re-shuffling* per eksperimen. Dengan demikian:
> * Setiap model melihat **8.640 sampel latih yang identik** dan dievaluasi pada **2.160 sampel uji yang identik**.
> * Perbedaan performa antar-eksperimen **hanya** berasal dari perbedaan representasi fitur dan/atau classifier — bukan dari variasi data.
> * Hasil dapat direproduksi bit-identik oleh siapa pun yang menjalankan ulang notebook dengan seed yang sama.

### 7.2 Mengapa tidak ada split berbeda per model?

* **Reproduksibilitas ilmiah:** Satu seed yang terkunci (`42`) menghilangkan sumber varians acak yang tidak perlu.
* **Keadilan ablation study:** Jika setiap skema fitur memakai split berbeda, selisih accuracy bisa disebabkan oleh keberuntungan pembagian data, bukan keunggulan fitur.
* **Efisiensi:** Tidak perlu menyimpan 28 versi indeks train/test terpisah — cukup satu logika yang diulang.
* **Konsistensi dengan validasi silang:** `StratifiedKFold(shuffle=True, random_state=42)` di dalam `GridSearchCV` juga memakai seed yang selaras, sehingga seluruh pipeline (split + CV) deterministik secara end-to-end.

### 7.3 Daftar 28 notebook yang berbagi split yang sama

| # | Fitur | SVM | GNB | RF | LR |
|:-:|-------|:---:|:---:|:--:|:--:|
| 1 | `vit-face` | `2.1.1` | `2.2.1` | `2.4.1` | `2.5.1` |
| 2 | `vit-emotion` | `2.1.2` | `2.2.2` | `2.4.2` | `2.5.2` |
| 3 | `vit-age` | `2.1.3` | `2.2.3` | `2.4.3` | `2.5.3` |
| 4 | `vit-face-age` | `2.1.4` | `2.2.4` | `2.4.4` | `2.5.4` |
| 5 | `vit-emotion-age` | `2.1.5` | `2.2.5` | `2.4.5` | `2.5.5` |
| 6 | `vit-emotion-face` | `2.1.6` | `2.2.6` | `2.4.6` | `2.5.6` |
| 7 | `vit-face-emotion-age` | `2.1.7` | `2.2.7` | `2.4.7` | `2.5.7` |

Semua notebook di atas memuat sel identik:

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42)
```

Verifikasi dapat dilakukan dengan `grep -r "random_state=42" experiment/code/2*.ipynb` — seluruh 28 berkas mengembalikan baris yang sama.

---

## 8. Validasi & Kontrol Kualitas Data

| Pemeriksaan | Cara Validasi | Hasil yang Diharapkan |
|-------------|---------------|-----------------------|
| **Kelengkapan metadata** | `len(open(f).readlines()) == 1801` per berkas (1 header + 1.800 data) | 6 berkas x 1.800 = 10.800 baris data |
| **Kelengkapan citra** | `len(list(Path(images).rglob("*.jpg"))) == 10800` | 600 folder x 18 citra = 10.800 JPEG |
| **Keseimbangan kelas** | `Counter(d['label'] for d in data)` | 1.800 per kelas, tepat |
| **Kunci fitur** | `set(data_image_paths) == set(features.keys())` untuk setiap `features/*.pkl` | Selaras sempurna |
| **Stratifikasi split** | `Counter(y_train)` dan `Counter(y_test)` | 1.440 / 360 per kelas |
| **Determinisme** | Jalankan `train_test_split` dua kali dengan seed sama | `np.array_equal` bernilai `True` |

---

## 9. Posisi Tahap Ini dalam Alur Penelitian Keseluruhan

```
[01] Persiapan Data (dokumen ini)
      │
      │  load_demogpairs() -> 10.800 records
      │  Stratified Split 80/20 (42) -> 8.640 train / 2.160 test  ──► dipakai ulang di 28 eksperimen
      ▼
[02] Preprocessing — ViT AutoImageProcessor (Resize 224x224, Normalisasi)
      │
[03] Feature Extraction — 3x ViT [CLS] (768-d) -> features/*.pkl (29,37 / 29,36 / 29,36 MB)
      │
[04] Methods — 7 skema fusion (768 / 1.536 / 2.304-d) x 4 classifier x GridSearchCV 5-Fold CV
      │
[05] Results — Evaluasi held-out 2.160 sampel (accuracy, macro F1, per-class OvR, confusion matrix)
```

Tahap persiapan data adalah **fondasi** yang menjamin bahwa seluruh hasil pada [`05_results.md`](./05_results.md) dan [`00_overview.md`](./00_overview.md) berasal dari partisi data yang identik dan tidak bias.

---

## 10. Referensi Silang

| Dokumen | Kaitan |
|---------|--------|
| [`dataset_demogpairs.md`](./dataset_demogpairs.md) | Spesifikasi lengkap DemogPairs (paper, demografi, motivasi keseimbangan) |
| [`00_overview.md`](./00_overview.md) | Ringkasan framework, 7 skema fitur, dan hasil ablation study |
| [`03_feature-extraction.md`](./03_feature-extraction.md) | Detail ekstraksi ViT-Face / Emotion / Age dan penyimpanan `.pkl` |
| [`04_methods.md`](./04_methods.md) | Konfigurasi Grid Search, 5-Fold CV, dan pipeline classifier |
| `experiment/code/utils/dataset.py` | Implementasi `load_demogpairs()` |
| `experiment/code/utils/constants.py` | Definisi `DEMOGPairs_CLASSES` & `DEMOGPairs_LABEL_TO_IDX` |

---

*Dokumen diperbarui: 2026 — Split 8.640/2.160 (`random_state=42`, `stratify=y`) yang terdokumentasi di sini adalah satu-satunya partisi yang digunakan untuk seluruh 28 eksperimen (7 fitur x 4 classifier) tanpa pengecualian.*
