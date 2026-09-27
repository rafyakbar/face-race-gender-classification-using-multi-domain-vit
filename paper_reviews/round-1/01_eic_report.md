### Peer Review Report — Editor-in-Chief (EIC)

- **Reviewer Role**: Editor-in-Chief (EIC)
- **Dimensi Tanggung Jawab**: `D5` (writing_and_structure) & `D6` (venue_fit_and_contribution)
- **Target Venue**: **IEEE Access**
- **Rekomendasi**: **Minor Revision** *(Konsolidasi Penilaian Panel Multi-Model)*
- **Confidence Score**: 5 / 5 (Sangat Tinggi — Tata Kelola Editorial & Publikasi IEEE)

---

## 1. Rencana Skoring Pra-Komitmen (Fase 1: Paper-Blind Phase)

Sebelum menelaah draf naskah secara penuh, EIC menetapkan tolok ukur editorial berdasarkan standar spesifik jurnal **IEEE Access**:
- `what_to_look_for`:
  - Keselarasan mendalam dengan cakupan multidisiplin IEEE Access (visi komputer, pembelajaran mesin terapan, biometrik wajah, keadilan algoritmik).
  - Orisinalitas dan kebaruan saintifik yang melampaui karya inkremental marjinal (*clear advance over state-of-the-art*).
  - Kepatuhan struktur naskah IEEE standar (format IMRaD, judul komprehensif, abstrak informatif berangka, biografi penulis dengan foto, dan gaya sitasi numerik IEEE).
  - Ketersediaan deklarasi transparansi wajib IEEE (pernyataan ketersediaan data/kode dan etika penelitian data subjek manusia).
  - Keringkasan dan ketajaman penyusunan poin kontribusi ilmiah di Pendahuluan.
- `what_triggers_block`:
  - Naskah hanya merupakan penambahan fitur sepele (*trivial increment*) dari publikasi konferensi penulis sendiri tanpa pendalaman teoretis atau eksperimental yang substansial.
  - Struktur naskah tidak lengkap, mengabaikan konvensi IEEE, atau tidak menyertakan biografi penulis.
- `what_triggers_warn`:
  - Ketiadaan pernyataan ketersediaan kode dan data (*reproducibility statement*), ketiadaan deklarasi persetujuan etik biometrik wajah, atau pemaparan kontribusi yang terlalu bertele-tele dan redundan.
  - Diskusi hasil eksperimen bersifat deskriptif tanpa interpretasi mekanistik mengenai dinamika pemisahan fitur.
- `what_triggers_fatal`:
  - Pelanggaran etika publikasi berat, fabrikasi data, atau redundansi teks/data masif dari artikel terdahulu (*dual submission/plagiarism*).

`[CONTRACT-ACKNOWLEDGED]`

---

## 2. Ringkasan Penilaian Editorial (Fase 2: Paper-Visible Phase)

Naskah ini mengusulkan kerangka kerja fusi fitur laten tri-domain dari tiga model Vision Transformer (ViT) pra-latih (biometrik wajah, ekspresi afektif, estimasi usia) untuk klasifikasi enam subkelompok demografis interseksional ras-gender pada dataset DemogPairs (10,800 citra). Kerangka kerja dievaluasi secara masif melintasi empat pengklasifikasi pembelajaran mesin klasik (RF, GNB, LR, SVM) dengan GridSearchCV teroptimasi (28 konfigurasi, 38,010 fits), mencatatkan performa puncak pada SVM tri-domain dengan Akurasi 93.70% dan F1-Score 93.69%.

Dari perspektif tata kelola jurnal **IEEE Access**, naskah ini menunjukkan tata tulis ilmiah yang sangat matang, artikulasi perumusan masalah yang terarah, penyajian tabel benchmark yang rapi, dan kelengkapan elemen IMRaD yang sangat baik termasuk penyertaan biografi naratif keempat penulis di Bagian VII. Evaluasi per subkelompok demografis (Tabel XI) juga melampaui praktik pelaporan umum yang hanya melaporkan metrik agregat.

Namun demikian, hasil konsolidasi panel reviewer mengidentifikasi beberapa catatan kritis yang wajib diperbaiki:
1. **Risiko Persepsi Inkrementalisme (*Novelty & Advance Risk*)**: Pada Tabel XII ([Table XII](04_results-and-discussion_e-comparison-with-prior-studies.md#tab12)), pembanding model hanya karya dari kelompok penulis yang sama persis (Putri et al. [19] ICVEE 2025 dan Putri et al. [20] JIEET 2025). Delta peningkatan akurasi dari skema dual-domain (93.29% pada SVM) ke tri-domain (93.70%) relatif marjinal (+0.41%), sehingga editor IEEE Access berpotensi mempertanyakan apakah kontribusi ini cukup substansial (*sufficient advance*) jika tidak disertai pendalaman analisis teoretis atau wawasan ilmiah baru.
2. **Ketiadaan Statuta Wajib IEEE Access**: Naskah belum menyertakan *Data Availability Statement*, *Code Availability Statement*, serta *Ethical Compliance Statement*.
3. **Penyajian Poin Kontribusi dan Kedalaman Diskusi**: Poin kontribusi pada Bagian I disajikan dalam format dwi-bahasa yang sangat panjang dan redundan, sementara diskusi di Bagian IV masih cenderung deskriptif tanpa eksplorasi mekanistik mendalam.

---

## 3. Poin Kekuatan Naskah (Strengths)

- **S1: Kesesuaian Sempurna Ruang Lingkup IEEE Access (`D6`)**:
  - Integrasi tri-domain ViT (biometrik + ekspresi + usia) untuk klasifikasi demografis interseksional memadukan ranah visi komputer, pembelajaran mesin, dan audit disparitas demografis, yang sangat selaras dengan cakupan multidisiplin IEEE Access.
  - Evidence Anchor: `[section: 01_introduction]`, `[section: 02_related-works]`
- **S2: Eksperimen Terstruktur dan Komprehensif (`D6`)**:
  - Evaluasi sistematis 7 konfigurasi fitur × 4 classifier = 28 eksperimen dengan total 38,010 fits memberikan landasan empiris yang kuat dan transparan.
  - Evidence Anchor: `[table: VII]`, `[table: VIII]`, `[table: IX]`, `[table: X]`
- **S3: Kualitas Penyajian dan Struktur IMRaD yang Eksemplar (`D5`)**:
  - Naskah mengalir secara sangat logis dari abstraksi, formulasi matematis Persamaan (1) hingga (17), hingga visualisasi bagan alir (Gambar 1) dan matriks konfusi (Gambar 4).
  - Evidence Anchor: `[section: 03_materials-and-methods_0-overview]`, `[section: 03_materials-and-methods_b-vision-transformer]`
- **S4: Kepatuhan Format Biografi Penulis IEEE (`D5`)**:
  - Bagian VII menyajikan biodata naratif komprehensif, riwayat pendidikan, fokus riset, dan slot foto untuk seluruh 4 penulis, yang merupakan persyaratan wajib dalam proses finalisasi *IEEE Access*.
  - Evidence Anchor: `[section: 07_biographies]`

---

## 4. Kelemahan Naskah & Catatan Perbaikan (Weaknesses)

### W1: Justifikasi Kontribusi Novelty vs. Riwayat Publikasi Penulis Sendiri
- **ID Isu**: `ISSUE-EIC-01`
- [dimension: D6]
- Severity: MAJOR
- **Verbatim Trigger**: `"what_triggers_warn: naskah hanya merupakan penambahan fitur dari publikasi konferensi penulis sendiri tanpa pendalaman teoretis atau eksperimental yang substansial"`
- **Evidence Anchor**: `[table: 12]`, `[section: 04_results-and-discussion_e-comparison-with-prior-studies]`, `[section: 06_references]` (Ref [19], [20])
- **Deskripsi Temuan**:
  Pada Tabel XII ([Table XII](04_results-and-discussion_e-comparison-with-prior-studies.md#tab12)), penulis membandingkan model usulan (Akurasi 93.70%) terhadap MD-ViT (89.07%) dan Dual-ViT (92.41%). Kedua karya pembanding tersebut ditulis oleh kelompok penulis yang sama (Putri, Putra, Yamasari, Akbar dkk., 2025). Pada konferensi terdahulu ([19]), penulis telah mengeksplorasi fusi Dual-ViT (Face + Emotion) dengan SVM yang menghasilkan akurasi 92.41% (pada draf ini tercatat 93.29%). Penambahan domain ketiga (Age) hanya memberikan peningkatan akurasi bersih sebesar 0.41% pada data uji independen. 
  
  Dalam kacamata Associate Editor *IEEE Access*, situasi ini sangat berisiko dinilai sebagai publikasi "salami-slicing" atau peningkatan inkremental sempit (*marginal incremental contribution*) jika penulis tidak mempertegas kebaruan konseptual naskah ini. Penulis wajib mendefinisikan secara eksplisit apa wawasan ilmiah baru (*novel scientific insights*) yang membedakan naskah jurnal ini dari prosiding konferensi sebelumnya—misalnya kajian mendalam mengenai dinamika batas keputusan antarmodel (linear vs non-linear vs kernel), analisis pergeseran pola galat antarras (Gambar 4), serta karakterisasi disparitas subkelompok interseksional.
- **Rekomendasi Aksi**:
  1. Perkaya Bagian I ([Section I](01_introduction.md)) dengan paragraf distingsi eksplisit yang membedakan kontribusi naskah jurnal ini dari draf awal konferensi ICVEE 2025 ([19]).
  2. Tambahkan pembanding terhadap model/metode dari literatur eksternal yang diuji pada dataset demografis acuan untuk membuktikan keunggulan representasi usulan di luar lingkaran sitasi internal.

### W2: Ketiadaan Statuta Wajib IEEE (Data, Code, & Ethics Statements)
- **ID Isu**: `ISSUE-EIC-02`
- [dimension: D6]
- Severity: MINOR
- **Verbatim Trigger**: `"what_triggers_warn: ketiadaan pernyataan ketersediaan kode dan data, ketiadaan deklarasi persetujuan etik biometrik wajah"`
- **Evidence Anchor**: `[section: 05_conclusion]`, `[section: 03_materials-and-methods_a-dataset]`
- **Deskripsi Temuan**:
  Jurnal *IEEE Access* memberlakukan pedoman kepatuhan reproduktibilitas dan integritas etika yang ketat:
  1. *Data and Code Availability Statement*: Tidak ada penjelasan mengenai ketersediaan repositori kode publik (misal: GitHub / Zenodo / IEEE DataPort) atau aksesibilitas bobot model hasil pelatihan pipeline.
  2. *Ethics & Institutional Approval*: Penelitian ini mengklasifikasikan ras dan gender dari citra wajah manusia. Penulis belum mencantumkan pernyataan etika resmi (*Human Subjects / Institutional Review Board / Dataset License Agreement*) terkait legalitas pemrosesan dataset DemogPairs.
- **Rekomendasi Aksi**:
  Tambahkan subbab atau paragraf deklarasi khusus sebelum *References* yang memuat:
  - *Data Availability Statement*: Tautan unduhan resmi dataset DemogPairs dan repositori skrip evaluasi.
  - *Ethics Statement*: Pernyataan kepatuhan penggunaan data sekunder publik yang tidak memerlukan persetujuan etik langsung subjek baru, sesuai Deklarasi Helsinki atau regulasi institusional lokal.

### W3: Poin Kontribusi Ilmiah Redundan dan Terlalu Panjang
- **ID Isu**: `ISSUE-EIC-03`
- [dimension: D5]
- Severity: MINOR
- **Verbatim Trigger**: `"what_triggers_warn: pemaparan kontribusi yang terlalu bertele-tele dan redundan"`
- **Evidence Anchor**: `[section: 01_introduction, baris 13-17]`
- **Deskripsi Temuan**:
  Keempat poin kontribusi ilmiah di Bagian I ditulis dalam format ganda (bahasa Inggris yang diulang dengan terjemahan bahasa Indonesia di dalam tanda kurung), menghasilkan paragraf yang sangat panjang dan memecah fokus pembaca. Selain itu, poin 2 (benchmark komparatif) dan poin 4 (analisis subkelompok) lebih merupakan protokol evaluasi empiris daripada kontribusi inovasi metodologis orisinal.
- **Rekomendasi Aksi**:
  Padatkan poin kontribusi menjadi 3 poin ringkas dan tajam dengan memisahkan kontribusi arsitektur representasi, temuan komparasi batas keputusan, dan wawasan disparitas interseksional.

### W4: Diskusi Hasil Perlu Diperdalam dengan Interpretasi Mekanistik
- **ID Isu**: `ISSUE-EIC-04`
- [dimension: D5]
- Severity: MINOR
- **Verbatim Trigger**: `"what_triggers_warn: diskusi hasil eksperimen bersifat deskriptif tanpa interpretasi mekanistik"`
- **Evidence Anchor**: `[section: 04_results-and-discussion_a-global-performance]`, `[section: 04_results-and-discussion_b-feature-ablation-study]`
- **Deskripsi Temuan**:
  Narasi pembahasan pada Bagian IV cenderung bersifat deskriptif ("meningkat dari X% menjadi Y%") tanpa memberikan penjelasan mekanistik mengapa kombinasi representasi tertentu menghasilkan pola yang teramati. Misalnya, mengapa Random Forest justru mencatatkan akurasi terbaik pada dual-domain (86.85%) dan menurun pada tri-domain (86.20%), sedangkan model kernel seperti SVM mampu memanfaatkan seluruh 2,304 dimensi secara optimal?
- **Rekomendasi Aksi**:
  Perdalam diskusi dengan analisis sifat pemisahan batas keputusan (*decision boundary characteristics*), dampak kerapatan data pada ruang berdimensi tinggi (*curse of dimensionality*), dan interaksi antardimensi fitur laten.

---

## 5. Ringkasan Status Dimensi EIC

| Dimensi | Status | Justifikasi Evaluasi |
|:---:|:---:|---|
| **D5** (*writing_and_structure*) | **`WARN`** | Struktur IMRaD lengkap dan penulisan rapi, namun poin kontribusi terlalu panjang dan diskusi memerlukan pendalaman interpretasi mekanistik (2 isu `MINOR`). |
| **D6** (*venue_fit_and_contribution*) | **`WARN`** | Topik sangat relevan dengan scope IEEE Access, namun naskah memuat 1 isu `MAJOR` (risiko persepsi kontribusi inkremental dari paper konferensi sendiri) dan 1 isu `MINOR` (ketiadaan data/code/ethics statements). |
