# Panduan Urutan Prioritas Eksekusi Revisi IEEE Access
**Manuskrip ID:** `Access-2026-50857`  
**Judul Manuskrip:** *Multi-Domain Vision Transformer Fusion for Intersectional Demographic Classification from Facial Images*  
**Status Editorial:** *Reject & Resubmit* (Tepat 1 Kesempatan Resubmission Biner)  
**Tujuan Dokumen:** Menentukan urutan kerja (*step-by-step priority sequence*) yang wajib didahulukan agar revisi berjalan efisien, terstruktur, dan tepat sasaran tanpa ada kekhawatiran reviewer yang terlewat.

---

## 🎯 Ringkasan Eksekutif Urutan Kerja

Berdasarkan analisis tingkat keparahan (*severity*) dan risiko penolakan permanen (*rejection risk*), pekerjaan revisi dibagi menjadi **3 Fase Utama**:

```
┌────────────────────────────────────────────────────────────────────────┐
│  FASE 1: PRIORITAS TERTINGGI (P1: MUST-FIX / BLOCKER AKSEPTASI)       │
│  "Fondasi Metodologi, Pembuktian Bebas Leakage, Signifikansi & Gambar" │
│  Estimasi: 4 - 5 Jam Kerja • Target: Menjawab Reviewer 2 & Reviewer 1 │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│  FASE 2: PRIORITAS MENENGAH (P2: SHOULD-FIX / PENGUATAN NARASI)        │
│  "Pemadatan Teks, Formulasi Matematika, Rincian Checkpoint & Diskusi" │
│  Estimasi: 3 - 4 Jam Kerja • Target: Memenuhi Standar Formal IEEE     │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│  FASE 3: PRIORITAS EDITORIAL & FINALISASI (P3: PACKAGING & SUBMIT)     │
│  "Sinkronisasi LaTeX, Highlighted PDF, Response Letter & Checklist"    │
│  Estimasi: 2 - 3 Jam Kerja • Target: Paket 3 Berkas Portal Atypon Rex │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 🚀 FASE 1: Prioritas P1 (Must-Fix — Wajib Didahulukan)

> [!CRITICAL]
> **Mengapa Ini Nomor 1?**  
> Komentar Reviewer 2 #2 (*Data Leakage*) dan #5 (*Statistical Interpretation*) adalah alasan utama manuskrip ini diputuskan *Reject & Resubmit*. Jika bagian ini tidak diselesaikan dengan data yang sahih, manuskrip akan langsung ditolak permanen pada kesempatan resubmission tunggal ini.

### Langkah 1.1: Pemutakhiran Metodologi Partisi Data (Bebas Kebocoran)
* **ID Komentar Terkait:** `R2-2`, `R1-5`
* **Berkas Naskah yang Diedit:** [`paper_v2/03_materials-and-methods_a-dataset.md`](../paper_v2/03_materials-and-methods_a-dataset.md)
* **Tindakan Konkret:**
  1. Jelaskan spesifikasi dataset DemogPairs: 10.800 citra, 600 identitas unik (100 identitas per kelas, 18 citra per identitas).
  2. Deklarasikan secara formal **Strict Subject-Disjoint Partitioning** sebagai tolok ukur utama: 480 subjek latih (8.640 citra) dan 120 subjek uji *held-out* (2.160 citra) dengan **0.00% kebocoran identitas**.
* **Sumber Data Rujukan:** [`experiment/code/md/3.0_compare.md`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/md/3.0_compare.md) dan modul [`utils/dataset.py`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/utils/dataset.py).

---

### Langkah 1.2: Perombakan Tabel Benchmark Utama & Penambahan Subbab Ablasi Kebocoran Data
* **ID Komentar Terkait:** `R2-2`
* **Berkas Naskah yang Diedit:** [`paper_v2/04_results-and-discussion_a-global-performance.md`](../paper_v2/04_results-and-discussion_a-global-performance.md)
* **Tindakan Konkret:**
  1. Ganti seluruh angka Tabel VII (RF), VIII (GNB), IX (LR), dan X (SVM) menggunakan hasil evaluasi *Subject-Disjoint* ($N = 2.160$). Puncak performa baru adalah **Logistic Regression Tri-Domain (88.66%)** dan **SVM Tri-Domain (88.61%)**.
  2. Tambahkan subbab baru di Section IV-B: **"Comparative Ablation Study on Data Leakage"** (Tabel XII). Tampilkan komparasi *Subject-Overlap* (93.70% SVM / 92.73% LR) vs *Subject-Disjoint* (88.61% SVM / 88.66% LR), yang menguantifikasi beban memorisasi identitas sebesar 5.09 percentage points pada SVM (dan 4.07 pp pada LR).
* **Sumber Data Rujukan:** Tabel komparasi di [`README.ai.md` Seksi 7.1 & 7.3](file:///D:/Research/face-race-gender-classification-using-multi-domain-vit/README.ai.md#71-leaderboard-utama-subject-disjoint-leaderboard-28-model).

---

### Langkah 1.3: Integrasi Hasil Uji Signifikansi Inferensial (Paired McNemar & 95% CI)
* **ID Komentar Terkait:** `R2-5`
* **Berkas Naskah yang Diedit:** [`paper_v2/04_results-and-discussion_a-global-performance.md`](../paper_v2/04_results-and-discussion_a-global-performance.md) & [`paper_v2/04_results-and-discussion_b-feature-ablation-study.md`](../paper_v2/04_results-and-discussion_b-feature-ablation-study.md)
* **Tindakan Konkret:**
  1. Cantumkan rentang **95% Wilson Score Confidence Interval** di dalam narasi pembahasan Tabel VII s.d. X.
  2. Paparkan hasil uji McNemar berpasangan pada **Tabel XIII**:
     * Fusi multi-domain terbukti unggul signifikan secara statistik dibanding biometrik wajah murni ($p = 3.46 \times 10^{-6} < 0.001$ pada SVM; $p = 6.78 \times 10^{-6} < 0.001$ pada LR).
     * Akurasi LR Tri (88.66%) dan SVM Tri (88.61%) menunjukkan **ketiadaan perbedaan performa prediktif yang signifikan secara statistik / paritas prediktif** ($p = 1.0000$, selisih bersih +1 citra: 1.915 vs 1.914).
     * Pada SVM non-linear, penambahan domain usia di atas `Emotion ⊕ Face` mengindikasikan **kejenuhan fitur asimtotik (*asymptotic feature saturation*)** ($p = 0.7343$, meskipun terhadap `Face ⊕ Age` 87.55% tetap signifikan pada $p = 0.0086$), sedangkan pada LR linear memberikan kenaikan signifikan ($p = 0.0073 < 0.01$).
* **Sumber Data Rujukan:** [`experiment/code/md/3.1_statistical_significance.md`](file:///D:/Research/face-race-gender-classification-using-multi-domain-vit/experiment/code/md/3.1_statistical_significance.md).

---

### Langkah 1.4: Penyusunan Tabel Profil Efisiensi Komputasi
* **ID Komentar Terkait:** `R2-8`, `R1-5`
* **Berkas Naskah yang Diedit:** [`paper_v2/04_results-and-discussion_a-global-performance.md`](../paper_v2/04_results-and-discussion_a-global-performance.md) (Paragraf 6, **Tabel XI**)
* **Tindakan Konkret:**
  1. Sajikan **Tabel XI** kuantitatif metrik komputasi:
     * Waktu ekstraksi fitur offline (10.800 citra): **124.5 ms/citra pada GPU RTX 4060** (39.7 ms Face + 39.7 ms Emotion + 45.1 ms Age; total 22.41 menit) vs **~1.487 ms/citra pada CPU baseline** (total 4.46 jam; akselerasi GPU 11.9×).
     * Durasi pelatihan 5-Fold GridSearchCV (31.920 CV fits): **LR Tri = 54.8 menit** vs **SVM Tri = 511.1 menit** (9.3× lebih cepat dilatih), RF Tri = 110.5 menit, GNB Dual = 25.5 menit.
     * Latensi inferensi kepala pengklasifikasi hilir per sampel: **LR = 0.0046 ms** (>1.000× lebih cepat; total *end-to-end* GPU $\approx 124.505\text{ ms/citra}$), **SVM = 4.6785 ms**, RF = 0.0334 ms, GNB Dual = 0.0088 ms.
     * Ukuran model tersimpan & RAM: **LR = 0.11 MB** (>330× lebih hemat), **SVM = 36.60 MB**, RF = 6.19 MB, GNB Dual = 0.78 MB (GNB Tri = 1.36 MB); jejak RAM array uji 18.98 MB (cache fitur 30.8 MB/domain).
  2. Kualifikasikan bahwa keunggulan `0.11 MB` dan `0.0046 ms` berada pada kepala pengklasifikasi hilir (*downstream classification head*), sementara deployment *end-to-end* pada *Edge AI* berdaya rendah diarahkan pada kuantisasi/distilasi ketiga backbone ViT.
* **Sumber Data Rujukan:** Berkas JSON di [`experiment/code/results/`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/results/) dan [`experiment/code/md/3.0_compare.md`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/md/3.0_compare.md).

---

### Langkah 1.5: Perancangan Ulang Gambar 3 (Diagram Arsitektur ViT Vektor)
* **ID Komentar Terkait:** `R1-3`, `R2-1`
* **Berkas Naskah yang Diedit:** [`paper_v2/images/vit_v2.2.png`](../paper_v2/images/vit_v2.2.png) & [`paper_v2/03_materials-and-methods_b-vision-transformer.md`](../paper_v2/03_materials-and-methods_b-vision-transformer.md)
* **Tindakan Konkret:**
  1. Hasilkan diagram arsitektur vektor resolusi tinggi (300+ DPI) yang memperlihatkan pemrosesan paralel 3 backbone ViT (`skutaada/VIT-VGGFace`, `dima806/facial_emotions...`, `dima806/facial_age...`), ekstraksi token `[CLS]` 768-d ($\mathbf{z}_L^0$), konkatenasi 2.304-d, dan pipeline GridSearchCV hilir.
  2. Perluas penjelasan di narasi Bab III-B mengenai sinergi fitur ortogonal (geometri kraniofasial + afektif dinamis + penuaan biologis).

---

### Langkah 1.6: Kalibrasi Klaim Keadilan Algoritmik (Fairness Scope)
* **ID Komentar Terkait:** `R2-6`
* **Berkas Naskah yang Diedit:** [`paper_v2/04_results-and-discussion_c-intersectional-subgroup-performance.md`](../paper_v2/04_results-and-discussion_c-intersectional-subgroup-performance.md)
* **Tindakan Konkret:**
  1. Perbarui metrik per subkelompok pada partisi *Subject-Disjoint* (White Males 94.44% s.d. Black Females 84.72%).
  2. Nyatakan nilai *Equal Opportunity Difference* ($\Delta\text{TPR} = 9.72\text{ pp}$) sebagai indikator disparitas performa subkelompok, dan tegaskan bahwa ini **bukan audit keadilan algoritmik universal**.

---

## 📝 FASE 2: Prioritas P2 (Should-Fix — Penguatan Narasi & Struktur)

> [!NOTE]
> Setelah data empiris dan gambar arsitektur pada Fase 1 diperbarui, Fase 2 berfokus pada penyempurnaan alur naskah, formulasi matematis, dan pemenuhan seluruh permintaan klarifikasi penelaah.

### Langkah 2.1: Pemadatan Narasi Bab I (Introduction)
* **ID Komentar Terkait:** `R1-1`, `R2-1`
* **Berkas Naskah:** [`paper_v2/01_introduction.md`](../paper_v2/01_introduction.md)
* **Tindakan:** Kurangi pembahasan demografi umum yang bertele-tele sebesar ~25-30%. Langsung fokus pada kompleksitas interseksionalitas ras-gender dan batasi kontribusi menjadi 4 butir deklarasi ilmiah padat di akhir bab.

### Langkah 2.2: Restrukturisasi Bab II & Formulasi Matematika Formal
* **ID Komentar Terkait:** `R1-2`
* **Berkas Naskah:** [`paper_v2/02_related-works.md`](../paper_v2/02_related-works.md)
* **Tindakan:** Bagi tinjauan pustaka ke dalam 3 tema terstruktur: *(A) Estimasi Atribut Demografis Wajah*, *(B) Vision Transformers dalam Analisis Wajah*, dan *(C) Fusi Representasi Multi-Domain*. Sisipkan persamaan matematis proyeksi patch $\mathbf{x}_p$, mekanisme MHSA, dan fusi konkatenasi $\mathbf{z}_{\text{tri}} \in \mathbb{R}^{2304}$.

### Langkah 2.3: Dokumentasi Checkpoint HuggingFace & Reproduktibilitas
* **ID Komentar Terkait:** `R2-3`
* **Berkas Naskah:** [`paper_v2/03_materials-and-methods_b-vision-transformer.md`](../paper_v2/03_materials-and-methods_b-vision-transformer.md)
* **Tindakan:** Dokumentasikan parameter prapemrosesan secara presisi: ID resmi checkpoint HuggingFace beserta Git commit SHA (`skutaada/VIT-VGGFace` [`e85f0c9`], `dima806/facial_emotions_image_detection` [`747cf16`], `dima806/facial_age_image_detection` [`ad35933`]), resolusi input $224 \times 224$ dari citra *pre-cropped* tanpa MTCNN, rescale $1/255$ dan normalisasi seragam $\mu = \sigma = [0.5, 0.5, 0.5]$ ke $[-1, 1]$, serta formulasi penarikan token `[CLS]` dari lapisan ke-12 ($\mathbf{z}_L^0$).

### Langkah 2.4: Rekonsiliasi Ruang Pencarian Hyperparameter
* **ID Komentar Terkait:** `R2-4`
* **Berkas Naskah:** [`paper_v2/03_materials-and-methods_g-classification-pipeline.md`](../paper_v2/03_materials-and-methods_g-classification-pipeline.md)
* **Tindakan:** Selaraskan narasi dan Tabel III–VI ruang pencarian hyperparameter: RF 288 + GNB 240 + LR 96 + SVM 288 (108 konfigurasi unik efektif) = **912 kombinasi** $\times$ 5 folds $\times$ 7 skema fitur = **31.920 CV fits** + 28 refits akhir.

### Langkah 2.5: Pendalaman Analisis Matriks Konfusi 6×6 & Pola Error (Figure 4)
* **ID Komentar Terkait:** `R1-4`, `R2-9`
* **Berkas Naskah:** [`paper_v2/04_results-and-discussion_d-error-pattern-assessment.md`](../paper_v2/04_results-and-discussion_d-error-pattern-assessment.md)
* **Tindakan:** Bahas dekomposisi kuantitatif kesalahan pada matriks konfusi 6×6 ($N=2.160$, 245 error pada LR Tri-Domain): kesalahan didominasi oleh kekeliruan antar-ras dalam gender yang sama (**165 citra / 67.3% dari total error; 7.64% dari $N$**), sedangkan kesalahan lintas-gender berjumlah **80 citra (32.7% dari total error; 3.70% dari $N$)**. Hilangkan spekulasi kausal fenotipik biologis dan pencahayaan; batasi murni pada data distribusi frekuensi matriks konfusi.

### Langkah 2.6: Perluasan Komparasi Literatur Baseline
* **ID Komentar Terkait:** `R1-6`, `R2-7`
* **Berkas Naskah:** [`paper_v2/04_results-and-discussion_e-comparison-with-prior-studies.md`](../paper_v2/04_results-and-discussion_e-comparison-with-prior-studies.md)
* **Tindakan:** Sajikan **Tabel XV** dengan memisahkan kelompok protokol **Stratified** untuk studi terdahulu (Putri et al. 2025) dan kelompok protokol **Subject-Disjoint** untuk baseline internal pada partisi bebas kebocoran yang identik.

### Langkah 2.7: Revisi Bab Kesimpulan & Delimitasi Batasan Studi
* **ID Komentar Terkait:** `R1-7`, `R2-10`
* **Berkas Naskah:** [`paper_v2/05_conclusion.md`](../paper_v2/05_conclusion.md)
* **Tindakan:** Tulis ulang kesimpulan secara padat; soroti temuan utama (LR 88.66% / SVM 88.61% bebas kebocoran, efisiensi LR untuk edge computing), dan batasi kesimpulan secara eksplisit hanya pada 3 ras makro DemogPairs serta perlunya validasi dataset eksternal di masa depan.

---

## 📦 FASE 3: Prioritas P3 (Editorial, Paket LaTeX & Resubmission)

> [!IMPORTANT]
> Fase ini memastikan naskah bersih, berkas tanggapan tersusun rapi, dan seluruh dokumen administratif siap diunggah ke portal resmi IEEE Access.

### Langkah 3.1: Sinkronisasi ke Paket LaTeX Siap-Submit
* **Direktori Terkait:** [`paper_latex_en/`](../paper_latex_en/)
* **Tindakan:** Sinkronisasikan seluruh teks baru dari `paper_v2/*.md` ke berkas `sections/*.tex` dan `access.tex`. Kompilasi ulang menggunakan `pdflatex` dan `bibtex` hingga menghasilkan `access.pdf` dua kolom yang rapi tanpa galat.

### Langkah 3.2: Pembangkitan Manuskrip Tersorot (Highlighted PDF)
* **Target Berkas:** `Access-2026-50857_Highlighted-Revision.pdf`
* **Tindakan:** Buat versi PDF di mana seluruh teks tambahan, perubahan tabel, dan persamaan baru ditandai dengan warna sorotan kuning (*yellow highlight tool*) untuk mempermudah pelacakan oleh Reviewer dan Associate Editor.

### Langkah 3.3: Finalisasi Dokumen Tanggapan Penelaah (Response to Reviewers)
* **Berkas Rujukan:** [`paper_reviews_ieee/10_response_letter_skeleton.md`](file:///D:/Research/face-race-gender-multi-vit/paper_reviews_ieee/10_response_letter_skeleton.md)
* **Tindakan:** Perbarui nomor halaman, kolom, nomor baris, dan nomor tabel aktual hasil kompilasi PDF ke dalam berkas tanggapan resmi (format DOCX atau PDF).

### Langkah 3.4: Finalisasi Dokumen Administratif
* **Formulir Byline Change:** [`paper_reviews_ieee/Request-for-Byline-Change.md`](file:///D:/Research/face-race-gender-multi-vit/paper_reviews_ieee/Request-for-Byline-Change.md) (penambahan Dr. Shukor Sanim Mohd Fauzi).
* **Checklist Kepatuhan 10-Butir:** [`paper_reviews_ieee/Resubmission-Checklist.md`](file:///D:/Research/face-race-gender-multi-vit/paper_reviews_ieee/Resubmission-Checklist.md).

---

## 📊 Matriks Rangkuman Cepat Urutan Pengerjaan

| Urutan | Prioritas | Butir Isu | Berkas Naskah Target | Data Acuan di Repositori | Kesiapan Data |
|:---:|:---:|:---|:---|:---|:---:|
| **1** | **P1** | R2-2, R1-5 | `paper_v2/03_materials-and-methods_a-dataset.md` | `experiment/code/utils/dataset.py` | ✅ 100% Siap |
| **2** | **P1** | R2-2 | `paper_v2/04_results-and-discussion_a-global-performance.md` | `README.ai.md` Seksi 7.1 & 7.3 | ✅ 100% Siap |
| **3** | **P1** | R2-5 | `paper_v2/04_results-and-discussion_a-global-performance.md` | `experiment/code/md/3.1_statistical_significance.md` | ✅ 100% Siap |
| **4** | **P1** | R2-8, R1-5 | `paper_v2/04_results-and-discussion` (Subseksi Komputasi) | `experiment/code/md/3.0_compare.md` | ✅ 100% Siap |
| **5** | **P1** | R1-3, R2-1 | `paper_v2/images/vit_v2.2.png` & `03_..._b-vision-transformer.md` | `images/` & skrip diagram | 🎨 Siap Gambar |
| **6** | **P1** | R2-6 | `paper_v2/04_results-and-discussion_c-intersectional...md` | `experiment/code/md/3.1_statistical_significance.md` | ✅ 100% Siap |
| **7** | **P2** | R1-1, R2-1 | `paper_v2/01_introduction.md` | `paper_reviews_ieee/08_revision_roadmap.md` | 📝 Siap Edit |
| **8** | **P2** | R1-2 | `paper_v2/02_related-works.md` | Formulasi matematis MHSA & fusi | 📝 Siap Edit |
| **9** | **P2** | R2-3 | `paper_v2/03_materials-and-methods_b-vision-transformer.md` | `README.ai.md` Seksi 3.1-3.2 | ✅ 100% Siap |
| **10** | **P2** | R2-4 | `paper_v2/03_materials-and-methods_g-classification...md` | `README.ai.md` Seksi 6.2-6.3 | ✅ 100% Siap |
| **11** | **P2** | R1-4, R2-9 | `paper_v2/04_results-and-discussion_d-error-pattern...md` | Matriks konfusi 6×6 di `results/` | ✅ 100% Siap |
| **12** | **P2** | R1-6, R2-7 | `paper_v2/04_results-and-discussion_e-comparison...md` | `README.ai.md` Seksi 9.1 | ✅ 100% Siap |
| **13** | **P2** | R1-7, R2-10 | `paper_v2/05_conclusion.md` | `README.ai.md` Seksi 15 & 16 | 📝 Siap Edit |
| **14** | **P3** | AE-1 s.d. AE-4 | `paper_latex_en/` & berkas submission | `paper_reviews_ieee/10_response_letter_skeleton.md` | 📦 Siap Sinkron |
