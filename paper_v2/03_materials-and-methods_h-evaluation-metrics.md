## H. Evaluation Metrics

Evaluasi performa klasifikasi multi-kelas enam subkelompok demografis pada tingkat subkelompok dilakukan melalui skema biner One-vs-Rest (OvR) [[44]](06_references.md#ref44). Skema ini memanfaatkan empat komponen matriks konfusi per kelas untuk menghitung Akurasi OvR, Presisi, Recall, dan F1-Score pada setiap kelas $c \in \{1, \dots, K\}$ [[45]](06_references.md#ref45). Keempat komponen tersebut mencakup $TP_c$ (True Positive), $TN_c$ (True Negative), $FP_c$ (False Positive), dan $FN_c$ (False Negative) [[46]](06_references.md#ref46). Akurasi OvR pada [(10)](#eq10) mengukur rasio total prediksi benar terhadap seluruh data uji, sedangkan Presisi pada [(11)](#eq11) dan Recall pada [(12)](#eq12) memetakan ketepatan positif serta sensitivitas deteksi sistem per subkelompok [[47]](06_references.md#ref47). F1-Score pada [(13)](#eq13) dirumuskan sebagai rata-rata harmonik antara Presisi dan Recall untuk merepresentasikan keseimbangan evaluasi performa deteksi per subkelompok [[47]](06_references.md#ref47).

<a id="eq10"></a>
$$
\text{Accuracy}_c = \frac{TP_c + TN_c}{TP_c + TN_c + FP_c + FN_c} \tag{10}
$$

<a id="eq11"></a>
$$
\text{Precision}_c = \frac{TP_c}{TP_c + FP_c} \tag{11}
$$

<a id="eq12"></a>
$$
\text{Recall}_c = \frac{TP_c}{TP_c + FN_c} \tag{12}
$$

<a id="eq13"></a>
$$
\text{F1-Score}_c = \frac{2 \cdot \text{Precision}_c \cdot \text{Recall}_c}{\text{Precision}_c + \text{Recall}_c} \tag{13}
$$

Untuk mengevaluasi efektivitas sistem klasifikasi secara menyeluruh pada data uji independen, metrik performa per subkelompok diagregasikan menjadi metrik evaluasi global. Pada formulasi ini, simbol $N$ menyatakan total sampel data uji ($N=2,160$), sedangkan $K$ menyatakan jumlah total subkelompok demografis ($K=6$). Akurasi Global (Overall Accuracy) pada [(14)](#eq14) dihitung sebagai rasio total prediksi benar, yaitu penjumlahan elemen diagonal utama matriks konfusi $\sum_{c=1}^K TP_c$, terhadap total sampel data uji $N$. Selanjutnya, Presisi global (Macro Precision) pada [(15)](#eq15), Recall global (Macro Recall) pada [(16)](#eq16), dan F1-Score global (Macro F1-Score) pada [(17)](#eq17) dihitung melalui perataan makro tanpa bobot (unweighted macro average) melintasi $K=6$ subkelompok untuk memberikan bobot evaluasi yang setara pada setiap kelas demografis.

<a id="eq14"></a>
$$
\text{Accuracy}_{\text{Global}} = \frac{\sum_{c=1}^K TP_c}{N} \tag{14}
$$

<a id="eq15"></a>
$$
\text{Precision}_{\text{Global}} = \frac{1}{K} \sum_{c=1}^K \text{Precision}_c \tag{15}
$$

<a id="eq16"></a>
$$
\text{Recall}_{\text{Global}} = \frac{1}{K} \sum_{c=1}^K \text{Recall}_c \tag{16}
$$

<a id="eq17"></a>
$$
\text{F1-Score}_{\text{Global}} = \frac{1}{K} \sum_{c=1}^K \text{F1-Score}_c \tag{17}
$$
