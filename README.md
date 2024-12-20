# (T&A-CV) CDD through Prompt2Guard on expanded dataset

## 1. Overview
This is the repository for the project on **deep fake images detection** of the course "Trends and Applications in Computer Vision".
Specifically, the **Continual Deepfake Detection(CDD)** problem which has become a prominent topic after the more and more rapid development of **generative models** in the image and video field. 

For this task, we explored various methods, focusing not only on accuracy but also on other relevant factors such as code availability and implementation costs, identifying the model and approach that best align with our needs. 
We choose to adopt [Prompt2Guard](https://github.com/laitifranz/Prompt2Guard), which achieves state of the art performances on the CDDB Hard benchmark with relatively limited amount of available data. 

## 2. Setup

Create the environment with the requirements.txt file.

Change the path of the dataset and the parameter num_workers in the cddb_inference.json/cddb_training.json file.

If you want to add classes in the training, you have to modify the zeroshot_classprediction.py file at line 91 (add the name of the class that must be in the same directory of the other) and then run it. Remeber that if you generate a new pickle file you have to change the path in the data_manager.py file at line 174 with your new file.

If you want to use a wandb account you have to modify the data in the file data_manager at line 72 (and line 306 for the name of the run).

If you want to try some new experiments, you have to change the configuration in the cddb_training.json. In particular we suggest you to change: the number of epochs, the order of the task (parameters: task_name and multiclass).

## 3. Examples and Experiments

## 4. Structure

## 5. References
