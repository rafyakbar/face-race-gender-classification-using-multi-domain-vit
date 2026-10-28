# DOKUMENTASI SESI KERJA ANTIGRAVITY (AGY)
**Nama Berkas**: `docs/sessions/2026-10-28_dekonstruksi-review-ieee-roadmap-revisi-dan-audit-numerik-hasil.md`  
**Cermin Berkas**: `sessions/session_2026-10-28_dekonstruksi-review-ieee-roadmap-revisi-dan-audit-numerik-hasil.md`  
**Tanggal**: 28 Oktober 2026  
**Waktu Sesi**: 19:15:00 – 21:40:00 WIB  
**Workspace**: `D:\Research\face-race-gender-multi-vit`  
**Konteks Repositori**: `rafyakbar/face-race-gender-multi-vit`  
**Target Publikasi**: IEEE Access (ID Manuskrip: `Access-2026-50857`, Keputusan: *Reject & Resubmit* — 1 Kesempatan Resubmission)  
**Lingkungan Eksekusi**: Windows 11, Python 3.11+ (Conda `torch-gpu`), PyTorch CUDA, Scikit-Learn 1.4+, Antigravity Agentic Assistant / Gemini 3.8 Flash (High)  

---

## 1. IKHTISAR DAN TUJUAN UTAMA SESI

Sesi kerja intensif pada 28 Oktober 2026 difokuskan pada transisi strategis dari fase infrastruktur kode dan benchmark eksperimental menuju **Tahap 5 Workflow: Penanganan Peer-Review dan Perencanaan Eksekusi Revisi Manuskrip Ilmiah IEEE Access**. 

Rangkaian sasaran utama yang berhasil direalisasikan pada sesi ini meliputi:
1. **Internalisasi Konteks Otoritatif Repositori:** Membaca dan memahami secara menyeluruh berkas panduan referensi utama [`README.ai.md`](file:///D:/Research/face-race-gender-multi-vit/README.ai.md) (693 baris), log sesi sebelumnya ([`docs/sessions/2026-10-27_standardisasi-arsip-re-eksekusi-notebook-dan-dokumentasi-dual-benchmark.md`](file:///D:/Research/face-race-gender-multi-vit/docs/sessions/2026-10-27_standardisasi-arsip-re-eksekusi-notebook-dan-dokumentasi-dual-benchmark.md)), serta membedah keterkaitan 4 pilar direktori naskah dan hasil eksperimen (`paper/`, `paper_reviews_ieee/`, `archive/md_old/`, dan `md/`).
2. **Dekonstruksi Komentar Reviewer IEEE Access melalui Skill `ar-paper-revision-coach`:**
   - Membedah secara mendalam seluruh 17 butir komentar reviewer (7 komentar Reviewer 1 dan 10 komentar kritis Reviewer 2) serta 4 direktif prosedural Associate Editor Dr. Vincenzo Conti.
   - Menghasilkan 3 artefak bebestari resmi berstandar internasional di direktori [`paper_reviews_ieee/`](file:///D:/Research/face-race-gender-multi-vit/paper_reviews_ieee/):
     * [`08_revision_roadmap.md`](file:///D:/Research/face-race-gender-multi-vit/paper_reviews_ieee/08_revision_roadmap.md) (Schema 7: Matriks P1/P2/P3, pola silang reviewer, urutan sprint, dan estimasi waktu).
     * [`09_revision_tracking.md`](file:///D:/Research/face-race-gender-multi-vit/paper_reviews_ieee/09_revision_tracking.md) (Schema 11 / #268 / Kong et al. 2026: *Nested Commitment Ledger* YAML).
     * [`10_response_letter_skeleton.md`](file:///D:/Research/face-race-gender-multi-vit/paper_reviews_ieee/10_response_letter_skeleton.md) (Rangka formal *Point-by-Point Response to Reviewers* berpola R $\to$ A $\to$ C).
   - Memvalidasi kepatuhan linter otomatis [`verify_revision_roadmap.py`](file:///D:/Research/face-race-gender-multi-vit/.agents/skills/ar-paper-revision-coach/scripts/verify_revision_roadmap.py) dengan **0 error, 0 warning** (100% kepatuhan invarian N1–N5 dan prinsip *zero-orphan*).
3. **Penyusunan Panduan Prioritas Kerja Otoritatif (`paper_reviews_ieee/00_URUTAN_PRIORITAS_REVISI.md`):**
   - Merancang panduan eksekusi langkah-demi-langkah yang membagi pekerjaan revisi ke dalam 3 fase terstruktur (Fase 1: P1 Must-Fix / Blockers, Fase 2: P2 Should-Fix / Penguatan Narasi, dan Fase 3: P3 Editorial & Packaging Resubmission).
   - Memetakan setiap butir review ke berkas target di [`paper/*.md`](file:///D:/Research/face-race-gender-multi-vit/paper/) dan sumber data eksperimen rujukan di [`experiment/code/`](file:///D:/Research/face-race-gender-multi-vit/experiment/code/).
4. **Audit Komprehensif Berkas Metodologi Hasil (`experiment/05_results.md`):**
   - Mengerahkan subagent khusus `Results & Metrics Auditor` untuk memvalidasi programatik **856 butir data numerik** antara `05_results.md` dengan seluruh 56 berkas JSON mentah dan buku besar audit konsolidasi.
   - Mengonfirmasi tingkat kecocokan 98,95% sempurna dan langsung menerapkan 5 koreksi presisi numerik (rata-rata rumpun Tabel 3.3, perbaikan format satuan, koreksi header matriks konfusi `Total Sampel (Support)`, dan pembersihan pemisah tipografi).
5. **Pencatatan Riwayat Prompt & Penerbitan Commit Git Atomik:**
   - Mendokumentasikan instruksi prompt audit terperinci ke dalam [`prompts.txt`](file:///D:/Research/face-race-gender-multi-vit/prompts.txt).
   - Menerbitkan 3 commit atomik (*Conventional Commits*) dan mendorong seluruhnya ke cabang `main` repositori remote GitHub.

---

## 2. KRONOLOGI PERMINTAAN PENGGUNA & TINDAKAN YANG DIAMBIL

### A. Pembacaan dan Pemahaman Mandiri `README.ai.md`
* **Permintaan Pengguna:** *"baca readme ai md"*
* **Tindakan yang Diambil:**
  - Membaca secara tuntas berkas [`README.ai.md`](file:///D:/Research/face-race-gender-multi-vit/README.ai.md) (693 baris).
  - Menguasai seluruh konteks naskah: identitas kepengarangan UNESA, target IEEE Access, tonggak *Reject & Resubmit* (20 Oktober 2026), arsitektur fusi tri-domain ViT (Wajah, Emosi, Usia), dataset DemogPairs (10.800 citra, 600 subjek seimbang), arsitektur *Dual-Benchmark*, serta 28 batasan dan direktif ilmiah wajib.

### B. Eksplorasi Dokumentasi Sesi (`docs/sessions/`)
* **Permintaan Pengguna:** *"pelajari docs/sessions"*
* **Tindakan yang Diambil:**
  - Memeriksa direktori `docs/sessions/` dan membaca berkas [`2026-10-27_standardisasi-arsip-re-eksekusi-notebook-dan-dokumentasi-dual-benchmark.md`](file:///D:/Research/face-race-gender-multi-vit/docs/sessions/2026-10-27_standardisasi-arsip-re-eksekusi-notebook-dan-dokumentasi-dual-benchmark.md).
  - Menarik benang merah bahwa infrastruktur komputasi telah 100% matang (33 notebook aktif seragam 16 sel, re-eksekusi berbasis bobot tersimpan tanpa re-training, cermin Markdown sinkron, dan dokumentasi berbahasa Indonesia baku akademik).

### C. Pembelajaran Cepat 4 Pilar Repositori
* **Permintaan Pengguna:** *"pelajari: - paper/ - paper_reviews_ieee/ - experiment/code/archive/md_old/ - experiment/code/md/ pelajari dengan cepat"*
* **Tindakan yang Diambil:**
  - Menginspeksi dan menganalisis secara paralel keempat direktori:
    1. `paper/`: Draf naskah modular saat ini masih berada dalam status pra-revisi (memuat angka historis SVM 93.70%) dan siap direvisi pada Tahap 5.
    2. `paper_reviews_ieee/`: Membedah surat keputusan editorial resmi, templat respons, daftar periksa kepatuhan, serta berkas `Comments.md`.
    3. `experiment/code/archive/md_old/`: Mengonfirmasi 35 cermin markdown historis (split acak tingkat citra, 100% kebocoran identitas subjek).
    4. `experiment/code/md/`: Mengonfirmasi 33 cermin markdown aktif (split *subject-disjoint*, 0% kebocoran identitas, LR 88.66% & SVM 88.61%, uji McNemar, dan Wilson 95% CI).

### D. Pengaktifan Skill `ar-paper-revision-coach`
* **Permintaan Pengguna:** *"/ar-paper-revision-coach bantu saya menyelesaikan revisi-revisi pada paper_reviews_ieee"*
* **Tindakan yang Diambil:**
  - Mengaktifkan skill bebestari akademik `ar-paper-revision-coach`.
  - Mengurai 17 komentar penelaah (R1 #1 s.d. #7 dan R2 #1 s.d. #10) ditambah 4 direktif Associate Editor (`AE-1` s.d. `AE-4`).
  - Menghasilkan 3 artefak terstruktur di `paper_reviews_ieee/`:
    * [`08_revision_roadmap.md`](file:///D:/Research/face-race-gender-multi-vit/paper_reviews_ieee/08_revision_roadmap.md) (Schema 7).
    * [`09_revision_tracking.md`](file:///D:/Research/face-race-gender-multi-vit/paper_reviews_ieee/09_revision_tracking.md) (Schema 11 / #268 Nested Commitment Ledger).
    * [`10_response_letter_skeleton.md`](file:///D:/Research/face-race-gender-multi-vit/paper_reviews_ieee/10_response_letter_skeleton.md) (Rangka respons formal pola R $\to$ A $\to$ C).
  - Menjalankan linter otomatis [`verify_revision_roadmap.py`](file:///D:/Research/face-race-gender-multi-vit/.agents/skills/ar-paper-revision-coach/scripts/verify_revision_roadmap.py) dengan hasil **SUKSES (0 error, 0 warning)**.
  - Menyusun *Pre-Advising Talking Points* untuk konsultasi bersama dosen pembimbing (Dr. Ir. Ricky Eka Putra).

### E. Penyusunan Panduan Urutan Prioritas Pengerjaan
* **Permintaan Pengguna:** *"tolong berikan juga informasi pada paper_reviews_ieee/ agar saya tahu mana mana saja yang perlu didahulukan untuk dikerjakan"*
* **Tindakan yang Diambil:**
  - Menyusun dokumen panduan prioritas baru: [`paper_reviews_ieee/00_URUTAN_PRIORITAS_REVISI.md`](file:///D:/Research/face-race-gender-multi-vit/paper_reviews_ieee/00_URUTAN_PRIORITAS_REVISI.md).
  - Mengelompokkan seluruh tugas revisi ke dalam 3 Fase:
    * **Fase 1 (P1: Must-Fix / Blocker Akseptasi):** 6 langkah kritis (Partisi bebas leakage, Tabel benchmark baru & ablasi leakage, Uji McNemar & 95% CI, Profil efisiensi komputasi, Redesain Gambar 3 ViT, dan Delimitasi keadilan EOD).
    * **Fase 2 (P2: Should-Fix / Penguatan Narasi):** 7 langkah (Pemadatan Bab I, Formulasi matematika Bab II, Spesifikasi checkpoint ViT, Rekonsiliasi 38.010 fits, Analisis matriks konfusi Gambar 4, Perluasan baseline kontekstual, dan Penajaman kesimpulan DemogPairs).
    * **Fase 3 (P3: Editorial & Resubmission):** 4 langkah (Sinkronisasi LaTeX, Highlighted PDF, Finalisasi Response Letter, Formulir Byline Change & Checklist).
  - Memperbarui [`paper_reviews_ieee/README.md`](file:///D:/Research/face-race-gender-multi-vit/paper_reviews_ieee/README.md) dengan menyematkan kotak info (*callout alert*) dan tautan inventaris dokumen baru.

### F. Pemeriksaan Kelengkapan `experiment/05_results.md`
* **Permintaan Pengguna:** *"apakah experiment/05_results.md sudah mencakup hasil sebelum evaluasi kebocoran data dan setelah evaluasi kebocoran data?"*
* **Tindakan yang Diambil:**
  - Memeriksa isi berkas [`experiment/05_results.md`](file:///D:/Research/face-race-gender-multi-vit/experiment/05_results.md) secara mendalam.
  - Mengonfirmasi bahwa berkas tersebut telah menyajikan kedua hasil secara lengkap: Bagian 1 (Subject-Disjoint terbaru), Bagian 2 (Subject-Overlap historis), dan Bagian 3 (Studi komparatif ablasi kebocoran data 28 model berdampingan).

### G. Audit Ulang Hasil Eksperimen via Subagent & Patching Numerik
* **Permintaan Pengguna:** *"tolong audit ulang results dengan yang ada pada hasil di code, delegasikan ke subagent agar optimal dan berikan instruksi dengan jelas"*
* **Tindakan yang Diambil:**
  - Mengerahkan subagent `Results & Metrics Auditor` (`68b5e5db-6cd6-4932-a616-89d5621a836f`) dengan instruksi audit programatik 100% presisi.
  - Subagent memverifikasi 856 butir data numerik terhadap 56 berkas JSON mentah dan `audit_ledger.json`:
    * 847 butir (98,95%) terverifikasi cocok sempurna sejak awal.
    * 9 butir (1,05%) diskrepansi terlokalisasi pada pembulatan rata-rata aritmatika kelompok di Tabel 3.3.
  - Mengaplikasikan langsung 5 perbaikan presisi pada [`experiment/05_results.md`](file:///D:/Research/face-race-gender-multi-vit/experiment/05_results.md):
    1. Rata-rata Tabel 3.3 LR: Akurasi Baru 0.8618 (dari 0.8615), Drop -4.22 pp, Relatif -4.67%.
    2. Rata-rata Tabel 3.3 RF: Akurasi Baru 0.8057 (dari 0.8071), Drop -2.24 pp, Relatif -2.74%.
    3. Rata-rata Tabel 3.3 GNB: Akurasi Baru 0.7837 (dari 0.7836), Drop -0.99 pp, Relatif -1.31%.
    4. Format satuan drop SVM: `-4.99 pp (-0.0499)`.
    5. Header matriks konfusi (Seksi 1.6.3, 1.6.4, dan 2.4): diubah menjadi `Total Sampel (Support)`.
    6. Pembersihan pemisah tipografi pada Seksi 2.3.2.
  - Memastikan berkas `05_results.md` mencapai status **100.0% sinkron sempurna**.

### H. Dokumentasi Prompt & Penerbitan Commit Git
* **Permintaan Pengguna:** *"tuliskan prompt untuk audit pada prompts.txt"* $\to$ disusul *"maksud saya prompt yang jelas"* $\to$ *"Identifikasi dan pelajari perubahan yang telah terjadi dilakukan, jika bisa dibuat menjadi beberapa commit, maka buat menjadi beberapa commit! Sekarang buat commit untuk perubahan-perubahan tersebut dan PUSH!"*
* **Tindakan yang Diambil:**
  - Mencatat instruksi lengkap dan terstruktur mengenai audit hasil eksperimen ke dalam riwayat aktif [`prompts.txt`](file:///D:/Research/face-race-gender-multi-vit/prompts.txt) sesuai konvensi repositori.
  - Mengelompokkan seluruh modifikasi ke dalam 3 commit atomik (*Conventional Commits*):
    * `3c6b879`: `docs(reviews)`
    * `6bdef9c`: `fix(experiment)`
    * `5b56ba5`: `chore`
  - Mendorong (*push*) seluruh commit ke cabang `main` repositori remote GitHub.

---

## 3. ARSITEKTUR STRATEGIS REVISI IEEE ACCESS (ROADMAP & PRIORITAS)

```
                              [EVALUASI BEBESTARI IEEE ACCESS]
                                             │
               ┌─────────────────────────────┴─────────────────────────────┐
               ▼                                                           ▼
     [Reviewer 1: 7 Masukan]                                     [Reviewer 2: 10 Masukan]
  (Penyajian, Diagram, Waktu)                                   (Metodologi, Leakage, Statistik)
               │                                                           │
               └─────────────────────────────┬─────────────────────────────┘
                                             ▼
                       [08_revision_roadmap.md & 00_URUTAN_PRIORITAS]
                                             │
      ┌──────────────────────────────────────┼──────────────────────────────────────┐
      ▼                                      ▼                                      ▼
[FASE 1: PRIORITAS TERTINGGI (P1)]    [FASE 2: PRIORITAS MENENGAH (P2)]    [FASE 3: EDITORIAL & RESUBMIT (P3)]
• Subject-Disjoint Primary Benchmark  • Pemadatan Bab I Pendahuluan        • Sinkronisasi LaTeX (access.tex)
• Data Leakage Ablation Study         • Rumus Matematis MHSA & Fusi (Bab II) • Pembangkitan Highlighted PDF
• Uji McNemar & 95% Wilson Score CI   • Rincian Checkpoint Pre-trained     • Finalisasi Response to Reviewers
• Profil Latensi Inferensi & Memori   • Rekonsiliasi 38.010 CV Fits        • Formulir Byline Change (UiTM)
• Desain Ulang Gambar 3 Arsitektur ViT • Analisis Error Asimetris Gambar 4  • Audit Resubmission Checklist 10-Pt
• Delimitasi Keadilan Algoritmik (EOD)• Delimitasi Kesimpulan DemogPairs
```

### Rekapitulasi Metrik Utama Naskah Revisi (Ground-Truth Terverifikasi):

| Parameter / Metrik | Primary Benchmark (Subject-Disjoint) | Historical Baseline (Subject-Overlap) | Catatan Ilmiah untuk Resubmission |
|:---|:---:|:---:|:---|
| **Tingkat Kebocoran Identitas** | **0.00% (Zero Leakage)** | **100.00% (Full Leakage)** | Mengeliminasi total bias *identity memorization*. |
| **Model Performa Puncak** | **Logistic Regression Tri-Domain** | **SVM Tri-Domain (Poly d=2)** | LR merebut peringkat 1 pada subjek tak terlihat. |
| **Akurasi Pengujian (Accuracy)** | **88.66%** (1.915 / 2.160 benar) | **93.70%** (2.024 / 2.160 benar) | Drop 5.09 pp menguantifikasi beban hafalan identitas. |
| **Macro F1-Score** | **0.8868** | **0.9369** | Kinerja seimbang di seluruh 6 subkelompok demografi. |
| **95% Wilson Score CI** | **[87.25%, 89.93%]** | [92.61%, 94.66%] | Rentang ketidakpastian statistik inferensial terstandarisasi. |
| **Latensi Inferensi per Sampel** | **0.0054 ms** (LR) vs 4.4481 ms (SVM) | — | LR beroperasi **>820× lebih cepat** dibanding SVM. |
| **Ukuran Berkas Bobot Model** | **0.11 MB** (LR) vs 36.60 MB (SVM) | — | LR **>330× lebih hemat memori** untuk *Edge AI*. |
| **Uji McNemar: LR vs SVM Tri** | $\chi^2 = 0.0000, \mathbf{p = 1.0000}$ | — | Paritas performa prediktif setara secara statistik. |
| **Uji McNemar: Tri vs Face** | $\chi^2 = 19.6923, \mathbf{p = 6.78 \times 10^{-6}}$ | — | Fusi multi-domain **unggul sangat signifikan ($p < 0.001$)**. |
| **Uji McNemar: Tri vs Dual** | LR: $\mathbf{p = 0.0073}$ vs SVM: $p = 0.7343$ | SVM: $p = 0.3057$ | Mengonfirmasi fenomena **saturasi fitur asimtotik**. |
| **Equal Opportunity Disparity** | $\Delta\text{TPR} = \mathbf{9.72\text{ pp}}$ (94.44% vs 84.72%) | $\Delta\text{TPR} = 7.50\text{ pp}$ (96.94% vs 89.44%) | Evaluasi disparitas subkelompok interseksional. |

---

## 4. INVENTARIS STRUKTUR BERKAS TERBARU DI `paper_reviews_ieee/`

```
paper_reviews_ieee/
├── 00_URUTAN_PRIORITAS_REVISI.md           # [BARU] Panduan operasional langkah-demi-langkah (Fase 1, 2, 3)
├── 08_revision_roadmap.md                  # [BARU] Matriks Peta Jalan Revisi Schema 7 (P1/P2/P3, beban kerja)
├── 09_revision_tracking.md                 # [BARU] Nested Commitment Ledger Schema 11 / #268 (Kong et al. 2026)
├── 10_response_letter_skeleton.md          # [BARU] Rangka formal tanggapan reviewer IEEE Access (R -> A -> C)
├── Comments.md                             # Terjemahan & dekonstruksi dwibahasa 17 butir review
├── IEEE-Access_Decision-on-Manuscript-ID-Access-2026-50857.md # Salinan asli surat keputusan editorial EIC
├── IEEE-Access_Response-to-Reviewers-template.md # Templat resmi tanggapan IEEE Access
├── Request-for-Byline-Change.md            # Formulir resmi penambahan co-author (Dr. Shukor Sanim, UiTM)
├── Resubmission-Checklist.md               # Daftar periksa kendali mutu 10-butir kepatuhan IEEE Access
├── README.md                               # Panduan master dossier dengan tautan dokumen baru
└── raw/                                    # Berkas korespondensi asli (.docx & webmail HTML)
```

---

## 5. REKAPITULASI COMMIT GIT HARI INI (28 OKTOBER 2026)

| Hash Commit | Tipe / Scope | Pesan Commit | Cakupan Berkas & Perubahan Kunci |
|:---:|:---|:---|:---|
| [`3c6b879`](https://github.com/rafyakbar/face-race-gender-classification-using-multi-domain-vit/commit/3c6b879) | `docs(reviews)` | `docs(reviews): add revision roadmap, tracking ledger, response skeleton, and priority action guide for IEEE Access` | Penerbitan 4 dokumen strategis revisi (`00_URUTAN_PRIORITAS_REVISI.md`, `08_revision_roadmap.md`, `09_revision_tracking.md`, `10_response_letter_skeleton.md`) dan pembaruan `README.md`. |
| [`6bdef9c`](https://github.com/rafyakbar/face-race-gender-multi-vit/commit/6bdef9c) | `fix(experiment)` | `fix(experiment): align 05_results.md arithmetic averages, confusion matrix headers, and format units from audit findings` | Penyelarasan numerik 100% pada `experiment/05_results.md` berdasarkan temuan audit subagent (rata-rata Tabel 3.3, format satuan, header matriks konfusi `Total Sampel (Support)`). |
| [`5b56ba5`](https://github.com/rafyakbar/face-race-gender-multi-vit/commit/5b56ba5) | `chore` | `chore: update prompt history log with comprehensive results audit instructions in prompts.txt` | Pencatatan riwayat instruksi prompt audit hasil eksperimen terstruktur ke dalam `prompts.txt` sesuai urutan kronologis terbalik. |

---

## 6. HASIL AUDIT INTEGRITAS & STATUS SISTEM AKHIR

1. **Integritas Naskah dan Kode Terjaga:**
   * Draf manuskrip pada `paper/*.md`, `paper_latex_en/`, dan `paper_latex_id/` aman dan tidak disentuh sembarangan sebelum Fase 22 dieksekusi.
   * Modul utilitas kode pada `experiment/code/utils/` dan seluruh model tersimpan di `experiment/code/models/` tetap utuh.
2. **Kepatuhan Terhadap Skema Internasional:**
   * Linter [`verify_revision_roadmap.py`](file:///D:/Research/face-race-gender-multi-vit/.agents/skills/ar-paper-revision-coach/scripts/verify_revision_roadmap.py) mengonfirmasi 0 error dan 0 warning untuk artefak Schema 7 dan Schema 11 (#268).
3. **Status Git Repositori:**
   * Cabang aktif: `main`.
   * Status sinkronisasi: `Your branch is up to date with 'origin/main'`.
   * Status *working tree*: Bersih (*clean*).

---

## 7. PANDUAN DAN REKOMENDASI UNTUK AI AGENT SESI BERIKUTNYA

Bagi AI agent yang melanjutkan pengerjaan pada sesi mendatang, berikut adalah panduan operasional prioritas:

1. **Titik Tolak Eksekusi:** Buka langsung dokumen [`paper_reviews_ieee/00_URUTAN_PRIORITAS_REVISI.md`](file:///D:/Research/face-race-gender-multi-vit/paper_reviews_ieee/00_URUTAN_PRIORITAS_REVISI.md).
2. **Langkah Kerja Berikutnya (Fase 1: P1 Must-Fix):**
   * **Langkah 1.1:** Edit [`paper/03_materials-and-methods_a-dataset.md`](file:///D:/Research/face-race-gender-multi-vit/paper/03_materials-and-methods_a-dataset.md) untuk mendokumentasikan spesifikasi dataset DemogPairs dan protokol *Subject-Disjoint Partitioning* (480 subjek latih / 120 subjek uji, 0.00% leakage).
   * **Langkah 1.2:** Edit [`paper/04_results-and-discussion_a-global-performance.md`](file:///D:/Research/face-race-gender-multi-vit/paper/04_results-and-discussion_a-global-performance.md) untuk mengganti angka Tabel VII–X dengan hasil *Subject-Disjoint* (LR 88.66% & SVM 88.61%) dan menambahkan subbab *Comparative Ablation Study on Data Leakage* (Tabel XI).
   * **Langkah 1.3:** Masukkan data uji signifikansi inferensial *Paired McNemar* dan 95% Wilson Score CI ke Bab IV.
   * **Langkah 1.4:** Masukkan tabel profil efisiensi komputasi (latensi, throughput, dan ukuran model).
3. **Aturan Konsistensi Data:** Seluruh angka yang dimasukkan ke naskah revisi **WAJIB 100% KONSISTEN** dengan data ground-truth pada [`experiment/05_results.md`](file:///D:/Research/face-race-gender-multi-vit/experiment/05_results.md) dan [`README.ai.md`](file:///D:/Research/face-race-gender-multi-vit/README.ai.md).
