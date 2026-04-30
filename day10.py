# #Keyword Argument
# def user_info(fname, lname, age):
#     return f'my name is {fname}{lname}'
# print (user_info ("Sudan", "Bhandari", 28))
# print (user_info (fname="sudan", lname='Bhandari', age = 28))

# #Arbitary Postal Argument

# def sum_number(*num):
#     int_values = [i for i in num if isinstance(i, int)]

#     if len(int_values) > 1:
#         total = 0
#         for i in int_values:
#             total += i
#         return f"Total Sum = {total}"
#     else:
#         return "Len must be more than 1"


# def per(**data):
#     if "Math" not in data:
#         return "Data for Math is missing"
    
#     print("Eng", data.get("Eng"))
#     print("Nep", data.get("Nep"))
#     print("Math", data.get("Math"))


# print(per(Eng=100, Nep=98, Math=90))
# print(per(Eng=100, Nep=98))


def per(**data):
    # if 'Eng' not in data or 'Nep' not in data or 'Math' not in data:
    #     print ("Error")
    # else:

    if "Math" not in data:
        return "Data for Math is missing"
    
    print("Eng", data ["Eng"])
    print("Nep", data ["Nep"])
    print("Math", data ["Math"])


print(per(Eng=100, Nep=98, Math=90))
print(per(Eng=100, Nep=98))


def per(**data):
    need = ["eng", "nep", "math"]

    for key in need:
        if key not in data:
            return f"Key '{key}' is missing"
    return data["eng"] , data["nep"] ,data["math"]
print(per(eng=100, nep=75, math=10))
print(per(eng=20))

#ARBITARY POSITIONAL ARGUMENTS & ARBITARY KEYWORDS ARGUMENTS TOGETHER

def student_info (*marks, **info):
    print (info)
    print (marks)
student_info (100, 45, 69, 66, name="Sudan", school= "Trinity")

