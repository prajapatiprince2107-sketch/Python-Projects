students = {
    "Rahul": 85,
    "Amit": 67,
    "Priya": 92,
    "Neha": 38,
    "Karan": 74
}

total = 0
highest = 0
topper = ""
passed = 0
failed = 0

for name, marks in students.items():

    total = total + marks

    if marks > highest:
        highest = marks
        topper = name

    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "F"

    if marks >= 40:
        result = "PASS"
        passed = passed + 1
    else:
        result = "FAIL"
        failed = failed + 1

    print("Name:", name)
    print("Marks:", marks)
    print("Grade:", grade)
    print("Result:", result)
    print("----------------------")

average = total / len(students)

print("\n========== FINAL REPORT ==========")
print("Total Students:", len(students))
print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Marks:", highest)
print("Topper:", topper)
print("Passed Students:", passed)
print("Failed Students:", failed)