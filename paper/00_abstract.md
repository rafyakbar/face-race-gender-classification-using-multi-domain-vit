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

---

## Abstract

Pengenalan atribut demografis wajah seperti ras dan gender secara simultan menghadapi tantangan variasi ekspresi, penuaan biologis, phenotypic overlap, serta keterbatasan representasi single-domain. Penelitian ini mengusulkan kerangka kerja fusi fitur laten multi-domain yang mengintegrasikan representasi visual dari tiga model Vision Transformer (ViT) pre-trained spesifik tugas untuk biometrik wajah, ekspresi afektif, dan estimasi usia, yang dipadukan dengan optimasi pipeline machine learning klasik untuk klasifikasi enam intersectional demographic subgroups pada dataset DemogPairs. Representasi laten diekstraksi secara offline dari token [CLS] berdimensi 768 per domain dan digabungkan menjadi vektor fusi tri-domain berdimensi 2.304. Tujuh konfigurasi fitur dievaluasi melalui 5-Fold Stratified Cross-Validation pada empat classifier: Random Forest (RF), Gaussian Naive Bayes (GNB), Logistic Regression (LR), dan Support Vector Machine (SVM) dengan hyperparameter tuning via Grid Search Cross-Validation (GridSearchCV). Hasil eksperimen menunjukkan bahwa fusi tri-domain meraih performa tertinggi pada tiga dari empat classifier yang dievaluasi, dengan model SVM berbasis kernel polynomial degree 2 menghasilkan performa terbaik, mencatat Accuracy 93.70%, Precision 93.72%, Recall 93.70%, dan F1-Score 93.69% pada data uji held-out. Evaluasi granular pada keenam subkelompok mencatat rentang F1-Score antara 91.74% dan 96.14%, yang membuktikan efektivitas fusi representasi laten multi-domain dalam mengenali atribut demografis interseksional.

---

## Keywords

Facial demographic recognition; intersectional classification; Vision Transformer; multi-domain feature fusion; algorithmic fairness; Support Vector Machine; DemogPairs.
