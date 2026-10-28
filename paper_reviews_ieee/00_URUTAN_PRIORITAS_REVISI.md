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
* **Berkas Naskah yang Diedit:** [`paper/03_materials-and-methods_a-dataset.md`](file:///D:/Research/face-race-gender-multi-vit/paper/03_materials-and-methods_a-dataset.md)
* **Tindakan Konkret:**
  1. Jelaskan spesifikasi dataset DemogPairs: 10.800 citra, 600 identitas unik (100 identitas per kelas, 18 citra per identitas).
  2. Deklarasikan secara formal **Strict Subject-Disjoint Partitioning** sebagai tolok ukur utama: 480 subjek latih (8.640 citra) dan 120 subjek uji *held-out* (2.160 citra) dengan **0.00% kebocoran identitas**.
* **Sumber Data Rujukan:** [`experiment/code/md/3.0_compare.md`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/md/3.0_compare.md) dan modul [`utils/dataset.py`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/utils/dataset.py).

---

### Langkah 1.2: Perombakan Tabel Benchmark Utama & Penambahan Subbab Ablasi Kebocoran Data
* **ID Komentar Terkait:** `R2-2`
* **Berkas Naskah yang Diedit:** [`paper/04_results-and-discussion_a-global-performance.md`](file:///D:/Research/face-race-gender-multi-vit/paper/04_results-and-discussion_a-global-performance.md)
* **Tindakan Konkret:**
  1. Ganti seluruh angka Tabel VII (RF), VIII (GNB), IX (LR), dan X (SVM) menggunakan hasil evaluasi *Subject-Disjoint* ($N = 2.160$). Puncak performa baru adalah **Logistic Regression Tri-Domain (88.66%)** dan **SVM Tri-Domain (88.61%)**.
  2. Tambahkan subbab baru: **"Comparative Ablation Study on Data Leakage"** (Tabel XI baru). Tampilkan komparasi *Subject-Overlap* (93.70%) vs *Subject-Disjoint* (88.61%), yang membuktikan dan menguantifikasi beban memorisasi identitas sebesar 5.09 percentage points.
* **Sumber Data Rujukan:** Tabel komparasi di [`README.ai.md` Seksi 7.1 & 7.3](file:///D:/Research/face-race-gender-multi-vit/README.ai.md#71-leaderboard-utama-subject-disjoint-leaderboard-28-model).

---

### Langkah 1.3: Integrasi Hasil Uji Signifikansi Inferensial (Paired McNemar & 95% CI)
* **ID Komentar Terkait:** `R2-5`
* **Berkas Naskah yang Diedit:** [`paper/04_results-and-discussion_a-global-performance.md`](file:///D:/Research/face-race-gender-multi-vit/paper/04_results-and-discussion_a-global-performance.md) & [`paper/04_results-and-discussion_b-feature-ablation-study.md`](file:///D:/Research/face-race-gender-multi-vit/paper/04_results-and-discussion_b-feature-ablation-study.md)
* **Tindakan Konkret:**
  1. Tambahkan kolom rentang **95% Wilson Score Confidence Interval** pada Tabel VII s.d. X.
  2. Paparkan hasil uji McNemar berpasangan:
     * Fusi multi-domain terbukti unggul signifikan secara statistik dibanding biometrik wajah murni ($p = 3.46 \times 10^{-6} < 0.001$ pada SVM; $p = 6.78 \times 10^{-6} < 0.001$ pada LR).
     * Akurasi LR Tri (88.66%) dan SVM Tri (88.61%) terbukti **setara secara statistik** ($p = 1.0000$, selisih bersih +1 citra).
     * Pada SVM non-linear, penambahan domain usia mengalami **kejenuhan fitur asimtotik (*asymptotic feature saturation*)** ($p = 0.7343$), sedangkan pada LR linear memberikan kenaikan signifikan ($p = 0.0073 < 0.01$).
* **Sumber Data Rujukan:** [`experiment/code/md/3.1_statistical_significance.md`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/md/3.1_statistical_significance.md).

---

### Langkah 1.4: Penyusunan Tabel Profil Efisiensi Komputasi
* **ID Komentar Terkait:** `R2-8`, `R1-5`
* **Berkas Naskah yang Diedit:** [`paper/04_results-and-discussion_a-global-performance.md`](file:///D:/Research/face-race-gender-multi-vit/paper/04_results-and-discussion_a-global-performance.md) (subseksi komputasi)
* **Tindakan Konkret:**
  1. Sajikan tabel kuantitatif metrik komputasi:
     * Waktu ekstraksi fitur per domain: ~15.2 ms/citra pada GPU (~45.6 ms untuk fusi tri-domain).
     * Latensi inferensi per sampel: **LR = 0.0054 ms** (sangat cepat), **SVM = 4.4481 ms**, RF = 0.0537 ms, GNB = 0.0081 ms.
     * Ukuran model tersimpan: **LR = 0.11 MB** (>330× lebih hemat), **SVM = 36.60 MB**, RF = 6.19 MB, GNB = 1.36 MB.
  2. Tekankan argumen bahwa Logistic Regression merupakan model paling unggul untuk implementasi komputasi tepi (*edge computing / mobile AI*).
* **Sumber Data Rujukan:** Berkas JSON di [`experiment/code/results/`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/results/) dan [`experiment/code/md/3.0_compare.md`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/md/3.0_compare.md).

---

### Langkah 1.5: Perancangan Ulang Gambar 3 (Diagram Arsitektur ViT Vektor)
* **ID Komentar Terkait:** `R1-3`, `R2-1`
* **Berkas Naskah yang Diedit:** [`paper/images/vit.png`](file:///D:/Research/face-race-gender-multi-vit/paper/images/) & [`paper/03_materials-and-methods_b-vision-transformer.md`](file:///D:/Research/face-race-gender-multi-vit/paper/03_materials-and-methods_b-vision-transformer.md)
* **Tindakan Konkret:**
  1. Hasilkan diagram arsitektur vektor resolusi tinggi (300+ DPI) yang memperlihatkan pemrosesan paralel 3 backbone ViT (`skutaada/VIT-VGGFace`, `dima806/facial_emotions...`, `dima806/facial_age...`), ekstraksi token `[CLS]` 768-d ($\mathbf{z}_L^0$), konkatenasi 2.304-d, dan pipeline GridSearchCV hilir.
  2. Perluas penjelasan di narasi Bab III-B mengenai sinergi fitur ortogonal (geometri kraniofasial + afektif dinamis + penuaan biologis).

---

### Langkah 1.6: Kalibrasi Klaim Keadilan Algoritmik (Fairness Scope)
* **ID Komentar Terkait:** `R2-6`
* **Berkas Naskah yang Diedit:** [`paper/04_results-and-discussion_c-intersectional-subgroup-performance.md`](file:///D:/Research/face-race-gender-multi-vit/paper/04_results-and-discussion_c-intersectional-subgroup-performance.md)
* **Tindakan Konkret:**
  1. Perbarui metrik per subkelompok pada partisi *Subject-Disjoint* (White Males 94.44% s.d. Black Females 84.72%).
  2. Nyatakan nilai *Equal Opportunity Difference* ($\Delta\text{TPR} = 9.72\text{ pp}$) sebagai indikator disparitas performa subkelompok, dan tegaskan bahwa ini **bukan audit keadilan algoritmik universal**.

---

## 📝 FASE 2: Prioritas P2 (Should-Fix — Penguatan Narasi & Struktur)

> [!NOTE]
> Setelah data empiris dan gambar arsitektur pada Fase 1 diperbarui, Fase 2 berfokus pada penyempurnaan alur naskah, formulasi matematis, dan pemenuhan seluruh permintaan klarifikasi penelaah.

### Langkah 2.1: Pemadatan Narasi Bab I (Introduction)
* **ID Komentar Terkait:** `R1-1`, `R2-1`
* **Berkas Naskah:** [`paper/01_introduction.md`](file:///D:/Research/face-race-gender-multi-vit/paper/01_introduction.md)
* **Tindakan:** Kurangi pembahasan demografi umum yang bertele-tele sebesar ~25-30%. Langsung fokus pada kompleksitas interseksionalitas ras-gender dan batasi kontribusi menjadi 4 butir deklarasi ilmiah padat di akhir bab.

### Langkah 2.2: Restrukturisasi Bab II & Formulasi Matematika Formal
* **ID Komentar Terkait:** `R1-2`
* **Berkas Naskah:** [`paper/02_related-works.md`](file:///D:/Research/face-race-gender-multi-vit/paper/02_related-works.md)
* **Tindakan:** Bagi tinjauan pustaka ke dalam 3 tema terstruktur: *(A) Estimasi Atribut Demografis Wajah*, *(B) Vision Transformers dalam Analisis Wajah*, dan *(C) Fusi Representasi Multi-Domain*. Sisipkan persamaan matematis proyeksi patch $\mathbf{x}_p$, mekanisme MHSA, dan fusi konkatenasi $\mathbf{z}_{\text{tri}} \in \mathbb{R}^{2304}$.

### Langkah 2.3: Dokumentasi Checkpoint HuggingFace & Reproduktibilitas
* **ID Komentar Terkait:** `R2-3`
* **Berkas Naskah:** [`paper/03_materials-and-methods_b-vision-transformer.md`](file:///D:/Research/face-race-gender-multi-vit/paper/03_materials-and-methods_b-vision-transformer.md)
* **Tindakan:** Buat tabel ringkasan parameter prapemrosesan: ID resmi checkpoint HuggingFace, resolusi input $224 \times 224$, nilai mean dan standard deviation normalisasi tiap kanal, serta formulasi penarikan token `[CLS]` dari lapisan ke-12 ($\mathbf{z}_L^0$).

### Langkah 2.4: Rekonsiliasi Ruang Pencarian Hyperparameter
* **ID Komentar Terkait:** `R2-4`
* **Berkas Naskah:** [`paper/03_materials-and-methods_g-classification-pipeline.md`](file:///D:/Research/face-race-gender-multi-vit/paper/03_materials-and-methods_g-classification-pipeline.md)
* **Tindakan:** Selaraskan narasi ruang pencarian hyperparameter: SVM 288 + LR 270 + RF 288 + GNB 240 = 1.086 kombinasi $\times$ 5 folds $\times$ 7 skema fitur = **38.010 CV fits** + 28 refits akhir.

### Langkah 2.5: Pendalaman Analisis Matriks Konfusi 6×6 & Pola Error (Figure 4)
* **ID Komentar Terkait:** `R1-4`, `R2-9`
* **Berkas Naskah:** [`paper/04_results-and-discussion_d-error-pattern-assessment.md`](file:///D:/Research/face-race-gender-multi-vit/paper/04_results-and-discussion_d-error-pattern-assessment.md)
* **Tindakan:** Bahas asimetri kesalahan pada matriks konfusi 6×6. Tunjukkan bahwa kesalahan mayoritas terjadi antar-ras dalam gender yang sama (*same-gender cross-race*), sedangkan kesalahan gender mendekati 0%. Hilangkan spekulasi fenotipik biologis yang berlebihan; batasi murni pada data distribusi matriks konfusi.

### Langkah 2.6: Perluasan Komparasi Literatur Baseline
* **ID Komentar Terkait:** `R1-6`, `R2-7`
* **Berkas Naskah:** [`paper/04_results-and-discussion_e-comparison-with-prior-studies.md`](file:///D:/Research/face-race-gender-multi-vit/paper/04_results-and-discussion_e-comparison-with-prior-studies.md)
* **Tindakan:** Perluas Tabel XII dengan menambahkan baseline literatur lebih luas. Beri catatan kaki/penjelasan eksplisit bahwa studi terdahulu (seperti Putri et al. 2025) menggunakan partisi *image-level overlap*, sehingga komparasi ini disajikan secara **kontekstual**, bukan sebagai tolok ukur terkontrol (*controlled benchmark*).

### Langkah 2.7: Revisi Bab Kesimpulan & Delimitasi Batasan Studi
* **ID Komentar Terkait:** `R1-7`, `R2-10`
* **Berkas Naskah:** [`paper/05_conclusion.md`](file:///D:/Research/face-race-gender-multi-vit/paper/05_conclusion.md)
* **Tindakan:** Tulis ulang kesimpulan secara padat; soroti temuan utama (LR 88.66% / SVM 88.61% bebas kebocoran, efisiensi LR untuk edge computing), dan batasi kesimpulan secara eksplisit hanya pada 3 ras makro DemogPairs serta perlunya validasi dataset eksternal di masa depan.

---

## 📦 FASE 3: Prioritas P3 (Editorial, Paket LaTeX & Resubmission)

> [!IMPORTANT]
> Fase ini memastikan naskah bersih, berkas tanggapan tersusun rapi, dan seluruh dokumen administratif siap diunggah ke portal resmi IEEE Access.

### Langkah 3.1: Sinkronisasi ke Paket LaTeX Siap-Submit
* **Direktori Terkait:** [`paper_latex_en/`](file:///D:/Research/face-race-gender-multi-vit/paper_latex_en/)
* **Tindakan:** Sinkronisasikan seluruh teks baru dari `paper/*.md` ke berkas `sections/*.tex` dan `access.tex`. Kompilasi ulang menggunakan `pdflatex` dan `bibtex` hingga menghasilkan `access.pdf` dua kolom yang rapi tanpa galat.

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
| **1** | **P1** | R2-2, R1-5 | `paper/03_materials-and-methods_a-dataset.md` | `experiment/code/utils/dataset.py` | ✅ 100% Siap |
| **2** | **P1** | R2-2 | `paper/04_results-and-discussion_a-global-performance.md` | `README.ai.md` Seksi 7.1 & 7.3 | ✅ 100% Siap |
| **3** | **P1** | R2-5 | `paper/04_results-and-discussion_a-global-performance.md` | `experiment/code/md/3.1_statistical_significance.md` | ✅ 100% Siap |
| **4** | **P1** | R2-8, R1-5 | `paper/04_results-and-discussion` (Subseksi Komputasi) | `experiment/code/md/3.0_compare.md` | ✅ 100% Siap |
| **5** | **P1** | R1-3, R2-1 | `paper/images/vit.png` & `03_..._b-vision-transformer.md` | `images/` & skrip diagram | 🎨 Siap Gambar |
| **6** | **P1** | R2-6 | `paper/04_results-and-discussion_c-intersectional...md` | `experiment/code/md/3.1_statistical_significance.md` | ✅ 100% Siap |
| **7** | **P2** | R1-1, R2-1 | `paper/01_introduction.md` | `paper_reviews_ieee/08_revision_roadmap.md` | 📝 Siap Edit |
| **8** | **P2** | R1-2 | `paper/02_related-works.md` | Formulasi matematis MHSA & fusi | 📝 Siap Edit |
| **9** | **P2** | R2-3 | `paper/03_materials-and-methods_b-vision-transformer.md` | `README.ai.md` Seksi 3.1-3.2 | ✅ 100% Siap |
| **10** | **P2** | R2-4 | `paper/03_materials-and-methods_g-classification...md` | `README.ai.md` Seksi 6.2-6.3 | ✅ 100% Siap |
| **11** | **P2** | R1-4, R2-9 | `paper/04_results-and-discussion_d-error-pattern...md` | Matriks konfusi 6×6 di `results/` | ✅ 100% Siap |
| **12** | **P2** | R1-6, R2-7 | `paper/04_results-and-discussion_e-comparison...md` | `README.ai.md` Seksi 9.1 | ✅ 100% Siap |
| **13** | **P2** | R1-7, R2-10 | `paper/05_conclusion.md` | `README.ai.md` Seksi 15 & 16 | 📝 Siap Edit |
| **14** | **P3** | AE-1 s.d. AE-4 | `paper_latex_en/` & berkas submission | `paper_reviews_ieee/10_response_letter_skeleton.md` | 📦 Siap Sinkron |
