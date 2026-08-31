# Validasi 7 Laporan RF — Ringkasan PASS/FAIL
**Path:** `D:/Research/face-race-gender-multi-vit/experiment/code/reports/rf/`
**Tanggal Validasi:** 31 Aug 2026
**Kriteria:** Struktur WAJIB, Tabel lengkap, OvR Accuracy ada, CM 6x6 ada, Angka wajar

## Tabel Ringkasan

| No | File | OvR Accuracy | CM 6x6 | Angka Wajar | Struktur | Verdict |
|----|------|--------------|--------|-------------|----------|---------|
| 2.4.1 | `2.4.1_rf_vit-face.md` | ❌ TIDAK ADA | ✅ Ada (319,322,302,334,275,294 → 1846/2160=0.8546) | ✅ 0.8546 wajar | ✅ Lengkap 8 bab | **FAIL** |
| 2.4.2 | `2.4.2_rf_vit-emotion.md` | ✅ Ada (0.9588/0.9333/0.9194/0.9440/0.9380/0.9185) | ✅ Ada (310,290,274,317,288,262 → 1741/2160=0.8060) | ✅ 0.8060 wajar | ✅ Lengkap 10 bab | **PASS** |
| 2.4.3 | `2.4.3_rf_vit-age.md` | ✅ Ada (0.9255/0.9116/0.9000/0.9245/0.9028/0.9088) | ✅ Ada (287,262,228,289,247,278 → 1591/2160=0.7366) | ✅ 0.7366 wajar (terendah, ekspektasi age) | ✅ Lengkap 11 bab | **PASS** |
| 2.4.4 | `2.4.4_rf_vit-face-age.md` | ✅ Ada (0.9588/0.9620/0.9431/0.9681/0.9417/0.9421) | ✅ Ada (322,319,304,334,279,295 → 1853/2160=0.8579) | ✅ 0.8579 wajar | ⚠️ Ringkas, tanpa heading Key Observations eksplisit | **PASS* (minor)** |
| 2.4.5 | `2.4.5_rf_vit-emotion-age.md` | ✅ Ada (0.9519/0.9384/0.9255/0.9440/0.9366/0.9259) | ✅ Ada (311,287,272,313,286,283 → 1752/2160=0.8111) | ✅ 0.8111 wajar | ✅ Lengkap 8 bab | **PASS** |
| 2.4.6 | `2.4.6_rf_vit-emotion-face.md` | ✅ Ada (0.9699/0.9620/0.9454/0.9685/0.9495/0.9417) | ✅ Ada (325,319,306,338,290,298 → 1876/2160=0.8685) | ✅ 0.8685 wajar (tertinggi) | ✅ Lengkap 10 bab | **PASS** |
| 2.4.7 | `2.4.7_rf_vit-face-emotion-age.md` | ✅ Ada (0.9667/0.9602/0.9431/0.9644/0.9468/0.9431) | ✅ Ada (331,323,300,332,284,292 → 1862/2160=0.8620) | ✅ 0.8620 wajar | ✅ Lengkap Bab 1-5 + Lampiran | **PASS** |

*2.4.4 struktur ringkas: tidak ada bagian Key Observations terpisah, tapi konten observasi tercakup di analisis fold. Tidak blocking.

## Detail Per File

### 2.4.1_rf_vit-face.md — FAIL ❌
- **Struktur WAJIB:** Lengkap (Overview → Saved Artifacts 8 bab)
- **Tabel lengkap:** Classification report 6 kelas + accuracy/macro/weighted avg ada, support 360/kelas, precision/recall/F1 lengkap
- **OvR Accuracy:** **TIDAK ADA** — tidak ada tabel One-vs-Rest, tidak ada header OvR Accuracy. Ini satu-satunya pelanggaran kritikal WAJIB.
- **CM 6x6:** Ada, 6×6 valid, row sums 360, total 2160, diagonal [319,322,302,334,275,294], konsisten dengan accuracy 0.8546
- **Angka wajar:** Accuracy 0.8546, macro 0.8543, OvR seharusnya ~0.92-0.96 jika ada. Tidak ada anomali.
- **Action:** Tambahkan tabel OvR Accuracy 6 baris (copy dari results JSON `demogpairs_rf_vit-face_RandomForestClassifier.json` atau hitung ulang via `u.evaluate_models`).

### 2.4.2_rf_vit-emotion.md — PASS ✅
- Struktur lengkap (Imports→Catatan Teknis 10 bab), tabel klasifikasi lengkap, OvR 6 baris (range 0.9185-0.9588 wajar), CM 6×6 valid diag 1741, accuracy 0.8060 konsisten, angka wajar, training time 3818s wall / 14653s total.

### 2.4.3_rf_vit-age.md — PASS ✅
- Struktur lengkap 11 bab, OvR 0.9000-0.9255 wajar, CM 6×6 valid diag 1591, accuracy 0.7366 wajar untuk ViT-age (paling rendah), konsisten. Fold results top/bottom lengkap.

### 2.4.4_rf_vit-face-age.md — PASS ✅ (minor)
- Struktur ringkas (Ringkasan→Artefak) — missing heading Key Observations eksplisit tapi konten tercover, tabel lengkap, OvR ada range 0.9417-0.9681, CM valid diag 1853, accuracy 0.8579 konsisten. Training time 6311s/24456s.

### 2.4.5_rf_vit-emotion-age.md — PASS ✅
- Struktur lengkap 8 bab, OvR 0.9255-0.9519 (perhatikan tabel ada kolom OvR di posisi terakhir — valid), CM diag 1752 konsisten 0.8111, angka wajar.

### 2.4.6_rf_vit-emotion-face.md — PASS ✅
- Struktur lengkap 10 bab self-contained, OvR 0.9417-0.9699 wajar, CM diag 1876 konsisten 0.8685 (best RF), angka wajar.

### 2.4.7_rf_vit-face-emotion-age.md — PASS ✅
- Struktur Bab 1-5 + Lampiran lengkap (2304-D tri-domain), OvR 0.9431-0.9667 wajar, CM diag 1862 konsisten 0.8620, angka wajar. Catatan: heading Observations ada sebagai Bab 5 Interpretasi CV.

## Kesimpulan
- **6/7 PASS, 1/7 FAIL.**
- Satu-satunya FAIL adalah **2.4.1** karena **OvR Accuracy tidak ada**. Semua file lain memenuhi 5 kriteria: struktur, tabel, OvR, CM 6×6, angka wajar + konsistensi diagonal CM = accuracy.
- Semua CM 6×6 terverifikasi row sum 360, total 2160, diagonal/2160 = reported accuracy (diff <0.0001).
- Semua angka dalam rentang wajar (0.73-0.86 accuracy, OvR 0.90-0.97) tidak ada yang anomali/acak.
- Rekomendasi: perbaiki 2.4.1 dengan menambah tabel OvR (6 baris) agar 100% PASS.

