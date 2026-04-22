def find_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

nums = [1, 2, 3, 4, 5]
print("Sum:", find_sum(nums))

numbers = (1, 2, 3, 4, 5, 6)

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)


num = 5
i = 1

while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1

def find_max(t):
    max_num = t[0]
    for num in t:
        if num > max_num:
            max_num = num
    return max_num

data = (10, 25, 7, 45, 30)
print("Max:", find_max(data))

t = (1, 2, 3, 4, 5)
reversed_list = []

for i in range(len(t)-1, -1, -1):
    reversed_list.append(t[i])

print("Reversed:", tuple(reversed_list))

def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
    else:
        return "Invalid operation"

print(calculator(10, 5, "+"))
print(calculator(10, 5, "*"))


for i in range(1, 21):
    if i % 3 == 0:
        print(i)

num = 5
fact = 1
i = 1

while i <= num:
    fact *= i
    i += 1

print("Factorial:", fact)

