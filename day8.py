import random

guess_attempt = 5

random_num = random.randint(10,20)
print("this is random num", random_num)
count = 0
while True:
    user_num = input("Enter the number: ")
    count += 1
    if user_num == str(random_num):
        print(f"Number match in {count} times" )
        play = input("Do you want to play again? y/n ").lower()
        if play == "y":
            random_num = random.randint(10,20)
            count = 0
        else:
            print("Thank you playing")
            break
    else:
        print("Try again!! ")