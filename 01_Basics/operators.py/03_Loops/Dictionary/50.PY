students = {
    "Prince": 85,
    "Rahul": 45,
    "Amit": 72,
    "Raj": 38
}

for name, marks in students.items():
    if marks >= 50:
        print(name, "Passed with", marks)