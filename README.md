# Computer Vision RPS
# Computer vision Project Documentation Guideline

## Description 
Rock-Paper-Scissors is a game in which each player simultaneously shows one of three hand signals representing rock, paper, or scissors. Rock beats scissors. Scissors beats paper. Paper beats rock. The player who shows the first option that beats the other player's option wins. This is an implementation of an interactive Rock-Paper-Scissors game, in which the user can play with the computer using the camera


## Learning objective
Creating of an image database for computer vision tasks using Teachable-Machine(https://teachablemachine.withgoogle.com/).
Setting up virtual environments and the installation of all required packages.
The practice of intermediate Python programming - (Object Oriented Programming, numpy, time, 'if-else' statement, 'while' loops).

## Project outline
### Milestone 1 & 2
- Used Teachable-Machine  to start creating the model.
- Downloaded the model from the "Tensorflow" tab in Teachable-Machine. The model is called keras_model.h5 and the text file containing the labels called labels.txt.

### Milestone 3 
- Before you can use the model, you need to install the libraries that it depends on.
- Create a conda environment and then install the necessary requirements. You need opencv-python, tensorflow, and ipykernel
Start by creating the environment, activate it, and then install pip by running the following command in your terminal conda install pip. Then, to install the rest of the libraries, run pip install 

### Milestone 4
- Added "play ()" function to play the game. 


## Libraries
import cv2
    The module import name for opencv-python
from keras.models import load_model 
    Keras model is to make prediction
import numpy as np
    To get a result from the prediction.
        'prediction from the    def get_user_choice(self):' 
        'result = np.argmax(self.get_prediction())'
import time
import random


## Conclusions

### What I learnt from this project
- How Object Oriented Progamming(OOP) works
- How to use Class
- How to use method
- How to use numpy 
- How to recall methods in a function
- Be familiar with CV2 

