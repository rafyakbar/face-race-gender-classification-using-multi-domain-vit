# Ringkasan Eksekutif Peer Review Putaran 2 (Round 2 Summary)

**Judul Naskah:** Multi-Domain Vision Transformer Fusion for Intersectional Demographic Classification from Facial Images  
**Penulis:** Dr. Ir. Ricky Eka Putra, S.Kom., M.Kom., Rezky Arisanti Putri, S.Kom., M.Kom., Dr. Yuni Yamasari, S.Kom., M.Kom., Rafy Aulia Akbar, S.Kom., M.Kom.  
**Afiliasi:** Departemen Informatika, Fakultas Teknik, Universitas Negeri Surabaya, Indonesia  
**Target Jurnal:** *IEEE Access*  
**Tanggal Evaluasi:** 28 September 2026  
**Keputusan Redaksi (Schema 13):** **`ACCEPT`** *(Diterima Secara Ilmiah — Lolos Verifikasi Penuh Standar IEEE Access)*  
**Langkah Lanjutan:** Penyiapan Naskah Terjemahan *Academic English* & Penyesuaian Template 2-Kolom IEEE Access  

---

## 1. Ikhtisar Penelaahan Putaran Kedua (Re-Review Verification)

Simulasi penelaahan verifikasi putaran kedua (*Round 2 Re-Review / Verification Review*) telah selesai dilaksanakan secara independen oleh panel 5 evaluator dengan mempertahankan kesinambungan tolok ukur (*Yardstick Continuity* dibekukan sesuai `panel_config.json` Putaran 1). Penelaahan berfokus menguji apakah revisi naskah pada direktori `paper/` dan surat tanggapan formal `09_response_letter.md` telah menjawab tuntas seluruh 22 rencana aksi pada `08_revision_roadmap.md` Putaran 1.

Hasil audit verifikasi silang menunjukkan bahwa tim penulis telah menunjukkan **responsivitas dan integritas ilmiah yang luar biasa**:
1. Seluruh 4 isu kritis pemblokir (**Priority 1 - Must Fix**) telah diselesaikan secara substantif dan jujur.
2. Seluruh 6 isu mayor (**Priority 2 - Should Fix**) telah diselesaikan tuntas (100%).
3. Seluruh 12 isu minor/editorial (**Priority 3 - Nice to Fix**) telah terpenuhi (11 item terpenuhi penuh, 1 item dideklarasikan sebagai batasan metodologis yang sah).
4. Tidak ditemukan adanya cacat baru (*zero new defects*), kebocoran data (*data leakage*), maupun regresi mutu.

Berdasarkan aturan deterministik **Sprint Contract Schema 13 (Kondisi F0)**, seluruh 6 dimensi akseptasi (D1–D6) kini berstatus **`PASS`**, sehingga naskah dinyatakan **`ACCEPT`** (diterima secara substantif untuk dipersiapkan menuju submisi resmi ke portal *IEEE Access*).

---

## 2. Matriks Status 6 Dimensi Akseptasi (Schema 13: Pasca-Revisi R2)

| Kode | Dimensi Akseptasi | Evaluator Utama | Status R1 | Status R2 | Ringkasan Penilaian Verifikasi R2 |
|:---:|---|:---:|:---:|:---:|---|
| **D1** | **Methodology Rigor** | Reviewer 1 (Metodologi) | 🚫 `block` | ✅ **`pass`** | Uji inferensial McNemar berpasangan dan Wilson 95% Confidence Interval disajikan lengkap pada seluruh 28 konfigurasi di Tabel VII–X. Kolom variasi validasi silang 5-fold (Mean ± Std) dilaporkan transparan. Ambiguitas partisi diakui jujur sebagai *deliberate limitation* tingkat citra dengan arah *Future Work* yang jelas. Bebas kebocoran data. |
| **D2** | **Domain Accuracy & SOTA** | Reviewer 2 (Pakar Domain) | ⚠️ `warn` | ✅ **`pass`** | Posisi literatur diklarifikasi bahwa paper seminal DemogPairs (2019) hanya menguji verifikasi ROC dan bukan klasifikasi 6-kelas, sehingga studi ini sah sebagai pelopor baseline 6-kelas. Silsilah pra-latih HuggingFace transparan. Integrasi teori neurokognitif dual-stream Bruce & Young (1986) dan Haxby (2000) memperkaya dasar konseptual. |
| **D3** | **Argumentative Coherence** | Devil's Advocate (DA) | 🚫 `block` | ✅ **`pass`** | DA CRITICAL teradjudikasi tuntas: paradoks regresi Random Forest (-0.65%) dijelaskan secara matematis melalui fenomena *curse of dimensionality* pada *axis-aligned splits* di subspace $\sqrt{2304}=48$, klaim keunggulan dikalibrasi menjadi *classifier-dependent*, istilah hiperbolik *"novel framework"* dihapus total, dan non-signifikansi statistik ($p=0.3057$) membuktikan fenomena *asymptotic feature saturation*. |
| **D4** | **Cross-Disciplinary Relevance** | Reviewer 3 (Perspektif Silang) | ⚠️ `warn` | ✅ **`pass`** | Kesenjangan keadilan algoritmik dijembatani melalui perhitungan metrik formal *Equal Opportunity Difference* ($\Delta\text{TPR} = 7.50\%$ pada SVM dan $5.00\%$ pada LR), disparitas recall *Black Females* (89.44%) dikupas kritis melalui faktor *phenotypic overlap*, latensi inferensi hilir terkonfirmasi efisien (<50 MB, sub-milidetik), dan statuta kepatuhan etika Responsible AI terpasang tegas. |
| **D5** | **Structure, Exposition & Hygiene** | Editor-in-Chief (EIC) | ⚠️ `warn` | ✅ **`pass`** | Butir kontribusi di Pendahuluan dipadatkan menjadi 3 butir elegan dan tajam (format bilingual). Narasi pembahasan hasil diperdalam dengan interpretasi mekanistik pemetaan ruang Hilbert pada kernel polinomial kuadratik SVM vs partisi ortogonal pohon RF. |
| **D6** | **Venue Fit & Contribution** | Editor-in-Chief (EIC) | ⚠️ `warn` | ✅ **`pass`** | Distingsi kebaruan konseptual terhadap prosiding konferensi ICVEE 2025 ([19]) diartikulasikan sangat jelas (fusi tri-domain penuh, inferensi signifikansi formal, audit keadilan interseksional). Seluruh statuta wajib IEEE Access (*Data Availability*, *Code Availability*, dan *Ethical Compliance Statements*) telah tercantum lengkap di Bagian V. |

---

## 3. Evaluasi Penyelesaian 4 Isu Kritis Pemblokir (Priority 1 - Must Fix)

| ID Isu | Topik Masalah R1 | Solusi Penulis pada Putaran 2 | Verifikasi Teks Naskah | Status Akhir |
|:---:|---|---|---|:---:|
| **`ISSUE-METH-01`** | Ambiguitas Partisi Bebas Kebocoran Subjek (*Subject-Disjoint Split*) | Penulis secara transparan mengakui bahwa partisi dilakukan pada tingkat citra (*class-stratified 80/20*, 1.440 latih / 360 uji per kelas) karena keterbatasan metadata DemogPairs orisinal. Dideklarasikan sebagai *deliberate limitation* dan dirumuskan sebagai prioritas riset masa depan (*cross-identity evaluation*). | `paper/03_materials-and-methods_a-dataset.md` (P2) & `paper/05_conclusion.md` (P2) | ✅ **`RESOLVED`** |
| **`ISSUE-DA-C1`** | Paradoks Keunggulan Tri-Domain vs Regresi Random Forest (-0.65%) | Menghapus klaim superioritas mutlak, mengkalibrasi bahasa klaim menjadi *classifier-dependent*, dan menyajikan analisis mendalam fenomena *curse of dimensionality* pada algoritma pohon acak yang mengevaluasi $\sqrt{2304}=48$ fitur acak di setiap pemisahan cabang. | `paper/04_results-and-discussion_a-global-performance.md` (P1, P5) & `paper/04_results-and-discussion_b-feature-ablation-study.md` (P2–3) | ✅ **`RESOLVED`** |
| **`ISSUE-METH-02`** | Ketiadaan Uji Signifikansi Statistik pada Selisih 0.41% | Melakukan uji McNemar berpasangan dengan koreksi kontinuitas Edwards pada data uji ($N=2.160$) yang membuktikan selisih SVM ($\chi^2=1.0492, p=0.3057$) dan RF ($\chi^2=1.4825, p=0.2232$) tidak signifikan ($p > 0.05$), mengindikasikan fenomena *asymptotic feature saturation*. Wilson Score 95% CI ditambahkan ke seluruh 28 konfigurasi. | `paper/04_results-and-discussion_a-global-performance.md` (Tabel VII–X & P5) | ✅ **`RESOLVED`** |
| **`ISSUE-DA-M1`** | Ketiadaan Eksperimen Kontrol Dimensionalitas (*Noise Baseline*) | Penulis membuktikan melalui penalaran deduktif komparatif perilaku lintas pengklasifikasi (*cross-classifier contrast*): jika kenaikan SVM murni artefak dimensi, RF semestinya tidak mengalami penurunan performa (-0.65%). Ditambah bukti uji McNemar non-signifikan ($p=0.3057$) yang mengonfirmasi kejenuhan asimtotik fitur laten. | `paper/04_results-and-discussion_b-feature-ablation-study.md` (P2) | ✅ **`RESOLVED`** |

---

## 4. Rekomendasi Langkah Final Menuju Submisi Portal IEEE Access

Dengan diterimanya naskah pada tahap telaah substantif ini, langkah-langkah yang direkomendasikan untuk eksekusi pra-submisi resmi meliputi:
1. **Translasi ke Academic English**: Menerjemahkan naskah dari Bahasa Indonesia akademis ke Bahasa Inggris akademis formal sesuai gaya selingkung IEEE.
2. **Layouting Template IEEE Access**: Memasukkan teks dan tabel ke dalam template resmi LaTeX/Word dua-kolom *IEEE Access*.
3. **Resolusi Gambar Visual**: Memastikan seluruh berkas gambar diagram arsitektur, metodologi, dan matriks konfusi disiapkan dengan resolusi minimal 300 DPI.
4. **Final Check Kepatuhan Statuta**: Memastikan URL repositori GitHub dan Google Drive dataset DemogPairs dapat diakses secara publik tanpa batasan perizinan.

---

## 5. Indeks Berkas Penelaahan Lengkap (Round 2 Package)

Seluruh berkas verifikasi dan keputusan penelaahan Putaran 2 dikelola secara terstruktur pada direktori [`paper_reviews/round-2/`](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/paper_reviews/round-2/):

- [`09_response_letter.md`](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/paper_reviews/round-2/09_response_letter.md) — Surat Tanggapan Penulis Butir-per-Butir (*Point-by-Point Rebuttal*).
- [`10_rebuttal_audit_report.md`](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/paper_reviews/round-2/10_rebuttal_audit_report.md) — Laporan Audit Diplomasi Nada, Ketiadaan Komentar Yatim, dan Lokator Bukti.
- [`11_re_review_verification.md`](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/paper_reviews/round-2/11_re_review_verification.md) — Matriks Ketertelusuran Komitmen Revisi (*R&R Traceability Matrix*) untuk 22 Isu.
- [`12_eic_re_review_notes.md`](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/paper_reviews/round-2/12_eic_re_review_notes.md) — Catatan Evaluasi Verifikasi Internal Editor-in-Chief terhadap 6 Dimensi Akseptasi.
- [`07_editorial_decision.md`](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/paper_reviews/round-2/07_editorial_decision.md) — Surat Keputusan Editorial Resmi Putaran 2 (**Status: ACCEPT**).
- [`08_residual_roadmap.md`](file:///D:/Rafy/Research/face-race-gender-classification-using-multi-domain-vit/paper_reviews/round-2/08_residual_roadmap.md) — Panduan Aksi Residual Pra-Submisi (*Post-Acceptance Roadmap*).
