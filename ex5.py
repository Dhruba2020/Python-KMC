questions = {
    "Capital of Nepal?": "Kathmandu",
    "2 + 2?": "4",
    "Color of sky?": "blue"
}

score = 0

for q in questions:
    answer = input(q + " ")

    if answer.lower() == questions[q]:
        print("Correct")
        score += 1
    else:
        print("Wrong")

print("Your score:", score)