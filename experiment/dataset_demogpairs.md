# Dataset DemogPairs - Rangkuman & Spesifikasi Lengkap

> Dokumen ini merangkum dataset **DemogPairs** yang digunakan dalam penelitian klasifikasi ras–gender multi-kelas berbasis Vision Transformer (ViT) multi-domain. Semua angka telah diverifikasi langsung terhadap file metadata (`dataset/demogpairs/metadata/*.txt`), folder citra (`dataset/demogpairs/images/`), artefak fitur (`.pkl`), dan log audit ground-truth (`experiment/code/archive/audit_ledger.json`).

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

1. **Kuantifikasi bias demografis** — untuk pertama kalinya mengukur ketidakseimbangan identitas, gender, dan etnis pada dataset wajah publik populer (LFW, VGGFace, VGGFace2, IJB-B, CWF, dll.).
2. **Merilis DemogPairs** — *validation set* baru berisi **10.800 citra wajah** (*10.8K*) dan **58,3 juta pasangan verifikasi identitas** (*58.3M identity verification pairs*), yang didistribusikan dalam *fold* seimbang secara demografis: *Asian, Black, White × Female, Male*.
3. **Benchmark model SOTA** — evaluasi perilaku lintas-demografis pada model *deep face recognition* ternama (SphereFace, FaceNet, ResNet50) dan menunjukkan bahwa model-model tersebut menderita bias demografis yang sangat terstruktur dan merugikan.
4. **Protokol pengujian baru** — mengusulkan protokol validasi yang lebih tepat untuk menguji kemampuan generalisasi model pengenalan wajah lintas kelompok demografis.

### Abstrak (terjemahan ringkas)

> Meskipun pengenalan wajah berbasis *deep learning* telah mencapai hasil mengesankan, kontroversi muncul terkait bias ras dan gender yang mempertanyakan penerapannya pada skenario sensitif. Karya ini mengukur ketidakseimbangan demografis pada dataset wajah publik populer dan merilis DemogPairs — *validation set* seimbang yang memungkinkan benchmark yang adil antar kelompok demografis. Hasil eksperimen menunjukkan bias demografis yang sistematis pada model SOTA dan perlunya protokol evaluasi yang memperhatikan keseimbangan demografis.

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

* Pada CWF, VGGFace, dan LFW, lebih dari **83–89%** citra adalah etnis White — Asian dan Black sangat direpresentasikan rendah (< 10%).
* Gender pada LFW sangat timpang (74,2% Male), sedangkan CWF dan VGGFace2 juga condong ke Male.
* **DemogPairs** satu-satunya yang **seimbang sempurna**: 50% Female / 50% Male dan 33,3% untuk masing-masing ras (Asian / Black / White), sehingga ideal untuk evaluasi *fairness* dan generalisasi lintas-demografis.
* Ketidakseimbangan identitas (beberapa selebriti memiliki ratusan citra, lainnya hanya sedikit) memperparah bias pelatihan — DemogPairs mengatasinya dengan jumlah citra seragam per subjek.

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
| **Pasangan verifikasi** | **58,3 juta** pasangan verifikasi identitas (protokol verifikasi paper asli; tidak dipakai pada klasifikasi 6-kelas) |
| **Sumber citra** | Agregasi dari dataset publik (CWF, VGGFace2, dll. — kolom `db_code` pada metadata) |

> Verifikasi: `metadata/*.txt` masing-masing 1.800 baris × 6 file = 10.800; `images/**/*.jpg` = 10.800 file; tiap kelas memiliki tepat 100 folder subjek unik dengan 18 citra/subjek.

### 3.2 Enam Kelompok Demografis

| No. | Label Kelas (`label`) | Subjek | Citra | Proporsi Dataset |
|-----|-----------------------|:------:|:-----:|:----------------:|
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
|---|---|---|
| `db_code` | `CWF`, `VGGFace2` | Kode dataset sumber citra |
| `image_path` | `able_wanamakok/002.jpg` | Path relatif terhadap `images/` |

Saat dimuat melalui `utils.dataset.load_demogpairs()`, setiap baris diperkaya menjadi:

```python
{
    "db_code": "CWF",
    "image_path": "able_wanamakok/002.jpg",
    "full_path": "dataset/demogpairs/images/able_wanamakok/002.jpg",
    "label": "Asian_Females",  # nama kelas kanonik
    "label_idx": 5,  # indeks integer sesuai mapping
    "subject_id": "able_wanamakok",  # identitas unik untuk isolasi kelompok subjek
}
```

---

## 4. Pemetaan Label (`label_idx`) - Standar Penelitian Ini

### 4.1 Urutan Kanonik Kelas

Urutan alfabetis/kanonik yang didefinisikan di `utils/constants.py` (`DEMOGPairs_CLASSES`):

```python
DEMOGPairs_CLASSES = [
    "Asian_Females",  # indeks kanonik 0 (urutan list)
    "Asian_Males",  # indeks kanonik 1
    "Black_Females",  # indeks kanonik 2
    "Black_Males",  # indeks kanonik 3
    "White_Females",  # indeks kanonik 4
    "White_Males",  # indeks kanonik 5
]
```

### 4.2 Mapping `label → label_idx` yang Digunakan untuk Training

> **Penting:** Untuk kompatibilitas historis, mapping integer yang dipakai pada *training* dan evaluasi (`DEMOGPairs_LABEL_TO_IDX`) **tidak** mengikuti urutan alfabetis di atas, melainkan sebagai berikut (didefinisikan eksplisit di `utils/constants.py`):

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
    "Black_Males": 0,
    "White_Females": 1,
    "Asian_Males": 2,
    "White_Males": 3,
    "Black_Females": 4,
    "Asian_Females": 5,
}
DEMOGPairs_IDX_TO_LABEL = {v: k for k, v in DEMOGPairs_LABEL_TO_IDX.items()}
```

Semua notebook dan fungsi `load_demogpairs()` menggunakan mapping ini, sehingga `y = np.array([d['label_idx'] for d in data])` selalu menghasilkan label 0–5 sesuai tabel di atas.

---

## 5. Pembagian Data (Train / Test Split): Subject-Disjoint vs. Subject-Overlap

Untuk merespons secara langsung dan komprehensif catatan kritis **IEEE Access Reviewer 2 (Comment #2: Data Leakage and Generalization)**, repositori ini mengimplementasikan **dua protokol partisi data secara komparatif**:

### 5.1 Protokol Utama Revisi IEEE Access: Subject-Disjoint Split (Zero Data Leakage)

Pemisahan data dilakukan secara terstratifikasi murni pada tingkat identitas individu subjek (`subject_id`):
- Menggunakan fungsi kanonik `utils.dataset.split_demogpairs_subject_disjoint(data, train_ratio=0.8, random_state=42)`.
- Dari 100 subjek unik pada tiap kelas: **80 subjek dialokasikan untuk data latih** dan **20 subjek dialokasikan untuk data uji held-out independen**.
- **Data Latih:** 480 subjek × 18 citra = **8.640 citra** (1.440 citra per kelas).
- **Data Uji:** 120 subjek × 18 citra = **2.160 citra** (360 citra per kelas).
- **Tingkat Kebocoran Identitas (*Identity Overlap*):** **Tepat 0 subjek (0,00%)**. Seluruh 120 subjek uji belum pernah dilihat oleh model dalam bentuk apa pun.
- **Validasi Silang Terisolasi:** Proses GridSearchCV pada data latih menggunakan `StratifiedGroupKFold(n_splits=5, shuffle=True, random_state=42)` dengan `groups=groups_train` (16 subjek per kelas per fold). Tidak ada subjek yang muncul bersamaan di fold latih dan validasi (kebocoran antar-lipatan = 0%).

Implementasi kode:
```python
from utils.dataset import load_demogpairs, split_demogpairs_subject_disjoint

data = load_demogpairs()
train_idx, test_idx = split_demogpairs_subject_disjoint(
    data, train_ratio=0.8, random_state=42
)
# len(train_idx) == 8640 (480 subjek unik, 80 per kelas)
# len(test_idx)  == 2160 (120 subjek unik, 20 per kelas)
# set(subjects_train) ∩ set(subjects_test) == ∅ (Zero Overlap)
```

### 5.2 Protokol Baseline Historis: Subject-Overlap Split (100% Identity Leakage)

Sebelum revisi, pembagian dilakukan secara acak pada tingkat citra individual (*image-level stratified split*):
- Menggunakan `sklearn.model_selection.train_test_split(..., test_size=0.2, stratify=y, random_state=42)`.
- Menghasilkan 8.640 citra latih dan 2.160 citra uji (proporsi seimbang 16,67% per kelas).
- Namun, audit empiris membuktikan bahwa **593 dari 593 subjek unik pada set uji (100,00%) juga hadir pada set latih** dengan foto yang berbeda.
- Protokol ini dipertahankan sebagai dasar **Studi Ablasi Kebocoran Data (*Data Leakage Ablation Study*)** untuk membuktikan secara kuantitatif besaran *shortcut learning*.

### 5.3 Tabel Perbandingan Komparatif Kedua Protokol

| Karakteristik Partisi | Protokol Utama (Subject-Disjoint) | Protokol Historis (Subject-Overlap) | Catatan Kepatuhan Akademik |
|---|:---:|:---:|---|
| **Metode Partisi** | `split_demogpairs_subject_disjoint` | `train_test_split(stratify=y)` | Menjawab Reviewer 2 IEEE Access #2 |
| **Unit Pemisahan** | Subjek Individu (`subject_id`) | Citra individual (`image_path`) | Menghilangkan *identity shortcuts* |
| **Jumlah Subjek Latih** | **480 subjek** (80 per kelas) | 600 subjek (tersebar) | Keseimbangan subjek sempurna |
| **Jumlah Subjek Uji** | **120 subjek** (20 per kelas) | 593 subjek (tumpang tindih) | Subjek uji held-out murni |
| **Tingkat Kebocoran Identitas** | **0,00% (0 subjek bocor)** | **100,00% (593 subjek bocor)** | **Eliminasi tuntas kebocoran data** |
| **Citra Latih** | 8.640 citra (1.440 per kelas) | 8.640 citra (1.440 per kelas) | Ukuran data latih identik |
| **Citra Uji** | 2.160 citra (360 per kelas) | 2.160 citra (360 per kelas) | Ukuran data uji identik |
| **Skema Cross-Validation** | 5-Fold `StratifiedGroupKFold` | 5-Fold `StratifiedKFold` | Validasi silang bebas kebocoran |
| **Kemampuan yang Diuji** | Generalisasi pada identitas baru | Pengenalan pola citra bercampur | Generalisasi sejati vs hafalan |

---

## 6. Fitur Vision Transformer (768-D)

### 6.1 Tiga Domain ViT

Penelitian ini mengekstrak representasi wajah menggunakan **tiga model ViT pra-latih** yang masing-masing berspesialisasi pada domain berbeda. Fitur diambil dari token `[CLS]` (*last_hidden_state[:, 0, :]*) sehingga setiap citra menghasilkan vektor **768 dimensi** (`hidden_dim = 768`).

| Domain | Model HuggingFace (`model_path`) | File Fitur (`.pkl`) | Dimensi | Jumlah Vektor |
|--------|----------------------------------|----------------------|---------|---------------|
| **Wajah / Identitas** | `skutaada/VIT-VGGFace` | `features/demogpairs_vit-face.pkl` | **768-D** (`float32`) | 10.800 |
| **Emosi** | `dima806/facial_emotions_image_detection` | `features/demogpairs_vit-emotion.pkl` | **768-D** (`float32`) | 10.800 |
| **Usia** | `dima806/facial_age_image_detection` | `features/demogpairs_vit-age.pkl` | **768-D** (`float32`) | 10.800 |

* Verifikasi: `joblib.load(...)[key].shape == (768,)` untuk ketiga berkas; `len(dict) == 10.800`; *keys* berupa `image_path` (mis. `able_wanamakok/002.jpg`).
* Ekstraksi dilakukan via `utils.extraction.extract_vit_features(..., feature_type="cls")`.
* **Paritas Fitur Absolut:** Arsip fitur `.pkl` bersifat statis dan digunakan bersama oleh kedua protokol evaluasi, menjamin bahwa perbandingan performa terisolasi murni pada dampak protokol pemisahan data.

### 6.2 Varian Gabungan Fitur

Untuk eksperimen klasifikasi, vektor 768-D digabungkan (konkatenasi langsung) menjadi 7 varian representasi multi-domain:

| Varian Fitur | Dimensi Gabungan | Kategori Domain | Akurasi Subject-Disjoint (Zero Leakage) | Akurasi Historis (Subject-Overlap Baseline) |
|---|:---:|:---:|:---:|:---:|
| `vit-face` | 768-D | Single-Domain | 86,39% (LR) / 86,16% (SVM) | 90,83% (SVM) / 90,60% (LR) |
| `vit-emotion` | 768-D | Single-Domain | 85,79% (SVM) / 85,23% (LR) | 90,19% (SVM) / 88,47% (LR) |
| `vit-age` | 768-D | Single-Domain | 82,55% (SVM) / 81,48% (LR) | 87,64% (SVM) / 86,48% (LR) |
| `vit-face-age` | 1.536-D | Dual-Domain | 87,55% (SVM) / 87,41% (LR) | 92,55% (SVM) / 91,62% (LR) |
| `vit-emotion-age` | 1.536-D | Dual-Domain | 86,67% (LR) / 86,25% (SVM) | 92,08% (SVM) / 90,51% (LR) |
| `vit-emotion-face` | 1.536-D | Dual-Domain | 88,43% (SVM) / 87,45% (LR) | 93,29% (SVM) / 92,41% (LR) |
| `vit-face-emotion-age` | **2.304-D** | **Tri-Domain (Usulan Utama)** | **88,66% (LR) / 88,61% (SVM)** | **93,70% (SVM) / 92,73% (LR)** |

> **Catatan Kinerja Puncak:**
> 1. Pada tolok ukur bebas kebocoran (**Subject-Disjoint**), performa tertinggi dicapai oleh **Logistic Regression (LR) Tri-Domain (Akurasi 88,66%, F1 0,8868)** dan **SVM Tri-Domain (Akurasi 88,61%, F1 0,8863)**. Keduanya terbukti ekuivalen secara statistik melalui uji McNemar ($p = 1,0000$, selisih hanya +1 citra), namun LR unggul mutlak dalam efisiensi komputasi (>820× lebih cepat dan >330× lebih hemat memori).
> 2. Angka historis **93,70% (SVM Tri-Domain)** berasal dari protokol lama (**Subject-Overlap**) yang terinflasi oleh kebocoran data identitas subjek dan kini diposisikan sebagai baseline untuk studi ablasi kebocoran data.

---

## 7. Penggunaan Dataset dalam Penelitian Ini

### Tugas
**Klasifikasi interseksional 6-kelas (3 ras × 2 gender)** secara terpadu — memprediksi kombinasi ras dan gender sekaligus dalam satu model, bukan dua tugas terpisah.

### Alur Eksperimen Komparatif
1. **Ekstraksi Fitur Statis:** Setiap citra diproses oleh ketiga ViT untuk menghasilkan vektor 768-D per domain (total 10.800 vektor per berkas `.pkl`), disimpan dengan kompresi `joblib`.
2. **Evaluasi Sistem Dual-Benchmark:**
   - **Protokol Utama (Revisi IEEE Access):** Evaluasi 480 subjek latih / 120 subjek uji held-out independen via `split_demogpairs_subject_disjoint` (0% kebocoran identitas).
   - **Protokol Baseline Historis:** Evaluasi partisi tingkat citra 8.640 latih / 2.160 uji via `train_test_split` (100% kebocoran identitas).
3. **Optimasi Hyperparameter Terenkapsulasi:**
   - Pipeline: `MinMaxScaler` $\to$ `PCA(n_components=None/0.5/0.75)` $\to$ `Classifier`.
   - Subject-Disjoint: 5-Fold `StratifiedGroupKFold(groups=subject_id)` (38.010 fits + 28 refits).
   - Subject-Overlap: 5-Fold `StratifiedKFold` (38.010 fits + 28 refits).
   - Empat keluarga klasifikator: Support Vector Machine (SVM), Logistic Regression (LR), Random Forest (RF), Gaussian Naive Bayes (GNB).
4. **Evaluasi Holistik pada 2.160 Citra Uji:**
   - Metrik global: Akurasi, Macro Precision, Macro Recall, Macro F1, Interval Kepercayaan 95% Wilson Score.
   - Uji signifikansi statistik inferensial: Uji McNemar berpasangan dan Uji Eksak Binomial.
   - Profil efisiensi komputasi: Latensi inferensi per sampel (ms) dan ukuran penyimpanan model (MB).
   - Audit keadilan algoritmik: Per-class One-vs-Rest (OvR) metrics dan *Equal Opportunity Disparity*.
   - Studi komparatif ablasi kebocoran data: Analisis dampak *shortcut learning* (drop akurasi -4,07 pp pada LR, -5,09 pp pada SVM).

---

## 8. Catatan Rekonstruksi & Reproduksibilitas

* **Dependensi utama:** `transformers` (`AutoImageProcessor`, `AutoModelForImageClassification`), `torch`, `scikit-learn` (1.3+), `joblib`, `pandas`, `scipy`.
* **Perangkat keras:** `torch.device("cuda" if torch.cuda.is_available() else "cpu")` — ekstraksi ViT otomatis memakai GPU jika tersedia; inferensi klasifikator hilir berjalan efisien pada CPU multi-threading.
* **Reproduksibilitas partisi:** Selalu gunakan `utils.dataset.split_demogpairs_subject_disjoint` dengan `train_ratio=0.8` dan `random_state=42` untuk protokol bebas kebocoran, atau `train_test_split(stratify=y, test_size=0.2, random_state=42)` untuk mereplikasi baseline historis.
* **Mapping label:** Selalu gunakan pemetaan `DEMOGPairs_LABEL_TO_IDX` dari `utils/constants.py` untuk menjamin keselarasan indeks kelas (0=Black_Males, 1=White_Females, 2=Asian_Males, 3=White_Males, 4=Black_Females, 5=Asian_Females).
* **Lokasi dataset:** `experiment/code/dataset/demogpairs/` (`images/` di-*gitignore* untuk perlindungan hak cipta dataset; `metadata/` tetap ter-*track* di repositori git).
* **Sitiran:** Jika menggunakan DemogPairs, sitir Hupont & Fernández (IEEE FG 2019), DOI: `10.1109/FG.2019.8756625`.

---

*Dokumen diperbarui: 27 Oktober 2026 — diselaraskan secara komprehensif dengan temuan eksperimen Subject-Disjoint terbaru, tolok ukur historis, dan pemenuhan revisi IEEE Access.*
