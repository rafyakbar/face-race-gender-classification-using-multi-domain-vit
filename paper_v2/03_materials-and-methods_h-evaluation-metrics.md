## H. Evaluation Metrics

Evaluasi performa klasifikasi multikelas interseksional ($K = 6$) pada tingkat subkelompok dirumuskan melalui skema One-vs-Rest (OvR) per kelompok demografis $c \in \{1, \dots, K\}$ [[44]](06_references.md#ref44). Skema ini memanfaatkan empat komponen matriks konfusi per kelas, yaitu $TP_c$ (True Positive), $TN_c$ (True Negative), $FP_c$ (False Positive), dan $FN_c$ (False Negative) [[45]](06_references.md#ref45), [[46]](06_references.md#ref46). Akurasi subkelompok pada [(13)](#eq13) mengukur rasio prediksi benar terhadap seluruh sampel, sedangkan Presisi pada [(14)](#eq14) dan Recall atau True Positive Rate (TPR) pada [(15)](#eq15) memetakan ketepatan positif serta sensitivitas deteksi per subkelompok [[47]](06_references.md#ref47). F1-Score pada [(16)](#eq16) merangkum rata-rata harmonik antara presisi dan sensitivitas. Untuk mengevaluasi efektivitas sistem secara menyeluruh pada data uji held-out independen berukuran $N = 2.160$ sampel, metrik subkelompok diagregasikan ke tingkat global. Akurasi Global pada [(17)](#eq17) menghitung rasio total prediksi benar terhadap $N$. Selanjutnya, Macro Precision pada [(18)](#eq18), Macro Recall pada [(19)](#eq19), dan Macro F1-Score pada [(20)](#eq20) dihitung melalui perataan makro tanpa bobot (unweighted macro average) melintasi $K = 6$ subkelompok untuk menjamin bobot evaluasi yang setara.

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
\text{Precision}_{\text{Global}} = \frac{1}{K} \sum_{c=1}^K \text{Precision}_c \tag{18}
$$

<a id="eq19"></a>
$$
\text{Recall}_{\text{Global}} = \frac{1}{K} \sum_{c=1}^K \text{Recall}_c \tag{19}
$$

<a id="eq20"></a>
$$
\text{F1-Score}_{\text{Global}} = \frac{1}{K} \sum_{c=1}^K \text{F1-Score}_c \tag{20}
$$

Validasi signifikansi komparatif antarmodel klasifikasi dievaluasi melalui uji hipotesis inferensial berpasangan McNemar dengan koreksi kontinuitas Edwards pada [(21)](#eq21) [[44]](06_references.md#ref44). Statistik uji $\chi^2$ dihitung berbasis tabel kontingensi 2 × 2 berpasangan pada pasangan prediksi diskordan, dengan $b$ menyatakan jumlah sampel uji yang diklasifikasikan secara benar oleh model pertama namun salah oleh model kedua, sedangkan $c$ merepresentasikan jumlah sampel yang salah diprediksi oleh model pertama namun benar oleh model kedua. Derajat ketidakpastian estimasi akurasi empiris pada himpunan data uji held-out berukuran $N = 2.160$ sampel diukur melalui estimasi Wilson Score 95% Confidence Interval (CI) berdasarkan [(22)](#eq22), di mana $\hat{p}$ merupakan proporsi akurasi empiris sampel dan $z = 1.96$ adalah nilai kritis distribusi normal standar pada tingkat kepercayaan 95%. Sementara itu, evaluasi disparitas performa antarkelompok dikuantifikasi melalui metrik Equal Opportunity Difference (EOD) pada [(23)](#eq23) yang menghitung selisih absolut maksimum True Positive Rate (TPR) atau Recall antarpasangan subkelompok demografis $i, j \in \{1, \dots, K\}$. Metrik EOD tersebut dikalibrasi secara objektif murni sebagai indikator disparitas performa empiris antarsubkelompok, bukan sebagai jaminan matematis keadilan universal.

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
