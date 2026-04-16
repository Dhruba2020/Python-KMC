# Food = ("Pizza")
# Fruit = ("Avocado")
# Pet = ("Rabbit")
# print ((Food) + " " + (Fruit)+ " " + (Pet))


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

# print (list1)
#print(list1[-7])
# isinstance
#print(type(list1))

#print(len(list1))  # to find the length of list



# print(isinstance(list5[len(list5) - 1], float))
# print(isinstance(list5[-1], float))

# #Slicing
# a= [1,2,3,4,5,6,7,8,9]

# print (a [0:4])
# print (a [3:6])
# print (a [1:2])



#LIST METHODS

#1. Append- Append adds data at the last but only one data can be added at a time
list5.append ("Hello")

# print (list5)

# data =[]
# data.append (1)
# print (data)


# #2. Insert
# dataz = ["apple", 54, 71.3, False, "Orange", True, 21, 13.8]
# dataz.insert (20000, "iphone")
# print (dataz)


#3. Extend

a=[1,2,3,4,5,6,7]
b=[8,9]

a.extend(b)
b. extend (a)


# print (a)
# print (b)


#4. Concatenate

a= [1,2,3,4,5,6,7]
b= [8,9]
c = a + b
print (c)
print (a, b)

dataz = ["apple", 54, 71.3, False, "Orange", True, 21, 13.8]
dataz [0]="updated"

print (dataz)


#APPEND, INSERT, EXTEND, CONCATENATE

ap = ["Mango", 23, 71.3, True, "Orange", False, 21, 30]

ap .append ("Peach")
ap .append ("Pears")

print (ap)

dataA = ["apple", 54, 71.3, False, "Orange", True, 21, 13.8]
dataA .insert ("Camera")
print (dataA)

x= (2,4,6,8)
y=(3,5,7,9)
x.extend (y)
y.extend (x)

print (x)
print (y)

x= (2,4,6,8)
y=(3,5,7,9)
Z = x + y

print (z)

