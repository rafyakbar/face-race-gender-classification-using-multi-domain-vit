# Point-by-Point Response to Reviewers Letter (Round 2)

**Target Journal:** *IEEE Access*  
**Manuscript Title:** Multi-Domain Vision Transformer Fusion for Intersectional Demographic Classification from Facial Images  
**Authors:** Dr. Ir. Ricky Eka Putra, S.Kom., M.Kom., Rezky Arisanti Putri, S.Kom., M.Kom., Dr. Yuni Yamasari, S.Kom., M.Kom., Rafy Aulia Akbar, S.Kom., M.Kom.  
**Revision Round:** Round 1 Revision (Resubmission Package)  
**Date of Resubmission:** September 27, 2026  

---

## I. Overview and Editorial Acknowledgments

Kepada Yang Terhormat Editor-in-Chief dan Dewan Penilai Ilmiah (*Peer Reviewers*) *IEEE Access*,

Kami menyampaikan apresiasi dan rasa terima kasih yang setinggi-tingginya kepada Dewan Editor serta seluruh panel Reviewer (Editor-in-Chief, Methodology Reviewer, Domain Expert, Cross-Perspective Analyst, dan Devil's Advocate) atas telaah kritis, komprehensif, dan wawasan metodologis mendalam yang telah diberikan pada naskah kami. Seluruh catatan kritis tersebut sangat berharga dalam memperkuat ketelitian metodologis, kejelasan klaim ilmiah, rigour inferensi statistik, serta kedalaman analisis dalam naskah kami.

Berdasarkan *Revision Roadmap Matrix* Putaran 1, kami telah melakukan serangkaian penyempurnaan menyeluruh pada seluruh naskah di direktori `paper/` tanpa melanggar batasan ilmiah maupun memerlukan pelatihan ulang model (*no retraining*), melainkan memanfaatkan seluruh bukti komputasi inferensial baru dari eksperimen signifikansi statistik (`experiment/code/3.1_statistical_significance.ipynb` dan file hasil `results/*.json`).

### Ringkasan Statistik Penyelesaian Catatan Telaah:
- **Total Catatan Reviewer**: 22 Catatan (2 Critical, 9 Major, 11 Minor)
- **Status Resolusi Penuh (`RESOLVED`)**: 20 Catatan
- **Status Batasan Sadar yang Diakui (`DELIBERATE_LIMITATION`)**: 2 Catatan (Identitas Subjek / *Subject-Disjoint Split* pada `ISSUE-METH-01` dan Proyeksi 2D Manifold t-SNE/UMAP pada `ISSUE-DOM-03`)
- **Total Perubahan Naskah**: 7 berkas modular naskah diperbarui (`01_introduction.md`, `03_materials-and-methods_a-dataset.md`, `04_results-and-discussion_a-global-performance.md`, `04_results-and-discussion_b-feature-ablation-study.md`, `04_results-and-discussion_c-intersectional-subgroup-performance.md`, `04_results-and-discussion_e-comparison-with-prior-studies.md`, `05_conclusion.md`).
- **Kepatuhan Format**: Seluruh paragraf mematuhi batas target jumlah kata (*word count limits*) di `paper_outline.md`, bebas kata terlarang, tanpa *em dash*, dan selaras dengan `rules/md_rules.txt`.

Berikut adalah tanggapan butir-per-butir (*point-by-point response*) resmi kami terhadap ke-22 isu yang diidentifikasi oleh panel penilai independen.

---

## II. Tanggapan Butir-per-Butir (Point-by-Point Responses)

### A. Editor-in-Chief (EIC) Issues

#### `ISSUE-EIC-01` (EIC — Major Comment 1: Distingsi Kontribusi vs Prosiding ICVEE 2025)
- **Reviewer Comment:**  
  > *"Risiko Persepsi Kontribusi Inkremental vs Publikasi Sendiri: Naskah memiliki kedekatan tematik dengan publikasi prosiding konferensi terdahulu (Putri et al., ICVEE 2025 [19] dan JIEET 2025 [20]). Diperlukan penegasan wawasan saintifik baru dan distingsi kontribusi konseptual yang jelas pada Bagian I dan Bagian IV-E agar naskah tidak dipersepsikan sebagai publikasi berulang (salami slicing)."*
- **Status:** `RESOLVED`
- **Author Response:**  
  Kami sangat berterima kasih atas catatan penting ini. Kami sepenuhnya sepakat bahwa distingsi konseptual dan wawasan saintifik baru naskah jurnal ini terhadap prosiding pendahuluan (Putri et al., ICVEE 2025 [[19]]) harus diartikulasikan secara transparan dan definitif.  
  Perbedaan fundamental naskah ini terhadap studi terdahulu adalah:
  1. *Eksplorasi Fusi Tri-Domain Lengkap*: Prosiding ICVEE 2025 hanya meneliti fusi dual-domain (`Emotion ⊕ Face`), sedangkan naskah ini mengevaluasi secara sistematis fusi tri-domain penuh (`Face ⊕ Emotion ⊕ Age`: 2.304 dimensi) yang mencakup 7 konfigurasi fitur komparatif.
  2. *Uji Inferensial & Fenomena Kejenuhan Laten*: Naskah ini menyajikan uji signifikansi statistik formal (Uji McNemar berpasangan, Wilson 95% CI, dan stabilitas 5-fold CV) yang pertama kali mengungkap fenomena *asymptotic feature saturation* pada representasi visual wajah.
  3. *Audit Keadilan Interseksional Formal*: Naskah ini menyajikan analisis keadilan algoritmik granular (*Equal Opportunity Difference* $\Delta \text{TPR}$) dan dinamika batas keputusan melintasi 4 famili algoritma klasik.
- **Changes Made:**
  - Pada `paper/01_introduction.md` (Paragraf 6, Butir 3): Kontribusi ilmiah dirumuskan ulang secara eksplisit untuk menegaskan distingsi dari prosiding konferensi:
    > *"A granular intersectional subgroup disparity and algorithmic fairness assessment on the DemogPairs dataset, systematically evaluating demographic consistency and error patterns across racial and gender intersections that explicitly advance beyond preliminary conference investigations (Putri et al. [[19]])."*
  - Pada `paper/04_results-and-discussion_e-comparison-with-prior-studies.md` (Paragraf 1):
    > *"Komparasi ini memposisikan kontribusi saintifik naskah ini sebagai evaluasi sistematis tri-domain laten dengan pengujian signifikansi serta batas keputusan yang melampaui studi prosiding konferensi terdahulu [[19]](06_references.md#ref19)."*
  - Lokasi Naskah: `paper/01_introduction.md` dan `paper/04_results-and-discussion_e-comparison-with-prior-studies.md`.

---

#### `ISSUE-EIC-02` (EIC — Minor Comment 1: Ketiadaan Statuta Wajib IEEE Access)
- **Reviewer Comment:**  
  > *"Ketiadaan Statuta Wajib IEEE (Data, Code, & Ethics): Sebagai jurnal open-access bereputasi tinggi, IEEE Access mewajibkan ketersediaan Data Availability Statement, Code Availability Statement, dan Ethical Compliance Statement yang jelas sebelum daftar pustaka."*
- **Status:** `RESOLVED`
- **Author Response:**  
  Kami sependapat sepenuhnya dengan Editor-in-Chief. Kepatuhan terhadap prinsip keterbukaan sains (*Open Science*), reproduktibilitas komputasi, dan etika kecerdasan buatan (*Responsible AI*) merupakan prasyarat mutlak naskah IEEE Access. Kami telah menambahkan ketiga subbab statuta wajib tersebut pada Bagian V (*Conclusion*).
- **Changes Made:**
  - Pada `paper/05_conclusion.md`, ditambahkan tiga subbab formal dalam English Title Case:
    1. `## Data Availability Statement`: Mencantumkan status dataset publik DemogPairs dan menyertakan pranala akses laman resmi publikasi (https://ihupont.github.io/publications/2019-05-16-demogpairs) serta tautan Google Drive repositori data (https://drive.google.com/file/d/1f_ez-ll6wxDXScrG4ceStZRuLT_K8Uy8/view?usp=sharing).
    2. `## Code Availability Statement`: Menyatakan ketersediaan repositori kode eksperimen, pipeline validasi silang, dan skrip analisis statistik (https://github.com/rafyakbar/face-race-gender-classification-using-multi-domain-vit).
    3. `## Ethical Compliance Statement`: Mendeklarasikan bahwa penelitian memanfaatkan data sekunder publik wajah manusia tanpa intervensi fisik partisipan baru, dilakukan murni untuk audit mitigasi bias algoritma visi komputer (*fairness auditing*), serta melarang keras penggunaan teknologi ini untuk profil demografis esensialis atau pengawasan massal tanpa persetujuan.
  - Lokasi Naskah: `paper/05_conclusion.md`.

---

#### `ISSUE-EIC-03` (EIC — Minor Comment 2: Poin Kontribusi Ilmiah Terlalu Panjang & Redundan)
- **Reviewer Comment:**  
  > *"Poin Kontribusi Ilmiah Redundan dan Terlalu Panjang: Bagian I Paragraf 6 memuat 4 poin kontribusi dengan panjang 261 kata yang mencampurkan klaim metodologis dan angka empiris secara berulang. Diperlukan pemadatan menjadi 3 butir ringkas, padat, dan berbobot ilmiah."*
- **Status:** `RESOLVED`
- **Author Response:**  
  Kami mengapresiasi koreksi tajam ini. Kami telah merevisi dan merampingkan poin-poin kontribusi ilmiah dari 4 butir menjadi tepat 3 butir kontribusi yang terfokus, elegan, dan padat (total 159 kata, memenuhi batas target 125–175 kata di `paper_outline.md`), disajikan dalam format bilingual (Bahasa Inggris akademis disertai terjemahan Bahasa Indonesia).
- **Changes Made:**
  - Pada `paper/01_introduction.md` (Paragraf 6), kontribusi dipadatkan menjadi 3 butir terpadu:
    1. *Formulasi integrasi representasi laten multi-domain* berbasis ViT backbone yang dibekukan (`Face ⊕ Emotion ⊕ Age`).
    2. *Evaluasi komparatif komprehensif tanpa kebocoran data* pada spektrum 4 famili pengklasifikasi classical machine learning (linear, probabilistik, ensemble, kernel-based).
    3. *Audit keadilan interseksional granular dan analisis pola kesalahan* pada dataset DemogPairs yang melampaui investigasi pendahuluan.
  - Lokasi Naskah: `paper/01_introduction.md`.

---

#### `ISSUE-EIC-04` (EIC — Minor Comment 3: Diskusi Hasil Perlu Diperdalam dengan Interpretasi Mekanistik)
- **Reviewer Comment:**  
  > *"Diskusi Hasil Perlu Diperdalam dengan Interpretasi Mekanistik: Pembahasan Bagian IV jangan hanya mengulang pelaporan angka akurasi secara deskriptif, melainkan harus memperkaya penalaran mengapa batas keputusan kernel polinomial SVM mampu memisahkan fitur laten lebih baik dibandingkan algoritma linier dan ensemble."*
- **Status:** `RESOLVED`
- **Author Response:**  
  Kami sepakat sepenuhnya. Kami telah memperdalam narasi pembahasan pada Bagian IV-A (Paragraf 5) dan Bagian IV-B (Paragraf 2) dengan menguraikan interaksi mekanistik antarfitur. Kami menjelaskan bahwa kernel polinomial derajat dua ($K(\mathbf{x}_i,\mathbf{x}_j) = (\gamma \langle \mathbf{x}_i,\mathbf{x}_j \rangle)^2$) memetakan ruang fitur ke dalam interaksi perkalian silang nonlinier seluruh pasangan dimensi secara simultan, sehingga efektif mengekstraksi korelasi antara ciri morfologi biometrik wajah dan deformasi ekspresi afektif.
- **Changes Made:**
  - Pada `paper/04_results-and-discussion_a-global-performance.md` (Paragraf 5) dan `paper/04_results-and-discussion_b-feature-ablation-study.md` (Paragraf 2), elaborasi teoretis batas keputusan nonlinier ditambahkan secara substantif.
  - Lokasi Naskah: `paper/04_results-and-discussion_a-global-performance.md`, `paper/04_results-and-discussion_b-feature-ablation-study.md`.

---

### B. Methodology Reviewer Issues

#### `ISSUE-METH-01` (R1 — Critical Comment 1: Ambiguitas Partisi Data Tingkat Subjek)
- **Reviewer Comment:**  
  > *"Ambiguitas Partisi Data Tingkat Subjek: Naskah tidak menegaskan apakah pembagian data 80/20 dilakukan pada tingkat citra atau tingkat identitas subjek (subject-disjoint). Jika citra dari subjek/orang yang sama muncul di set latih dan set uji, terjadi risiko identity leakage yang menggelembungkan estimasi akurasi."*
- **Status:** `DELIBERATE_LIMITATION`
- **Author Response:**  
  Kami sangat menghargai ketelitian metodologis Reviewer 1. Berdasarkan verifikasi kode eksperimen (`experiment/code/`), pembagian data 80/20 dilakukan menggunakan protokol *class-stratified split* acak berbasis sampel kelas dengan seed terkunci (`random_state=42`, `stratify=y`), yang menghasilkan 8.640 citra latih (1.440 sampel/kelas) dan 2.160 citra uji *held-out* (360 sampel/kelas).  
  Secara jujur dan transparan, kami tidak melakukan partisi *subject-disjoint* karena metadata identitas individu per subjek pada dataset DemogPairs dirancang untuk tugas verifikasi pasangan (58.3 juta pasangan) dan memiliki variasi jumlah citra per identitas yang sangat timpang jika dipartisi secara 6-kelas seimbang.  
  Sesuai arahan penelaah, kami mengakui hal ini secara transparan sebagai batasan metodologis yang disengaja (*deliberate limitation* dalam kerangka benchmark representasi laten statis) dan memformulasikan evaluasi *cross-identity generalization* secara eksplisit sebagai arah riset masa depan (*Future Work*).
- **Changes Made:**
  - Pada `paper/03_materials-and-methods_a-dataset.md` (Paragraf 2): Protokol pembagian ditegaskan secara eksplisit sebagai *80/20 stratified split* dengan `random_state=42` dan `stratify=y`, yang mengisolasi penuh 2.160 citra uji *held-out* dari pencarian hyperparameter maupun proses fitting PCA/Scaler.
  - Pada `paper/05_conclusion.md` (Paragraf 2): Ditambahkan pernyataan eksplisit keterbatasan partisi dan perumusan *Future Work*:
    > *"Selain itu, evaluasi ini menerapkan skema partisi stratified split acak berbasis sampel kelas; oleh karena itu, pengujian cross-identity generalization melalui protokol partisi strictly subject-disjoint di mana subjek yang sama tidak muncul pada set latih dan uji secara simultan menjadi prioritas utama riset mendatang guna memverifikasi kekokohan representasi fitur terhadap variabilitas identitas individu baru."*
  - Lokasi Naskah: `paper/03_materials-and-methods_a-dataset.md` dan `paper/05_conclusion.md`.

---

#### `ISSUE-METH-02` (R1 — Major Comment 1: Ketiadaan Uji Signifikansi Statistik pada Selisih 0.41%)
- **Reviewer Comment:**  
  > *"Ketiadaan Uji Signifikansi Statistik pada Selisih 0.41%: Selisih peningkatan akurasi dari Dual-Domain (93.29%) ke Tri-Domain (93.70%) pada SVM hanya sebesar 0.41% (+9 sampel dari 2,160 citra uji). Tanpa pengujian signifikansi inferensial formal (seperti Uji McNemar berpasangan) dan pelaporan Confidence Interval, klaim superioritas Tri-Domain tidak memiliki justifikasi statistik yang kuat."*
- **Status:** `RESOLVED`
- **Author Response:**  
  Kritik ini sangat berharga dan tepat sasaran. Kami telah menjalankan analisis signifikansi statistik inferensial lengkap pada data uji *held-out* independen ($N = 2.160$), yang didokumentasikan pada notebook `experiment/code/3.1_statistical_significance.ipynb`:
  1. *Uji McNemar Berpasangan (Tri-Domain vs Dual-Domain)*:
     - **SVM**: Menghasilkan kontingensi diskordan $b = 35$ (Tri benar, Dual salah) dan $c = 26$ (Tri salah, Dual benar), dengan net gain $+9$ citra (+0.41%). Uji McNemar dengan koreksi kontinuitas Edwards menghasilkan $\chi^2 = 1.0492$ dan exact two-sided binomial $p\text{-value} = 0.3057$. Karena $p > 0.05$, selisih ini **tidak berbeda signifikan secara statistik**.
     - **Random Forest**: Menghasilkan diskordan $b = 50$ dan $c = 64$, net gain $-14$ citra (-0.65%), $\chi^2 = 1.4825$, $p\text{-value} = 0.2232$ ($p > 0.05$).
  2. *Estimasi Wilson Score 95% Confidence Interval*:
     - SVM Tri-Domain: Akurasi 93.70%, 95% CI $[92.60\%, 94.65\%]$.
     - SVM Dual-Domain: Akurasi 93.29%, 95% CI $[92.15\%, 94.27\%]$.
     - Interval kedua model saling bertumpukan (*overlapping*), mengonfirmasi terjadinya kejenuhan representasi fitur laten (*asymptotic feature saturation*).
- **Changes Made:**
  - Pada `paper/04_results-and-discussion_a-global-performance.md`:
    - Tabel VII, VIII, IX, dan X diperbarui dengan menambahkan kolom resmi **95% CI** (Wilson Score 95% Confidence Interval) untuk seluruh 28 konfigurasi model.
    - Paragraf 5 diperbarui untuk melaporkan secara transparan nilai $\chi^2$, $p\text{-value}$ uji McNemar, dan interpretasi *asymptotic feature saturation*.
  - Lokasi Naskah: `paper/04_results-and-discussion_a-global-performance.md`.

---

#### `ISSUE-METH-03` (R1 — Major Comment 2: Ketiadaan Pelaporan Skor CV Fold Mean ± Std)
- **Reviewer Comment:**  
  > *"Ketiadaan Pelaporan Skor Cross-Validation Fold (Mean ± Std): Tabel VII–X hanya menyajikan metrik pada subset uji held-out tanpa mencantumkan kestabilan skor validasi silang 5-fold selama proses GridSearchCV, sehingga pembaca tidak dapat menilai variabilitas model terhadap variasi partisi lipatan data latih."*
- **Status:** `RESOLVED`
- **Author Response:**  
  Kami sepakat sepenuhnya. Kami telah mengekstrak skor validasi silang 5-fold (`cv_results_`) dari seluruh 28 eksperimen GridSearchCV dan mencantumkan nilai rata-rata beserta deviasi standarnya (*CV Score: Mean ± Std*) secara lengkap pada Tabel VII, VIII, IX, dan X.
- **Changes Made:**
  - Tabel VII (RF): Menambahkan kolom `CV Score` (misal: Tri-Domain $87.48\% \pm 0.86\%$, Dual-Domain $87.72\% \pm 0.69\%$).
  - Tabel VIII (GNB): Menambahkan kolom `CV Score` (misal: Tri-Domain $85.53\% \pm 0.57\%$).
  - Tabel IX (LR): Menambahkan kolom `CV Score` (misal: Tri-Domain $92.19\% \pm 0.45\%$).
  - Tabel X (SVM): Menambahkan kolom `CV Score` (misal: Tri-Domain $92.65\% \pm 0.93\%$, Dual-Domain $92.31\% \pm 0.80\%$, Face tunggal $91.41\% \pm 0.85\%$).
  - Lokasi Naskah: `paper/04_results-and-discussion_a-global-performance.md`.

---

#### `ISSUE-METH-04` (R1 — Minor Comment 1: Distorsi Metrik Akurasi OvR pada Klasifikasi 6-Kelas)
- **Reviewer Comment:**  
  > *"Distorsi Metrik Akurasi OvR pada Klasifikasi 6-Kelas Seimbang: Pelaporan OvR Accuracy pada Tabel XI (yang berkisar antara 97.31% hingga 98.70%) berpotensi memberikan ilusi performa yang terlalu optimistik karena dominansi rasio sampel negatif 5:1. Diperlukan metrik pelengkap seperti False Negative Rate (FNR) atau False Positive Rate (FPR) per subkelompok."*
- **Status:** `RESOLVED`
- **Author Response:**  
  Kami sangat menghargai ketajaman analisis Reviewer 1. Dalam evaluasi biner One-vs-Rest pada 6 kelas seimbang, sampel negatif mencakup 5/6 (83.33%) dari total kohort uji, sehingga akurasi OvR secara alamiah terdorong tinggi oleh tingginya jumlah True Negative ($TN$). Untuk memberikan gambaran kesalahan yang jujur dan berimbang, kami telah menambahkan kolom **Recall (TPR)** dan **FNR (%)** (*False Negative Rate*) pada Tabel XI serta membahas rasio dominansi negatif tersebut dalam narasi naskah.
- **Changes Made:**
  - Tabel XI diperbarui dengan kolom formal: `Recall (TPR)`, `Precision`, `F1-Score`, `OvR Accuracy`, dan `FNR (%)`.
  - Pada model SVM Tri-Domain, nilai FNR per subkelompok dilaporkan transparan: White Males (3.06%), White Females (5.28%), Asian Males (5.56%), Black Males (5.83%), Asian Females (7.50%), dan Black Females (10.56%).
  - Paragraf 1 Bagian IV-C secara eksplisit mendiskusikan bahwa tingginya akurasi OvR dipengaruhi oleh rasio dominansi sampel negatif 5:1, sehingga FNR dan Recall dijadikan indikator utama disparitas.
  - Lokasi Naskah: `paper/04_results-and-discussion_c-intersectional-subgroup-performance.md`.

---

#### `ISSUE-METH-05` (R1 — Minor Comment 2: Dokumentasi Random Seed dan Pemilihan Scaler)
- **Reviewer Comment:**  
  > *"Random Seed Tidak Dilaporkan & Pilihan Scaler Terbatas: Untuk replikasi eksperimen identik, nilai random seed pada seluruh split dan model harus dicantumkan, serta alasan pemilihan MinMaxScaler vs StandardScaler perlu didokumentasikan."*
- **Status:** `RESOLVED`
- **Author Response:**  
  Kami telah memastikan seluruh nilai random seed terdokumentasi secara eksplisit. Pada naskah Bagian III-A dan III-G, dicantumkan bahwa pembagian data menggunakan `random_state=42` dan 5-fold StratifiedKFold menggunakan `random_state=42`. Mengenai pilihan scaler, MinMaxScaler dipilih dalam ruang pencarian GridSearchCV (`None` vs `MinMaxScaler`) untuk membatasi rentang fitur laten teranormalisasi ke dalam $[0, 1]$ tanpa mengasumsikan distribusi Gaussian murni pada fitur hasil LayerNorm transformer, yang sangat cocok untuk fungsi kernel polinomial berderajat positif.
- **Changes Made:**
  - Bagian III-A Paragraf 2 menegaskan parameter `random_state=42` dan `stratify=y`.
  - Lokasi Naskah: `paper/03_materials-and-methods_a-dataset.md`.

---

### C. Domain Expert Issues

#### `ISSUE-DOM-01` (R2 — Major Comment 1: Ketiadaan Baseline Arsitektur Standar Eksternal)
- **Reviewer Comment:**  
  > *"Ketiadaan Baseline Arsitektur Standar Eksternal: Tabel XII hanya membandingkan model dengan publikasi konferensi sebelumnya. Diperlukan klarifikasi mengenai posisi tolok ukur literatur orisinal DemogPairs [25] atau model arsitektur tunggal standar."*
- **Status:** `RESOLVED`
- **Author Response:**  
  Kami berterima kasih atas catatan penting ini. Kami telah memeriksa secara mendalam publikasi seminal perancangan dataset DemogPairs oleh Hupont & Fernández (IEEE FG 2019 [[25]]). Kami menemukan bahwa studi seminal tersebut dirancang secara eksklusif sebagai benchmark evaluasi verifikasi identitas wajah (*pairwise verification ROC* yang menguji 58.3 juta pasangan citra pada metrik TAR@FAR) dan **tidak pernah melakukan pelatihan tugas klasifikasi 6-kelas tertutup (*closed-set multiclass classification*)**.  
  Dengan demikian, tidak ada model klasifikasi 6-kelas yang dilaporkan dalam paper orisinal DemogPairs. Hal ini menempatkan penelitian kami bersama studi pendahulu terkait ([[19]], [[20]]) sebagai pelopor yang menyediakan baseline terkontrol internal komprehensif pertama untuk klasifikasi interseksional 6-kelas pada dataset DemogPairs.
- **Changes Made:**
  - Pada `paper/04_results-and-discussion_e-comparison-with-prior-studies.md` (Paragraf 2):
    > *"Penelitian seminal perancangan dataset DemogPairs oleh Hupont dan Fernández [[25]](06_references.md#ref25) dirancang secara eksklusif sebagai benchmark verifikasi identitas (identity verification ROC pada 58.3 juta pasangan citra) dan tidak melakukan pelatihan klasifikasi 6-kelas (closed-set intersectional classification). Oleh karena itu, penelitian ini bersama studi terkait terdahulu [[19]](06_references.md#ref19), [[20]](06_references.md#ref20) memelopori dan menyediakan baseline terkontrol internal pertama yang komprehensif untuk klasifikasi demografis interseksional 6-kelas pada dataset DemogPairs."*
  - Lokasi Naskah: `paper/04_results-and-discussion_e-comparison-with-prior-studies.md`.

---

#### `ISSUE-DOM-02` (R2 — Minor Comment 1: Silsilah Checkpoint HuggingFace)
- **Reviewer Comment:**  
  > *"Opasitas Silsilah Data Checkpoint HuggingFace: Checkpoint pra-latih yang digunakan (`skutaada/VIT-VGGFace` dan `dima806/*`) perlu didokumentasikan arsitektur dasar dan korpus sumber latihannya."*
- **Status:** `RESOLVED`
- **Author Response:**  
  Kami sepakat. Pada naskah Bagian III-B Paragraf 2, kami telah mendokumentasikan spesifikasi ketiga checkpoint backbone:
  1. `ViT-Face` (`skutaada/VIT-VGGFace`): Arsitektur ViT-Base/16 yang dilatih pada korpus VGGFace2 untuk representasi biometrik morfologi wajah.
  2. `ViT-Emotion` (`dima806/facial_emotions_image_detection`): Arsitektur ViT-Base/16 yang dilatih pada dataset ekspresi wajah FER untuk representasi deformasi afektif wajah.
  3. `ViT-Age` (`dima806/facial_age_image_detection`): Arsitektur ViT-Base/16 yang dilatih untuk estimasi rentang usia wajah.  
  Seluruh backbone diekstrak dalam mode *eval* (*frozen weights*) secara offline.
- **Changes Made:**
  - Penjelasan peran representasi ketiga domain dipertegas pada Bagian III-B Paragraf 2 dan dirujuk pada Bagian I Paragraf 5.
  - Lokasi Naskah: `paper/03_materials-and-methods_b-vision-transformer.md`, `paper/01_introduction.md`.

---

#### `ISSUE-DOM-03` (R2 — Minor Comment 2: Visualisasi Feature Embedding t-SNE / UMAP)
- **Reviewer Comment:**  
  > *"Ketiadaan Visualisasi Feature Embedding (t-SNE / UMAP): Naskah akan lebih kaya jika menyertakan proyeksi manifold 2D dari ruang representasi laten untuk memperlihatkan pemadatan klaster dari domain tunggal ke tri-domain."*
- **Status:** `DELIBERATE_LIMITATION`
- **Author Response:**  
  Kami sangat mengapresiasi saran ini. Proyeksi manifold 2D nonlinier (seperti t-SNE atau UMAP) memang sangat informatif secara visual; namun demikian, literatur terkini mengenai proyeksi manifold berdimensi tinggi (misal: Chari & Pachter, *Nature Biotechnology* 2023) memperingatkan bahwa distorsi stokastik pada t-SNE/UMAP sering kali mengaburkan densitas global sebenarnya dan dapat menyesatkan interpretasi pemisahan kelas.  
  Oleh karena itu, kami memilih untuk bertumpu secara ketat pada bukti kuantitatif langsung di ruang dimensi asli ($D = 2.304$), yaitu matriks konfusi multi-kelas pada 2.160 data uji independen (Figure 4) serta tabel kontingensi kesalahan berpasangan (discordant pairs), yang secara matematis merefleksikan dinamika batas keputusan pengklasifikasi tanpa distorsi reduksi manifold 2D. Kami merumuskan eksplorasi interpretasi manifold t-SNE terkontrol sebagai rekomendasi riset masa depan.
- **Changes Made:**
  - Penegasan visualisasi berbasis matriks konfusi komparatif (Figure 4) dan metrik One-vs-Rest pada ruang laten dipertahankan sebagai bukti primer pada Bagian IV-D.
  - Lokasi Naskah: `paper/04_results-and-discussion_d-error-pattern-assessment.md`.

---

#### `ISSUE-DOM-04` (R2 — Minor Comment 3: Landasan Teori Kognitif Pengenalan Wajah Dual-Stream)
- **Reviewer Comment:**  
  > *"Penguatan Landasan Teori Kognitif Visi Wajah: Penggabungan representasi biometrik statis (wajah) dan representasi dinamis (emosi/usia) sebaiknya dikaitkan dengan landasan teori persepsi kognitif wajah dual-stream (Bruce & Young, 1986; Haxby et al., 2000)."*
- **Status:** `RESOLVED`
- **Author Response:**  
  Saran ini sangat konstruktif dan memperkaya kedalaman konseptual penelitian kami. Teori neuro-kognitif persepsi wajah yang digagas oleh Bruce & Young (1986) serta model sistem neural pengenalan wajah Haxby et al. (2000) mempostulatkan adanya pemisahan jalur pemrosesan antara *invariant facial aspects* (struktur identitas dan morfologi biometrik) dan *changeable facial aspects* (ekspresi emosi dinamis dan perubahan penuaan). Integrasi domain `Face`, `Emotion`, dan `Age` dalam naskah kami merealisasikan sinergi komputasional dari kedua jalur kognitif tersebut.
- **Changes Made:**
  - Konseptualisasi integrasi representasi invarian morfologis dan dinamis afektif/penuaan diselaraskan pada Bagian I Paragraf 5 dan Bagian IV-B Paragraf 2.
  - Lokasi Naskah: `paper/01_introduction.md`, `paper/04_results-and-discussion_b-feature-ablation-study.md`.

---

### D. Cross-Perspective Analyst Issues

#### `ISSUE-CROSS-01` (R3 — Major Comment 1: Kesenjangan Klaim Fairness vs Metrik Formal & Drop Recall Black Females)
- **Reviewer Comment:**  
  > *"Kesenjangan Klaim Algorithmic Fairness vs Metrik Formal & Drop Recall Black Females: Abstrak mengklaim 'fair demographic attribute recognition', namun naskah tidak menghitung metrik keadilan formal. Terlebih lagi, Tabel XI memperlihatkan penurunan recall yang signifikan pada Black Females (89.44%) dibandingkan White Males (96.94%), menghasilkan kesenjangan sebesar 7.50%. Hal ini harus dihitung secara formal dan didiskusikan secara kritis."*
- **Status:** `RESOLVED`
- **Author Response:**  
  Kami sangat berterima kasih atas catatan kritis ini yang sangat esensial bagi kredibilitas ilmiah studi tentang keadilan algoritmik (*algorithmic fairness*). Kami telah menindaklanjuti catatan ini secara menyeluruh:
  1. *Perhitungan Metrik Keadilan Formal*: Kami secara formal menghitung metrik *Equal Opportunity Difference* ($\Delta \text{TPR} = \max_c \text{TPR}_c - \min_c \text{TPR}_c$):
     - Pada **SVM Tri-Domain**: $\text{TPR}_{\text{White\_Males}} = 96.94\%$ dan $\text{TPR}_{\text{Black\_Females}} = 89.44\%$, sehingga menghasilkan $\Delta \text{TPR} = 7.50\%$ (kesenjangan 7.50 poin persentase).
     - Pada **LR Tri-Domain**: $\Delta \text{TPR} = 5.00\%$ ($\text{TPR}_{\text{White\_Males}} = 96.11\%$ vs $\text{TPR}_{\text{Black\_Females/Asian\_Females}} = 91.11\%$).
  2. *Diskusi Kritis Disparitas*: Kami secara substantif mendiskusikan bahwa meskipun subkelompok *Black Females* mencatatkan presisi yang sangat tinggi (94.15%), tingkat sensitivitas deteksinya (Recall 89.44% dengan FNR 10.56%) merupakan yang terendah di antara keenam kelas. Hal ini secara transparan membuktikan bahwa fusi fitur multi-domain belum sepenuhnya mengeliminasi bias representasi bawaan (*phenotypic overlap* dan bias representasi historis) pada kelompok interseksional wanita berkulit gelap.
- **Changes Made:**
  - Tabel XI diperbarui dengan mencantumkan kolom `Recall (TPR)` dan `FNR (%)`.
  - Paragraf 1 dan 2 Bagian IV-C memuat analisis mendalam kesenjangan $\Delta \text{TPR} = 7.50\%$ dan merefleksikan keterbatasan fusi fitur terhadap disparitas fenotipik interseksional.
  - Lokasi Naskah: `paper/04_results-and-discussion_c-intersectional-subgroup-performance.md`.

---

#### `ISSUE-CROSS-02` (R3 — Minor Comment 1: Ketiadaan Analisis Biaya Komputasi Inferensi)
- **Reviewer Comment:**  
  > *"Ketiadaan Analisis Biaya Komputasi Inferensi: Penggabungan tiga model ViT-Base meningkatkan kapasitas parameter menjadi ~258M. Diperlukan pelaporan estimasi kompleksitas inferensi dan efisiensi memori."*
- **Status:** `RESOLVED`
- **Author Response:**  
  Kami sepakat. Pendekatan ekstraksi fitur offline (*frozen backbone*) dirancang secara sengaja untuk mengisolasi beban komputasi deep learning ke tahap persiapan data (*preprocessing*). Pada tahap operasional hilir (*inference time*), ekstraksi fitur dijalankan sekali per citra dan klasifikasi dilakukan oleh model classical machine learning (SVM/LR) yang hanya membutuhkan memori kecil (<50 MB) dengan latensi inferensi milidetik (sub-millisecond per sample).
- **Changes Made:**
  - Efisiensi komputasi klasifikasi hilir menggunakan model pembelajaran mesin klasik tanpa komputasi gradien propagasi balik backbone ditegaskan pada Bagian I Paragraf 5 dan Bagian V Paragraf 1.
  - Lokasi Naskah: `paper/01_introduction.md`, `paper/05_conclusion.md`.

---

#### `ISSUE-CROSS-03` (R3 — Minor Comment 2: Refleksi Etika Kategorisasi Rasial & Risiko Dual-Use)
- **Reviewer Comment:**  
  > *"Refleksi Etika Kategorisasi Rasial Otomatis & Risiko Dual-Use: Sistem pengenalan ras otomatis memiliki sensitivitas sosial dan risiko disalahgunakan untuk profil diskriminatif. Diperlukan pernyataan batasan etis yang tegas."*
- **Status:** `RESOLVED`
- **Author Response:**  
  Kami sependapat sepenuhnya. Kategorisasi rasial otomatis membawa risiko esensialisme demografis dan potensi bahaya penyalahgunaan (*dual-use*). Dalam penelitian ini, label demografis diposisikan secara ketat sebagai instrumen teknis evaluasi untuk mendeteksi dan mengukur disparitas akurasi sistem visi komputer (*bias detection and fairness auditing*), bukan melegitimasi klasifikasi ras biologis esensialis.
- **Changes Made:**
  - Ditambahkan `## Ethical Compliance Statement` resmi pada `paper/05_conclusion.md` yang secara eksplisit melarang penggunaan kerangka kerja ini untuk pengawasan massal tanpa persetujuan, penegakan hukum tanpa verifikasi manusia, atau profil diskriminatif.
  - Lokasi Naskah: `paper/05_conclusion.md`.

---

### E. Devil's Advocate Issues

#### `ISSUE-DA-C1` (DA — Critical Comment 1: Paradoks Keunggulan Tri-Domain & Regresi Random Forest -0.65%)
- **Reviewer Comment:**  
  > *"Paradoks Keunggulan Tri-Domain & Regresi Random Forest: Klaim bahwa Tri-Domain merupakan konfigurasi terbaik bertentangan dengan data empiris Tabel VII di mana Random Forest justru mengalami degradasi performa sebesar -0.65% (dari 86.85% pada Dual-Domain menjadi 86.20% pada Tri-Domain). Penurunan ini harus dijelaskan secara teoretis dan klaim universal harus dikalibrasi secara ketat."*
- **Status:** `RESOLVED`
- **Author Response:**  
  Kritik dari Devil's Advocate ini sangat tajam dan kami sikapi dengan kalibrasi ilmiah yang mendalam:
  1. *Kalibrasi Bahasa Klaim*: Kami telah mengoreksi seluruh narasi klaim di abstrak, introduksi, dan kesimpulan, dengan menegaskan bahwa keunggulan fusi tri-domain bersifat *classifier-dependent* (hanya unggul pada 3 dari 4 classifier: SVM, LR, GNB), sementara Random Forest mencapai puncak performanya pada konfigurasi dual-domain `Emotion ⊕ Face`.
  2. *Penjelasan Teoretis Regresi RF*: Kami menyajikan analisis teoretis bahwa degradasi performa Random Forest pada fitur 2.304 dimensi merupakan manifestasi klasik dari fenomena *curse of dimensionality* pada algoritma pohon keputusan ortogonal sejajar sumbu (*axis-aligned tree splits*). Pada subspace fitur acak $\text{max\_features} = \sqrt{2304} = 48$ fitur per percabangan, probabilitas terpilihnya dimensi fitur usia yang kurang informatif (sebagaimana performa single-domain `Age` yang paling rendah, 73.66%) meningkat secara signifikan, sehingga mencemari kualitas pemisahan partisi pohon acak.
- **Changes Made:**
  - Pada `paper/04_results-and-discussion_a-global-performance.md` (Paragraf 1 dan Paragraf 5): Ditegaskan sifat *classifier-dependent* dan hasil uji McNemar pada RF (selisih -14 citra, $p = 0.2232$).
  - Pada `paper/04_results-and-discussion_b-feature-ablation-study.md` (Paragraf 2): Penjelasan komprehensif mengenai *curse of dimensionality* pada *axis-aligned splits* RF ditambahkan secara mendalam.
  - Lokasi Naskah: `paper/04_results-and-discussion_a-global-performance.md`, `paper/04_results-and-discussion_b-feature-ablation-study.md`, `paper/05_conclusion.md`.

---

#### `ISSUE-DA-M1` (DA — Major Comment 1: Ketiadaan Kontrol Dimensionalitas / Argumen Kapasitas)
- **Reviewer Comment:**  
  > *"Ketiadaan Kontrol Dimensionalitas (Noise Baseline): Peningkatan akurasi SVM sebesar 0.41% pada Tri-Domain (2,304-d) dibandingkan Dual-Domain (1,536-d) dicurigai sebagai artefak dari pertambahan kapasitas parameter pada ruang dimensi yang lebih tinggi, bukan karena kontribusi informasi komplementer domain usia."*
- **Status:** `RESOLVED`
- **Author Response:**  
  Kami berterima kasih atas tantangan kritis ini. Argumen Devil's Advocate berhasil kami bantah melalui perbandingan perilaku lintas pengklasifikasi (*cross-classifier behavioral contrast*):
  - Jika peningkatan akurasi semata-mata merupakan artefak pertambahan kapasitas dimensi ($1.536 \to 2.304$), maka seluruh model semestinya mengalami peningkatan akurasi serupa. Kenyataannya, Random Forest justru mengalami penurunan akurasi sebesar -0.65% pada ruang 2.304-d.
  - Perbedaan kontras ini membuktikan bahwa kenaikan SVM sebesar 0.41% dimungkinkan oleh karakteristik formulasi kernel polinomial derajat dua ($d=2$) yang mengevaluasi seluruh kombinasi produk titik pasangan dimensi secara simultan, bukan sekadar penambahan dimensi linier.
  - Namun demikian, karena selisih SVM tersebut tidak signifikan secara statistik ($p = 0.3057$ pada Uji McNemar), kami menyimpulkan bahwa representasi laten usia berada pada kondisi kejenuhan fitur (*asymptotic feature saturation*).
- **Changes Made:**
  - Pada `paper/04_results-and-discussion_b-feature-ablation-study.md` (Paragraf 2), argumen kontrol dimensionalitas dan komparasi perilaku RF vs SVM diintegrasikan secara rinci.
  - Lokasi Naskah: `paper/04_results-and-discussion_b-feature-ablation-study.md`.

---

#### `ISSUE-DA-M2` (DA — Major Comment 2: Inflasi Semantik Klaim Fusi Konkatenasi Mentah)
- **Reviewer Comment:**  
  > *"Inflasi Semantik Klaim Fusi Konkatenasi Mentah: Naskah menggunakan istilah 'novel framework' dan 'novel feature fusion', padahal operasi yang dilakukan secara teknis hanyalah konkatenasi vektor offline (direct sum ⊕) diikuti pengklasifikasi klasik standar scikit-learn. Terminologi harus disesuaikan secara proporsional."*
- **Status:** `RESOLVED`
- **Author Response:**  
  Kami menerima kritik ini dengan penuh kerendahan hati. Kami telah membersihkan seluruh klaim hiperbolik ("novel framework", "novel feature fusion architecture") dari seluruh naskah. Kami menggantinya dengan deskripsi saintifik yang objektif dan presisi: *"kerangka evaluasi fusi representasi laten multi-domain terpadu"* (*a unified multi-domain latent representation evaluation framework*).
- **Changes Made:**
  - Pada `paper/01_introduction.md` (Paragraf 5): Istilah disesuaikan menjadi *"kerangka evaluasi fusi representasi laten multi-domain terpadu yang memadukan tiga representasi laten spesifik tugas"*.
  - Paragraf 6 (Butir 1 Kontribusi): Menggunakan formulasi *"A multi-domain latent representation integration framework combining frozen pre-trained Vision Transformer backbones"*.
  - Lokasi Naskah: `paper/01_introduction.md`.

---

#### `ISSUE-DA-M3` (DA — Major Comment 3: Ketiadaan Justifikasi Komparatif terhadap Fine-Tuning Single-ViT)
- **Reviewer Comment:**  
  > *"Ketiadaan Justifikasi Komparatif terhadap Fine-Tuning Single-ViT: Naskah tidak menjelaskan mengapa memilih strategi fusi tiga backbone beku + classical ML dibandingkan melakukan fine-tuning end-to-end pada satu model ViT tunggal."*
- **Status:** `RESOLVED`
- **Author Response:**  
  Kami sepakat bahwa rasionalisasi arsitektural ini sangat penting. Pendekatan fusi representasi beku (*frozen pre-trained representations*) dipadukan dengan pengklasifikasi pembelajaran mesin klasik dipilih dengan pertimbangan teknis:
  1. *Pencegahan Catastrophic Forgetting*: Fine-tuning end-to-end pada satu backbone tunggal berisiko mendistorsi manifold representasi spesifik tugas (misal: fitur biometrik wajah terdistorsi saat diadaptasi ke klasifikasi gender).
  2. *Efisiensi Komputasi & Stabilitas*: Mengekstrak representasi laten secara offline memungkinkan penjelajahan ruang hyperparameter secara masif (38.010 fits GridSearchCV) dengan jaminan ketiadaan variabilitas stokastik pelatihan ulang model berparameter besar (~86M parameter per backbone).
  3. *Isolasi Evaluasi Laten*: Memungkinkan perbandingan ablasi murni mengenai kontribusi informasi masing-masing domain tanpa bias optimasi optimizer neural network.
- **Changes Made:**
  - Justifikasi efisiensi komputasi dan isolasi variabilitas ekstraksi offline tanpa fine-tuning dipertegas pada Bagian I Paragraf 5 dan Bagian V Paragraf 2.
  - Lokasi Naskah: `paper/01_introduction.md`, `paper/05_conclusion.md`.

---

#### `ISSUE-DA-m1` (DA — Minor Comment 1: Seleksi Visualisasi Matriks Konfusi yang Bias)
- **Reviewer Comment:**  
  > *"Seleksi Visualisasi Matriks Konfusi yang Bias: Figure 4 hanya memvisualisasikan model SVM yang performanya naik, sementara model Random Forest yang mengalami degradasi performa tidak dianalisis matriks konfusinya secara berimbang."*
- **Status:** `RESOLVED`
- **Author Response:**  
  Kami berterima kasih atas masukan ini. Kami telah menambahkan pembahasan analitis mengenai pola kesalahan pada model non-SVM (khususnya Random Forest) di Bagian IV-D, dengan menjelaskan bahwa pada Random Forest, misklasifikasi pada subkelompok wanita meningkat saat fitur usia ditambahkan akibat peningkatan dispersi partisi pohon acak pada ruang 2.304 dimensi.
- **Changes Made:**
  - Pembahasan dinamika kesalahan diperluas pada Bagian IV-D Paragraf 4.
  - Lokasi Naskah: `paper/04_results-and-discussion_d-error-pattern-assessment.md`.

---

#### `ISSUE-DA-m2` (DA — Minor Comment 2: Definisi Formal Metrik 'Stabilitas' Subkelompok)
- **Reviewer Comment:**  
  > *"Klaim 'Stabilitas' Subkelompok Tanpa Definisi Formal: Penggunaan istilah bahwa performa subkelompok 'stabil' memerlukan definisi metrik dispersi kuantitatif yang jelas (seperti rentang disparitas F1 atau Equal Opportunity Difference) agar tidak menjadi klaim kualitatif longgar."*
- **Status:** `RESOLVED`
- **Author Response:**  
  Kami sependapat sepenuhnya. Kami telah mengikat istilah "stabilitas" subkelompok pada dua definisi kuantitatif formal:
  1. *Disparitas Rentang F1-Score*: Selisih antara subkelompok tertinggi dan terendah ($\Delta \text{F1} = 4.40\%$ pada SVM Tri-Domain: 91.74% s.d. 96.14%; dan $\Delta \text{F1} = 4.22\%$ pada LR Tri-Domain: 91.36% s.d. 95.58%), di mana seluruh 6 kelas berhasil melampaui ambang batas 91.00%.
  2. *Equal Opportunity Difference*: Selisih tingkat True Positive Rate ($\Delta \text{TPR} = 7.50\%$ pada SVM dan $\Delta \text{TPR} = 5.00\%$ pada LR).
- **Changes Made:**
  - Definisi kuantitatif formal dan batasan rentang disparitas dicantumkan secara eksplisit pada Bagian IV-C Paragraf 1 dan Paragraf 2.
  - Lokasi Naskah: `paper/04_results-and-discussion_c-intersectional-subgroup-performance.md`.

---

## III. Matriks Ringkasan Pemenuhan Komitmen Revisi (Schema 11 Summary)

| ID Temuan | Penilai Sumber | Dimensi Evaluasi | Tingkat Keparahan | Lokasi Perubahan Naskah | Status Pemenuhan |
|:---:|:---:|:---:|:---:|---|:---:|
| `ISSUE-METH-01` | Reviewer 1 | `D1` (Metodologi) | **`CRITICAL`** | `paper/03_materials-and-methods_a-dataset.md`, `paper/05_conclusion.md` | `DELIBERATE_LIMITATION` |
| `ISSUE-DA-C1` | Devil's Advocate | `D3` (Rasionalitas) | **`CRITICAL`** | `paper/04_results-and-discussion_a-global-performance.md`, `paper/04_results-and-discussion_b-feature-ablation-study.md` | `RESOLVED` |
| `ISSUE-METH-02` | Reviewer 1 | `D1` (Metodologi) | **`MAJOR`** | `paper/04_results-and-discussion_a-global-performance.md` (Table VII–X & P5) | `RESOLVED` |
| `ISSUE-DA-M1` | Devil's Advocate | `D3` (Rasionalitas) | **`MAJOR`** | `paper/04_results-and-discussion_b-feature-ablation-study.md` (P2) | `RESOLVED` |
| `ISSUE-EIC-01` | Editor-in-Chief | `D6` (Kesesuaian Ruang Lingkup) | **`MAJOR`** | `paper/01_introduction.md` (P6), `paper/04_results-and-discussion_e-comparison-with-prior-studies.md` | `RESOLVED` |
| `ISSUE-DOM-01` | Reviewer 2 | `D2` (Penguasaan Domain) | **`MAJOR`** | `paper/04_results-and-discussion_e-comparison-with-prior-studies.md` (Table XII & P2) | `RESOLVED` |
| `ISSUE-CROSS-01` | Reviewer 3 | `D4` (Analisis Lintas Disiplin) | **`MAJOR`** | `paper/04_results-and-discussion_c-intersectional-subgroup-performance.md` (Table XI & P1–P2) | `RESOLVED` |
| `ISSUE-DA-M2` | Devil's Advocate | `D3` (Rasionalitas) | **`MAJOR`** | `paper/01_introduction.md` (P5, P6) | `RESOLVED` |
| `ISSUE-DA-M3` | Devil's Advocate | `D3` (Rasionalitas) | **`MAJOR`** | `paper/01_introduction.md` (P5), `paper/05_conclusion.md` (P2) | `RESOLVED` |
| `ISSUE-METH-03` | Reviewer 1 | `D1` (Metodologi) | **`MAJOR`** | `paper/04_results-and-discussion_a-global-performance.md` (Table VII, VIII, IX, X) | `RESOLVED` |
| `ISSUE-EIC-02` | Editor-in-Chief | `D6` (Kesesuaian Ruang Lingkup) | **`MINOR`** | `paper/05_conclusion.md` (Subbab Statuta Resmi IEEE Access) | `RESOLVED` |
| `ISSUE-EIC-03` | Editor-in-Chief | `D5` (Struktur & Bahasa) | **`MINOR`** | `paper/01_introduction.md` (P6: 3 Butir Kontribusi Ringkas) | `RESOLVED` |
| `ISSUE-EIC-04` | Editor-in-Chief | `D5` (Struktur & Bahasa) | **`MINOR`** | `paper/04_results-and-discussion_a-global-performance.md` (P5), `paper/04_results-and-discussion_b-feature-ablation-study.md` (P2) | `RESOLVED` |
| `ISSUE-METH-04` | Reviewer 1 | `D1` (Metodologi) | **`MINOR`** | `paper/04_results-and-discussion_c-intersectional-subgroup-performance.md` (Table XI & P1) | `RESOLVED` |
| `ISSUE-METH-05` | Reviewer 1 | `D1` (Metodologi) | **`MINOR`** | `paper/03_materials-and-methods_a-dataset.md` (P2), `paper/03_materials-and-methods_g-classification-pipeline.md` | `RESOLVED` |
| `ISSUE-DOM-02` | Reviewer 2 | `D2` (Penguasaan Domain) | **`MINOR`** | `paper/03_materials-and-methods_b-vision-transformer.md` (P2) | `RESOLVED` |
| `ISSUE-DOM-03` | Reviewer 2 | `D2` (Penguasaan Domain) | **`MINOR`** | `paper/04_results-and-discussion_d-error-pattern-assessment.md` | `DELIBERATE_LIMITATION` |
| `ISSUE-DOM-04` | Reviewer 2 | `D2` (Penguasaan Domain) | **`MINOR`** | `paper/01_introduction.md` (P5), `paper/04_results-and-discussion_b-feature-ablation-study.md` (P2) | `RESOLVED` |
| `ISSUE-CROSS-02` | Reviewer 3 | `D4` (Analisis Lintas Disiplin) | **`MINOR`** | `paper/01_introduction.md` (P5), `paper/05_conclusion.md` (P1) | `RESOLVED` |
| `ISSUE-CROSS-03` | Reviewer 3 | `D4` (Analisis Lintas Disiplin) | **`MINOR`** | `paper/05_conclusion.md` (Subbab Ethical Compliance Statement) | `RESOLVED` |
| `ISSUE-DA-m1` | Devil's Advocate | `D3` (Rasionalitas) | **`MINOR`** | `paper/04_results-and-discussion_d-error-pattern-assessment.md` (P4) | `RESOLVED` |
| `ISSUE-DA-m2` | Devil's Advocate | `D3` (Rasionalitas) | **`MINOR`** | `paper/04_results-and-discussion_c-intersectional-subgroup-performance.md` (P1, P2) | `RESOLVED` |

---

## IV. Kesimpulan dan Pernyataan Penutup

Seluruh catatan, keberatan metodologis, dan saran penyempurnaan dari Dewan Editor dan Dewan Reviewer independen telah kami laksanakan secara tuntas, jujur, dan berlandaskan bukti inferensial yang kokoh. Naskah revisi yang dihasilkan kini memiliki ketegasan metodologis yang lebih tinggi, klaim saintifik yang terkalibrasi secara ketat, pengujian inferensial statistik yang komprehensif, kepatuhan etika Responsible AI, serta memenuhi seluruh standar format naskah jurnal bereputasi tinggi (*IEEE Access*).

Kami menyatakan kesiapan penuh untuk memberikan penjelasan tambahan atau melakukan penyesuaian lanjutan apabila Dewan Editor dan Reviewer memandang masih terdapat aspek yang memerlukan penyempurnaan.

Hormat kami,  
Atas nama seluruh penulis,

**Dr. Ir. Ricky Eka Putra, S.Kom., M.Kom.**  
*Corresponding Author*  
Jurusan Teknik Informatika, Fakultas Teknik  
Universitas Negeri Surabaya, Surabaya, Indonesia  
Pos-el: `rickyeka@unesa.ac.id`
