import random
games_data = ["r", 'p', 's']
data = random.choice (games_data)
print (data)

while True:
    user_data = input ("Enter, r, p, s: ")
    if user_data not in games_data:
        print ("Invalid Choice")
        continue
    print ("Correct Input")
    if data == user_data:
        print ("Game Draw!")

   
