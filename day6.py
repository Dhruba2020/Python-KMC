# # data1 = ["apple", 54, 71.3, False, "Orange", True, 21, 13.8]
# # #NESTED LIST


# # b = [6,7,8]
# # a= [1,2,3,4,5,b]
# # print (a)
# # c=[1,2,3,4,5,[6,7,8,9]]

# # #to print 8 from the above list
# # print (c [-1][2])

# # d= c[-1]

# # print (d[2])

# # e= [1,2,3 [4,5][6,7 (8)]]

# # #e=1,2,3,4,5,6,7,8

# # DICTIONARY (Polymorphism:)

# a = {
#     "name": "Hari",
#     "address": "Kathmandu",
#     "age": "23",
#     "phone": [123, 456],
#     "Address": "Nepal",
# }
# # print(type(a))
# # print(a["name"], a["address"], a["Address"])

# # print(len(a))
# # # a="Sudan"
# # print (len(a))
# # print(a.keys())
# # print(a.values())
# # print("this is print")
# # print(a ["phone"] [-1])

# # #HOW TO ADD DICTIONARY?

# user_info = {
#     "name": "Sudan",
#     "age": 22
# }
# user_info ["name"]= "Hari"
# user_info ["phone"] = 123
# user_info ["age"]=28
# print (user_info)

# user_info.update({"name": "Hari", "age": 12, "phone": 123, "role": "Teacher"})

# print(user_info)


# # del
# # pop 
# # popitem
# # clear


# del user_info["role"]

# a =data.pop ("role")
# print (a)

# a={} #This is empty item
# a.popitem()
# print (a) #this throws error

# data.clear ()
# print (data)


#QUESTION
user_info ={
    "name": "Hari",
    "age": 123,
    "phone": [
        {
            "type": "NTC",
            "num": 9844444444
        },
        {
            "type":"Ncell",
            "num": 9800000000
        }
    ],
    "role": "teacher"
}

print (f'{user_info ["name"]} {user_info ["phone"] [0]["type"]} number is {user_info ["phone"] [0]["num"]}') 
print (f'{user_info ["name"]} {user_info ["phone"] [1]["type"]} number is {user_info ["phone"] [1]["num"]}') 
