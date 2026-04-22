# TUPLE
a= (1,2,3,4,5,6) #paranthesis
print (type (a))
print (a[0])

b= list (a)
print (b)
b[0] =100  
a=tuple (b)
print (a)

data = {1,2,3, "hello", 'testing', 5,1,1}
print (data)


# FUNCTION - Block of Code
def test ():
    a = 600
    print (" This is value of a", a)
    return a
test ()
test ()
test ()
test ()
test ()


def test ():
    print ("This is Python")
    return [1,2,3,4,5], [6,7,8,9]
print (test ())


def sum_of_list ():
    a= [1,2,3,4,5]
    total = 0
    for i in a:
        total = total + i 
    return total

def user_info (fname, lname):
    # fname = "Sudan"
    # lname = "Bhandari"
    return f'my name is {fname} {lname}'
print (user_info ("Sudan", "Bhandari"))


def check_number (num):
    if num%2==0:
        return "even"
    else:
        return "odd"
result = check_number (10)
print (result)

result = check_number (11)
print (result)





    
