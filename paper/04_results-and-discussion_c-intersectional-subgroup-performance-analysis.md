## C. Intersectional Subgroup Performance Analysis

Profil kinerja klasifikasi granular pada model terbaik SVM berbasis fusi tri-domain Face ⊕ Emotion ⊕ Age dievaluasi secara mendalam berdasarkan metrik OvR sebagaimana disajikan pada [Table XI](#tab11). Seluruh subkelompok demografis berhasil mencapai F1-Score melampaui 91.00%, dengan rentang capaian bergerak dari 91.74% pada Black_Females hingga 96.14% pada White_Males, sehingga menghasilkan selisih disparitas rentang sebesar 4.40% (0.0440). Sementara itu, nilai Akurasi OvR berada pada rentang 97.31% hingga 98.70% dengan disparitas sebesar 1.39 pp. Perlu dicatat secara metodologis bahwa tingginya nilai Akurasi OvR tersebut turut dipengaruhi oleh rasio dominansi sampel negatif sebesar 5:1 pada evaluasi biner OvR, sehingga metrik ini tidak diposisikan sebagai indikator tunggal disparitas kinerja.

Perbandingan profil kinerja subkelompok antara model SVM dan pengklasifikasi linier LR pada konfigurasi tri-domain disajikan pada [Table XI](#tab11). Model LR tri-domain turut memperlihatkan konsistensi performa yang tinggi dengan capaian F1-Score melampaui 91.00% pada seluruh kelas demografis, yang merentang dari 91.36% pada Asian_Females hingga 95.58% pada White_Males dengan selisih disparitas rentang sebesar 4.22% (0.0422). Subkelompok White_Males secara konsisten mencatatkan performa klasifikasi tertinggi pada kedua pengklasifikasi tersebut. Temuan empiris ini membuktikan bahwa fusi representasi tri-domain menghasilkan representasi visual yang tangguh dan terdistribusi stabil melintasi seluruh subkelompok demografis, baik pada model linier maupun model non-linier. Meskipun demikian, evaluasi subkelompok ini mencerminkan kinerja granular per kelas dan bukan audit keadilan algoritmik komprehensif.

<a id="tab11"></a>
**Table XI. Subgroup-Level Performance for Tri-Domain Models.**

| Classifier | Subgroup | Recall | Precision | F1-Score | OvR Accuracy |
|---|---|:---:|:---:|:---:|:---:|
| **SVM (Tri)** | `White_Males` | 0.9694 | 0.9536 | 0.9614 | 98.70% |
| | `Black_Males` | 0.9417 | 0.9549 | 0.9483 | 98.29% |
| | `White_Females` | 0.9472 | 0.9241 | 0.9355 | 97.82% |
| | `Asian_Males` | 0.9444 | 0.9239 | 0.9341 | 97.78% |
| | `Asian_Females` | 0.9250 | 0.9250 | 0.9250 | 97.50% |
| | `Black_Females` | 0.8944 | 0.9415 | 0.9174 | 97.31% |
| **LR (Tri)** | `White_Males` | 0.9611 | 0.9505 | 0.9558 | 98.52% |
| | `Black_Males` | 0.9306 | 0.9571 | 0.9437 | 98.15% |
| | `White_Females` | 0.9222 | 0.9121 | 0.9171 | 97.22% |
| | `Asian_Males` | 0.9278 | 0.9076 | 0.9176 | 97.22% |
| | `Asian_Females` | 0.9111 | 0.9162 | 0.9136 | 97.13% |
| | `Black_Females` | 0.9111 | 0.9213 | 0.9162 | 97.22% |
