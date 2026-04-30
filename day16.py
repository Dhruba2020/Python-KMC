class Parent1:
    a = 10
    b = 11


class Parent2:
    c = 100
    d = 10


class Child(Parent1, Parent2):
    a = 2


# class.Child2 (Child):
# .....d. = .10


obj = Child()
print(obj.a)
print(Child.__mro__)


# LAMBDA

# def add (a,b):
#     return a+add (1, 5)

# or
# Above lines are equavalent to the below Lambda Function

add = lambda x, y: x + y
print(add(1, 5))


def add(x, y):
    return x + y


print(add(1, 2))


data = lambda x, y: x + y
print(data(1, 2))


data = [1, 2, 3, 4]
a = [i**2 for i in data]

print(a)

square = lambda *args: [i**2 for i in args]

print(square(1, 2, 3, 4, 5))
print(square(15, 26))
