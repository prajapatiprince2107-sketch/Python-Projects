students = {
    "Rahul": 78,
    "Amit": 45,
    "Priya": 92,
    "Neha": 32,
    "Karan": 66
}

total = 0
highest = 0
topper = ""

for name, marks in students.items():
    total = total + marks

    if marks > highest:
        highest = marks
        topper = name

average = total / len(students)

print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Marks:", highest)
print("Topper:", topper)