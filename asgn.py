import random

while True:
    random_num = random.randint(10, 20)

    attempts_left = 20
    player_score = 0
    computer_score = 0

    print("Game started! Guess the number between 10 and 20.")

    while attempts_left > 0:
        print("\nAttempts left:", attempts_left)
        print("Player Score:", player_score, "| Computer Score:", computer_score)

        user_num = int(input("Enter the number: "))

        if user_num == random_num:
            print("Correct number!")
            player_score += 5
        else:
            print("Wrong guess!")
            computer_score += 5

        attempts_left -= 1

    
        if player_score >= 100:
            print("\n You win the game!")
            break
        elif computer_score >= 100:
            print("\n Computer wins the game!")
            break

    else:
        # If all attempts finished
        print("\nGame Over! All attempts used.")
        print("Final Score -> Player:", player_score, "| Computer:", computer_score)

        if player_score > computer_score:
            print("You win!")
        elif computer_score > player_score:
            print("Computer wins!")
        else:
            print("It's a draw!")

    # Play again
    choice = input("\nDo you want to play again? (Y/N): ").lower()

    if choice != 'y':
        print("Thank you for playing!")
        break