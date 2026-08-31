marks = {
    "Prince": 85,
    "Rahul": 65,
    "Amit": 92
}

for name, mark in marks.items():
    if mark >= 70:
        print(name, "Passed")
    else:
        print(name, "Needs improvement")