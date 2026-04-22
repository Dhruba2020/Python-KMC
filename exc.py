ABC = 23
print(type(ABC))

a = None
ab = "Days"
bc = 2 + 2

print(type(a))
print(type(ab))
print(type(bc))

x = 55
y = 25
print(x + y)
print(x * y)
print(x - y)
print(y - x)
print(y / x)
print(x % y)
print(x**y)
print(y // x)

d = "Days"
w = "Weeks"
print(d + w)

S = 44
D = 23
print(S + D)
print(S * D)

print(2 == 2)
print(2 == "2")
print(5 != 3)
print(7 > 3)
print(2 < 5)
print(6 >= 6)
print(4 <= 6)
print(not ("logged_in"))
print(1 == 1 and "test" != "hello")

q = 2
r = 4
s = 6
t = 8
u = 10
print(q + r + s * t / u)
print("t=s")
print(q == r)
print(r < s)
print(t > r)
print("p<=s")
print(r >= s)
print(s != r)

name = "Alisha"
age = 25
pi = 3.14
is_active = True
number = None

name = input("Enter your name:")
age = int(input("Enter your age:"))

print("My name is {} and I am {} years old".format("Alisha", 25))

a = "22"
b = 55
a = input()

print("The 1st value .....")
print("The 2nd value....")
print("a+b")
print("a*b")
print("The value of a is", a)
print(type(a))

a = int(123)

print("Before type casting", type(a))

b = int(a)

print("After type casting", type(b))


print(int(a) + int(b))
print(isinstance(a, str))
data1 = input("Enter a word")

print(data1)


if 1 == 1 and 5 >= 3:
    print("This is true condition")
    a = 10
if "test" != "hello":
    print("This is str compare")

elif 1 == 1:
    print("This is str compare")
else:
    print("This is else condition")

percentage = float(input("Enter your percentage: "))

if percentage > 100 or percentage < 0:
    print("Invalid input")
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

Food = "Pizza"
Fruit = "Avocado"
Pet = "Rabbit"
print((Food) + " " + (Fruit) + " " + (Pet))


list1 = [
    1,
    2,
    3,
    4,
    5,
    5,
    6,
]  # index: 0,1,2,3,4,5,6   #-ve index: -7, -6, -5, -4, -3, -2, -1
list2 = ["Mango", "Banana", "Cherry", "Orange"]
list3 = [True, False, True, True, False, True]
list4 = [17.3, 71.3, 34.5, 87.0, 23.4]
list5 = ["apple", 54, 71.3, False, "Orange", True, 21, 13.8]

print(list1)
print(list1[-7])
isinstance
print(type(list1))

print(len(list1))  # to find the length of list


print(isinstance(list5[len(list5) - 1], float))
print(isinstance(list5[-1], float))

# Slicing
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a[0:4])
print(a[3:6])
print(a[1:2])


# LIST METHODS

# 1. Append- Append adds data at the last but only one data can be added at a time
list5.append("Hello")

print(list5)

data = []
data.append(1)
print(data)


# 2. Insert
dataz = ["apple", 54, 71.3, False, "Orange", True, 21, 13.8]
dataz.insert(20000, "iphone")
print(dataz)


# 3. Extend

a = [1, 2, 3, 4, 5, 6, 7]
b = [8, 9]

a.extend(b)
b.extend(a)


print(a)
print(b)


# 4. Concatenate

a = [1, 2, 3, 4, 5, 6, 7]
b = [8, 9]
c = a + b
print(c)
print(a, b)

dataz = ["apple", 54, 71.3, False, "Orange", True, 21, 13.8]
dataz[0] = "updated"

print(dataz)


# APPEND, INSERT, EXTEND, CONCATENATE

ap = ["Mango", 23, 71.3, True, "Orange", False, 21, 30]

ap.append("Peach")
ap.append("Pears")

print(ap)

dataA = ["apple", 54, 71.3, False, "Orange", True, 21, 13.8]
dataA.insert(20000, "Camera")
print(dataA)


x = (2, 4, 6, 8)
y = (3, 5, 7, 9)
Z = x + y
print(Z)


# DEL, REMOVE, POP, CLEAR
# Del: deletes index or value, Remove: Removes value, Pop: Removes index or last value, Clear: clears all list)

dataB = ["apple", 54, 71.3, False, "Orange", True, 21, 13.8]
# del
del dataB[0]
print(dataB)

# remove
dataC = ["apple", 54, 71.3, False, "Orange", True, 21, 13.8]
dataC.remove(71.3)
print(dataC)

# pop: it removes last value if specific value of index is not defined
dataD = ["apple", 54, 71.3, False, "Orange", True, 21, 13.8]
dataD.pop(0)
print(dataD)

# clear: This clears all the variables
dataE = ["apple", 54, 71.3, False, "Orange", True, 21, 13.8]
dataE.clear()
print(dataE)

# COUNT

teachers = ["Sangam", "Sagun", "Ramesh", "Ramit", "Sagun", "Sangam"]
count_teacher = teachers.count("Sangam")
print(count_teacher)

# REVERSE
teachers = ["Sangam", "Sagun", "Ramesh", "Ramit", "Sagun", "Sangam"]
teachers.reverse()
print(teachers)

# Sort
teachers = ["Sangam", "Sagun", "Ramesh", "Ramit", "Sagun", "Sangam"]
teachers.sort()
print(teachers)


a = "Kathmandu"
b = "Pokhara"
c = "Dharan"
d = "Dhankuta"
w = 5

Place = input("Enter the name of place:")
Birthplace = input("Enter the Birth Place:")
Ward = int(input("Enter Ward No:"))

print(
    "My birth place is {}, Ward No {} and I am living in {} now".format(
        "Dhankuta", 5, "Kathmandu"
    )
)
