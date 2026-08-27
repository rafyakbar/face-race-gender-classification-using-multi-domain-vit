# Gap Analysis: Face Race & Gender Demographic Recognition and Vision Transformer Fusion

> **Dasar Analisis**: Sintesis 10 Paper Terpilih (2022–2025) pada [`tren_analisis.md`](file:///G:/My%20Drive/Research/BIMA/Face%20Race%20Gender%203%20Fitur/research/related_works/sintesis_literatur/tren_analisis.md) dan [`literature_matrix.md`](file:///G:/My%20Drive/Research/BIMA/Face%20Race%20Gender%203%20Fitur/research/related_works/sintesis_literatur/literature_matrix.md)  
> **Tujuan**: Memetakan kesenjangan riset (G1–G8) dan memformulasikan kebaruan (*novelty*) serta posisi strategis penelitian kita.  
> **Tanggal**: 2026-08-21

---

## 1. Ringkasan Kesenjangan Riset

Berdasarkan analisis kritis terhadap 10 paper dalam korpus literatur (2022–2025), teridentifikasi **8 kesenjangan riset utama (G1–G8)** dalam ranah klasifikasi demografis wajah berbasis deep learning dan Vision Transformers. Delapan kesenjangan ini dirinci pada §2, kemudian diprioritaskan menjadi **4 fokus utama (P1–P4)** pada §3 yang dijawab secara tuntas oleh model usulan kita (*Tri-Domain ViT + SVM GridSearchCV pada DemogPairs*).

---

## 2. Formalisasi Kesenjangan G1–G8 dan Bukti Literatur

| Kode Gap | Nama Kesenjangan Riset | Deskripsi Masalah & Bukti dari Literatur |
|:--------:|------------------------|------------------------------------------|
| **G1** | **Keterbatasan Representasi Domain Tunggal (*Single-Domain Limitation*)** | Mayoritas metode hanya mengandalkan fitur biometrik identitas murni (Belcar 2022, Tahyudin 2024, Kalkatawi 2024), sehingga gagal menangkap variabilitas ekspresi mikro dan degradasi penuaan wajah yang dinamis. |
| **G2** | **Bias dan *Domain Shift* pada Dataset Monorasial / Tidak Seimbang** | Melatih model pada dataset satu ras (AFAD - hanya Asia) terbukti memicu *drop* akurasi tajam (~17%) pada uji lintas-ras (Tahyudin et al., 2024). Ketimpangan kelas pada dataset publik juga merusak akurasi minoritas (Kalkatawi 2024: Middle Eastern jatuh ke 38,5%). |
| **G3** | **Kerentanan Pengenalan Demografis terhadap Usia Ekstrem** | Pengenalan gender dan etnisitas mengalami tingkat kegagalan tertinggi pada anak-anak di bawah 10 tahun (error 43,07%) dan lansia di atas 80 tahun (error hingga 87,50%) karena ketiadaan fitur invarian penuaan (Tahyudin et al., 2024). |
| **G4** | **Tumpang Tindih Fenotipe pada Klasifikasi Multi-Etnis (*Phenotypic Overlap*)** | Pengenalan etnisitas hingga 6 kelas secara *end-to-end* tertahan pada akurasi 77,20% akibat tumpang tindih morfologi visual yang parah pada kelompok multirasial Hispanik dan Timur Tengah (Kalkatawi & Saeed, 2024). |
| **G5** | **Kelemahan dan Risiko Overfitting Classifier *SoftMax End-to-End*** | Lapisan Dense/SoftMax berbasis backpropagation rentan terjebak pada *local minima* dan mengalami overfitting pada embedding laten berdimensi tinggi (Sunitha 2022, Liao 2022). |
| **G6** | **Ketiadaan Evaluasi Keadilan Interseksional Terpadu (*Lack of Intersectional Fairness Audit*)** | Sebagian besar penelitian mengevaluasi ras atau gender secara terpisah tanpa mengaudit keadilan gabungan (3 Ras × 2 Gender = 6 kelas) secara simultan (Belcar 2022, Sunitha 2022, Ramachandran 2023). |
| **G7** | **Keterbatasan Eksplorasi Hyperparameter Pipeline Terintegrasi** | Optimasi classifier pada studi sebelumnya sering kali bersifat terbatas pada parameter model tunggal tanpa mengeksplorasi interaksi antara teknik *scaling*, reduksi PCA, dan jenis kernel secara komprehensif (Putri et al. ICVEE 2025: hanya 48 kombinasi; JIEET 2025: hanya 36 kombinasi). |
| **G8** | **Trade-off Antara Akurasi dan Keadilan Algoritmik** | Banyak metode mitigasi bias sebelumnya (seperti adversarial debiasing atau data augmentation) menurunkan akurasi klasifikasi demi mengejar metrik keadilan (Brinkmann et al., ICCV 2023; Ramachandran & Rattani, 2023). |

---

## 3. Kesenjangan Prioritas (P1–P4) sebagai Motivasi Riset Kita

| Prioritas | Kesenjangan Terkait | Solusi & Kontribusi Kebaruan Riset Kita (*Tri-Domain ViT + SVM*) |
|:---------:|:-------------------:|-------------------------------------------------------------------|
| **P1** | **G1 + G3 (Multi-Domain Synergy & Age Resilience)** | **Integrasi Tri-Domain ViT (Identitas + Emosi + Usia: 2.304-d):** Menyatukan `ViT-Face` (struktur statis), `ViT-Emotion` (ekspresi dinamis), dan `ViT-Age` (morfologi penuaan biologis) untuk menghasilkan representasi yang holistik dan kebal terhadap distorsi usia/ekspresi. |
| **P2** | **G2 + G6 (Dataset Balance & Intersectional Fairness)** | **Formulasi Interseksional 6-Kelas pada DemogPairs (10.800 Citra):** Menggunakan dataset yang berimbang sempurna (1.800 sampel per kelas pada 3 Ras × 2 Gender), mengeliminasi bias distribusi kelas dan mencapai F1 seimbang (0,9174–0,9614) di seluruh subkelompok. |
| **P3** | **G4 + G5 (Optimal Decision Boundary via Non-Linear SVM)** | **Support Vector Classifier (SVC) dengan Kernel Polinomial Derajat 2:** Menggantikan SoftMax/XGBoost dengan SVM berbasis optimasi margin cembung global ($C=10$, kernel `'poly'`, degree=2, gamma=`'scale'`), sukses mendongkrak akurasi hingga **93,70%** (Macro F1 **0,9369**). |
| **P4** | **G7 + G8 (Systematic GridSearch & Zero Trade-off)** | **Eksplorasi 288 Kombinasi Pipeline GridSearchCV (5-Fold Stratified CV):** Meneliti interaksi Scaler (none/Standard/Robust/MinMax), PCA (none/50/100/200), parameter $C$, kernel, degree, dan gamma secara empiris dan membuktikan bahwa representasi murni tanpa PCA/Scaler memberikan akurasi dan keadilan tertinggi tanpa *trade-off*. |

---

## 4. Matriks Posisi Riset Terhadap Literatur Terpilih

```
                                  [AKURASI KLASIFIKASI]
                                           ▲
                                           │
  93.70% ──────────────────────────────────┼───────────────────────────★ Riset Terkini Kita (Tri-ViT + SVM)
                                           │
  92.41% ──────────────────────────────────┼────────────◆ Putri et al. (Dual-ViT Face+Emotion + SVM, 2025)
                                           │
  89.07% ──────────────────────────────────┼────────────◆ Putri et al. (MD-ViT Face+Age + XGBoost, 2025)
                                           │
  81.74% ───────────────────■ Tahyudin     │
         (Cross-test Gender) (2024)        │
                                           │
  77.20% ────────────▲ Kalkatawi (2024)   │
         (6-Class End-to-End MaxViT)       │
                                           │
  61.74% ──● Belcar (2022)                 │
         (Middle-face CNN)                 │
                                           └────────────────────────────────────────►
                                             [KEKAYAAN DOMAIN & KEADILAN DEMOGRAFIS]
                                             Single-Domain ────> Dual-Domain ────> Tri-Domain
```

---

## 5. Kesimpulan Metodologis

1. Fusi tiga domain Vision Transformer (**ViT-Face + ViT-Emotion + ViT-Age**) terbukti secara konsisten memecahkan limitasi representasi domain tunggal dan menyediakan informasi ortogonal yang saling melengkapi.
2. Penggunaan **Support Vector Machine (SVM)** dengan kernel polinomial derajat 2 dan regularisasi $C=10$ terbukti jauh lebih unggul dalam memetakan batas keputusan non-linear pada ruang laten 2.304 dimensi dibandingkan arsitektur SoftMax *end-to-end* maupun model ensemble pohon (*XGBoost*).
3. Pengujian pada benchmark **DemogPairs (10.800 citra)** membuktikan bahwa sistem kita mencapai performa *state-of-the-art* (**93,70% akurasi**, **0,9369 Macro F1**, dan **0,9948 CV ROC-AUC**) dengan disparitas keadilan yang sangat rendah di seluruh 6 subkelompok interseksional.
