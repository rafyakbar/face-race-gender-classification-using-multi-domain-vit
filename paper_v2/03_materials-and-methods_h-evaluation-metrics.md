## H. Evaluation Metrics

Evaluasi performa klasifikasi multikelas interseksional ($K = 6$) pada tingkat subkelompok dirumuskan melalui skema One-vs-Rest (OvR) per kelompok demografis $c \in \{1, \dots, K\}$ [[44]](06_references.md#ref44). Formulasi ini memanfaatkan komponen matriks konfusi $TP_c$, $TN_c$, $FP_c$, dan $FN_c$ [[45]](06_references.md#ref45), [[46]](06_references.md#ref46). Akurasi subkelompok pada [(13)](#eq13) mengukur rasio prediksi benar, sedangkan Presisi pada [(14)](#eq14), Recall atau True Positive Rate (TPR) pada [(15)](#eq15), dan F1-Score pada [(16)](#eq16) memetakan ketepatan serta sensitivitas deteksi [[47]](06_references.md#ref47). Untuk mengevaluasi data uji held-out ($N = 2.160$), metrik subkelompok diagregasikan ke tingkat global. Akurasi Global pada [(17)](#eq17) menghitung rasio total prediksi benar, sedangkan Macro Precision pada [(18)](#eq18), Macro Recall pada [(19)](#eq19), dan Macro F1-Score pada [(20)](#eq20) dirata-ratakan tanpa bobot melintasi $K = 6$ subkelompok demi menjamin kesetaraan evaluasi.

<a id="eq13"></a>
$$
\text{Accuracy}_c = \frac{TP_c + TN_c}{TP_c + TN_c + FP_c + FN_c} \tag{13}
$$

<a id="eq14"></a>
$$
\text{Precision}_c = \frac{TP_c}{TP_c + FP_c} \tag{14}
$$

<a id="eq15"></a>
$$
\text{Recall}_c = \frac{TP_c}{TP_c + FN_c} \tag{15}
$$

<a id="eq16"></a>
$$
\text{F1-Score}_c = \frac{2 \cdot \text{Precision}_c \cdot \text{Recall}_c}{\text{Precision}_c + \text{Recall}_c} \tag{16}
$$

<a id="eq17"></a>
$$
\text{Accuracy}_{\text{Global}} = \frac{\sum_{c=1}^K TP_c}{N} \tag{17}
$$

<a id="eq18"></a>
$$
\text{Precision}_{\text{Macro}} = \frac{1}{K} \sum_{c=1}^K \text{Precision}_c \tag{18}
$$

<a id="eq19"></a>
$$
\text{Recall}_{\text{Macro}} = \frac{1}{K} \sum_{c=1}^K \text{Recall}_c \tag{19}
$$

<a id="eq20"></a>
$$
\text{F1-Score}_{\text{Macro}} = \frac{1}{K} \sum_{c=1}^K \text{F1-Score}_c \tag{20}
$$

Validasi signifikansi komparatif antarmodel dievaluasi melalui uji hipotesis inferensial berpasangan McNemar dengan koreksi kontinuitas Edwards pada [(21)](#eq21) [[44]](06_references.md#ref44). Statistik $\chi^2$ dihitung pada tabel kontingensi 2 × 2 berbasis pasangan diskordan, di mana $b$ dan $c$ mencatat perbedaan klasifikasi benar-salah antarmodel yang diperkuat uji eksak binomial dua arah. Ketidakpastian akurasi empiris pada data uji held-out ($N = 2.160$) diukur melalui estimasi Wilson Score 95% Confidence Interval (CI) pada [(22)](#eq22), dengan $\hat{p}$ sebagai proporsi akurasi dan $z = 1.96$ sebagai nilai kritis standar. Evaluasi disparitas performa dikuantifikasi melalui Equal Opportunity Difference (EOD) pada [(23)](#eq23) sebagai selisih absolut maksimum TPR antarpasangan subkelompok $i, j \in \{1, \dots, K\}$, yang dikalibrasi murni sebagai indikator disparitas empiris antarsubkelompok, bukan jaminan matematis keadilan universal.

<a id="eq21"></a>
$$
\chi^2 = \frac{(|b - c| - 1)^2}{b + c} \tag{21}
$$

<a id="eq22"></a>
$$
\text{CI}_{95\%} = \frac{\hat{p} + \frac{z^2}{2N} \pm z \sqrt{\frac{\hat{p}(1-\hat{p})}{N} + \frac{z^2}{4N^2}}}{1 + \frac{z^2}{N}} \tag{22}
$$

<a id="eq23"></a>
$$
\text{EOD} = \max_{i, j \in \{1, \dots, K\}} |\text{Recall}_i - \text{Recall}_j| = \max \text{TPR} - \min \text{TPR} \tag{23}
$$
