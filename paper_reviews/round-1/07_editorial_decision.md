# Surat Keputusan Editorial (Editorial Decision Letter)

**Status Keputusan**: **MAJOR REVISION**  
*(Setara dengan status **Reject and Resubmit (R&R)** pada model keputusan biner IEEE Access)*  
**Target Publikasi**: **IEEE Access**  
**Tanggal Evaluasi**: 2026-09-27  
**Panel Evaluator**: 5 Penilai Independen — Konsolidasi Multi-Model (Gemini 3.8 Flash + Claude Opus)  
**Protokol Evaluasi**: Kontrak Sprint Schema 13.2 (*Sprint Contract Protocol v2*)  

---

## 0. Baris Audit Sintesis Kanonikal (Pinned Audit Line Grammar)
```text
dimension_verdicts: [D1=BLOCK, D2=WARN, D3=BLOCK, D4=WARN, D5=WARN, D6=WARN]
fired_conditions: [F2]
da_critical_adjudications: [ISSUE-DA-C1=VALIDATED]
editorial_decision=major_revision
```

---

## 1. Konteks Khusus Target Jurnal: IEEE Access

Jurnal **IEEE Access** beroperasi di bawah **model keputusan biner (*binary decision model*)**:
- Pada penelaahan formal IEEE Access, opsi keputusan editorial resmi hanya terdiri atas **Accept** (diterima langsung atau dengan perbaikan tipografis minor) dan **Reject** (ditolak, baik penolakan permanen maupun undangan untuk melakukan *Reject and Resubmit* / revisi menyeluruh dan memasukkan kembali sebagai naskah baru).
- IEEE Access **tidak mengenal status "Major Revision"** dalam siklus penelaahan standarnya. Naskah yang memiliki kekurangan metodologis atau eksperimental yang substansial akan diberikan keputusan **Reject with recommendation to resubmit (Reject & Resubmit)**, di mana penulis hanya diberikan satu kali kesempatan untuk mengajukan kembali naskah baru yang dilengkapi dokumen tanggapan poin-demi-poin (*Point-by-Point Response Document*).
- Oleh karena itu, penetapan keputusan **MAJOR REVISION** di bawah Kontrak Sprint Schema 13 pada simulasi ini berfungsi sebagai *sparring partner* kritis untuk memastikan bahwa seluruh cacat berderajat `BLOCK` dan `WARN` diselesaikan secara tuntas **sebelum naskah diserahkan ke portal resmi IEEE Access**, guna menghindarkan naskah dari vonis *Desk Reject* atau *Permanent Reject* seketika.

---

## 2. Ringkasan Rekomendasi Panel Reviewer

| Peran Reviewer | Fokus Ulasan Utama | Rekomendasi Mandiri | Key Dimension |
|---|---|:---:|:---:|
| **Editor-in-Chief (EIC)** | `venue_fit_and_contribution` & `writing_structure` | **Minor Revision** | `D5`, `D6` |
| **Reviewer 1 (Methodology)** | `methodology_rigor` & `statistical_validity` | **Major Revision** | `D1` |
| **Reviewer 2 (Domain Expert)** | `domain_accuracy` & `sota_benchmarks` | **Minor Revision** | `D2` |
| **Reviewer 3 (Cross-Perspective)** | `cross_disciplinary_relevance` & `fairness_ethics` | **Minor Revision** | `D4` |
| **Devil's Advocate (Adversarial)** | `argumentative_coherence` & `thesis_challenge` | **Major Revision** | `D3` |

---

## 3. Evaluasi 6 Dimensi Akseptasi (Schema 13.2)

| Dimensi | Nama Dimensi | Prioritas | Peran Pemilik | Status Evaluasi | Ringkasan Dasar Penilaian |
|:---:|---|:---:|:---:|:---:|---|
| **D1** | `methodology_rigor` | **Mandatory** | Reviewer 1 | **🚫 BLOCK** | Ambiguitas pemisahan tingkat identitas subjek (*subject-disjoint split*), ketiadaan uji signifikansi statistik formal (McNemar, 95% CI) untuk selisih 9 sampel, dan ketiadaan pelaporan nilai CV score mean ± std. |
| **D2** | `domain_accuracy` | **Mandatory** | Reviewer 2 | **⚠️ WARN** | Perbandingan baseline komparatif bersifat sirkular (hanya karya internal penulis terdahulu), ketiadaan baseline model tunggal standar, opasitas checkpoint HuggingFace, dan ketiadaan visualisasi embedding t-SNE/UMAP. |
| **D3** | `argumentative_coherence` | **Mandatory** | Devil's Advocate | **🚫 BLOCK** | Paradoks selisih 9 sampel (+0.41%) yang disertai regresi performa pada Random Forest (-0.65%), ketiadaan baseline kontrol dimensionalitas (noise control), dan inflasi semantik fusi konkatenasi mentah. |
| **D4** | `cross_disciplinary_relevance` | **High** | Reviewer 3 | **⚠️ WARN** | Kesenjangan antara klaim kata kunci *algorithmic fairness* dengan ketiadaan metrik keadilan formal (drop recall 7.50% Black Females), ketiadaan analisis latensi komputasi inferensi, dan perlunya ethical statement biometrik. |
| **D5** | `writing_and_structure` | **Normal** | EIC | **⚠️ WARN** | Struktur IMRaD lengkap dan formulasi matematis presisi, namun poin kontribusi terlalu panjang dan diskusi memerlukan interpretasi mekanistik mendalam. |
| **D6** | `venue_fit_and_contribution` | **Mandatory** | EIC | **⚠️ WARN** | Risiko persepsi penambahan fitur inkremental marjinal dari prosiding ICVEE 2025 serta ketiadaan statuta ketersediaan data/kode resmi IEEE Access. |

> **Evaluasi Kondisi Aturan Deterministik**:
> - Aturan **F2** Terpicu: Terdapat dimensi *Mandatory* yang berstatus `BLOCK` (`D1=BLOCK` dan `D3=BLOCK`) $\rightarrow$ `editorial_decision=major_revision`.

---

## 4. Adjudikasi Temuan Kritis Devil's Advocate (DA Adjudication)

Sesuai Aturan Emas Schema 13, EIC melakukan adjudikasi eksplisit terhadap temuan kritis dari Devil's Advocate:
- **Isu `ISSUE-DA-C1` (Paradoks Keunggulan Tri-Domain: Selisih 9 Sampel dan Regresi Random Forest)**:
  - **Status Adjudikasi**: **`VALIDATED`**
  - **Dasar Pertimbangan Editorial**: EIC memvalidasi temuan ini secara penuh. Bukti pada Tabel VII, VIII, IX, dan X menunjukkan bahwa penambahan domain usia hanya membalikkan antara 4 hingga 9 sampel pada tiga model, namun justru merusak akurasi Random Forest sebesar 14 sampel (-0.65%). Klaim bahwa Tri-Domain merupakan arsitektur unggulan mutlak tidak didukung oleh konsistensi data lintas model. Penulis wajib mengalibrasi narasi klaim dan menyertakan uji signifikansi statistik inferensial.
  - **Konsekuensi**: Status `VALIDATED` memblokir penerbitan status *Accept* sampai penulis merevisi narasi dan memberikan pembuktian inferensial.

---

## 5. Empat Isu Pemblokir Utama (Top Blocking Issues)

| Peringkat | ID Isu | Penilai Sumber | Dimensi | Severity | Deskripsi Cacat Kritis & Lokasi Bukti |
|:---:|:---:|:---:|:---:|:---:|---|
| **#1** | **`ISSUE-METH-01`** | Reviewer 1 | `D1` | **`CRITICAL`** | **Ambiguitas Pembagian Data Tingkat Identitas Subjek**: Tidak ada jaminan eksplisit bahwa pemisahan stratified split 80/20 bebas dari kebocoran identitas orang yang sama antara set latih dan uji (`[section: 03_materials-and-methods_a-dataset]`, `[table: 1]`). |
| **#2** | **`ISSUE-DA-C1`** | Devil's Advocate | `D3` | **`CRITICAL`** | **Paradoks Keunggulan Tri-Domain & Regresi Random Forest**: Penambahan domain usia hanya membalikkan 4–9 citra pada SVM/LR/GNB tetapi menurunkan akurasi sebesar 14 citra pada RF, bertentangan dengan tesis keunggulan mutlak Tri-Domain (`[table: 7]`, `[table: 10]`). |
| **#3** | **`ISSUE-METH-02`** | Reviewer 1 | `D1` | **`MAJOR`** | **Ketiadaan Uji Signifikansi Statistik Inferensial & 95% CI**: Selisih 0.41% (9 sampel uji) antara Tri-Domain dan Dual-Domain tidak didukung oleh uji McNemar atau Interval Kepercayaan 95%, diperparah oleh pengakuan ketiadaan uji hipotesis formal pada teks naskah (`[section: 04_results-and-discussion_a-global-performance]`). |
| **#4** | **`ISSUE-DA-M1`** | Devil's Advocate | `D3` | **`MAJOR`** | **Ketiadaan Eksperimen Kontrol Dimensionalitas**: Belum ada eksperimen kontrol (misal: penambahan 768-d Gaussian noise acak) untuk membuktikan peningkatan akurasi berasal dari domain usia komplementer dan bukan sekadar pembesaran kapasitas ruang dimensi (`[section: 04_results-and-discussion_b-feature-ablation-study]`). |

---

## 6. Catatan Evaluasi Mendalam per Dimensi (Konsolidasi 22 Isu)

### D1: Ketatnya Metodologi (Methodology Rigor — Reviewer 1)
- **[ISSUE-METH-01] [CRITICAL] Pembagian Data Bebas Kebocoran Identitas**: Penulis wajib memperjelas struktur dataset DemogPairs dan menyatakan secara eksplisit bahwa pembagian data dilakukan secara *subject-disjoint* (0% tumpang tindih identitas individu).
- **[ISSUE-METH-02] [MAJOR] Uji Signifikansi Statistik & 95% CI**: Lakukan uji McNemar pada prediksi data uji dan sertakan Interval Kepercayaan 95% (Wilson/Bootstrap) pada seluruh tabel performa utama.
- **[ISSUE-METH-03] [MAJOR] Pelaporan Skor Cross-Validation (Mean ± Std)**: Tambahkan nilai rata-rata dan deviasi standar validasi silang 5 fold pada Tabel VII s/d X untuk membuktikan stabilitas pelatihan.
- **[ISSUE-METH-04] [MINOR] Penyeimbangan Pelaporan Akurasi OvR**: Lengkapi Tabel XI dengan *False Positive Rate* (FPR) atau *False Negative Rate* (FNR) per subkelompok agar evaluasi biner OvR tidak terdistorsi rasio 5:1.
- **[ISSUE-METH-05] [MINOR] Random Seed & Pilihan Scaler**: Cantumkan nilai seed acak untuk menjamin reprodusibilitas dan diskusikan justifikasi penskalaan fitur.

### D2: Akurasi Domain & SOTA (Domain Accuracy — Reviewer 2)
- **[ISSUE-DOM-01] [MAJOR] Perluasan Baseline Eksternal Standar**: Jangan hanya membandingkan model dengan paper internal sendiri ([19], [20]). Tambahkan baseline model tunggal standar (seperti ResNet-50 standar, ViT-Base ImageNet murni, atau CLIP ViT-B/16 linear probe) pada dataset DemogPairs.
- **[ISSUE-DOM-02] [MINOR] Transparansi Checkpoint HuggingFace**: Dokumentasikan korpus pra-latih dan spesifikasi checkpoint `skutaada` dan `dima806` pada Bagian III-B.
- **[ISSUE-DOM-03] [MINOR] Visualisasi Feature Embedding (t-SNE/UMAP)**: Sertakan visualisasi proyeksi manifold 2D untuk memverifikasi separabilitas klaster demografis secara visual.
- **[ISSUE-DOM-04] [MINOR] Integrasi Landasan Teori Kognitif**: Hubungkan fusi fitur invarian (wajah) dan dinamis (emosi/usia) dengan teori pemrosesan wajah dual-stream (Bruce & Young / Haxby).

### D3: Koherensi Argumen & Logika (Argumentative Coherence — Devil's Advocate)
- **[ISSUE-DA-C1] [CRITICAL] Kalibrasi Narasi Keunggulan Tri-Domain**: Akui keterbatasan kontribusi domain usia dan bahas secara mendalam mengapa pohon keputusan Random Forest mengalami regresi pada fitur 2,304 dimensi.
- **[ISSUE-DA-M1] [MAJOR] Eksperimen Kontrol Dimensionalitas**: Buktikan bahwa peningkatan akurasi bukan artefak penambahan dimensi dengan menjalankan baseline noise control atau analisis teoretis komparatif.
- **[ISSUE-DA-M2] [MAJOR] Penyesuaian Klaim Terminologi Fusi**: Hindari melabeli konkatenasi fitur beku sederhana sebagai "kerangka kerja fusi baru" (*novel architectural framework*); gunakan terminologi yang objektif.
- **[ISSUE-DA-M3] [MAJOR] Justifikasi Pendekatan Frozen Backbone vs Fine-Tuning**: Jelaskan mengapa pendekatan *frozen feature extraction + classical ML* dipilih alih-alih melakukan *end-to-end fine-tuning* pada model ViT tunggal.
- **[ISSUE-DA-m1] [MINOR] Keseimbangan Visualisasi Matriks Konfusi**: Bahas pola galat pada Random Forest untuk mengimbangi visualisasi SVM.
- **[ISSUE-DA-m2] [MINOR] Batasan Definisi Metrik Stabilitas**: Sertakan batasan formal mengenai definisi stabilitas rentang disparitas 4.40 pp.

### D4: Relevansi Lintas Disiplin & Etika (Cross-Perspective — Reviewer 3)
- **[ISSUE-CROSS-01] [MAJOR] Kuantifikasi Metrik Keadilan Algoritmik Formal**: Hitung metrik keadilan standar (*Equal Opportunity Difference*, *Equalized Odds*) dan bahas implikasi kesenjangan sensitivitas 7.50% antara *White Males* (96.94%) dan *Black Females* (89.44%).
- **[ISSUE-CROSS-02] [MINOR] Analisis Biaya Komputasi Inferensi**: Laporkan estimasi latensi inferensi per citra (ms) dan jejak memori GPU dari pengoperasian 3 backbone ViT (~258M parameter).
- **[ISSUE-CROSS-03] [MINOR] Kepatuhan Etika Biometrik & Refleksi Dual-Use**: Sertakan *Ethical Statement* resmi dan refleksi etika bahwa kategorisasi rasial dibatasi oleh taksonomi dataset untuk tujuan audit bias.

### D5: Kualitas Penulisan & Struktur (Writing and Structure — EIC)
- **[ISSUE-EIC-03] [MINOR] Peringkasan Poin Kontribusi**: Padatkan narasi kontribusi Bagian I menjadi 3 butir terfokus dan hindari pengulangan dwi-bahasa yang berlebihan.
- **[ISSUE-EIC-04] [MINOR] Pendalaman Interpretasi Mekanistik**: Perkaya narasi pembahasan dengan analisis batas keputusan antarmodel.

### D6: Kesesuaian Venue & Nilai Tambah (Venue Fit & Contribution — EIC)
- **[ISSUE-EIC-01] [MAJOR] Penegasan Distingsi Kebaruan terhadap Publikasi Terdahulu**: Paparkan wawasan saintifik baru yang membedakan naskah jurnal ini dari prosiding ICVEE 2025 ([19]).
- **[ISSUE-EIC-02] [MINOR] Penyertaan Statuta Transparansi IEEE Access**: Tambahkan subbab resmi *Data Availability Statement* dan *Code Availability Statement*.

---

## 7. Instruksi Revisi & Linimasa

Naskah Anda ditetapkan berstatus **MAJOR REVISION** (setara dengan persiapan untuk putaran *Reject & Resubmit* IEEE Access). Penulis diberikan tenggat waktu **6–8 minggu** untuk menyelesaikan seluruh 22 butir perbaikan pada dokumen rencana aksi (*Revision Roadmap* di `08_revision_roadmap.md`).

Pengajuan revisi putaran kedua (Round 2) wajib menyertakan:
1. Naskah naskah yang telah diperbarui di folder `paper/`.
2. Dokumen resmi surat tanggapan poin-demi-poin (*Point-by-Point Response Letter*).
3. Matriks keterlacakan pemenuhan komitmen (*Traceability Matrix*).
