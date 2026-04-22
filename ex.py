def calculate_total(marks):
    total = 0
    for m in marks:
        total += m
    return total


def calculate_average(marks):
    total = calculate_total(marks)
    return total / len(marks)


def find_highest(marks):
    highest = marks[0]
    for m in marks:
        if m > highest:
            highest = m
    return highest


def count_pass_fail(marks):
    passed = 0
    failed = 0

    for m in marks:
        if m >= 40:
            passed += 1
        else:
            failed += 1

    return passed, failed


# Tuple of student marks
student_marks = (55, 70, 35, 90, 40)

print("Marks:", student_marks)

total = calculate_total(student_marks)
print("Total:", total)

average = calculate_average(student_marks)
print("Average:", average)

highest = find_highest(student_marks)
print("Highest:", highest)

passed, failed = count_pass_fail(student_marks)
print("Passed:", passed)
print("Failed:", failed)

for m in student_marks:
    if m >= 80:
        print(m, "A")
    elif m >= 60:
        print(m, "B")
    elif m >= 40:
        print(m, "C")
    else:
        print(m, "Fail")


def calculate_total(marks):
    total = 0
    for m in marks:
        total += m
    return total


def calculate_average(marks):
    return calculate_total(marks) / len(marks)


def find_highest(marks):
    highest = marks[0]
    for m in marks:
        if m > highest:
            highest = m
    return highest


def count_pass_fail(marks):
    passed = 0
    failed = 0

    for m in marks:
        if m >= 40:
            passed += 1
        else:
            failed += 1

    return passed, failed


# -------- USER INPUT PART --------
name = (input("Enter name of students: "))
n = int(input("Enter number of students: "))

marks_list = []

i = 1
while i <= n:
    m = int(input("Enter marks of student " + str(i) + ": "))
    marks_list.append(m)
    i += 1

# Convert list to tuple
student_marks = tuple(marks_list)

print("\nMarks:", student_marks)

# -------- CALCULATIONS --------

total = calculate_total(student_marks)
print("Total:", total)

average = calculate_average(student_marks)
print("Average:", average)

highest = find_highest(student_marks)
print("Highest:", highest)

passed, failed = count_pass_fail(student_marks)
print("Passed:", passed)
print("Failed:", failed)