# Log Riwayat Penelaahan Ilmiah (Review Log)

Dokumen ini mencatat linimasa, status, dan riwayat keputusan penelaahan sejawat (*peer review*) berkala untuk naskah ilmiah:
**"Multi-Domain Vision Transformer Fusion for Intersectional Demographic Classification from Facial Images"**  
Target Publikasi: **IEEE Access**

---

## Ringkasan Eksekutif Lintas Putaran

| Putaran (Round) | Tanggal Evaluasi | Status Keputusan Editorial | Mesin Keputusan (Schema 13) | Kondisi Terpicu | Catatan Utama |
|:---:|:---:|:---:|:---:|:---:|---|
| **Round 1 (Initial Review)** | 2026-09-27 | **MAJOR REVISION** *(IEEE Access: Reject & Resubmit)* | `D1=BLOCK, D2=WARN, D3=BLOCK, D4=WARN, D5=WARN, D6=WARN` | `F2`, `F3` | **Sintesis Konsensus Multi-Model (Gemini 3.8 Flash + Claude Opus)**: Total 22 temuan terintegrasi (P1: 4 item, P2: 6 item, P3: 12 item). Diperlukan verifikasi bebas kebocoran identitas subjek (*subject-disjoint split*), uji signifikansi statistik (McNemar / 95% CI) untuk delta 0.41%, eksperimen kontrol noise dimensionalitas, kalibrasi paradoks regresi Random Forest, perluasan baseline SOTA eksternal, metrik keadilan formal, stabilitas lipatan CV (Mean ± Std), visualisasi t-SNE/UMAP, dan statuta wajib IEEE Access. |

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
