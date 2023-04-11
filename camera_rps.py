import cv2 #Note: the module import name for opencv-python
from keras.models import load_model #Note: keras model is to make prediction
import numpy as np   
import time
import random

"""
Rock-Paper-Scissors is a game in which each player simultaneously 
shows one of three hand signals representing rock, paper, or scissors.
Rock beats scissors. Scissors beats paper. 
Paper beats rock. The player who shows the first option that beats 
the other player's option wins. This is an implementation of an interactive 
Rock-Paper-Scissors game, in which the user can play with the computer using the camera.

Methods
- timer: To count 3 seconds before the game starts
- get_camera_image: To get picture of the user's choice
- get_prediction: To get prediction using get_camera_image
- get_user_choice: To finalize a user's gesture and print it
- get_computer_choice: To get a computer choice from move_list
- count_scores: count scores and print the result of the game
- get_winner: to compare choices, to get a result, and to add a point

Function 
- play() : Count rounds and play the game 
"""

class Game:
    def __init__(self):
        
        self.model = load_model('keras_model.h5')  #Note: Save the model to make prediction
        self.cap = cv2.VideoCapture(0)    #Note: To capture an image
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32) #Note: An array object represents a multidimensional, homogeneous array of fixed-size items.

        self.user_choice = self.get_prediction()
        self.computer_choice = None
        
        self.user = "user"
        self.computer = "computer"
        self.winner = None   
    
        self.computer_score = 0
        self.user_score = 0

        self.move_list = ["Rock", "Paper", "Scissors"]
        self.decoder = ["Rock", "Paper", "Scissors", "Nothing"]

    def timer(self):
         self.start_time = time.time()
         print("")
         print("Get ready...")
         while time.time() - self.start_time < 3:
             print(3 - int(time.time() - self.start_time))
             cv2.waitKey(1000) #Note: wait for 1 sec
         print("Go!")

    
    def get_camera_image(self):
        end_time = time.time() +1
        while time.time() < end_time: 
            ret, frame = self.cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):   #Note: Press q to close the window
                break
        return normalized_image

    def get_prediction(self):
        self.data[0] = self.get_camera_image()
        prediction = self.model.predict(self.data)
        return prediction
    
    def get_user_choice(self): 
        result = np.argmax(self.get_prediction()) 
        user_choice = self.decoder[result]
        print(f"The camera predicted {self.user_choice} as your choice.")
        return user_choice

    def get_computer_choice(self):
        computer_choice = (random.choice(self.move_list))
        return computer_choice

    def count_scores(self):
        winner = self.get_winner(self.computer_choice, self.user_choice, self.winner)
        if winner == "user":
            self.user_score += 1
            if self.user_score == 3:
                print("Congratulations! You won this game!")
        if winner == "computer":
            self.computer_score += 1
            if self.computer_score == 3:
                print("Game over. Sorry you lost this game.")

    def get_winner(self,computer_choice, user_choice,winner):
        user_choice = self.get_user_choice()
        print(f"Your choise is {user_choice}.")
        computer_choice = self.get_computer_choice()
        print(f"Computer's choice is {computer_choice}.")
        if computer_choice == user_choice:
            print(f"It is a tie! The other player chose {computer_choice} too!")
        elif user_choice == "Paper":
            if computer_choice == "Rock":
                print(f"You won! The other player chose {computer_choice}")
                winner = self.user
            else:
                print(f"Sorry, you lost. The other player chose {computer_choice}")
                winner = self.computer
        elif user_choice== "Scissors":
            if computer_choice == "Paper":
                print(f"You won! The other player chose {computer_choice}")
                winner = self.user
            else:
                print(f"Sorry, you lost. The other player chose {computer_choice}")
                winner = self.computer
        elif user_choice == "Rock":
            if computer_choice == "Scissors":
                print(f"You won! The other player chose {computer_choice}")
                winner = self.user
            else: 
                print(f"Sorry, you lost. The other player chose {computer_choice}")
                winner = self.computer
        else:
            print("Sorry, your input was invalid")
        return winner



def play():
    round_number = 1
    game = Game()
    while round_number <= 10:
        game.get_camera_image()
        print(f" This is Round {round_number}")
        cv2.waitKey(2000)
        game.timer()
        game.count_scores()
        cv2.waitKey(2000)
        print(f"Your score is {game.user_score}, computer's score is {game.computer_score} !")
        round_number += 1
        if game.user_score >= 3 or game.computer_score >= 3:
            break
    game.cap.release()
    game.cv2.destroyAllWindows()


if __name__ == '__main__':
    play()

