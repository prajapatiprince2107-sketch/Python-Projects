import json

students = []

n = int(input("Enter number of students: "))

for i in range(n):

    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    marks = float(input("Enter marks: "))

    student = {
        "name": name,
        "age": age,
        "marks": marks
    }

    students.append(student)


with open("students.json", "w") as file:

    json.dump(students, file, indent=4)

print("\nData saved successfully! ✅")


with open("students.json", "r") as file:

    data = json.load(file)


print("\n========== STUDENT DATA ==========")

for student in data:

    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Marks:", student["marks"])
    print("-------------------------")