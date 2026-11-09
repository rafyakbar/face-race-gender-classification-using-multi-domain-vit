# Surat Tanggapan Penulis atas Komentar Reviewer (Response to Reviewers)
**ID Manuskrip:** `Access-2026-50857`  
**Judul Artikel:** *Multi-Domain Vision Transformer Fusion for Intersectional Demographic Classification from Facial Images*  
**Target Jurnal:** IEEE Access (Open Access, Q1)  
**Associate Editor:** Dr. Vincenzo Conti (Università Kore di Enna, Italia)  
**Penulis:** Dr. Ir. Ricky Eka Putra (Penulis Korespondensi), Rezky Arisanti Putri, Dr. Yuni Yamasari, Rafy Aulia Akbar, dan Dr. Shukor Sanim Mohd Fauzi  
**Tanggal Pengajuan:** November 2026  

---

## Bagian I: Tanggapan kepada Associate Editor & Ikhtisar Revisi Utama

Kepada Yth. **Dr. Vincenzo Conti**,  
Associate Editor, IEEE Access,

Kami menyampaikan terima kasih yang sebesar-besarnya kepada Editor dan kedua Reviewer independen atas evaluasi yang sangat konstruktif, mendalam, dan terperinci terhadap manuskrip kami. Seluruh masukan dan telaah kritis dari para penelaah telah kami pelajari secara saksama. Berdasarkan arahan tersebut, kami telah melakukan restrukturisasi menyeluruh terhadap naskah, memperkuat fondasi teoretis, mengeksekusi evaluasi ulang di bawah protokol partisi tanpa kebocoran identitas (*Strict Subject-Disjoint Partitioning*), serta mengintegrasikan pengujian inferensial dan profil efisiensi komputasi terukur.

Berikut adalah ringkasan lima perbaikan metodologis dan empiris utama yang telah diterapkan pada naskah revisi:

1. **Resolusi Kebocoran Data melalui Tolok Ukur Utama *Subject-Disjoint* (Reviewer 2 #2 & Reviewer 1 #5):**  
   Untuk menjawab kekhawatiran kritis mengenai potensi tumpang tindih identitas (*identity overlap*), kami menetapkan protokol partisi **Strict Subject-Disjoint** pada 600 subjek independen dalam dataset DemogPairs. Melalui pemisahan berbasis identitas deterministik (rasio 80/20 dengan pengacakan terkontrol per subkelompok), sebanyak 480 subjek (8.640 citra; 80 subjek per kelas) dialokasikan khusus untuk data latih dan validasi silang 5-Fold *StratifiedGroupKFold* berbasis ID subjek, sedangkan 120 subjek independen lainnya (2.160 citra; 20 subjek per kelas) dijadikan himpunan uji terisolasi (*held-out test set*), menjamin **0,00% kebocoran identitas (*zero identity leakage*)**. Pada tolok ukur utama bebas kebocoran ini:
   - Model **Logistic Regression (LR) + Tri-Domain ViT** mencatat performa tertinggi dengan **Akurasi 88,66%**, Macro F1 **0,8868**, Interval Kepercayaan 95% Wilson **[87,25%, 89,93%]**, latensi inferensi hilir **0,0046 ms/sampel**, dan ukuran model **0,11 MB**.
   - Model **Support Vector Machine (SVM) + Tri-Domain ViT** meraih **Akurasi 88,61%** dan Macro F1 **0,8863**.
   - Hasil pengujian lama berbasis pemisahan acak tingkat citra (93,70% pada SVM dan 92,73% pada LR) tetap dipertahankan secara transparan sebagai **Studi Ablasi Kebocoran Data** pada Seksi IV-B (Tabel XII) untuk mengukur secara kuantitatif besaran penalti penghafalan identitas wajah (penurunan performa 5,09 percentage points pada SVM dan 4,07 percentage points pada LR).

2. **Pengujian Hipotesis Inferensial & Uji McNemar (Reviewer 2 #5):**  
   Kami menerapkan uji signifikansi statistik berpasangan McNemar dengan koreksi kontinuitas Edwards dan uji eksak binomial dua arah (*exact two-sided binomial test*) pada seluruh 2.160 sampel uji held-out (Tabel XIII). Fusi multi-domain ViT terbukti memberikan peningkatan performa yang signifikan secara statistik dibanding biometrik wajah domain tunggal (*p* < 0,001). Perbandingan antara model terbaik LR Tri-Domain (88,66%, 1.915 prediksi benar) dan SVM Tri-Domain (88,61%, 1.914 prediksi benar) menghasilkan nilai chi-square 0,0000 dan nilai *p* = 1,0000 (selisih diskordan hanya 1 citra), membuktikan **paritas prediktif (ketiadaan perbedaan signifikan dalam performa klasifikasi)**. Selain itu, kontribusi domain usia dikualifikasikan secara presisi: penambahan fitur usia di atas representasi emosi dan wajah memberikan peningkatan yang signifikan secara statistik pada model linier LR (*p* = 0,0073 < 0,01), sedangkan pada kernel non-linier RBF SVM terjadi **kejenuhan fitur asimtotik (*asymptotic feature saturation*)** (*p* = 0,7343 > 0,05). Karakteristik fusi ini juga dilaporkan bersifat bergantung pada algoritma (*classifier-dependent*) untuk Random Forest dan Gaussian Naive Bayes.

3. **Profil Efisiensi Komputasi Terukur (Reviewer 1 #5 & Reviewer 2 #8):**  
   Kami menyajikan tabel profil efisiensi komputasi terperinci (Seksi IV-A Paragraf 6, Tabel XI) yang diukur pada perangkat keras standar (Intel Core i9-13900H, RAM 32 GB DDR5, dan GPU NVIDIA GeForce RTX 4060 Laptop 8 GB VRAM):
   - Waktu ekstraksi fitur ViT secara *offline* pada GPU dengan *in-memory caching* membutuhkan **124,5 ms/citra** untuk fusi tri-domain (total 22,41 menit untuk 10.800 citra), mencatat **percepatan komputasi 11,9× lebih cepat** dibanding baseline CPU (~1.487 ms/citra; total 4,46 jam).
   - Durasi pelatihan *grid search* validasi silang pada 31.920 penyesuaian model (*fits*): LR Tri-Domain membutuhkan **54,8 menit**, sedangkan SVM Tri-Domain membutuhkan **511,1 menit** (pelatihan LR **9,3× lebih cepat**).
   - Latensi inferensi per sampel pengklasifikasi hilir: LR mencatat **0,0046 ms/sampel**, sedangkan SVM mencatat **4,6785 ms/sampel** (kepala pengklasifikasi hilir LR **>1.000× lebih cepat**).
   - Ukuran model pada penyimpanan: LR berukuran **0,11 MB**, sedangkan SVM berukuran **36,60 MB** (LR **>330× lebih ringkas**). Kami menegaskan secara jujur bahwa efisiensi tinggi ini berada pada kepala pengklasifikasi hilir, sedangkan implementasi menyeluruh pada perangkat *Edge AI* berdaya rendah membutuhkan kompresi atau kuantisasi backbone transformer di masa mendatang.

4. **Penyempurnaan Arsitektur, Rumus, dan Transparansi Reproduksibilitas (Reviewer 1 #2, #3 & Reviewer 2 #1, #3, #4):**  
   Gambar 3 telah didesain ulang menjadi diagram arsitektur beresolusi tinggi (300+ DPI, format vektor) yang memperlihatkan 7 tahapan alur sistem secara visual. Landasan teoretis naskah diperkuat melalui penyajian formulasi matematis formal (Persamaan 1 hingga 23) yang terdistribusi secara runtut pada Seksi II dan Seksi III. Spesifikasi versi checkpoint HuggingFace dicantumkan secara lengkap beserta parameter normalisasi seragam (nilai *mean* dan *std* [0.5, 0.5, 0.5] ke rentang [-1, 1] tanpa deteksi MTCNN tambahan). Selain itu, ruang pencarian hyperparameter telah direkonsiliasi secara konsisten: **912 kombinasi per skema fitur**, **4.560 fits per skema**, **31.920 fits validasi silang total**, dan **28 refits akhir** melintasi Tabel III hingga VI.

5. **Kalibrasi Batasan Klaim Keadilan & Ruang Lingkup Generalisasi (Reviewer 1 #1, #7 & Reviewer 2 #6, #7, #9, #10):**  
   Bagian Pendahuluan telah diringkas sekitar 28% agar terfokus langsung pada permasalahan klasifikasi interseksional. Metrik keadilan *Equal Opportunity Difference* (EOD = 9,72 percentage points pada Tabel XIV) dikualifikasikan secara objektif sebagai indikator disparitas performa empiris antar-subkelompok, bukan sebagai jaminan matematis keadilan universal. Tabel komparasi literatur (Tabel XV) dipisahkan menjadi Part A (*Perbandingan Kontekstual* untuk studi terdahulu dengan tumpang tindih identitas) dan Part B (*Tolok Ukur Terkontrol* untuk protokol subject-disjoint). Seluruh spekulasi kausal biologis maupun kontras pencahayaan dihapus dari pembahasan, dan kesimpulan dibatasi secara tegas pada 3 ras makro DemogPairs (Asian, Black, White).

---

## Bagian II: Tanggapan Butir-per-Butir terhadap Reviewer 1 (R1)

### Komentar R1-1: Pemadatan Bagian Pendahuluan (*Introduction*)
> *"1. the introduction is too long need to be summarized."*

**Tanggapan Penulis:**  
Kami sependapat dengan masukan Reviewer 1. Bagian Pendahuluan pada draf awal memuat pembahasan latar belakang disparitas demografis yang terlalu luas dan repetitif. Pada naskah revisi, Seksi I telah direstrukturisasi dan dipadatkan sekitar 28%. Alur narasi difokuskan langsung pada urgensi klasifikasi demografis interseksional (persilangan ras dan gender), keterbatasan representasi domain tunggal, serta manfaat komplementer dari penggabungan representasi afektif dan usia biologis. Selain itu, kontribusi ilmiah penelitian dirumuskan kembali menjadi empat butir pernyataan ilmiah yang ringkas, tegas, dan berbobot di akhir Seksi I.

**Tindakan pada Naskah:**  
- **Lokasi pada Naskah:** Seksi I (*Introduction*), Halaman 1–2.
- **Rincian Perubahan:** Paragraf 2 hingga 5 dipadatkan dengan mengeliminasi kalimat-kalimat umum yang berulang. Empat butir kontribusi utama disajikan secara eksplisit pada Halaman 2 Kolom 2.

---

### Komentar R1-2: Restrukturisasi Studi Terkait & Penambahan Persamaan Matematika
> *"2. The related works needs to be modified in better way and add equations."*

**Tanggapan Penulis:**  
Kami menyampaikan terima kasih atas saran yang sangat baik ini. Pada naskah revisi, Seksi II (*Related Works*) telah kami tata ulang menjadi tiga subseksi tematik yang runtut: *(A) Demographic Face Recognition*, *(B) Vision Transformers in Face Analysis*, dan *(C) Multi-Domain Feature Fusion*.  
Untuk memperkuat landasan teoretis tanpa membebani pembaca dengan rumus yang berlebihan, kami menambahkan perumusan matematis formal kunci yang merepresentasikan literatur sebelumnya:
1. Pemetaan fungsi keputusan kernel KELM non-linier pada literatur pengenalan etnisitas (Persamaan 1).
2. Proyeksi linier patch citra dan penambahan embedding spasial pada Vision Transformer (Persamaan 2).
3. Mekanisme atensi Multi-Head Self-Attention (MHSA) berskala (Persamaan 3).
4. Formulasi ruang representasi bersama melalui fusi konkatenasi fitur multi-domain (Persamaan 4).  
Setiap persamaan dilengkapi dengan penjelasan naratif mengenai definisi simbol variabelnya, dan subseksi II-C diakhiri dengan penegasan posisi kebaruan metodologis penelitian ini dibanding studi-studi terdahulu.

**Tindakan pada Naskah:**  
- **Lokasi pada Naskah:** Seksi II (*Related Works*), Subseksi II-A hingga II-C, Persamaan (1) hingga (4).
- **Rincian Perubahan:** Naskah ditata ulang secara tematik dengan menyertakan Persamaan (1)–(4) dan telaah perambatan bias representasi transformer.

---

### Komentar R1-3: Desain Ulang dan Penjelasan Gambar 3 (Diagram ViT)
> *"3. The figure 3 needs to be redesigned and explained in better way to show the novelty of the proposed method and also not clear."*

**Tanggapan Penulis:**  
Kami sepenuhnya setuju. Diagram pada naskah awal memiliki resolusi visual yang kurang optimal dan belum memvisualisasikan mekanisme ekstraksi paralel serta fusi representasi secara gamblang. Kami telah mendesain ulang Gambar 3 (`images/vit_v2.2.png`) secara profesional dalam format resolusi tinggi (300+ DPI). Diagram baru ini memetakan tujuh tahapan pemrosesan terpadu:
1. Standardisasi citra masukan RGB berukuran 224 × 224 piksel dan pemotongan menjadi 196 patch spasial berukuran 16 × 16 piksel.
2. Proyeksi linier patch ke dimensi laten 768 serta penambahan token kelas [CLS] dan embedding posisi.
3. Ekstraksi fitur paralel melalui tiga model Vision Transformer pra-latih yang dibekukan bobotnya (ViT-Face untuk biometrik, ViT-Emotion untuk dinamika ekspresi, dan ViT-Age untuk morfologi penuaan).
4. Pengambilan vektor representasi laten token [CLS] lapisan ke-12 dari masing-masing domain (3 × 768 dimensi).
5. Penggabungan representasi melalui operasi konkatenasi langsung menjadi vektor fusi Tri-Domain 2.304 dimensi.
6. Rantai pemrosesan modular terisolasi (penskalaan MinMaxScaler dan reduksi dimensi PCA).
7. Optimasi hyperparameter empat famili pengklasifikasi klasik (RF, GNB, LR, SVM) di bawah protokol 5-Fold StratifiedGroupKFold untuk klasifikasi 6-kelas interseksional.  
Penjelasan teks naratif pada Seksi III-B turut diperluas untuk mempertegas kebaruan kerangka kerja fusi fitur komplementer ini tanpa memerlukan proses pelatihan ulang (*fine-tuning*) yang mahal.

**Tindakan pada Naskah:**  
- **Lokasi pada Naskah:** Seksi III-B (*Vision Transformer Feature Extraction*), Gambar 3 dan Paragraf 1–3 (Persamaan (5)–(8)).
- **Rincian Perubahan:** Gambar 3 lama diganti dengan diagram vektor resolusi tinggi (`images/vit_v2.2.png`), disertai elaborasi sistematis alur komputasi setiap tahapan.

---

### Komentar R1-4: Pembahasan Mendalam Dinamika Kesalahan Gambar 4
> *"4. Graph in figure 4 needs to be discussed in better way."*

**Tanggapan Penulis:**  
Kami mengucapkan terima kasih atas masukan ini. Pada Seksi IV-D (*Error Pattern Assessment*), kami memperdalam telaah empiris terhadap matriks konfusi 6 × 6 pada model terbaik Logistic Regression melintasi 2.160 citra uji held-out (Gambar 4a Domain Tunggal Wajah, Gambar 4b Domain Ganda Emosi+Wajah, dan Gambar 4c Tri-Domain Wajah+Emosi+Usia). Alih-alih sekadar membaca akurasi diagonal, kami melakukan dekomposisi kuantitatif terhadap sebaran sel kesalahan non-diagonal:
1. **Penurunan Kesalahan Menyeluruh:** Total kesalahan klasifikasi menurun secara konsisten dari 294 citra (akurasi 86,39% pada domain tunggal) menjadi 271 citra (87,45% pada domain ganda) dan 245 citra (88,66% pada model tri-domain).
2. **Dominasi Kesalahan Intra-Gender Lintas-Ras:** Pada model tri-domain (245 kesalahan), mayoritas kesalahan merupakan kebingungan intra-gender lintas-ras (67,35% dari seluruh error; atau 7,64% dari total sampel uji), turun signifikan dari 212 error pada domain tunggal. Sementara itu, kesalahan lintas-gender hanya mencakup 80 citra (32,65% dari total error; atau 3,70% dari total sampel uji).
3. **Pola Kesalahan Spesifik Subkelompok:** Narasi menguraikan penurunan kesalahan nyata pada kelompok minoritas, seperti subkelompok wanita berkulit hitam (*Black Females*) yang mengalami penurunan kesalahan dari 73 citra pada domain tunggal menjadi 55 citra pada model tri-domain, dengan penjelasan berbasis data observasional tanpa membuat spekulasi fenotipik biologis yang tidak terverifikasi.

**Tindakan pada Naskah:**  
- **Lokasi pada Naskah:** Seksi IV-D (*Error Pattern Assessment*), Gambar 4(a)–(c) dan Paragraf 1–3.
- **Rincian Perubahan:** Ditambahkan analisis dekomposisi sel matriks konfusi secara kuantitatif yang membedah proporsi kesalahan intra-gender vs lintas-gender melintasi ketiga konfigurasi representasi.

---

### Komentar R1-5: Rincian Karakteristik Dataset, Kontribusi, dan Biaya Waktu (*Time Cost*)
> *"5. Experimental works need to mention the dataset used in more detail and show the contribution of your proposed method and also to consider the time cost in the evaluation."*

**Tanggapan Penulis:**  
Kami sangat mengapresiasi rekomendasi komprehensif ini dan telah menindaklanjutinya dalam tiga aspek:
1. **Spesifikasi Rinci Dataset:** Pada Seksi III-A (Tabel I dan Gambar 2), kami mendokumentasikan komposisi 600 subjek independen DemogPairs (18 citra per subjek, total 10.800 citra seimbang melintasi 6 subkelompok) serta memformalkan protokol pemisahan data 80/20 berbasis subjek (480 subjek latih / 8.640 citra dan 120 subjek uji held-out / 2.160 citra).
2. **Penegasan Kontribusi Metode:** Pada Seksi IV-A dan IV-B (Tabel VII hingga XIII), kami membuktikan kontribusi signifikan fusi tri-domain dibanding biometrik wajah tunggal (+2,27 percentage points pada LR dan +2,45 percentage points pada SVM, *p* < 0,001).
3. **Evaluasi Biaya Waktu & Efisiensi Komputasi:** Pada Seksi IV-A Paragraf 6, kami menambahkan **Tabel XI** yang memuat profil efisiensi komputasi terukur secara empiris:
   - Durasi ekstraksi fitur ViT pada GPU NVIDIA RTX 4060: **124,5 ms/citra** untuk tri-domain (total 22,41 menit untuk 10.800 citra), mencatat akselerasi **11,9× lebih cepat** dibanding CPU (~1.487 ms/citra; total 4,46 jam).
   - Durasi pelatihan *grid search* 5-fold CV: LR Tri-Domain membutuhkan **54,8 menit**, jauh lebih efisien dibanding SVM Tri-Domain yang membutuhkan **511,1 menit** (pelatihan LR **9,3× lebih cepat**).
   - Latensi inferensi per sampel pengklasifikasi hilir: LR mencatat **0,0046 ms**, sedangkan SVM membutuhkan **4,6785 ms** (kepala pengklasifikasi LR **>1.000× lebih cepat**).
   - Ukuran penyimpanan model: LR hanya membutuhkan **0,11 MB**, sedangkan SVM memerlukan **36,60 MB** (LR **>330× lebih ringkas**).

**Tindakan pada Naskah:**  
- **Lokasi pada Naskah:** Seksi III-A (*Dataset*), Tabel I; Seksi IV-A (*Global Performance*), Paragraf 6, Tabel XI.
- **Rincian Perubahan:** Karakteristik dataset diperinci secara terstruktur dan Tabel XI mengenai profil efisiensi komputasi kuantitatif diintegrasikan penuh.

---

### Komentar R1-6: Perluasan Metode Pembanding (*Baselines*)
> *"6. the authors need to compare their proposed method with more methods to validate their contribution."*

**Tanggapan Penulis:**  
Kami sependapat dengan Reviewer 1. Pada naskah revisi, perbandingan literatur pada **Seksi IV-E, Tabel XV** telah diperluas secara signifikan menjadi 12 entri komparasi yang dikelompokkan secara transparan ke dalam dua bagian:
1. **Part A: Perbandingan Kontekstual (Studi Terdahulu pada DemogPairs):** Membandingkan model terdahulu yang dievaluasi di bawah pembagian acak tingkat citra (Putri et al. *JIEET* 2025 fusi Wajah+Usia dengan XGBoost [89,07%], Putri et al. *IEEE ICVEE* 2025 fusi Emosi+Wajah dengan SVM [92,41%], dan baseline historis kami [93,70%]).
2. **Part B: Tolok Ukur Terkontrol (Protokol Subject-Disjoint 6-Kelas):** Membandingkan model usulan Tri-Domain LR (88,66%) dan SVM (88,61%) terhadap beragam baseline arsitektur transfer learning CNN (ResNet-50 [81,25%], VGG-16 [79,81%], MobileNetV2 [78,43%], EfficientNet-B0 [80,14%]) serta model ViT domain tunggal dan ganda yang seluruhnya dievaluasi pada 120 subjek uji held-out yang sama persis ($N = 2.160$).  
Hasil ini menegaskan keunggulan empiris model usulan atas arsitektur CNN konvensional maupun model domain tunggal.

**Tindakan pada Naskah:**  
- **Lokasi pada Naskah:** Seksi IV-E (*Comparison with Prior Studies*), Paragraf 1–3, Tabel XV.
- **Rincian Perubahan:** Tabel XV diperluas menjadi dua panel terpisah (Part A Kontekstual dan Part B Terkontrol) dengan anotasi protokol partisi yang jelas.

---

### Komentar R1-7: Penyempurnaan Bagian Kesimpulan (*Conclusion*)
> *"7. conclusion part does not show the contribution in good way."*

**Tanggapan Penulis:**  
Kami menyampaikan terima kasih atas telaah kritis ini. Bagian Kesimpulan (Seksi V) telah ditulis ulang sepenuhnya menjadi dua paragraf terstruktur yang menyajikan kontribusi ilmiah secara lugas dan berimbang:
1. Merangkum efektivitas fusi representasi multi-domain ViT (Wajah + Emosi + Usia) pada tolok ukur bebas kebocoran DemogPairs (LR 88,66% dan SVM 88,61%), dengan penegasan bahwa fusi fitur memberikan peningkatan akurasi yang signifikan secara statistik dibanding biometrik wajah tunggal (*p* < 0,001).
2. Menjelaskan temuan kunci paritas prediktif antara model linier Logistic Regression dan model non-linier RBF SVM (*p* = 1,0000), yang didukung oleh keunggulan komputasi pengklasifikasi hilir LR yang >1.000× lebih cepat dalam latensi inferensi dan >330× lebih ringkas dalam ukuran model.
3. Menyatakan secara transparan keterbatasan ruang lingkup penelitian (terbatas pada 3 ras makro DemogPairs dan beban komputasi ekstraksi ViT offline) serta menetapkan agenda riset lanjutan pada validasi dataset eksternal (FairFace, UTKFace) dan kompresi arsitektur transformer untuk komputasi Edge AI.

**Tindakan pada Naskah:**  
- **Lokasi pada Naskah:** Seksi V (*Conclusion*), Paragraf 1–2.
- **Rincian Perubahan:** Kesimpulan lama diganti dengan sintesis temuan empiris yang berbobot, objektif, dan memuat batas-batas penelitian yang jelas.

---

## Bagian III: Tanggapan Butir-per-Butir terhadap Reviewer 2 (R2)

### Komentar R2-1: Kebaruan Metodologis Melampaui Konkatenasi Sederhana
> *"1. Novelty and contribution: The methodological novelty beyond concatenating three pretrained feature representations and applying conventional classifiers should be more clearly established relative to existing dual-domain and multidomain approaches."*

**Tanggapan Penulis:**  
Kami berterima kasih kepada Reviewer 2 atas perhatian mendalam terhadap aspek kebaruan metodologis. Kami telah merevisi narasi pada Seksi I dan Seksi III untuk mengartikulasikan kebaruan tingkat kerangka kerja (*framework-level novelty*) penelitian ini:
1. **Sinergi Representasi Laten Multi-Domain Ortogonal:** Berbeda dari pendekatan konvensional yang mengandalkan biometrik wajah tunggal atau model *end-to-end multi-task* (yang rentan terhadap interferensi gradien negatif antara tugas identitas dan atribut), pendekatan ekstraksi representasi beku ini memadukan tiga ruang laten ortogonal yang saling melengkapi: geometri kraniofasial biometrik statis (`ViT-Face`), dinamika afektif ekspresi emosi (`ViT-Emotion`), dan morfologi penuaan biologis (`ViT-Age`).
2. **Investigasi Sistematis 28 Model & Protokol Terisolasi:** Kami menyajikan eksplorasi komparatif komprehensif melintasi empat famili pengklasifikasi (linier, kernel non-linier, *ensemble tree*, dan probabilistik) di bawah validasi silang 5-Fold StratifiedGroupKFold GridSearchCV yang terisolasi penuh (total 31.920 fits CV), membuktikan secara empiris bahwa pemisahan linier ter-regularisasi $L_2$ (LR) mampu menyamai batas keputusan kernel RBF non-linier berdimensi tinggi (*p* = 1,0000).
3. **Karakterisasi Empiris Fenomena Kejenuhan Fitur & Penalti Identitas:** Kami menyajikan analisis signifikansi inferensial formal yang mengidentifikasi terjadinya kejenuhan fitur asimtotik pada penambahan fitur usia terhadap model kernel RBF, serta studi ablasi kuantitatif kebocoran data yang memetakan disparitas performa akibat penghafalan identitas.

**Tindakan pada Naskah:**  
- **Lokasi pada Naskah:** Seksi I, Paragraf 5–6; Seksi III (Overview); Seksi III-G.
- **Rincian Perubahan:** Penegasan kebaruan konseptual sinergi representasi multi-domain dan protokol validasi terisolasi diuraikan secara tegas pada teks naskah.

---

### Komentar R2-2: Kebocoran Data dan Evaluasi *Subject-Disjoint* (Komentar Kritis)
> *"2. Data leakage and generalization: The image-level stratified split may allow images of the same identity to occur in both training and test sets. Please clarify whether identity overlap exists and provide subject-disjoint evaluation to establish genuine generalization."*

**Tanggapan Penulis:**  
Reviewer 2 telah mengangkat isu metodologis yang sangat fundamental dan krusial bagi integritas ilmiah penelitian ini. Kami mengakui secara terbuka bahwa eksperimen pada draf awal naskah menggunakan pembagian terstratifikasi pada tingkat citra (*image-level split*), yang setelah kami audit ulang ternyata menimbulkan tumpang tindih identitas (593 dari 600 subjek unik memiliki citra yang tersebar di himpunan latih dan uji).

Untuk menyelesaikan permasalahan ini secara definitif dan tuntas, kami merestrukturisasi seluruh kerangka eksperimen ke dalam **Dual-Benchmark Framework**:
1. **Tolok Ukur Utama (Strict Subject-Disjoint Partitioning, 0% Kebocoran Identitas):**  
   Melalui pembagian berbasis ID subjek yang deterministik (rasio 80/20 per subkelompok), kami mengisolasi 600 subjek DemogPairs menjadi **480 subjek latih** (8.640 citra) dan **120 subjek uji held-out** (2.160 citra, Tabel I). Penalaan hyperparameter pada data latih strictly menggunakan 5-Fold *StratifiedGroupKFold* berbasis `groups = subject_id`. Tidak ada satu pun identitas subjek uji yang pernah dilihat oleh model selama proses pelatihan, penskalaan, PCA, maupun validasi silang (**0,00% kebocoran data identitas**). Di bawah tolok ukur utama ini, Logistic Regression Tri-Domain mencapai akurasi **88,66%**, SVM Tri-Domain meraih **88,61%**, Random Forest meraih **85,00%**, dan Gaussian Naive Bayes meraih **84,31%** pada domain ganda Emosi+Wajah (83,61% pada tri-domain).
2. **Baseline Historis (Studi Ablasi Kebocoran Data):**  
   Hasil eksperimen lama berbasis pemisahan citra (93,70% pada SVM dan 92,73% pada LR) tidak kami buang, melainkan kami sajikan secara transparan pada Seksi IV-B (**Tabel XII**) sebagai **Studi Ablasi Kebocoran Data** untuk mengukur besaran efek penghafalan identitas (*facial identity memorization penalty*), yang terbukti mendongkrak performa semu sebesar 5,09 percentage points pada SVM dan 4,07 percentage points pada LR.

**Tindakan pada Naskah:**  
- **Lokasi pada Naskah:** Abstrak; Seksi III-A (*Dataset*), Paragraf 2, Tabel I; Seksi III-G; Seksi IV-A, Tabel VII–X; Seksi IV-B, Paragraf 2, Tabel XII.
- **Rincian Perubahan:** Seluruh tabel hasil utama (Tabel VII–X) diperbarui menggunakan tolok ukur bebas kebocoran *Subject-Disjoint*, disertai tabel khusus studi ablasi kebocoran data (Tabel XII).

---

### Komentar R2-3: Spesifikasi Prapemrosesan dan Reproduktibilitas ViT
> *"3. Preprocessing and reproducibility: Please specify the exact checkpoint versions, image processors, normalization parameters, and feature extraction procedures used for all three pretrained ViT models."*

**Tanggapan Penulis:**  
Kami sepenuhnya setuju dengan tuntutan reproduktibilitas ini. Pada Seksi III-A Paragraf 2 dan Seksi III-B Paragraf 2–3, kami telah mendokumentasikan spesifikasi teknis prapemrosesan dan ekstraksi fitur yang diverifikasi langsung dari kode implementasi repositori:
- **ViT-Face:** Checkpoint HuggingFace `skutaada/VIT-VGGFace` (versi commit SHA: `e85f0c9`, arsitektur ViT-Base/16 yang di-*fine-tune* pada VGGFace2).
- **ViT-Emotion:** Checkpoint HuggingFace `dima806/facial_emotions_image_detection` (versi commit SHA: `747cf16`, arsitektur ViT-Base/16 yang di-*fine-tune* pada FER-2013).
- **ViT-Age:** Checkpoint HuggingFace `dima806/facial_age_image_detection` (versi commit SHA: `ad35933`, arsitektur ViT-Base/16 yang di-*fine-tune* pada UTKFace dan IMDB-WIKI).
- **Prapemrosesan & Normalisasi Standar:** Citra DemogPairs telah dipotong berpusat pada wajah dari sumber aslinya, sehingga tidak ada deteksi atau penyelarasan wajah MTCNN tambahan yang diterapkan. Citra dikonversi ke RGB 3-kanal, diubah ukurannya menggunakan interpolasi bilinear menjadi 224 × 224 piksel melalui `AutoImageProcessor` masing-masing model, diskalakan ke rentang [0, 1], dan dinormalisasi per kanal warna menggunakan **rata-rata seragam $\mu = [0.5, 0.5, 0.5]$ dan deviasi standar $\sigma = [0.5, 0.5, 0.5]$** ke rentang [-1, 1] melintasi ketiga model.
- **Prosedur Ekstraksi Token [CLS]:** Tensor teranormalisasi diumpankan ke encoder 12-lapisan ViT-Base dalam mode inferensi beku (`torch.no_grad()`), dan representasi 768 dimensi diekstrak dari output LayerNorm akhir token [CLS] (`last_hidden_state[:, 0, :]`, Persamaan 7). Seluruh konfigurasi ablasi fitur diringkas pada **Tabel II**.

**Tindakan pada Naskah:**  
- **Lokasi pada Naskah:** Seksi III-A, Paragraf 2; Seksi III-B, Paragraf 2–3, Persamaan (7), Tabel II.
- **Rincian Perubahan:** Nama checkpoint HuggingFace, versi git commit, parameter normalisasi seragam, dan alur ekstraksi token [CLS] didokumentasikan secara presisi.

---

### Komentar R2-4: Rekonsiliasi Konsistensi Ruang Pencarian Hyperparameter
> *"4. Hyperparameter search consistency: The reported totals of 1,086 configurations, 38,010 cross-validation fits, and 28 final refits should be reconciled with the individual search spaces reported in Tables 3–6."*

**Tanggapan Penulis:**  
Kami menyampaikan terima kasih yang mendalam kepada Reviewer 2 atas ketelitian audit aritmatika ini. Setelah memeriksa kode eksekusi aktual (`experiment/code/md/`), kami menemukan bahwa draf awal salah mencatat kombinasi Logistic Regression dengan menghitung parameter yang sebenarnya tidak dievaluasi. Pada naskah revisi (Seksi III-C hingga III-G, **Tabel III–VI**), seluruh ruang pencarian parameter telah direkonsiliasi secara transparan dan tepat:
- **Random Forest (Tabel III):** 2 opsi scaler × 3 opsi PCA × 2 n_estimators ({100, 200}) × 3 max_depth ({None, 20, 30}) × 2 max_features ({'sqrt', 'log2'}) × 2 min_samples_split ({2, 5}) × 2 min_samples_leaf ({1, 2}) = **288 kombinasi** (1.440 fits per skema fitur).
- **Gaussian Naive Bayes (Tabel IV):** 2 opsi scaler × 3 opsi PCA × 40 nilai var_smoothing logaritmik ($1.0 \times 10^{-9}$ hingga $1.0 \times 10^{2}$) = **240 kombinasi** (1.200 fits per skema fitur).
- **Logistic Regression (Tabel V):** 2 opsi scaler × 3 opsi PCA × 4 nilai kekuatan regularisasi $C$ ({0.01, 0.1, 1, 10}) × 2 solver ({'lbfgs', 'saga'}) × 2 max_iter ({500, 1000}) = **96 kombinasi** (480 fits per skema fitur).
- **Support Vector Machine (Tabel VI):** Grid evaluasi Cartesian scikit-learn penuh dari 2 opsi scaler × 3 opsi PCA × 4 nilai penalti $C$ ({0.01, 0.1, 1, 10}) × 3 fungsi kernel ({'linear', 'rbf', 'poly'}) × 2 koefisien gamma ({'scale', 'auto'}) × 2 derajat polinomial ({2, 3}) = **288 evaluasi Cartesian** (1.440 fits per skema fitur). Kami mencantumkan catatan penjelas pada Tabel VI bahwa 288 evaluasi Cartesian ini setara dengan **108 konfigurasi unik efektif** secara fungsional (karena parameter derajat hanya aktif pada kernel polinomial dan gamma tidak berpengaruh pada kernel linier).
- **Total Kombinasi per Skema Fitur:** 288 + 240 + 96 + 288 = **912 kombinasi** (× 5 folds = **4.560 fits per skema fitur**).
- **Total Validasi Silang melintasi 7 Skema Fitur:** 4.560 × 7 = **31.920 fits validasi silang total**.
- **Refits Akhir:** 4 algoritma × 7 skema fitur = **28 refits akhir** pada keseluruhan 480 subjek data latih.

**Tindakan pada Naskah:**  
- **Lokasi pada Naskah:** Seksi I, Paragraf 5; Seksi III-C hingga III-F, Tabel III–VI; Seksi III-G, Paragraf 1.
- **Rincian Perubahan:** Tabel V diselaraskan menjadi 96 kombinasi, Tabel VI dilengkapi penjelasan 108 konfigurasi unik efektif, dan angka global diperbarui menjadi 912 kombinasi per skema fitur dan 31.920 fits validasi silang total.

---

### Komentar R2-5: Signifikansi Statistik & Uji Inferensial McNemar
> *"5. Statistical interpretation: The SVM accuracy improvement from 93.29% to 93.70% is not statistically significant according to the reported McNemar test (p = 0.3057). Consequently, claims of tri-domain superiority and feature saturation should be appropriately qualified."*

**Tanggapan Penulis:**  
Kami sepenuhnya sepakat dengan ketegasan Reviewer 2 mengenai perlunya kualifikasi inferensial yang tepat. Pada naskah revisi (Seksi IV-A dan IV-B, **Tabel XIII**), kami menyajikan hasil evaluasi pengujian hipotesis berpasangan McNemar dengan koreksi kontinuitas Edwards, uji eksak binomial dua arah, serta Interval Kepercayaan 95% Wilson Score melintasi 2.160 sampel uji held-out:
1. **Tri-Domain vs Domain Tunggal (Biometrik Wajah):** Peningkatan performa terbukti signifikan secara statistik pada kedua model terbaik: SVM Tri-Domain (88,61%) vs Single Face (86,16%) menghasilkan peningkatan +2,45 percentage points (+53 citra bersih, *p* < 0,001), dan LR Tri-Domain (88,66%) vs Single Face (86,39%) menghasilkan peningkatan +2,27 percentage points (+49 citra bersih, *p* < 0,001).
2. **Kualifikasi Kejenuhan Fitur Domain Usia (Tri-Domain vs Dual-Domain):**
   - Pada model non-linier RBF SVM, penambahan domain usia di atas fusi Emosi+Wajah (88,43% menjadi 88,61%) hanya menghasilkan selisih marjinal +0,19 percentage points (+4 citra bersih, *p* = 0,7343 > 0,05). Kami menyatakan secara terbuka dan objektif bahwa fenomena ini mencerminkan **kejenuhan fitur asimtotik (*asymptotic feature saturation*)** pada kernel RBF non-linier ketika informasi penuaan digabungkan dengan representasi afektif dan biometrik (meskipun dibanding model Wajah+Usia pada 87,55%, peningkatan ke Tri-Domain SVM tetap signifikan pada +1,06 percentage points, *p* = 0,0086 < 0,01).
   - Sebaliknya, pada model linier Logistic Regression, penambahan domain usia di atas Emosi+Wajah (87,45% menjadi 88,66%) menghasilkan peningkatan +1,20 percentage points (+26 citra bersih) yang terbukti signifikan secara statistik (*p* = 0,0073 < 0,01), membuktikan manfaat diskriminatif fitur penuaan bagi pembentukan bidang pemisah linier.
   - Kami juga melaporkan bahwa sifat fusi bergantung pada famili algoritma (*classifier-dependent*): Random Forest hanya mencatat kenaikan non-signifikan +0,14 percentage points (85,00% vs 84,86%, *p* = 0,8408), sementara Gaussian Naive Bayes justru mencapai puncak performanya pada domain ganda Emosi+Wajah (84,31% vs 83,61% pada tri-domain, *p* = 0,2349).
3. **Paritas Prediktif LR vs SVM:** Uji McNemar berpasangan antara LR Tri-Domain (88,66%, 1.915 benar) dan SVM Tri-Domain (88,61%, 1.914 benar) menghasilkan nilai *p* = 1,0000 (selisih diskordan 36 vs 35 citra, net +1 citra). Karena uji McNemar menguji hipotesis nol kesamaan tingkat kesalahan marginal, kami membingkai hasil ini secara hati-hati sebagai **ketiadaan perbedaan signifikan dalam performa prediktif (paritas prediktif)**, yang menjadi justifikasi ilmiah kuat untuk memilih LR atas keunggulan efisiensi komputasi hilirnya.

**Tindakan pada Naskah:**  
- **Lokasi pada Naskah:** Abstrak; Seksi I, Paragraf 6; Seksi IV-A, Paragraf 3–5; Seksi IV-B, Paragraf 1 & 3, Tabel XIII; Seksi V, Paragraf 1.
- **Rincian Perubahan:** Tabel XIII diintegrasikan untuk melaporkan pasangan sel diskordan, statistik chi-square Edwards, dan nilai *p* binomial eksak. Seluruh klaim kejenuhan fitur dan kesetaraan statistik telah dikualifikasikan secara ketat di seluruh bab.

---

### Komentar R2-6: Batasan Ruang Lingkup Analisis Keadilan Algoritmik
> *"6. Fairness analysis: The reported Equal Opportunity Difference values provide useful subgroup information but do not establish comprehensive demographic fairness. Please clarify the scope and limitations of the fairness claims."*

**Tanggapan Penulis:**  
Kami menyampaikan apresiasi dan terima kasih yang mendalam kepada Reviewer 2 atas koreksi etis dan metodologis yang sangat penting ini. Kami telah merevisi Seksi IV-C (*Intersectional Subgroup Performance*, **Tabel XIV**) dan Seksi V (*Conclusion*) untuk mendelimitasi batas analisis keadilan algoritmik secara transparan:
1. Kami melaporkan metrik Presisi, Recall (TPR), F1-Score, dan Akurasi One-vs-Rest (OvR) per subkelompok pada Tabel XIV, di mana nilai *Equal Opportunity Difference* (EOD = 9,72 percentage points antara *White Males* pada TPR 94,44% dan *Black Females* pada TPR 84,72%) disajikan murni sebagai alat ukur disparitas tingkat pengenalan empiris pada subset uji yang dievaluasi ($N = 2.160$).
2. Kami menyatakan secara eksplisit di dalam teks naskah bahwa nilai EOD dan metrik OvR (dengan rasio ketidakseimbangan kelas 5:1 pada skema OvR biner 6-kelas) **tidak dapat disamakan dengan sertifikasi keadilan demografis komprehensif atau jaminan keadilan universal**, yang sejatinya menuntut evaluasi multidimensi mencakup *demographic parity*, *equalized odds*, kalibrasi probabilitas, dan *counterfactual fairness* pada populasi sosio-kultural terbuka.

**Tindakan pada Naskah:**  
- **Lokasi pada Naskah:** Seksi III-H (*Evaluation Metrics*); Seksi IV-C (*Intersectional Subgroup Performance*), Paragraf 1–2, Tabel XIV; Seksi V, Paragraf 2.
- **Rincian Perubahan:** Narasi Seksi IV-C dan batasan pada Seksi V diperjelas untuk memposisikan metrik EOD strictly sebagai evaluasi disparitas performa empiris, bukan klaim keadilan algoritmik mutlak.

---

### Komentar R2-7: Kualifikasi Sifat Perbandingan dengan Metode Terdahulu
> *"7. Baseline comparison: Please clarify whether the prior methods in Table 12 used comparable data partitions, preprocessing, and evaluation protocols. Otherwise, the comparison should be presented as contextual rather than a controlled benchmark."*

**Tanggapan Penulis:**  
Kami sependapat dengan distingsi ilmiah yang diajukan oleh Reviewer 2. Pada Seksi IV-E (*Comparison with Prior Studies*), perbandingan literatur telah kami restrukturisasi menjadi **Tabel XV** dengan dua panel yang terpisah secara tegas:
1. **Part A: Perbandingan Kontekstual (*Contextual Comparison*):** Memuat publikasi DemogPairs terdahulu (Putri et al. *JIEET* 2025 pada 89,07% dan Putri et al. *ICVEE* 2025 pada 92,41%) serta baseline historis kami (93,70%), dengan penjelasan eksplisit bahwa studi-studi tersebut menggunakan pembagian acak tingkat citra dengan tumpang tindih identitas (*subject-overlap*), sehingga perbandingan ini disajikan semata-mata sebagai rujukan kontekstual historis.
2. **Part B: Tolok Ukur Terkontrol (*Controlled Benchmark*):** Menyajikan perbandingan terkontrol secara ketat antara model usulan Tri-Domain LR (88,66%) dan SVM (88,61%) melawan baseline transfer learning CNN (ResNet-50, VGG-16, MobileNetV2, EfficientNet-B0) dan model ViT domain tunggal/ganda yang seluruhnya dievaluasi pada partisi data *subject-disjoint* yang identik (480 subjek latih dan 120 subjek uji held-out).

**Tindakan pada Naskah:**  
- **Lokasi pada Naskah:** Seksi IV-E (*Comparison with Prior Studies*), Paragraf 1–3, Tabel XV.
- **Rincian Perubahan:** Tabel XV dipisahkan menjadi dua bagian (Part A Kontekstual dan Part B Terkontrol) dengan catatan pembeda protokol yang transparan di dalam teks dan keterangan tabel.

---

### Komentar R2-8: Pelaporan Profil Efisiensi Komputasi Lengkap
> *"8. Computational efficiency: Please report feature extraction time, classifier training time, inference latency, memory consumption, and model storage requirements to substantiate the efficiency claims."*

**Tanggapan Penulis:**  
Kami berterima kasih atas dorongan pengujian praktis ini. Pada Seksi IV-A Paragraf 6, kami telah menambahkan **Tabel XI** (*Computational Efficiency and Resource Consumption Profile*) yang melaporkan kelima dimensi komputasi yang diukur pada spesifikasi perangkat keras standar (**CPU Intel Core i9-13900H, RAM 32 GB DDR5, dan GPU NVIDIA GeForce RTX 4060 Laptop 8 GB VRAM**):
1. **Durasi Waktu Ekstraksi Fitur ViT (10.800 citra):** Pada GPU NVIDIA RTX 4060 dengan *in-memory processor caching*, ekstraksi membutuhkan **39,7 ms/citra** (`ViT-Face`), **39,7 ms/citra** (`ViT-Emotion`), dan **45,1 ms/citra** (`ViT-Age`), dengan total **124,5 ms/citra** (total **22,41 menit** untuk ketiga domain), mencatat percepatan **11,9× lebih cepat** dibanding baseline CPU (~1.487 ms/citra; total 4,46 jam).
2. **Waktu Pelatihan Pengklasifikasi (Grid Search 5-Fold CV pada CPU):** Logistic Regression Tri-Domain membutuhkan **54,8 menit** (3.287,07 detik); SVM Tri-Domain membutuhkan **511,1 menit** (30.666,02 detik; LR **9,3× lebih cepat dilatih**); Random Forest Tri-Domain membutuhkan **110,5 menit**; dan GNB Dual-Domain membutuhkan **25,5 menit**.
3. **Latensi Inferensi Pengklasifikasi Hilir per Sampel:** Logistic Regression Tri-Domain mencatat **0,0046 ms/sampel**; SVM Tri-Domain mencatat **4,6785 ms/sampel** (kepala pengklasifikasi hilir LR **>1.000× [1.027×] lebih cepat**); Random Forest Tri-Domain mencatat **0,0334 ms**; dan GNB Dual-Domain mencatat **0,0088 ms**. Jika memperhitungkan durasi ekstraksi fitur ViT pada GPU (124,5 ms), total latensi ujung-ke-ujung (*end-to-end GPU latency*) adalah sekitar **124,505 ms/citra untuk LR** dibanding **129,179 ms/citra untuk SVM**.
4. **Ukuran Penyimpanan Model di Disk:** Logistic Regression Tri-Domain hanya berukuran **0,11 MB**, sedangkan SVM Tri-Domain berukuran **36,60 MB** (LR **>330× lebih ringkas**); Random Forest berukuran **6,19 MB**; dan GNB berukuran **0,78 MB**.
5. **Konsumsi Memori RAM & Cache Fitur:** Array fitur data uji held-out ($N = 2.160$, format `float32`) mengonsumsi **18,98 MB RAM** untuk tri-domain dan **12,66 MB RAM** untuk dual-domain. Berkas cache fitur biner di disk menempati **30,8 MB per domain** (total **92,4 MB** untuk tri-domain).  
Kami menegaskan secara objektif pada Seksi IV-A Paragraf 6 dan Seksi V bahwa efisiensi tinggi LR (`0,11 MB`, `0,0046 ms`) berlaku pada **kepala pengklasifikasi hilir (*downstream head*)**, sedangkan deployment menyeluruh pada perangkat *low-power Edge AI* di masa depan membutuhkan kompresi atau kuantisasi backbone transformer.

**Tindakan pada Naskah:**  
- **Lokasi pada Naskah:** Seksi III-I (*Experimental Setup*); Seksi IV-A (*Global Performance*), Paragraf 6, Tabel XI; Seksi V, Paragraf 1–2.
- **Rincian Perubahan:** Tabel XI terintegrasi penuh memuat rincian kuantitatif kelima metrik efisiensi, disertai kualifikasi pembeda antara kepala pengklasifikasi hilir dan pemrosesan ujung-ke-ujung.

---

### Komentar R2-9: Landasan Empiris Pola Kesalahan Fenotipik
> *"9. Results and discussion: Several interpretations concerning phenotypic overlap, the contribution of age-related features, and reductions in inter-racial errors remain insufficiently supported by confusion matrices alone. These statements should be qualified or supported by additional analyses."*

**Tanggapan Penulis:**  
Kami menerima kritik ini dengan penuh keterbukaan ilmiah. Pada Abstrak, Seksi IV-C (*Intersectional Subgroup Performance*), dan Seksi IV-D (*Error Pattern Assessment*), kami telah menghapus seluruh klaim interpretatif spekulatif mengenai morfologi kraniofasial, tekstur kerutan epidermis, maupun pengaruh kontras pencahayaan:
1. Seluruh analisis pola kesalahan antarsubkelompok kini didasarkan murni pada distribusi frekuensi observasional matriks konfusi 6 × 6 melintasi 2.160 sampel uji held-out (misalnya melaporkan bahwa pada model LR Tri-Domain, dari 55 kesalahan pada subkelompok wanita berkulit hitam, 37 kesalahan terjadi secara intra-gender ke wanita kulit putih [23 citra] dan wanita Asia [14 citra]).
2. Kontribusi domain usia pada model Logistic Regression dijelaskan secara terukur melalui penurunan riil kesalahan intra-gender lintas-ras (turun dari 185 kesalahan pada model Emosi+Wajah menjadi 165 kesalahan pada Tri-Domain) serta didukung oleh signifikansi statistik uji McNemar (*p* = 0,0073), bukan melalui asumsi biologis spekulatif.

**Tindakan pada Naskah:**  
- **Lokasi pada Naskah:** Abstrak; Seksi IV-C, Paragraf 2; Seksi IV-D, Paragraf 2–3.
- **Rincian Perubahan:** Seluruh pernyataan spekulatif fenotipik dan pencahayaan dieliminasi; pembahasan ditopang murni oleh frekuensi matriks konfusi empiris dan uji hipotesis berpasangan.

---

### Komentar R2-10: Pembatasan Ruang Lingkup Kesimpulan & Generalisasi
> *"10. Conclusion and limitations: The conclusions should be restricted to the evaluated DemogPairs benchmark unless additional cross-identity or external-dataset validation is provided."*

**Tanggapan Penulis:**  
Kami sepenuhnya sependapat dengan Reviewer 2. Pada **Abstrak** dan **Seksi V (*Conclusion*, Paragraf 1–2)**, kami telah membatasi ruang lingkup kesimpulan penelitian secara eksplisit hanya berlaku pada 6 subkelompok interseksional yang mencakup **3 kategori ras makro (Asian, Black, White)** dalam tolok ukur DemogPairs *subject-disjoint*.  
Selain itu, pada Seksi V Paragraf 2, kami menyajikan paragraf khusus mengenai keterbatasan penelitian yang menegaskan bahwa generalisasi model pada populasi multirasial yang lebih luas (seperti komunitas Hispanik, Timur Tengah, Asia Selatan, atau kelompok Pribumi) serta kondisi akuisisi liar (*in-the-wild*) memerlukan validasi eksperimental lanjutan pada dataset eksternal independen seperti FairFace dan UTKFace.

**Tindakan pada Naskah:**  
- **Lokasi pada Naskah:** Abstrak; Seksi V (*Conclusion*), Paragraf 1–2.
- **Rincian Perubahan:** Klaim generalisasi dibatasi secara eksplisit pada 3 ras makro DemogPairs pada Abstrak dan Kesimpulan, dengan validasi lintas-dataset ditetapkan sebagai arah penelitian masa depan.

---

## Bagian IV: Matriks Verifikasi Kelengkapan Dokumen Resubmission

Sesuai dengan ketentuan resmi IEEE Access, seluruh dokumen pendukung resubmission telah dipersiapkan dan diverifikasi kelengkapannya:

| Butir Berkas Kelengkapan | Status Verifikasi | Rincian Dokumen |
|:---|:---:|:---|
| **Author Response File** | **Lengkap & Terverifikasi** | Dokumen tanggapan rinci butir-per-butir (dokumen ini) yang membedah seluruh komentar AE, Reviewer 1, dan Reviewer 2 dengan struktur Komentar $\to$ Tanggapan $\to$ Tindakan pada Naskah. |
| **Highlighted PDF** | **Lengkap & Terverifikasi** | Berkas PDF naskah revisi dengan penandaan warna kuning pada seluruh pembaruan teks naratif, persamaan, angka tabel, dan referensi baru. |
| **Main Manuscript (Clean PDF & TeX)** | **Lengkap & Terverifikasi** | Naskah final bersih dua kolom standar IEEE Access dalam format PDF dan berkas sumber LaTeX lengkap siap kompilasi. |
| **Request for Byline Change** | **Lengkap & Terverifikasi** | Formulir resmi bertandatangan seluruh penulis untuk penambahan rekan penulis Dr. Shukor Sanim Mohd Fauzi (Universiti Teknologi MARA) dengan justifikasi kontribusi ilmiah formal. |
| **Resubmission Checklist** | **Lengkap & Terverifikasi** | Verifikasi kepatuhan 10 butir mutu naskah IEEE Access (tata bahasa, format matematika, sitasi acuan, format tabel booktabs, dan resolusi gambar). |

Kami meyakini bahwa revisi menyeluruh, evaluasi ketat di bawah protokol *Strict Subject-Disjoint*, validasi signifikansi inferensial, profil efisiensi komputasi terukur, serta kalibrasi klaim ilmiah yang kami lakukan telah menjawab seluruh pertanyaan penelaah secara tuntas dan meningkatkan kualitas naskah sesuai standar publikasi jurnal internasional bereputasi tinggi *IEEE Access*.

Hormat kami,

**Dr. Ir. Ricky Eka Putra, S.Kom., M.Kom.** (Penulis Korespondensi)  
Departemen Teknik Informatika, Fakultas Ilmu Komputer  
Universitas Negeri Surabaya (UNESA), Surabaya, Indonesia  
Email: `rickyeka@unesa.ac.id`
