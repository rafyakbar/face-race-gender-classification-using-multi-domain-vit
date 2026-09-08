## E. Comparison with Prior Studies

<a id="tab12"></a>
**Table XII. Comparative Performance of Proposed Framework against Prior Studies on the DemogPairs Dataset.**

| Model | Accuracy | Precision | Recall | F1-Score |
|---|:---:|:---:|:---:|:---:|
| MD-ViT [[20]](06_references.md#ref20) | 89.07% | 89.12% | 89.07% | 89.01% |
| Dual-ViT [[19]](06_references.md#ref19) | 92.41% | 92.48% | 92.41% | 92.38% |
| **Ours** | **93.70%** | **93.72%** | **93.70%** | **93.69%** |

Perbandingan empiris secara langsung antara kerangka kerja yang diusulkan dan studi terdahulu yang dievaluasi pada dataset DemogPairs dirangkum pada [Table XII](#tab12). Model usulan berbasis Tri-Domain ViT + SVM (Face ⊕ Emotion ⊕ Age) meraih Akurasi 93.70%, Presisi 93.72%, Recall 93.70%, dan F1-Score 93.69%. Capaian kuantitatif tersebut melampaui metrik yang dilaporkan pada model Dual-ViT + SVM, yaitu Akurasi 92.41% dan F1-Score 92.38%, serta model MD-ViT + XGBoost dengan Akurasi 89.07% dan F1-Score 89.01% [[19]](06_references.md#ref19), [[20]](06_references.md#ref20). Seluruh angka pembanding disitasi langsung dari publikasi masing-masing, sehingga komparasi ini berfungsi sebagai penempatan kontekstual pada dataset acuan yang sama dan tidak dimaksudkan sebagai replikasi eksperimen yang sepenuhnya identik.

Penelitian seminal mengenai perancangan dataset DemogPairs meletakkan landasan penting dalam mengukur dampak ketidakseimbangan demografis pada sistem pengenalan wajah [[25]](06_references.md#ref25). Menanggapi tantangan tersebut, kerangka kerja integrasi representasi tiga domain yang diusulkan dalam penelitian ini menghasilkan akurasi tertinggi di antara studi-studi yang dibandingkan pada dataset DemogPairs [[19]](06_references.md#ref19), [[20]](06_references.md#ref20). Selain mengevaluasi metrik agregat global, penyelidikan ini menjalankan analisis disparitas subkelompok secara komprehensif pada konfigurasi tri-domain terbaik untuk memetakan variasi performa antarsubkelompok demografis secara transparan. Evaluasi terperinci tersebut membuktikan stabilitas pengenalan lintas kategori ras dan gender interseksional, meskipun perbandingan disparitas lintas seluruh skema sebelumnya tidak dapat disertakan karena informasi variasi performa tersebut tidak dilaporkan dalam literatur terkait [[19]](06_references.md#ref19), [[20]](06_references.md#ref20).

