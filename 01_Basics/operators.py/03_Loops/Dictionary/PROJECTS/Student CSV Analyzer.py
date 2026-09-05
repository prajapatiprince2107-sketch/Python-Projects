import csv

filename = "students.csv"

print("===== STUDENT SEARCH =====")

search_name = input("Enter student name to search: ")

found = False

with open(filename, "r") as file:

    reader = csv.DictReader(file)

    for student in reader:

        if student["Name"].lower() == search_name.lower():

            print("\nStudent Found! ✅")
            print("Name:", student["Name"])
            print("Age:", student["Age"])
            print("Marks:", student["Marks"])

            found = True
            break

if not found:
    print("Student not found! ❌")


print("\n===== TOP STUDENTS =====")

with open(filename, "r") as file:

    reader = csv.DictReader(file)

    for student in reader:

        marks = float(student["Marks"])

        if marks >= 80:
            print(
                student["Name"],
                "→",
                marks
            )