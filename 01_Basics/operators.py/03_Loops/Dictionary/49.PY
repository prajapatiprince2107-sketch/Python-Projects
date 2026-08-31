marks = {
    "Math": 80,
    "Python": 95,
    "SQL": 70
}

highest = 0

for subject, mark in marks.items():
    if mark > highest:
        highest = mark

print("Highest Mark =", highest)