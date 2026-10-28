# Revision Tracking Table: Access-2026-50857

> Matriks pelacakan status resolusi dan Nested Commitment Ledger (Schema 11 / Kong et al. 2026 §7.4.3).  
> Memastikan seluruh janji perbaikan memiliki bukti nyata di naskah dan bebas desinkronisasi indeks (#268).

---

## 1. Tabel Pelacakan Resolusi Komentar

| ID | Reviewer | Tipe | Seksion | Ringkasan Isu | Rencana Tindakan Resolusi | Lokasi Perubahan | Status | Alasan (Jika Non-Fulfilled) |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| `AE-1` | EIC | `Major` | `procedural` | Penolakan Biner & Batas Resubmission | Mengakomodasi seluruh masukan R1 dan R2 secara tuntas tanpa butir terlewat (*zero-orphan*). | `Response Letter` | `RESOLVED` | - |
| `AE-2` | EIC | `Major` | `administrative` | Persyaratan Tiga Berkas Wajib | Menyiapkan 3 berkas unggah: Author Response, Highlighted PDF, dan Clean Manuscript (LaTeX ZIP & PDF). | `Response Letter` | `RESOLVED` | - |
| `AE-3` | EIC | `Major` | `administrative` | Formulir Penambahan Penulis | Menyusun formulir Request for Byline Change untuk penambahan Dr. Shukor Sanim Mohd Fauzi (UiTM). | `Request-for-Byline-Change.md` | `RESOLVED` | - |
| `AE-4` | EIC | `Editorial` | `administrative` | Kepatuhan Checklist 10-Butir | Memverifikasi kepatuhan naskah terhadap 10 butir checklist resmi IEEE Access sebelum submit. | `Resubmission-Checklist.md` | `RESOLVED` | - |
| `R1-1` | R1 | `Minor` | `01_introduction.md` | Pendahuluan Terlalu Panjang | Meringkas Seksi I dengan memadatkan latar belakang umum dan menonjolkan 4 poin kontribusi utama. | `01_introduction.md` | `RESOLVED` | - |
| `R1-2` | R1 | `Minor` | `02_related-works.md` | Restrukturisasi Studi Terkait & Rumus | Menata Seksi II ke dalam 3 tema dan menyertakan formulasi matematis MHSA serta fusi fitur. | `02_related-works.md` | `RESOLVED` | - |
| `R1-3` | R1 | `Major` | `03_materials-and-methods_b-vision-transformer.md` | Redesain & Penjelasan Figure 3 | Merancang ulang Gambar 3 diagram arsitektur ViT vektor resolusi tinggi dan memperdalam narasi. | `03_materials-and-methods_b-vision-transformer.md` | `RESOLVED` | - |
| `R1-4` | R1 | `Minor` | `04_results-and-discussion_d-error-pattern-assessment.md` | Pembahasan Mendalam Dinamika Figure 4 | Menganalisis matriks konfusi 6×6 secara mendalam, menguraikan pola kesalahan intra-gender vs lintas-gender. | `04_results-and-discussion_d-error-pattern-assessment.md` | `RESOLVED` | - |
| `R1-5` | R1 | `Major` | `03_materials-and-methods_a-dataset.md` | Detail Dataset & Biaya Waktu (*Time Cost*) | Merinci spesifikasi subjek DemogPairs dan menyajikan tabel profil efisiensi waktu komputasi. | `03_materials-and-methods_a-dataset.md` | `RESOLVED` | - |
| `R1-6` | R1 | `Minor` | `04_results-and-discussion_e-comparison-with-prior-studies.md` | Perluasan Baseline Pembanding Literatur | Memperluas perbandingan terhadap literatur demografi wajah dan memberi kualifikasi protokol partisi. | `04_results-and-discussion_e-comparison-with-prior-studies.md` | `RESOLVED` | - |
| `R1-7` | R1 | `Minor` | `05_conclusion.md` | Penyempurnaan Kesimpulan & Kontribusi | Menulis ulang Seksi V agar padat, menyajikan capaian tolok ukur utama secara objektif. | `05_conclusion.md` | `RESOLVED` | - |
| `R2-1` | R2 | `Major` | `01_introduction.md` | Distingsi Kebaruan Metodologis | Menjelaskan kebaruan sinergi fitur ortogonal multi-domain ViT dan isolasi pipeline tuning. | `01_introduction.md` | `RESOLVED` | - |
| `R2-2` | R2 | `Major` | `03_materials-and-methods_a-dataset.md` | Kebocoran Data & Generalisasi Subjek | Menerapkan partisi Subject-Disjoint (0% leakage) sebagai tolok ukur utama dan menyajikan ablasi leakage. | `03_materials-and-methods_a-dataset.md` | `RESOLVED` | - |
| `R2-3` | R2 | `Minor` | `03_materials-and-methods_b-vision-transformer.md` | Spesifikasi Preprocessing & Reproduktibilitas | Mencantumkan ID checkpoint HuggingFace resmi, nilai normalisasi kanal, dan formulasi token CLS. | `03_materials-and-methods_b-vision-transformer.md` | `RESOLVED` | - |
| `R2-4` | R2 | `Minor` | `03_materials-and-methods_g-classification-pipeline.md` | Rekonsiliasi Ruang Pencarian Hyperparameter | Merekonsiliasikan total 1.086 konfigurasi dan 38.010 CV fits secara konsisten pada teks dan tabel. | `03_materials-and-methods_g-classification-pipeline.md` | `RESOLVED` | - |
| `R2-5` | R2 | `Major` | `04_results-and-discussion_a-global-performance.md` | Interpretasi Signifikansi Uji McNemar | Menyajikan p-value McNemar, 95% Wilson CI, dan mengualifikasikan fenomena saturasi fitur asimtotik. | `04_results-and-discussion_a-global-performance.md` | `RESOLVED` | - |
| `R2-6` | R2 | `Major` | `04_results-and-discussion_c-intersectional-subgroup-performance.md` | Batasan Analisis Keadilan Algoritmik | Membatasi klaim keadilan formal, menegaskan EOD sebagai metrik disparitas performa subkelompok. | `04_results-and-discussion_c-intersectional-subgroup-performance.md` | `RESOLVED` | - |
| `R2-7` | R2 | `Minor` | `04_results-and-discussion_e-comparison-with-prior-studies.md` | Kualifikasi Komparasi Baseline Literatur | Menegaskan bahwa perbandingan dengan literatur terdahulu bersifat kontekstual karena variasi partisi. | `04_results-and-discussion_e-comparison-with-prior-studies.md` | `RESOLVED` | - |
| `R2-8` | R2 | `Major` | `04_results-and-discussion_a-global-performance.md` | Profil Efisiensi Komputasi Lengkap | Menyajikan tabel komparasi latensi inferensi per sampel, konsumsi memori, dan ukuran berkas model. | `04_results-and-discussion_a-global-performance.md` | `RESOLVED` | - |
| `R2-9` | R2 | `Minor` | `04_results-and-discussion_d-error-pattern-assessment.md` | Penguatan Landasan Klaim Fenotipik | Menyelaraskan analisis tumpang tindih visual murni berdasarkan data empiris matriks konfusi 6×6. | `04_results-and-discussion_d-error-pattern-assessment.md` | `RESOLVED` | - |
| `R2-10` | R2 | `Minor` | `05_conclusion.md` | Pembatasan Generalisasi pada DemogPairs | Menyatakan batas generalisasi model secara eksplisit hanya pada 3 ras makro dataset DemogPairs. | `05_conclusion.md` | `RESOLVED` | - |

---

## 2. Nested Commitment Ledger (YAML Blok Terstruktur)

```yaml
# Schema 11 R&R Traceability Matrix - Nested Shape (#268 / Kong et al. 2026 §7.4.3)
- concern_id: "AE-1"
  commitment_extracted:
    - commitment_text: "Mengakomodasi seluruh masukan R1 dan R2 secara tuntas tanpa butir terlewat (zero-orphan)."
      commitment_type: add_clarification
      required_evidence_type: acknowledgment_only

- concern_id: "AE-2"
  commitment_extracted:
    - commitment_text: "Menyiapkan paket resmi 3 berkas unggah: Author Response, Highlighted PDF, dan Clean Manuscript."
      commitment_type: other
      required_evidence_type: acknowledgment_only

- concern_id: "AE-3"
  commitment_extracted:
    - commitment_text: "Menyusun formulir resmi Request for Byline Change dan justifikasi kontribusi Dr. Shukor Sanim Mohd Fauzi."
      commitment_type: other
      required_evidence_type: acknowledgment_only

- concern_id: "AE-4"
  commitment_extracted:
    - commitment_text: "Melakukan audit kendali mutu 10-butir kepatuhan IEEE Access sebelum resubmission."
      commitment_type: other
      required_evidence_type: acknowledgment_only

- concern_id: "R1-1"
  commitment_extracted:
    - commitment_text: "Meringkas Seksi I Pendahuluan agar padat, fokus pada urgensi interseksionalitas, dan menyajikan 4 poin kontribusi."
      commitment_type: restructure
      required_evidence_type: prose_edit

- concern_id: "R1-2"
  commitment_extracted:
    - commitment_text: "Menata ulang Seksi II Studi Terkait secara tematik dan menambahkan persamaan matematis proyeksi patch, MHSA, dan fusi."
      commitment_type: add_clarification
      required_evidence_type: prose_edit

- concern_id: "R1-3"
  commitment_extracted:
    - commitment_text: "Mendesain ulang Gambar 3 arsitektur Vision Transformer resolusi tinggi dan memperjelas mekanisme fusi multi-domain."
      commitment_type: restructure
      required_evidence_type: new_figure
    - commitment_text: "Memperkaya teks penjelasan Gambar 3 pada Seksi III-B mengenai sinergi representasi laten antar-domain."
      commitment_type: add_clarification
      required_evidence_type: methods_paragraph

- concern_id: "R1-4"
  commitment_extracted:
    - commitment_text: "Memperdalam pembahasan Gambar 4 matriks konfusi 6x6, menguraikan asimetri kesalahan same-gender cross-race."
      commitment_type: add_analysis
      required_evidence_type: discussion_paragraph

- concern_id: "R1-5"
  commitment_extracted:
    - commitment_text: "Menguraikan spesifikasi dataset DemogPairs (600 subjek, 100 subjek/kelas) dan protokol partisi subject-disjoint."
      commitment_type: add_clarification
      required_evidence_type: methods_paragraph
    - commitment_text: "Menyajikan tabel profil efisiensi waktu komputasi, durasi ekstraksi, dan latensi inferensi per sampel."
      commitment_type: add_analysis
      required_evidence_type: new_table

- concern_id: "R1-6"
  commitment_extracted:
    - commitment_text: "Memperluas perbandingan terhadap literatur demografi wajah dan mengontekstualisasikan perbedaan protokol partisi."
      commitment_type: add_citation
      required_evidence_type: new_table

- concern_id: "R1-7"
  commitment_extracted:
    - commitment_text: "Merevisi Seksi V Kesimpulan untuk menyajikan kontribusi nyata tolok ukur utama secara objektif dan padat."
      commitment_type: restructure
      required_evidence_type: prose_edit

- concern_id: "R2-1"
  commitment_extracted:
    - commitment_text: "Mengartikulasikan kebaruan konseptual sinergi representasi multi-domain ViT dan isolasi pipeline GridSearchCV."
      commitment_type: add_clarification
      required_evidence_type: discussion_paragraph

- concern_id: "R2-2"
  commitment_extracted:
    - commitment_text: "Mengimplementasikan evaluasi berbasis Subject-Disjoint Partitioning (0% leakage) sebagai Primary Benchmark pada naskah."
      commitment_type: add_experiment
      required_evidence_type: new_table
    - commitment_text: "Menyajikan studi ablasi komparatif kebocoran data (Subject-Overlap 93.70% vs Subject-Disjoint 88.66% LR / 88.61% SVM)."
      commitment_type: add_analysis
      required_evidence_type: discussion_paragraph

- concern_id: "R2-3"
  commitment_extracted:
    - commitment_text: "Mendokumentasikan checkpoint HuggingFace resmi, nilai normalisasi kanal, dan formulasi ekstraksi token CLS z_L^0."
      commitment_type: add_clarification
      required_evidence_type: methods_paragraph

- concern_id: "R2-4"
  commitment_extracted:
    - commitment_text: "Merekonsiliasikan aritmatika kombinasi hyperparameter: 1.086 kombinasi x 5 folds x 7 skema = 38.010 fits + 28 refits."
      commitment_type: add_clarification
      required_evidence_type: methods_paragraph

- concern_id: "R2-5"
  commitment_extracted:
    - commitment_text: "Melaporkan nilai p-value uji McNemar berpasangan dan 95% Wilson Score CI untuk seluruh skema fitur."
      commitment_type: add_analysis
      required_evidence_type: new_table
    - commitment_text: "Mengualifikasikan klaim saintifik: keunggulan tri-domain signifikan atas single-domain, dan saturasi asimtotik pada SVM."
      commitment_type: add_clarification
      required_evidence_type: discussion_paragraph

- concern_id: "R2-6"
  commitment_extracted:
    - commitment_text: "Mengkualifikasikan ruang lingkup klaim keadilan formal; menegaskan EOD sebagai metrik disparitas subkelompok."
      commitment_type: add_clarification
      required_evidence_type: discussion_paragraph

- concern_id: "R2-7"
  commitment_extracted:
    - commitment_text: "Menyajikan perbandingan dengan literatur terdahulu sebagai komparasi kontekstual akibat perbedaan partisi data."
      commitment_type: add_clarification
      required_evidence_type: discussion_paragraph

- concern_id: "R2-8"
  commitment_extracted:
    - commitment_text: "Menyajikan profil efisiensi komputasi kuantitatif lengkap (latensi inferensi LR 0.0054 ms vs SVM 4.4481 ms, ukuran model, dan RAM)."
      commitment_type: add_analysis
      required_evidence_type: new_table

- concern_id: "R2-9"
  commitment_extracted:
    - commitment_text: "Memperhalus narasi interpretasi tumpang tindih fenotipik agar berlandaskan murni pada data distribusi matriks konfusi 6x6."
      commitment_type: add_clarification
      required_evidence_type: discussion_paragraph

- concern_id: "R2-10"
  commitment_extracted:
    - commitment_text: "Membatasi kesimpulan secara eksplisit hanya pada 3 ras makro DemogPairs dan menyatakan kebutuhan validasi eksternal."
      commitment_type: add_clarification
      required_evidence_type: discussion_paragraph
```

---

## 3. Glosarium Status Resolusi
- `RESOLVED`: Isu reviewer sepenuhnya terselesaikan dengan bukti nyata di teks naskah baru.
- `DELIBERATE_LIMITATION`: Permintaan reviewer diakui sebagai batasan inheren penelitian yang dicantumkan secara transparan di naskah.
- `UNRESOLVABLE`: Isu yang secara metodologis atau komputasi tidak memungkinkan untuk dipenuhi, disertai argumen defensif sopan.
- `REVIEWER_DISAGREE`: Sanggahan ilmiah beralasan terhadap premis reviewer yang didukung oleh data empiris atau literatur teoretis.
