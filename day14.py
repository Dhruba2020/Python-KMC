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
        return f"Name = {self.name}, Average = {self.average()}, Grade: {self.grade()}"


obj = StudentResult("Ramesh", 78, 88, 99, 96, 87, 98, 87, 89, 90, 97)
print(obj.display())


# INHERITANCE
class Parent:
    a = 100
    b = 45

    def Parent_Value(self):
        print("Parent a:", self.a)
        print("Parent b:", self.b)

    def Parent_Message(self):
        print("This is Parent Message")


class Child(Parent):
    b = "Hari Sharma"
    d = 10

    def Child_Value(self):
        print("Child b:", self.b)
        print("Child d:", self.d)

    def Child_Message(self):
        print("This is Child Message")


obj = Child()

print(obj.b)
print(obj.a)


obj.Parent_Value()
obj.Parent_Message()
obj.Child_Value()
obj.Child_Message()


# ASSIGN
class Parent:
    a = 100
    b = 45

    def add(self):
        return self.a + self.b


class Child(Parent):
    d = 10

    def display(self):
        return self.add()

obj = Child()
print(obj.b)
print(obj.a)
print(obj.display())

    # ASSIGN
class TestParent ():
    def __init__ (self):
        print (" I am from Test Parent")

class TestChild (TestParent):
    def __init__(self):
        print (" I am from Test Child")
        TestParent.__init__ (self)
        super().__init__()

obj = TestChild ()

#ASSIGN

class TestParent ():
    def __init__ (self, a):
        print (" I am from Test Parent")

class TestChild (TestParent):
    def __init__(self, a, b, c, d):
        print (" I am from Test Child")
        self.b = b
        TestParent.__init__ (self, a)
        super().__init__(a)


def test (self, amount):
    return self.b


class Child (TestChild):
    pass
obj = TestChild (1,2,3,4)
obj.test (5000)
