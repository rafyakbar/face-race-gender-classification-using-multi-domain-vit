# Multi-Domain Vision Transformer Fusion for Intersectional Demographic Classification from Facial Images

## Authors & Affiliation

1. **Dr. Ir. Ricky Eka Putra, S.Kom., M.Kom.** ([ORCID: 0000-0002-5515-7967](https://orcid.org/0000-0002-5515-7967))  
   Department of Informatics, Faculty of Informatics, Universitas Negeri Surabaya, Surabaya 60231, Indonesia  
   Corresponding Author Email: `rickyeka@unesa.ac.id`

2. **Rezky Arisanti Putri, S.Kom., M.Kom.** ([ORCID: 0009-0000-8021-1833](https://orcid.org/0009-0000-8021-1833))  
   Department of Informatics, Faculty of Informatics, Universitas Negeri Surabaya, Surabaya 60231, Indonesia

3. **Dr. Yuni Yamasari, S.Kom., M.Kom.** ([ORCID: 0000-0001-9719-3491](https://orcid.org/0000-0001-9719-3491))  
   Department of Informatics, Faculty of Informatics, Universitas Negeri Surabaya, Surabaya 60231, Indonesia

4. **Rafy Aulia Akbar, S.Kom., M.Kom.** ([ORCID: 0009-0003-6991-0694](https://orcid.org/0009-0003-6991-0694))  
   Department of Informatics, Faculty of Informatics, Universitas Negeri Surabaya, Surabaya 60231, Indonesia

5. **Assoc. Prof. Dr. Shukor Sanim Mohd Fauzi** ([ORCID: 0000-0003-4333-7853](https://orcid.org/0000-0003-4333-7853))  
   School of Computing Sciences, College of Computing, Informatics and Mathematics, Universiti Teknologi MARA, Cawangan Perlis, Kampus Arau, 02600 Arau, Perlis, Malaysia  
   Email: `shukorsanim@uitm.edu.my`

---

## Abstract

Pengenalan atribut demografis wajah (ras dan gender) interseksional menghadapi tantangan variasi ekspresi afektif, penuaan biologis, phenotypic overlap, keterbatasan representasi single-domain, serta ancaman kebocoran data (data leakage) akibat pemisahan berbasis citra acak (random image-level split). Untuk mengatasi kendala tersebut, penelitian ini mengusulkan kerangka fusi multi-domain Vision Transformer (ViT) yang mengintegrasikan tiga representasi laten terpisah, yaitu geometri biometrik wajah, ekspresi afektif, dan usia biologis, melalui konkatenasi langsung berdimensi 2.304. Evaluasi menerapkan protokol Strict Subject-Disjoint Partitioning bebas kebocoran identitas (480 subjek latih dan 120 subjek uji held-out) pada dataset DemogPairs. Berbasis backbone ViT pra-latih yang dibekukan, representasi laten diproses melalui pipeline modular penskalaan fitur, reduksi dimensionalitas Principal Component Analysis (PCA), dan empat pengklasifikasi pembelajaran mesin klasik, yaitu Random Forest (RF), Gaussian Naive Bayes (GNB), Logistic Regression (LR), serta Support Vector Machine (SVM), yang dioptimasi via 5-Fold StratifiedGroupKFold Grid Search Cross-Validation (GridSearchCV) pada tingkat-fold terisolasi. Hasil empiris membuktikan fusi tri-domain meraih performa terbaik pada pengklasifikasi linier dan non-linier, di mana LR meraih akurasi puncak 88.66% (F1-score: 88.68%) dan SVM meraih 88.61% (F1-score: 88.63%) pada data uji held-out. Uji hipotesis inferensial berpasangan (McNemar test) mengonfirmasi keunggulan signifikan fusi tri-domain atas baseline domain tunggal (p < 0.001) dan menunjukkan paritas prediktif antara LR dan SVM, namun LR menawarkan efisiensi komputasi yang jauh lebih unggul untuk inferensi praktis. Model ini juga menunjukkan stabilitas performa lintas enam kelompok interseksional dengan rentang recall 84.44% hingga 92.50%.

---

## Keywords

Biometrics, face recognition, feature extraction, intersectional demographic recognition, multi-domain feature fusion, Vision Transformer.
