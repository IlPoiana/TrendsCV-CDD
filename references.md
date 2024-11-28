# References for the project

- [1]**CIL paper github link:** https://github.com/Coral79/CDDB
- [2]**On the detection of synthetic images generated by diffusion models:** https://github.com/grip-unina/DMimageDetection
    DIFFUSION MODELS
    - *"Spec [9], based on **frequency analysis**, PatchForensics [18], that relies on **local patch analysis**, Wang2020 [15], a **ResNet50** with blurring and compression augmentation, and Grag2021 [16], same **backbone as before but avoiding down-sampling** in the first layer and intense augmentation."*
- [4]**Prompt2Guard**: https://github.com/laitifranz/Prompt2Guard

## Datasets

- **CDDB:** https://drive.google.com/file/d/1NgB8ytBMFBFwyXJQvdVT_yek1EaaEHrg/view?usp=sharing (No diffusion)
- **Diffusion generated synth images:** https://drive.google.com/file/d/1grvgKiIq0ny8ImQzSUXPk3nd-AMEDjNb/view?usp=share_link
  Synthetic images used as test
- **List of real images datasets used:** 
  - https://image-net.org/index.php
  - https://www.spiedigitallibrary.org/conference-proceedings-of-spie/5307/0000/UCID-an-uncompressed-color-image-database/10.1117/12.525375.short
  - https://cocodataset.org/#home

## Models

- **LRCIL:** https://github.com/lrzpellegrini/Latent-Replay
- **LUCIL, iCaRL, DyTox:** https://github.com/Coral79/CDDB/tree/main



## Overall structure
1. Presentation of the problem/solution
2. Explaination of the theory/model/architecture behind it
3. Limitations or something that is missing

### Example
1. **DeepFake detection:** The topic of today presentation is... which is ..... 
2. To adress this problem, the standard approach is a Feature extractor + MLP (CNNDet/ ConViT + MLP)
3. These models need lots of data to be fine tuned properly, and the Synth data generation landscape is changing rapidly, to adress this problems, these models result inadequate. **Low Accuracy, Data Mess, and Catastrophic forgetting**

## Presentation
 
1. **DeepFake detection:** 
   1.  
   2. Feature extractor(CNN, VaE) + MLP for classifying real vs fake
   3. The diffusion model case:
        - [2] **Detection, GAN vs Diffusion:** Overview, on the existing methods(2022) to detect fake images, BOTH GAN and Diffusion(NO CIL)
          - **"Generalization remains the main hurdle, and detectors trained only on GAN images work poorly on these new images."**
        - [5] **SeDID Method:** *"SeDID uniquely exploits the distinct properties of diffusion models, particularly focusing on the errors between reverse and denoise samples at specific timesteps during the generation process."*
        *"...Both branches calculate the Area Under the Receiver Operating Characteristic Curve (AUC), the Accuracy (ACC), and the True Positive Rate at a given False Positive Rate (TPR@FPR), and classify images with real or generated output..."*
          - **Statistical-SeDID Stat:**
            - *"The **SeDID Stat** branch involves statistical analysis, error calculation, and model evaluation."*
            - *"...If the error is smaller than a threshold h, we classify it to the synthetic sample."*
          - **Neural-SeDID NN:**
            - *"The SeDID NNs branch employs a ResNet-18 model, which computes prediction errors, and updates weights via backpropagation."*
2. **Avoiding Catastrophic forgetting - Reharsal for CIL:**
   1. **Pseudo:** [6]
   2. **Native:** [7]
   3. **Generative:** CNN-GAN [8]
3. **Prompt2Guard:** 
   - Multimodal, CLIP
   - Prompt Tuning/Learning
4. **Our ideas:**

## Papers Reference
[1] (CIL)*A Continual Deepfake Detection Benchmark: Dataset, Methods, and Essentials*

[2] (Diff)*On the detection of synthetic images generated by diffusion models*

[3] (FSL)*A Comprehensive Survey of Few-shot Learning: Evolution, Applications, Challenges, and Opportunities*

[4] (MultiModal+CIL+FSL)*Conditioned Prompt-Optimization for Continual Deepfake Detection* - 

[5] (Diff)*Exposing the Fake: Effective Diffusion-Generated Images Detection* -  Ruipeng Ma, Jinhao Duan, Fei Kong, Xiaoshuang Shi, Kaidi Xu 

[6] (CIL)*Catastrophic Forgetting, Rehearsal and Pseudorehearsal.* - Anthony Robins.

[7] (CIL)*Latent Replay for Real-Time Continual Learning* - Lorenzo Pellegrini, Gabriele Graffieti, Vincenzo Lomonaco, Davide Maltoni

[8] (CIL)*GAN-CNN Ensemble: A Robust Deepfake Detection Model of Social Media Images Using Minimized Catastrophic Forgetting and Generative Replay Technique* - Preeti Sharma, Manoj Kumar, Hitesh Kumar Sharma