import random

def get_computer_choice():
    list_1 = ["Rock", "Paper", "Scissors"]
    return(random.choice(list_1))

def get_user_choice():
    user = input("What is your choice?")
    return user

def get_winner(computer_choice, user_choice):
    computer_choice= get_computer_choice()
    user_choice= get_user_choice()
    if computer_choice == user_choice:
        print("It is a tie!")
    elif user_choice == "Paper":
        if computer_choice == "Rock":
            print("You won!")
        else:
            print("You lost")
    elif user_choice== "Scissors":
        if computer_choice == "Paper":
            print("You won!")
        else:
            print("You lost")
    elif user_choice == "Rock":
        if computer_choice == "Scissors":
            print("You won!")
        else: 
            print("You lost")
    else:
        print("It is not valid")
get_winner("Rock","Paper")  
