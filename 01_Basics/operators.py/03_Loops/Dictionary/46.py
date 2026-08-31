students = {
    "Prince": 22,
    "Rahul": 17,
    "Amit": 21
}

for name, age in students.items():
    if age >= 18:
        print(name, "is adult")