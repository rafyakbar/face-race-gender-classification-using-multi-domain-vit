# Tanggapan terhadap Penelaah (Response to Reviewers)

**ID Naskah Asli:** Access-2026-50857  
**Judul Artikel Asli:** *"Multi-Domain Vision Transformer Fusion for Intersectional Demographic Classification from Facial Images"*  
**Kepada:** Editor *IEEE Access*  
**Perihal:** Tanggapan terhadap penelaah  

---

Yth. Editor,

Terima kasih telah mengizinkan pengajuan ulang naskah kami dan memberikan kesempatan untuk menanggapi komentar para penelaah.

Kami mengunggah **(a)** tanggapan kami untuk setiap butir komentar di bawah ini (*Author's Response Files*), **(b)** naskah yang telah diperbarui dengan sorotan kuning untuk menandai perubahan (*Highlighted PDF*), dan **(c)** naskah yang telah diperbarui tanpa sorotan dalam format berkas sumber LaTeX dan dokumen utama PDF (*Main Manuscript*).

Melalui pengajuan ini, kami juga memohon kepada Editor agar menugaskan penelaah yang sama apabila memungkinkan.

Salam hormat,  
**Dr. Ir. Ricky Eka Putra, S.Kom., M.Kom.** dkk.

---

## Penelaah #1

### Penelaah #1, Komentar #1:
> *"1. the introduction is too long need to be summarized."*

**Tanggapan penulis:**  
Para penulis sepakat dengan komentar penelaah mengenai perlunya pemadatan Seksi I (*Introduction*). Narasi latar belakang telah dipadatkan dan ditata ulang menjadi tujuh paragraf terfokus dengan disiplin maksimal dua sitasi per kalimat agar alur pembacaan lebih padat, serta merumuskan empat kontribusi ilmiah utama secara eksplisit.

**Tindakan penulis:**  
Kami memperbarui Seksi I (*Introduction*, Halaman 1–2) dengan meringkas paragraf pengantar dan menambahkan rumusan empat kontribusi berikut pada Halaman 2:

> Kontribusi ilmiah utama dari penelitian ini dirangkum ke dalam empat aspek esensial sebagai berikut:
> 1. Formulasi kerangka kerja ablasi tujuh skema fitur yang mengintegrasikan backbone ViT pra-latih yang dibekukan dengan prapemrosesan tingkat-fold bebas kebocoran serta optimasi hyperparameter lintas empat famili pengklasifikasi untuk klasifikasi demografis interseksional.
> 2. Penetapan tolok ukur evaluasi bebas kebocoran identitas pada dataset DemogPairs dan studi komparatif ablasi kebocoran data untuk menguantifikasi efek memorisasi identitas wajah.
> 3. Evaluasi signifikansi statistik inferensial berpasangan yang memvalidasi keunggulan signifikan representasi multi-domain atas baseline domain tunggal, membuktikan paritas prediktif model linier dan non-linier teratas, serta mengungkap komplementaritas fitur usia linier versus kejenuhan representasi asimtotik non-linier.
> 4. Penyajian profil efisiensi komputasi komprehensif mencakup waktu ekstraksi ViT, biaya pelatihan, latensi inferensi, dan jejak memori yang merealisasikan kepala pengklasifikasi hilir berbobot sangat ringan untuk implementasi praktis.

---

### Penelaah #1, Komentar #2:
> *"2. The related works needs to be modified in better way and add equations."*

**Tanggapan penulis:**  
Para penulis berterima kasih atas saran konstruktif ini. Seksi II (*Related Works*) telah ditata ulang ke dalam tiga subseksi tematik yang runtut, yaitu *(II-A) Demographic Face Recognition*, *(II-B) Vision Transformers in Face Analysis*, dan *(II-C) Multi-Domain Feature Fusion*, disertai penambahan formulasi matematis untuk memperkuat landasan teoretis.

**Tindakan penulis:**  
Kami memperbarui Seksi II (*Related Works*, Halaman 2–4) dengan menyusun ulang tinjauan pustaka ke dalam Subseksi II-A hingga II-C serta menambahkan empat persamaan formal beserta definisi variabelnya pada Halaman 3: fungsi keputusan kernel KELM [Eq. (1)], proyeksi linear *patch* citra [Eq. (2)], mekanisme *Scaled Dot-Product Attention* dalam *Multi-Head Self-Attention* [Eq. (3)], dan formulasi fusi konkatenasi multi-domain [Eq. (4)], diikuti penegasan posisi kebaruan penelitian di akhir Subseksi II-C (Halaman 3–4).

---

### Penelaah #1, Komentar #3:
> *"3. The figure 3 needs to be redesigned and explained in better way to show the novelty of the proposed method and also not clear."*

**Tanggapan penulis:**  
Para penulis sepenuhnya setuju bahwa diagram arsitektur sebelumnya kurang jelas. Kami mendesain ulang **Figure 3** menjadi diagram arsitektur beresolusi tinggi yang memetakan tujuh tahapan terpadu secara berurutan: (1) prapemrosesan citra RGB 224 × 224, (2) pemartisian menjadi 196 *patch* 16 × 16, (3) proyeksi linear ke dimensi laten 768, (4) penambahan token `[CLS]` dan *positional embedding* (tahap 1–4 berjalan independen pada tiap *backbone* ViT), (5) ekstraksi paralel token `[CLS]` lapisan ke-12 dari tiga model ViT pra-latih yang dibekukan (`ViT-Face`, `ViT-Emotion`, `ViT-Age`), (6) konkatenasi langsung $\oplus$ menjadi vektor 2.304 dimensi, dan (7) klasifikasi hilir enam kelas menggunakan empat pengklasifikasi klasik.

**Tindakan penulis:**  
Kami mengganti **Figure 3** (Halaman 6) dengan diagram arsitektur baru dan memperluas penjelasan alur tujuh tahapan tersebut pada Seksi III-B (Halaman 4–5, Eq. (5)–(8)) untuk memperjelas kebaruan kerangka fusi tanpa *fine-tuning* ulang.

---

### Penelaah #1, Komentar #4:
> *"4. Graph in figure 4 needs to be discussed in better way."*

**Tanggapan penulis:**  
Para penulis mengucapkan terima kasih atas masukan ini. Pada Seksi IV-D (*Error Pattern Assessment*), kami memperdalam pembahasan matriks konfusi 6 × 6 Logistic Regression pada 2.160 citra uji *held-out* melintasi tiga tahapan representasi pada **Figure 4(a)–(c)** dengan membedah distribusi sel kesalahan non-diagonal secara kuantitatif.

**Tindakan penulis:**  
Kami memperbarui **Figure 4(a)–(c)** (Halaman 12) dan memperluas Seksi IV-D (Halaman 11 dan 13) dengan menambahkan analisis dekomposisi kesalahan berikut pada Halaman 13:

> Dekomposisi kuantitatif terhadap sel-sel off-diagonal matriks konfusi mengungkap bahwa pola kesalahan klasifikasi didominasi oleh misklasifikasi antarras dalam gender yang sama (same-gender cross-race). Pada model tri-domain (245 kesalahan), kebingungan intra-gender lintas-ras mencakup 165 citra (67.35% dari total kesalahan atau 7.64% dari seluruh sampel uji), menurun signifikan dari 194 kasus pada domain tunggal. Sel konfusi terbesar teramati pada Black Males ke Asian Males (23 citra), Black Females ke White Females (23 citra), dan Asian Females ke Black Females (23 citra). Sebaliknya, kesalahan lintas-gender hanya berjumlah 80 citra (32.65% dari total kesalahan atau 3.70% dari seluruh sampel uji). Pola ini selaras dengan profil recall Black Females (84.72%), di mana 37 dari 55 kesalahannya terjadi secara intra-gender menuju White Females (23) dan Asian Females (14).

---

### Penelaah #1, Komentar #5:
> *"5. Experimental works need to mention the dataset used in more detail and show the contribution of your proposed method and also to consider the time cost in the evaluation."*

**Tanggapan penulis:**  
Para penulis telah menindaklanjuti ketiga aspek tersebut: (1) merinci struktur 600 subjek DemogPairs (10.800 citra seimbang pada 6 kelas; 18 citra/subjek) dan partisi 80/20 *subject-disjoint*, (2) membuktikan kontribusi fusi tri-domain di atas domain tunggal secara inferensial ($p < 0.001$), dan (3) menambahkan profil biaya waktu serta efisiensi komputasi terukur.

**Tindakan penulis:**  
Kami memperbarui Seksi III-A (Halaman 4), **Figure 2** (Halaman 5), dan **Table 1** (Halaman 6) untuk rincian dataset, Seksi III-I (Halaman 8) untuk spesifikasi perangkat keras pengujian, serta Seksi IV-B dan **Table 14** (Halaman 11–12) untuk validasi statistik kontribusi metode ($p < 0.001$). Selain itu, kami menambahkan **Table 11** (Halaman 10), **Table 12** (Halaman 12), dan Paragraf 6 pada Seksi IV-A (Halaman 9 dan 11) yang melaporkan bahwa ekstraksi ViT *offline* pada GPU RTX 4060 membutuhkan **124.50 ms/citra** (22.41 menit total untuk 10.800 citra), pelatihan 5-fold CV LR Tri-Domain (**54.78 menit**) **9.3× lebih cepat** dari SVM (**511.10 menit**), dan inferensi kepala hilir LR (**0.0046 ms/sampel**) **1.027× (>1.000×) lebih cepat** dari SVM (**4.6785 ms/sampel**).

---

### Penelaah #1, Komentar #6:
> *"6. the authors need to compare their proposed method with more methods to validate their contribution."*

**Tanggapan penulis:**  
Para penulis sepakat dan telah memperluas perbandingan metode pembanding secara komprehensif dengan memisahkan studi terdahulu yang menggunakan partisi tingkat citra (*Stratified*) dan evaluasi terkontrol pada partisi bebas kebocoran (*Subject-Disjoint*).

**Tindakan penulis:**  
Kami memperbarui Seksi IV-E dan **Table 16** (Halaman 13) menjadi 12 entri komparasi empiris, mencakup tiga model pada kelompok protokol *Stratified* (Putri et al. *JIEET* 2025: 89.07%; Putri et al. *IEEE ICVEE* 2025: 92.41%; dan baseline historis kami: 93.70%) serta sembilan konfigurasi terkontrol pada kelompok protokol *Subject-Disjoint* (meliputi empat konfigurasi domain tunggal [`Face` pada LR dan SVM, `Emotion` pada SVM, serta `Age` pada SVM], dua konfigurasi domain ganda `Emotion` $\oplus$ `Face` [pada SVM 88.43% dan GNB 84.31%], serta tiga konfigurasi tri-domain lintas pengklasifikasi RF [85.00%], SVM [88.61%], dan LR [88.66%]).

---

### Penelaah #1, Komentar #7:
> *"7. conclusion part does not show the contribution in good way."*

**Tanggapan penulis:**  
Para penulis berterima kasih atas masukan ini dan telah menulis ulang seluruh Seksi V (*Conclusion*) menjadi dua paragraf terstruktur yang merangkum kontribusi empiris utama, paritas prediktif dan efisiensi komputasi, batasan penelitian, serta arah riset lanjutan.

**Tindakan penulis:**  
Kami memperbarui Seksi V (*Conclusion*, Halaman 14) menjadi dua paragraf terstruktur; paragraf pertama yang merangkum kesimpulan dan kontribusi utama adalah sebagai berikut (sementara paragraf kedua mengenai batasan penelitian dan arah riset lanjutan dikutip pada tanggapan Penelaah #2, Komentar #10):

> Penelitian ini membuktikan efektivitas fusi representasi multi-domain ViT (Face ⊕ Emotion ⊕ Age) untuk klasifikasi enam kelas interseksional dari tiga kelompok ras makro (Asian, Black, White) pada dataset DemogPairs. Di bawah protokol Strict Subject-Disjoint Partitioning dengan 0% kebocoran identitas (480 subjek latih dan 120 subjek uji held-out), pengklasifikasi LR meraih performa puncak dengan akurasi 88.66%, presisi makro 88.75%, recall makro 88.66%, dan F1-score makro 88.68%, disusul pengklasifikasi SVM dengan akurasi 88.61%, presisi makro 88.71%, recall makro 88.61%, dan F1-score makro 88.63%. Pengujian signifikansi statistik inferensial McNemar berpasangan membuktikan signifikansi fusi tri-domain terhadap representasi domain tunggal Face ($p < 0.001$) serta mengonfirmasi paritas prediktif antara LR dan SVM ($p = 1.0000$, dengan selisih bersih satu sampel dari 2.160 citra). Evaluasi keadilan algoritmik antarsubkelompok menunjukkan stabilitas prediksi dengan rentang recall 84.72% hingga 94.44% serta kesenjangan EOD sebesar 9.72 pp pada kedua model teratas. Dari aspek efisiensi komputasi, pengklasifikasi hilir LR terbukti paling optimal dengan latensi inferensi 0.0046 ms per sampel dan ukuran model 0.11 MB, merealisasikan kepala klasifikasi berbobot sangat ringan untuk implementasi praktis.

---

## Penelaah #2

### Penelaah #2, Komentar #1:
> *"1. Novelty and contribution: The methodological novelty beyond concatenating three pretrained feature representations and applying conventional classifiers should be more clearly established relative to existing dual-domain and multidomain approaches."*

**Tanggapan penulis:**  
Para penulis telah memperjelas kebaruan tingkat kerangka kerja (*framework-level novelty*) melampaui konkatenasi fitur sederhana: (1) sinergi tiga ruang laten komplementer (`ViT-Face`, `ViT-Emotion`, `ViT-Age`) secara *offline* dari *backbone* pra-latih yang dibekukan untuk menjaga efisiensi komputasi tanpa *fine-tuning* ulang, (2) investigasi sistematis tujuh skema fitur lintas empat famili pengklasifikasi di bawah validasi silang *5-Fold StratifiedGroupKFold* terisolasi penuh yang membuktikan kesetaraan performa pemisah linear LR terhadap kernel RBF non-linear ($p = 1.0000$), dan (3) karakterisasi empiris efek memorisasi identitas (5.09 pp) serta pembedaan komplementaritas usia linear vs. kejenuhan asimtotik non-linear.

**Tindakan penulis:**  
Kami memperbarui narasi konseptual penegasan kebaruan pada Seksi I Paragraf 5–6 (Halaman 2), Seksi II-C Paragraf 2 (Halaman 3–4), dan Seksi III Overview (Halaman 4), serta menyajikan pembuktian empiris paritas prediktif ($p = 1.0000$) dan efek memorisasi identitas (5.09 pp) pada Seksi IV-B (Halaman 11–12).

---

### Penelaah #2, Komentar #2:
> *"2. Data leakage and generalization: The image-level stratified split may allow images of the same identity to occur in both training and test sets. Please clarify whether identity overlap exists and provide subject-disjoint evaluation to establish genuine generalization."*

**Tanggapan penulis:**  
Para penulis mengonfirmasi bahwa partisi acak tingkat citra pada naskah awal menyebabkan tumpang tindih identitas penuh (berdasarkan audit partisi historis pada `experiment/code/archive/`, 593 dari 600 subjek hadir di data latih dan uji sekaligus, yang di dalam naskah Seksi IV-B [Halaman 11] dan **Table 13** [Halaman 12] dirangkum sebagai evaluasi tumpang tindih subjek penuh [*subject-overlap*]). Untuk menyelesaikannya secara tuntas, kami menetapkan protokol **Strict Subject-Disjoint Partitioning** sebagai tolok ukur utama (480 subjek latih / 8.640 citra; 120 subjek uji *held-out* / 2.160 citra; **0% kebocoran identitas**), menggunakan *5-Fold StratifiedGroupKFold* (`groups = subject_id`) untuk seluruh penalaan, penskalaan, dan PCA. Hasil partisi lama tetap disajikan secara transparan sebagai studi ablasi kebocoran data untuk mengukur efek memorisasi identitas wajah (penurunan 5.09 pp pada SVM dari 93.70% ke 88.61%, dan 4.07 pp pada LR dari 92.73% ke 88.66%).

**Tindakan penulis:**  
Kami memperbarui Abstrak (Halaman 1), Seksi III Overview (Halaman 4), **Figure 1** (Halaman 5, dengan label *"80:20 Subject-Disjoint Split"* dan *"5-Fold StratifiedGroupKFold Cross-Validation"*), Seksi III-A & **Table 1** (Halaman 4, 6), Seksi III-G (Halaman 7), seluruh benchmark utama pada **Table 7–10** (Halaman 9–10), serta studi ablasi kebocoran data pada Seksi IV-B dan **Table 13** (Halaman 11–12).

---

### Penelaah #2, Komentar #3:
> *"3. Preprocessing and reproducibility: Please specify the exact checkpoint versions, image processors, normalization parameters, and feature extraction procedures used for all three pretrained ViT models."*

**Tanggapan penulis:**  
Para penulis telah mendokumentasikan spesifikasi teknis reproduktibilitas pada Seksi III-A dan III-B, serta melengkapinya dengan rincian konfigurasi *image processor* berikut:
1. **Versi *Checkpoint*:** Sebagaimana tercantum pada Seksi III-B Paragraf 2 (Halaman 4), ketiga model merupakan arsitektur ViT-Base/16 (12 lapisan encoder, dimensi laten $D = 768$; dengan 12 *attention heads* per lapisan sesuai konfigurasi standar ViT-Base) turunan `google/vit-base-patch16-224-in21k`: `ViT-Face` (`skutaada/VIT-VGGFace`, versi `e85f0c9`, *fine-tuned* VGGFace2), `ViT-Emotion` (`dima806/facial_emotions_image_detection`, versi `747cf16`, *fine-tuned* FER-2013), dan `ViT-Age` (`dima806/facial_age_image_detection`, versi `ad35933`, *fine-tuned* UTKFace + IMDB-WIKI).
2. **Prapemrosesan & Normalisasi:** Sebagaimana dijelaskan pada Seksi III-A Paragraf 2 (Halaman 4) dan Seksi III-B Paragraf 2 (Halaman 4), citra wajah terpusat DemogPairs dikonversi ke format RGB 3-kanal, diubah resolusinya menjadi 224 × 224 piksel, dan diproses melalui `AutoImageProcessor` dengan normalisasi kanal seragam $\mu = \sigma = [0.5, 0.5, 0.5]$ tanpa augmentasi sintetis. Sebagai rincian teknis tambahan dari konfigurasi *processor* (`preprocessor_config.json`), korpus DemogPairs telah berformat *pre-cropped* sehingga tidak memerlukan deteksi wajah eksternal (seperti MTCNN), sedangkan `AutoImageProcessor` menerapkan interpolasi bilinear dan penskalaan intensitas $1/255$ sebelum normalisasi ke rentang $[-1, 1]$.
3. **Ekstraksi `[CLS]` & Fusi:** Sebagaimana dirumuskan pada Seksi III-B Paragraf 3 (Halaman 4–5) dan **Table 2** (Halaman 6), ketiga *backbone* dibekukan (*frozen*, tanpa pembaruan gradien), lalu token `[CLS]` lapisan ke-12 setelah *Layer Normalization* [Eq. (7)] digabungkan menjadi vektor 2.304 dimensi [Eq. (8)].

**Tindakan penulis:**  
Kami menambahkan spesifikasi *checkpoint* beserta nomor versinya, parameter normalisasi `AutoImageProcessor`, **Eq. (7)–(8)**, dan ringkasan tujuh konfigurasi ablasi pada Seksi III-A Paragraf 2 (Halaman 4), Seksi III-B Paragraf 2–3 (Halaman 4–5), dan **Table 2** (Halaman 6).

---

### Penelaah #2, Komentar #4:
> *"4. Hyperparameter search consistency: The reported totals of 1,086 configurations, 38,010 cross-validation fits, and 28 final refits should be reconciled with the individual search spaces reported in Tables 3–6."*

**Tanggapan penulis:**  
Para penulis berterima kasih atas audit aritmatika ini. Audit kode sumber menunjukkan bahwa angka draf awal (1.086 konfigurasi dan 38.010 fits) muncul akibat pencantuman parameter Logistic Regression berlebih pada **Table 5** ($C=100$, `'newton-cg'`, dan `max_iter=2000` yang tidak dieksekusi), sehingga LR tercatat 270 kombinasi padahal eksekusi aktualnya adalah **96 kombinasi** ($2 \text{ scaler} \times 3 \text{ PCA} \times 4 \ C \times 2 \text{ solver} \times 2 \text{ max\_iter}$). Selain itu, pada **Table 6** (SVM), dari 288 kombinasi grid Cartesian ($2 \text{ scaler} \times 3 \text{ PCA} \times 4 \ C \times 3 \text{ kernel} \times 2 \text{ degree} \times 2 \ \gamma$), jumlah konfigurasi unik efektifnya adalah **168 konfigurasi unik efektif** ($24 \text{ [linear]} + 48 \text{ [rbf]} + 96 \text{ [poly]} = 168$). Rekonsiliasi lengkapnya adalah sebagai berikut:

| Pengklasifikasi & Tabel | Draf Awal | Revisi Aktual | Fits/Skema ($\times 5$ Folds) | Total CV Fits ($\times 7$ Skema) | Keterangan |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Random Forest (Table 3)** | 288 | **288** | 1.440 | 10.080 | $2 \times 3 \times 2 \times 3 \times 2 \times 2 \times 2$ |
| **Gaussian Naive Bayes (Table 4)** | 240 | **240** | 1.200 | 8.400 | $2 \text{ scaler} \times 3 \text{ PCA} \times 40 \text{ var\_smoothing}$ |
| **Logistic Regression (Table 5)** | 270 | **96** | **480** | **3.360** | Dikoreksi: tanpa $C=100$, `'newton-cg'`, `2000` |
| **Support Vector Machine (Table 6)** | 288 | **288** | 1.440 | 10.080 | 288 Cartesian (**168 unik efektif**) |
| **Total per Skema / Global** | **1.086 / 38.010** | **912 / 31.920** | **4.560** | **31.920 CV fits + 28 refits** | Seluruh bab telah diselaraskan |

**Tindakan penulis:**  
Kami menyelaraskan rincian ruang pencarian pada **Table 3–6** (Halaman 7), narasi Seksi III-F (Halaman 6, mengenai 288 kombinasi grid Cartesian atau **168 konfigurasi unik efektif** SVM dan 1.440 fits), serta Seksi III-G (Halaman 7, `912 kombinasi × 5 folds = 4.560 fits × 7 skema fitur + 28 refits akhir`, yang setara dengan total **31.920** *cross-validation fits*).

---

### Penelaah #2, Komentar #5:
> *"5. Statistical interpretation: The SVM accuracy improvement from 93.29% to 93.70% is not statistically significant according to the reported McNemar test (p = 0.3057). Consequently, claims of tri-domain superiority and feature saturation should be appropriately qualified."*

**Tanggapan penulis:**  
Para penulis sepenuhnya setuju dan telah menerapkan uji McNemar berpasangan dengan koreksi kontinuitas Edwards [Eq. (21)], uji eksak binomial dua arah, serta 95% Wilson Score CI [Eq. (22)] pada tolok ukur *subject-disjoint* ($N = 2.160$):
1. **Tri-Domain vs. Single `Face`:** Terbukti signifikan secara statistik baik pada SVM (88.61% vs. 86.16%; $+2.45\text{ pp}$, $\chi^2 = 20.96$, McNemar $p < 0.001$, Exact Binomial $p < 0.001$) maupun LR (88.66% vs. 86.39%; $+2.27\text{ pp}$, $\chi^2 = 19.69$, McNemar $p < 0.001$, Exact Binomial $p < 0.001$).
2. **Kualifikasi Kejenuhan Fitur (*Tri-Domain* vs. `Emotion` $\oplus$ `Face`):** Pada RBF SVM, penambahan fitur usia menghasilkan selisih non-signifikan ($88.43\% \to 88.61\%$, $+0.18\text{ pp}$, $\chi^2 = 0.12$, McNemar $p = 0.7341$, Exact Binomial $p = 0.7343$), yang dikualifikasikan sebagai **kejenuhan fitur laten asimtotik**. Sebagai verifikasi tambahan dari log prediksi eksperimen, perbandingan SVM Tri-Domain terhadap `Face` $\oplus$ `Age` (87.55%, $\chi^2 = 6.82$, Exact Binomial $p = 0.0086 < 0.01$) tetap mengonfirmasi signifikansi kontribusi fitur emosi. Sebaliknya, pada LR linear, penambahan fitur usia di atas `Emotion` $\oplus$ `Face` memberikan kenaikan signifikan ($87.45\% \to 88.66\%$, $+1.21\text{ pp}$, $\chi^2 = 7.10$, McNemar $p = 0.0077$, Exact Binomial $p = 0.0073 < 0.01$).
3. **Paritas Prediktif LR vs. SVM:** Perbandingan LR Tri-Domain (1.915 benar) dan SVM Tri-Domain (1.914 benar) menghasilkan $\chi^2 = 0.00$, McNemar $p = 1.0000$, dan Exact Binomial $p = 1.0000$ (+1 citra bersih), yang dibingkai sebagai **paritas prediktif**.

**Tindakan penulis:**  
Kami menambahkan **Table 14** (Halaman 12) dengan nilai McNemar $\chi^2$ $p$-value dan Exact Binomial $p$-value yang terverifikasi, serta mengualifikasikan seluruh klaim statistik secara konsisten di Abstrak (Halaman 1), Seksi IV-A & IV-B (Halaman 8–12), dan Seksi V (Halaman 14).

---

### Penelaah #2, Komentar #6:
> *"6. Fairness analysis: The reported Equal Opportunity Difference values provide useful subgroup information but do not establish comprehensive demographic fairness. Please clarify the scope and limitations of the fairness claims."*

**Tanggapan penulis:**  
Para penulis sependapat bahwa *Equal Opportunity Difference* (EOD) tidak membuktikan keadilan demografis secara menyeluruh. Kami mengualifikasikan EOD ($9.72\text{ pp}$ antara *White Males* TPR 94.44% dan *Black Females* TPR 84.72%) murni sebagai indikator disparitas performa empiris antarsubkelompok pada data uji DemogPairs.

**Tindakan penulis:**  
Kami menambahkan definisi batas EOD pada Seksi III-H (Halaman 8, Eq. (23)), menyajikan **Table 15** (Halaman 12), dan menyertakan kalimat kualifikasi berikut pada Seksi IV-C (Halaman 11):

> Sebagai komitmen etika Artificial Intelligence (AI) dan delimitasi ruang lingkup (Responsible AI), disparitas ini secara tegas tidak diklaim sebagai jaminan tercapainya keadilan demografis universal (no overclaim of complete demographic fairness), melainkan sebagai audit transparansi performa subkelompok empiris.

---

### Penelaah #2, Komentar #7:
> *"7. Baseline comparison: Please clarify whether the prior methods in Table 12 used comparable data partitions, preprocessing, and evaluation protocols. Otherwise, the comparison should be presented as contextual rather than a controlled benchmark."*

**Tanggapan penulis:**  
Para penulis sependapat dan telah mengklarifikasi adanya perbedaan partisi data, prapemrosesan, dan protokol evaluasi antara literatur terdahulu dan tolok ukur utama kami. Oleh karena itu, kami memisahkan tabel perbandingan literatur secara tegas menjadi komparasi kontekstual (*Stratified*, untuk studi DemogPairs terdahulu dengan partisi tingkat citra yang mengandung tumpang tindih identitas subjek serta potensi variasi prapemrosesan antarstudi) dan tolok ukur terkontrol (*Subject-Disjoint*, untuk evaluasi internal dengan prapemrosesan seragam dan protokol evaluasi bebas kebocoran yang identik).

**Tindakan penulis:**  
Kami memperbarui **Table 16** (Halaman 13) beserta narasi kualifikasi metodologis pada Seksi IV-E (Halaman 13) yang membedakan kedua kelompok protokol evaluasi tersebut.

---

### Penelaah #2, Komentar #8:
> *"8. Computational efficiency: Please report feature extraction time, classifier training time, inference latency, memory consumption, and model storage requirements to substantiate the efficiency claims."*

**Tanggapan penulis:**  
Para penulis telah mengukur dan melaporkan kelima dimensi efisiensi pada perangkat keras Intel Core i9-13900H, RAM 32 GB DDR5, dan GPU NVIDIA RTX 4060 (8 GB VRAM):
1. **Ekstraksi ViT (10.800 citra):** 39.74 ms (`Face`), 39.65 ms (`Emotion`), 45.11 ms (`Age`), total tri-domain **124.50 ms/citra** (22.41 menit total di GPU).
2. **Pelatihan 5-Fold CV:** LR Tri-Domain **3,287.07 detik (54.78 menit)** vs. SVM Tri-Domain **30,666.02 detik (511.10 menit)** (**9.3× lebih cepat**).
3. **Latensi Inferensi Kepala Hilir:** LR **0.0046 ms/sampel** vs. SVM **4.6785 ms/sampel** (**1.027× [>1.000×] lebih cepat**; sebagai penjumlahan kumulatif waktu ekstraksi **Table 11** dan inferensi **Table 12**, total latensi *end-to-end* GPU adalah $\approx 124.505\text{ ms}$ untuk LR vs. $\approx 129.179\text{ ms}$ untuk SVM).
4. **Konsumsi RAM & Cache:** Array uji *held-out* ($N = 2.160$, `float32`) memakai **18.98 MB RAM** (tri-domain) dan **12.66 MB RAM** (dual-domain); *cache* fitur di disk 30.8 MB/domain (92.4 MB total).
5. **Ukuran Model:** LR **0.11 MB** vs. SVM **36.60 MB** (**330× [>330×] lebih ringkas**).

**Tindakan penulis:**  
Kami menambahkan Seksi III-I (*Experimental Setup*, Halaman 8), **Table 11** (Halaman 10), **Table 12** (Halaman 12), analisis efisiensi pada Seksi IV-A Paragraf 6 (Halaman 9 dan 11), serta Seksi V (Halaman 14), dengan menegaskan bahwa keunggulan 0.11 MB dan 0.0046 ms berlaku pada kepala pengklasifikasi hilir, sementara pengembangan ke depan pada Seksi V Paragraf 2 (Halaman 14) mencakup penerapan teknik kuantisasi atau *knowledge distillation* pada *backbone* ViT.

---

### Penelaah #2, Komentar #9:
> *"9. Results and discussion: Several interpretations concerning phenotypic overlap, the contribution of age-related features, and reductions in inter-racial errors remain insufficiently supported by confusion matrices alone. These statements should be qualified or supported by additional analyses."*

**Tanggapan penulis:**  
Para penulis menerima koreksi ini sepenuhnya dan telah menghapus seluruh spekulasi mengenai morfologi kraniofasial, tekstur kerutan epidermis, maupun kontras pencahayaan dari Abstrak, Seksi IV-C, dan Seksi IV-D.

**Tindakan penulis:**  
Kami memperbarui Abstrak (Halaman 1), Seksi IV-C (Halaman 11), dan Seksi IV-D (Halaman 11 dan 13), termasuk menambahkan paragraf kualifikasi berikut pada Seksi IV-D (Halaman 13):

> Fenomena tumpang tindih visual antarras yang melandasi pola misklasifikasi tersebut dikaji secara objektif murni berdasarkan distribusi variasi visual citra, tanpa menyertakan asumsi kausal biologis yang tidak teruji secara mandiri. Evaluasi empiris menunjukkan bahwa matriks konfusi merefleksikan karakteristik sebaran data observasional pada korpus yang dievaluasi. Penambahan representasi penuaan usia biologis terbukti memberikan kontribusi terukur dalam menekan kebingungan intra-gender lintas-ras dari 185 menjadi 165 kasus, selaras dengan signifikansi statistik uji McNemar (p = 0.0073). Kualifikasi ini menegaskan bahwa keunggulan fusi multi-domain bersumber dari pengayaan kovariat fitur laten yang saling melengkapi, sehingga mampu mengurai ambiguitas visual pada ruang representasi tanpa bertumpu pada spekulasi fenotipik atau kondisi pencahayaan.

---

### Penelaah #2, Komentar #10:
> *"10. Conclusion and limitations: The conclusions should be restricted to the evaluated DemogPairs benchmark unless additional cross-identity or external-dataset validation is provided."*

**Tanggapan penulis:**  
Para penulis sepenuhnya setuju. Cakupan klaim dan kesimpulan penelitian dibatasi secara eksplisit pada enam kelas interseksional dari tiga ras makro (**Asian, Black, White**) dalam tolok ukur DemogPairs *subject-disjoint*.

**Tindakan penulis:**  
Kami membatasi ruang lingkup klaim pada Abstrak (Halaman 1) serta menambahkan pernyataan batasan penelitian secara eksplisit pada Paragraf 2 Seksi V (*Conclusion*, Halaman 14) sebagai berikut:

> Meskipun menawarkan kontribusi empiris yang signifikan, penelitian ini memiliki dua batasan utama yang memerlukan perhatian. Pertama, cakupan demografis penyelidikan ini terbatas pada tiga kelompok ras makro dalam dataset DemogPairs (Asian, Black, White), sehingga generalisasi performa klasifikasi ke kelompok multirasial maupun populasi etnisitas lain tetap membutuhkan pengujian empiris tambahan. Kedua, proses ekstraksi representasi multi-domain masih dijalankan secara terpisah (offline) memanfaatkan tiga model backbone ViT-Base beku tanpa fine-tuning end-to-end terpadu, sehingga memerlukan tahapan pemrosesan fitur tersendiri sebelum klasifikasi hilir.

---

*Catatan: Referensi yang disarankan oleh penelaah hanya boleh ditambahkan apabila relevan dengan artikel dan membuatnya lebih lengkap. Kasus rekomendasi artikel yang tidak relevan secara berlebihan perlu dilaporkan kepada `ieeeaccesseic@ieee.org`.*
