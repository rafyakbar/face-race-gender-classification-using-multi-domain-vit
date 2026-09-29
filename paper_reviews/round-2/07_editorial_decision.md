# Surat Keputusan Editorial Putaran 2 (Editorial Decision Letter — Round 2)

**Kepada:**  
Dr. Ir. Ricky Eka Putra, S.Kom., M.Kom., Rezky Arisanti Putri, S.Kom., M.Kom., Dr. Yuni Yamasari, S.Kom., M.Kom., Rafy Aulia Akbar, S.Kom., M.Kom.  
Departemen Informatika, Fakultas Teknik, Universitas Negeri Surabaya  

**Perihal:** Keputusan Hasil Penelaahan Putaran Kedua (*Round 2 Re-Review Verification*)  
**Judul Naskah:** *Multi-Domain Vision Transformer Fusion for Intersectional Demographic Classification from Facial Images*  
**Jurnal Sasaran:** *IEEE Access* (Kategori: Regular Paper)  
**ID Naskah:** IEEE-ACCESS-2026-MOCK-R2  
**Tanggal Keputusan:** 28 September 2026  
**Penilai Independen:** Editor-in-Chief (EIC), Reviewer 1 (Methodology), Reviewer 2 (Domain Expert), Reviewer 3 (Cross-Perspective), Devil's Advocate (Adversarial Evaluator)

---

## I. Keputusan Akhir Editorial (Official Editorial Decision)

Berdasarkan evaluasi menyeluruh terhadap berkas naskah terevisi pada direktori `paper/`, surat tanggapan butir-per-butir (`09_response_letter.md`), serta laporan verifikasi ketertelusuran komitmen (*R&R Traceability Matrix*), dewan editor dengan bangga menyampaikan keputusan penelaahan Putaran Kedua:

### **STATUS KEPUTUSAN: ACCEPT (DITERIMA SECARA ILMIAH)**
*(Memenuhi Ambang Batas Standar Publikasi IEEE Access — Siap Melangkah ke Tahap Penerjemahan Bahasa Inggris & Pemformatan Akhir)*

---

## II. Dasar Pertimbangan Keputusan (Decision Rationale — Schema 13 F0)

Keputusan ini didasarkan pada penerapan mesin keputusan deterministik Schema 13 dan protokol verifikasi re-review multi-putaran:

1. **Pemenuhan Komitmen Prioritas Penuh**:
   - Seluruh 4 komitmen **Priority 1 (Must Fix / Blocker)** telah terselesaikan secara tuntas dan jujur (100% kepatuhan substantif).
   - Seluruh 6 komitmen **Priority 2 (Should Fix / Major)** telah terpenuhi secara penuh (100%).
   - Seluruh 12 komitmen **Priority 3 (Nice to Fix / Minor)** telah terpenuhi atau dijustifikasi secara ilmiah yang sah (100%).
2. **Kenaikan Status Seluruh 6 Dimensi Akseptasi (D1–D6 = `PASS`)**:
   - `D1` (Methodology Rigor): **`PASS`** (Hambatan signifikansi statistik dan validasi silang terselesaikan tuntas melalui uji McNemar, Wilson 95% CI, dan skor fold CV).
   - `D2` (Domain Accuracy): **`PASS`** (Silsilah checkpoint HuggingFace transparan, landasan kognitif dual-stream Bruce & Young/Haxby terpasang rapi).
   - `D3` (Argumentative Coherence): **`PASS`** (DA CRITICAL paradoks Tri-Domain teradjudikasi; klaim terkalibrasi menjadi *classifier-dependent*; regresi RF dijelaskan via *curse of dimensionality*).
   - `D4` (Cross-Disciplinary Relevance): **`PASS`** (Metrik keadilan formal $\Delta\text{TPR} = 7.50\%$ dihitung, transparansi disparitas fenotipik Black Females, dan statuta etika lengkap).
   - `D5` (Writing & Structure Hygiene): **`PASS`** (Struktur 3 poin kontribusi padat; interpretasi mekanistik batas keputusan diperdalam).
   - `D6` (Venue Fit & Contribution): **`PASS`** (Distingsi kebaruan naskah terhadap prosiding ICVEE 2025 tegas; tiga statuta wajib IEEE Access terpenuhi).
3. **Kondisi F0 Terpicu**: Tidak ada dimensi mandatory yang berstatus `warn`, `block`, atau `fatal`, dan seluruh isu kritis Devil's Advocate telah diadjudikasi tuntas (**`RESOLVED`**).
4. **Bebas Cacat Fatal Baru (*Zero New Defects*)**: Tidak terdeteksi kebocoran data (*data leakage*), manipulasi angka empiris, ataupun inkonsistensi matematis baru.

---

## III. Matriks Perbandingan Status Dimensi Lintas Putaran

| Dimensi Akseptasi | Bobot Evaluasi | Status Putaran 1 (R1) | Status Putaran 2 (R2) | Perubahan Evaluasi |
|---|:---:|:---:|:---:|:---:|
| **D1: Methodology Rigor** | Mandatori | 🚫 `BLOCK` | ✅ **`PASS`** | ⬆️ Meningkat Signifikan |
| **D2: Domain Accuracy** | Mandatori | ⚠️ `WARN` | ✅ **`PASS`** | ⬆️ Meningkat |
| **D3: Argumentative Coherence** | Mandatori | 🚫 `BLOCK` | ✅ **`PASS`** | ⬆️ Meningkat Signifikan |
| **D4: Cross-Disciplinary Relevance** | Pendukung | ⚠️ `WARN` | ✅ **`PASS`** | ⬆️ Meningkat |
| **D5: Writing & Structure Hygiene** | Pendukung | ⚠️ `WARN` | ✅ **`PASS`** | ⬆️ Meningkat |
| **D6: Venue Fit & Contribution** | Mandatori | ⚠️ `WARN` | ✅ **`PASS`** | ⬆️ Meningkat |
| **Keputusan Editorial Global** | **Schema 13** | **MAJOR REVISION (F2/F3)** | **ACCEPT (F0)** | ✅ **Lolos Verifikasi** |

---

## IV. Apresiasi Khusus Dewan Editor atas Kedewasaan Ilmiah Penulis

Dewan Editor dan seluruh anggota panel reviewer mengapresiasi integritas akademik yang dicerminkan oleh tim penulis:
1. **Kejujuran Statistik yang Luar Biasa**: Penulis secara terbuka dan transparan melaporkan bahwa kenaikan akurasi +0.41% tidak signifikan secara statistik ($p = 0.3057$) dan merumuskan fenomena ilmiah baru berupa *asymptotic feature saturation*, alih-alih memanipulasi klaim keunggulan mutlak.
2. **Keterbukaan terhadap Disparitas Keadilan Interseksional**: Penulis tidak menutupi kelemahan model terhadap subkelompok *Black Females* (Recall 89.44%, $\Delta\text{TPR} = 7.50\%$), melainkan mengupasnya secara ilmiah melalui perspektif *phenotypic overlap* dan bias representasi historis pada data pra-latih.
3. **Penyempurnaan Retorika Ilmiah**: Penulis dengan rendah hati menanggalkan istilah hiperbolik (*"novel framework"*) dan mengadopsi formulasi objektif yang presisi secara teknis.

---

## V. Panduan Tahap Akhir Pra-Submisi Portal IEEE Access (Post-Acceptance Roadmap)

Meskipun naskah telah diterima secara ilmiah dalam simulasi peer review ini, penulis wajib menuntaskan langkah prosedural teknis berikut sebelum melakukan pengiriman berkas (*submission*) resmi ke portal IEEE Author Portal:

1. **Alih Bahasa ke Academic English**:
   - Seluruh berkas naskah pada `paper/*.md` yang saat ini berbahasa Indonesia wajib diterjemahkan ke dalam Bahasa Inggris akademis formal (*Standard Academic English*) dengan tata bahasa presisi dan terminologi visi komputer terkini.
2. **Pemformatan Template IEEE Access**:
   - Naskah wajib dialihkan ke format template resmi *IEEE Access* (LaTeX atau Microsoft Word 2-kolom) dengan menyertakan seluruh gambar beresolusi tinggi (minimal 300 DPI, format TIFF/EPS/PNG), persamaan bernomor rapi, dan tabel sesuai standar tipografi IEEE.
3. **Kelengkapan Profil ORCID & Biografi**:
   - Pastikan keempat penulis memiliki nomor ORCID aktif yang terhubung pada metadata pengiriman dan pasfoto penulis disiapkan sesuai spesifikasi biografi naratif IEEE.

---

Selamat kepada tim penulis atas kerja keras, dedikasi metodologis, dan penyempurnaan substansial yang telah dicapai pada naskah ini.

**Hormat kami,**  
*Atas nama Dewan Editor dan Panel Reviewer Independen IEEE Access Mock Review,*

**Prof. Dr. Academic Editor, Ph.D., Fellow IEEE**  
*Editor-in-Chief (Simulasi Panel Peer Review)*  
IEEE Access Editorial Board
