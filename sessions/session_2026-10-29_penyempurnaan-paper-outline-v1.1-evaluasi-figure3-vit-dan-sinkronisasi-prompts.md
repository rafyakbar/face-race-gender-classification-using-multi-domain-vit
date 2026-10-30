# DOKUMENTASI SESI KERJA ANTIGRAVITY (AGY)
**Nama Berkas**: `docs/sessions/2026-10-29_penyempurnaan-paper-outline-v1.1-evaluasi-figure3-vit-dan-sinkronisasi-prompts.md`  
**Cermin Berkas**: `sessions/session_2026-10-29_penyempurnaan-paper-outline-v1.1-evaluasi-figure3-vit-dan-sinkronisasi-prompts.md`  
**Tanggal**: 29–30 Oktober 2026  
**Waktu Sesi**: 13:30:00 (29 Okt) – 10:15:00 (30 Okt) WIB  
**Workspace**: `D:\Research\face-race-gender-classification-using-multi-domain-vit`  
**Konteks Repositori**: `rafyakbar/face-race-gender-classification-using-multi-domain-vit`  
**Target Publikasi**: IEEE Access (ID Manuskrip: `Access-2026-50857`, Keputusan: *Reject & Resubmit* — 1 Kesempatan Resubmission Tunggal Berbasis *Binary Peer Review*)  
**Lingkungan Eksekusi**: Windows 11, Python 3.11+ (Conda `torch-gpu`), Git SSH, Antigravity Agentic Assistant / Gemini 3.8 Flash (High)  

---

## 1. IKHTISAR DAN TUJUAN UTAMA SESI

Sesi kerja komprehensif pada 29–30 Oktober 2026 difokuskan pada penuntasan dan pembakuan **Kerangka Kerja Naskah Revisi Ilmiah (Paper Outline Versi 1.1)** untuk manuskrip IEEE Access, evaluasi teknis aset visual arsitektur Vision Transformer (Figure 3), penyusunan prompt terarah untuk agen AI, serta tata kelola riwayat prompt dan penerbitan commit git berstandar *Conventional Commits*.

Sasaran strategis utama yang berhasil dicapai dalam sesi ini:
1. **Penyempurnaan Outline Manuskrip (`paper_outline_v1.1.md`):**
   - Mengintegrasikan kata kunci resmi IEEE terbaru: *Biometrics, face recognition, feature extraction, intersectional demographic recognition, multi-domain feature fusion, Vision Transformer*.
   - Menyelaraskan seluruh judul subseksi dan judul per-paragraf ke dalam Bahasa Inggris formal akademik.
   - Mengimplementasikan sistem **Catatan Respons Reviewer** terstruktur pada setiap subseksi/paragraf yang relevan, memuat kutipan teks komentar penelaah dan rincian mitigasi metodologis konkret.
   - Merestrukturisasi Section I (*Introduction*): kalibrasi batas kata per paragraf (Paragraf 1, 2, 4: 100–115 kata; Paragraf 3: 135–225 kata dengan 10 sitasi wajib tanpa braket numerik; Paragraf 5: 135–175 kata dengan optimasi 38.010 fits dan protokol Dual-Benchmark; Paragraf 6: 125–150 kata dengan pembersihan seluruh angka numerik hasil empiris; Paragraf 7: 50–75 kata).
   - Merestrukturisasi Section II (*Related Works*): menyusun 3 subseksi tematik ringkas $\times$ 2 paragraf (total 6 paragraf, 100–115 kata/paragraf) dilengkapi 4 formulasi matematis formal metode terdahulu: KELM decision boundary (Eq. 1), ViT patch linear projection (Eq. 2), ViT Multi-Head Self-Attention (Eq. 3), dan multi-domain concatenative direct sum (Eq. 4).
   - Menyelaraskan Section III (*Materials and Methods*): Overview diselaraskan dengan tata letak visual Figure 1 (`images/method.png`), subseksi A disederhanakan menjadi `### A. Dataset` dengan target kata per paragraf, contoh citra komposit Figure 2 (a–f), dan Tabel I diterjemahkan 100% ke Bahasa Inggris.
   - Menyelaraskan seluruh penomoran persamaan dari awal hingga akhir naskah secara kronologis ketat menjadi **Eq. (1) s.d. Eq. (23)** beserta pembaruan tabel *Master Element Sequence & Layout Specifications*.
2. **Evaluasi Teknis Gambar Figure 3 ViT (`images/vit_v2.0.png`):**
   - Melakukan inspeksi multimodal terhadap gambar `images/vit_v2.0.png` guna memverifikasi pemenuhan masukan Reviewer 1 Poin 3 (*clarity and novelty*).
   - Memastikan bahwa gambar baru berhasil mengoreksi kesalahan representasi (grid $14 \times 14$, 196 token, resolusi tinggi) dan memperluas alur ke cabang 3 model ViT pra-latih yang dibekukan (`ViT-Face`, `ViT-Emotion`, `ViT-Age`), fusi direct sum 2.304 dimensi, serta klasifikasi hilir 6 kelas interseksional.
   - Menyusun prompt singkat satu paragraf dwibahasa (Inggris & Indonesia) untuk instruksi agen AI pembuat grafik/visual.
3. **Sinkronisasi Riwayat Prompt & Manajemen Git Commit:**
   - Memutakhirkan berkas `prompts.txt` secara kronologis di bawah blok riwayat prompt aktif.
   - Membersihkan berkas salinan sementara `images/vit_v2.0 - Copy.png`.
   - Menerbitkan 3 commit atomik logis (*Conventional Commits*) dan berhasil melakukan `git push` ke cabang `main` repositori remote GitHub.

---

## 2. KRONOLOGI PERMINTAAN PENGGUNA & TINDAKAN YANG DIAMBIL

### A. Penyesuaian Kata Kunci dan Bahasa Judul Paragraf
* **Permintaan Pengguna:**
  1. *"pada paper outline keywords nya ganti menjadi: Biometrics, face recognition, feature extraction, intersectional demographic recognition, multi-domain feature fusion, Vision Transformer"*
  2. *"judul per paragraf gunakan bahasa inggris seperti sebelumnya"*
* **Tindakan yang Diambil:**
  - Memperbarui bagian *Keywords* pada [paper_outline_v1.1.md](file:///D:/Research/face-race-gender-classification-using-multi-domain-vit/paper_outline_v1.1.md).
  - Mengembalikan seluruh penamaan judul per-paragraf di Section I s.d. V ke dalam Bahasa Inggris baku akademik sesuai gaya pada versi 1.0.

### B. Klarifikasi Evaluasi Bebas Kebocoran Data (Reviewer 2 #2)
* **Permintaan Pengguna:**
  *"sebelum melanjutkan, saya tanya dulu, untuk komentar reviewer 2 nomor 2 mengenai Potensi Kebocoran Data dan Generalisasi Tingkat Identitas itu maksudnya menyediakan 2 evaluasi (stratified split dan split berdasarkan identitas) atau bagaimana?"*
* **Tindakan yang Diambil:**
  - Menjelaskan esensi komentar Reviewer 2 #2 secara komprehensif:
    1. Pembagian acak berbasis citra konvensional (*stratified split*) memiliki kelemahan fatal karena memungkinkan foto dari subjek yang sama tersebar di set latih dan set uji (100% kebocoran identitas subjek), memicu model menghafal wajah individu (*identity memorization*).
    2. Reviewer meminta pembuktian generalisasi sejati melalui evaluasi berbasis pemisahan identitas (*subject-disjoint evaluation*, 0% kebocoran identitas).
    3. Solusi strategis terbaik yang diadopsi adalah **Arsitektur Dual-Benchmark**:
       - *Primary Benchmark*: Evaluasi definitif pada subjek *held-out* yang belum pernah dilihat sebelumnya (LR 88.66% / SVM 88.61%).
       - *Historical Baseline Archive*: Replikasi partisi acak historis (SVM 93.70%) yang disajikan sebagai **studi ablasi kebocoran data (*data leakage ablation study*)** untuk menguantifikasi beban memorisasi identitas (penurunan 5.09 pp).

### C. Konfirmasi Penambahan Dual Benchmark dan Struktur Related Works
* **Permintaan Pengguna:**
  1. *"berarti apakah paper_outline_v1.1.md pada introduction Paragraph 5 dan A. Dataset apakah sudah sesuai?"* $\to$ *"ya, tolong tambahkan mengenai dual benchmark"*
  2. *"untuk II. RELATED WORKS apakah reviewer meminta dibuat menjadi subsection?"* $\to$ *"ooh ok, sepertinya lebih baik dijadikan subsection, ini berarti satu subsection hanya memiliki satu paragraf? karena sebelumnya ada 6 paragraf"*
* **Tindakan yang Diambil:**
  - Mengonfirmasikan bahwa Reviewer 1 #2 meminta restrukturisasi tematik naskah (*"modified in better way and add equations"*).
  - Merekomendasikan struktur seimbang: **3 subseksi tematik $\times$ 2 paragraf per subseksi (total 6 paragraf)**, sehingga seluruh pustaka dan kedalaman analisis dari versi 1.0 tetap dipertahankan utuh tanpa ada yang tereduksi.

### D. Perbaikan Mendalam Section I, II, dan III Sesuai Detail Spesifikasi
* **Permintaan Pengguna:**
  *Global: Jika ada subsection atau paragraf untuk menjawab komentar reviewer, berikan note di bawahnya agar tahu komentar dan mitigasinya.*  
  *Section I: Paragraf 1, 2, 4: 100–115 kata; Paragraf 3: 135–225 kata + daftar sitasi wajib tanpa nomor; Paragraf 5: 135–175 kata + poin optimasi hyperparameter; Paragraf 6: 125–150 kata tanpa angka hasil empiris; Paragraf 7: samakan seperti v1.0.*  
  *Section II: Perbaiki judul subseksi agar tidak terlalu panjang, lengkapi sumber literatur terkait tanpa nomor, tambahkan persamaan matematika termasuk pada subseksi A.*  
  *Section III: Overview samakan seperti v1.0 dan munculkan Figure 1; Subseksi A. Dataset judul cukup dataset, target kata per paragraf, munculkan Figure 2 komposit, tabel bahasa Inggris.*
* **Tindakan yang Diambil:**
  - Mengembangkan script pembaharuan terprogram (`scratch/update_outline_v2.py`) untuk memastikan integritas sintaks Markdown, perataan LaTeX, dan kepatuhan batasan kata.
  - Memperbarui [paper_outline_v1.1.md](file:///D:/Research/face-race-gender-classification-using-multi-domain-vit/paper_outline_v1.1.md):
    * **Catatan Respons Reviewer Global**: Setiap blok catatan diuraikan dengan format:
      `> **Catatan Respons Reviewer (Reviewer ... Poin ...):**`
      `> - **Komentar Reviewer:** ...`
      `> - **Rencana Mitigasi:** ...`
    * **Section I**:
      - Paragraf 1, 2, 4 dikalibrasi pada rentang 100–115 kata.
      - Paragraf 3 (135–225 kata) menyertakan daftar 10 sitasi artikel wajib tanpa penomoran braket angka.
      - Paragraf 5 (135–175 kata) mengintegrasikan optimasi *5-Fold StratifiedGroupKFold GridSearchCV* (38.010 fits) dan protokol *Dual-Benchmark*.
      - Paragraf 6 (125–150 kata) menyajikan 4 kontribusi formal dwibahasa murni berbasis kebaruan metodologis dan konseptual tanpa memuat angka hasil empiris.
      - Paragraf 7 (50–75 kata) menyajikan organisasi artikel secara ringkas.
    * **Section II**:
      - Menyusun 3 subseksi tematik: `A. Demographic Face Recognition`, `B. Vision Transformers in Face Analysis`, dan `C. Multi-Domain Feature Fusion`.
      - Menambahkan formulasi matematika KELM dari literatur Sunitha et al. (IVC 2022) pada Eq. (1).
      - Menyelaraskan Eq. (2) (Patch flattening & linear projection), Eq. (3) (Multi-Head Self-Attention), dan Eq. (4) (Multi-domain concatenative direct sum).
      - Melampirkan daftar "Sumber Literatur Terkait" tanpa nomor braket pada tiap paragraf.
    * **Section III**:
      - Overview: diselaraskan dengan v1.0, memunculkan diagram visual Figure 1 (`images/method.png`).
      - A. Dataset: judul disederhanakan, target kata per-paragraf (100–115 kata), visual komposit Figure 2 (a–f), dan Tabel I diubah 100% ke Bahasa Inggris.
      - B. Vision Transformer: visualisasi Figure 3 diselaraskan ke `images/vit_v2.0.png`.
      - Merapikan penomoran persamaan beruntun dari Eq. (1) hingga Eq. (23) beserta pembaruan tabel *Master Element Sequence & Layout Specifications*.

### E. Evaluasi Gambar Figure 3 ViT (`images/vit_v2.0.png`)
* **Permintaan Pengguna:**
  *"coba cek images/vit_v2.0.png apakah sudah sesuai dengan Reviewer 1 yang meminta desain ulang Figure 3 yang kurang jelas?"*
* **Tindakan yang Diambil:**
  - Melakukan telaah visual terhadap [images/vit_v2.0.png](file:///D:/Research/face-race-gender-classification-using-multi-domain-vit/images/vit_v2.0.png) dibandingkan dengan gambar lama `images/vit.png`:
    1. *Kelebihan yang telah dicapai*: Kejelasan teknis (*clarity*) terpenuhi sempurna (grid $14 \times 14$, 196 token, resolusi tinggi, anotasi dimensi di tiap tahap).
    2. *Tuntutan kebaruan (*novelty*)*: Gambar telah memperlihatkan cabang ekstraksi paralel 3 model ViT pra-latih yang dibekukan (`ViT-Face`, `ViT-Emotion`, `ViT-Age`), fusi direct sum 2.304 dimensi, serta klasifikasi hilir 6 kelas interseksional.
  - Memberikan rekomendasi teknis bahwa gambar tersebut sudah sangat representatif dan siap digunakan pada manuskrip.

### F. Pembuatan Prompt Ringkas untuk AI Agent Lain
* **Permintaan Pengguna:**
  1. *"buatkan prompt agar ai agent lain memperbaiki gambar tersebut"*
  2. *"jangan terlalu panjang, cukup satu paragraf singkat saja, tuliskan pada prompts.txt"*
* **Tindakan yang Diambil:**
  - Menyusun prompt ringkas 1 paragraf padat instruktif dalam format dwibahasa (Inggris dan terjemahan Indonesia).
  - Memasukkan prompt tersebut langsung ke berkas [prompts.txt](file:///D:/Research/face-race-gender-classification-using-multi-domain-vit/prompts.txt) di bawah deretan prompt aktif.

### G. Identifikasi Perubahan, Pembuatan Commit Atomik, dan Push ke Remote
* **Permintaan Pengguna:**
  *"Identifikasi dan pelajari perubahan yang telah terjadi dilakukan, jika bisa dibuat menjadi beberapa commit, maka buat menjadi beberapa commit! Sekarang buat commit untuk perubahan-perubahan tersebut dan PUSH! Gunakan skill 'git-commit' atau sesuai dengan best practice!"*
* **Tindakan yang Diambil:**
  - Menganalisis seluruh perubahan yang belum ter-stage (`git status -u`).
  - Menghapus berkas salinan cadangan yang tidak diperlukan (`images/vit_v2.0 - Copy.png`).
  - Membagi pekerjaan ke dalam 3 commit logis atomik:
    1. **Commit 1 (`a36cd1a`)**: `feat(figures): add redesigned Figure 3 ViT architecture with multi-domain fusion` (menambahkan `images/vit_v2.0.png`).
    2. **Commit 2 (`4f02a53`)**: `docs(outline): update paper outline v1.1 with reviewer mitigations and visual elements` (memperbarui `paper_outline_v1.1.md`).
    3. **Commit 3 (`6901895`)**: `chore: record recent user prompts and Figure 3 refinement prompt in prompts.txt` (memperbarui `prompts.txt`).
  - Melakukan `git push origin main` dan memverifikasi sinkronisasi penuh dengan remote GitHub.

---

## 3. INVENTARIS PERUBAHAN BERKAS

| No | Berkas yang Diubah / Dibuat | Kategori Tindakan | Deskripsi Perubahan Utama |
|:---:|---|:---:|---|
| 1 | [`paper_outline_v1.1.md`](file:///D:/Research/face-race-gender-classification-using-multi-domain-vit/paper_outline_v1.1.md) | Diperbarui (*Modified*) | Menyelaraskan catatan respons reviewer terstruktur, kata kunci, target kata Bab I, formulasi matematis Bab II (Eq. 1–4), visualisasi Figure 1–3 Bab III, penomoran Eq. 1–23, dan tabel master. |
| 2 | [`images/vit_v2.0.png`](file:///D:/Research/face-race-gender-classification-using-multi-domain-vit/images/vit_v2.0.png) | Ditambahkan (*Added*) | Gambar resolusi tinggi vektor redesign Figure 3 yang memvisualisasikan alur ViT-Base dan fusi paralel 3-domain hingga klasifikasi hilir. |
| 3 | [`prompts.txt`](file:///D:/Research/face-race-gender-classification-using-multi-domain-vit/prompts.txt) | Diperbarui (*Modified*) | Mencatat riwayat prompt aktif pengguna dan menyematkan prompt ringkas perbaikan Figure 3 untuk AI agent. |
| 4 | [`docs/sessions/2026-10-29_penyempurnaan-paper-outline-v1.1-evaluasi-figure3-vit-dan-sinkronisasi-prompts.md`](file:///D:/Research/face-race-gender-classification-using-multi-domain-vit/docs/sessions/2026-10-29_penyempurnaan-paper-outline-v1.1-evaluasi-figure3-vit-dan-sinkronisasi-prompts.md) | Dibuat (*New*) | Dokumentasi resmi sesi kerja komprehensif pada direktori `docs/sessions/`. |
| 5 | [`sessions/session_2026-10-29_penyempurnaan-paper-outline-v1.1-evaluasi-figure3-vit-dan-sinkronisasi-prompts.md`](file:///D:/Research/face-race-gender-classification-using-multi-domain-vit/sessions/session_2026-10-29_penyempurnaan-paper-outline-v1.1-evaluasi-figure3-vit-dan-sinkronisasi-prompts.md) | Dibuat (*New*) | Berkas cermin dokumentasi sesi kerja pada direktori `sessions/`. |

---

## 4. STATUS DAN KESIAPAN TAHAP SELANJUTNYA

* **Integritas Outline Manuskrip**: Berkas [paper_outline_v1.1.md](file:///D:/Research/face-race-gender-classification-using-multi-domain-vit/paper_outline_v1.1.md) telah 100% matang, baku, dan secara komprehensif memuat seluruh rencana mitigasi atas 17 komentar reviewer IEEE Access.
* **Aset Visual Naskah**:
  - Figure 1: `images/method.png` (sudah terintegrasi).
  - Figure 2: `images/sample_*.jpg` komposit (sudah terintegrasi).
  - Figure 3: `images/vit_v2.0.png` (sudah terintegrasi dan di-commit).
  - Figure 4: `images/confusion_matrix_*.png` komparatif (sudah terintegrasi).
* **Rekomendasi Langkah Berikutnya**:
  1. Melakukan penulisan dan penyelarasan draf bab naskah utama di direktori [`paper/`](file:///D:/Research/face-race-gender-classification-using-multi-domain-vit/paper/) mengacu secara presisi pada [paper_outline_v1.1.md](file:///D:/Research/face-race-gender-classification-using-multi-domain-vit/paper_outline_v1.1.md).
  2. Melakukan sinkronisasi ke berkas LaTeX naskah (`.tex`) dan kompilasi naskah revisi bersih serta *Highlighted PDF*.
