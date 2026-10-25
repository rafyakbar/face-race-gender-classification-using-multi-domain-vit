# Kompilasi Komentar Reviewer IEEE Access

Dokumen ini berisi kompilasi lengkap komentar dan masukan dari Associate Editor serta Reviewer 1 dan Reviewer 2 untuk naskah **`Access-2026-50857`** yang diterjemahkan dan dijelaskan ke dalam Bahasa Indonesia formal dengan tetap menyertakan teks asli bahasa Inggris sebagai rujukan presisi.

---

## 📌 Informasi Manuskrip & Keputusan Editorial

- **ID Manuskrip:** `Access-2026-50857`
- **Judul Artikel:** *Multi-Domain Vision Transformer Fusion for Intersectional Demographic Classification from Facial Images*
- **Target Publikasi:** IEEE Access (Open Access, Q1)
- **Associate Editor:** Dr. Vincenzo Conti (`vincenzo.conti@unikore.it`, `vinc.conti@gmail.com`)
- **Article Administrator:** Mr. Adesh Choudhary (`adesh.choudhary@ieee.org`)
- **Tanggal Keputusan:** 20 Oktober 2026
- **Status Keputusan:** **Reject & Resubmit** (*Ditolak dengan 1 Kesempatan Resubmission*)
- **Ketentuan Resubmission IEEE Access:**
  - IEEE Access menerapkan model penelaahan biner (*binary peer review*), di mana naskah ditolak bahkan jika hanya memerlukan revisi minor.
  - Penulis diberikan tepat **satu kesempatan** (*one opportunity*) untuk mengajukan manuskrip yang telah diperbaiki.
  - Tiga berkas utama yang wajib diunggah pada portal resubmission:
    1. *Author's Response Files* (Surat tanggapan rinci *point-by-point* berbasis *template* resmi IEEE Access).
    2. *Highlighted PDF* (Naskah revisi berformat PDF dengan penandaan/sorotan kuning pada seluruh perubahan teks, rumus, dan tabel).
    3. *Main Manuscript* (Naskah final bersih tanpa sorotan dalam format LaTeX source/ZIP dan PDF).
    4. Dokumen administratif tambahan: formulir perubahan daftar penulis (*Request for Byline Change*) jika terdapat pembaruan susunan penulis, serta *Resubmission Checklist*.

---

## 👨‍🏫 Reviewer 1 (R1)

### Catatan Pengantar
> *"Dear authors, thanks for your valuable work, this manuscript can be acceptable for publication after reviewing it according to the following comments:"*  
> *(Yang terhormat para penulis, terima kasih atas karya Anda yang berharga. Manuskrip ini dapat diterima untuk publikasi setelah direvisi sesuai dengan komentar-komentar berikut:)*

---

### Rincian 7 Komentar Reviewer 1

#### 1. Bagian Pendahuluan (*Introduction*) Terlalu Panjang
- **Teks Asli:**  
  > *"1. the introduction is too long need to be summarized."*
- **Terjemahan & Penjelasan:**  
  Bagian Pendahuluan (*Section I: Introduction*) dinilai terlalu panjang dan perlu diringkas/dipadatkan. Narasi latar belakang, motivasi, dan kesenjangan riset harus disajikan secara lebih ringkas dan fokus langsung pada permasalahan inti klasifikasi demografis interseksional.

---

#### 2. Restrukturisasi Bagian Studi Terkait (*Related Works*) & Penambahan Persamaan Matematika
- **Teks Asli:**  
  > *"2. The related works needs to be modified in better way and add equations."*
- **Terjemahan & Penjelasan:**  
  Bagian penelitian terkait (*Section II: Related Works*) perlu dimodifikasi agar memiliki alur dan pengorganisasian tematik yang lebih baik, serta wajib menambahkan formulasi atau persamaan matematis yang merepresentasikan metode-metode dalam literatur sebelumnya guna memperkuat landasan teoretis.

---

#### 3. Perancangan Ulang dan Penjelasan Figure 3 (Diagram Arsitektur ViT)
- **Teks Asli:**  
  > *"3. The figure 3 needs to be redesigned and explained in better way to show the novelty of the proposed method and also not clear."*
- **Terjemahan & Penjelasan:**  
  Gambar 3 (*Figure 3*, diagram arsitektur Vision Transformer dan proyeksi patch) saat ini dinilai kurang jelas. Gambar ini harus didesain ulang agar lebih informatif, berkualitas visual tinggi, dan dijelaskan secara lebih gamblang di dalam narasi untuk menonjolkan kebaruan (*novelty*) dari metode yang diusulkan.

---

#### 4. Pembahasan Lebih Mendalam Terhadap Grafik Figure 4
- **Teks Asli:**  
  > *"4. Graph in figure 4 needs to be discussed in better way."*
- **Terjemahan & Penjelasan:**  
  Grafik pada Gambar 4 (*Figure 4*, visualisasi matriks konfusi dan pola kesalahan) perlu dibahas dan dianalisis secara lebih mendalam pada bagian Hasil dan Pembahasan, tidak sekadar menampilkan angka, melainkan menguraikan dinamika kesalahan klasifikasi antar-subkelompok demografis.

---

#### 5. Rincian Dataset, Penegasan Kontribusi, dan Evaluasi Biaya Waktu (*Time Cost*)
- **Teks Asli:**  
  > *"5. Experimental works need to mention the dataset used in more detail and show the contribution of your proposed method and also to consider the time cost in the evaluation."*
- **Terjemahan & Penjelasan:**  
  Bagian eksperimen (*Section III & IV*) harus menguraikan karakteristik dataset DemogPairs secara lebih mendalam, mempertegas kontribusi nyata dari metode yang diajukan, serta menyertakan evaluasi biaya komputasi/waktu eksekusi (*time cost* / *latency* / durasi pelatihan dan ekstraksi) dalam analisis performa.

---

#### 6. Perbandingan dengan Lebih Banyak Metode Acuan (*Baselines*)
- **Teks Asli:**  
  > *"6. the authors need to compare their proposed method with more methods to validate their contribution."*
- **Terjemahan & Penjelasan:**  
  Penulis diminta untuk membandingkan kerangka kerja yang diusulkan dengan lebih banyak metode pembanding (*baseline methods*), baik dari model arsitektur sejenis maupun studi literatur terdahulu, guna memvalidasi efektivitas dan kontribusi empiris metode.

---

#### 7. Penyempurnaan Bagian Kesimpulan (*Conclusion*)
- **Teks Asli:**  
  > *"7. conclusion part does not show the contribution in good way."*
- **Terjemahan & Penjelasan:**  
  Bagian Kesimpulan (*Section V: Conclusion*) belum menampilkan dan merangkum kontribusi utama penelitian secara optimal. Bagian ini perlu ditulis ulang agar secara tegas, ringkas, dan jelas menyajikan temuan kunci serta implikasi kontribusi ilmiah yang dihasilkan.

---

### Jawaban Kuesioner Evaluasi Reviewer 1
- **Konfirmasi Penelaahan Berkas:** Ya, seluruh berkas telah ditelaah (*Yes, all files have been reviewed*).
- **1) Kontribusi terhadap Khazanah Keilmuan (*Contribute to the body of knowledge*):** **Ya (*Yes*)**.
- **2) Soliditas Teknis (*Technically sound*):** **Ya (*Yes*)**.
- **3) Penyajian yang Komprehensif (*Comprehensive manner*):** **Ya (*Yes*)**.
- **4) Kecukupan dan Kesesuaian Referensi (*References applicable and sufficient*):** **Ya (*Yes*)**.
- **5) Referensi yang Tidak Sesuai (*Inappropriate references*):** **Tidak ada (*No*)**.

---

## 👨‍🏫 Reviewer 2 (R2)

### Catatan Kritis
Reviewer 2 memberikan telaah metodologis dan statistik yang sangat mendalam, mencakup 10 aspek krusial terkait kebaruan, kebocoran data, reproduktibilitas, signifikansi statistik, batasan klaim keadilan algoritmik, serta efisiensi komputasi.

---

### Rincian 10 Komentar Reviewer 2

#### 1. Kebaruan dan Distingsi Kontribusi Metodologis (*Novelty and Contribution*)
- **Teks Asli:**  
  > *"1. Novelty and contribution: The methodological novelty beyond concatenating three pretrained feature representations and applying conventional classifiers should be more clearly established relative to existing dual-domain and multidomain approaches."*
- **Terjemahan & Penjelasan:**  
  Kebaruan metodologis dari penelitian ini harus ditetapkan dan ditegaskan secara lebih jelas jika dibandingkan dengan pendekatan *dual-domain* maupun *multi-domain* yang telah ada sebelumnya, agar tidak dipandang sekadar sebagai penggabungan sederhana (konkatenasi) tiga representasi fitur pra-latih yang kemudian diumpankan ke pengklasifikasi standar (*off-the-shelf*).

---

#### 2. Potensi Kebocoran Data dan Generalisasi Tingkat Identitas (*Data Leakage and Generalization*)
- **Teks Asli:**  
  > *"2. Data leakage and generalization: The image-level stratified split may allow images of the same identity to occur in both training and test sets. Please clarify whether identity overlap exists and provide subject-disjoint evaluation to establish genuine generalization."*
- **Terjemahan & Penjelasan:**  
  Pembagian data terstratifikasi pada tingkat citra (*image-level stratified split*) berpotensi memungkinkan citra dari identitas/subjek individu yang sama muncul di kedua subset (data latih dan data uji). Penulis diminta mengklarifikasi apakah terdapat tumpang tindih identitas (*identity overlap*) dan menyediakan evaluasi berbasis pemisahan identitas subjek (*subject-disjoint evaluation*) untuk membuktikan kemampuan generalisasi model yang sebenarnya.

---

#### 3. Spesifikasi Preprocessing dan Reproduktibilitas (*Preprocessing and Reproducibility*)
- **Teks Asli:**  
  > *"3. Preprocessing and reproducibility: Please specify the exact checkpoint versions, image processors, normalization parameters, and feature extraction procedures used for all three pretrained ViT models."*
- **Terjemahan & Penjelasan:**  
  Untuk menjamin keterulangan (*reproducibility*), penulis wajib mencantumkan secara eksplisit rincian teknis meliputi: versi *checkpoint* HuggingFace yang digunakan, pustaka/konfigurasi pemroses citra (*image processor*), parameter normalisasi (nilai *mean* dan *standard deviation* per *channel* warna), serta alur prosedur ekstraksi fitur token `[CLS]` pada ketiga model ViT pra-latih.

---

#### 4. Rekonsiliasi Konsistensi Ruang Pencarian Hyperparameter (*Hyperparameter Search Consistency*)
- **Teks Asli:**  
  > *"4. Hyperparameter search consistency: The reported totals of 1,086 configurations, 38,010 cross-validation fits, and 28 final refits should be reconciled with the individual search spaces reported in Tables 3–6."*
- **Terjemahan & Penjelasan:**  
  Jumlah keseluruhan yang dilaporkan dalam metodologi—yakni 1.086 kombinasi hyperparameter, 38.010 penyesuaian validasi silang (*cross-validation fits*), dan 28 model *refit* akhir—harus direkonsiliasi dan diselaraskan secara konsisten dengan rincian parameter individu yang tercantum pada tabel ruang pencarian masing-masing pengklasifikasi (Tabel 3 s.d. 6).

---

#### 5. Interpretasi Signifikansi Statistik Inferensial & Uji McNemar (*Statistical Interpretation*)
- **Teks Asli:**  
  > *"5. Statistical interpretation: The SVM accuracy improvement from 93.29% to 93.70% is not statistically significant according to the reported McNemar test (p = 0.3057). Consequently, claims of tri-domain superiority and feature saturation should be appropriately qualified."*
- **Terjemahan & Penjelasan:**  
  Kenaikan akurasi SVM dari 93,29% (pada *dual-domain* `Emotion ⊕ Face`) menjadi 93,70% (pada *tri-domain*) terbukti tidak signifikan secara statistik berdasarkan hasil Uji McNemar berpasangan ($p = 0,3057 > 0,05$). Konsekuensinya, klaim mengenai keunggulan mutlak *tri-domain* serta fenomena kejenuhan fitur (*feature saturation*) harus dikualifikasikan (diberikan batasan objektif yang tepat) di dalam teks.

---

#### 6. Batasan Ruang Lingkup Analisis Keadilan Algoritmik (*Fairness Analysis Scope*)
- **Teks Asli:**  
  > *"6. Fairness analysis: The reported Equal Opportunity Difference values provide useful subgroup information but do not establish comprehensive demographic fairness. Please clarify the scope and limitations of the fairness claims."*
- **Terjemahan & Penjelasan:**  
  Nilai *Equal Opportunity Difference* (EOD) yang dilaporkan memang memberikan informasi performa antar-subkelompok yang berharga, namun belum membuktikan tercapainya keadilan demografis secara utuh dan menyeluruh. Penulis diminta untuk memperjelas batasan dan ruang lingkup dari klaim keadilan algoritmik (*fairness*) tersebut.

---

#### 7. Kualifikasi Perbandingan dengan Metode Terdahulu (*Baseline Comparison*)
- **Teks Asli:**  
  > *"7. Baseline comparison: Please clarify whether the prior methods in Table 12 used comparable data partitions, preprocessing, and evaluation protocols. Otherwise, the comparison should be presented as contextual rather than a controlled benchmark."*
- **Terjemahan & Penjelasan:**  
  Penulis harus mengklarifikasi apakah metode-metode pembanding terdahulu pada Tabel 12 dievaluasi menggunakan partisi data, prapemrosesan, dan protokol evaluasi yang identik/sebanding. Jika terdapat perbedaan protokol, perbandingan tersebut wajib disajikan sebagai perbandingan kontekstual (*contextual comparison*), bukan sebagai tolok ukur terkontrol (*controlled benchmark*).

---

#### 8. Pelaporan Profil Efisiensi Komputasi (*Computational Efficiency Profiling*)
- **Teks Asli:**  
  > *"8. Computational efficiency: Please report feature extraction time, classifier training time, inference latency, memory consumption, and model storage requirements to substantiate the efficiency claims."*
- **Terjemahan & Penjelasan:**  
  Untuk membuktikan klaim efisiensi sistem, penulis harus menyajikan data kuantitatif komputasi yang mencakup: durasi waktu ekstraksi fitur per citra, waktu pelatihan pengklasifikasi, latensi inferensi saat pengujian, konsumsi memori utama (RAM/VRAM), serta ukuran penyimpanan model/fitur (*storage requirements*).

---

#### 9. Penguatan Bukti Interpretasi Fenotipik & Pola Kesalahan (*Results and Discussion*)
- **Teks Asli:**  
  > *"9. Results and discussion: Several interpretations concerning phenotypic overlap, the contribution of age-related features, and reductions in inter-racial errors remain insufficiently supported by confusion matrices alone. These statements should be qualified or supported by additional analyses."*
- **Terjemahan & Penjelasan:**  
  Sejumlah klaim interpretatif dalam pembahasan—seperti adanya tumpang tindih fenotipik (*phenotypic overlap*), kontribusi fitur usia dalam membedakan ras, serta penurunan kesalahan klasifikasi antar-ras—belum memiliki landasan pembuktian yang cukup kuat jika hanya bersumber dari matriks konfusi semata. Pernyataan-pernyataan ini harus dikualifikasikan (diperhalus bahasanya) atau diperkuat dengan analisis pendukung tambahan.

---

#### 10. Pembatasan Cakupan Kesimpulan dan Generalisasi (*Conclusion and Limitations*)
- **Teks Asli:**  
  > *"10. Conclusion and limitations: The conclusions should be restricted to the evaluated DemogPairs benchmark unless additional cross-identity or external-dataset validation is provided."*
- **Terjemahan & Penjelasan:**  
  Kesimpulan penelitian harus dibatasi secara tegas dan jujur hanya berlaku pada tolok ukur dataset DemogPairs yang dievaluasi (tiga ras makro: Asian, Black, White), kecuali apabila penulis menyajikan validasi eksperimental tambahan pada skenario lintas-identitas (*cross-identity*) atau dataset eksternal independen.

---

### Jawaban Kuesioner Evaluasi Reviewer 2
- **Konfirmasi Penelaahan Berkas:** Ya, seluruh berkas telah ditelaah (*Yes, all files have been reviewed*).
- **1) Kontribusi terhadap Khazanah Keilmuan (*Contribute to the body of knowledge*):** **Ya (*Yes*)**.
- **2) Soliditas Teknis (*Technically sound*):** **Ya (*Yes*)**.
- **3) Penyajian yang Komprehensif (*Comprehensive manner*):** **Ya (*Yes*)**.
- **4) Kecukupan dan Kesesuaian Referensi (*References applicable and sufficient*):** **Ya (*Yes*)**.
- **5) Referensi yang Tidak Sesuai (*Inappropriate references*):** **Tidak ada (*No*)**.

---

## 📊 Matriks Pemetaan Komentar ke Bagian Naskah & Rencana Tindak Lanjut

| Reviewer & No. | Kategori Isu Pokok | Bab Terkait pada Naskah | Rencana Aksi / Data Pendukung yang Tersedia di Repositori |
|:---:|---|---|---|
| **R1 - #1** | Panjang Pendahuluan | Section I (`01_introduction.md` / `.tex`) | Ringkas dan padatkan narasi pengantar; fokuskan pada urgensi interseksional dan kesenjangan riset. |
| **R1 - #2** | Studi Terkait & Rumus | Section II (`02_related-works.md` / `.tex`) | Restrukturisasi literatur secara tematik; sertakan formulasi matematis metode representasi terdahulu. |
| **R1 - #3** | Desain Ulang Figure 3 | Section III-B (`images/vit.png` & narasi) | Desain ulang diagram arsitektur ViT agar resolusi tinggi, memperlihatkan alur ekstraksi token `[CLS]` dan fusi multi-domain secara visual. |
| **R1 - #4** | Analisis Figure 4 | Section IV-D (`04_results-and-discussion_d-error-pattern-assessment.md`) | Perdalam analisis matriks konfusi 6×6, jelaskan dominasi kesalahan *same-gender cross-race* dan minimnya *gender confusion*. |
| **R1 - #5** | Detail Dataset & Waktu | Section III-A, IV-A | Rinci 600 subjek DemogPairs, seimbangkan tabel partisi, serta sajikan tabel profil durasi/biaya komputasi. |
| **R1 - #6** | Baseline Pembanding | Section IV-E (`04_results-and-discussion_e-comparison-with-prior-studies.md`) | Perluas komparasi dengan arsitektur lain dan model pada literatur atribut demografis wajah. |
| **R1 - #7** | Revisi Kesimpulan | Section V (`05_conclusion.md` / `.tex`) | Tulis ulang kesimpulan agar padat, fokus pada pencapaian 93,70%, dan tidak overclaim. |
| **R2 - #1** | Kebaruan Metodologi | Section I, III-0, III-G | Artikulasi distingsi sinergi multi-domain (biometrik statis + dinamika afektif + penuaan) dan pipeline GridSearchCV terisolasi. |
| **R2 - #2** | Data Leakage & Identitas | Section III-A (`03_materials-and-methods_a-dataset.md`) | Jelaskan sifat partisi citra DemogPairs, klarifikasi batasan identitas, dan bahas implikasi *subject-disjoint generalization*. |
| **R2 - #3** | Reproduktibilitas ViT | Section III-B (`03_materials-and-methods_b-vision-transformer.md`) | Cantumkan ID checkpoint HuggingFace (`skutaada/VIT-VGGFace`, `dima806/...`), resolusi 224×224, nilai mean/std normalisasi, dan rumus token `[CLS]`. |
| **R2 - #4** | Rekonsiliasi Search Space | Section III-G (`03_materials-and-methods_g-classification-pipeline.md`) | Selaraskan hitungan kombinasi (SVM: 288, LR: 270, RF: 288, GNB: 240 = 1.086 × 5 folds = 5.430 × 7 skema = 38.010 fits + 28 refits). |
| **R2 - #5** | Uji McNemar & Statistik | Section IV-A, IV-B, Batasan | Rujuk hasil `experiment/code/md/3.1_statistical_significance.md` ($p = 0,3057$); kualifikasikan klaim sebagai *asymptotic feature saturation*. |
| **R2 - #6** | Batasan Klaim Keadilan | Section IV-C (`04_results-and-discussion_c-intersectional-subgroup-performance.md`) | Klarifikasi bahwa metrik EOD ($\Delta\text{Recall} = 7,50\text{ pp}$) adalah audit performa subkelompok, bukan klaim keadilan algoritmik mutlak. |
| **R2 - #7** | Sifat Komparasi Baseline | Section IV-E (`04_results-and-discussion_e-comparison-with-prior-studies.md`) | Beri catatan kaki/penjelasan eksplisit bahwa studi di luar DemogPairs disajikan sebagai komparasi kontekstual, bukan *controlled benchmark*. |
| **R2 - #8** | Profil Efisiensi Komputasi | Section IV (Subseksi Baru) | Sajikan tabel efisiensi komputasi (waktu ekstraksi ~15 ms/citra, latensi inferensi pengklasifikasi, ukuran cache ~30 MB/domain). |
| **R2 - #9** | Koreksi Overclaim Fenotipik | Section IV-D | Perhalus narasi interpretasi fenotipik dan tekstur penuaan agar berbasis data empiris matriks konfusi tanpa spekulasi biologis berlebih. |
| **R2 - #10** | Batasan Kesimpulan & Ruang Lingkup | Section V (`05_conclusion.md`) | Batasi generalisasi secara eksplisit pada 3 ras makro DemogPairs dan cantumkan perlunya validasi dataset eksternal di masa depan. |
