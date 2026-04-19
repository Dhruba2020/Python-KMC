import random

choices = ["rock", "paper", "scissors"]

user = input("Enter rock, paper, or scissors: ")
computer = random.choice(choices)

print("Computer chose:", computer)

if user == computer:
    print("It's a tie!")
elif user == "rock" and computer == "scissors":
    print("You win!")
elif user == "paper" and computer == "rock":
    print("You win!")
elif user == "scissors" and computer == "paper":
    print("You win!")
else:
    print("You lose!")
    