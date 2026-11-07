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

Pengenalan atribut demografis wajah interseksional (ras dan gender) menghadapi tantangan variasi ekspresi afektif, penuaan biologis, phenotypic overlap, keterbatasan representasi domain tunggal, serta ancaman kebocoran identitas akibat pemisahan berbasis citra acak. Penelitian ini mengusulkan kerangka fusi multi-domain Vision Transformer (ViT) yang mengintegrasikan representasi biometrik wajah, ekspresi afektif, dan usia biologis melalui konkatenasi langsung berdimensi 2.304. Evaluasi menerapkan protokol Strict Subject-Disjoint Partitioning bebas kebocoran identitas pada dataset DemogPairs. Berbasis backbone ViT beku, representasi laten diproses melalui penskalaan fitur, Principal Component Analysis (PCA), dan empat pengklasifikasi klasik (RF, GNB, LR, SVM) yang dioptimasi via 5-Fold StratifiedGroupKFold GridSearchCV pada tingkat-fold terisolasi. Hasil empiris membuktikan keunggulan fusi tri-domain pada pengklasifikasi linier dan non-linier. Logistic Regression memimpin tolok ukur dengan akurasi 88.66%, presisi makro 88.75%, recall makro 88.66%, F1-score makro 88.68%, dan selang kepercayaan 95% Wilson Score [87.25%, 89.93%], setara secara statistik dengan Support Vector Machine yang mencatat akurasi 88.61%, presisi makro 88.66%, recall makro 88.61%, F1-score makro 88.63%, dan selang kepercayaan 95% Wilson Score [87.20%, 89.88%]. Uji hipotesis McNemar mengonfirmasi keunggulan signifikan fusi tri-domain atas domain tunggal (p < 0.001) serta menegaskan paritas prediktif antara Logistic Regression dan Support Vector Machine (p = 1.0000). Namun, Logistic Regression unggul mutlak dalam efisiensi komputasi dengan latensi inferensi 0.0046 ms per sampel dan ukuran model 0.11 MB, beroperasi lebih dari 1.000 kali lebih cepat serta 330 kali lebih hemat memori dibanding Support Vector Machine. Model teratas mempertahankan stabilitas lintas enam kelompok interseksional dengan rentang recall 84.72% hingga 94.44% dan kesenjangan Equal Opportunity Difference sebesar 9.72 poin persentase.

---

## Keywords

Biometrics, face recognition, feature extraction, intersectional demographic recognition, multi-domain feature fusion, Vision Transformer.
