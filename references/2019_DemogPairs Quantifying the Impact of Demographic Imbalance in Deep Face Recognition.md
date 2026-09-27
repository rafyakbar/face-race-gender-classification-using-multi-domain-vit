See discussions, stats, and author profiles for this publication at: https://www.researchgate.net/publication/334424870 

## DemogPairs: Quantifying the Impact of Demographic Imbalance in Deep Face Recognition 

**Conference Paper** · May 2019 

DOI: 10.1109/FG.2019.8756625 



<!-- Start of picture text -->
CITATIONS READS<br>89 908<br>2 authors:<br>Isabelle Hupont Torres Carles Fernández<br>European Commission 51 PUBLICATIONS 754 CITATIONS<br>90 PUBLICATIONS 1,195 CITATIONS<br>SEE PROFILE<br>SEE PROFILE<br><!-- End of picture text -->

All content following this page was uploaded by Isabelle Hupont Torres on 22 January 2020. 

The user has requested enhancement of the downloaded file. 

# **DemogPairs: Quantifying the Impact of Demographic Imbalance in Deep Face Recognition** 

Isabelle Hupont and Carles Fern´andez Herta Security, Barcelona, Spain 

**_Abstract_ — Although deep face recognition has achieved impressive results in recent years, controversy has arisen regarding racial and gender bias of the models, questioning their deployment into sensitive scenarios. This work quantifies for the first time the demographic imbalance of popular public face datasets in terms of identity, gender and ethnicity. We also publicly release DemogPairs, a new validation set with 10.8K facial images and 58.3M identity verification pairs, distributed in demographically-balanced folds of Asian, Black and White females and males. A benchmark of experiments is carried out using DemogPairs over state-of-the-art deep face recognition models (SphereFace, FaceNet and ResNet50), in order to analyze their cross-demographic behavior. Experimental results demonstrate that studied models suffer from a very structured and damaging demographic bias. Our experiments shine a light on novel testing protocols to appropriately validate the generalization capabilities of face recognition models.** 

### I. INTRODUCTION 

Convolutional Neural Networks (CNNs) have significantly contributed to the improvement of the state-of-the-art in computer vision applications and facilitated deployments in highly unconstrained scenarios. A particularly interesting field of application is face recognition for video-surveillance, where faces often exhibit challenges such as unconstrained pose, lighting, blur, non-neutral expressions or occlusions. Typical video-surveillance locations are also characterized by ethnically diverse populations (e.g. train stations, airports, border controls). Models need to be invariant to this diversity and to generalize well across facial characteristics. 

The key ingredient for success of deep face recognition is the use of large quantities of training data to cover a wide range of variations in facial appearance. In recent years, an increasing number of very large face datasets has become publicly available. Unfortunately, these datasets are highly imbalanced at several levels, which may dramatically impact the performance of deep models [13], [2]. 

One of the major sources of imbalance comes from the disparity in the number of training samples among subjects. It is common to find between-identities imbalance ratios on the order of 10:1, 50:1, 100:1 or even 500:1. CNNs aim to learn a good feature space, in which the faces of the same person become closer to each other, whereas faces of other identities move farther away. An identity with a small number of samples can only claim a small partition in the feature space, therefore resulting inevitably underrepresented [10]. 

Another important, yet under-studied, source of imbalance in current datasets is related to demographics. Research in 978-1-7281-0089-0/19/$31.00 _⃝_ c 2019 IEEE 

psychology and cognitive science has demonstrated that race perception is not only determined by skin color information, but also by morphological racially-discriminative salient facial features of the subject, such as eye corners or nose tip [18]. Related with this race perceptual model is the so called _other-race-effect_ (ORE): given a face recognition task, human observers tend to perform significantly better with their own-race as compared to others [33]. The explanation for this bias is that people become experts in recognizing faces of their own race because of having more interest and contact with people of their same ethnicity. Interestingly, previous studies found connections between ORE and its influence on automatic face processing. Phillips et al. [22] demonstrated that algorithms developed by Westerners tend to recognize Caucasian faces more accurately than Asian faces, and vice-versa, indicating that algorithms also favor the majority race data in the training set. Other own-group biases, namely own-age bias and own-gender bias, have also been reported [30]. Consequently, it is of utmost importance to train with demographically balanced sets [9]. 

While the imbalance problem has been well-studied for face recognition based on traditional machine learning [35], [20], its implications have not yet been systematically analyzed for deep face recognition. More importantly, it has been mostly tackled at identity level, ignoring the influence of having a dataset that is also demographically biased [34], [32]. This work quantifies to what extent data imbalance impacts deep face recognition, not only from the perspective of identity but also taking into account gender and ethnicity demographic cues. More particularly, it makes the following contributions: 

- An in-depth demographic annotation and analysis of state-of-the-art face datasets is performed, to quantify their imbalance in terms of gender and ethnicity. 

- We publicly release DemogPairs, a new demographically-balanced validation set specially built to evaluate the impact of different demographic factors. 

- This set is used to explore the cross-demographic behavior of popular deep face recognition models, through a novel benchmark of experiments. 

The paper is organized as follows. Section II reviews literature. Section III quantifies the demographic gap in public deep face recognition datasets. Section IV describes how DemogPairs was built and the experiments carried out in this study. The obtained results are presented and discussed in Section V. Finally, Section VI concludes the paper. 

### II. RELATED WORK 

Choices about architectures for deep face recognition have caught the attention of most researchers. Even though the advancement of face recognition is partially due to the gradual improvement of network architecture designs, it is also the underlying ability of CNNs to learn from massive data that allows these techniques to be so effective. CNNs require very large datasets for training, ideally with hundreds of thousands or even millions of labeled face images [1]. In the field of deep face recognition, such large public datasets have been missing, and therefore most of the recent advances in the community remain restricted to Internet giants such as Facebook, Google, Baidu or Microsoft. This was originally demonstrated with Facebook’s DeepFace [26], which used a relatively simple deep architecture with over 4M images for training, and obtained far more impressive results than its predecessors. More recently, the FaceNet architecture by Google [25] was trained using 200M images and 8M unique identities. The size of this dataset is almost three orders of magnitude larger than any publicly available face dataset. 

Public datasets available to date can be divided into two groups: (i) deep datasets, i.e. datasets with many images per subject; and (ii) wide datasets, i.e. datasets with many subjects but fewer images per subject. Datasets considered wide typically provide at most 10 images on average per identity. Well-known examples are Labeled Faces in the Wild (LFW) [14] and MegaFace [15]. They are generally used for validating or testing purposes rather than for training. For instance, LFW has long been the _de facto_ validation dataset to evaluate face recognition performances [10]. Datasets considered deep usually contain more than 30 images on average per subject. Examples include Casia Web Faces (CWF) [31], VGGFace [21] and the recent VGGFace2 [4]. They are more varied in pose, expression, illumination and quality, and therefore more suitable for training. The only deep dataset that has been exclusively released as an evaluation benchmark is the IARPA Janus Benchmark-B (IJB-B) [16]. 

The general approach followed for building public datasets is web crawling. A negative consequence is that most of them are highly noisy, i.e. many images have incorrect identity labels. Microsoft’s MS-Celeb-1M [11] (10M images from 100K celebrities) and MegaFace (4.7M images from 690K identities) are the largest-scale public datasets to date. However, images were directly retrieved from the web without any manual filtering, and their noise ratio is higher than 30% [28]. Recent studies have demonstrated a clear degradation in performance when noise level increases. For instance, Reale et al. [23] show that a manual correction of 10% of mislabeled samples produces roughly similar results to doubling the dataset size. 

Another consequence of web crawling is that collected images generally belong to celebrities. Training datasets are intentionally conceived to be disjoint with those which are frequently used as validation, such as LFW. Occasionally, however, they overlap significantly, as depicted in Table I. The reason is that the majority of datasets draw upon a 

TABLE I: Identities repeated among publicly available face datasets. Percentages are taken over the identities in the column database. Parentheses denote the total number of identities in each database. 

||CWF|LFW|IJB-B|VGGFace|VGGFace2|
|---|---|---|---|---|---|
|CWF|**(10572)**|0.4%|4.9%|70.3%|11.1%|
|LFW|0.0%|**(5749)**|19.0%|0.0%|6.4%|
|IJB-B|0.8%|6.1%|**(1845)**|0.1%|0.6%|
|VGGFace|16.9%|0.0%|0.2%|**(2622)**|0.2%|
|VGGFace2|9.3%|10.2%|3.1%|0.7%|**(9131)**|



relatively small group of public personalities with highly available images. Moreover, the imbalance between the number of images for the most famous subjects and the least popular ones can reach ratios up to 500:1. 

Besides imbalance in the number of images per subject, it is important to highlight that most datasets are not annotated in terms of ethnicity and gender. Without these annotations, it turns out to be difficult to quantitatively evaluate the level of demographic imbalance and its impact. Indeed, imbalance and its related generalization problem have rarely been tackled from a demographic perspective. Some previous works propose techniques such as cost-sensitive learning [10] or sampling methods [7], [17] to mitigate imbalance, but focus on identity exclusively. As highlighted in Section I, many discriminative features for face recognition are highly related to ethnicity and gender factors. Deep face recognition may be simultaneously impacted by imbalance both at identity and demographic levels but, to the best of our knowledge, as of yet there is no systematic study in the literature that quantifies this impact. Hence, thorough cross-demographic (cross-gender and cross-ethnicity) experiments are needed in deep face recognition literature. 

### III. IN-DEPTH DEMOGRAPHIC ANALYSIS OF PUBLIC FACIAL DATASETS 

As pointed out in section II, most public datasets are not annotated in terms of ethnicity and gender. In the context of this work, four experts on facial recognition manually annotated demographic information for the widely used CWF, LFW, VGGFace and VGGFace2 datasets. A fraction of the data (15%) was annotated twice by different annotators and the level of consensus was measured by Cohen’s kappa coefficient _K_ [27], obtaining excellent agreement values of _K_ = 0 _._ 98 for gender and _K_ = 0 _._ 94 for ethnicity. Table II summarizes the demographic information collected for these four datasets, as well as for IJB-B (as provided by its authors). 

A wide imbalance in terms of ethnicity was found, which potentially favors the ORE. As is depicted in the _ethnicity_ column in Table II, most public datasets contain a large majority of White faces. Gender imbalance is less dramatic but also present. Interestingly, the dataset most impacted by gender imbalance is LFW (25.8% of females), which has been widely used for testing in the past without taking this gender issue into consideration. 

TABLE II: Statistical demographic information of the most representative “in the wild” public face recognition datasets. 

|DB name|#Samples<br>Images/Videos|#IDs|#Samples/ID<br>min/avg/max|Gende<br>Female|r (%)<br>Male|E<br>Asian|thnicity (%<br>Black|)<br>White|Source|Noise<sup>_§_</sup>|
|---|---|---|---|---|---|---|---|---|---|---|
|CWF*|494K / –|10.6K|2 / 47 / 804|41.1%|58.9%|2.3%|8.6%|**89.1%**|IMDB|medium|
|LFW*<br>|13K / –|5.7K|1 / 2 / 530|25.8%|**74.2%**|6.2%|8.5%|**85.3%**|Yahoo News|low|
|VGGFace*<sup>_†_</sup>|1.4M / –|2.6K|121 / 570 / 1K|49.4%|50.6%|2.2%|9.4%|**88.4%**|Search engines|medium|
|VGGFace2*<br>|3.3M / –|9.1K|87 / 363 / 843|40.7%|59.3%|6.9%|9.2%|**83.9%**|Search engines|medium|
|IJB-B<sup>_‡_</sup>|12.7K / 7.1K|1.8K|1 / 30 / 1.7K|46.2%|53.8%|15.6%|10.3%|**74.1%**|Internal|clean|
|MegaFace|4.7M / –|690K|3 / 7 / 2.5K|N/A|N/A|N/A|N/A|N/A|Flickr|high|
|MS-Celeb-1M|10M / –|100K|100|N/A|N/A|N/A|N/A|N/A|Search engines|high|
|**DemogPairs**<br>**(this work)**|**10.8K / –**|**600**|**18**|**50.0%**|**50.0%**|**33.3%**|**33.3%**|**33.3%**|**CWF, VGGFace**<br>**and VGGFace2**|**clean**|



* We have manually annotated gender and ethnicity, as it was not provided in the original dataset. 

_†_ The original dataset contained 2.6M samples (1K per ID), but only 1.4M remained available for download as of February 2018. 

_‡_ Ethnicity percentages have been obtained from the Fitzpatrick I-to-VI skin type annotations [8] provided in the original dataset. Types I-III were assumed White, type IV Asian and types V-VI Black, in accordance with the guidelines used for manual annotation. 

_§_ Noise in terms of incorrectly annotated identity labels. This information has been taken from [28]. 

Many deep face recognition works claim near-perfect performances using training/validation datasets with virtually no subject overlap (e.g. CWF for training and LFW for validation) [19], [6]. Although these results are valuable, it must be taken under consideration that training and validation sets share demographic characteristics. Thus, it is important not to fall into overoptimism as the generalization capabilities of the models may still be limited. 

### IV. DEMOGPAIRS AND EXPERIMENTS 

This work aims to quantify the impact of demographic imbalance on deep face recognition. However, as previously discussed, current validation sets are not optimized to perform this kind of study. Next we introduce DemogPairs, a demographically-balanced validation set conceived to analyze the cross-demographic behavior of deep face models, and the set of experiments carried out with it. 

### _A. DemogPairs_ 

The DemogPairs validation set contains a total of 10.8K images, divided into 6 demographic folds: Asian females, Asian males, Black females, Black males, White females and White males. Each demographic fold has 100 subjects, with 18 images per subject (see last row in Table II). The dataset is clean, as noisy images have been manually discarded. It has been released to the scientific community as a tool to validate the demographic bias of any trained model<sup>1</sup> . 

DemogPairs has been built thanks to the exhaustive demographic annotation effort carried out in this work. Images have been taken from CWF, VGGFace and VGGFace2. The percentage of images collected from each of these datasets is, in the worst case, below 1.3% (0.13% for VGGFace2, 0.02% for VGGFace and 1.27% for CWF). Researchers wishing to train their models with any of these sets and to validate/test with DemogPairs, would need only to discard a small amount of training samples. DemogPairs therefore has minor impact on training processes and, at the same time, takes advantage 

> 1Publicly available at http://download.hertasecurity.com/ research/DemogPairs.zip 

of deep databases with many instances per subject. This approach greatly enlarges the set of potential pairs of positive and negative compared identities. 

As a result, a total of 58.3M evaluation pairs can be built from DemogPairs, distributed as shown in Table III. Each demographic fold leads to 15.3K positive pairs and 1.6M negative pairs. DemogPairs also offers 29.1M crossgender pairs (female-male pairs), 38.7M cross-ethnicity pairs (Asian-Black, Asian-White and Black-White pairs) and 19.5M cross-demographic pairs (female-male pairs of different ethnicities). Figure 1 illustrates the different types of pairs that can be obtained. 

The most challenging pairs of compared images are those coming from the same demographic group (top left quadrant in the figure), as morphological characteristics related to ethnicity and gender are shared between both individuals [36]. This type of pairs accounts for 16.67% of the total number of pairs in the dataset. Accordingly, the easiest pairs to evaluate are cross-demographic ones (bottom right quadrant), which are twice as many (33.33%). 

### _B. Description of the experiments_ 

In our experiments, the following state-of-the-art publicly available deep face recognition models are used over the DemogPairs: 

- **FaceNet** [25]: Two pre-trained models publicly available for TensorFlow [24], one trained with CWF and the other with MS-Celeb-1M. 

- **SphereFace** [19]: Caffe model published by its authors and pre-trained with CWF [29] . 

- **ResNet50** [12]: Caffe model provided by the authors of VGGFace2 [5]. It was fine-tuned on the training set of VGGFace2, based on a model pre-trained with MSCeleb-1M. 

These models have been previously validated on popular datasets, such as LFW and MegaFace, but their crossdemographic behavior is yet unexplored. The current study opens this line of research by carrying out three different experiments: 

TABLE III: Total number of positive and negative evaluation pairs in DemogPairs, by gender and ethnicity. 

||||Same|gender||Differen|t gender|
|---|---|---|---|---|---|---|---|
|||Female-<br>#negative pairs|Female<br>#positive pairs|Male<br>#negative pairs|-Male<br>#positive pairs|Female<br>#negative pairs|-Male<br>#positive pairs|
||Asian-Asian|1.6M|15.3K|1.6M|15.3K|3.2M|0|
|Same<br>|Black-Black|1.6M|15.3K|1.6M|15.3K|3.2M|0|
|ethnicity|White-White|1.6M|15.3K|1.6M|15.3K|3.2M|0|
||Asian-Black|3.2M|0|3.2M|0|6.5M|0|
|Different<br>|Asian-White|3.2M|0|3.2M|0|6.5M|0|
|ethnicity|Black-White|3.2M|0|3.2M|0|6.5M|0|





<!-- Start of picture text -->
SAME ETHNICITY DIFFERENT ETHNICITY<br>§ ifoa = / >. F ’ ‘ y ~3)rid a \ st i =<br>Z |yf" ./| =* hes | PS% | H tSo<4 eeSaale<br>a4. Sey yall = le) = |e<br>= ee hee Lt ‘ “SB URS5 ms 253 4 keee e5<br>° de a L iN ~ iS i We » i S A tr 2<br>‘Same demographic group (top: positive pairs, bottom: negative pairs) 16.67% Cross-ethnicity pairs (all negative pairs) 33.33%<br>% - ae 3 ge] mr ££<br>é a! SasaPRA: 7!j 3 ks) es = 1) es=a:* ; b <j<br>:| wr ; Sa om | Fon a q .<br>2| eae Mee \s & als a~ ml ee) > le’) ay<br>ry - S I\ow S | = j ws gs<br>[|= - Pe ee A ai. «|Z A [in AX<br>Cross-gender pairs (all negative pairs) 16.67% Cross-demographic pairs (all negative pairs) 33.33%<br><!-- End of picture text -->

Fig. 1: The different types of evaluation pairs that can be obtained from DemogPairs. Four types of pairs are represented: (top left) Pairs belonging to the same demographic group; (top right) Cross-ethnicity pairs, i.e. pairs from different ethnicities but shared gender; (bottom left) Cross-gender pairs, i.e. pairs of different gender but same ethnicity; (bottom right) Crossdemographic pairs, i.e. female-male pairs of different ethnicity. In bold, the percentage of each type out of the total number of dataset pairs. 

- **Experiment 1: All pairs.** Our first experiment follows the traditional approach in deep face recognition: ROC curves are built using all evaluation pairs in the dataset. One ROC curve is computed for each model over DemogPairs, and also over LFW for the sake of comparison. 

- **Experiment 2: Same demographic fold pairs.** In the second experiment, each demographic fold is evaluated separately. For each studied model, 6 ROC curves are computed, one per demographic group: Asian females, Asian males, Black females, Black males, White females and White males. This scenario involves pairs from the same demographic group exclusively, and thus is the most challenging (top left quadrant in Figure 1, c.f. Section IV-A). 

- **Experiment 3: Cross-demographic distractors.** Conversely, the third experiment tackles the easiest scenario, as it considers distractors of different gender and race. Again, 6 ROC curves are computed by using positive pairs from each demographic fold and all their cor- 

responding cross-demographic negative pairs (bottom right quadrant in Figure 1). For instance, the ROC curve for Asian females is computed using White and Black male distractors. 

### V. RESULTS 

Figure 2 shows the results of experiment 1. ROC curves reveal the overall challenging nature of DemogPairs. All models yield much lower TAR with DemogPairs than with LFW. For example, SphereFace’s TAR falls from 0.94 to 0.64 at a False Acceptance Rate (FAR) of 10<sup>_−_4</sup> . More dramatically, FaceNet (MS-Celeb-1M version) drops from 0.85 to 0.33 at the same FAR. Even though the architectures of the studied models present very significant differences among them (e.g. type of layers or dataset used for training), this first experiment shows that they all seem to suffer from a very damaging demographic bias. 

Results from experiment 2 (Figure 3) provide further insights about the demographic behavior of the models. The ROC curves corresponding to different demographic folds 



<!-- Start of picture text -->
\ Experiment 1: All pairs - LFW vs DemogPairs<br>nestee<br>09 A gett<br>a wen“Ueyt<br>08 Let 7oe<br>-707 oe<br>07 ote “,<br>& loreotle . wetes<br>Cosy Ve5t erttee<br>é Pat ‘ .<br>$05 ae pete<br>g a ot °<br>Boake oe<br>g mee, = = = DenogPais-SphereFoce(OWF)<br>Fos eet /= = = DemogPairs<br>Leet |= = =DemnogPairs- FaceNet (CWF)<br>2b ue |= = =DomogPairs-- FaceNet ResNet50 (MS-Celeb-1M)(VGGFace2)<br>oe I LFW SphereFace (CWF)<br>on eet |——=-——— LewLrw-LFW - ResNets0 FaceNetFaceNet (MS-Celeb-1M)(CWF) (veGFace2)<br>°<br>10% 10° 107 10" 10°<br>False Accept Rate (FAR)<br><!-- End of picture text -->

Fig. 2: Results from experiment 1. All pairs are used to compute two ROC curves for each model: one over LFW (continuous lines) and the other one over DemogPairs (dashed lines). The dataset used to train each model appears in parentheses. 

show very large differences. All models appear to suffer from almost identical demographic biases, always benefiting White males and especially harming Asian females. For instance, SphereFace has a TAR of 0.87 for White males which drops to 0.28 for Asian females, at a FAR of 10<sup>_−_4</sup> . Thus, this second experiment quantitatively demonstrates that the demographic generalization capability of studied models is limited. 

ROC curves resulting from our third experiment are shown in Figure 4. As expected, using cross-demographic distractors substantially rises their shapes with regard to experiment 2. More importantly, differences between demographic groups are greatly reduced and curves even virtually overlap for some models (e.g. FaceNet and ResNet50). We could argue that in this case the face verification problem has been simplified to some extent to a gender/ethnicity attributes classification problem. 

However obvious the latter conclusion may seem, it must be taken into account that the current trend in face recognition is to follow the same approach as in our first experiment: all the negative pairs, or a random subset of them, are used to compute ROC curves. It is therefore common that the two compared individuals in negative pairs have different gender or race, while the positive pairs have the same demographic characteristics. Thus, this traditional approach is in fact similar to our third experiment scenario and leads to overoptimistic results. Interestingly, the ROC curves resulting from the third experiment are indeed close to those obtained validating with LFW in experiment 1. In order to appropriately validate face recognition models, there is a need to pay attention to demographic factors and reconsider the way ROC curves and associated validation pairs are built. 

### VI. CONCLUSIONS AND FUTURE WORK 

Current deep face recognition models are highly accurate on standard validation datasets. Nevertheless, we have shown that existing datasets (both for training and validation) are remarkably biased. This implies that any model trained or validated on them will inexorably show similarly biased patterns. In this work, we have quantitatively demonstrated that public state-of-the-art face recognition models (FaceNet, SphereFace and VGGFace2) indeed suffer from very structured and damaging demographic biases. 

We have also contributed to the advancement of universal facial recognition by introducing DemogPairs, a new validation set composed of 10.8K images (58.3M identity verification pairs), balanced on the basis of gender, ethnicity and identity. To our knowledge, this is the first demographicallybalanced benchmark conceived for deep face recognition to date, and a valuable tool to appropriately analyze the crossdemographic behavior of any trained model. The benchmark of experiments described in this paper provides a novel demographic-aware testing protocol to evaluate human face recognition. 

Deep face recognition technology is increasingly being used in high-stakes sectors such as law enforcement, video surveillance and health care, and the objective must be to build universal, human-centered and inclusive face recognition systems. As stated by the Algorithmic Justice League [3] and demonstrated in this work, the demographic gap in facial analysis is still far from being resolved and properly tackled by academia and industry. As a future work, we will investigate novel deep-learning strategies to mitigate demographic imbalance and to help bridge this gap. 

### VII. ACKNOWLEDGMENTS 

The authors would like to thank Daniel Espejo and Angel<sup>´</sup> De Paz for their valuable help at annotating public facial datasets. We also thank Christina Zitello for her useful English review. 

### REFERENCES 

- [1] A. Bansal, C. D. Castillo, R. Ranjan, and R. Chellappa. The do’s and don’ts for CNN-based face verification. In _ICCV Workshops_ , pages 2545–2554, 2017. 

- [2] M. Buda, A. Maki, and M. A. Mazurowski. A systematic study of the class imbalance problem in convolutional neural networks. _Neural Networks_ , 106:249–259, 2018. 

- [3] J. Buolamwini and T. Gebru. Gender shades: Intersectional accuracy disparities in commercial gender classification. In _Conference on Fairness, Accountability and Transparency_ , pages 77–91, 2018. 

- [4] Q. Cao, L. Shen, W. Xie, O. M. Parkhi, and A. Zisserman. VGGFace2: A dataset for recognising faces across pose and age. In _13th IEEE International Conference on Automatic Face & Gesture Recognition (FG 2018)_ , pages 67–74, 2018. 

- [5] Q. Cao, L. Shen, W. Xie, O. M. Parkhi, and A. Zisserman. VGGFace2 Caffe model. https://www.robots.ox.ac.uk/˜vgg/data/ vgg_face2/, 2018. [Online; accessed 15-September-2018]. 

- [6] J. Deng, Y. Zhou, and S. Zafeiriou. Marginal loss for deep face recognition. In _IEEE International Conference on Computer Vision and Pattern Recognition (CVPRW), Faces in-the-wild Workshop/Challenge_ , volume 4, 2017. 

- [7] C. Ding and D. Tao. Robust face recognition via multimodal deep face representation. _IEEE Transactions on Multimedia_ , 17(11):2049–2058, 2015. 



<!-- Start of picture text -->
Experiment 2: Same demographic fold pairs.<br>; SpheroFace (CHF) . ResNetso (VaGFace2)<br>09 — 7 ost il<br>&; os wo “ ét ost aerae “<br>Sos et = srr Zost a = saree<br>o2pe-” en ot oe T= dont eee<br>= Sectnaee io al et<br>° . ° |<br>Fale cop Ra (FAR) Fale Accopt Rata (FAR)<br>, FaceNet (HF) . FoceNet(MS-Ceab-1)<br>os G 09) ti<br>Zor £5 gor A fe<br>S06 ‘ 1 08F oo ”<br>dos és os} ft<br>Sos ie Soste* Sy Ae [== Asan rae<br>wees = etn on een = = trone<br>o re a ee Osre a a<br>Fale cop Rae (FAR) Fale cept Rate (FAR)<br><!-- End of picture text -->

Fig. 3: Results from experiment 2. ROC curves are computed from each demographic fold of DemogPairs, separately. Ethnical and gender biases follow similar patterns across publicly available models, in spite of having different architectures and training databases (in parentheses). 



<!-- Start of picture text -->
Experiment 3: Cross-demographic distractors<br>. SpnereFace CHF) , ResNets0 VoGFece2)<br>os —— os<br>os E> 08 oa -<br>Fore Zor<br>Boe Ee<br>} ;<br>gos Sou<br>2asl naman]== Zos Nemnnawe<br>oat al=al mahaeymy oo -aoe)=—== Sestmaae<br>Osa Fale ccopta Rate FAR)a ee [) RpereveerorRS SUTOOTFalse BEVINAccept Rate Eine (FAR)er maversowehrs |2<br>. FaceNet(CWF) , FacoNet (s-Coeb-1)<br>as) EE os ze<br>os) Ca os Ca<br>go fg gor<br>Sosty re i.<br>Boal =n] Sal ener<br>osA : =e os° == ve<br>we oo<br>Fale Accept Rat (FAR) Fale cop Ra (FAR)<br><!-- End of picture text -->

Fig. 4: Results from experiment 3. ROC curves are computed using positive pairs from each demographic fold and all their corresponding cross-demographic negative pairs. Overall performance rises and differences between demographic groups are highly reduced. 

- [8] T. B. Fitzpatrick. The validity and practicality of sun-reactive skin types I through VI. _Archives of Dermatology_ , 124(6):869–871, 1988. 

- [9] S. Fu, H. He, and Z.-G. Hou. Learning race from face: A survey. _IEEE Transactions on Pattern Analysis and Machine Intelligence_ , 36(12):2483–2509, 2014. 

- [10] Y. Guo and L. Zhang. One-shot face recognition by promoting underrepresented classes. _arXiv preprint arXiv:1707.05574_ , 2017. 

- [11] Y. Guo, L. Zhang, Y. Hu, X. He, and J. Gao. MS-Celeb-1M: A dataset and benchmark for large-scale face recognition. In _European Conference on Computer Vision_ , pages 87–102. Springer, 2016. 

   - [34] X. Zhang, Z. Fang, Y. Wen, Z. Li, and Y. Qiao. Range loss for deep face recognition with long-tailed training data. In _IEEE Conference on Computer Vision and Pattern Recognition_ , pages 5409–5418, 2017. 

   - [35] Y. Zhang and Z.-H. Zhou. Cost-sensitive face recognition. _IEEE Transactions on Pattern Analysis and Machine Intelligence_ , 32(10):1758– 1769, 2010. 

   - [36] T. Zheng, W. Deng, and J. Hu. Cross-age LFW: A database for studying cross-age face recognition in unconstrained environments. _arXiv preprint arXiv:1708.08197_ , 2017. 

- [12] K. He, X. Zhang, S. Ren, and J. Sun. Deep residual learning for image recognition. In _IEEE Conference on Computer Vision and Pattern Recognition_ , pages 770–778, 2016. 

- [13] C. Huang, Y. Li, C. Change Loy, and X. Tang. Learning deep representation for imbalanced classification. In _IEEE Conference on Computer Vision and Pattern Recognition_ , pages 5375–5384, 2016. 

- [14] G. B. Huang, M. Ramesh, T. Berg, and E. Learned-Miller. Labeled Faces in the Wild: A database for studying face recognition in unconstrained environments. Technical Report 07-49, University of Massachusetts, Amherst, 2007. 

- [15] I. Kemelmacher-Shlizerman, S. M. Seitz, D. Miller, and E. Brossard. The MegaFace benchmark: 1 million faces for recognition at scale. In _IEEE Conference on Computer Vision and Pattern Recognition_ , pages 4873–4882, 2016. 

- [16] B. F. Klare, B. Klein, E. Taborsky, A. Blanton, J. Cheney, K. Allen, P. Grother, A. Mah, and A. K. Jain. Pushing the frontiers of unconstrained face detection and recognition: IARPA Janus Benchmark A. In _IEEE Conference on Computer Vision and Pattern Recognition_ , pages 1931–1939, 2015. 

- [17] B. Leng, K. Yu, and Q. Jingyan. Data augmentation for unbalanced face recognition training sets. _Neurocomputing_ , 235:10–14, 2017. 

- [18] D. T. Levin and B. L. Angelone. Categorical perception of race. _Perception_ , 31(5):567–578, 2002. 

- [19] W. Liu, Y. Wen, Z. Yu, M. Li, B. Raj, and L. Song. Sphereface: Deep hypersphere embedding for face recognition. In _IEEE Conference on Computer Vision and Pattern Recognition (CVPR)_ , volume 1, page 1, 2017. 

- [20] Y.-H. Liu and Y.-T. Chen. Face recognition using total margin-based adaptive fuzzy support vector machines. _IEEE Transactions on Neural Networks_ , 18(1):178–192, 2007. 

- [21] O. M. Parkhi, A. Vedaldi, A. Zisserman, et al. Deep face recognition. In _British Machine Vision Conference_ , volume 1, page 6, 2015. 

- [22] P. J. Phillips, F. Jiang, A. Narvekar, J. Ayyad, and A. J. O’Toole. An other-race effect for face recognition algorithms. _ACM Transactions on Applied Perception_ , 8(2):14, 2011. 

- [23] C. Reale, N. M. Nasrabadi, and R. Chellappa. An analysis of the robustness of deep face recognition networks to noisy training labels. In _IEEE Global Conference on Signal and Information Processing_ , pages 1192–1196, 2016. 

- [24] D. Sandberg. FaceNet for Tensorflow. https://github. com/davidsandberg/facenet, 2018. [Online; accessed 15September-2018]. 

- [25] F. Schroff, D. Kalenichenko, and J. Philbin. Facenet: A unified embedding for face recognition and clustering. In _IEEE Conference on Computer Vision and Pattern Recognition_ , pages 815–823, 2015. 

- [26] Y. Taigman, M. Yang, M. Ranzato, and L. Wolf. Deepface: Closing the gap to human-level performance in face verification. In _IEEE Conference on Computer Vision and Pattern Recognition_ , pages 1701– 1708, 2014. 

- [27] A. J. Viera, J. M. Garrett, et al. Understanding interobserver agreement: The kappa statistic. _Fam Med_ , 37(5):360–363, 2005. 

- [28] F. Wang, L. Chen, C. Li, S. Huang, Y. Chen, C. Qian, and C. Change Loy. The devil of face recognition is in the noise. In _European Conference on Computer Vision (ECCV)_ , September 2018. 

- [29] L. Weiyang, W. Yandong, Y. Zhiding, L. Ming, R. Bhiksha, and S. Le. SphereFace Caffe model. https://github.com/wy1iu/ sphereface, 2018. [Online; accessed 15-September-2018]. 

- [30] D. B. Wright and B. Sladden. An own gender bias and the importance of hair in face recognition. _Acta Psychologica_ , 114(1):101–114, 2003. 

- [31] D. Yi, Z. Lei, S. Liao, and S. Z. Li. Learning face representation from scratch. _arXiv preprint arXiv:1411.7923_ , 2014. 

- [32] X. Yin, X. Yu, K. Sohn, X. Liu, and M. Chandraker. Feature transfer learning for deep face recognition with long-tail data. _arXiv preprint arXiv:1803.09014_ , 2018. 

- [33] S. G. Young, K. Hugenberg, M. J. Bernstein, and D. F. Sacco. Perception and motivation in face recognition: A critical review of theories of the cross-race effect. _Personality and Social Psychology Review_ , 16(2):116–142, 2012. 

View publication stats 

