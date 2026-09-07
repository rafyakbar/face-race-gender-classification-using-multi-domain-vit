## E. Comparison with Prior Studies

<a id="tab12"></a>
**Table XII. Comparative Performance of Proposed Framework against Prior Studies on the DemogPairs Dataset.**

| Model | Accuracy | Precision | Recall | F1-Score |
|---|:---:|:---:|:---:|:---:|
| MD-ViT | 89.07% | 0.8912 | 0.8907 | 0.8901 |
| Dual-ViT | 92.41% | 0.9248 | 0.9241 | 0.9238 |
| **Ours** | **93.70%** | **0.9372** | **0.9370** | **0.9369** |

Perbandingan empiris secara langsung antara kerangka kerja yang diusulkan dan studi terdahulu yang dievaluasi pada dataset DemogPairs dirangkum pada [Table XII](#tab12). Model usulan berbasis Tri-Domain ViT + SVM (Face ⊕ Emotion ⊕ Age) meraih Akurasi 93.70%, Presisi 0.9372, Recall 0.9370, dan F1-Score 0.9369. Capaian kuantitatif tersebut melampaui metrik yang dilaporkan pada model Dual-ViT + SVM, yaitu Akurasi 92.41% dan F1-Score 0.9238, serta model MD-ViT + XGBoost dengan Akurasi 89.07% dan F1-Score 0.8901. Seluruh angka pembanding disitasi langsung dari publikasi masing-masing, sehingga komparasi ini berfungsi sebagai penempatan kontekstual pada dataset acuan yang sama dan tidak dimaksudkan sebagai replikasi eksperimen yang sepenuhnya identik.

Penelitian seminal mengenai perancangan dataset DemogPairs meletakkan landasan penting dalam mengukur dampak ketidakseimbangan demografis pada sistem pengenalan wajah. Menanggapi tantangan tersebut, kerangka kerja integrasi representasi tiga domain yang diusulkan dalam penelitian ini menghasilkan akurasi tertinggi di antara studi-studi yang dibandingkan pada dataset DemogPairs. Selain mengevaluasi metrik agregat global, penyelidikan ini menjalankan analisis disparitas subkelompok secara komprehensif pada konfigurasi tri-domain terbaik untuk memetakan variasi performa antarsubkelompok demografis secara transparan. Evaluasi terperinci tersebut membuktikan stabilitas pengenalan lintas kategori ras dan gender interseksional, meskipun perbandingan disparitas lintas seluruh skema sebelumnya tidak dapat disertakan karena informasi variasi performa tersebut tidak dilaporkan dalam literatur terkait.

