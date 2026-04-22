# Taking user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
address = input("Enter your address: ")

# Different ways of printing
print("My name is {} and my age is {} and my address is {}".format(name, age, address))

output = "My name is {} and age is {} and address is {}".format(name, age, address)
print(output)

output = f"My name is {name} and my age is {age} and my address is {address}"
print(output)

# Percentage grading
percentage = float(input("Enter your percentage: "))

if percentage > 100 or percentage < 0:
    print("Invalid Input")
elif 80 <= percentage <= 100:
    print("Distinction")
elif 60 <= percentage < 80:
    print("First Division")
elif 45 <= percentage < 60:
    print("Second Division")
elif 40 <= percentage < 45:
    print("Third Division")
else:
    print("Fail")

# Marks grading
marks = int(input("Enter your marks: "))

if marks >= 90:
    if marks == 90:
        print("Lucky A++")
    else:
        print("None")
elif marks >= 80:
    if marks == 80:
        print("Lucky A")
elif marks >= 70:
    print("C")
else:
    print("D")

# Gender check
gender = input("Enter gender (M/F): ")

if gender == "F":
    print("Female")
else:
    print("Male")

# Short (ternary) form
data = "Female" if gender == "F" else "Male"
print(data)