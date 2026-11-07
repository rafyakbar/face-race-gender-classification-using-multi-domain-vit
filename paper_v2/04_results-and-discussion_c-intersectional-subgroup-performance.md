## C. Intersectional Subgroup Performance

Profil performa klasifikasi granular pada model terbaik Logistic Regression (LR) tri-domain Face ⊕ Emotion ⊕ Age dianalisis melintasi enam subkelompok demografis interseksional pada data uji subject-disjoint berukuran $N = 2.160$ citra (360 citra held-out per subkelompok) sebagaimana dirangkum pada [Table XIV](#tab14). Hasil evaluasi empiris menunjukkan bahwa model mencapai akurasi One-vs-Rest (OvR) rata-rata sebesar 96.26%, dengan rentang antara 95.88% pada White Females hingga 96.53% pada Black Males. Subkelompok Black Males mencatatkan sensitivitas klasifikasi tertinggi dengan Recall 92.50%, Presisi 87.17%, dan F1-Score 89.76%. Sebaliknya, subkelompok Black Females mencatatkan Recall terendah sebesar 84.44%, meskipun tetap mempertahankan Presisi tertinggi sebesar 90.48% serta F1-Score 87.36%. Pada kohort lainnya, subkelompok White Males meraih Recall 90.00%, Presisi 88.77%, dan F1-Score 89.38%, diikuti oleh Asian Males dengan Recall 89.17%, Presisi 89.42%, dan F1-Score 89.29%. Sementara itu, subkelompok White Females memperoleh Recall 88.06%, Presisi 87.57%, dan F1-Score 87.81%, sedangkan Asian Females mencatatkan Recall 87.78%, Presisi 89.04%, dan F1-Score 88.40%. Secara keseluruhan, seluruh subkelompok mencapai F1-Score di atas 87.00% dengan rata-rata agregat makro 88.68%, yang mengonfirmasi kestabilan representasi fitur tri-domain dalam memisahkan identitas demografis lintas kategori.

<a id="tab14"></a>
**Table XIV. Intersectional Subgroup Performance and Algorithmic Fairness Profile ($N = 2,160$).**

| Subkelompok Demografis | Ukuran Sampel Uji ($N$) | Akurasi OvR (%) | Presisi (%) | Recall / TPR (%) | F1-Score (%) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Asian Females | 360 | 96.25 | 89.04 | 87.78 | 88.40 |
| Asian Males | 360 | 96.48 | 89.42 | 89.17 | 89.29 |
| Black Females | 360 | 95.97 | **90.48** | 84.44 | 87.36 |
| Black Males | 360 | **96.53** | 87.17 | **92.50** | **89.76** |
| White Females | 360 | 95.88 | 87.57 | 88.06 | 87.81 |
| White Males | 360 | 96.44 | 88.77 | 90.00 | 89.38 |
| **Rata-Rata Agregat** | **2.160** | **96.26** | **88.75** | **88.66** | **88.68** |

Evaluasi disparitas keadilan algoritmik antarsubkelompok dikuantifikasi melalui metrik Equal Opportunity Difference (EOD) berdasarkan selisih True Positive Rate maksimum dan minimum ($\text{EOD} = \Delta \text{TPR} = \max \text{TPR} - \min \text{TPR} = 92.50\% - 84.44\% = 8.06\%$). Kesenjangan sebesar 8.06% ini merefleksikan variasi distribusi kesalahan empiris antarsubkelompok pada himpunan data uji held-out ($N = 2.160$ citra), di mana subkelompok Black Females mengalami tingkat kesalahan negatif palsu yang lebih tinggi dibandingkan Black Males. Sebagai bentuk pemenuhan transparansi ilmiah dan delimitasi ruang lingkup, pelaporan metrik keadilan ini disajikan secara objektif murni sebagai indikator disparitas performa empiris dalam domain terdistribusi dataset DemogPairs. Temuan ini secara tegas tidak diklaim sebagai jaminan tercapainya keadilan demografis yang sempurna atau absolut (no overclaim of complete demographic fairness) pada skenario dunia nyata di luar dataset uji. Pengukuran ini berfungsi sebagai kerangka audit komprehensif bagi etika kecerdasan buatan dalam memetakan sensitivitas deteksi secara bertanggung jawab.
