import random

def get_computer_choice():
    list_1 = ["Rock", "Paper", "Scissors"]
    return(random.choice(list_1))
get_computer_choice()

def get_user_choice():
    user = input("What is your choice?")
    return user
get_user_choice()