name = input("Enter student name: ")

total = 0
subject = 1

while subject <= 5:
    marks = int(input("Enter marks: "))
    total = total + marks
    subject = subject + 1

percentage = total / 5

print("\nStudent:", name)
print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 90:
    print("Grade: A+")
elif percentage >= 80:
    print("Grade: A")
elif percentage >= 70:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 50:
    print("Grade: D")
else:
    print("Fail")