# class Person ():
#     a = 10
#     b = 100
#     def test (self):
#         self.a = "Testing from class method"
#         print ("This is class attributes", self.a)
#         print (self.a)
#         print (self.b)
#         return self.a

#     def multi (self):
#         #return self.b*100
#         return self.b * self.test ()


# obj = Person ()
# print (obj)
# print (obj.a)

# obj.c = "Hari"
# print (obj.c)
# print (obj.test ())
# print (obj.multi ())


# CONSTRUCTOR


# class Math:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#         print(a, b, c)
#         print("This is a Constructor, not required to return")

#     #  return None

#     def add(self):
#         return self.a + self.b + self.c


# obj = Math(3, 6, 9)
# print(obj.add())


# ASSIGN


class Rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b


obj = Rectangle(3, 5)
print(obj.area())


# ASSGN 2
class StudentResult:
    def __init__(self, name, *marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        else:
            return "C"

    def display(self):
        return f"Name: {self.name}, Average: {self.average():}, Grade: {self.grade()}"


obj = StudentResult("Ramesh", 78, 88, 99, 96, 87, 98,87, 89, 90, 97)
print(obj.display())
