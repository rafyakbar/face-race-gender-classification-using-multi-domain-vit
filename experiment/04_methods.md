# Metode Klasifikasi — Support Vector Machine & Optimasi Hyperparameter

## Ringkasan

Metode klasifikasi yang diterapkan dalam penelitian ini adalah **Support Vector Classifier (SVC)** yang diintegrasikan ke dalam pipeline pembelajaran mesin modular (`imblearn.pipeline.Pipeline`). Pipeline ini mengkombinasikan tahap pra-pemrosesan vektor fitur (*scaling* dan reduksi dimensi *PCA*) dengan algoritma klasifikasi *Support Vector Machine* (SVM). 

Untuk memastikan model yang dihasilkan optimal dan bebas dari *data leakage*, dilakukan pencarian *hyperparameter* secara mendalam melalui **GridSearchCV** yang mengeksplorasi **288 kombinasi parameter** dengan validasi silang **5-Fold Stratified Cross-Validation** (1.440 proses fitting per eksperimen) pada 8.640 data latih.

---

## Arsitektur Pipeline Pembelajaran Mesin

Struktur pipeline modular yang dibangun pada setiap eksperimen:

```
                  Input Vektor Fitur (X_train)
                              │
                              ▼
        ┌──────────────────────────────────────────┐
        │ 1. Feature Scaler                        │
        │    Pilihan: None | MinMaxScaler()        │
        └─────────────────────┬────────────────────┘
                              │
                              ▼
        ┌──────────────────────────────────────────┐
        │ 2. Dimensionality Reducer (PCA)          │
        │    Pilihan: None | PCA(50%) | PCA(75%)   │
        └─────────────────────┬────────────────────┘
                              │
                              ▼
        ┌──────────────────────────────────────────┐
        │ 3. Classifier (SVC)                      │
        │    Pilihan: C, Kernel, Gamma, Degree     │
        └─────────────────────┬────────────────────┘
                              │
                              ▼
              Prediksi Kelas Demografis (0 .. 5)
```

### Implementasi Pipeline & Grid Search

```python
pipeline = Pipeline(steps=[
    ('scaler', None),      # Scaler opsional
    ('pca', None),         # PCA opsional
    ('classifier', None)   # Model klasifikasi SVC
])

grid_params = [
    {
        'scaler': [None, MinMaxScaler()],
        'pca': [None, PCA(n_components=0.5), PCA(n_components=0.75)],
        'classifier': [SVC()],
        'classifier__C': [0.01, 0.1, 1, 10],
        'classifier__kernel': ['rbf', 'poly', 'linear'],
        'classifier__gamma': ['scale', 'auto'],
        'classifier__degree': [2, 3],
        'classifier__tol': [1e-3],
        'classifier__probability': [True],
    }
]

skv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

grid_search = GridSearchCV(
    estimator=pipeline,
    param_grid=grid_params,
    cv=skv,
    refit='accuracy',
    scoring={
        'accuracy': 'accuracy', 
        'f1': 'f1_macro', 
        'precision': 'precision_macro', 
        'recall': 'recall_macro',
        'roc_auc_ovr': 'roc_auc_ovr'
    },
    n_jobs=int(joblib.cpu_count() * 0.6),
    verbose=1,
    error_score='raise',
    return_train_score=True
)
```

---

## Ruang Eksplorasi Hyperparameter (288 Kombinasi)

Tabel berikut merinci kombinasi hyperparameter yang dievaluasi dalam *Grid Search*:

| Komponen Pipeline | Parameter | Nilai Kandidat | Jumlah Pilihan |
|-------------------|-----------|----------------|:--------------:|
| **Scaler** | `scaler` | `None`, `MinMaxScaler()` | 2 |
| **PCA** | `pca` | `None`, `PCA(0.5)`, `PCA(0.75)` | 3 |
| **SVM Regularization** | `classifier__C` | `0.01`, `0.1`, `1`, `10` | 4 |
| **SVM Kernel** | `classifier__kernel` | `'rbf'`, `'poly'`, `'linear'` | 3 |
| **Kernel Gamma** | `classifier__gamma` | `'scale'`, `'auto'` | 2 |
| **Poly Degree** | `classifier__degree` | `2`, `3` | 2 |
| **Tolerance** | `classifier__tol` | `0.001` (konstan) | 1 |
| **Probability** | `classifier__probability` | `True` (konstan) | 1 |
| **Total Kombinasi** | — | 2 × 3 × 4 × 3 × 2 × 2 | **288** |

Dengan skema **5-Fold Cross-Validation**, setiap konfigurasi eksperimen menjalankan:
* Total Fits = 288 × 5 = 1.440 proses training dan validasi per model

---

## Metrik Evaluasi

Evaluasi performa model dilakukan secara kuantitatif melalui dua lapisan pengujian:

### 1. Metrik Global (Macro-Averaged)
* **Accuracy:** Proporsi seluruh prediksi yang benar terhadap total sampel data uji (N = 2.160).
  * `Accuracy = Total Prediksi Benar / Total Sampel Uji`
* **Macro Precision:** Rata-rata tidak berbobot dari presisi seluruh kelas:
  * `Macro Precision = (1 / K) * Σ Precision_i`
* **Macro Recall:** Rata-rata tidak berbobot dari recall seluruh kelas:
  * `Macro Recall = (1 / K) * Σ Recall_i`
* **Macro F1-Score:** Rata-rata harmonik dari Macro Precision dan Macro Recall:
  * `Macro F1-Score = (1 / K) * Σ [ (2 * Precision_i * Recall_i) / (Precision_i + Recall_i) ]`

### 2. Metrik Per-Kelas (One-vs-Rest)
Untuk menguji keadilan klasifikasi (*fairness* / *demographic disparity*), setiap kelas demografis dievaluasi secara mandiri dalam skema biner *One-vs-Rest (OvR)* terhadap 5 kelas lainnya:
* **One-vs-Rest Accuracy:** `(TP + TN) / (TP + TN + FP + FN)`
* **Class Precision, Recall, dan F1-Score**
* **Confusion Matrix 6×6:** Memetakan secara detail kesalahan klasifikasi silang (*cross-demographic confusion*) antara ras dan gender.

---

## Pengaturan Komputasi & Paralelisasi

* **Backend Paralel:** `joblib.parallel_backend('threading')`
* **Alokasi Sumber Daya:** 60% total core CPU logis (`n_jobs = int(cpu_count * 0.6)`).
* **Persistensi Model:** Model terbaik dan durasi komputasi disimpan dalam format serial terkompresi tingkat tinggi (`compress=9` via `joblib.dump`).
* **Penyimpanan Hasil:** Seluruh metrik pengujian, prediksi baris-per-baris, dan parameter terbaik dicatat dalam berkas JSON di direktori `results/`.
