# IV. RESULTS AND DISCUSSION

## A. Global Performance

Evaluasi empiris Random Forest melintasi tujuh skema konfigurasi fitur pada dataset uji held-out dengan protokol Strict Subject-Disjoint ($N = 2.160$) dirangkum pada [Table VII](#tab7). Hasil pengujian menunjukkan bahwa konfigurasi Tri-Domain mencapai performa tertinggi dengan Akurasi 85.00%, Presisi 85.06%, Recall 85.00%, dan F1-Score 84.93%. Capaian tersebut mengungguli skema dual-domain `Emotion ⊕ Face` (Akurasi 84.86% dan F1-Score 84.79%) serta melampaui baseline domain tunggal `Face` sebesar 84.03%. Domain `Age` mencatat akurasi terendah (71.81%), mencerminkan tantangan partisi fitur kontinu berdimensi tinggi melalui pemotongan pohon acak ortogonal. Mayoritas konfigurasi memilih reduksi PCA 0.75, menegaskan bahwa penambahan dimensi fitur tanpa seleksi representasi meningkatkan varians pemilihan fitur acak pada simpul pohon [[48]](06_references.md#ref48).

<a id="tab7"></a>
**Table VII. Performance Benchmark of Random Forest across Seven Feature Configurations on Subject-Disjoint Test Set ($N = 2,160$).**

| Feature Configuration | Latent Dimension | Accuracy (%) | Precision (%) | Recall (%) | F1-Score (%) | Best Hyperparameters |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| Face | 768 | 84.03 | 84.13 | 84.03 | 84.03 | n_est=200, depth=20, max_feat=log2, min_split=5, min_leaf=1, pca=PCA(0.75), scaler=None |
| Emotion | 768 | 76.11 | 76.02 | 76.11 | 76.03 | n_est=200, depth=None, max_feat=sqrt, min_split=2, min_leaf=2, pca=PCA(0.75), scaler=None |
| Age | 768 | 71.81 | 71.76 | 71.81 | 71.70 | n_est=200, depth=None, max_feat=log2, min_split=5, min_leaf=2, pca=PCA(0.75), scaler=None |
| Emotion ⊕ Face | 1,536 | 84.86 | 84.93 | 84.86 | 84.79 | n_est=200, depth=None, max_feat=sqrt, min_split=2, min_leaf=1, pca=PCA(0.75), scaler=MinMaxScaler |
| Face ⊕ Age | 1,536 | 84.86 | 84.88 | 84.86 | 84.78 | n_est=200, depth=None, max_feat=sqrt, min_split=2, min_leaf=1, pca=None, scaler=None |
| Emotion ⊕ Age | 1,536 | 77.31 | 77.34 | 77.31 | 77.28 | n_est=200, depth=20, max_feat=log2, min_split=2, min_leaf=2, pca=PCA(0.75), scaler=None |
| **Face ⊕ Emotion ⊕ Age** | **2,304** | **85.00** | **85.06** | **85.00** | **84.93** | **n_est=200, depth=30, max_feat=sqrt, min_split=2, min_leaf=1, pca=None, scaler=MinMaxScaler** |

Evaluasi performa Gaussian Naive Bayes melintasi tujuh konfigurasi fitur pada dataset uji held-out disajikan pada [Table VIII](#tab8). Berbeda dengan pengklasifikasi lainnya, puncak performa GNB diraih oleh konfigurasi dual-domain `Emotion ⊕ Face` dengan Akurasi 84.31%, Presisi 84.37%, Recall 84.31%, dan F1-Score 84.30%. Pada konfigurasi Tri-Domain, performa klasifikasi menurun menjadi Akurasi 83.61% dan F1-Score 83.64%. Penurunan ini merupakan konsekuensi langsung dari pelanggaran asumsi independensi fitur bersyarat kelas yang mendasari distribusi Gaussian multivariat. Ketika dimensi diperluas ke 2.304 dimensi melalui penggabungan tiga domain, korelasi laten antarfitur meningkat tajam sehingga estimasi probabilitas univariat terdistorsi. Sementara itu, kategori domain tunggal `Face` mencatat Akurasi 82.55%, melampaui `Emotion` (72.13%) dan `Age` (67.08%). Seluruh konfigurasi secara seragam memilih reduksi PCA 0.75.

<a id="tab8"></a>
**Table VIII. Performance Benchmark of Gaussian Naive Bayes across Seven Feature Configurations on Subject-Disjoint Test Set ($N = 2,160$).**

| Feature Configuration | Latent Dimension | Accuracy (%) | Precision (%) | Recall (%) | F1-Score (%) | Best Hyperparameters |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| Face | 768 | 82.55 | 82.68 | 82.55 | 82.50 | var_smoothing=4.1246e-02, pca=PCA(0.75), scaler=MinMaxScaler |
| Emotion | 768 | 72.13 | 72.51 | 72.13 | 71.99 | var_smoothing=5.8780e-03, pca=PCA(0.75), scaler=MinMaxScaler |
| Age | 768 | 67.08 | 66.91 | 67.08 | 66.86 | var_smoothing=8.3768e-04, pca=PCA(0.75), scaler=MinMaxScaler |
| **Emotion ⊕ Face** | **1,536** | **84.31** | **84.37** | **84.31** | **84.30** | **var_smoothing=1.1253e-02, pca=PCA(0.75), scaler=MinMaxScaler** |
| Face ⊕ Age | 1,536 | 83.06 | 83.47 | 83.06 | 83.10 | var_smoothing=1.1253e-02, pca=PCA(0.75), scaler=MinMaxScaler |
| Emotion ⊕ Age | 1,536 | 75.88 | 75.97 | 75.88 | 75.78 | var_smoothing=1.1253e-02, pca=PCA(0.75), scaler=MinMaxScaler |
| Face ⊕ Emotion ⊕ Age | 2,304 | 83.61 | 83.79 | 83.61 | 83.64 | var_smoothing=1.1253e-02, pca=PCA(0.75), scaler=None |

Hasil benchmark empiris multinomial Logistic Regression melintasi tujuh konfigurasi fitur pada dataset uji held-out dipaparkan pada [Table IX](#tab9). Sebagai model terbaik, LR Tri-Domain `Face ⊕ Emotion ⊕ Age` meraih Akurasi 88.66%, Presisi 88.75%, Recall 88.66%, dan F1-Score 88.68%. Capaian ini secara konsisten melampaui baseline domain tunggal `Face` (Akurasi 86.39%), `Emotion` (85.23%), dan `Age` (81.48%), serta mengungguli skema dual-domain `Emotion ⊕ Face` (87.45%). Keberhasilan LR membuktikan komplementaritas linier yang sangat kuat antarentang representasi laten. Melalui fungsi aktivasi Softmax ter-regularisasi penalti $L_2$, LR memodelkan kovariat fitur multivariabel berdimensi tinggi secara efektif [[49]](06_references.md#ref49). Bobot linier model menghasilkan batas keputusan hiperplane pemisah multikelas yang stabil melalui regularisasi terbobot [[50]](06_references.md#ref50), di mana seluruh konfigurasi mempertahankan dimensi penuh tanpa reduksi PCA.

<a id="tab9"></a>
**Table IX. Performance Benchmark of Logistic Regression across Seven Feature Configurations on Subject-Disjoint Test Set ($N = 2,160$).**

| Feature Configuration | Latent Dimension | Accuracy (%) | Precision (%) | Recall (%) | F1-Score (%) | Best Hyperparameters |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| Face | 768 | 86.39 | 86.46 | 86.39 | 86.40 | C=0.1, solver=saga, max_iter=500, pca=None, scaler=None |
| Emotion | 768 | 85.23 | 85.35 | 85.23 | 85.27 | C=0.1, solver=lbfgs, max_iter=500, pca=None, scaler=None |
| Age | 768 | 81.48 | 81.45 | 81.48 | 81.46 | C=0.1, solver=lbfgs, max_iter=500, pca=None, scaler=None |
| Emotion ⊕ Face | 1,536 | 87.45 | 87.59 | 87.45 | 87.49 | C=1, solver=saga, max_iter=500, pca=None, scaler=MinMaxScaler |
| Face ⊕ Age | 1,536 | 87.41 | 87.44 | 87.41 | 87.40 | C=0.1, solver=lbfgs, max_iter=500, pca=None, scaler=MinMaxScaler |
| Emotion ⊕ Age | 1,536 | 86.67 | 86.68 | 86.67 | 86.67 | C=0.1, solver=saga, max_iter=500, pca=None, scaler=MinMaxScaler |
| **Face ⊕ Emotion ⊕ Age** | **2,304** | **88.66** | **88.75** | **88.66** | **88.68** | **C=0.1, solver=saga, max_iter=500, pca=None, scaler=MinMaxScaler** |

Perkembangan performa Support Vector Machine melintasi seluruh konfigurasi fitur disajikan pada [Table X](#tab10). Sebagai model terbaik kedua, SVM Tri-Domain `Face ⊕ Emotion ⊕ Age` mencapai Akurasi 88.61%, Presisi 88.71%, Recall 88.61%, dan F1-Score 88.63% melalui formulasi kernel RBF standar [[51]](06_references.md#ref51) dengan parameter penalti $C = 10$. Evaluasi memperlihatkan lonjakan performa signifikan dari domain tunggal `Face` (Akurasi 86.16%) menuju konfigurasi dual-domain `Emotion ⊕ Face` (Akurasi 88.43%) dengan kenaikan bersih 2.27 percentage points. Namun, penambahan fitur usia pada skema Tri-Domain hanya menghasilkan peningkatan marjinal sebesar 0.18 percentage points. Fenomena ini mengindikasikan kejenuhan representasi asimtotik pada pemetaan ruang Hilbert non-linier kernel RBF, di mana manifold gabungan biometrik dan emosi telah mengekstraksi hampir seluruh varians diskriminatif utama subkelompok interseksional.

<a id="tab10"></a>
**Table X. Performance Benchmark of Support Vector Machine across Seven Feature Configurations on Subject-Disjoint Test Set ($N = 2,160$).**

| Feature Configuration | Latent Dimension | Accuracy (%) | Precision (%) | Recall (%) | F1-Score (%) | Best Hyperparameters |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| Face | 768 | 86.16 | 86.24 | 86.16 | 86.19 | C=0.01, poly, γ=scale, deg=3, pca=None, scaler=MinMaxScaler |
| Emotion | 768 | 85.79 | 85.84 | 85.79 | 85.80 | C=10, rbf, γ=scale, pca=None, scaler=None |
| Age | 768 | 82.55 | 82.68 | 82.55 | 82.58 | C=10, rbf, γ=scale, pca=None, scaler=None |
| Emotion ⊕ Face | 1,536 | 88.43 | 88.50 | 88.43 | 88.44 | C=0.1, poly, γ=scale, deg=2, pca=None, scaler=MinMaxScaler |
| Face ⊕ Age | 1,536 | 87.55 | 87.66 | 87.55 | 87.57 | C=10, rbf, γ=scale, pca=None, scaler=None |
| Emotion ⊕ Age | 1,536 | 86.25 | 86.26 | 86.25 | 86.24 | C=10, rbf, γ=scale, pca=None, scaler=None |
| **Face ⊕ Emotion ⊕ Age** | **2,304** | **88.61** | **88.71** | **88.61** | **88.63** | **C=10, rbf, γ=scale, pca=None, scaler=MinMaxScaler** |

Sintesis komparatif antarmodel pada [Table VII](#tab7), [Table VIII](#tab8), [Table IX](#tab9), dan [Table X](#tab10) menegaskan bahwa efektivitas fusi representasi multi-domain bersifat sangat bergantung pada arsitektur pengklasifikasi. Model linier LR dan non-linier SVM memimpin tolok ukur global dengan performa puncak kompetitif pada konfigurasi Tri-Domain (Akurasi 88.66% berbanding 88.61%), dengan selisih marjinal hanya satu citra uji dari total 2.160 sampel. Sebaliknya, RF dan GNB memperlihatkan dinamika batas keputusan yang berbeda. RF mencapai akurasi 85.00% pada Tri-Domain namun tertahan oleh kompleksitas partisi pohon acak berdimensi tinggi, sedangkan GNB mencapai titik optimal pada skema dual-domain (84.31%) akibat kendala asumsi independensi kovariansi. Temuan ini membuktikan bahwa fusi fitur laten multi-domain paling efektif dipetakan oleh pengklasifikasi dengan estimasi batas keputusan global.

Profil efisiensi komputasi dievaluasi melalui dua aspek terukur pada [Table XI](#tab11) dan [Table XII](#tab12). Ekstraksi fitur ViT secara offline terakselerasi GPU mencatatkan durasi 39.74 ms untuk Face, 39.65 ms untuk Emotion, dan 45.11 ms untuk Age, dengan total durasi tri-domain sebesar 124.50 ms per citra (total 22.41 menit untuk 10.800 citra dengan ukuran cache 90 MB). Pada pelatihan validasi silang 5-fold di CPU, GNB memerlukan 25.49 menit pada dual-domain, disusul LR sebesar 54.78 menit, RF sebesar 110.47 menit, dan SVM mencapai 511.10 menit. Pada tahap pengujian, kepala pengklasifikasi hilir LR menunjukkan keunggulan dengan latensi hanya 0.0046 ms per sampel, 1.027 kali lebih cepat dibandingkan SVM (4.6785 ms). Dari segi kebutuhan penyimpanan, LR hanya membutuhkan berkas model 0.11 MB, 330 kali lebih ringkas dibandingkan SVM (36.60 MB), menetapkan LR sebagai arsitektur hilir paling optimal untuk implementasi praktis.

<a id="tab11"></a>
**Table XI. Vision Transformer Feature Extraction Runtime and Storage Profile.**

| Feature Domain | Pre-Trained Backbone Checkpoint | Latent Dim ($D$) | Execution Hardware | Latency (ms/img) | Throughput (img/s) | Total Extraction Duration | Backbone Size (MB) | Feature Cache (MB) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Biometric Face | `skutaada/VIT-VGGFace` | 768 | NVIDIA RTX 4060 GPU | 39.74 | 25.16 | 429.22 s (7m 09s) | 371 | ≈30 (raw 31.64) |
| Facial Emotion | `dima806/facial_emotions_image_detection` | 768 | NVIDIA RTX 4060 GPU | 39.65 | 25.22 | 428.24 s (7m 08s) | 343 | ≈30 (raw 31.64) |
| Facial Age | `dima806/facial_age_image_detection` | 768 | NVIDIA RTX 4060 GPU | 45.11 | 22.17 | 487.17 s (8m 07s) | 343 | ≈30 (raw 31.64) |
| **Tri-Domain Fusion** | **All Three ViT-Base Models** | **2,304** | **NVIDIA RTX 4060 GPU** | **124.50** | **8.03** | **1,344.64 s (22m 25s)** | **1,057** | **≈90 (raw 94.92)** |

*Catatan Table XI: Nilai ekstraksi fitur diukur langsung menggunakan akselerasi GPU NVIDIA RTX 4060 dengan batch inference torch.no_grad() dan input citra $224 \times 224$ piksel. Ukuran cache fitur pada penyimpanan sekunder menggunakan kompresi joblib level 9.*

<a id="tab12"></a>
**Table XII. Downstream Classifier Training Runtime, Inference Latency, and Memory Footprint Profile.**

| Classifier | Feature Scheme | Latent Dim ($D$) | Accuracy (%) | Macro F1 (%) | 5-Fold CV Training Time (s) | Inference Latency (ms/sample) | Model Size (MB) | RAM Footprint (MB) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Logistic Regression (LR)** | **Tri-Domain** | **2,304** | **88.66** | **88.68** | **3,287.07 (54.78 min)** | **0.0046** | **0.11** | **≈0.11 (buffer 18.98)** |
| Support Vector Machine (SVM) | Tri-Domain | 2,304 | 88.61 | 88.63 | 30,666.02 (511.10 min) | 4.6785 | 36.60 | ≈36.60 (buffer 18.98) |
| Random Forest (RF) | Tri-Domain | 2,304 | 85.00 | 84.93 | 6,628.03 (110.47 min) | 0.0334 | 6.19 | ≈6.19 (buffer 18.98) |
| Gaussian Naive Bayes (GNB) | Dual-Domain (`Emotion ⊕ Face`) | 1,536 | 84.31 | 84.30 | 1,529.50 (25.49 min) | 0.0088 | 0.78 | ≈0.78 (buffer 12.66) |

*Catatan Table XII: Waktu pelatihan merepresentasikan durasi wall-clock GridSearchCV 5-fold pada CPU standar. Latensi inferensi mengukur waktu prediksi pengklasifikasi hilir per sampel uji pada set held-out ($N = 2.160$). Buffer RAM merepresentasikan alokasi memori deterministik nbytes untuk menampung matriks fitur data uji float32 ($2.160 \times 2.304 \times 4\text{ bytes} \approx 18.98\text{ MB}$). Total latensi end-to-end per citra adalah penjumlahan waktu ekstraksi GPU dan latensi inferensi hilir ($\approx 124.505\text{ ms}$ untuk LR vs $\approx 129.179\text{ ms}$ untuk SVM).*
