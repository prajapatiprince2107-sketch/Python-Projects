filename = "students.txt"

n = int(input("Enter number of students: "))

with open(filename, "w") as file:

    for i in range(n):

        name = input("Enter student name: ")
        marks = input("Enter marks: ")

        file.write(f"Name: {name}, Marks: {marks}\n")

print("\nData saved successfully! ✅")

print("\n========== STUDENT DATA ==========")

with open(filename, "r") as file:

    data = file.read()

    print(data)