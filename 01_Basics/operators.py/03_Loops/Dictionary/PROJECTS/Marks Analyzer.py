students = {}

n = int(input("How many students? "))

for i in range(n):

    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))

    students[name] = marks


passed = {
    name: marks
    for name, marks in students.items()
    if marks >= 40
}

failed = {
    name: marks
    for name, marks in students.items()
    if marks < 40
}

grades = {
    name: (
        "A" if marks >= 80
        else "B" if marks >= 60
        else "C" if marks >= 40
        else "F"
    )
    for name, marks in students.items()
}


print("\n========== ALL STUDENTS ==========")
print(students)

print("\n========== PASSED ==========")
print(passed)

print("\n========== FAILED ==========")
print(failed)

print("\n========== GRADES ==========")
print(grades)