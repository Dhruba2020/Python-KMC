import random

while True:   
    random_num = random.randint(10, 20)
   
    count = 0

    while True:   
        user_num = int(input("Enter the number: "))
        count += 1

        if user_num == random_num:
            print("Number matched!")
            print("You guessed it in", count, "attempt(s).")
            break
        else:
            print("Try again!!")

    choice = input("Do you want to play again? (Y/N): ").lower()

    if choice != 'y':
        print("Thank you for playing!")
        break
