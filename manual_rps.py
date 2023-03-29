import random

def get_computer_choice():
    list_1 = ["Rock", "Paper", "Scissors"]
    return(random.choice(list_1))

def get_user_choice():
    user = input("What is your choice?")
    return user

def get_winner():
    computer= get_computer_choice()
    player= get_user_choice()
    if computer == "Rock" and player == "Rock":
        print("It is a tie!")
    if computer == "Paper"and player == "Paper":
        print("It is a tie!")
    if computer == "Scissors" and player == "Scissors":
        print("It is a tie!")
    elif computer == "Rock" and player == "Paper":
        print("You won!")
    elif computer == "Rock" and player == "Scissors":
        print("You lost")
    elif computer == "Paper" and player == "Scissors":
        print("You won!")
    elif computer == "Paper" and player == "Rock":
        print("You lost")
    elif computer == "Scissors" and player == "Rock":
        print("You won!")
    elif computer == "Scissors" and player == "Paper":
        print("You lost")
    else:
        print("It is not valid")
get_winner()  
