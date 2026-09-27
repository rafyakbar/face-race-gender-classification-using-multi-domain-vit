# Ringkasan Eksekutif Peer Review Putaran 1 (Round 1 Summary)

**Judul Naskah:** Multi-Domain Vision Transformer Fusion for Intersectional Demographic Classification from Facial Images  
**Penulis:** Dr. Ir. Ricky Eka Putra, S.Kom., M.Kom., Rezky Arisanti Putri, S.Kom., M.Kom., Dr. Yuni Yamasari, S.Kom., M.Kom., Rafy Aulia Akbar, S.Kom., M.Kom.  
**Afiliasi:** Departemen Informatika, Fakultas Informatika, Universitas Negeri Surabaya, Indonesia  
**Target Jurnal:** *IEEE Access*  
**Tanggal Evaluasi:** 27 September 2026  
**Keputusan Redaksi (Schema 13):** **`MAJOR REVISION`** *(Setara dengan Reject with Resubmission Encouraged pada portal IEEE Access)*  
**Tenggat Waktu Revisi:** 6 (enam) Minggu (Jatuh Tempo: 8 November 2026)  

---

## 1. Ikhtisar Penelaahan

Simulasi penelaahan sejawat (*mock peer review*) putaran pertama (Round 1) telah selesai dilaksanakan secara independen oleh panel 5 evaluator dengan menerapkan standar publikasi **IEEE Access** dan protokol evaluasi **Sprint Contract Schema 13.2** (sintesis konsensus panel multi-model: Gemini 3.8 Flash + Claude Opus). Naskah dievaluasi berdasarkan draf Bahasa Indonesia pra-translasi.

Secara umum, naskah dinilai memiliki **kesesuaian ruang lingkup (*scope fit*) yang tinggi** dengan *IEEE Access*, ketelitian formulasi matematis pada Persamaan (1)–(17), disiplin isolasi transformasi scikit-learn tanpa kebocoran data pra-pemrosesan, serta transparansi pelaporan performa interseksional 6 kelas. Namun, naskah memperoleh rekomendasi **MAJOR REVISION** terutama akibat temuan *blocking* pada aspek ambiguitas partisi data berbasis identitas subjek (*subject-disjoint split*), ketiadaan uji signifikansi statistik formal (McNemar & 95% CI) untuk selisih 9 sampel (0.41%), paradoks regresi performa Random Forest (-0.65%), serta ketiadaan eksperimen kontrol dimensionalitas (*noise baseline*).

---

## 2. Matriks Status 6 Dimensi Akseptasi (Schema 13)

| Kode | Dimensi Akseptasi | Evaluator Utama | Status | Ringkasan Penilaian |
|:---:|---|:---:|:---:|---|
| **D1** | **Methodology Rigor** | Reviewer 1 (Metodologi) | **`block`** | Memerlukan audit partisi data berbasis identitas subjek (*subject-disjoint split*) untuk menjamin bebas kebocoran identitas (*zero leakage*), penambahan uji signifikansi statistik (McNemar & 95% CI) pada selisih 0.41%, pelaporan stabilitas fold CV (Mean ± Std), dan penyeimbangan metrik akurasi OvR. |
| **D2** | **Domain Accuracy & SOTA** | Reviewer 2 (Pakar Domain) | **`warn`** | Komparasi benchmark bersifat sirkular (hanya karya internal penulis terdahulu); memerlukan minimal satu baseline model tunggal eksternal standar, transparansi silsilah checkpoint HuggingFace, visualisasi feature embedding (t-SNE/UMAP), dan pengayaan teori kognisi dual-stream. |
| **D3** | **Argumentative Coherence** | Devil's Advocate (DA) | **`block`** | Terjadi paradoks empiris kritis: penambahan domain usia hanya membalikkan 4–9 sampel pada model linier/kernel namun mendegradasi Random Forest sebesar -0.65% (14 sampel bertambah salah). Memerlukan eksperimen kontrol dimensionalitas (Gaussian noise), kalibrasi klaim fusi konkatenasi, dan justifikasi vs fine-tuning. |
| **D4** | **Cross-Disciplinary Relevance** | Reviewer 3 (Perspektif Silang) | **`warn`** | Kesenjangan antara klaim kata kunci *algorithmic fairness* dengan ketiadaan metrik keadilan formal, disparitas drop recall 7.50% pada *Black Females*, ketiadaan profil latensi komputasi inferensi (ms/citra) dari 3 backbone ViT (~258M parameter), dan ketiadaan refleksi etika biometrik. |
| **D5** | **Structure, Exposition & Hygiene** | Editor-in-Chief (EIC) | **`warn`** | Format IMRaD dan formulasi matematis sangat rapi, namun butir kontribusi di Pendahuluan terlalu panjang dan berulang secara dwibahasa, serta narasi pembahasan hasil perlu diperdalam dengan analisis mekanistik batas pemisahan kelas. |
| **D6** | **Venue Fit & Contribution** | Editor-in-Chief (EIC) | **`warn`** | Risiko persepsi penambahan fitur inkremental marjinal dari prosiding ICVEE 2025 ([19]), serta ketiadaan statuta wajib IEEE Access (*Data Availability*, *Code Availability*, dan *Ethical Compliance Statements*). |

---

## 3. Poin Kritis & Isu Pemblokir Utama (*Top Blocking Issues - Priority 1*)

1. **[P1-1] Audit Partisi Bebas Kebocoran Identitas Subjek (*Subject-Disjoint Split*):**
   - *Masalah:* Bagian III-A dan Tabel I menyebut pembagian stratified 80:20 pada 10,800 citra DemogPairs, tetapi belum menegaskan apakah partisi dipisah pada tingkat identitas individu unik. Tumpang tindih identitas orang pada data latih dan uji akan menimbulkan *identity leakage* fatal pada evaluasi biometrik.
   - *Tindakan:* Konfirmasi tertulis pada teks Bagian III-A bahwa tidak ada subjek/orang yang sama yang muncul di set latih dan uji secara bersamaan (*zero identity overlap*), serta cantumkan jumlah identitas subjek unik per partisi.
2. **[P1-2] Estimasi Ketidakpastian & Uji Signifikansi Statistik Inferensial:**
   - *Masalah:* Selisih keunggulan Tri-Domain atas Dual-Domain pada SVM (93.70% vs 93.29%) hanya merepresentasikan tepat 9 sampel citra dari $N=2,160$. Naskah mengakui perbandingan hanya bersifat deskriptif tanpa pengujian hipotesis formal.
   - *Tindakan:* Lakukan uji McNemar berpasangan pada set uji held-out ($p < 0.05$), laporkan Interval Kepercayaan 95% (Wilson/Bootstrap) pada Tabel VII–X, dan lakukan uji beda rata-rata performa lintas 5 fold cross-validation.
3. **[P1-3] Kalibrasi Paradoks Keunggulan Tri-Domain & Regresi Random Forest:**
   - *Masalah:* Penambahan domain usia berdimensi 768 (+86M parameter) justru merusak akurasi Random Forest sebesar -0.65% (14 citra bertambah salah pada Tabel VII), bertentangan dengan klaim bahwa arsitektur Tri-Domain optimal secara seragam.
   - *Tindakan:* Turunkan derajat klaim keunggulan mutlak Tri-Domain; tambahkan analisis mendalam mengenai fenomena *curse of dimensionality* pada pohon keputusan RF dan akui batas kejenuhan representasi fitur usia pada tugas klasifikasi demografis.
4. **[P1-4] Eksperimen Kontrol Dimensionalitas (*Gaussian Noise Baseline*):**
   - *Masalah:* Naskah belum membuktikan apakah kenaikan akurasi tipis berasal dari informasi komplementer domain usia atau sekadar efek artifisial peningkatan kapasitas dimensi representasi (768 ke 1,536 ke 2,304 dimensi).
   - *Tindakan:* Sajikan data eksperimen kontrol baseline (konkatenasi fitur Face + 768-d Gaussian noise acak pada classifier SVM) atau berikan analisis dimensi efektif yang membuktikan peran komplementer biologis domain usia.
5. **[P1-5] Penyiapan Naskah Terjemahan Bahasa Inggris Akademik IEEE:**
   - *Tindakan:* Lakukan alih bahasa menyeluruh naskah dari Bahasa Indonesia ke dalam *Academic English* sesuai standar publikasi dan template resmi *IEEE Access* sebelum submisi ke portal editorial IEEE.

---

## 4. Indeks Berkas Penelaahan Rinci (Round 1 Package)

Seluruh laporan evaluasi mendalam dan instrumen revisi tersedia pada folder [`round-1/`](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/paper_reviews/round-1/):

- [`00_desk_screening.md`](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/paper_reviews/round-1/00_desk_screening.md) — Laporan Skrining Meja EIC (*Desk Pass*).
- [`01_eic_report.md`](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/paper_reviews/round-1/01_eic_report.md) — Laporan Evaluasi EIC (Format, Gaya Selingkung, & Lingkup *IEEE Access*).
- [`02_methodology_report.md`](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/paper_reviews/round-1/02_methodology_report.md) — Laporan Reviewer 1 (Rigor Metodologi, *Subject Leakage*, & Uji Signifikansi Statistik).
- [`03_domain_report.md`](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/paper_reviews/round-1/03_domain_report.md) — Laporan Reviewer 2 (Pakar Domain Visi Komputer, Baseline Eksternal, & Silsilah Checkpoint).
- [`04_cross_perspective_report.md`](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/paper_reviews/round-1/04_cross_perspective_report.md) — Laporan Reviewer 3 (Keadilan Algoritmik, Drop Recall 7.50%, & Profil Komputasi 3 ViT).
- [`05_devils_advocate_report.md`](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/paper_reviews/round-1/05_devils_advocate_report.md) — Laporan Devil's Advocate (Pengujian Adversarial, Paradoks 9 Sampel, & Kontrol Noise).
- [`06_findings_database.json`](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/paper_reviews/round-1/06_findings_database.json) — Basis data terstruktur 22 butir temuan reviewer konsensus multi-model.
- [`07_editorial_decision.md`](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/paper_reviews/round-1/07_editorial_decision.md) — Surat Keputusan Editorial resmi Dewan Redaksi (*Major Revision* / *Reject & Resubmit*).
- [`08_revision_roadmap.md`](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/paper_reviews/round-1/08_revision_roadmap.md) — Matriks Rencana Aksi Revisi terstruktur (Prioritas P1, P2, dan P3).
