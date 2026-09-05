import csv

filename = "students.csv"

n = int(input("Enter number of students: "))

with open(filename, "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "Marks"])

    for i in range(n):

        name = input("Enter student name: ")
        age = int(input("Enter age: "))
        marks = float(input("Enter marks: "))

        writer.writerow([name, age, marks])

print("\nData saved successfully! ✅")


print("\n========== STUDENT DATA ==========")

with open(filename, "r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)