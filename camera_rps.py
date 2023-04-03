import cv2
from keras.models import load_model
import numpy as np
import time
import random

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()



#To get prediction
def get_prediction():
    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        # Press q to close the window
        print(prediction)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

#To set a 3 seconds countdown timer
def timer():
    start_time = time.time()
    while time.time() - start_time < 3:
        print(3 - int(time.time() - start_time))

#To print user's gesture
def user_choice(): 
    result = np.argmax(prediction) 
    if result == [0]:
        user_choice = "Rock"
    elif result == [1]:
        user_choice = "Paper"
    elif result == [2]:
        user_choice = "Scissors"
    else:
        user_choice = "Nothing"
    print(f"you choose {user_choice}")

#Computer to choose their choice
def get_computer_choice():
    list_1 = ["Rock", "Paper", "Scissors"]
    return(random.choice(list_1))

#To keep scores
def scores():
    user_wins = 0
    computer_wins = 0
    if winner == user:
        user_score += 1
        if user_score == 3:
            print("Congratulations! You won this game!")
    if winner == computer:
        computer_score += 1
        if computer_score == 3:
            print("Game over. Sorry you lost this game.")

def check_rounds():
    rounds = 5
    while rounds >= 1:
        get_winner()
        rounds -= 1
    else:
        print("Game over! You played 5 rounds already.")


#To compare choices and get a result and add a point
def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        print(f"It is a tie! The other player chose{computer_choice} too!")
    elif user_choice == "Paper":
        if computer_choice == "Rock":
            print(f"You won! The other player chose{computer_choice}")
            winner = user
        else:
            print("Sorry, you lost. The other player chose{computer_choice}")
            winner = computer

    elif user_choice== "Scissors":
        if computer_choice == "Paper":
            print(f"You won! The other player chose{computer_choice}")
            winner = user
        else:
            print("Sorry, you lost. The other player chose{computer_choice}")
            winner = computer
    elif user_choice == "Rock":
        if computer_choice == "Scissors":
            print(f"You won! The other player chose{computer_choice}")
            winner = user
        else: 
            print("Sorry, you lost. The other player chose{computer_choice}")
            winner = computer
    else:
        print("Sorry, your input was invalid")




def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    get_winner(computer_choice, user_choice)
scores()
