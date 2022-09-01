
import random
user_choice=input('Enter choice (Rock, Paper, Scissors):')
possible_actions = ["Rock","Paper","Scissors"]
system_action = random.choice (possible_actions)
print(f"\nYou chose {user_choice}, computer chose {system_action}.\n")
if user_choice == system_action:
    print(f"Both players selected {user_choice}. It's a tie!")
elif user_choice == "rock":
    if system_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_choice == "paper":
    if system_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_choice == "scissors":
    if system_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")

import random

user_action = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
system_action = random.choice(possible_actions)
print(f"\nYou chose {user_choice}, computer chose {system_action}.\n")

if user_choice == system_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_choice == "rock":
    if system_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_choice == "paper":
    if system_action == "rock":
            print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_choice== "scissors":
    if system_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")


