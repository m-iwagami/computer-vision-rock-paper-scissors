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
    if computer == player:
        print("It is a tie!")
    elif player == "Paper":
        if computer == "Rock":
            print("You won!")
        else:
            print("You lost")
    elif player == "Scissors":
        if computer == "Paper":
            print("You won!")
        else:
            print("You lost")
    elif player == "Rock":
        if computer == "Scissors":
            print("You won!")
        else: 
            print("You lost")
    else:
        print("It is not valid")
get_winner()  
