students = {}

n = int(input("Enter number of students: "))

for i in range(n):

    name = input("Enter student name: ")
    attendance = float(input("Enter attendance percentage: "))

    students[name] = attendance

print("\n========== ATTENDANCE REPORT ==========")

for name, attendance in students.items():

    if attendance >= 75:
        status = "Eligible"
    else:
        status = "Not Eligible"

    print("Name:", name)
    print("Attendance:", attendance, "%")
    print("Status:", status)
    print("-------------------------")