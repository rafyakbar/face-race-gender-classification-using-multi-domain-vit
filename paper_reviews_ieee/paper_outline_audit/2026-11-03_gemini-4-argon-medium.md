# Audit Kesesuaian `paper_outline_v1.1.md` terhadap `paper_reviews_ieee/`

**Tanggal Audit:** 2026-11-03  
**Auditor:** Gemini 4 Argon (Medium)  
**Objek Audit:** [`paper_outline_v1.1.md`](../../paper_outline_v1.1.md) (911 baris)  
**Dokumen Acuan:**  
- [`paper_reviews_ieee/Comments.md`](../Comments.md) (4 direktif AE, 7 komentar R1, 10 komentar R2)  
- [`paper_reviews_ieee/00_URUTAN_PRIORITAS_REVISI.md`](../00_URUTAN_PRIORITAS_REVISI.md)  
- [`paper_reviews_ieee/08_revision_roadmap.md`](../08_revision_roadmap.md)  
- [`paper_reviews_ieee/09_revision_tracking.md`](../09_revision_tracking.md)  
- [`paper_reviews_ieee/10_response_letter_skeleton.md`](../10_response_letter_skeleton.md)  
**Verifikasi Silang Kode & Data:**  
- [`experiment/code/md/`](../../experiment/code/md/) (`3.0_compare.md`, `3.1_statistical_significance.md`, notebook classifier)  
- [`experiment/code/results/*.json`](../../experiment/code/results/) & [`experiment/code/utils/`](../../experiment/code/utils/) (`dataset.py`, `extraction.py`, `evaluation.py`, `constants.py`)  
- [`images/`](../../images/) (`confusion_matrix_lr_*_v1.1.png`, `vit_v2.2.png`, `sample_demogpairs.png`)

---

## 1. Ringkasan Eksekutif

Secara struktural dan metodologis, [`paper_outline_v1.1.md`](../../paper_outline_v1.1.md) telah mengakomodasi seluruh **21 butir tuntutan revisi** (4 AE + 7 R1 + 10 R2). Namun, **audit forensik lintas-kode, JSON eksperimen, dan gambar menemukan 6 diskrepansi faktual/numerik dan 3 celah kualifikasi klaim** yang sangat berisiko memicu penolakan pada kesempatan *one-shot binary peer review* IEEE Access jika tidak dikoreksi sebelum penulisan draf final.

### Ringkasan Temuan Utama Berdasarkan Tingkat Keparahan:
1. **[KRITIS — F1] Korupsi/Permutasi Label pada 3 Tabel Acuan Matriks Konfusi di Subseksi IV.D (Baris 757–791):** Angka pada 3 tabel acuan Markdown di bawah Subseksi IV.D mengalami permutasi indeks (`DEMOGPairs_LABEL_TO_IDX` vs urutan alfabetis `DEMOGPairs_CLASSES`), sehingga **tidak cocok** dengan gambar [`images/confusion_matrix_lr_*_v1.1.png`](../../images/confusion_matrix_lr_tri_v1.1.png), **tidak cocok** dengan teks narasi IV.D Paragraf 2, dan **tidak cocok** dengan Recall per-subkelompok di Tabel XIV.
2. **[KRITIS — F2] Ketidaksesuaian Ruang Pencarian Hyperparameter Logistic Regression antara Tabel V Outline vs Eksekusi Kode Aktual (R2 #4):** Tabel V & Subseksi III.G di outline mengklaim LR menggunakan **270 kombinasi (1.350 fits)** dengan `C` (5 nilai), `solver` (3 nilai termasuk `'newton-cg'`), dan `max_iter` (3 nilai). Faktanya, di seluruh kode/notebook *subject-disjoint* (`experiment/code/md/lr/*.md`), LR hanya menjalankan **96 kombinasi (480 fits)** (`C`: 4 nilai, `solver`: 2 nilai tanpa `'newton-cg'`, `max_iter`: 2 nilai), sehingga total aktual adalah **912 kombinasi (31.920 fits)**, bukan 1.086 kombinasi (38.010 fits).
3. **[MAYOR — F3] Diskrepansi Angka Latensi Inferensi pada Tabel XI & Teks terhadap JSON Hasil Terbaru (R2 #8 & R1 #5):** Tabel XI dan narasi di outline masih mencantumkan angka latensi dari proses *run* lama (`0.0054 ms` untuk LR, `4.4481 ms` untuk SVM, `0.0537 ms` untuk RF, `0.0083 ms` untuk GNB), sedangkan berkas [`experiment/code/results/*.json`](../../experiment/code/results/) dan [`3.0_compare.md`](../../experiment/code/md/3.0_compare.md) mencatat: LR `0.0046 ms` (`0.004554 ms`), SVM `4.6785 ms`, RF `0.0334 ms`, dan GNB `0.0088 ms` (rasio kecepatan LR vs SVM menjadi **>1.020×**, bukan >820×).
4. **[MAYOR — F4] Inkonsistensi Deskripsi Pra-pemrosesan dan Partisi Dataset pada Subseksi III.A Paragraf 2 (R2 #2 & R2 #3):** Baris 306–308 mengklaim partisi 80/20 menggunakan `StratifiedGroupKFold` dan prapemrosesan menggunakan deteksi MTCNN serta normalisasi $[0, 1]$, padahal kode aktual ([`utils/dataset.py`](../../experiment/code/utils/dataset.py) & [`utils/extraction.py`](../../experiment/code/utils/extraction.py)) membagi subjek per kelas via `train_test_split` dan langsung memproses citra lewat `AutoImageProcessor` ($\mu=\sigma=[0.5, 0.5, 0.5]$ ke $[-1, 1]$) tanpa tahap MTCNN terpisah.
5. **[MAYOR — F5] Kebocoran Klaim Kausal Fenotipik & Overclaim di Luar Subseksi Terkalibrasi (R2 #5, R2 #9, R2 #10):** Walaupun Subseksi IV.B dan IV.D Paragraf 3 sudah dikalibrasi dengan baik, masih terdapat klaim kausal fenotipik tanpa bukti pada Subseksi IV.C Paragraf 2 (baris 724) dan klaim keunggulan mutlak tanpa kualifikasi saturasi SVM di Abstract serta Section V Paragraf 1.
6. **[MAYOR — F6] Desinkronisasi Dokumen Pendukung di `paper_reviews_ieee/` terhadap Outline v1.1:** Berkas [`10_response_letter_skeleton.md`](../10_response_letter_skeleton.md), [`08_revision_roadmap.md`](../08_revision_roadmap.md), dan [`00_URUTAN_PRIORITAS_REVISI.md`](../00_URUTAN_PRIORITAS_REVISI.md) masih memuat angka/referensi usang (mis. waktu ekstraksi "~15 ms/image", normalisasi ImageNet `[0.485, ...]` untuk ViT-Face, kesalahan lintas-gender "<0.4%", kolom 95% CI di Tabel VII–X, dan penomoran Tabel XI–XII lama).

---

## 2. Matriks Evaluasi Butir-demi-Butir terhadap `paper_reviews_ieee/`

| ID Isu | Komentar / Tuntutan Penelaah | Status di Outline v1.1 | Verifikasi & Catatan Audit Detail |
|:---:|---|:---:|---|
| **AE-1** | Kebijakan *Binary Peer Review* (1 kesempatan resubmisi) | **TERPENUHI** | Diatur pada Bab 0 dan Front Matter. |
| **AE-2** | 3 berkas wajib (*Response Letter*, *Highlighted PDF*, *Clean Manuscript*) | **PERLU SINKRONISASI** | Kerangka ada, namun `10_response_letter_skeleton.md` belum sinkron dengan perubahan terbaru di `paper_outline_v1.1.md` (lihat **Temuan F6**). |
| **AE-3** | Penambahan Co-Author (*Request for Byline Change*) | **TERPENUHI** | 5 penulis (termasuk Assoc. Prof. Dr. Shukor Sanim Mohd Fauzi) tercantum lengkap dengan afiliasi dan ORCID di baris 53–58. |
| **AE-4** | Kepatuhan *Resubmission Checklist* 10 butir | **TERPENUHI** | Tata letak gambar/tabel (`figure*`, `table*`), larangan *em dash*, dan batas sitasi telah diatur di Bab 0 dan Master Table. |
| **R1-1** | *Introduction is too long, need to be summarized* | **TERPENUHI** | Section I dipadatkan menjadi 7 paragraf terstruktur (total target 745–995 kata), langsung fokus pada masalah interseksional dan 4 kontribusi inti tanpa bocoran angka hasil. |
| **R1-2** | *Related works needs to be modified in better way and add equations* | **TERPENUHI** | Section II dibagi menjadi 3 subseksi tematik $\times$ 2 paragraf (600–690 kata) dengan tambahan 4 persamaan formal: Eq. (1) KELM, Eq. (2) Patch projection, Eq. (3) MHSA, dan Eq. (4) Multi-domain fusion. |
| **R1-3** | *Figure 3 needs to be redesigned and explained in better way to show novelty* | **TERPENUHI** | Diganti dengan diagram vektor resolusi tinggi `images/vit_v2.2.png` (`figure*`) dengan panduan penjelasan eksplisit tahapan ①–⑦ dan klarifikasi pemrosesan independen per *backbone* di baris 345–350. |
| **R1-4** | *Graph in Figure 4 needs to be discussed in better way* | **PARSIAL (ADA BUG TABEL)** | Narasi IV.D Paragraf 1–2 sudah sangat baik menguraikan matriks konfusi 6×6 (Single 294 error $\to$ Dual 271 $\to$ Tri 245; *same-gender cross-race* 67.3% vs *cross-gender* 32.7%). **NAMUN**, 3 tabel acuan di baris 757–791 mengalami korupsi/permutasi baris-kolom (lihat **Temuan F1**). |
| **R1-5** | *Mention dataset in more detail, show contribution, consider time cost* | **PARSIAL (PERLU KOREKSI ANGKA)** | Detail 600 subjek (100/kelas, 18 citra/subjek) di Tabel I sudah jelas. Namun narasi pembagian data di III.A P2 dan angka latensi di Tabel XI memiliki sedikit ketidaksesuaian dengan JSON terbaru (lihat **Temuan F3 & F4**). |
| **R1-6** | *Compare proposed method with more methods to validate contribution* | **PARSIAL** | Tabel XV membandingkan dengan 2 studi eksternal (Bagian A) dan 9 konfigurasi internal (Bagian B). Perlu dipastikan dalam narasi bahwa 9 konfigurasi Bagian B dibingkai sebagai *internal architectural & representation baselines* (single/dual/tri lintas 4 famili classifier), karena tidak ada *reproduced external SOTA architecture* baru (mis. ResNet/MaxViT/Swin) yang dieksekusi pada split *subject-disjoint*. |
| **R1-7** | *Conclusion part does not show the contribution in good way* | **PARSIAL** | Section V Paragraf 1 sudah merangkum kontribusi, tetapi poin 1 & 3 masih terdengar mutlak tanpa menyebut kualifikasi saturasi fitur pada SVM dan batas evaluasi satu dataset (lihat **Temuan F5**). |
| **R2-1** | *Novelty beyond concatenating three pretrained representations* | **TERPENUHI** | Dijelaskan secara jujur dan kokoh di Section I P5–P6, Section II.C P2, dan Section III.B P1 bahwa *novelty* terletak pada sinergi ruang laten komplementer bebas interferensi gradien, evaluasi *strict subject-disjoint*, uji inferensial McNemar, dan efisiensi komputasi tepi (*Edge AI*). |
| **R2-2** | *Clarify identity overlap and provide subject-disjoint evaluation* | **TERPENUHI** | Diselesaikan secara tuntas lewat arsitektur **Dual-Benchmark**: Primary Benchmark *Subject-Disjoint* (480 subjek latih / 120 subjek uji, 0% leakage; LR 88.66%, SVM 88.61%) pada Tabel VII–X dan *Data Leakage Ablation Study* (penurunan 5.09 pp dari 93.70%) pada Tabel XII. |
| **R2-3** | *Specify exact checkpoint versions, image processors, normalization, extraction* | **PARSIAL (INKONSISTENSI KECIL)** | Subseksi III.B P2 sudah sangat presisi mencantumkan ID HuggingFace, SHA commit (`e85f0c9`, `747cf16`, `ad35933`), resolusi $224 \times 224$, normalisasi $\mu=\sigma=[0.5, 0.5, 0.5]$, dan ekstraksi token `[CLS]` Layer 12 Eq. (7). Namun perlu diselaraskan dengan klaim $[0, 1]$ di III.A P2 (lihat **Temuan F4**). |
| **R2-4** | *Reconcile totals of 1,086 configurations, 38,010 fits, and 28 refits with Tables 3–6* | **BERMASALAH (DISKREPANSI KODE)** | Secara aritmetika di dalam teks outline, $288 + 240 + 270 + 288 = 1.086 \times 35 = 38.010$ terlihat konsisten. **TETAPI** di kode eksperimen *subject-disjoint* aktual, LR hanya mengevaluasi **96 kombinasi**, bukan 270! Selain itu, pada SVM, parameter `degree` `[2, 3]` dan `gamma` `['scale', 'auto']` dikalikan ke seluruh kernel termasuk `linear` dan `rbf` (lihat **Temuan F2**). |
| **R2-5** | *Statistical interpretation (McNemar test) & qualification of tri-domain superiority / saturation* | **PARSIAL** | Subseksi IV.B P1 & P3 serta Tabel XIII sangat presisi menyajikan uji McNemar Edwards & Exact Binomial ($p = 0.7343$ saturasi pada SVM Tri vs Dual; $p = 0.0073$ signifikan pada LR Tri vs Dual; $p = 1.0000$ ekuivalensi LR vs SVM). Namun kualifikasi penting ini belum tercermin di Abstract dan Section V P1 (lihat **Temuan F5**). |
| **R2-6** | *Clarify scope and limitations of fairness claims (EOD)* | **TERPENUHI** | Subseksi III.H P2 (Eq. 23) dan Subseksi IV.C P2 (Tabel XIV) secara eksplisit membatasi $\text{EOD} = 9.72\text{ pp}$ sebagai indikator disparitas TPR empiris antarsubkelompok, bukan jaminan keadilan demografis universal. |
| **R2-7** | *Clarify whether prior methods used comparable partitions; present as contextual* | **TERPENUHI** | Subseksi IV.E dan Tabel XV memisahkan secara tegas **Part A (Contextual Comparison — Subject-Overlap)** dan **Part B (Controlled Comparison — Subject-Disjoint)** disertai larangan pemeringkatan silang. |
| **R2-8** | *Report feature extraction time, training time, inference latency, memory, model storage* | **PARSIAL (PERLU UPDATE ANGKA)** | Kelima dimensi telah disajikan secara lengkap di Subseksi IV.A P6 dan Tabel XI, namun angka latensi inferensi perlu disinkronkan dengan berkas JSON hasil terbaru (lihat **Temuan F3**). |
| **R2-9** | *Interpretations concerning phenotypic overlap & age features should be qualified* | **PARSIAL** | Subseksi IV.D P3 sudah sangat patuh membatasi klaim pada frekuensi *off-diagonal* matriks konfusi. Namun pada Subseksi IV.C P2 (baris 724) masih terselip klaim kausal *"dipengaruhi oleh variasi fenotipik kraniofasial dan kontras pencahayaan"* (lihat **Temuan F5**). |
| **R2-10** | *Conclusions should be restricted to the evaluated DemogPairs benchmark* | **TERPENUHI** | Section V Paragraf 2 secara eksplisit membatasi generalisasi pada 3 kelompok ras makro DemogPairs (Asian, Black, White) dan menguraikan kebutuhan validasi lintas-dataset (*in-the-wild*). |

---

## 3. Penjabaran Detail Temuan Kritis & Mayor (Bukti Forensik & Solusi)

### Temuan F1 [KRITIS]: Korupsi/Permutasi Label pada 3 Tabel Acuan Matriks Konfusi di Subseksi IV.D (Baris 757–791)
* **Lokasi di Outline:** Subseksi IV.D (*Error Pattern Assessment*), baris 757–791 (`Tabel Acuan Matriks Konfusi (a) Single-Domain`, `(b) Dual-Domain`, dan `(c) Tri-Domain`).
* **Bukti Forensik:**
  Di dalam kode [`experiment/code/utils/constants.py`](../../experiment/code/utils/constants.py), pemetaan indeks label ke angka adalah:
  `{0: Black_Males, 1: White_Females, 2: Asian_Males, 3: White_Males, 4: Black_Females, 5: Asian_Females}`.
  Saat tabel acuan di baris 757–791 dibuat, matriks konfusi berurutan indeks `0..5` langsung dilabeli dengan urutan alfabetis `Asian_Females, Asian_Males, Black_Females, Black_Males, White_Females, White_Males` tanpa pemetaan ulang! Akibatnya:
  - Pada Tabel Acuan (c) Tri-Domain (baris 783–791), diagonal utama tertulis:
    `Asian_Females = 316`, `Asian_Males = 326`, `Black_Females = 316`, `Black_Males = 340`, `White_Females = 305`, `White_Males = 312`.
  - Padahal nilai sebenarnya (sesuai [`images/confusion_matrix_lr_tri_v1.1.png`](../../images/confusion_matrix_lr_tri_v1.1.png), output [`2.5.7_lr_vit-face-emotion-age.md`](../../experiment/code/md/lr/2.5.7_lr_vit-face-emotion-age.md) baris 474–480, dan Tabel XIV baris 707–712) adalah:
    - `Asian_Females`: **312** (Recall 86.67%) — *di tabel tertulis 316 (milik Black_Males)*
    - `Asian_Males`: **316** (Recall 87.78%) — *di tabel tertulis 326 (milik White_Females)*
    - `Black_Females`: **305** (Recall 84.72%) — *di tabel tertulis 316 (milik Asian_Males)*
    - `Black_Males`: **316** (Recall 87.78%) — *di tabel tertulis 340 (milik White_Males)*
    - `White_Females`: **326** (Recall 90.56%) — *di tabel tertulis 305 (milik Black_Females)*
    - `White_Males`: **340** (Recall 94.44%) — *di tabel tertulis 312 (milik Asian_Females)*
  - Hal yang sama terjadi pada seluruh sel *off-diagonal* di ketiga tabel acuan (a), (b), dan (c). Contohnya, pada Tabel (c) baris 785 tertulis `Asian_Females -> Asian_Males = 0`, padahal di narasi baris 749 dan di gambar Figure 4(c) nilainya adalah **18**.
* **Dampak:** Meskipun tabel tersebut diberi catatan *Non-Numbered*, penulis atau agen AI yang menyusun draf naskah dari `paper_outline_v1.1.md` dapat menyalin angka yang salah dari tabel tersebut ke dalam teks pembahasan.
* **Solusi Wajib:** Ganti ketiga tabel acuan di baris 757–791 dengan matriks terurut alfabetis yang benar sesuai `2.5.1_lr_vit-face.md` (baris 431–437), `2.5.6_lr_vit-emotion-face.md` (baris 461–467), dan `2.5.7_lr_vit-face-emotion-age.md` (baris 474–480).

---

### Temuan F2 [KRITIS]: Ketidaksesuaian Ruang Pencarian Hyperparameter Logistic Regression & Redundansi Grid SVM (R2 #4)
* **Lokasi di Outline:** Subseksi III.E Tabel V (baris 433–442), Subseksi III.F Tabel VI (baris 453–463), dan Subseksi III.G (baris 466–483).
* **Bukti Forensik:**
  1. **Logistic Regression (Tabel V vs Kode Aktual):**
     - Di `paper_outline_v1.1.md` Tabel V tertulis: `C` = `[0.01, 0.1, 1, 10, 100]` (5), `solver` = `['lbfgs', 'saga', 'newton-cg']` (3), `max_iter` = `[500, 1000, 2000]` (3) $\to$ $2 \times 3 \times 5 \times 3 \times 3 = \mathbf{270\text{ kombinasi (1.350 fits)}}$.
     - Di kode eksperimen aktual ([`experiment/code/md/lr/2.5.1_lr_vit-face.md`](../../experiment/code/md/lr/2.5.1_lr_vit-face.md) s.d. `2.5.7` baris 241–281 dan kolom `parameter_combinations` di tabel hasil baris 515), grid yang dieksekusi adalah:
       `C` = `[0.01, 0.1, 1, 10]` (4), `solver` = `['lbfgs', 'saga']` (2), `max_iter` = `[500, 1000]` (2) $\to$ $2 \times 3 \times 4 \times 2 \times 2 = \mathbf{96\text{ kombinasi (480 fits)}}$.
     - Akibatnya, total kombinasi yang benar-benar dijalankan pada eksperimen *subject-disjoint* adalah $288\text{ (SVM)} + 96\text{ (LR)} + 288\text{ (RF)} + 240\text{ (GNB)} = \mathbf{912\text{ kombinasi}}$ per skema fitur ($912 \times 5 = 4.560\text{ fits/skema} \times 7 = \mathbf{31.920\text{ CV fits}}$), bukan 1.086 kombinasi / 38.010 fits.
  2. **Support Vector Machine (Tabel VI vs `10_response_letter_skeleton.md`):**
     - Di kode aktual (`2.1.1_svm_vit-face.md` baris 243–259), `grid_params` menggunakan satu dictionary datar (*Cartesian product* penuh): $2\text{ (scaler)} \times 3\text{ (pca)} \times 4\text{ (C)} \times 3\text{ (kernel)} \times 2\text{ (degree)} \times 2\text{ (gamma)} = 288\text{ kombinasi}$. Karena `degree` tidak digunakan oleh kernel `linear` dan `rbf`, serta `gamma` tidak digunakan oleh kernel `linear`, terdapat kombinasi efektif yang lebih kecil (108 kombinasi unik) dari 288 *grid evaluations* yang dieksekusi `GridSearchCV`.
     - Lebih berbahaya lagi, di [`10_response_letter_skeleton.md`](../10_response_letter_skeleton.md) baris 207 tertulis rumus palsu: `[1 linear + 1 rbf × 2 gamma + 1 poly × 2 degrees × 2 gamma] = 2 × 3 × 4 × 12 = 288` (padahal $1 + 2 + 4 = 7 \neq 12$, dan $2 \times 3 \times 4 \times 7 = 168 \neq 288$).
* **Dampak:** Reviewer 2 secara spesifik memeriksa aritmetika ruang pencarian di R2 #4. Jika kode repositori memperlihatkan 96 kombinasi untuk LR atau jika surat respons memuat aritmetika $1+2+4=12$, kredibilitas manuskrip akan runtuh.
* **Solusi Wajib:**
  - Putuskan apakah akan: **(Opsi A — Disarankan jika tidak ingin re-run LR)** melaporkan angka jujur sesuai kode yang dieksekusi di `experiment/code/md/` (LR = 96 kombinasi / 480 fits; Total = 912 kombinasi / 31.920 CV fits) sambil menjelaskan di Response Letter bahwa ruang pencarian LR dirampingkan pada saat re-benchmarking *subject-disjoint* (menghapus `C=100`, `newton-cg`, dan `max_iter=2000` yang redundan), **ATAU (Opsi B)** mempertahankan 270 kombinasi / 38.010 fits di naskah tetapi wajib menyelaraskan penjelasan *full Cartesian grid* SVM ($2 \times 3 \times 4 \times 3 \times 2 \times 2 = 288$ evaluasi grid dengan 108 konfigurasi fungsional unik karena `degree` hanya aktif pada `poly`) baik di outline maupun di `10_response_letter_skeleton.md`.

---

### Temuan F3 [MAYOR]: Diskrepansi Angka Latensi Inferensi pada Tabel XI, Bab 0, Abstract, dan Section V terhadap JSON Hasil Terbaru (R2 #8 & R1 #5)
* **Lokasi di Outline:** Bab 0 (baris 25), Subseksi IV.A Paragraf 6 & Tabel XI (baris 623, 633–636), serta Section V Paragraf 1 (baris 844).
* **Bukti Forensik:**
  Perbandingan antara angka di `paper_outline_v1.1.md` (yang diambil dari `README.md` lama) vs berkas JSON hasil evaluasi aktual di [`experiment/code/results/*.json`](../../experiment/code/results/) dan [`experiment/code/md/3.0_compare.md`](../../experiment/code/md/3.0_compare.md):

  | Model Terbaik per Famili | Latensi di Outline v1.1 (Tabel XI) | Latensi Aktual di `results/*.json` & `3.0_compare.md` | Ukuran Model (`results/*.json`) | Waktu Training (`train_time_seconds`) |
  |---|:---:|:---:|:---:|:---:|
  | **LR Tri-Domain** | `0.0054 ms` | **`0.0046 ms`** (`0.004554 ms`) | `0.11 MB` (`0.1081 MB`) | `3,287.07 s` (`54.8 min`) |
  | **SVM Tri-Domain** | `4.4481 ms` | **`4.6785 ms`** (`4.678548 ms`) | `36.60 MB` (`36.5960 MB`) | `30,666.02 s` (`511.1 min`) |
  | **RF Tri-Domain** | `0.0537 ms` | **`0.0334 ms`** (`0.033450 ms`) | `6.19 MB` (`6.1883 MB`) | `6,628.03 s` (`110.5 min`) |
  | **GNB Dual-Domain** | `0.0083 ms` | **`0.0088 ms`** (`0.008789 ms`) | `0.78 MB` (`0.7799 MB`) | `1,529.47 s` (`25.5 min`) |

* **Dampak:** Karena waktu training (`54.8 min`, `511.1 min`, `110.5 min`, `25.5 min`) diambil dari `results/*.json` terbaru sementara latensi inferensi diambil dari tabel `README.md` lama, terjadi ketidakcocokan internal terhadap berkas sumber yang sama. Selain itu, dengan angka JSON terbaru, rasio kecepatan inferensi LR vs SVM adalah $4.6785 / 0.004554 = \mathbf{1.027\times}$ (**>1.000× lebih cepat**, atau ~866× jika memakai 0.0054 ms vs 4.6785 ms).
* **Solusi Wajib:** Sinkronkan kolom `Inference (ms/sample)` pada Tabel XI, narasi IV.A P6, Bab 0.A.4, `README.md`, dan `10_response_letter_skeleton.md` agar menggunakan satu sumber kebenaran tunggal (disarankan mengikuti `results/*.json` & `3.0_compare.md`: `0.0046 ms`, `4.6785 ms`, `0.0334 ms`, `0.0088 ms`).

---

### Temuan F4 [MAYOR]: Inkonsistensi Teknis Partisi Data dan Pra-pemrosesan Citra antara Subseksi III.A P2 vs III.B P2 & Kode Aktual (R2 #2 & R2 #3)
* **Lokasi di Outline:** Subseksi III.A Paragraf 2 (baris 306 & 308) vs Subseksi III.B Paragraf 2 (baris 360).
* **Bukti Forensik:**
  1. **Metode Split Train/Test 80/20:** Baris 306 menyatakan *"Isolasi subjek secara ketat menggunakan pembagian 80/20 berbasis identitas (`StratifiedGroupKFold`, groups = `subject_id`): 480 subjek latih (8.640 citra) dan 120 subjek uji held-out (2.160 citra)"*. Faktanya, di [`utils/dataset.py`](../../experiment/code/utils/dataset.py) (fungsi `split_demogpairs_subject_disjoint`, baris 60–66), pemisahan 480 subjek latih vs 120 subjek uji dilakukan menggunakan `train_test_split(sorted_subs, train_size=0.8, random_state=42)` secara terstratifikasi tepat 80/20 subjek per kelas demografis, sedangkan `StratifiedGroupKFold(n_splits=5)` digunakan untuk **5-fold cross-validation di dalam 480 subjek latih**.
  2. **Deteksi MTCNN & Rentang Normalisasi $[0, 1]$ vs $[-1, 1]$:** Baris 308 menyatakan *"Preprocessing citra mencakup konversi ke 3-channel RGB, deteksi dan face alignment MTCNN, resize ke resolusi 224×224 piksel, dan normalisasi intensitas kanal ke rentang [0, 1]"*. Sementara itu, Baris 360 menyatakan citra dinormalisasi dengan $\mu = [0.5, 0.5, 0.5]$ dan $\sigma = [0.5, 0.5, 0.5]$, yang secara matematis memetakan piksel $[0, 1]$ menjadi $\frac{x - 0.5}{0.5} \in [-1, 1]$. Selain itu, dataset DemogPairs memang sudah berupa citra wajah yang telah di-*crop/align* sejak awal oleh pembuat dataset (Hupont & Fernández, 2019), dan kode [`utils/extraction.py`](../../experiment/code/utils/extraction.py) langsung memuat citra via PIL `Image.open(img).convert("RGB")` ke `AutoImageProcessor` (yang melakukan *rescaling* $1/255$ ke $[0, 1]$ diikuti normalisasi $\mu=\sigma=0.5$ ke $[-1, 1]$).
* **Solusi Wajib:**
  - Di Subseksi III.A P2 (baris 306): Perjelas bahwa partisi 80/20 tingkat subjek dilakukan secara terstratifikasi per subkelompok (80 subjek latih / 20 subjek uji per kelas, `random_state=42`), sementara `StratifiedGroupKFold` ($k=5$) diterapkan pada tahap validasi silang atas 480 subjek latih.
  - Di Subseksi III.A P2 (baris 308): Jelaskan bahwa citra wajah pada dataset DemogPairs yang telah ter-align dikonversi ke format 3-channel RGB, di-resize ke $224 \times 224$ piksel, di-*rescale* ke $[0, 1]$, dan dinormalisasi oleh `AutoImageProcessor` masing-masing *backbone* ViT menggunakan $\mu = \sigma = [0.5, 0.5, 0.5]$ ke rentang $[-1, 1]$.

---

### Temuan F5 [MAYOR]: Sisa Klaim Kausal Fenotipik & Kualifikasi Klaim Keunggulan di Abstract, IV.C P2, dan Section V P1 (R2 #5, R2 #9, R2 #10)
* **Lokasi di Outline:**
  1. **Subseksi IV.C Paragraf 2 (Baris 724):** Tertulis *"Capaian ini secara faktual merefleksikan disparitas performa empiris antarsubkelompok yang dipengaruhi oleh variasi fenotipik kraniofasial dan kontras pencahayaan pada citra wajah."* Kalimat ini melanggar langsung **R2 #9** (*"interpretations concerning phenotypic overlap... remain insufficiently supported"*) dan melanggar aturan internal **Bab 0.B.3** serta **Subseksi IV.D Paragraf 3**.
  2. **Abstract (Baris 61–68):**
     - Menyajikan hasil *Subject-Overlap* (93.70%) sebagai poin (1) sebelum *Subject-Disjoint* (88.66%) sebagai poin (2), padahal *Subject-Disjoint* adalah Primary Benchmark dan *Subject-Overlap* adalah ablasi kebocoran data.
     - Belum menyebutkan bahwa secara statistik LR Tri (88.66%) dan SVM Tri (88.61%) adalah ekuivalen ($p = 1.0000$) atau bahwa keunggulan signifikansi ($p < 0.001$) diuji pada dataset DemogPairs.
  3. **Section V Paragraf 1 (Baris 841–843):**
     - Butir 1 & 3 menyatakan *"berhasil membuktikan efektivitas fusi representasi multi-domain"* dan *"Uji McNemar berpasangan membuktikan keunggulan fusi multi-domain signifikan secara statistik ($p < 0.001$)"* tanpa menyebutkan kualifikasi inti yang diminta **R2 #5**: yaitu bahwa keunggulan signifikan ($p < 0.001$) adalah terhadap *single-domain* biometrik wajah, sedangkan transisi *dual-domain* ke *tri-domain* memberikan peningkatan signifikan pada LR linier ($p = 0.0073$) namun mengalami *asymptotic feature saturation* pada SVM non-linier ($p = 0.7343$).
* **Solusi Wajib:**
  - Pada IV.C P2 (baris 724): Hapus klaim kausal *"yang dipengaruhi oleh variasi fenotipik kraniofasial dan kontras pencahayaan"*, atau ubah menjadi pernyataan observasional murni berdasarkan distribusi kesalahan empiris pada sampel uji DemogPairs.
  - Pada Abstract (baris 64–67): Balik urutan penyajian hasil agar **Primary Benchmark Subject-Disjoint (Zero Identity Leakage: LR 88.66%, SVM 88.61%)** disebutkan lebih dulu sebagai capaian utama, diikuti **Subject-Overlap (93.70%)** sebagai studi ablasi untuk menguantifikasi efek memorisasi identitas sebesar 5.09 pp pada benchmark DemogPairs.
  - Pada Section V P1 (baris 841–843): Tambahkan kualifikasi bahwa keunggulan atas *single-domain* signifikan ($p < 0.001$), sementara penambahan domain usia menghasilkan peningkatan signifikan pada LR ($p = 0.0073$) namun mencapai *asymptotic feature saturation* pada SVM ($p = 0.7343$).

---

### Temuan F6 [MAYOR]: Desinkronisasi Dokumen Dossier `paper_reviews_ieee/` terhadap `paper_outline_v1.1.md`
* **Lokasi:** [`paper_reviews_ieee/10_response_letter_skeleton.md`](../10_response_letter_skeleton.md), [`08_revision_roadmap.md`](../08_revision_roadmap.md), dan [`00_URUTAN_PRIORITAS_REVISI.md`](../00_URUTAN_PRIORITAS_REVISI.md).
* **Bukti Forensik:**
  Karena `paper_outline_v1.1.md` telah mengalami pembaruan besar pada sesi 31 Oktober – 3 November 2026, berkas-berkas di `paper_reviews_ieee/` (yang dibuat pada 28 Oktober 2026) tertinggal dan memuat kontradiksi langsung terhadap outline v1.1:
  1. **Waktu Ekstraksi Fitur (R1-5 & R2-8):** Di `10_response_letter_skeleton.md` (baris 31, 110, 270) tertulis `~15 ms/image` (`~45.6 ms` untuk 3 ViT). Di `paper_outline_v1.1.md` (Tabel XI), waktu ekstraksi GPU terukur adalah **`124.5 ms/citra`** untuk tri-domain (`39.7 ms` Face, `39.7 ms` Emotion, `45.1 ms` Age).
  2. **Parameter Normalisasi `ViT-Face` (R2-3):** Di `10_response_letter_skeleton.md` (baris 191) tertulis `mean: [0.485, 0.456, 0.406], std: [0.229, 0.224, 0.225]`, dan merujuk ke "Table II" sebagai tabel spesifikasi checkpoint. Di `paper_outline_v1.1.md` (baris 360), telah diverifikasi bahwa ketiga model menggunakan **`mean = std = [0.5, 0.5, 0.5]`**, dan spesifikasi checkpoint disajikan secara naratif (Tabel II adalah tabel 7 skema fusi).
  3. **Proporsi Kesalahan Lintas-Gender (R1-4):** Di `10_response_letter_skeleton.md` (baris 94) tertulis *"cross-gender misclassifications are virtually nonexistent (<0.4%)"*. Di `paper_outline_v1.1.md` (baris 749), kesalahan lintas-gender pada LR Tri adalah **80 citra (3.70% dari $N=2.160$; 32.7% dari total kesalahan)**.
  4. **Penomoran Tabel & Kolom 95% CI:** `10_response_letter_skeleton.md` masih merujuk Tabel XI sebagai *Leakage Ablation* dan Tabel XII sebagai *Comparison with Prior Studies*, serta `08_revision_roadmap.md` masih menyebut kolom 95% CI di Tabel VII–X. Di `paper_outline_v1.1.md`, urutan tabel adalah: **Tabel XI** (Efisiensi Komputasi), **Tabel XII** (Ablasi Leakage), **Tabel XIII** (Uji McNemar), **Tabel XIV** (Performa Subkelompok & EOD), dan **Tabel XV** (Komparasi Studi Terdahulu), serta kolom 95% CI pada Tabel VII–X telah dihapus dan dipindahkan ke narasi.
* **Solusi Wajib:** Mutakhirkan `10_response_letter_skeleton.md` setelah draf naskah selesai agar seluruh angka, parameter normalisasi, dan nomor tabel/persamaan selaras 100% dengan `paper_outline_v1.1.md`.

---

## 4. Audit Konsistensi Penomoran Master Elements (Figures, Tables, Equations)

Pemeriksaan urutan kronologis seluruh elemen di dalam [`paper_outline_v1.1.md`](../../paper_outline_v1.1.md):
- **Figures (Figure 1 – Figure 4):** Urutan kemunculan kronologis (`Figure 1` di III.Overview $\to$ `Figure 2` di III.A $\to$ `Figure 3` di III.B $\to$ `Figure 4` di IV.D), seluruhnya berformat `figure*` dan memiliki berkas gambar valid di `images/`. **STATUS: 100% KONSISTEN.**
- **Tables (Table I – Table XV):** Urutan kemunculan kronologis dari `Table I` hingga `Table XV` lengkap tanpa nomor ganda atau terlewat. **Catatan kecil:** Pada Master Table baris 869, judul `Table II` tertulis *"Multi-Domain Feature Fusion and Systematic Ablation Configurations."*, sedangkan judul di atas tabel pada baris 377 tertulis *"Table II. Multi-Domain Feature Fusion and Systematic Ablation Configurations."* (sudah cocok); namun pada `Table VI` baris 453 tertulis *"Table VI. Hyperparameter Search Space for Support Vector Machine."* sementara di Master Table baris 873 tertulis *"Hyperparameter Search Space for Support Vector Machine Classifier."* (tambahkan kata *"Classifier"* di baris 453 agar identik 100%).
- **Equations (Eq. 1 – Eq. 23):** Seluruh 23 persamaan matematika (`\tag{1}` s.d. `\tag{23}`) berurutan kronologis ketat dari Section II.A hingga Section III.H tanpa ada nomor yang melompat atau terduplikasi. **STATUS: 100% KONSISTEN.**

---

## 5. Daftar Periksa Perbaikan (Actionable Checklist) pada `paper_outline_v1.1.md`

| Prioritas | Target Baris di `paper_outline_v1.1.md` | Tindakan Perbaikan Spesifik |
|:---:|:---:|---|
| **P1 (Wajib)** | Baris 757–791 (Subseksi IV.D) | Perbaiki ketiga tabel acuan matriks konfusi (Single, Dual, Tri) yang mengalami permutasi indeks label agar sesuai 100% dengan gambar `confusion_matrix_lr_*_v1.1.png` dan output `experiment/code/md/lr/`. |
| **P1 (Wajib)** | Baris 433–442, 453–463, 466–483 (Subseksi III.E, III.F, III.G) | Rekonsiliasikan perbedaan grid LR (270 kombinasi di Tabel V vs 96 kombinasi di kode aktual) dan tambahkan catatan penjelasan *effective vs full Cartesian grid* untuk parameter `degree`/`gamma` pada SVM (Tabel VI). |
| **P1 (Wajib)** | Baris 25, 623, 633–636, 844 (Bab 0, Tabel XI, Section V) | Perbarui angka latensi inferensi (`0.0054` $\to$ `0.0046 ms`, `4.4481` $\to$ `4.6785 ms`, `0.0537` $\to$ `0.0334 ms`, `0.0083` $\to$ `0.0088 ms`) agar sesuai 100% dengan berkas `experiment/code/results/*.json` dan `3.0_compare.md`. |
| **P1 (Wajib)** | Baris 306–308 (Subseksi III.A P2) | Luruskan deskripsi pemisahan 80/20 subjek (`train_test_split` per kelas untuk isolasi 480/120 subjek, diikuti 5-Fold `StratifiedGroupKFold` pada set latih) serta hapus klaim MTCNN terpisah dan selaraskan penjelasan rescaling $[0, 1] \to$ normalisasi $\mu=\sigma=0.5$ ($[-1, 1]$). |
| **P2 (Penting)** | Baris 64–68, 724, 841–843 (Abstract, IV.C P2, Section V P1) | (1) Dahulukan hasil Primary Benchmark Subject-Disjoint (88.66%) di atas Subject-Overlap (93.70%) pada Abstract; (2) hapus atribusi kausal fenotipik/pencahayaan di IV.C P2 baris 724; (3) cantumkan kualifikasi *asymptotic feature saturation* SVM ($p=0.7343$) vs signifikansi LR ($p=0.0073$) di Section V P1. |
| **P3 (Editorial)** | Baris 453 & `paper_reviews_ieee/10_response_letter_skeleton.md` | Samakan caption `Table VI` (tambahkan kata *"Classifier"*) dan mutakhirkan `10_response_letter_skeleton.md` agar seluruh angka dan nomor tabel sinkron dengan `paper_outline_v1.1.md`. |
