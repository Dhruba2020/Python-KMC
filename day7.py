# # FOR LOOP
"""
for i in [1,2,3,4,5,1]:
print (i)

"""

for i in [1, 2, 3, 4, 5, 1]:
    print(i)
    print("KMC")

for i in [12, 13, 14, 15, 16, 17, 18]:
    if i % 2 == 0:
        print(f"{i} even")
    else:
        print(f"{i} odd")

a = {"name": "Hari", "college": "KMC"}

for i in a:
    print(f"{i},={a[i]}")

for i in a.values():
    print (i)


  #RANGE to print even between 1 and 100

even = []
odd = []
for i in range (1,100,1):
    if i%2==0:
        even.append (i)
    else:
        odd.append(i)
print (even)
   

for i in [1,2,3,4,5,6,7,8,9,10]:
    print (i)
    if i == 5:
        break
    print (i)


a = [1,2,3,4, "hello", "test", 1,2,4,9.9, True]

for i in a:
    if isinstance(i, int):
        print(i)

#2nd method
a = [1,2,3,4, "hello", "test", 1,2,4,9.9, True]



a = [10,20,30,40]
total = 0
for i in a:
    total += i
print(total)


#NESTED FOR LOOP
for i in [1,2,3]:
    for j in [4,5,6,7]:
        print (i,j)


print ("........................."*20)
while (True):
    print ("This is while loop")
    break
i=1
while (i==1):
    print (i)
    i=3

i = 1
while i <= 10:
    print(i)
    i += 1
   
a=[1,2,3,4,5,6,7,7,"Hello", "Test"]
i = 0
while i < len(a):
    print(a[i])
    i += 1

