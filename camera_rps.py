import cv2 #the module import name for opencv-python
from keras.models import load_model #keras model is to make prediction
import numpy as np  # library 
import time
import random

class Game:
"""
Rock-Paper-Scissors is a game in which each player simultaneously 
shows one of three hand signals representing rock, paper, or scissors.
Rock beats scissors. Scissors beats paper. 
Paper beats rock. The player who shows the first option that beats 
the other player's option wins. This is an implementation of an interactive 
Rock-Paper-Scissors game, in which the user can play with the computer using the camera.


Attributes
__________


Methods
__________
- timer
- get_camera_image
- get_prediction
- user_choice
- get_computer_choice
- scores
- get_winner

Function
__________
- round

"""


def __init__(self):
    #Save the model to make prediction
    self.model = load_model('keras_model.h5')
    #To capture an image
    self.cap = cv2.VideoCapture(0)
    #An array object represents a multidimensional, homogeneous array of fixed-size items.
    self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    #user & computer choices
    self.user_choice = self.get_prediction()
    self.computer_choice = self.get_computer_choice
    
    #to count scores until one of the players gets 3 points
    self.scores = scores

    # After the loop release the cap object
    self.cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

#To set a 3 seconds countdown timer
def timer(self):
    self.start_time = time.time()
    print("Get ready...")
    while time.time() - self.start_time < 3:
        print(3 - int(time.time() - self.start_time))
    print("Show your hand")


#To get picture of the user's choice
def get_camera_image(self):
    while True: 
        ret, frame = self.cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        cv2.imshow('frame', frame)
        # Press q to close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    return normalized_image

def get_prediction(self):
    self.data[0] = self.get_camera_image()
    prediction = self.model.predict(self.data)
    return prediction


#To print user's gesture
def user_choice(self): 
    result = np.argmax(get_prediction)() 
    if result == [0]:
        self.user_choice = "Rock"
    elif result == [1]:
        self.user_choice = "Paper"
    elif result == [2]:
        self.user_choice = "Scissors"
    else:
        self.user_choice = "Nothing"
    print(f"The camera predicted {self.user_choice} as your choice.")
    return self.user_choice

#Computer to choose their choice
def get_computer_choice(self, computer_choice):
    computer_choice = (random.choice(list_1))
    list_1 = ["Rock", "Paper", "Scissors"]
    return computer_choice

#To keep scores
def scores(self, user_scores=0, computer_scores=0):
    if self.winner == self.user:
        self.user_score += 1
        if self.user_score == 3:
            print("Congratulations! You won this game!")
    if self.winner == self.computer:
        self.computer_score += 1
        if self.computer_score == 3:
            print("Game over. Sorry you lost this game.")


#To compare choices and get a result and add a point
def get_winner(self,computer_choice, user_choice,winner):
    user_choice = self.user_choice
    computer_choice = self.computer_choice
    if computer_choice == user_choice:
        print(f"It is a tie! The other player chose{computer_choice} too!")
    elif user_choice == "Paper":
        if computer_choice == "Rock":
            print(f"You won! The other player chose{computer_choice}")
            winner = self.user
        else:
            print(f"Sorry, you lost. The other player chose{computer_choice}")
            winner = self.computer

    elif user_choice== "Scissors":
        if computer_choice == "Paper":
            print(f"You won! The other player chose{computer_choice}")
            winner = self.user
        else:
            print(f"Sorry, you lost. The other player chose{computer_choice}")
            winner = self.computer
    elif user_choice == "Rock":
        if computer_choice == "Scissors":
            print(f"You won! The other player chose{computer_choice}")
            winner = self.user
        else: 
            print(f"Sorry, you lost. The other player chose{computer_choice}")
            winner = self.computer
    else:
        print("Sorry, your input was invalid")




def play():
    game = Game()
    game.timer
    while game.user_scores <= 3 or game.computer_scores <= 3:
        game.get_camera_image()
        game.get_prediction
        game.scores()
  # After the loop release the cap object
    game.cap.release()
  # Destroy all the windows
    game.cv2.destroyAllWindows()

if __name__ == '__main__':
  play()
