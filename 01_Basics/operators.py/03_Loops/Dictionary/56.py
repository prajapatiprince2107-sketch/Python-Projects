students = {
    "Rahul": [78, 85, 69],
    "Amit": [55, 62, 71],
    "Priya": [92, 88, 95],
    "Neha": [35, 42, 38],
    "Karan": [76, 81, 73]
}

for name, marks in students.items():

    total = 0

    for mark in marks:
        total = total + mark

    average = total / len(marks)

    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"

    print("Student:", name)
    print("Marks:", marks)
    print("Total:", total)
    print("Average:", average)
    print("Grade:", grade)
    print("----------------------")