### Peer Review Report — Reviewer 1 (Methodology)

- **Reviewer Role**: Peer Reviewer 1 (Methodology & Statistical Rigor)
- **Dimensi Tanggung Jawab**: `D1` (methodology_rigor) & `D3` (argumentative_coherence / mathematical logic)
- **Target Venue**: **IEEE Access**
- **Rekomendasi**: **Major Revision** *(Konsolidasi Penilaian Panel Multi-Model)*
- **Confidence Score**: 5 / 5 (Sangat Tinggi — Desain Eksperimental, Validitas Statistik & Data Integrity)

---

## 1. Rencana Skoring Pra-Komitmen (Fase 1: Paper-Blind Phase)

Sebelum menelaah draf naskah secara penuh, Reviewer 1 menetapkan tolok ukur ketat metodologi:
- `what_to_look_for`:
  - Protokol pemisahan dataset: apakah partisi dilakukan pada tingkat identitas/subjek unik (*subject-disjoint / identity-level split*) untuk mencegah kebocoran identitas (*identity leakage*).
  - Isolasi rantai transformasi data (*data leakage check*): apakah penskalaan dan reduksi dimensi (PCA) hanya dipelajari dari data latih di setiap fold CV.
  - Validitas inferensial dan signifikansi statistik: ketersediaan uji hipotesis formal (misal: uji McNemar, paired permutation test, atau Wilcoxon test) dan pelaporan Interval Kepercayaan 95% (95% CI) untuk seluruh klaim keunggulan empiris.
  - Pelaporan metrik cross-validation (mean ± standar deviasi) untuk mengukur variabilitas pelatihan antar-fold.
  - Reprodusibilitas eksperimen: pencantuman *random seed* dan variasi eksplorasi penskalaan data.
- `what_triggers_block`:
  - Ambiguitas atau ketiadaan isolasi tingkat subjek pada dataset citra wajah yang memuat banyak foto per individu.
  - Klaim keunggulan model/fitur yang bertumpu pada selisih akurasi marjinal tanpa pembuktian signifikansi statistik (*unsubstantiated superiority claim*).
- `what_triggers_warn`:
  - Penggunaan metrik yang terdistorsi oleh ketidakseimbangan kelas lokal (misal: pelaporan akurasi biner One-vs-Rest tanpa metrik tingkat galat FPR/FNR).
  - Ketiadaan pelaporan nilai cross-validation fold (mean ± std) atau ketiadaan *random seed*.
- `what_triggers_fatal`:
  - Kebocoran data eksplisit (*explicit data leakage*) di mana transformasi data atau hyperparameter tuning melibatkan data uji independen.

`[CONTRACT-ACKNOWLEDGED]`

---

## 2. Ringkasan Penilaian Metodologi (Fase 2: Paper-Visible Phase)

Secara metodologis, naskah ini menunjukkan komitmen yang sangat baik terhadap pencegahan kebocoran data pada rantai transformasi fitur. Penulis merancang pipeline modular scikit-learn secara terpuji: modul `Scaler` dan `PCA` dipelajari secara eksklusif hanya pada data latih di dalam setiap fold 5-Fold Stratified Cross-Validation pada proses GridSearchCV (Persamaan 9). Dataset uji independen (20% = 2,160 citra) diisolasi secara ketat dan hanya disentuh pada evaluasi final.

Meskipun demikian, konsolidasi ulasan panel metodologi mengidentifikasi celah krusial yang memerlukan **Revisi Mayor** sebelum naskah dapat diterima di *IEEE Access*:
1. **Potensi Identity-Level Leakage pada DemogPairs**: Dataset DemogPairs memuat pasangan citra untuk verifikasi wajah. Penulis menyebutkan partisi 80/20 dilakukan melalui *stratified split*, namun tidak menjelaskan apakah pemisahan tersebut menjamin bahwa citra dari subjek/orang yang sama tidak pernah tersebar di data latih dan data uji secara bersamaan.
2. **Ketiadaan Uji Signifikansi Statistik & 95% CI**: Penulis mengklaim model fusi Tri-Domain ViT (Face ⊕ Emotion ⊕ Age) mengungguli Dual-Domain (Emotion ⊕ Face) pada SVM (93.70% vs 93.29%). Pada data uji $N=2,160$, selisih 0.41% ini hanya merepresentasikan **tepat 9 citra uji**! Penulis secara terbuka mengakui pada Bagian IV-A bahwa perbandingan ini bersifat deskriptif tanpa uji hipotesis formal. Selisih 9 sampel tanpa uji McNemar atau Interval Kepercayaan 95% tidak memiliki keabsahan inferensial di IEEE Access.
3. **Ketiadaan Pelaporan CV Score (Mean ± Std)**: Tabel hasil hanya menampilkan metrik titik tunggal (*point estimate*) pada data uji tanpa menyajikan performa rata-rata dan deviasi standar pada 5 fold cross-validation.
4. **Reproduktibilitas**: Ketiadaan pencantuman *random seed* dan keterbatasan variasi scaler (tidak mengevaluasi `StandardScaler`).

---

## 3. Poin Kekuatan Metodologis (Strengths)

- **S1: Isolasi Rantai Transformasi Fitur yang Sangat Ketat (`D1`)**:
  - Penulis secara eksplisit mengimplementasikan pipeline pemrosesan data modular di mana `Scaler` dan `PCA` di-fit hanya pada fold pelatihan di dalam `GridSearchCV`, mencegah kebocoran informasi (*data leakage*) ke fold validasi maupun set uji independen.
  - Evidence Anchor: `[section: 03_materials-and-methods_g-classification-pipeline]`, `[section: 01_introduction]`
- **S2: Eksplorasi Hyperparameter yang Masif dan Terdokumentasi (`D1`)**:
  - Grid search dieksekusi melintasi 1,086 kombinasi hyperparameter dengan total 38,010 proses fitting pada 5-Fold Stratified CV melintasi 7 skema representasi, mencakup ruang pencarian yang terdefinisi dengan sangat baik pada Tabel III, IV, V, dan VI.
  - Evidence Anchor: `[table: III]`, `[table: IV]`, `[table: V]`, `[table: VI]`
- **S3: Stratified Split dan Keseimbangan Kelas Seimbang (`D1`)**:
  - Partisi 80/20 dengan 1,440 citra latih dan 360 citra uji per subkelompok menjaga proporsi seimbang ~16.67% per kelas di setiap fold dan set evaluasi.
  - Evidence Anchor: `[table: I]`, `[section: 03_materials-and-methods_a-dataset]`
- **S4: Ketepatan Formulasi Matematis Pipeline dan Metrik (`D1`)**:
  - Persamaan (1) hingga (17) memformulasikan arsitektur ViT, konkatenasi representasi laten, fungsi kepadatan Gaussian, regresi Softmax multinomial, kernel polinomial SVM, hingga metrik agregasi makro secara matematis presisi dan koheren.
  - Evidence Anchor: `[section: 03_materials-and-methods_b-vision-transformer]`, `[section: 03_materials-and-methods_h-evaluation-metrics]`

---

## 4. Kelemahan Metodologis & Catatan Kritis (Weaknesses)

### W1: Ambiguitas Pembagian Data Tingkat Identitas Subjek (Subject-Disjoint Partition)
- **ID Isu**: `ISSUE-METH-01`
- [dimension: D1]
- Severity: CRITICAL
- **Verbatim Trigger**: `"what_triggers_block: ambiguitas atau ketiadaan isolasi tingkat subjek pada dataset citra wajah yang memuat banyak foto per individu"`
- **Evidence Anchor**: `[section: 03_materials-and-methods_a-dataset]`, `[table: 1]`
- **Deskripsi Temuan**:
  Pada Bagian III-A ([Section III-A](03_materials-and-methods_a-dataset.md)), penulis menyatakan:
  > *"Untuk memastikan integritas pengujian empiris, dataset dibagi menggunakan prosedur stratified split 80/20... Pembagian tersebut menghasilkan 8,640 citra latih dengan 1,440 sampel per kelas serta 2,160 citra uji independen dengan 360 sampel per kelas, sebagaimana dirinci pada Table I."*
  
  Dataset DemogPairs dirancang oleh Hupont & Fernández (2019) ([25]) untuk pengujian verifikasi biometrik pasangan wajah (*pair-matching*), yang umumnya memuat beberapa variasi foto dari individu/subjek yang sama. Jika pembagian *stratified split* 80/20 dilakukan pada tingkat file citra acak (*image-level split*) tanpa pengelompokan berbasis identitas unik subjek (*subject/person ID-level split*), maka citra dari orang yang sama berpotensi masuk ke dalam data latih sekaligus data uji.
  
  Dalam tugas pengenalan atribut demografis, kebocoran identitas (*identity leakage*) merupakan cacat validitas fatal: classifier dapat "mengingat" wajah seseorang dari data latih dan memprediksi ras/gender pada data uji bukan berdasarkan generalisasi atribut biologis/visual, melainkan karena telah mengenali identitas individu tersebut. Penulis wajib mengklarifikasi apakah DemogPairs terdiri atas identitas unik per citra, atau jika terdapat multi-citra per identitas, apakah prosedur pemisahan telah menjamin pemisahan tingkat identitas (*subject-disjoint partitioning* dengan 0% overlap ID).
- **Rekomendasi Aksi**:
  1. Klarifikasi secara eksplisit struktur identitas subjek pada dataset DemogPairs yang digunakan: berapa jumlah subjek unik (*unique subjects*) di dalam 10,800 citra tersebut?
  2. Tegaskan dalam narasi Bagian III-A bahwa tidak ada subjek yang sama yang muncul bersamaan di data latih dan data uji (*strict subject-disjoint split*). Jika pemisahan sebelumnya hanya acak citra, penulis wajib memverifikasi bahwa tumpang tindih identitas bernilai nol.

### W2: Ketiadaan Uji Signifikansi Statistik Inferensial pada Selisih 0.41% dan 95% CI
- **ID Isu**: `ISSUE-METH-02`
- [dimension: D1]
- Severity: MAJOR
- **Verbatim Trigger**: `"what_triggers_block: klaim keunggulan model/fitur yang bertumpu pada selisih akurasi marjinal tanpa pembuktian signifikansi statistik"`
- **Evidence Anchor**: `[table: 10]`, `[section: 04_results-and-discussion_a-global-performance]`, `[section: 04_results-and-discussion_b-feature-ablation-study]`
- **Deskripsi Temuan**:
  Pada Bagian IV-A dan IV-B, penulis mengklaim bahwa fusi Tri-Domain (Face ⊕ Emotion ⊕ Age) menghasilkan performa klasifikasi tertinggi di antara seluruh konfigurasi, mencapai Akurasi 93.70% pada SVM, melampaui konfigurasi Dual-Domain Emotion ⊕ Face (93.29%).
  
  Pada sampel uji berukuran $N=2,160$:
  - Akurasi 93.70% = 2,024 prediksi benar (136 kesalahan).
  - Akurasi 93.29% = 2,015 prediksi benar (145 kesalahan).
  - **Selisih riil hanyalah 9 citra uji (0.41 percentage point)**!
  
  Penulis secara terbuka mengakui pada baris 67–68 Bagian IV-A ([Section IV-A](04_results-and-discussion_a-global-performance.md)):
  > *"Perbandingan tersebut bersifat deskriptif dan tidak membuktikan superioritas statistik suatu classifier karena penelitian ini tidak melakukan pengujian hipotesis formal."*
  
  Menambahkan satu domain fitur utuh (Age berdimensi 768, menambah dimensi sebesar 50% menjadi 2,304) untuk sekadar membalikkan 9 sampel tanpa pembuktian bahwa pergeseran ini bukan kebetulan stokastik (*random noise*) meragukan klaim kontribusi naskah. Penulis wajib melakukan uji statistik inferensial formal:
  - Uji **McNemar's test** dengan koreksi kontinuitas Edwards pada prediksi berpasangan data uji antara Tri-Domain vs Dual-Domain.
  - Perhitungan **Interval Kepercayaan 95% (95% CI)** (misal: Wilson score interval atau bootstrap 1,000 iterasi) untuk metrik Akurasi dan Macro F1-Score pada Tabel VII hingga Tabel X.
- **Rekomendasi Aksi**:
  1. Hitung dan laporkan nilai $p$-value uji McNemar antara model terbaik Tri-Domain dan Dual-Domain pada data uji.
  2. Cantumkan Interval Kepercayaan 95% (format: `Mean ± CI` atau `[Lower, Upper]`) pada seluruh tabel benchmark utama (Tabel VII, VIII, IX, X).
  3. Bahas hasil uji signifikansi tersebut pada Bagian IV-A untuk memberikan justifikasi inferensial yang kokoh bagi klaim keunggulan Tri-Domain.

### W3: Ketiadaan Pelaporan Skor Cross-Validation Fold (Mean ± Std)
- **ID Isu**: `ISSUE-METH-03`
- [dimension: D1]
- Severity: MAJOR
- **Verbatim Trigger**: `"what_triggers_warn: ketiadaan pelaporan nilai cross-validation fold"`
- **Evidence Anchor**: `[table: VII]`, `[table: VIII]`, `[table: IX]`, `[table: X]`
- **Deskripsi Temuan**:
  Tabel benchmark VII hingga X hanya melaporkan performa estimasi tunggal (*point estimate*) pada data uji held-out independen setelah model di-refit pada seluruh data latih. Penulis tidak melaporkan skor rata-rata dan deviasi standar validasi silang pada 5 fold pelatihan (`CV Score: Mean ± Std`). Melaporkan skor CV sangat krusial untuk membuktikan bahwa konfigurasi terbaik yang dipilih oleh GridSearchCV memang stabil melintasi seluruh lipatan data dan tidak mengalami varians overfitting yang tinggi.
- **Rekomendasi Aksi**:
  Tambahkan kolom `CV Score (Mean ± Std)` pada Tabel VII, VIII, IX, dan X untuk memperlihatkan stabilitas performa selama tahap optimasi hyperparameter.

### W4: Keterbatasan Informatif Metrik Akurasi OvR pada Klasifikasi 6-Kelas Seimbang
- **ID Isu**: `ISSUE-METH-04`
- [dimension: D1]
- Severity: MINOR
- **Verbatim Trigger**: `"what_triggers_warn: penggunaan metrik yang terdistorsi oleh ketidakseimbangan kelas lokal"`
- **Evidence Anchor**: `[section: 03_materials-and-methods_h-evaluation-metrics]`, `[table: 11]`
- **Deskripsi Temuan**:
  Pada Tabel XI ([Table XI](04_results-and-discussion_c-intersectional-subgroup-performance.md#tab11)), penulis melaporkan nilai *OvR Accuracy* yang sangat tinggi (berkisar antara 97.31% hingga 98.70%). Pada masalah klasifikasi 6-kelas seimbang, perbandingan sampel pada skema biner One-vs-Rest adalah 1 kelas positif berbanding 5 kelas negatif (rasio 1:5). Akibatnya, pengklasifikasi naif yang memprediksi seluruh sampel sebagai negatif akan secara otomatis memperoleh akurasi OvR sebesar $5/6 = 83.33\%$.
  
  Meskipun penulis telah menambahkan kalimat disclaimer pada narasi Bagian IV-C bahwa akurasi OvR dipengaruhi oleh rasio sampel negatif, menampilkan akurasi OvR sebagai metrik utama berpotensi memberikan ilusi performa yang terlalu optimistik (*inflated performance perception*). Evaluasi disparitas interseksional akan jauh lebih informatif jika dilengkapi dengan metrik tingkat galat spesifik seperti *False Positive Rate* (FPR) atau *False Negative Rate* (FNR) per subkelompok.
- **Rekomendasi Aksi**:
  Tambahkan kolom FPR/FNR atau gantikan penekanan Akurasi OvR pada Tabel XI dengan *Balanced Accuracy* atau *Specificity* per subkelompok guna mencerminkan disparitas klasifikasi secara lebih tajam dan objektif.

### W5: Random Seed Tidak Dilaporkan & Pilihan Scaler Terbatas
- **ID Isu**: `ISSUE-METH-05`
- [dimension: D1]
- Severity: MINOR
- **Verbatim Trigger**: `"what_triggers_warn: ketiadaan random seed"`
- **Evidence Anchor**: `[section: 03_materials-and-methods_g-classification-pipeline]`, `[table: III, IV, V, VI]`
- **Deskripsi Temuan**:
  1. Naskah tidak mencantumkan nilai *random seed* yang digunakan untuk pengacakan stratified split 80/20, inisialisasi StratifiedKFold 5-fold, dan inisialisasi model stokastik (khususnya Random Forest). Hal ini menghambat reproduktibilitas eksperimen secara presisi.
  2. Eksplorasi penskalaan fitur hanya mengevaluasi `None` dan `MinMaxScaler`. Mengingat representasi laten ViT dihasilkan dari Layer Normalization, evaluasi `StandardScaler` (z-score normalization) merupakan alternatif standar yang penting bagi model kernel SVM dan Logistic Regression.
- **Rekomendasi Aksi**:
  Cantumkan nilai seed acak pada Bagian III-G dan berikan justifikasi singkat mengenai pemilihan penskalaan fitur.

---

## 5. Ringkasan Status Dimensi Reviewer 1

| Dimensi | Status | Justifikasi Evaluasi |
|:---:|:---:|---|
| **D1** (*methodology_rigor*) | **`BLOCK`** | Terdapat 1 temuan berderajat `CRITICAL` (perlunya verifikasi bebas kebocoran identitas subjek/subject-disjoint split) dan 2 temuan `MAJOR` (ketiadaan uji signifikansi statistik formal seperti McNemar & 95% CI, serta ketiadaan pelaporan nilai cross-validation fold mean ± std). |
| **D3** (*argumentative_coherence*) | **`WARN`** | Klaim keunggulan mutlak Tri-Domain bertentangan dengan pengakuan eksplisit ketiadaan uji hipotesis formal pada teks naskah. |
