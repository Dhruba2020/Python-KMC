# def check_number (num):
#     if num%2==0:
#         return "even"
#     else:
#         return "odd"
# result = check_number (10)
# print (result)

# result = check_number (11)
# print (result)



def list_of_integer(my_list):
    integers = []
    
    for item in my_list:
        if isinstance(item, int):
            integers.append(item)
    
    print("List of integers:", integers)
    
    if len(integers) > 0:
        max_num = integers[0]
        for num in integers:
            if num > max_num:
                max_num = num
        print("Maximum number:", max_num)
    else:
        print("No integers found")

data = [10, 20, "hello", 50, 200, 5.5, 99, "test"]

list_of_integer(data)




def list_of_number(my_list):
    integers = []
    
    for item in my_list:
        if isinstance(item, int):
            integers.append(item)
    
    if len(integers) == 0:
        return "No integers found"
    
    max_num = integers[0]
    for num in integers:
        if num > max_num:
            max_num = num
    
    return integers, max_num


result = list_of_number([10, 20, "hello", 50, 200])
print(result)

    
