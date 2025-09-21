#Reid Sanders
#Rock Paper Scissors Game
#09/21/2025

import random


#Get the user input
def get_user_choice():
    user_input - input("Enter rock, paper or scissors: ").lower()
    while user_input not in ["rock", "paper", "scissors"]:
        user_input = input("Please enter a valid choice (rock, paper, or scissors): ").lower()
    return user_input

#Get the random computer choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

#determine the winner
def who_wins():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")
