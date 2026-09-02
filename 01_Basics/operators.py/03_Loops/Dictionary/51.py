students = {
    "Rahul": 78,
    "Amit": 45,
    "Priya": 92,
    "Neha": 32,
    "Karan": 66
}

for name, marks in students.items():
    print("Student:", name)
    print("Marks:", marks)

    if marks >= 40:
        print("Result: Pass")
    else:
        print("Result: Fail")

    print("----------------")