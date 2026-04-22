import random

choices = ["rock", "paper", "scissors"]

user = input("Enter rock, paper, or scissors (or 'quit' to stop): "). lower ()
if user not in choices:
    print ("Invalid Choice, Try again.")
    continue

computer = random.choice(choices)

print("Computer chose:", computer)

if user == computer:
    print("It's a tie!")
elif (user == "rock" and computer == "scissors"): or\ 
     (user == "paper" and computer == "rock"): or \  
     (user == "scissors" and computer == "paper"): or \
     print("You win!")
else:
    print("You lose!")
    