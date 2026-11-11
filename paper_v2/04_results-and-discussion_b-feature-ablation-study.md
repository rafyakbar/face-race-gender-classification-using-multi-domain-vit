## B. Feature Ablation Study

Evaluasi komparatif kebocoran data disajikan secara transparan untuk memvalidasi kekokohan model terhadap telaah kritis tumpang tindih identitas subjek. Perbandingan antara protokol Stratified Split berbasis pembagian acak berstrata tingkat citra dengan tumpang tindih subjek penuh dan protokol utama partisi ketat subjek independen dirangkum pada [Table XIII](#tab13). Seluruh arsitektur mengalami penurunan akurasi pada protokol subjek independen, membuktikan keberadaan efek pembaur memorisasi identitas pada evaluasi acak. Koreksi performa terbesar terjadi pada model berkapasitas representasi tinggi, yaitu SVM yang terkoreksi dari 93.70% ke 88.61% (penurunan -5.09 pp) serta LR dari 92.73% ke 88.66% (penurunan -4.07 pp). Sebaliknya, model berkapasitas rendah menunjukkan penurunan minimal, seperti RF (-1.85 pp) dan GNB (-1.44 pp). Hasil ini membuktikan bahwa capaian 88.66% pada LR mencerminkan batas generalisasi demografis riil.

<a id="tab13"></a>
**Table XIII. Data Leakage Ablation Study on Stratified Split and Subject-Disjoint Protocols.**

| Classifier | Stratified Split* | Subject-Disjoint | Difference (Δ) | Leakage Severity |
| :--- | :---: | :---: | :---: | :--- |
| Random Forest | 86.85% | 85.00% | -1.85% | Low |
| Gaussian Naive Bayes | 85.05% | 83.61% | -1.44% | Very Low |
| **Logistic Regression** | **92.73%** | **88.66%** | **-4.07%** | **High (Corrected)** |
| Support Vector Machine | 93.70% | 88.61% | -5.09% | High (Corrected) |

(Note: Evaluated on random stratified image-level split with full subject overlap).

Pengujian statistik inferensial berpasangan dilakukan pada seluruh 2.160 sampel uji independen menerapkan uji McNemar berkoreksi kontinuitas Edwards serta uji binomial eksak dua arah sebagaimana dirangkum pada [Table XIV](#tab14). Keunggulan representasi tri-domain atas domain tunggal terbukti signifikan secara statistik pada LR ($\chi^2 = 19.69$, $p < 0.001$) maupun SVM ($\chi^2 = 20.96$, $p < 0.001$). Pada integrasi fitur usia di atas pasangan Emotion dan Face, LR memperoleh kenaikan signifikan ($\chi^2 = 7.10$, $p = 0.0073$). Sebaliknya, SVM mencatat hasil tidak signifikan ($\chi^2 = 0.12$, $p = 0.7343$), mengonfirmasi terjadinya kejenuhan fitur laten asimtotik. Selain itu, komparasi langsung antara LR Tri dan SVM Tri menghasilkan $\chi^2 = 0.00$ ($p = 1.0000$) dengan selisih hanya satu citra, membuktikan tercapainya paritas performa prediktif.

<a id="tab14"></a>
**Table XIV. Paired Inferential Hypothesis Testing Across Multi-Domain Configurations.**

| Comparison Pair | Edwards $\chi^2$ | McNemar $p$-value | Exact Binomial $p$-value | Statistical Inference ($\alpha = 0.05$) | Scientific Interpretation |
| :--- | :---: | :---: | :---: | :---: | :--- |
| Tri-Domain LR vs Single Face | 19.69 | < 0.001 | < 0.001 | Significant ($p < 0.001$) | Multi-domain representation superiority |
| Tri-Domain SVM vs Single Face | 20.96 | < 0.001 | < 0.001 | Significant ($p < 0.001$) | Multi-domain representation superiority |
| Tri-Domain LR vs Dual Emotion $\oplus$ Face | 7.10 | 0.0073 | 0.0075 | Significant ($p < 0.01$) | Linear age feature complementarity |
| Tri-Domain SVM vs Dual Emotion $\oplus$ Face | 0.12 | 0.7343 | 0.7500 | Not Significant ($p > 0.05$) | Asymptotic non-linear feature saturation |
| Tri-Domain LR vs Tri-Domain SVM | 0.00 | 1.0000 | 1.0000 | Not Significant ($p = 1.0000$) | Strict predictive parity |

Dinamika kontribusi fusi bertahap dari representasi domain tunggal menuju domain ganda dan tri-domain pada [Table VII](#tab7), [Table VIII](#tab8), [Table IX](#tab9), serta [Table X](#tab10) menunjukkan respons ruang fitur yang berbeda secara fundamental antarpengklasifikasi. Pada model linier LR, integrasi representasi usia biologis di atas pasangan Emotion dan Face menghasilkan peningkatan komplementer sebesar +1.21 pp dari 87.45% menuju 88.66%. Sebaliknya, pengklasifikasi non-linier SVM memperlihatkan kejenuhan asimtotik, di mana penambahan domain usia dari kombinasi Emotion dan Face (88.43%) ke tri-domain (88.61%) hanya menghasilkan kenaikan marjinal +0.18 pp. Perbedaan respons ini menegaskan bahwa batas keputusan non-linier kernel RBF telah menyerap mayoritas varians diskriminatif sejak tahap dual-domain, sedangkan regularisasi L2 pada LR efektif memanfaatkan ortogonalitas informasi penuaan.
