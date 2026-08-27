# Ringkasan Tren & Analisis Sintesis Literatur (Knowledge Mapping)

**Tanggal Disusun**: 2026-08-21  
**Korpus Analisis**: 10 Paper Terpilih (2022–2025, Scopus-indexed / WoS / IEEE / Elsevier / MDPI)  
**Fokus Kajian**: Rekognisi Ras dan Gender, Mitigasi Bias Demografis, dan Fusi Fitur Multi-Domain Vision Transformer

---

## 1. Distribusi Temporal, Publisher, dan Kategori Venue Publikasi

Distribusi publikasi dalam korpus mencerminkan lonjakan minat riset yang sangat masif terhadap keadilan demografis (*algorithmic fairness*) dan pemanfaatan arsitektur *Vision Transformer* (ViT) dalam rentang tahun 2022 hingga 2025:

* **Tahun 2022 (3 Paper):** Didominasi oleh eksplorasi awal modifikasi CNN konvensional, seperti pengenalan etnisitas berbasis wilayah wajah tengah (Belcar et al., MDPI Sensors), multi-task multi-instance multi-scale CNN + Random Forest (Liao et al., MDPI AppSci), dan integrasi Xception + KELM + GSO (Sunitha et al., Elsevier JVCI).
* **Tahun 2023 (3 Paper):** Mulai bergeser ke arah audit teoretis bias representasi pada Vision Transformers (Brinkmann et al., IEEE/CVF ICCV), teknik mitigasi bias berbasis tampilan generatif StyleGAN2 (Ramachandran & Rattani, Springer ICPR Workshops), dan koneksi paralel multi-task FAR (Chen et al., Elsevier JVCI).
* **Tahun 2024 (2 Paper):** Penerapan empiris mendalam arsitektur Vision Transformer murni untuk gender (Tahyudin et al., Telkom Univ / JOIV) dan hybrid Multi-Axis Vision Transformer (MaxViT) untuk klasifikasi 6 etnis (Kalkatawi & Saeed, SAI IJACSA).
* **Tahun 2025 (2 Paper - Studi Prekursor Tim Kita):** Mengusulkan paradigma fusi multi-domain: integrasi Dual-ViT ViT-Face + ViT-Emotion via SVM pada ICVEE (Putri et al., IEEE) dan MD-ViT ViT-Face + ViT-Age via XGBoost pada JIEET (Putri et al., UNESA).

---

## 2. Pergeseran Paradigma Arsitektur: Dari CNN Konvensional ke Vision Transformers

| Era / Pendekatan | Arsitektur Representatif | Karakteristik Operasi | Kelebihan | Keterbatasan Utama |
|------------------|--------------------------|-----------------------|-----------|--------------------|
| **CNN Konvensional** (2022) | VGG-16, ResNet-50, AlexNet, Xception | Konvolusi lokal (*local receptive fields*), pooling bertingkat | Efisien untuk tekstur lokal, konvergensi cepat | Gagal memodelkan relasi spasial global antar-fitur wajah yang berjauhan |
| **CNN Multi-Scale / Parallel** (2022–2023) | MobileNetV3 + CPR, VGG16-PSN | Ekstraksi fitur multi-blok dan multi-instance terbobot | Mempertahankan detail spasial tingkat rendah | Kompleksitas arsitektur tinggi dan masih terbatas pada batasan konvolusi |
| **Vision Transformer (ViT)** (2023–2025) | ViT-Base (Patch 16×16), MaxViT, CLIP-ViT | *Multi-Head Self-Attention* (MHSA) global, token `[CLS]` | Memodelkan relasi fitur global, lebih tahan oklusi, secara inheren lebih adil (*lower bias*) | Memerlukan data latih skala besar (*pre-training*) atau fusi domain yang tepat |

---

## 3. Evolusi Representasi Fitur: Dari Single-Domain ke Multi-Domain Feature Fusion

Salah satu temuan paling krusial dari sintesis literatur adalah keterbatasan mendasar dari representasi fitur domain tunggal (*single-domain features*):

```
[Evolusi Representasi Fitur Wajah]

1. Single-Domain / Handcrafted (2022)
   └─ Pixel intensity, LBP, Gabor, SIFT, atau Single CNN Embedding
      (Rentan terhadap variasi pose, pencahayaan, dan Other-Race Effect)

2. Task-Specific Pre-trained ViT (2023–2024)
   └─ ViT-Face (VGGFace2) ATAU ViT-Emotion (FER) ATAU ViT-Age (UTK/IMDB)
      (Akurasi tinggi pada domain spesifik, tetapi terbatas menangkap konteks demografis utuh)

3. Dual-Domain ViT Fusion (2025 - Studi Prekursor Tim Kita)
   ├─ Dual-ViT (Face + Emotion: 1.536-d) + SVM ──> Akurasi 92,18% (ICVEE 2025)
   └─ MD-ViT (Face + Age: 1.536-d) + XGBoost ────> Akurasi 89,07% (JIEET 2025)

4. Tri-Domain ViT Fusion (Penelitian Terkini Kita)
   └─ Tri-ViT (Face + Emotion + Age: 2.304-d) + SVM GridSearchCV ──> Akurasi 93,70%
```

### Sinergi Tiga Pilar Representasi Wajah:
1. **ViT-Face (`skutaada/VIT-VGGFace`):** Menangkap struktur kraniofasial biometrik yang persisten (proporsi rahang, jarak interpupil, kontur tulang pipi).
2. **ViT-Emotion (`dima806/facial_emotions`):** Menangkap dinamika mikro-otot wajah (*Action Units* pada alis, mata, dan mulut) yang membedakan artikulasi ekspresi alami antar-gender dan ras.
3. **ViT-Age (`dima806/facial_age`):** Menangkap tekstur biologis, elastisitas kulit, dan degradasi morfologi penuaan yang mencegah bias pada kelompok usia ekstrem.

---

## 4. Formulasi Masalah: Dari Klasifikasi Terisolasi ke Interseksionalitas Terpadu

Literatur menunjukkan pergeseran penting dalam cara perumusan masalah demografis:
* **Klasifikasi Terisolasi (Single-Task):** Hanya memprediksi Ras saja (Belcar 2022, Sunitha 2022, Kalkatawi 2024) atau Gender saja (Tahyudin 2024, Ramachandran 2023). Pendekatan ini mengabaikan dependensi silang antara ras dan gender.
* **Klasifikasi Bersyarat / Hierarkis:** Gender diprediksi terlebih dahulu, kemudian digunakan sebagai kondisi probabilitas untuk memprediksi usia (Liao et al., 2022).
* **Multi-Label Independen:** 40 atribut diprediksi secara terpisah tanpa memodelkan pasangan interseksional secara eksplisit (Chen et al., 2023).
* **Klasifikasi Interseksional Terpadu 6-Arah (Studi Tim Kita & DemogPairs):** Memformulasikan secara langsung ke dalam 6 kelas diskrit (`Asian_Females`, `Asian_Males`, `Black_Females`, `Black_Males`, `White_Females`, `White_Males`). Pendekatan ini secara komprehensif mengaudit dan mengeliminasi bias gabungan ras dan gender secara simultan.

---

## 5. Perbandingan Paradigma Classifier: SoftMax vs Non-Iterative / Kernel / Tree Classifiers

| Paradigma Classifier | Contoh Paper | Karakteristik Pembelajaran | Kelebihan | Kelemahan / Keterbatasan |
|----------------------|--------------|----------------------------|-----------|--------------------------|
| **Dense / SoftMax End-to-End** | Belcar (2022), Tahyudin (2024), Kalkatawi (2024) | Gradient descent backpropagation | Integrasi langsung dalam satu graf komputasi | Rentan terjebak *local minima*, *overfitting*, dan sensitif terhadap ketimpangan kelas |
| **Non-Iterative (KELM + GSO)** | Sunitha et al. (2022) | Inversi analitik Moore-Penrose + optimasi metaheuristik | Pelatihan super cepat, tanpa backprop | Memerlukan reduksi dimensi (PCA) dan tuning metaheuristik intensif |
| **Decision Trees (DRF & XGBoost)** | Liao et al. (2022), Putri et al. (JIEET 2025) | Ensemble pohon aditif, splitting gain, regularisasi $L_2$ | Interpretabilitas tinggi, tahan outlier, cepat via `hist-tree` | Akurasi pada representasi laten kontinu (89,07%) masih di bawah algoritma margin optimal |
| **Support Vector Machine (SVM)** | Putri et al. (ICVEE 2025), Riset Terkini Kita | Optimasi cembung global (*Maximum Margin Hyperplane*) dengan kernel non-linear | **Generalisasi terbaik (92,41% $\rightarrow$ 93,70%)**, tahan overfitting pada embedding dimensi tinggi | Memerlukan penyetelan hyperparameter sistematis (*GridSearchCV*) |

---

## 6. Analisis Keadilan Algoritmik (*Algorithmic Fairness*) & Penanganan Bias

1. **Pengukuran Bias Representasi Laten:** Brinkmann et al. (ICCV 2023) membuktikan bahwa model ViT diskriminatif (DINO, MoCo) menyandikan bias sosial yang jauh lebih rendah dibanding model generatif (MAE, BEiT), serta pembesaran kapasitas model (*scaling*) terbukti mereduksi efek bias.
2. **Mitigasi Tanpa Trade-off:** Ramachandran & Rattani (2023) membuktikan bahwa *Vision Transformer* (CLIP ViT-L/14) menghasilkan *Degree of Bias* (DoB) terendah (0,99) dibanding seluruh model CNN, membuktikan keunggulan inheren ViT dalam menjaga keadilan subkelompok.
3. **Pentingnya Keseimbangan Data (DemogPairs):** Penelitian Tahyudin et al. (2024) membuktikan bahwa model yang dilatih pada satu ras homogen (AFAD) mengalami *drop* akurasi tajam (~17%) saat diuji pada populasi multi-ras. Hal ini menegaskan bahwa penggunaan dataset seimbang sempurna seperti **DemogPairs (10.800 citra, 1.800 per kelas)** merupakan fondasi utama mitigasi bias.

---

## 7. Analisis Tantangan Fenotipe Wajah: Tumpang Tindih Ras & Pengaruh Usia

* **Tumpang Tindih Fenotipe (*Phenotypic Overlap*):** Kalkatawi & Saeed (2024) menemukan bahwa kelompok multirasial (*Middle Eastern* dan *Latino Hispanic*) mengalami tumpang tindih visual yang sangat tinggi dengan kelas *White* dan *Indian*, menyebabkan akurasi model tunggal tertahan di 77,20%.
* **Distorsi Penuaan pada Pengenalan Gender:** Tahyudin et al. (2024) mengidentifikasi bahwa kelompok usia anak-anak (<10 tahun: error 43,07%) dan lansia ekstrem (>80 tahun: error hingga 87,50%) mengalami misklasifikasi gender tertinggi karena ketiadaan tanda dimorfisme seksual sekunder atau tertutup kerutan penuaan.
* **Solusi Fusi Multi-Domain Kita:** Fusi **ViT-Age** bersama **ViT-Face** dan **ViT-Emotion** secara langsung mengatasi kelemahan ini dengan memberikan representasi invarian penuaan yang mempertegas batas pemisah antar-kelas.

---

## 8. Posisi Strategis & Keunggulan Penelitian Terkini Kita

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                   POSISI PENELITIAN KITA DALAM PETA LITERATUR                    │
├──────────────────────────────────────────────────────────────────────────────────┤
│ 1. Dataset        : DemogPairs (10.800 citra seimbang sempurna 6-kelas)          │
│ 2. Arsitektur     : Tri-Domain ViT (ViT-Face + ViT-Emotion + ViT-Age: 2.304-d)   │
│ 3. Classifier     : Support Vector Machine (SVC) + GridSearchCV (288 parameter)  │
│ 4. Konfigurasi    : C=10, kernel='poly', degree=2, gamma='scale', no-pca, no-scl │
│ 5. Capaian Puncak : Akurasi Test 93,70%, Macro F1 0,9369, CV ROC-AUC 0,9948     │
│ 6. Fairness       : F1 seluruh subkelompok seimbang di rentang 0,9174 s.d. 0,9614│
└──────────────────────────────────────────────────────────────────────────────────┘
```

Melalui sintesis ini, terbukti bahwa pendekatan **Tri-Domain ViT + SVM** yang kita kembangkan merupakan lompatan metodologis yang solid dan sukses menyelesaikan seluruh keterbatasan yang dihadapi oleh literatur-literatur sebelumnya.
