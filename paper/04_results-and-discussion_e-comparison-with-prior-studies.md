## E. Comparison with Prior Studies

<a id="tab12"></a>
**Table XII. Comparative Performance of Proposed Framework against Prior Studies on the DemogPairs Dataset.**

| Model | Accuracy | Precision | Recall | F1-Score |
|---|:---:|:---:|:---:|:---:|
| MD-ViT [[20]](06_references.md#ref20) | 89.07% | 89.12% | 89.07% | 89.01% |
| Dual-ViT [[19]](06_references.md#ref19) | 92.41% | 92.48% | 92.41% | 92.38% |
| **Ours** | **93.70%** | **93.72%** | **93.70%** | **93.69%** |

Perbandingan empiris secara langsung antara kerangka kerja usulan dan studi terdahulu pada dataset DemogPairs dirangkum pada [Table XII](#tab12). Model usulan berbasis Tri-Domain ViT + SVM (Face ⊕ Emotion ⊕ Age) meraih Akurasi 93.70%, Presisi 93.72%, Recall 93.70%, dan F1-Score 93.69%. Capaian kuantitatif tersebut melampaui performa yang dilaporkan pada model Dual-ViT + SVM dengan Akurasi 92.41% dan F1-Score 92.38% [[19]](06_references.md#ref19), serta model MD-ViT + XGBoost dengan Akurasi 89.07% dan F1-Score 89.01% [[20]](06_references.md#ref20). Komparasi ini memposisikan kontribusi saintifik naskah ini sebagai evaluasi sistematis tri-domain laten dengan pengujian signifikansi serta batas keputusan yang melampaui studi prosiding konferensi terdahulu [[19]](06_references.md#ref19). Seluruh angka pembanding disitasi langsung dari publikasi masing-masing sebagai penempatan kontekstual pada dataset acuan yang sama.

Penelitian seminal perancangan dataset DemogPairs oleh Hupont dan Fernández [[25]](06_references.md#ref25) dirancang secara eksklusif sebagai benchmark verifikasi identitas (identity verification ROC pada 58.3 juta pasangan citra) dan tidak melakukan pelatihan klasifikasi 6-kelas (closed-set intersectional classification). Oleh karena itu, penelitian ini bersama studi terkait terdahulu [[19]](06_references.md#ref19), [[20]](06_references.md#ref20) memelopori dan menyediakan baseline terkontrol internal pertama yang komprehensif untuk klasifikasi demografis interseksional 6-kelas pada dataset DemogPairs. Selain mengevaluasi metrik agregat global, penyelidikan ini menjalankan analisis disparitas subkelompok secara mendalam pada konfigurasi tri-domain terbaik untuk memetakan variasi performa antarsubkelompok demografis secara transparan. Evaluasi mendalam tersebut membuktikan stabilitas klasifikasi lintas kategori ras dan gender interseksional, di mana informasi variasi performa subkelompok tidak dilaporkan dalam literatur pembanding sebelumnya [[19]](06_references.md#ref19), [[20]](06_references.md#ref20).
