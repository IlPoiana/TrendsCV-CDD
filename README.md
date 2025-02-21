# (T&A-CV) CDD through Prompt2Guard on expanded dataset

## 1. Overview
This is the repository for the project on **deep fake images detection** of the course "Trends and Applications in Computer Vision (2024/2025)".
Specifically, it studies a recent approach to the **Continual Deepfake Detection(CDD)** task which has become a prominent topic after the more and more rapid development of **generative models** in the image and video field. 

For this task, we firstly explored various methods, focusing not only on accuracy but also on other relevant factors such as code availability and implementation costs, identifying the model and approach that best align with our needs. 
We choose to adopt [Prompt2Guard](https://github.com/laitifranz/Prompt2Guard), which achieves state of the art performances on the CDDB Hard benchmark with relatively limited amount of training data, tipical for this category of problems.

We test this solution on synthetic images generated from Diffusion Models, a generative tool not tested in the P2G paper to see if it generalize well on these data.

## 2. Setup

1. **Environment:** Create a python3.9 or more environment with the requirements.txt file.
  
    `$ pip install -r requirements.txt`

2. **Dataset:** Download the [dataset](https://drive.google.com/file/d/1DyDZxpGHh1MkccXvbJtNJ2gyvjiIqKHe/view?usp=drive_link) (CDDBdataset) and extract it, you should see a structure like: 

    ```
    CDDBdataset/
    ┣ CDDB/
    ┃ ┣ biggan/
    ┃ ┃ ┣ train/
    ┃ ┃ ┃ ┣ 0_real/
    ┃ ┃ ┃ ┗ 1_fake/
    ┃ ┃ ┗ val/
    ┃ ┃   ┣ 0_real/
    ┃ ┃   ┗ 1_fake/
    ┃ ┣ crn/
    ┃ ┃ ┣ train/
    ┃ ┃ ┃ ┣ 0_real/
    ┃ ┃ ┃ ┗ 1_fake/
    ┃ ┃ ┗ val/
    ┃ ┃   ┣ 0_real/
    ┃ ┃   ┗ 1_fake/
    
    ...

    ┃ ┗ wild/
    ┃   ┣ train/
    ┃ ┃ ┃ ┣ 0_real/
    ┃ ┃ ┃ ┗ 1_fake/
    ┃   ┗ val/
    ┃ ┃   ┣ 0_real/
    ┃ ┃   ┗ 1_fake/
    ┗ Mix/
      ┣ biggan/
      ┃
      ┣ gaugan/
      ┃
      ┣ guided-diffusion_noise2image_LSUNbedrooms/
      ┃  
      ┣ guided-diffusion_noise2image_LSUNcats/
      ┃
      ┣ latent-diffusion_noise2image_FFHQ/
      ┃
      ┣ latent-diffusion_noise2image_LSUNbedrooms/
      ┃
      ┣ san/
      ┃
      ┣ whichfaceisreal/
      ┃
      ┗ wild/
        ┣ train/
        ┃   ┣ 0_real/
        ┃   ┗ 1_fake/
        ┗ val/
            ┣ 0_real/
            ┗ 1_fake/

    ```   

3. Change the path `data_path` of the dataset and the parameter `num_workers` in the `cddb_inference/cddb_training.json` file.
   
   ```
   {   
    "batch_size" : 2,
    "batch_size_eval" : 32,
    "epochs" : 2,
    ...,
    "task_name": ["biggan", "whichfaceisreal",  "san"],
    "data_path": "YOURPATH",
    ...,
    "num_workers" : 6
    }
    ```

## 3. Examples and Experiments
### 3.1 Reproduce results
Here there are the specifications used to recreate the results we obtained in our presentation.(the pickle file with the zero-shot predictions has been already included, see *classes_mix.pkl*)

- In `cddb_training.json`:
  - **CDDB + DM:** 
    - `task_name": ["guided-diffusion_noise2image_LSUNbedrooms",  "guided-diffusion_noise2image_LSUNcats", "latent-diffusion_noise2image_FFHQ", "san", "wild"]`
    - `"data_path": "YOURPATH/CDDBdataset/Mix/"`
  - **CDDB3:**
    - `"task_name": ["biggan", "whichfaceisreal",  "san"]`
    - `"data_path": "YOURPATH/CDDBdataset/Mix/"`
  - `"epochs" : 5`

- Run `python3 src/train.py` from the Prompt2Guard directory

### 3.2 Experiments
#### Adding Classes
If you want to add classes in the training, you have to modify the `zeroshot_classprediction.py` file at line 91 (add the name of the class that must be in the same directory of the other) and then run it.
After you have run it, a new pickle file will be generate, next you have to change the path in the `data_manager.py` file at line 174 with your new file.

#### Wandb
If you want to use a **wandb account** you have to modify the data in the file `data_manager.py` at line 72 and line 306 for the name of the run.
Then run the training or the inference with the `--wandb` flag (same as the original P2G)

#### Experiments
If you want to try different combination of hyperparameters, you have to change the configuration in the `cddb_training.json`.
For example, we suggest you to modify: the number of epochs, the order of the task (parameters: task_name and multiclass) or to create a new task made as an union of differents and compare the results .

## 4. References
1. The model we use: [Prompt2Guard](https://arxiv.org/pdf/2407.21554)
2. The dataset with images generate with diffusion models: [On the detection if synthetic images generatedby diffusion models](https://arxiv.org/pdf/2211.00680)
3. The CDDB dataset: [A Continual Deepfake Detection Benchmark: Dataset, Methods, and Essentials](https://arxiv.org/pdf/2205.05467)
