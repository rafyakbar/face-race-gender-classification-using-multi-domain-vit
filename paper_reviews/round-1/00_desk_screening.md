# Laporan Skrining Meja Editor (Desk Screening Report)

**Judul Naskah**: Multi-Domain Vision Transformer Fusion for Intersectional Demographic Classification from Facial Images  
**Penulis**: Ricky Eka Putra, Rezky Arisanti Putri, Yuni Yamasari, Rafy Aulia Akbar  
**Afiliasi**: Department of Informatics, Faculty of Informatics, Universitas Negeri Surabaya, Indonesia  
**Target Publikasi**: **IEEE Access**  
**Tanggal Evaluasi**: 2026-09-27  
**Evaluator**: Editor-in-Chief (EIC) Desk Office  
**Keputusan Skrining Meja**: **`DESK_PASS`** (Proceed to Full Panel Peer Review)

---

## 1. Evaluasi 4 Pilar Skrining Awal Meja Editor

### A. Kesesuaian Ruang Lingkup (Scope & Venue Fit for IEEE Access)
- **Kesesuaian Topik**: Topik yang diangkat—pengenalan atribut demografis wajah (ras dan gender secara interseksional) memanfaatkan arsitektur Vision Transformer (ViT) dan optimasi algoritma pembelajaran mesin klasik—sangat selaras dengan cakupan multidisiplin *IEEE Access*, khususnya pada area *Computer Vision*, *Pattern Analysis*, *Biometrics*, dan *Applied Machine Learning*.
- **Nilai Tambah & Daya Tarik Pembaca**: Naskah menyasar isu krusial dalam keandalan dan disparitas sistem biometrik modern. Meskipun terdapat kekhawatiran awal mengenai tingkat kebaruan arsitektural (karena bertumpu pada ekstraksi fitur laten offline dari model komunitas yang dibekukan), pertanyaan penelitian yang diajukan memiliki relevansi saintifik yang memadai untuk dikirim ke penelaahan sejawat penuh.
- **Hasil**: **MEMENUHI SYARAT (PASS)**

### B. Kepatuhan Format & Kelengkapan Struktur (Format & Structure Hygiene)
- **Struktur IMRaD**: Naskah tersusun secara lengkap dan terorganisir rapi mengikuti konvensi ilmiah standar:
  - *Title & Abstract*: Abstrak memuat latar belakang, metode (3 model ViT, 4 classifier, 5-Fold Stratified CV), temuan kuantitatif eksplisit (Akurasi 93.70%, F1 93.69%), serta kata kunci.
  - *Section I (Introduction)*: Menguraikan latar belakang, kesenjangan riset, usulan solusi, dan 4 butir kontribusi ilmiah.
  - *Section II (Related Works)*: Memetakan literatur transisi CNN ke ViT, bias demografis, dan studi multi-domain.
  - *Section III (Materials and Methods)*: Dirinci ke dalam 8 subbab (A sampai H) lengkap dengan formulasi matematis Persamaan (1) hingga (17).
  - *Section IV (Results and Discussion)*: Memuat benchmark komprehensif pada Tabel VII s/d XII serta Gambar 1 s/d 4.
  - *Section V (Conclusion)*: Menyajikan sintesis temuan, keterbatasan riset, dan arah pengembangan mendatang.
  - *Section VI (References)*: Menyertakan 51 referensi terformat gaya IEEE dengan DOI aktif dan cakupan publikasi mutakhir (2021–2026).
  - *Section VII (Biographies)*: Memuat biodata naratif lengkap beserta slot foto untuk seluruh 4 penulis sesuai standar wajib *IEEE Access*.
- **Hasil**: **MEMENUHI SYARAT (PASS)**

### C. Integritas Orisinalitas & Etika Awal (Integrity & Early Ethics Screening)
- **Transparansi Data**: Naskah secara eksplisit menyebutkan penggunaan dataset publik DemogPairs (10,800 citra seimbang melintasi 6 subkelompok ras-gender).
- **Potensi Cacat Etika Dini**: Pengenalan demografis wajah (ras dan gender) merupakan ranah sensitif biometrik manusia yang memerlukan kepatuhan etika ketat (*Responsible AI*). Namun, ketiadaan pernyataan persetujuan etik (*Ethics Statement*) pada draf awal ini belum tergolong sebagai pelanggaran fatal meja (*desk reject blocker*), melainkan menjadi catatan perbaikan penting yang akan dievaluasi mendalam oleh Reviewer 3.
- **Hasil**: **MEMENUHI SYARAT (PASS DENGAN CATATAN PENELAAHAN)**

### D. Penyaringan Cacat Fatal Dini (Fatal Flaw Screening)
- **Pemeriksaan Skala Eksperimen**: Eksperimen melibatkan ukuran sampel yang memadai (10,800 citra dengan partisi 80/20 train/test: 8,640 train dan 2,160 test), pengujian 7 konfigurasi ablasi fitur, 4 algoritma pembelajaran mesin (RF, GNB, LR, SVM), serta GridSearchCV dengan total 38,010 proses *fit*. Naskah ini bukan eksperimen berskala kecil (*toy problem*).
- **Prosedur Data Leakage Dini**: Pipeline pemrosesan mencantumkan fitting modul Scaler dan PCA secara eksklusif hanya pada fold data latih di dalam GridSearchCV, yang menunjukkan kehati-hatian metodologis awal.
- **Hasil**: **BEBAS CACAT FATAL AWAL (PASS)**

---

## 2. Kesimpulan & Rekomendasi Editorial

Naskah **LOLOS SKRINING MEJA (`DESK_PASS`)** dan diteruskan ke putaran penelaahan sejawat penuh (*Full Panel Peer Review*). 

Panel evaluasi independen dibentuk dengan 5 persona reviewer:
1. **Editor-in-Chief (EIC)** — Fokus pada kesesuaian ruang lingkup *IEEE Access*, kebaruan relatif, dan kejelasan struktur naskah.
2. **Reviewer 1 (Methodology)** — Fokus pada validitas desain eksperimental, audit pemisahan data tingkat identitas (*subject-disjoint split*), dan signifikansi statistik.
3. **Reviewer 2 (Domain Expert)** — Fokus pada akurasi representasi biometrik wajah, validitas checkpoint transformer upstream, dan kelengkapan baseline SOTA.
4. **Reviewer 3 (Cross-Perspective)** — Fokus pada metrik keadilan algoritmik formal, implikasi etika pengenalan demografis, dan efisiensi komputasi inferensi.
5. **Devil's Advocate (Adversarial Evaluator)** — Fokus pada pengujian skeptis terhadap hipotesis keunggulan tri-domain (paradoks delta 0.41% / 9 sampel) dan anomali perilaku pengklasifikasi.
