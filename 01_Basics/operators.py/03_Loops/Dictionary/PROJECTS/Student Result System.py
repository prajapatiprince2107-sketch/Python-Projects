students = {}

n = int(input("Enter number of students: "))

for i in range(n):

    name = input("Enter student name: ")
    marks = []

    for j in range(3):
        mark = float(input(f"Enter marks of subject {j + 1}: "))
        marks.append(mark)

    students[name] = marks

print("\n========== STUDENT REPORT ==========")

highest_average = 0
topper = ""

for name, marks in students.items():

    total = 0

    for mark in marks:
        total = total + mark

    average = total / len(marks)

    if average >= 80:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "F"

    if average >= 40:
        result = "PASS"
    else:
        result = "FAIL"

    if average > highest_average:
        highest_average = average
        topper = name

    print("Name:", name)
    print("Marks:", marks)
    print("Total:", total)
    print("Average:", average)
    print("Grade:", grade)
    print("Result:", result)
    print("-------------------------")

print("Topper:", topper)
print("Highest Average:", highest_average)