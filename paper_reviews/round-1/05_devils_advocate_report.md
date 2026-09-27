### Peer Review Report — Devil's Advocate (Adversarial Evaluator)

- **Reviewer Role**: Devil's Advocate (Adversarial Evaluator)
- **Dimensi Tanggung Jawab**: `D3` (argumentative_coherence)
- **Target Venue**: **IEEE Access**
- **Rekomendasi**: **Major Revision** *(Konsolidasi Penilaian Panel Multi-Model)*
- **Confidence Score**: 5 / 5 (Sangat Tinggi — Register Skeptis dan Adversarial Murni)

---

## 1. Rencana Skoring Pra-Komitmen (Fase 1: Paper-Blind Phase)

Sebelum membaca teks naskah, Devil's Advocate menyusun postulat penantang (*adversarial challenge strategy*) untuk menguji tesis inti naskah:
- `what_to_look_for`:
  - Bukti bahwa klaim superioritas fitur tri-domain bukan sekadar fluktuasi acak atau ilusi peningkatan marjinal (*marginal gain illusion*).
  - Konsistensi klaim lintas pengklasifikasi: apakah fusi tiga domain benar-benar unggul secara seragam di semua classifier, atau justru gagal pada beberapa model?
  - Pembuktian bahwa peningkatan performa berasal dari *informasi domain komplementer*, bukan sekadar *efek penambahan dimensionalitas fitur* (kapasitas parameter).
  - Pembuktian bahwa "fusi" yang diusulkan benar-benar merupakan terobosan arsitektur baru, bukan sekadar penumpukan vektor fitur beku (*naive feature dumping/concatenation*).
  - Pertanyaan *"So What?"*: apakah arsitektur rumit dengan 3 backbone ViT (258M parameter) memberikan keuntungan praktis nyata dibandingkan model tunggal yang di-fine-tune?
- `what_triggers_block`:
  - Klaim "terobosan superioritas" yang bertumpu pada selisih akurasi <1% yang terbukti tidak konsisten (misal: performa justru anjlok pada algoritma lain).
  - Tesis inti runtuh ketika diperiksa dari sudut pandang efisiensi atau ketiadaan eksperimen kontrol dimensionalitas.
- `what_triggers_warn`:
  - Penyamaran teknik dasar (seperti konkatenasi vektor offline scikit-learn) sebagai inovasi arsitektur deep learning mutakhir.
  - Seleksi visualisasi yang bias (hanya menampilkan visualisasi pada model yang berhasil dan menyembunyikan model yang gagal).
- `what_triggers_fatal`:
  - Fabrikasi klaim empiris yang dibantah secara langsung oleh tabel data naskah itu sendiri.

`[CONTRACT-ACKNOWLEDGED]`

---

## 2. Argumen Penyangkal Terkuat (Strongest Counter-Argument)

> **Tesis Utama Penulis**: *"Kerangka kerja fusi Tri-Domain ViT (Face ⊕ Emotion ⊕ Age) menghasilkan representasi terpadu yang superior dan komplementer untuk klasifikasi ras dan gender interseksional."*
>
> **Sanggahan Adversarial Inti**:
> Klaim keunggulan fusi tri-domain ini adalah sebuah **ilusi empiris yang sangat rapuh**. Pada data uji independen ($N=2,160$), penambahan domain ketiga (Age) ke dalam model Dual-Domain (Emotion ⊕ Face) pada SVM hanya menghasilkan kenaikan akurasi sebesar **0.41%—yang secara matematis setara dengan tepat 9 sampel citra dari 2,160 citra uji**! 
> 
> Lebih fatal lagi bagi koherensi argumen naskah: **pada algoritma Random Forest, fusi Tri-Domain justru menyebabkan penurunan performa (regresi) sebesar -0.65%** (Akurasi anjlok dari 86.85% pada Dual-Domain menjadi 86.20% pada Tri-Domain, atau 14 citra uji bertambah salah!). Pada Gaussian Naive Bayes, penambahan domain usia hanya membalikkan **4 citra** (+0.19%), dan pada Logistic Regression hanya membalikkan **7 citra** (+0.32%). 
> 
> Menambah satu model transformer utuh (~86 juta parameter) dan memperbesar dimensi fitur sebesar 50% (dari 1,536 menjadi 2,304) demi membalikkan 4 hingga 9 sampel—sembari merusak performa pohon keputusan—membuktikan bahwa domain usia bukanlah informasi komplementer ortogonal yang kokoh. Terlebih lagi, **penulis tidak menyajikan eksperimen kontrol dimensionalitas**: apakah kenaikan 9 sampel pada SVM tersebut benar-benar membawa informasi biologis penuaan, ataukah sekadar efek penambahan 768 dimensi angka acak (*Gaussian noise baseline*) pada ruang berdimensi tinggi?

---

## 3. Poin Kekuatan yang Diakui Secara Terbatas (Reluctant Strengths)

- **S1: Kejujuran dalam Menampilkan Regresi Random Forest (`D3`)**:
  - Penulis tidak menyembunyikan atau melakukan *cherry-picking* pada hasil eksperimen di mana model Tri-Domain kalah dari Dual-Domain pada Random Forest (Tabel VII), serta mengakui bahwa manfaat fusi multi-domain bersifat *classifier-dependent*.
  - Evidence Anchor: `[table: VII]`, `[section: 05_conclusion]`
- **S2: Transparansi Pengakuan Ketiadaan Uji Signifikansi (`D3`)**:
  - Penulis secara eksplisit menuliskan kalimat penafian bahwa perbandingan performa bersifat deskriptif tanpa pengujian hipotesis formal, meskipun pengakuan ini justru memvalidasi kritik utama kami.
  - Evidence Anchor: `[section: 04_results-and-discussion_a-global-performance]`

---

## 4. Kelemahan Argumen & Tantangan Adversarial (Weaknesses)

### C1: Paradoks Keunggulan Tri-Domain: Selisih 9 Sampel (+0.41%) dan Degradasi Random Forest
- **ID Isu**: `ISSUE-DA-C1`
- [dimension: D3]
- Severity: CRITICAL
- **Verbatim Trigger**: `"what_triggers_block: klaim terobosan superioritas yang bertumpu pada selisih akurasi <1% yang terbukti tidak konsisten"`
- **Evidence Anchor**: `[table: 7]`, `[table: 8]`, `[table: 9]`, `[table: 10]`, `[section: 04_results-and-discussion_b-feature-ablation-study]`
- **Deskripsi Temuan**:
  Mari kita bedah secara telanjang angka-angka pada data uji held-out ($N=2,160$) saat beralih dari skema **Dual-Domain (Emotion ⊕ Face)** ke **Tri-Domain (Face ⊕ Emotion ⊕ Age)**:
  
  | Classifier | Dual-Domain Accuracy | Tri-Domain Accuracy | Selisih Akurasi | Selisih Sampel Benar (dari 2,160) |
  |---|:---:|:---:|:---:|:---:|
  | **SVM** | 93.29% (2,015 benar) | 93.70% (2,024 benar) | **+0.41%** | **+9 citra** |
  | **LR** | 92.41% (1,996 benar) | 92.73% (2,003 benar) | **+0.32%** | **+7 citra** |
  | **GNB** | 84.86% (1,833 benar) | 85.05% (1,837 benar) | **+0.19%** | **+4 citra** |
  | **RF** | **86.85%** (1,876 benar) | 86.20% (1,862 benar) | **-0.65%** | **-14 citra (REGRESI)** |
  
  Dari empat model yang diuji:
  - Pada 3 model linier/kernel/probabilistik (SVM, LR, GNB), perbaikan yang diberikan oleh penambahan domain usia (*Age*) berada pada rentang yang sangat tidak meyakinkan: hanya **antara 4 hingga 9 citra uji**!
  - Pada model ensemble non-parametrik (Random Forest), penambahan domain usia justru **merusak akurasi, menyebabkan 14 sampel citra yang semula diprediksi benar menjadi salah**.
  
  Penulis membangun narasi kontribusi utama naskah (Kontribusi 1 dan 3 pada Pendahuluan) di atas klaim bahwa kerangka kerja Tri-Domain adalah konfigurasi optimal. Namun, bukti empiris memperlihatkan bahwa domain usia memberikan kontribusi yang sangat marginal pada model linier dan menjadi *noise* yang mengacaukan pemisahan partisi pohon pada Random Forest. Mengklaim fusi Tri-Domain sebagai arsitektur unggulan tanpa mengkalibrasi bahasa klaim secara realistis adalah kelemahan argumentasi yang fatal.
- **Rekomendasi Aksi**:
  1. Penulis wajib menurunkan derajat klaim (*temper the claims*): ubah penekanan dari "Tri-Domain superiority" menjadi analisis objektif tentang "pertukaran batas keputusan (*decision boundary trade-offs*) dan batas kejenuhan representasi (*feature saturation limit*)".
  2. Bahas secara eksplisit dalam bab *Discussion* mengapa penambahan 768 dimensi fitur usia hanya menghasilkan peningkatan marjinal 9 sampel pada SVM dan mengapa pohon keputusan RF mengalami *curse of dimensionality* pada ruang 2,304 dimensi.

### M1: Ketiadaan Eksperimen Kontrol Dimensionalitas (Noise Baseline Control)
- **ID Isu**: `ISSUE-DA-M1`
- [dimension: D3]
- Severity: MAJOR
- **Verbatim Trigger**: `"what_triggers_block: tidak ada eksperimen kontrol yang membuktikan peningkatan berasal dari informasi domain komplementer"`
- **Evidence Anchor**: `[section: 04_results-and-discussion_b-feature-ablation-study]`
- **Deskripsi Temuan**:
  Penulis mengklaim bahwa informasi usia "melengkapi profil morfologi wajah." Namun, tidak ada eksperimen kontrol yang membuktikan bahwa peningkatan akurasi 0.41% benar-benar berasal dari informasi biologis penuaan dan bukan semata-mata konsekuensi dari pembesaran dimensi ruang fitur (768→1,536→2,304 dimensi) yang mempermudah pemisahan linear/polinomial pada SVM.
  
  Eksperimen kontrol minimal yang diperlukan untuk membungkam skeptisisme ini: menguji performa model saat fitur Face digabungkan dengan 768 dimensi vektor acak (*Gaussian noise*) atau fitur dari model vision generik (ImageNet). Jika penambahan fitur acak berdimensi 768 juga menaikkan akurasi 0.3–0.4% pada SVM berpenalti tinggi (C=10), maka klaim bahwa domain usia membawa informasi komplementer ortogonal akan terbantahkan.
- **Rekomendasi Aksi**:
  Jalankan eksperimen kontrol baseline (konkatenasi fitur Face + 768-d Gaussian noise acak pada SVM) atau sertakan justifikasi teoretis mendalam mengenai mengapa peningkatan tersebut bukan artefak pembesaran dimensi semata.

### M2: Inflasi Semantik: Mengklaim Konkatenasi Vektor Sederhana sebagai "Kerangka Kerja Fusi Baru"
- **ID Isu**: `ISSUE-DA-M2`
- [dimension: D3]
- Severity: MAJOR
- **Verbatim Trigger**: `"what_triggers_warn: penyamaran teknik dasar sebagai inovasi arsitektur deep learning mutakhir"`
- **Evidence Anchor**: `[section: 01_introduction]`, `[section: 03_materials-and-methods_0-overview]`, `[section: 03_materials-and-methods_b-vision-transformer]`
- **Deskripsi Temuan**:
  Pada Kontribusi 1 ([Section I](01_introduction.md)), penulis mengklaim:
  > *"A Tri-Domain ViT feature fusion framework integrating face-associated biometric representations, expression-related representations, and age-associated facial representations into a unified latent feature vector..."*
  
  Ketika kita memeriksa Persamaan (5) pada Bagian III-B:
  $$\mathbf{z}_{\text{tri}} = \mathbf{f}_{\text{face}} \oplus \mathbf{f}_{\text{emotion}} \oplus \mathbf{f}_{\text{age}}$$
  
  Tidak ada arsitektur fusi terpelajar (*learned cross-attention*), tidak ada mekanisme gating dinamis, tidak ada modul penimbang bobot atensi lintas domain, dan tidak ada lapisan proyeksi terlatih. Prosedur komputasi yang dilakukan hanyalah menjalankan fungsi `concatenate` dasar pada tiga larik angka yang diekstraksi dari checkpoint HuggingFace publik, lalu mengumpankannya ke fungsi `GridSearchCV` standar dari pustaka `scikit-learn`.
  
  Menyebut operasi konkatenasi mentah (*raw feature concatenation*) ini sebagai sebuah *"framework"* baru di jurnal IEEE Access rentan dicap sebagai inflasi terminologi (*semantic overclaiming*). Pembaca IEEE Access mengharapkan inovasi komputasi substansial yang nyata.
- **Rekomendasi Aksi**:
  Perbaiki terminologi naskah: ganti klaim "novel architectural framework" dengan deskripsi yang jujur dan presisi seperti *"an empirical comparative pipeline investigating multi-domain frozen latent feature concatenation"*.

### M3: Uji "So What?": Ketiadaan Komparasi terhadap Single-ViT End-to-End Fine-Tuning
- **ID Isu**: `ISSUE-DA-M3`
- [dimension: D3]
- Severity: MAJOR
- **Evidence Anchor**: `[section: 03_materials-and-methods_0-overview]`, `[section: 05_conclusion]`
- **Deskripsi Temuan**:
  Mengapa seorang praktisi atau peneliti visi komputer harus repot-repot memuat tiga model Vision Transformer (~258 juta parameter) ke dalam memori komputer hanya untuk mengekstraksi 2,304 fitur, jika sebuah model ViT-Base tunggal (86 juta parameter) yang di-fine-tune secara end-to-end pada 8,640 data latih DemogPairs berpotensi mencapai akurasi $\ge 94\%$ dengan sepertiga jejak komputasi?
  
  Penulis mempertahankan strategi *frozen backbone* dengan alasan "efisiensi komputasi pelatihan" ([03_materials-and-methods_b-vision-transformer.md](03_materials-and-methods_b-vision-transformer.md#L38)). Namun efisiensi pelatihan offline ini dibayar mahal oleh ketidakefisienan inferensi (tiga forward pass transformer). Tanpa menyajikan baseline satu model ViT yang di-fine-tune langsung pada target kelas ras-gender, justifikasi logis penggunaan fusi tiga domain beku ini menjadi sangat lemah di hadapan penguji skeptis.
- **Rekomendasi Aksi**:
  Sertakan pembahasan justifikasi teknis pada Bagian III atau Bagian V mengenai mengapa pendekatan *frozen feature extraction + classical ML* dipilih dibandingkan *end-to-end fine-tuning* (misalnya: isolasi representasi tanpa risiko catastrophic forgetting, ketiadaan kebutuhan komputasi GPU berulang saat eksplorasi hyperparameter, atau efisiensi bagi lingkungan komputasi terbatas).

### m1: Seleksi Visualisasi Matriks Konfusi yang Bias
- **ID Isu**: `ISSUE-DA-m1`
- [dimension: D3]
- Severity: MINOR
- **Verbatim Trigger**: `"what_triggers_warn: seleksi visualisasi yang bias"`
- **Evidence Anchor**: `[figure: 4]`, `[section: 04_results-and-discussion_d-error-pattern-assessment]`
- **Deskripsi Temuan**:
  Gambar 4 hanya menampilkan diagram matriks konfusi untuk model SVM pada tiga konfigurasi (Face, Emotion ⊕ Face, dan Tri-Domain), yang memperlihatkan narasi "penurunan galat progresif yang mulus". Dari 28 konfigurasi yang diuji, penulis tidak memperlihatkan matriks konfusi pada model Random Forest di mana fusi tri-domain justru mengalami peningkatan galat (regresi). Penyajian yang hanya menonjolkan model sukses menimbulkan kesan pemilihan visualisasi yang selektif.
- **Rekomendasi Aksi**:
  Bahas secara singkat pola galat pada model non-SVM (misal: Random Forest) di narasi Bagian IV-D untuk menjaga transparansi ilmiah yang berimbang.

### m2: Klaim "Stabilitas" Subkelompok Tanpa Definisi Formal Metrik Stabilitas
- **ID Isu**: `ISSUE-DA-m2`
- [dimension: D3]
- Severity: MINOR
- **Evidence Anchor**: `[section: 04_results-and-discussion_c-intersectional-subgroup-performance]`
- **Deskripsi Temuan**:
  Penulis menyatakan bahwa F1-Score "terdistribusi stabil pada rentang 91.74% hingga 96.14%," namun tidak mendefinisikan metrik stabilitas formal (misalnya coefficient of variation, min/max ratio, atau fairness gap threshold). Rentang 4.40 pp bisa dianggap "stabil" atau "disparitas signifikan" tergantung konteks.
- **Rekomendasi Aksi**:
  Berikan kriteria atau acuan literatur yang mendasari klaim bahwa rentang disparitas 4.40 pp tergolong stabil.

---

## 5. Ringkasan Status Dimensi Devil's Advocate

| Dimensi | Status | Justifikasi Evaluasi |
|:---:|:---:|---|
| **D3** (*argumentative_coherence*) | **`BLOCK`** | Terdapat 1 isu `CRITICAL` (paradoks selisih 9 citra / +0.41% akurasi yang diiringi regresi performa pada RF), 3 isu `MAJOR` (ketiadaan kontrol dimensionalitas, inflasi semantik klaim fusi konkatenasi, dan ketiadaan komparasi terhadap single-ViT fine-tuning), serta 2 isu `MINOR`. |
