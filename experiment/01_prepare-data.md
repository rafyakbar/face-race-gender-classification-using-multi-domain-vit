# Persiapan Dataset — DemogPairs (Race & Gender Classification)

## Ringkasan

Tahap ini mencakup inventarisasi, pemuatan metadata, strukturisasi, dan pembagian dataset **DemogPairs**. DemogPairs merupakan benchmark citra wajah yang dirancang untuk menganalisis interseksionalitas demografis (kombinasi 3 kategori ras dan 2 gender) secara berimbang guna mengatasi permasalahan bias representasi (*fairness-aware machine learning*).

Dataset ini memuat total **10.800 citra wajah** yang terdistribusi secara seimbang sempurna (*balanced distribution*) ke dalam **6 kelompok demografis**, di mana setiap kelompok memiliki tepat **1.800 sampel citra**.

---

## Struktur Data & Direktori

```
dataset/demogpairs/
├── metadata/
│   ├── Asian_Females.txt   (1.800 baris metadata)
│   ├── Asian_Males.txt     (1.800 baris metadata)
│   ├── Black_Females.txt   (1.800 baris metadata)
│   ├── Black_Males.txt     (1.800 baris metadata)
│   ├── White_Females.txt   (1.800 baris metadata)
│   └── White_Males.txt     (1.800 baris metadata)
└── images/
    ├── able_wanamakok/
    ├── aisha_tyler/
    ├── 50_cent/
    ├── abigail_spencer/
    ├── amir_arison/
    └── ... (ratusan subdirektori identitas individu)
```

Setiap berkas metadata teks berisi dua kolom:
1. `db_code`: Kode basis data asal citra (misalnya `CWF` untuk *Celebrities in the Wild Faces*, atau `VGGFace2`).
2. `image_path`: Jalur relatif berkas citra berformat JPEG (`.jpg`).

---

## Definisi Kelas & Pemetaan Label (*Label Encoding*)

Penelitian ini memformulasikan klasifikasi ras dan gender sebagai tugas klasifikasi multi-kelas 6-arah (*6-class single-label classification*). Pemetaan indeks kelas pada implementasi kode (`utils.py` / `utilsv2.py`) adalah sebagai berikut:

| Indeks (`label_idx`) | Label Kelas (`label`) | Ras | Gender | Jumlah Sampel | Persentase |
|:--------------------:|-----------------------|-----|:------:|:-------------:|:----------:|
| **0** | `Black_Males` | Black | Pria (Male) | 1.800 | 16,67% |
| **1** | `White_Females` | White | Wanita (Female) | 1.800 | 16,67% |
| **2** | `Asian_Males` | Asian | Pria (Male) | 1.800 | 16,67% |
| **3** | `White_Males` | White | Pria (Male) | 1.800 | 16,67% |
| **4** | `Black_Females` | Black | Wanita (Female) | 1.800 | 16,67% |
| **5** | `Asian_Females` | Asian | Wanita (Female) | 1.800 | 16,67% |
| **Total** | **6 Subkelompok Demografis** | — | — | **10.800** | **100,00%** |

---

## Prosedur Pemuatan Data (*Data Loading*)

Pemuatan dataset dilakukan melalui fungsi `load_demogpairs()` yang memetakan setiap baris metadata menjadi dictionary terstruktur dengan penambahan jalur lengkap citra (`full_path`), nama label string (`label`), dan indeks numerik (`label_idx`):

```python
def load_demogpairs(metadata_path='dataset/demogpairs/metadata', images_path='dataset/demogpairs/images'):
    data = []
    for c in demogpairs_classes:
        metadata_full_path = f'{metadata_path}/{c}.txt'
        df = pd.read_csv(metadata_full_path, sep=r'\s+')
        data += [{
            **row, 
            'full_path': f"{images_path}/{row['image_path']}", 
            'label': c, 
            'label_idx': demogpairs_label_to_idx[c]
        } for row in df.to_dict('records')]
    return data
```

---

## Pembagian Dataset (*Dataset Splitting*)

Dataset dibagi menjadi dua subset independen menggunakan teknik **Stratified Train-Test Split** dengan rasio **80% Training : 20% Testing** dan penguncian seed acak (`random_state=42`).

```python
X = np.array([features[d['image_path']] for d in data])
y = np.array([d['label_idx'] for d in data])

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    stratify=y,
    random_state=42
)
```

### Rincian Kuantitatif Pembagian Subset

Stratifikasi menjamin bahwa setiap subset mempertahankan proporsi kelas yang identik dan berimbang sempurna:

| Kelas | Jumlah Total | Data Latih (*Train 80%*) | Data Uji (*Test 20%*) |
|-------|:------------:|:------------------------:|:---------------------:|
| `Black_Males` | 1.800 | 1.440 | 360 |
| `White_Females` | 1.800 | 1.440 | 360 |
| `Asian_Males` | 1.800 | 1.440 | 360 |
| `White_Males` | 1.800 | 1.440 | 360 |
| `Black_Females` | 1.800 | 1.440 | 360 |
| `Asian_Females` | 1.800 | 1.440 | 360 |
| **Total** | **10.800** | **8.640** | **2.160** |

* **Subset Pelatihan (8.640 sampel):** Digunakan untuk proses pelatihan model dan pencarian parameter optimal melalui 5-Fold Cross-Validation.
* **Subset Pengujian (2.160 sampel):** Ditahan secara ketat (*held-out test set*) dan hanya digunakan untuk pengujian performa akhir model secara obyektif tanpa bias seleksi.
