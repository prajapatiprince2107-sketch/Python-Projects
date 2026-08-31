marks = {
    "Math": 80,
    "Python": 90,
    "SQL": 70
}

total = 0

for subject, mark in marks.items():
    total = total + mark

print("Total =", total)