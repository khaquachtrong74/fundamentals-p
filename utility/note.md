# Abstract
Convolutional networks, transformers, hybrid models, and Mamba-based architectures have demonstrated strong performance
across various medical image classification tasks. However, these methods were primarily designed to classify clean images
using labeled data. In contrast, real-world clinical data often involve image corruptions that are unique to multi-center studies and
stem from variations in imaging equipment across manufacturers. In this paper, we introduce the Medical Vision Transformer
(MedViTV2), a novel architecture incorporating Kolmogorov-Arnold Network (KAN) layers into the transformer architecture
for the first time, aiming for generalized medical image classification. We have developed an e fficient KAN block to reduce
computational load while enhancing the accuracy of the original MedViT. Additionally, to counteract the fragility of our MedViT
when scaled up, we propose an enhanced Dilated Neighborhood Attention (DiNA), an adaptation of the efficient fused dot-product
attention kernel capable of capturing global context and expanding receptive fields to scale the model effectively and addressing
feature collapse issues. Moreover, a hierarchical hybrid strategy is introduced to stack our Local Feature Perception and Global
Feature Perception blocks in an e fficient manner, which balances local and global feature perceptions to boost performance.
Extensive experiments on 17 medical image classification datasets and 12 corrupted medical image datasets demonstrate that
MedViTV2 achieved state-of-the-art results in 27 out of 29 experiments with reduced computational complexity. MedViTV2
is 44% more computationally e fficient than the previous version and significantly enhances accuracy, achieving improvements
of 4.6% on MedMNIST, 5.8% on NonMNIST, and 13.4% on the MedMNIST-C benchmark. Our code is available at https:
//github.com/Omid-Nejati/MedViTV2.git
Keywords: Medical image classification, Kolmogorov–Arnold Networks, Medical image corruption, Deep learning
1. Introduction
Computer-aided diagnosis (CAD) systems have attracted sig-
nificant research interest in medical image analysis, aiming to
assist clinicians in making diagnostic decisions. These systems
are applied to various modalities, including X-ray radiography
[1], computed tomography (CT) [2], magnetic resonance imag-
ing (MRI) [3], ultrasound [4], and digital pathology [5]. The
success of deep learning in this domain is partly attributed to the
increasing availability of large-scale datasets. Large datasets
with reliable labels are ideal for training deep neural networks.
However, collecting labeled medical images remains challeng-
ing due to data privacy concerns and the time-consuming nature
of expert annotations.
CAD systems continue to encounter challenges in the medi-
cal domain, particularly when dealing with artifacts [6, 7] and
corruptions [8]. These corruptions often arise from various fac-
tors, including post-processing techniques, acquisition proto-
cols, data handling, and differences in imaging equipment (e.g.,
vendor variations). Fortunately, several studies have sought to
simulate common corruptions across di fferent medical modal-
∗Corresponding author: omid nejaty@alumni.iust.ac.ir
0 5 10 15 20 25 30 35
FLOPs (G)
81
83
85
87
89
91Average Accuracy (%)
ResNet(28)
ResNet(224)
MedViTV1
MedViTV2
MedMamba
Figure 1: Comparison between MedViTs (V1 and V2), MedMamba, and the
baseline ResNets, in terms of Average Accuracy vs. FLOPs trade-o ff over all
MedMNIST datasets. MedViTV2-T /S/L significantly improves average accu-
racy by 2.6%, 2.5%, and 4.6%, respectively, compared to MedViTV1-T/S/L.
ities, including digital pathology [9], dermatology [10], blood
microscopy [11], and multimodal imaging [12]. While these
efforts are foundational, they underscore the need for a robust
deep neural network capable of maintaining high performance
across diverse medical imaging modalities under such challeng-
ing conditions.
Elsevier February 20, 2025
arXiv:2502.13693v1  [cs.CV]  19 Feb 2025
