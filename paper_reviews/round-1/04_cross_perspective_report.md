### Peer Review Report — Reviewer 3 (Cross-Perspective)

- **Reviewer Role**: Peer Reviewer 3 (Cross-Disciplinary Perspective — Algorithmic Fairness, AI Ethics, & Systems Engineering)
- **Dimensi Tanggung Jawab**: `D4` (cross_disciplinary_relevance)
- **Target Venue**: **IEEE Access**
- **Rekomendasi**: **Minor Revision** *(Konsolidasi Penilaian Panel Multi-Model)*
- **Confidence Score**: 5 / 5 (Sangat Tinggi — Keadilan Algoritmik, Etika AI & Kelayakan Rekayasa Sistem)

---

## 1. Rencana Skoring Pra-Komitmen (Fase 1: Paper-Blind Phase)

Sebelum menelaah draf naskah secara penuh, Reviewer 3 menetapkan tolok ukur lintas-disiplin:
- `what_to_look_for`:
  - Kepatuhan terhadap metrik keadilan algoritmik formal (*algorithmic fairness metrics*) jika naskah mengklaim fokus pada isu bias/fairness (misal: *Equalized Odds*, *Demographic Parity*, *Equal Opportunity difference*).
  - Pembingkaian etika yang bertanggung jawab (*Responsible AI*) terhadap kategorisasi rasial dan gender pada sistem visi komputer, termasuk kesadaran bahwa ras merupakan konstruksi sosial dan risiko penyalahgunaan pengawasan biometrik (*mass surveillance/racial profiling*).
  - Ketersediaan pernyataan persetujuan etik (*Ethics Statement*) dan informed consent pada penggunaan data sekunder wajah manusia.
  - Kelayakan adopsi praktis dan analisis biaya komputasi inferensi (*inference latency, FLOPs, memory footprint*) pada skenario penerapan riil.
- `what_triggers_block`:
  - Klaim kontribusi keadilan algoritmik tanpa data audit disparitas yang transparan, atau pengabaian total terhadap etika diskriminasi demografis.
  - Model menuntut sumber daya komputasi yang ekstrem tanpa sedikit pun justifikasi efisiensi untuk aplikasi nyata.
- `what_triggers_warn`:
  - Mencantumkan *algorithmic fairness* sebagai kata kunci utama naskah namun tidak menghitung metrik keadilan matematis standar.
  - Ketiadaan profil latensi inferensi dan jejak parameter untuk model fusi multi-backbone.
  - Ketiadaan pernyataan kepatuhan etika data biometrik wajah.
- `what_triggers_fatal`:
  - Promosi teknologi yang secara eksplisit melanggar hak asasi manusia atau hukum perlindungan data pribadi internasional.

`[CONTRACT-ACKNOWLEDGED]`

---

## 2. Ringkasan Penilaian Lintas-Perspektif (Fase 2: Paper-Visible Phase)

Naskah ini menyentuh area yang sangat krusial bagi masyarakat modern: disparitas performa biometrik wajah pada persilangan kelompok demografis (*intersectional demographics*). Penulis layak diapresiasi karena melakukan evaluasi granular pada enam subkelompok ras-gender (Tabel XI) dan secara jujur menampilkan data di mana subkelompok rentan seperti *Black Females* mengalami performa terendah dibandingkan subkelompok dominan seperti *White Males*.

Kendati demikian, dari kacamata etika kecerdasan buatan, keadilan algoritmik, dan rekayasa sistem praktis, terdapat tiga kelemahan utama yang disepakati oleh panel:
1. **Disparitas Metrik Keadilan Formal vs. Klaim Kata Kunci (*Algorithmic Fairness Gap*)**: Penulis mencantumkan *"algorithmic fairness"* sebagai kata kunci abstrak ([Keywords](00_abstract.md#keywords)), namun naskah tidak mengukur satu pun metrik keadilan algoritmik formal (seperti *Equalized Odds*, *Equal Opportunity Difference*, atau *Disparate Impact*). Penulis hanya melaporkan rentang F1-Score (disparitas 4.40 pp), padahal jika ditinjau dari metrik *Recall* pada Tabel XI, terdapat kesenjangan tajam sebesar 7.50% antara *White Males* (96.94%) dan *Black Females* (89.44%). Kesenjangan ini mereplikasi temuan klasik *Gender Shades* (Buolamwini & Gebru, 2018).
2. **Ketiadaan Analisis Biaya Komputasi & Efisiensi Inferensi**: Menjalankan tiga model ViT-Base sekaligus membutuhkan ~258 juta parameter dan tiga *forward passes*. Penulis belum menyajikan profil latensi inferensi (milidetik per citra) atau konsumsi memori GPU pada skenario inferensi nyata.
3. **Ketiadaan Pernyataan Etika Data Biometrik & Refleksi Dual-Use**: Naskah belum menyertakan *Ethical Statement* formal terkait penggunaan citra wajah DemogPairs serta belum memberikan refleksi mengenai risiko penyalahgunaan sistem klasifikasi ras (*racial profiling*).

---

## 3. Poin Kekuatan Lintas-Perspektif (Strengths)

- **S1: Transparansi Pelaporan Disparitas Subkelompok Interseksional (`D4`)**:
  - Penulis tidak menyembunyikan disparitas performa di balik metrik agregat global, melainkan secara transparan membongkar kinerja granular per subkelompok pada Tabel XI dan matriks konfusi Gambar 4, memperlihatkan bahwa *Black Females* masih merupakan kohort paling rentan terhadap kesalahan klasifikasi.
  - Evidence Anchor: `[table: 11]`, `[section: 04_results-and-discussion_c-intersectional-subgroup-performance]`
- **S2: Pemisahan Data Terkontrol Mengurangi Bias Proporsi Sampel (`D4`)**:
  - Penggunaan dataset DemogPairs dengan kuota seimbang tepat 1,800 citra per subkelompok (360 citra per kelas uji) memastikan bahwa disparitas performa yang teramati bukan artefak dari ketimpangan jumlah data latih (*class imbalance artifact*).
  - Evidence Anchor: `[section: 03_materials-and-methods_a-dataset]`, `[table: 1]`
- **S3: Pengakuan Keterbatasan yang Jujur & Arah Responsible AI (`D4`)**:
  - Pada Bagian IV-C dan Bagian V, penulis secara terbuka mengakui bahwa evaluasi ini bukan audit keadilan algoritmik komprehensif serta menekankan perlunya tata kelola etika kecerdasan buatan (*Responsible AI*), mekanisme manusia dalam lingkaran kendali (*human-in-the-loop*), dan visual explainability (Attention Rollout/Grad-CAM).
  - Evidence Anchor: `[section: 04_results-and-discussion_c-intersectional-subgroup-performance]`, `[section: 05_conclusion]`

---

## 4. Kelemahan Lintas-Perspektif & Catatan Perbaikan (Weaknesses)

### W1: Ketidakhadiran Metrik Keadilan Algoritmik Formal & Analisis Disparitas Black Females
- **ID Isu**: `ISSUE-CROSS-01`
- [dimension: D4]
- Severity: MAJOR
- **Verbatim Trigger**: `"what_triggers_warn: mencantumkan algorithmic fairness sebagai kata kunci utama naskah namun tidak menghitung metrik keadilan matematis standar"`
- **Evidence Anchor**: `[section: 00_abstract]`, `[table: 11]`, `[section: 04_results-and-discussion_c-intersectional-subgroup-performance]`
- **Deskripsi Temuan**:
  Pada abstrak dan kata kunci, naskah menonjolkan *"algorithmic fairness"* sebagai kontribusi sentral. Namun, pada Bagian III-H dan IV-C, prosedur evaluasi hanya mengandalkan metrik performa standar (Akurasi, Presisi, Recall, F1-Score). Penulis mengukur disparitas hanya sebagai selisih rentang F1 tertinggi dan terendah ($96.14\% - 91.74\% = 4.40\%$).
  
  Dalam literatur komputasi keadilan modern (*Fairness in Machine Learning*), evaluasi keadilan menuntut kuantifikasi formal berbasis kriteria independensi (*demographic parity*), pemisahan (*equalized odds / equal opportunity*), atau kecukupan (*predictive parity*). Apabila ditilik dari Tabel XI:
  - Sensitivitas/Recall *White Males*: 96.94%
  - Sensitivitas/Recall *Black Females*: 89.44%
  - Kesenjangan *Equal Opportunity* ($\Delta \text{TPR}$): **7.50 percentage points**!
  
  Kesenjangan 7.50% ini mereplikasi temuan seminal *Gender Shades* (Buolamwini & Gebru, 2018), di mana subjek wanita berkulit gelap menanggung beban kesalahan deteksi tertinggi. Menghindari penyebutan metrik keadilan formal sembari mengklaim kontribusi *algorithmic fairness* menciptakan ketidaksinkronan klaim naskah.
- **Rekomendasi Aksi**:
  1. Tambahkan formulasi matematis dan tabel metrik keadilan algoritmik standar pada Bagian III-H dan IV-C:
     - *Equal Opportunity Difference* ($\max |\text{Recall}_a - \text{Recall}_b|$)
     - *Equalized Odds Ratio*
     - *Demographic Disparity Ratio*
  2. Berikan diskusi kritis pada Bagian IV-C mengenai implikasi sosial dari drop recall 7.50% pada *Black Females*, serta langkah mitigasi algoritmik yang relevan.

### W2: Ketiadaan Analisis Biaya Komputasi dan Latensi Inferensi
- **ID Isu**: `ISSUE-CROSS-02`
- [dimension: D4]
- Severity: MINOR
- **Verbatim Trigger**: `"what_triggers_warn: ketiadaan profil latensi inferensi dan jejak parameter untuk model fusi multi-backbone"`
- **Evidence Anchor**: `[section: 03_materials-and-methods_0-overview]`, `[section: 04_results-and-discussion_a-global-performance]`
- **Deskripsi Temuan**:
  Arsitektur yang diusulkan mengombinasikan tiga model ViT-Base terpisah (`skutaada/VIT-VGGFace`, `dima806/facial_emotions...`, `dima806/facial_age...`). Masing-masing model ViT-Base memiliki sekitar 86 juta parameter, sehingga total parameter representasi mencapai $\approx 258\text{ juta parameter}$, menghasilkan vektor fitur berdimensi 2,304.
  
  Meskipun ekstraksi fitur dilakukan secara *offline* untuk pelatihan pengklasifikasi SVM, pada fase deployment/inferensi dunia nyata, setiap citra wajah baru wajib melewati ketiga model ViT tersebut sebelum diklasifikasikan oleh SVM. Naskah sama sekali tidak melaporkan:
  - Waktu ekstraksi fitur offline dan waktu tuning GridSearchCV (38,010 fits).
  - Waktu latensi inferensi per citra (misal: milidetik pada GPU RTX 3060/4090 atau CPU standar).
  - Alokasi memori VRAM GPU selama ekstraksi fitur simultan.
  - Komparasi *throughput* (FPS) antara model domain tunggal (Face), domain ganda (Emotion+Face), dan tiga domain (Face+Emotion+Age).
  
  Bagi praktisi biometrik yang mempertimbangkan penerapan pada perangkat *edge* atau kontrol akses biometrik, peningkatan akurasi marjinal 0.41% harus ditimbang terhadap peningkatan beban komputasi 300%.
- **Rekomendasi Aksi**:
  Tambahkan tabel atau paragraf ringkas pada Bagian IV yang melaporkan estimasi jumlah parameter, ukuran memori fitur, dan waktu latensi inferensi per citra untuk memberikan gambaran kelayakan implementasi praktis.

### W3: Ketiadaan Pernyataan Etika Biometrik & Refleksi Risiko Dual-Use
- **ID Isu**: `ISSUE-CROSS-03`
- [dimension: D4]
- Severity: MINOR
- **Verbatim Trigger**: `"what_triggers_warn: ketiadaan pernyataan kepatuhan etika data biometrik wajah"`
- **Evidence Anchor**: `[section: 01_introduction]`, `[section: 05_conclusion]`
- **Deskripsi Temuan**:
  Klasifikasi ras otomatis berbasis citra wajah merupakan teknologi bernilai ganda (*dual-use technology*) yang memicu perdebatan etika sengit di komunitas visi komputer global. Ras bukanlah kategori biologis diskret yang kaku, melainkan konstruksi sosial yang cair dan memiliki kontinum fenotipe luas. Penyederhanaan menjadi tiga kelas makro (*Asian, Black, White*) dapat mengundang risiko pengawasan diskriminatif (*racial profiling*) jika disalahgunakan dalam penegakan hukum atau seleksi rekrutmen.
  
  Selain itu, naskah belum menyertakan *Ethical Statement* formal yang mengonfirmasi legitimasi penggunaan dataset publik DemogPairs dan perlindungan privasi subjek biometrik.
- **Rekomendasi Aksi**:
  Sertakan subbab/paragraf refleksi etika di Bagian V atau sebelum referensi yang memuat *Ethical Compliance Statement* serta penegasan bahwa kategorisasi rasial dibatasi oleh taksonomi dataset untuk tujuan audit bias dan bukan melegitimasi klasifikasi rasial esensialis.

---

## 5. Ringkasan Status Dimensi Reviewer 3

| Dimensi | Status | Justifikasi Evaluasi |
|:---:|:---:|---|
| **D4** (*cross_disciplinary_relevance*) | **`WARN`** | Analisis subkelompok disajikan sangat transparan, namun terdapat 1 kelemahan `MAJOR` (klaim keadilan algoritmik tanpa metrik keadilan formal) dan 2 kelemahan `MINOR` (analisis latensi komputasi inferensi dan kepatuhan etika data biometrik). |
