# Log Riwayat Penelaahan Ilmiah (Review Log)

Dokumen ini mencatat linimasa, status, dan riwayat keputusan penelaahan sejawat (*peer review*) berkala untuk naskah ilmiah:
**"Multi-Domain Vision Transformer Fusion for Intersectional Demographic Classification from Facial Images"**  
Target Publikasi: **IEEE Access**

---

## Ringkasan Eksekutif Lintas Putaran

| Putaran (Round) | Tanggal Evaluasi | Status Keputusan Editorial | Mesin Keputusan (Schema 13) | Kondisi Terpicu | Catatan Utama |
|:---:|:---:|:---:|:---:|:---:|---|
| **Round 1 (Initial Review)** | 2026-09-27 | **MAJOR REVISION** *(IEEE Access: Reject & Resubmit)* | `D1=BLOCK, D2=WARN, D3=BLOCK, D4=WARN, D5=WARN, D6=WARN` | `F2`, `F3` | **Sintesis Konsensus Multi-Model (Gemini 3.8 Flash + Claude Opus)**: Total 22 temuan terintegrasi (P1: 4 item, P2: 6 item, P3: 12 item). Diperlukan verifikasi bebas kebocoran identitas subjek (*subject-disjoint split*), uji signifikansi statistik (McNemar / 95% CI) untuk delta 0.41%, eksperimen kontrol noise dimensionalitas, kalibrasi paradoks regresi Random Forest, perluasan baseline SOTA eksternal, metrik keadilan formal, stabilitas lipatan CV (Mean ± Std), visualisasi t-SNE/UMAP, dan statuta wajib IEEE Access. |
| **Round 2 (Re-Review Verification)** | 2026-09-28 | **ACCEPT** *(IEEE Access: Accepted for Publication)* | `D1=PASS, D2=PASS, D3=PASS, D4=PASS, D5=PASS, D6=PASS` | `F0` | **Verifikasi Keterlacakan Komitmen Penuh (Traceability Audit)**: Seluruh 22 komitmen Roadmap R1 terverifikasi tuntas (20 item FULLY_ADDRESSED, 1 PARTIALLY_ADDRESSED dengan bukti saturasi inferensial, 1 DELIBERATE_LIMITATION yang sah). Uji McNemar berpasangan dan Wilson 95% CI disajikan lengkap; degradasi RF (-0.65%) dijelaskan via *curse of dimensionality*; metrik keadilan formal $\Delta\text{TPR}=7.50\%$ dihitung; statuta IEEE Access terintegrasi penuh. Naskah siap dialihbahasakan ke Academic English untuk submisi portal IEEE. |

---

## Linimasa & Riwayat Detail Penelaahan

### Putaran 1: Initial Review & Multi-Model Synthesis (2026-09-27)
- **Tahap 1: Desk Screening EIC** (`00_desk_screening.md`):
  - Status: **`DESK_PASS`**
  - Alasan: Format IMRaD lengkap, topik relevan dengan scope IEEE Access, abstraksi berangka, dan biografi naratif 4 penulis lengkap. Lolos untuk penelaahan panel penuh 5 evaluator.
- **Tahap 2: Pembekuan Panel Penilai (*Yardstick Freeze*)** (`panel_config.json`):
  - Ditetapkan 5 persona: Editor-in-Chief (EIC), Reviewer 1 (Methodology), Reviewer 2 (Domain Expert), Reviewer 3 (Cross-Perspective), Devil's Advocate (Adversarial).
- **Tahap 3: Ulasan Panel Independen & Sintesis Multi-Model**:
  - `01_eic_report.md`: Minor Revision (4 temuan: distingsi kebaruan konferensi ICVEE, statuta wajib IEEE, keringkasan poin kontribusi, pendalaman mekanistik).
  - `02_methodology_report.md`: Major Revision (5 temuan: ambiguitas subject-disjoint split [CRITICAL], uji signifikansi McNemar & 95% CI, pelaporan skor CV fold mean ± std, distorsi akurasi OvR, random seed & scaler).
  - `03_domain_report.md`: Minor Revision (4 temuan: ketiadaan baseline eksternal standar, silsilah korpus pra-latih HuggingFace, visualisasi feature embedding t-SNE/UMAP, teori kognitif dual-stream Bruce & Young).
  - `04_cross_perspective_report.md`: Minor Revision (3 temuan: ketiadaan metrik keadilan formal & drop recall 7.50% Black Females, profil latensi inferensi 3 ViT ~258M parameter, refleksi etika biometrik rasial & risiko dual-use).
  - `05_devils_advocate_report.md`: Major Revision (6 temuan: paradoks keunggulan tri-domain & regresi RF -0.65% [CRITICAL], eksperimen kontrol noise dimensionalitas, inflasi semantik klaim fusi konkatenasi, justifikasi komparatif fine-tuning single-ViT, seleksi gambar matriks konfusi, definisi stabilitas subkelompok).
- **Tahap 4: Sintesis Editorial & Rencana Aksi Revisi**:
  - Basis Data Temuan (`06_findings_database.json`): 22 temuan terpetakan (2 CRITICAL, 9 MAJOR, 11 MINOR).
  - Keputusan Editorial (`07_editorial_decision.md`): **MAJOR REVISION** (Kondisi `F2` & `F3` terpicu, setara dengan persiapan pengajuan ulang naskah IEEE Access).
  - Rencana Aksi Revisi (`08_revision_roadmap.md`): Matriks komitmen 22 rencana aksi terprioritas terbagi dalam 3 Sprint dengan kriteria keterterimaan (*Acceptance Criteria*) terukur.
  - Rangkuman Eksekutif Terpadu (`round-1.md`): Rangkuman eksekutif lengkap ulasan Putaran 1.

---

### Putaran 2: Re-Review Verification & Acceptance (2026-09-28)
- **Tahap 1: Verifikasi Kesinambungan Tolok Ukur (*Yardstick Continuity*)**:
  - Panel 5 evaluator dipertahankan identik sesuai `panel_config.json` Putaran 1 (EIC, Reviewer 1, Reviewer 2, Reviewer 3, Devil's Advocate).
- **Tahap 2: Audit Diplomasi & Surat Tanggapan Penulis** (`10_rebuttal_audit_report.md`):
  - Berkas yang diaudit: `09_response_letter.md`.
  - Hasil: LULUS PENUH (100% isu terpetakan, ketiadaan komentar yatim, lokator bukti presisi, nada kolegial dan konstruktif).
- **Tahap 3: Verifikasi Matriks Ketertelusuran Naskah** (`11_re_review_verification.md`):
  - Uji silang komprehensif antara `08_revision_roadmap.md` Putaran 1, `09_response_letter.md`, dan teks bab naskah `paper/*.md`.
  - Skor Pemenuhan: 20 item FULLY_ADDRESSED (90.91%), 1 item PARTIALLY_ADDRESSED (4.55% — didukung bukti kejenuhan asimtotik inferensial), 1 item DELIBERATE_LIMITATION (4.55% — penolakan beralasan t-SNE). 0 item NOT_ADDRESSED. Bebas cacat baru.
- **Tahap 4: Catatan Sintesis Editorial EIC & Adjudikasi DA CRITICAL** (`12_eic_re_review_notes.md`):
  - Evaluasi 6 Dimensi: Seluruh dimensi (`D1` s/d `D6`) dinaikkan statusnya menjadi **`PASS`**.
  - DA CRITICAL `ISSUE-DA-C1` (Paradoks Tri-Domain vs RF) dan `ISSUE-DA-M1` (Kontrol Dimensionalitas) diadjudikasi tuntas (**`RESOLVED`**).
- **Tahap 5: Penerbitan Surat Keputusan Editorial Putaran 2** (`07_editorial_decision.md`):
  - Keputusan: **`ACCEPT`** (Kondisi deterministik `F0` Schema 13 terpicu).
  - Naskah dinyatakan memenuhi standar publikasi *IEEE Access*.
- **Tahap 6: Panduan Aksi Residual & Rangkuman Eksekutif**:
  - `08_residual_roadmap.md`: Panduan persiapan naskah akhir (alih bahasa ke *Academic English* dan pemformatan template dua kolom IEEE Access).
  - `round-2.md`: Rangkuman eksekutif lengkap ulasan Putaran 2.
