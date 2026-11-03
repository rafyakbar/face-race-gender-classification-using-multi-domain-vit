# Audit Mendalam `paper_outline_v1.1.md` terhadap `paper_reviews_ieee/`

**Tanggal**: 2026-11-03
**Auditor**: Claude Sonnet 5.5 (Medium), Antigravity
**Objek audit**: [paper_outline_v1.1.md](../../paper_outline_v1.1.md) (911 baris, dibaca penuh)
**Rujukan reviewer**: [Comments.md](../Comments.md) (R1 #1-7, R2 #1-10, AE), [00_URUTAN_PRIORITAS_REVISI.md](../00_URUTAN_PRIORITAS_REVISI.md), [08_revision_roadmap.md](../08_revision_roadmap.md), [Resubmission-Checklist.md](../Resubmission-Checklist.md)
**Sumber verifikasi angka dan klaim**: `experiment/code/results/*.json` (28 model, termasuk `y_test`/`y_pred`), `experiment/code/times/*.json`, `experiment/code/md/**` (notebook hasil eksekusi), `experiment/code/utils/*.py`, `experiment/code/archive/md_old/`, `README.ai.md`, `images/*.png`.

> Audit ini berbeda dari [2026-11-03_claude-sonnet-5.5.md](2026-11-03_claude-sonnet-5.5.md) yang tidak memverifikasi angka ke sumber. Di sini setiap angka tabel IV.A-IV.E dihitung ulang dari JSON, dan klaim metodologis dicocokkan ke kode. Hasilnya menemukan **3 masalah kritis yang tidak terdeteksi oleh pemeriksaan konsistensi internal saja** (temuan K1, K2, K3).

---

## 1. Kesimpulan Eksekutif

Struktur outline v1.1 **memetakan seluruh 17 komentar reviewer** dan sebagian besar angka tabel hasil **akurat** terhadap JSON. Namun outline **belum layak dikunci** karena:

| # | Tingkat | Ringkasan |
|---|:---:|---|
| K1 | **Kritis** | Ruang pencarian Logistic Regression di outline (Tabel V: 270 kombinasi) **tidak sama** dengan yang dieksekusi untuk Primary Benchmark (96 kombinasi). Total 1.086 / 38.010 fits **salah**; yang benar 912 / 31.920. Ini tepat inti R2 #4. |
| K2 | **Kritis** | Tiga tabel acuan matriks konfusi (IV.D, "non-numbered") **salah label kelas** (indeks JSON dibaca urutan alfabet). Gambar PNG Figure 4 benar, tabel acuan di outline salah. Satu angka sel di narasi IV.D P2 juga salah. |
| K3 | **Kritis** | Klaim "MTCNN face alignment" di III.A P2 **tidak ada di kode manapun**. Klaim ini fiktif terhadap pipeline aktual (R2 #3 reproduktibilitas). |
| T1-T7 | Tinggi | Overclaim berulang ("membuktikan", "ekuivalen", "Edge AI", "tergeneralisasi") yang bertentangan dengan R2 #5, #6, #8, #9, #10 dan aturan 0.B outline sendiri. |
| S1-S8 | Sedang | Ketertelusuran angka latensi, konfounder studi ablasi leakage, R1 #6 lemah, dll. |
| M1-M10 | Rendah | Inkonsistensi kecil dan pembulatan. |

**Status akhir**: *Belum sesuai penuh*. 8 dari 17 komentar reviewer **Terpenuhi**, 9 **Parsial** (lihat Bagian 3). Setelah K1-K3 dan T1-T7 diperbaiki, outline dapat dianggap sesuai.

---

## 2. Cakupan dan Metode

1. Membaca penuh outline v1.1, `Comments.md`, `00_URUTAN_PRIORITAS_REVISI.md`, `08_revision_roadmap.md`, `Resubmission-Checklist.md`.
2. Menghitung ulang dari `results/*.json`: akurasi, F1, matriks konfusi 6x6 (dengan **pemetaan label yang benar** dari `utils/constants.py`), metrik per-subkelompok, tabel McNemar (b, c, chi-kuadrat Edwards, p eksak binomial), Wilson CI, rata-rata lintas konfigurasi, waktu pelatihan, latensi, ukuran model.
3. Membandingkan `param_grid` dan keluaran `len(ParameterGrid(...))` di 28 notebook `experiment/code/md/{svm,lr,rf,gnb}/`.
4. Memeriksa `utils/dataset.py` (cara pembagian data), `utils/extraction.py` (pra-pemrosesan dan ekstraksi CLS), `times/*.json`.
5. Memeriksa keberadaan seluruh berkas gambar yang dirujuk outline dan melihat `confusion_matrix_lr_tri_v1.1.png` serta `vit_v2.2.png`.

**Tidak dapat diverifikasi** (perlu dicek manual oleh penulis): SHA revisi checkpoint HuggingFace, korpus fine-tuning tiap checkpoint, isi `preprocessor_config.json`, sitasi dan angka studi Putri et al. (kutipan dari publikasi sendiri).

---

## 3. Status Kesesuaian per Komentar Reviewer

| Komentar | Status | Catatan ringkas |
|---|:---:|---|
| **AE** 3 berkas + Byline + Checklist | Di luar cakupan outline | Outline memuat 5 penulis (sesuai rencana Byline Change). Berkas administratif tidak diperiksa di sini. |
| **R1 #1** Intro terlalu panjang | **Parsial** | Klaim "700-850 kata" tetapi jumlah batas atas target 7 paragraf = **945 kata** (lihat M1). Tidak ada sitasi untuk klaim fakta P1-P2 (S7). |
| **R1 #2** Related Works + persamaan | Terpenuhi | 3 subseksi x 2 paragraf, Eq. 1-4. |
| **R1 #3** Figure 3 | Terpenuhi | `vit_v2.2.png` ada, 7 tahap sesuai panduan narasi, catatan interpretasi gambar tepat. |
| **R1 #4** Pembahasan Figure 4 | **Parsial** | Narasi kuat, tetapi tabel acuan salah label (K2) dan 1 sel salah. |
| **R1 #5** Dataset dan time cost | **Parsial** | Tabel I dan XI ada. Namun ketertelusuran latensi bermasalah (S1) dan metrik "RAM" tidak mencerminkan konsumsi memori sebenarnya (S2). |
| **R1 #6** Lebih banyak baseline | **Parsial (lemah)** | Hanya 2 studi eksternal, keduanya oleh penulis yang sama. Bagian B adalah ablasi internal (S4). |
| **R1 #7** Conclusion | **Parsial** | P1 memakai "membuktikan" dan tidak memuat kualifikasi saturasi (T3). |
| **R2 #1** Novelty | **Parsial** | Novelty dinyatakan di level kerangka evaluasi (jujur) tetapi tidak ada eksperimen pembeda terhadap "sekadar konkatenasi" (S5). |
| **R2 #2** Leakage | Terpenuhi (dengan catatan S3, S6) | Subject-disjoint, Tabel XII. Namun konfounder ablasi dan pra-pelatihan backbone belum dibahas. |
| **R2 #3** Reproduktibilitas | **Parsial** | Klaim MTCNN fiktif (K3), "[0,1]" bertentangan dengan mu=sigma=0.5 (M3), SHA tidak dapat diverifikasi. |
| **R2 #4** Rekonsiliasi hyperparameter | **Tidak terpenuhi** | Angka LR salah (K1). |
| **R2 #5** Interpretasi statistik | **Parsial** | Angka McNemar **benar**. Namun "membuktikan saturasi" dan "ekuivalen" melanggar kualifikasi yang diminta (T2, T3). |
| **R2 #6** Batas klaim fairness | **Parsial** | Ada penafian, tetapi IV.C P2 memuat atribusi kausal fenotipik dan pencahayaan (T5). |
| **R2 #7** Komparasi kontekstual | Terpenuhi | Tabel XV dipisah Bagian A dan B dengan catatan. |
| **R2 #8** Efisiensi komputasi | **Parsial** | Lima dimensi disajikan, tetapi klaim "Edge AI" tidak didukung (T4) dan ada masalah S1, S2. |
| **R2 #9** Klaim fenotipik | **Parsial** | IV.D P3 baik, tetapi Abstrak, Intro P1, IV.C P2 masih memuat klaim fenotipik (T5). |
| **R2 #10** Batas kesimpulan | **Parsial** | Limitations P2 baik, tetapi Abstrak dan Conclusion P1 menyatakan generalisasi (T1). |

---

## 4. Temuan Kritis (harus diperbaiki sebelum outline dikunci)

### K1. Ruang pencarian LR dan total fits tidak sesuai eksperimen aktual (R2 #4)

**Bukti** (`experiment/code/md/lr/2.5.*_lr_*.md`, ketujuh notebook): 

```python
'classifier__C': [0.01, 0.1, 1, 10],
'classifier__max_iter': [500, 1000],
'classifier__solver': ['lbfgs', 'saga'],
...
LogisticRegression: 96 kombinasi
```

Outline Tabel V menulis `C = {0.01, 0.1, 1, 10, 100}`, `solver = {lbfgs, saga, newton-cg}`, `max_iter = {500, 1000, 2000}` = **270**. Parameter `C=100`, `newton-cg`, `max_iter=2000` **tidak pernah dijalankan** pada Primary Benchmark. Konfigurasi 270 adalah grid protokol *subject-overlap* historis (JSON historis LR Tri memilih `solver=newton-cg`, lihat `README.ai.md` baris 343).

Verifikasi ulang seluruh grid (keluaran `len(ParameterGrid)` di semua 28 notebook):

| Classifier | Outline | Dieksekusi | Selisih |
|---|:---:|:---:|:---:|
| SVM | 288 | 288 | sesuai |
| RF | 288 | 288 | sesuai |
| GNB | 240 | 240 | sesuai |
| **LR** | **270** | **96** | **tidak sesuai** |
| **Total kombinasi** | **1.086** | **912** | |
| **CV fits per skema (x5)** | 5.430 | 4.560 | |
| **Total CV fits (x7)** | **38.010** | **31.920** | |
| Refit akhir | 28 | 28 | sesuai |

Rincian per famili yang benar: SVM 10.080, RF 10.080, GNB 8.400, LR 3.360 (jumlah 31.920).

**Dampak**: R2 #4 meminta rekonsiliasi total dengan Tabel 3-6. Outline merekonsiliasi **angka lama yang salah**; reviewer yang membuka log notebook (atau kode di repositori) akan menemukan 96. Kriteria keberhasilan di `08_revision_roadmap.md` R2-4 ("konsisten 100% dengan total fits eksperimen aktual") **gagal**. Juga memengaruhi klaim "LR 9,3x lebih cepat dilatih" (lihat S1: LR hanya mencari 96 kombinasi, SVM 288).

**Tindakan**: (a) Ubah Tabel V menjadi `C={0.01,0.1,1,10}`, `solver={lbfgs,saga}`, `max_iter={500,1000}` (96 kombinasi, 480 fits). (b) Ubah total menjadi 912 / 4.560 / **31.920** CV fits + 28 refit di III.G, Intro P5 (poin 4), 0.A, dan seluruh dokumen turunan (`README.md` baris 266, `README.ai.md`, `00_URUTAN_PRIORITAS_REVISI.md`, `08_revision_roadmap.md`, `09_revision_tracking.md`, `10_response_letter_skeleton.md`). (c) Alternatif: jalankan ulang LR dengan grid 270 jika ingin mempertahankan angka lama, tetapi seluruh hasil Tabel IX/XI/XIII/XIV/Figure 4 berpotensi berubah.

Catatan tambahan terkait R2 #4 (sebelumnya sudah ditandai audit lain): pada Tabel VI SVM, `degree` hanya aktif pada kernel `poly` dan `gamma` tidak aktif pada `linear`. Jumlah konfigurasi **efektif unik** SVM = 6 (scaler x PCA) x 4 (C) x (1 linear + 2 rbf + 4 poly) = **168**, bukan 288. Sebaiknya ditulis "288 kombinasi grid (168 konfigurasi efektif unik)" agar reviewer tidak mempermasalahkan.

### K2. Tabel acuan matriks konfusi (IV.D) salah label kelas

`DEMOGPairs_LABEL_TO_IDX` di `utils/constants.py` **bukan urutan alfabet**:

```
Black_Males=0, White_Females=1, Asian_Males=2, White_Males=3, Black_Females=4, Asian_Females=5
```

Tabel (a), (b), (c) di outline (baris 755-791) tampak dibangun dari `y_test`/`y_pred` mentah lalu **diberi label alfabet**. Angkanya mencocokkan JSON mentah, tetapi baris dan kolom salah nama. Bukti pembanding: notebook `lr/2.5.7*.md` dan gambar `images/confusion_matrix_lr_tri_v1.1.png` (yang benar) menampilkan baris `Asian_Females = [312, 18, 23, 0, 6, 1]`, sedangkan tabel (c) outline menampilkan `[316, 0, 23, 6, 15, 0]`. Metrik per-subkelompok Tabel XIV **benar** (dari `classification_metrics`), sehingga tabel (c) juga tidak konsisten dengan Tabel XIV (mis. presisi Asian_Females dari tabel (c) = 91,59% vs 86,43% di Tabel XIV).

Matriks yang **benar** (dihitung ulang dengan pemetaan label sesuai `constants.py`; urutan baris/kolom: AF, AM, BF, BM, WF, WM):

**(a) Single `Face` (LR; 294 kesalahan)**

| Actual \ Pred | Asian_Females | Asian_Males | Black_Females | Black_Males | White_Females | White_Males |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Asian_Females** | 313 | 14 | 24 | 0 | 8 | 1 |
| **Asian_Males** | 18 | 302 | 6 | 24 | 0 | 10 |
| **Black_Females** | 17 | 12 | 287 | 21 | 22 | 1 |
| **Black_Males** | 0 | 21 | 17 | 316 | 0 | 6 |
| **White_Females** | 32 | 3 | 7 | 0 | 314 | 4 |
| **White_Males** | 0 | 14 | 1 | 9 | 2 | 334 |

**(b) Dual `Emotion ⊕ Face` (LR; 271 kesalahan)**

| Actual \ Pred | Asian_Females | Asian_Males | Black_Females | Black_Males | White_Females | White_Males |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Asian_Females** | 304 | 19 | 26 | 0 | 10 | 1 |
| **Asian_Males** | 18 | 311 | 7 | 17 | 0 | 7 |
| **Black_Females** | 17 | 5 | 310 | 9 | 17 | 2 |
| **Black_Males** | 0 | 24 | 17 | 309 | 1 | 9 |
| **White_Females** | 26 | 1 | 12 | 0 | 317 | 4 |
| **White_Males** | 0 | 17 | 1 | 3 | 1 | 338 |

**(c) Tri `Face ⊕ Emotion ⊕ Age` (LR; 245 kesalahan; identik dengan PNG dan notebook)**

| Actual \ Pred | Asian_Females | Asian_Males | Black_Females | Black_Males | White_Females | White_Males |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Asian_Females** | 312 | 18 | 23 | 0 | 6 | 1 |
| **Asian_Males** | 17 | 316 | 4 | 17 | 0 | 6 |
| **Black_Females** | 14 | 8 | 305 | 8 | 23 | 2 |
| **Black_Males** | 0 | 23 | 15 | 316 | 0 | 6 |
| **White_Females** | 18 | 3 | 11 | 0 | 326 | 2 |
| **White_Males** | 0 | 14 | 0 | 4 | 2 | 340 |

Hasil penting: **angka agregat di narasi IV.D P1 dan P2 benar** (294/271/245; same-gender cross-race 194/185/165; cross-gender same-race 76/68/62; both 24/18/18; 165 = 67,3%; 80 = 3,70% N = 32,7%). Yang salah hanya tabel acuan dan satu sel narasi:

- IV.D P2 menulis `Black_Females → Asian_Females (17)`. Yang benar **14** (nilai 17 adalah `Asian_Males → Asian_Females`). Sel lain yang disebut (`Black_Males→Asian_Males 23`, `Black_Females→White_Females 23`, `Asian_Females→Black_Females 23`, `Asian_Females→Asian_Males 18`, `Asian_Males→Asian_Females 17`) **benar**.

**Tindakan**: ganti ketiga tabel acuan dengan tabel di atas (atau salin langsung dari notebook), koreksi "(17)" menjadi "(14)". Verifikasi juga bahwa `confusion_matrix_lr_single_v1.1.png` dan `..._dual_v1.1.png` memakai pemetaan benar (gambar tri sudah benar).

### K3. Klaim "MTCNN face alignment" tidak ada di pipeline

III.A Paragraph 2, poin 3: *"Preprocessing citra mencakup konversi ke 3-channel RGB, deteksi dan face alignment MTCNN, resize ... 224x224, dan normalisasi intensitas kanal ke rentang [0, 1]."*

Pencarian kata `mtcnn` (tidak peka huruf besar-kecil) di `experiment/code/*.py`, `scripts/`, 28+ notebook `md/`, `paper/*.md`, `README.ai.md` menghasilkan **nol hasil**. `utils/extraction.py` hanya melakukan: `Image.open` -> `convert("RGB")` -> `AutoImageProcessor` bawaan checkpoint -> `model.vit(**inputs).last_hidden_state[:, 0, :]`. Tidak ada deteksi atau penyelarasan wajah (DemogPairs sudah berupa crop wajah).

Selain itu "normalisasi ke [0,1]" bertentangan dengan III.B P2 (`mu = sigma = 0.5`, yaitu rentang [-1, 1] setelah rescale 1/255). Kedua kalimat tidak dapat benar bersamaan.

**Dampak**: R2 #3 meminta *exact* prosedur ekstraksi. Mencantumkan langkah yang tidak dijalankan merusak reproduktibilitas dan kredibilitas; reviewer dapat menolak naskah jika menemukan ketidaksesuaian dengan kode. **Tindakan**: hapus MTCNN. Tulis: "RGB -> resize 224x224 (interpolasi sesuai `preprocessor_config.json`) -> rescale 1/255 -> normalisasi mu=sigma=0.5 oleh `AutoImageProcessor` masing-masing checkpoint".

---

## 5. Temuan Tinggi (klaim berlebih dan bertentangan dengan reviewer)

### T1. Abstrak dan Kesimpulan menyatakan generalisasi (R2 #10)
- Abstrak, butir Kesimpulan: *"membuktikan bahwa fusi fitur multi-domain menghasilkan representasi demografis yang tangguh dan tergeneralisasi dengan baik pada subjek baru"*. Dasarnya satu dataset, 120 subjek uji, **satu** pembagian hold-out (`train_test_split(random_state=42)`), tanpa pengulangan. Padahal R2 #10 meminta kesimpulan dibatasi pada DemogPairs. Abstrak tidak menyebut batas ini sama sekali.
- Abstrak menempatkan 93,70% (skema leak) **lebih dulu** dari 88,66%, sementara Intro P5 menetapkan subject-disjoint sebagai tolok ukur utama. Urutkan Primary dulu.
- **Saran**: ganti dengan "menunjukkan performa 88,66% pada 120 subjek held-out DemogPairs (tiga ras makro) dan penurunan 5,09 pp relatif terhadap pembagian dengan overlap identitas".

### T2. "Membuktikan ekuivalensi" dari p = 1,0000 (R2 #5)
Muncul di 0.A.3, Intro P6 butir 3 ("membuktikan ekuivalensi prediktif"), IV.B P3 butir 3 dan Tabel XIII ("Statistically Equivalent"), Conclusion butir 4 ("terbukti ekuivalen"). McNemar tidak signifikan **tidak membuktikan** ekuivalensi (perlu uji ekuivalensi dengan margin, misalnya TOST). Terlebih ada 71 citra diskordan (36/35). Itu hanya "**tidak ada perbedaan yang signifikan secara statistik**". Padahal R2 #5 persis menuntut kualifikasi seperti ini.

### T3. "Membuktikan saturasi fitur" dan keunggulan fusi (R2 #5)
- IV.B P1: "mengonfirmasi secara objektif kejenuhan"; IV.B P3: "membuktikan kejenuhan fitur pada SVM". p = 0,7343 hanya berarti **tidak terdeteksi peningkatan**, bukan bukti saturasi.
- Pemilihan pembanding: saturasi SVM hanya diuji terhadap `Emotion ⊕ Face`. Dihitung ulang dari JSON: **SVM Tri vs SVM `Face ⊕ Age` = 47/24, chi2 = 6,8169, p = 0,0086 (signifikan)**. Jadi "penambahan domain ketiga tidak membantu SVM" bergantung pada dual yang dipilih. Outline tidak menyebut ini.
- LR Dual (`Emotion ⊕ Face`) vs LR Face: 75/52, chi2 = 3,811, **p = 0,0505 (tidak signifikan)**. Narasi "fusi multi-domain unggul signifikan" hanya benar untuk **Tri vs Face** (Tabel XIII), bukan untuk semua fusi.
- Tidak ada koreksi perbandingan ganda (5+ uji McNemar). Sebutkan sebagai keterbatasan atau terapkan Holm.
- Pada RF dan GNB, tri-domain tidak lebih baik dari dual (RF: 85,00 vs 84,86; GNB: 83,61 vs 84,31). Aturan 0.B.2 mengharuskan hal ini diakui, tetapi **Conclusion P1 dan IV.A P5 tidak mencantumkannya**.
- Conclusion P1 butir 3: "Uji McNemar membuktikan keunggulan fusi multi-domain signifikan ($p<0,001$)" tanpa menyebut bahwa itu hanya terhadap Face tunggal dan bahwa Tri vs Dual pada SVM tidak signifikan. Ini mengulangi masalah yang dikritik R2 #5.

### T4. Klaim "Edge AI / ultra-lightweight / deployment-ready" tidak didukung (R2 #8)
Muncul di 0.A.4 (judul "Keunggulan Efisiensi Komputasi Ekstrem"), Intro P6 butir 4, IV.A P6, Conclusion butir 4.
- Latensi dan ukuran model yang diklaim hanya untuk **pengklasifikasi hilir**. Inferensi nyata membutuhkan **tiga ViT-Base (~86 juta parameter masing-masing)**. Ekstraksi tri-domain = **124,5 ms/citra pada RTX 4060** dan **~1.487 ms pada CPU** (angka outline sendiri). Latensi LR 0,0054 ms = <0,01% dari total. Ukuran model 0,11 MB mengabaikan ~1 GB bobot backbone.
- Tidak ada pengukuran pada perangkat tepi (mobile/Jetson/Raspberry Pi). "Edge AI" tidak terbukti.
- `latency_ms_per_sample` di JSON = waktu `predict` untuk 2.160 sampel dibagi 2.160 (batch teramortisasi), **bukan** latensi per-permintaan. Variasi antar-model tampak noise (LR Face 0,0008 ms vs LR Face⊕Age 0,0056 ms).
- **Saran**: ganti dengan "pengklasifikasi hilir LR ringan (0,11 MB) sehingga biaya inferensi didominasi ekstraksi ViT; evaluasi pada perangkat tepi merupakan pekerjaan lanjutan". Tambahkan total latensi end-to-end (ekstraksi + klasifikasi) pada Tabel XI.

### T5. Atribusi kausal fenotipik dan pencahayaan masih ada (R2 #9)
- IV.C P2 dan catatan mitigasi IV.C: disparitas "dipengaruhi oleh variasi fenotipik kraniofasial dan kontras pencahayaan". Tidak ada analisis pencahayaan atau fenotipe apa pun; ini klaim kausal tanpa bukti dan **bertentangan dengan aturan 0.B.3 dan IV.D P3**.
- Abstrak (Latar Belakang) dan Intro P1/P2 menyebut "tumpang tindih fenotipik" sebagai fakta. Ganti dengan formulasi "overlap representasi/confusion antar kelompok".
- Intro P5 menyebut tiga representasi "**ortogonal**" dan R2-1 roadmap memakai "sinergi fitur ortogonal". Tidak ada bukti ortogonalitas (korelasi atau CKA antar fitur belum dihitung). Ganti "komplementer" atau lampirkan analisis korelasi.
- IV.D P3 mengaitkan peran domain usia dengan reduksi kesalahan 185 -> 165 dan p = 0,0073 (**hanya LR**). Untuk SVM tidak ada peningkatan signifikan (lihat T3), sehingga pernyataan ini harus dibatasi "pada LR".

### T6. Klaim "membuktikan" lain (IV.A, IV.B)
- IV.A P3: "membuktikan efektivitas regularisasi L2" (tidak ada ablasi regularisasi).
- IV.A P5: "membuktikan ... representasi tangguh dan stabil baik pada model linier maupun non-linier".
- IV.B P2: "membuktikan ketahanan dan stabilitas generalisasi model linier teratur": degradasi LR (-4,07 pp) vs SVM (-5,09 pp) bukan selisih yang diuji, dan kedua nilai berasal dari protokol, himpunan uji, dan grid yang berbeda (lihat S3).
Ganti dengan "konsisten dengan" atau "mengindikasikan".

### T7. Kontrol untuk kebocoran tingkat backbone (R2 #2) tidak dibahas
`ViT-Face` (`skutaada/VIT-VGGFace`) di-fine-tune pada VGGFace2 (menurut outline). DemogPairs (Hupont & Fernandez, FG 2019) dibangun dari subset gambar VGGFace2 (perlu penulis konfirmasi dari makalah aslinya). Bila benar, identitas uji kemungkinan **sudah pernah dilihat backbone** saat fine-tuning, sehingga pembagian subject-disjoint di tingkat pengklasifikasi **tidak menjamin generalisasi ke subjek tak dikenal sama sekali**. Ini ancaman validitas yang harus diakui di Limitations (dan klaim "zero identity leakage" perlu dibatasi pada "antara set latih dan uji pengklasifikasi").

---

## 6. Temuan Sedang

**S1. Ketertelusuran angka latensi Tabel XI.** Angka outline untuk latensi tidak sama dengan JSON/notebook eksperimen terkini, padahal catatan Tabel XI mengklaim sumber `experiment/code/times/*.json` dan log:

| Model | Outline (Tabel XI) | `results/*.json` dan `md/` | Sumber outline |
|---|:---:|:---:|---|
| LR Tri | 0,0054 | **0,0046** | `README.ai.md` 7.1 |
| SVM Tri | 4,4481 | **4,6785** | `README.ai.md` 7.1 |
| RF Tri | 0,0537 | **0,0334** | `README.ai.md` 7.1 |
| GNB Dual | 0,0083 | **0,0088** | tidak jelas |

Waktu pelatihan, ukuran model, dan RAM sesuai. Perlu satu sumber kebenaran tunggal (pilih JSON terbaru). Selain itu:
- Rasio ">820x" dan "9,3x" dikonfounder: LR mencari 96 kombinasi, SVM 288 (3x lebih banyak, lihat K1); `SVC(probability=True)` di semua notebook memicu pencocokan Platt dengan CV internal 5-lipat (waktu latih SVM menggelembung); `n_jobs = 0.6 x cpu_count` dengan antrean eksekusi (`queue_execution_log.txt`, `run_remaining_queue.py`) sehingga waktu *wall-clock* bisa terkontaminasi proses paralel. Catat atau normalisasi sebelum menyatakan rasio.
- Ekstraksi: angka GPU (39,7/39,7/45,1 ms; total 22,4 menit) **benar** dari `times/*.json` (device `cuda`), angka CPU (467/476,7/543,1 ms; 4,46 jam) **benar** dari log notebook `1.1_vit-*.md` (device `cpu`). Namun fitur `.pkl` yang dipakai klasifikasi dibuat oleh satu jalur (CPU) dan pengukuran GPU dari jalur lain; sebutkan agar jelas tidak ada ketidakselarasan.

**S2. Metrik "RAM Footprint" (18,98 MB) hanya ukuran array uji float32** (2.160 x 2.304 x 4 byte / 2^20), bukan konsumsi memori (puncak RAM saat ekstraksi/pelatihan/inferensi atau VRAM). R2 #8 meminta "memory consumption". Tambahkan puncak RAM dan VRAM terukur atau ganti nama kolom menjadi "Test Feature Array Size".

**S3. Ablasi kebocoran (Tabel XII) memiliki konfounder.** Selisih 5,09 pp (SVM) / 4,07 pp (LR) diklaim murni "efek memorisasi identitas". Padahal protokol overlap dan disjoint berbeda dalam: himpunan citra uji (bukan citra yang sama), grid LR (270 vs 96; LR historis memilih `newton-cg` yang tidak ada di grid baru), satu seed pembagian, dan tidak ada CI/uji untuk Δ. Kata "membuktikan dan menguantifikasi" perlu diganti "konsisten dengan penurunan akibat hilangnya overlap identitas"; tambahkan CI untuk Δ atau minimal catatan konfounder. Catatan pelabelan: "593/600 subjects" menyesatkan, yang benar 593 dari 593 subjek uji (100%) ada di data latih (log `0.0_data_leakage_audit.md`).

**S4. R1 #6 (lebih banyak metode pembanding) lemah.** Bagian A Tabel XV hanya berisi 2 karya dari penulis yang sama (Putri et al.) ditambah baseline historis sendiri. Bagian B adalah ablasi internal. Tidak ada metode independen (Belcar, Sunitha, Liao, Kalkatawi, Tahyudin, Chen disebut di Related Works tetapi tidak diperbandingkan), tidak ada baseline CNN (ResNet/VGG/ArcFace features) atau ViT yang di-fine-tune end-to-end. Dengan `00_URUTAN_PRIORITAS_REVISI.md` Langkah 2.6 ("perluas baseline literatur lebih luas"), ini belum terpenuhi. Jika eksperimen baru tidak mungkin, minimal tambahkan tabel kontekstual kualitatif studi lain (angka yang dilaporkan, dataset, protokol) dengan label "tidak sebanding".

**S5. R2 #1 (novelty).** II.C P2 tanpa sitasi dan hanya menegaskan kerangka evaluasi. Tidak ada pembanding strategi fusi lain (misalnya penjumlahan terbobot, PCA gabungan, atau late fusion) yang menunjukkan konkatenasi tri-domain memang pilihan yang bermakna. Risiko tetap dipandang "sekadar konkatenasi". Opsional: ablasi singkat late-fusion (rata-rata probabilitas) menggunakan prediksi yang sudah ada.

**S6. Statistik inferensial mengabaikan klaster subjek.** 2.160 citra berasal dari hanya 120 subjek (18 citra/subjek). McNemar, Wilson CI (Eq. 22), dan CI 87,25-89,93% mengasumsikan sampel independen; korelasi dalam-subjek membuat CI terlalu sempit dan p terlalu kecil. Dihitung ulang: nilai Tabel XIII dan CI **benar secara aritmetika** (b, c, chi2, p, CI semuanya cocok persis), tetapi interpretasinya perlu catatan "diasumsikan independen; CI berbasis subjek (cluster bootstrap) akan lebih lebar".

**S7. Intro P1 dan P2 tidak memiliki sumber untuk klaim fakta** (evaluasi NIST, disparitas pada wanita berkulit gelap, praktik literatur memisah ras dan gender). Hanya P3 yang memiliki daftar sitasi. Tambahkan sitasi (mis. NIST FRVT demographics, Buolamwini & Gebru) agar tidak memicu komentar baru.

**S8. EOD.** Definisi Eq. 23 (maks - min recall lintas 6 kelompok) bukan EOD standar (selisih TPR antar kelompok sensitif). Beri nama "recall range" atau jelaskan penyesuaiannya. Tambahkan CI untuk 9,72 pp (hanya 20 subjek per kelompok). Verifikasi: nilai 94,44 - 84,72 = 9,72 pp benar dan identik untuk LR dan SVM.

---

## 7. Temuan Rendah (Inkonsistensi dan Pembulatan)

- **M1**. Intro: "700-850 kata" vs jumlah batas atas P1-P7 = 100+100+250+100+175+150+75 = **950** (minimum 745). Kurangi batas P3 (135-250) atau ubah klaim.
- **M2**. III.A P2 poin 1: pembagian 80/20 disebut memakai `StratifiedGroupKFold`. Kode `utils/dataset.py` memakai `train_test_split` per kelas pada daftar subjek terurut (`random_state=42`). `StratifiedGroupKFold` hanya dipakai untuk 5-fold CV di dalam set latih. Koreksi kalimat dan tegaskan **satu split tetap seed 42**.
- **M3**. "Python 3.10" (III.I) vs `README.md`/`README.ai.md` `conda create ... python=3.11`. Samakan dengan versi aktual.
- **M4**. Tabel XIII vs narasi pembulatan: SVM Tri vs Dual **+0,19 pp** (tabel, IV.B P3) vs **+0,18 pp** (IV.B P1); LR Tri vs Dual +1,20 pp (tabel, P3) vs +1,21 pp (P1). Pilih satu konvensi (selisih akurasi pembulatan dari akurasi vs dari jumlah citra).
- **M5**. IV.A P5: rata-rata SVM 86,47% - dihitung 86,477 (**86,48%** bila dibulatkan). LR 86,18, RF 80,57, GNB 78,37 benar.
- **M6**. IV.B P1: klaim SVM Face -> Dual +2,27 pp (p<0,001) **benar** (dihitung: 85/36, chi2 = 19,04, p = 9,8e-6), tetapi pasangan ini **tidak ada di Tabel XIII**. Tambahkan baris atau rujuk `3.1_statistical_significance.md`.
- **M7**. Tabel XIV: urutan baris SVM (Asian_Males sebelum Black_Males) berbeda dari LR. Seragamkan.
- **M8**. Roadmap `00_URUTAN_PRIORITAS_REVISI.md` Langkah 1.3 meminta kolom 95% CI di Tabel VII-X; outline sengaja menghapusnya (kembali 6 kolom, CI hanya di narasi untuk dua model puncak). Dokumentasikan keputusan ini di response letter agar tidak tampak melewatkan permintaan.
- **M9**. Response letter dan `Comments.md` merujuk "Tabel 12" dan p = 0,3057 (protokol overlap). Pemetaan ulang ke Tabel XII, XIII, XV dan penjelasan bahwa uji diulang pada protokol subject-disjoint (p = 0,7343) diperlukan (tidak ada di outline, wajar karena itu ranah response letter).
- **M10**. Aturan "maksimal 2 sitasi per kalimat" ditetapkan di tingkat paragraf. Kepatuhan per kalimat baru dapat dicek pada draf, bukan outline. Catat sebagai pemeriksaan pasca-penulisan.

---

## 8. Hal yang Telah Diverifikasi dan Benar

| Item | Hasil |
|---|---|
| Akurasi, presisi, recall, F1 Tabel VII, VIII, IX, X (28 model) | Semua **cocok** dengan JSON |
| Rata-rata akurasi lintas konfigurasi RF, GNB, LR | Cocok |
| Pola pilihan PCA (RF 5/7 PCA 0,75; GNB 7/7; LR 7/7 None; SVM 7/7 None) | Cocok dengan `best_parameters` |
| Wilson CI 88,66% [87,25; 89,93] dan 88,61% [87,20; 89,88] | Cocok persis |
| Tabel XIII: b/c, chi2 Edwards, p eksak binomial (5 baris) | Cocok persis (dihitung dari `y_pred`) |
| Tabel XIV: LR dan SVM per-subkelompok (P, R, F1, FNR) | Cocok dengan `classification_metrics` |
| EOD 9,72 pp (WM 94,44 vs BF 84,72) | Benar, identik di kedua model |
| Total kesalahan 294/271/245 dan dekomposisi 194/185/165 dll. | Benar |
| Tabel XI: waktu latih (54,78; 511,10; 110,47; 25,49 menit), ukuran model (0,11; 36,60; 6,19; 0,78 MB), ekstraksi GPU (124,5/79,4 ms), RAM (18,98/12,66 MB) | Cocok |
| Total 22,41 menit ekstraksi GPU; 4,46 jam CPU; rasio 11,9x | Cocok |
| Tabel I (480/120 subjek, 8.640/2.160 citra, 360 per kelas) | Konsisten dengan `dataset.py` |
| 18 citra per subjek, 100 subjek per kelas, 10.800 citra | Konsisten |
| Seluruh berkas gambar rujukan (`method.png`, `vit_v2.2.png`, `sample_*`, 3 `confusion_matrix_lr_*_v1.1.png`) | Ada; `vit_v2.2.png` sesuai tahap 1-7 di panduan narasi; PNG matriks tri benar |
| Grid RF (288), GNB (240), SVM (288) | Sesuai notebook |
| Penomoran Eq. 1-23, Fig. 1-4, Table I-XV berurutan | Konsisten di dalam outline |
| Rekonsiliasi aritmatika 288+270+288+240 = 1.086; x5 = 5.430; x7 = 38.010 | Benar **secara internal**, tetapi angka LR tidak sesuai eksperimen (K1) |

---

## 9. Rencana Perbaikan Terprioritas

| Prioritas | Tindakan | Terkait |
|:---:|---|---|
| **P1** | Perbaiki Tabel V dan seluruh total menjadi LR 96 / total 912 / 4.560 / **31.920** CV fits + 28 refit (atau jalankan ulang LR 270). Selaraskan README, README.ai, roadmap, tracking, response letter. Tambahkan catatan konfigurasi efektif unik SVM (168). | R2 #4, K1 |
| **P1** | Ganti tabel acuan matriks konfusi (a)-(c) dengan Bagian 4 K2; koreksi "(17)" menjadi "(14)" di IV.D P2. | R1 #4, K2 |
| **P1** | Hapus klaim MTCNN dan "[0,1]"; tulis prosedur pra-pemrosesan sesuai `AutoImageProcessor`. Verifikasi SHA checkpoint dan korpus fine-tuning dengan model card HF. | R2 #3, K3 |
| **P1** | Lunakkan seluruh "membuktikan/terbukti" (Abstrak, Intro P6, IV.A P3 dan P5, IV.B P1-P3, Tabel XIII, Conclusion). Ganti "ekuivalen" menjadi "tidak berbeda signifikan". Tambahkan kualifikasi saturasi SVM, RF/GNB dual >= tri, dan batas DemogPairs di Abstrak dan Conclusion P1. | R2 #5, #10, R1 #7 |
| **P1** | Hapus klaim "Edge AI / ultra-lightweight / deployment-ready". Tambahkan latensi end-to-end (ekstraksi + klasifikasi) dan ukuran backbone; cantumkan keterbatasan pengukuran. | R2 #8, T4 |
| **P1** | Hapus atribusi kausal fenotipik dan pencahayaan (IV.C P2, catatan mitigasi IV.C), "tumpang tindih fenotipik" di Abstrak/Intro P1, dan "ortogonal". | R2 #9, #6 |
| **P2** | Seragamkan sumber angka latensi (JSON terbaru); ganti atau tambah metrik memori sebenarnya; catat konfounder rasio latih (grid, `probability=True`, paralelisme). | R2 #8, S1, S2 |
| **P2** | Tambahkan catatan konfounder pada Tabel XII (grid, himpunan uji, seed) dan koreksi label "593/600". | R2 #2, S3 |
| **P2** | Tambahkan paragraf Limitations: satu split seed 42, 120 subjek uji, asumsi independensi vs klaster subjek, ancaman pra-pelatihan VGGFace2 vs DemogPairs, tanpa koreksi perbandingan ganda. | R2 #10, #2, #5 |
| **P2** | Perkuat R1 #6: tambah baseline eksternal yang direproduksi atau tabel kontekstual studi independen. | R1 #6, S4 |
| **P2** | Tambah sitasi untuk klaim fakta Intro P1-P2; selaraskan batas kata Intro dengan klaim "700-850". | R1 #1, S7, M1 |
| **P3** | Koreksi M2 (cara split), M3 (versi Python), M4-M7 (pembulatan, baris Tabel XIII/XIV). Pemetaan ulang response letter (M9). | M2-M9 |

---

## 10. Catatan Penutup

Pekerjaan outline v1.1 secara struktur dan sebagian besar data **sangat baik**: seluruh angka hasil empiris utama (Tabel VII-X, XIII, XIV, narasi IV.D) terverifikasi dari prediksi mentah. Masalah utama terkonsentrasi pada (1) satu tabel hyperparameter yang menyimpang dari kode, (2) tabel acuan yang salah label, (3) satu langkah pra-pemrosesan yang tidak ada, dan (4) pola diksi "membuktikan" yang berulang. Keempatnya dapat diperbaiki tanpa eksperimen baru (kecuali opsi menjalankan ulang LR 270 atau menambah baseline R1 #6).
