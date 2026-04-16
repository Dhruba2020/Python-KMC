#Input  Function
a=100
b=55
a = input()

print ("The 1st value .....")
print ("The 2nd value....")

print ("a+b")
print ("a*b")
print ("The value of a is", a)


print (type(a))


a=int(123)

print ("Before type casting", type (a))

b=int(a)

print ("After type casting", type (b))




print(int(a)+int(b))
print (isinstance (a, str))

data1=input ("Enter a word")

print (data1)



if (1==1 and 5>=3):
    print ("This is true condition")
    a=10
if ("test"!="hello"):
    print ("This is str compare")

elif 1==1:
    print ("This is str compare")
else:
    print ("This is else condition")

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
