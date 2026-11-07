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

Pengenalan atribut demografis wajah interseksional menghadapi tantangan variasi ekspresi afektif, penuaan biologis, kemiripan visual antarsubkelompok, keterbatasan representasi domain tunggal, serta risiko kebocoran identitas akibat pemisahan citra acak. Penelitian ini mengusulkan kerangka fusi multi-domain Vision Transformer (ViT) yang mengintegrasikan representasi biometrik wajah, ekspresi emosi, dan usia biologis melalui konkatenasi 2.304 dimensi, dipadukan dengan penskalaan fitur, Principal Component Analysis, dan optimasi empat pengklasifikasi pembelajaran mesin klasik. Evaluasi menerapkan protokol utama Subject-Disjoint bebas kebocoran identitas serta protokol Stratified Split berbasis citra sebagai studi ablasi kebocoran data. Pada protokol Subject-Disjoint utama, Logistic Regression memimpin performa dengan akurasi 88.66%, presisi makro 88.75%, recall makro 88.66%, dan F1-score makro 88.68%, setara secara inferensial dengan Support Vector Machine yang meraih akurasi 88.61%, presisi makro 88.66%, recall makro 88.61%, dan F1-score makro 88.63%. Uji McNemar membuktikan keunggulan fusi tri-domain atas domain tunggal (p < 0.001) serta mengonfirmasi paritas prediktif antara Logistic Regression dan Support Vector Machine (p = 1.0000). Sebaliknya, pada studi ablasi Stratified Split, keberadaan tumpang tindih identitas menghasilkan estimasi performa optimis semu, di mana Support Vector Machine dan Logistic Regression masing-masing mencatat akurasi 93.70% dan F1-score makro 93.69% serta akurasi 92.73% dan F1-score makro 92.73%. Evaluasi keadilan algoritmik pada model teratas menunjukkan stabilitas prediksi lintas subkelompok dengan rentang recall 84.72% hingga 94.44% dan kesenjangan Equal Opportunity Difference sebesar 9.72 poin persentase.

---

## Keywords

Biometrics, face recognition, feature extraction, intersectional demographic recognition, multi-domain feature fusion, Vision Transformer.
