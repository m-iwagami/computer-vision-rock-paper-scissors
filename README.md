# Computer Vision RPS
# Computer vision Project Documentation Guideline

## Description 
Rock-Paper-Scissors is a game in which each player simultaneously shows one of three hand signals representing rock, paper, or scissors. Rock beats scissors. Scissors beats paper. Paper beats rock. The player who shows the first option that beats the other player's option wins. This is an implementation of an interactive Rock-Paper-Scissors game, in which the user can play with the computer using the camera
## Modules
- camera_rps.py: Main 
- keras_model.h5: an image database imported from Teachable-Machine.
- labels.txt: 4 gestures that are detected by the process of cerating the image database.
- requirements.txt: this file enables any other user that wants to use your computer to easily install these exact dependencies by running pip install requirements.txt.

### Additional modules
- RPS-Template.py: original file from the aicore platform.
- manual_rps.py: used in Milestone 3 to practice python code. 

## Learning objective
- Creating of an image database for computer vision tasks using Teachable-Machine(https://teachablemachine.withgoogle.com/).
- Setting up virtual environments and the installation of all required packages.
- The practice of intermediate Python programming - (Object Oriented Programming, numpy, time, 'if-else' statement, 'while' loops).

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
- `cv2`: The module import name for opencv-python. 
- `from keras.models import load_model`: Keras model is to make prediction.
- `import numpy as np`: To get a result from the prediction in `get_user_choice(self)`.`result = np.argmax(self.get_prediction())`.
- `import time`: To countdown time before the game starts.
- `import random`: To choose a computer's choice. used in `get_computer_choice(self)`

## Requirement
- Before you can use the model, you need to install the libraries that it depends on.
Create a conda environment and then install the necessary requirements. You need opencv-python, tensorflow, and ipykernel
Start by creating the environment, activate it, and then `install pip`. Then, to install the rest of the libraries, run `pip install` to install each item (opencv-python, tensorflow, and ipykernel).

- After that, the libraries you have to install are the ones mentioned above.

- Important: If you are on Ubuntu, the latest version of Tensorflow doens't work with the default version of Python. When creating the virtual environment, use Python 3.8 instead by running:
conda create -n my_env python=3.8

## Conclusions

### What I learnt from this project
- How Object Oriented Progamming(OOP) works
- How to use Class
- How to use method
- How to use numpy 
- How to recall methods in a function
- Be familiar with CV2 

