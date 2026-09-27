### Peer Review Report — Reviewer 2 (Domain Expert)

- **Reviewer Role**: Peer Reviewer 2 (Domain Expert — Facial Biometrics & Transformer Architectures)
- **Dimensi Tanggung Jawab**: `D2` (domain_accuracy)
- **Target Venue**: **IEEE Access**
- **Rekomendasi**: **Minor Revision** *(Konsolidasi Penilaian Panel Multi-Model)*
- **Confidence Score**: 5 / 5 (Sangat Tinggi — Kepakaran dalam Rekognisi Atribut Wajah, SOTA Benchmarks & Representasi Visi)

---

## 1. Rencana Skoring Pra-Komitmen (Fase 1: Paper-Blind Phase)

Sebelum menelaah draf naskah secara penuh, Reviewer 2 menetapkan tolok ukur kepakaran domain:
- `what_to_look_for`:
  - Akurasi representasi teoretis pengenalan atribut wajah (biometrik invariant vs sinyal ekspresi dinamis vs morfologi penuaan biologis).
  - Kelayakan komparasi terhadap literatur *State-of-the-Art* (SOTA) terkini dalam biometrik wajah dan klasifikasi demografis (FairFace, UTKFace, DemogPairs).
  - Transparansi dan reprodusibilitas model backbone upstream (arsitektur, data pra-latih, bobot pre-trained, dan metrik tugas asli).
  - Bukti visual pemisahan representasi (misal: proyeksi t-SNE atau UMAP) untuk memverifikasi keterpisahan klaster antarkelas pada fusi multi-domain.
  - Justifikasi teoretis kognitif mengenai bagaimana domain ekspresi dan usia memberikan kontribusi komplementer terhadap klasifikasi ras dan gender.
- `what_triggers_block`:
  - Kesalahan fatal dalam pemahaman konsep biometrik wajah atau pengabaian total terhadap literatur SOTA pengenalan wajah transformer dalam 3 tahun terakhir.
- `what_triggers_warn`:
  - Benchmark pembanding hanya terbatas pada karya internal penulis sendiri tanpa menyertakan model acuan standar industri/akademik (seperti ResNet standar, ViT ImageNet standar, atau CLIP/DINOv2).
  - Penggunaan checkpoint model publik dari repositori komunitas pihak ketiga tanpa rincian provenansi data latih (*pre-training lineage*).
  - Ketiadaan visualisasi representasi laten berdimensi tinggi.
- `what_triggers_fatal`:
  - Misrepresentasi mendasar terhadap dataset biometrik atau pelaporan hasil yang secara fisik/matematis mustahil.

`[CONTRACT-ACKNOWLEDGED]`

---

## 2. Ringkasan Penilaian Domain (Fase 2: Paper-Visible Phase)

Naskah ini memberikan pemaparan yang sangat kaya mengenai domain biometrik wajah, eksplorasi representasi Vision Transformer (ViT), dan fenomena tumpang tindih fenotipe (*phenotypic overlap*) antarras pada citra wajah. Penulis berhasil merangkum transisi historis dari fitur konvensional buatan tangan (handcrafted features) menuju ekstraksi representasi berbasis atensi global Multi-Head Self-Attention (MHSA).

Meskipun fondasi domain naskah ini sudah sangat baik, konsolidasi ulasan panel pakar domain mengidentifikasi beberapa catatan penting:
1. **Perbandingan Baseline yang Bersifat Sirkular (*Insular Benchmarking*)**: Pada Tabel XII, seluruh model pembanding pada dataset DemogPairs (MD-ViT dan Dual-ViT) merupakan publikasi internal kelompok penulis sendiri (Ref [19] dan [20]). Tidak ada evaluasi terhadap baseline model tunggal standar—misalnya ResNet-50 standar biometrik, ViT-Base pra-latih ImageNet murni, atau foundation model representasi visual seperti CLIP ViT-B/16 linear probe. Ketiadaan baseline standar ini menyulitkan pembaca IEEE Access untuk memastikan apakah keunggulan performa (93.70%) benar-benar berasal dari sifat komplementer multi-domain atau semata-mata karena kapasitas arsitektur transformer.
2. **Opasitas Provenansi Checkpoint Komunitas HuggingFace**: Ketiga model transformer yang digunakan diambil dari checkpoint pengguna HuggingFace (`skutaada/VIT-VGGFace`, `dima806/facial_emotions_image_detection`, dan `dima806/facial_age_image_detection`). Penulis belum memaparkan secara transparan silsilah data pra-latih, fungsi objektif, atau potensi kontaminasi data pra-latih dengan DemogPairs.
3. **Ketiadaan Visualisasi Feature Embedding**: Klaim bahwa fusi multi-domain mempertegas separabilitas klaster demografis belum didukung oleh visualisasi manifold (t-SNE / UMAP).

---

## 3. Poin Kekuatan Domain (Strengths)

- **S1: Pemahaman Evolusi Paradigma yang Koheren (`D2`)**:
  - Tinjauan pustaka mengonstruksi narasi evolusi yang logis: dari deskriptor buatan tangan → CNN region-spesifik ([11]) → multi-task CNN ([12]) → ViT ([14], [17]) → multi-domain ViT fusion ([19], [20]).
  - Evidence Anchor: `[section: 02_related-works]`
- **S2: Formulasi Matematis Arsitektur ViT yang Presisi (`D2`)**:
  - Formulasi matematis ViT-Base pada Persamaan (1) hingga (5) disajikan secara ringkas dan akurat, mencakup proyeksi patch linier, embedding posisi, MHSA, MLP blok, Layer Normalization, dan ekstraksi representasi token `[CLS]`.
  - Evidence Anchor: `[section: 03_materials-and-methods_b-vision-transformer]`
- **S3: Skema Ablasi Fitur yang Sangat Sistematis (`D2`)**:
  - Tujuh konfigurasi ablasi (3 domain tunggal, 3 domain ganda, 1 tri-domain) pada Tabel II memberikan pemetaan empiris yang jelas mengenai kontribusi individual dan interaksi antardomain.
  - Evidence Anchor: `[table: II]`
- **S4: Karakterisasi Domain Tumpang Tindih Fenotipe Antarras (`D2`)**:
  - Diskusi pada Bagian IV-D mengenai konsentrasi galat klasifikasi antarras dalam gender yang sama (khususnya antara Asian Females dan White/Black Females pada Gambar 4) selaras dengan fenomena kognitif *Other-Race Effect* (ORE) dan *phenotypic overlap* pada representasi visual wajah.
  - Evidence Anchor: `[section: 04_results-and-discussion_d-error-pattern-assessment]`, `[figure: 4]`

---

## 4. Kelemahan Domain & Catatan Perbaikan (Weaknesses)

### W1: Komparasi Benchmark Hanya dengan Self-Citations & Ketiadaan Baseline Standar
- **ID Isu**: `ISSUE-DOM-01`
- [dimension: D2]
- Severity: MAJOR
- **Verbatim Trigger**: `"what_triggers_warn: benchmark pembanding hanya terbatas pada karya internal penulis sendiri tanpa menyertakan model acuan standar industri/akademik"`
- **Evidence Anchor**: `[table: 12]`, `[section: 04_results-and-discussion_e-comparison-with-prior-studies]`
- **Deskripsi Temuan**:
  Pada Tabel XII ([Table XII](04_results-and-discussion_e-comparison-with-prior-studies.md#tab12)), penulis menempatkan performa model Tri-Domain ViT + SVM (93.70%) berhadapan dengan MD-ViT (89.07%) dan Dual-ViT (92.41%). Kedua studi pembanding tersebut berasal dari tim peneliti yang sama (Putri et al. [19], [20]).
  
  Dalam ranah biometrik wajah modern, pembaca jurnal internasional akan mengajukan pertanyaan kritis: *Apakah fusi tiga model ViT (total ~258 juta parameter) benar-benar diperlukan, ataukah sebuah backbone tunggal standar yang kuat (seperti ResNet-50 standar biometrik, ViT-Base pra-latih ImageNet-1k, atau CLIP ViT-B/16 linear probe) dapat mencapai akurasi 93–94% pada DemogPairs tanpa fusi multi-domain?*
  
  Ketiadaan baseline model tunggal non-fusi standar eksternal pada dataset DemogPairs melemahkan klaim bahwa keunggulan performa berasal secara spesifik dari sifat komplementer multi-domain.
- **Rekomendasi Aksi**:
  Tambahkan baris evaluasi baseline standar pada Tabel XII (atau draf pembahasan pendukung), minimal:
  1. Baseline representasi model tunggal standar: misalnya fitur dari ViT-Base murni pra-latih ImageNet (tanpa adaptasi domain wajah/emosi/usia) atau ResNet-50 standar dengan pengklasifikasi SVM/LR yang sama.
  2. Alternatif lain: sertakan pembanding dari literatur orisinal dataset DemogPairs (Hupont & Fernández, 2019 [25]) untuk memperlihatkan bagaimana performa model ini dibandingkan dengan tolok ukur awal dataset tersebut.

### W2: Opasitas Silsilah Data Pra-Latih Checkpoint Komunitas HuggingFace
- **ID Isu**: `ISSUE-DOM-02`
- [dimension: D2]
- Severity: MINOR
- **Verbatim Trigger**: `"what_triggers_warn: penggunaan checkpoint model publik dari repositori komunitas pihak ketiga tanpa rincian provenansi data latih"`
- **Evidence Anchor**: `[section: 03_materials-and-methods_b-vision-transformer]`
- **Deskripsi Temuan**:
  Penulis mengadopsi tiga model ViT pra-latih dari HuggingFace Hub:
  - `skutaada/VIT-VGGFace`
  - `dima806/facial_emotions_image_detection`
  - `dima806/facial_age_image_detection`
  
  Meskipun model-model ini mudah diakses, naskah tidak memberikan rincian teknis mengenai:
  - Arsitektur spesifik (apakah semuanya `vit-base-patch16-224`?).
  - Dataset pra-latih yang digunakan oleh kreator checkpoint tersebut (misal: VGGFace2 untuk skutaada; FER2013 atau AffectNet untuk model emosi dima806; UTKFace atau IMDB-WIKI untuk model usia dima806).
  - Apakah dataset pra-latih tersebut memiliki irisan subjek/gambar dengan dataset DemogPairs?
  
  Ketiadaan informasi provenansi ini menimbulkan celah reprodusibilitas dan kejelasan saintifik bagi komunitas domain biometrik.
- **Rekomendasi Aksi**:
  Perluas Bagian III-B dengan satu tabel atau paragraf ringkas mengenai arsitektur dasar, korpus pelatihan sumber, dan metrik akurasi upstream dari ketiga model checkpoint HuggingFace tersebut, serta sertakan konfirmasi bahwa dataset pra-latih upstream tidak mencemari integritas pengujian DemogPairs.

### W3: Ketiadaan Visualisasi Feature Embedding (t-SNE / UMAP)
- **ID Isu**: `ISSUE-DOM-03`
- [dimension: D2]
- Severity: MINOR
- **Verbatim Trigger**: `"what_triggers_warn: ketiadaan visualisasi representasi laten berdimensi tinggi"`
- **Evidence Anchor**: `[section: 04_results-and-discussion_b-feature-ablation-study]`
- **Deskripsi Temuan**:
  Untuk artikel yang berfokus pada fusi fitur representasi laten, penyertaan proyeksi manifold dua dimensi menggunakan t-SNE atau UMAP pada fitur data uji held-out (membandingkan klaster fitur domain tunggal Face vs dual-domain vs tri-domain) akan memberikan bukti visual yang sangat kuat bahwa fusi fitur multi-domain benar-benar mempertegas jarak pemisah antarkelas interseksional (*inter-cluster separability*). Saat ini, klaim pemisahan hanya bertumpu pada metrik numerik tabel.
- **Rekomendasi Aksi**:
  Sertakan diagram plot scatter t-SNE/UMAP dari ruang representasi data uji pada Bagian IV-B untuk memperlihatkan evolusi keterpisahan klaster dari domain tunggal ke tri-domain.

### W4: Integrasi Landasan Teori Kognitif Visi Wajah (Dual-Stream Face Processing)
- **ID Isu**: `ISSUE-DOM-04`
- [dimension: D2]
- Severity: MINOR
- **Evidence Anchor**: `[section: 04_results-and-discussion_b-feature-ablation-study]`, `[section: 01_introduction]`
- **Deskripsi Temuan**:
  Pada Bagian IV-B, penulis mendiskusikan bahwa penambahan fitur usia dan emosi ke fitur wajah meningkatkan akurasi, namun menambahkan kalimat hati-hati: *"tanpa mengklaim bahwa kontribusi informasi tersebut bersifat ortogonal atau komplementer mutlak secara teoretis."*
  
  Di ranah kognisi visual wajah dan visi komputer biometrik, terdapat landasan teori mapan mengenai pengolahan wajah (misalnya model fungsional Bruce & Young 1986 serta model neural Haxby et al. 2000) yang mempostulatkan bahwa karakteristik invarian wajah (identitas, ras, gender) dan karakteristik dinamis/berubah (ekspresi emosi, penuaan biologis) diproses melalui jalur representasi yang saling berinteraksi namun memiliki fokus fitur berbeda di korteks visual. Mengaitkan temuan fusi empiris ini dengan teori persepsi wajah tersebut akan memperkuat argumentasi domain naskah secara signifikan.
- **Rekomendasi Aksi**:
  Perkaya diskusi pada Bagian IV-B dengan 1–2 kalimat yang menghubungkan temuan empiris komplementaritas fitur dengan literatur neurologis/kognitif pemrosesan wajah invarian vs dinamis.

---

## 5. Ringkasan Status Dimensi Reviewer 2

| Dimensi | Status | Justifikasi Evaluasi |
|:---:|:---:|---|
| **D2** (*domain_accuracy*) | **`WARN`** | Teori biometrik dan arsitektur ViT dipahami dengan baik, namun terdapat 1 kelemahan `MAJOR` (ketiadaan baseline eksternal non-penulis sendiri) dan 3 kelemahan `MINOR` (opasitas provenansi checkpoint HF, ketiadaan visualisasi t-SNE/UMAP, dan pendalaman teori persepsi wajah). |
