# # RECURSION (Function calls function)


# def fact(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n * fact(n - 1)


# print(fact(5))


# # OOP
# class Person:
#     a = 100
#     b = 1000


# data = Person()
# print(data)

# print(data.a)
# print(data.b)

# data.door = "Main door"
# print(data.door)

# data2 = Person()
# print(data2)

# print(data2.a)
# print(data2.b)
# # print (data2.door) #This shows errors.


# class Test:
#     a = 567
#     b = 432

#     def add(self):
#         return self.a + self.b

#     def sub (self):
#         return self.a - self.b

#     def result (self):
#         return self.add (), self .sub ()

# obj1 = Test()
# print(obj1.a)
# print(obj1.add())
# print (obj1.result ())

# Assignment
# Requirements for python class:
# 1. Name & Marks (Manually assign - MArks shoudld be in list)
# 2. Method Grade:
# 	80+ = "A"
# 	60-79 = "B"
# 	40-59 = "C"
# 	Below 40 = "Fail"
# Obj = Student ()
# print (obj.grade ())


class Student:
    Name = "Dhruba"
    marks = [87, 75, 88, 90, 56]

    def grade(self):

        avg = sum(self.marks) / len(self.marks)

        print("Average:", avg)

        if avg >= 80:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 40:
            return "C"
        else:
            return "Fail"


obj = Student()
print("Grade:", obj.grade())
