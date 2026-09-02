students = {
    "student1": {
        "name": "Rahul",
        "age": 20,
        "marks": {
            "Python": 85,
            "SQL": 78,
            "English": 72
        }
    },

    "student2": {
        "name": "Priya",
        "age": 21,
        "marks": {
            "Python": 92,
            "SQL": 88,
            "English": 90
        }
    },

    "student3": {
        "name": "Amit",
        "age": 19,
        "marks": {
            "Python": 65,
            "SQL": 70,
            "English": 58
        }
    }
}

for student_id, details in students.items():

    print("Student ID:", student_id)
    print("Name:", details["name"])
    print("Age:", details["age"])

    total = 0

    print("Subjects:")

    for subject, marks in details["marks"].items():
        print(subject, ":", marks)
        total = total + marks

    average = total / len(details["marks"])

    print("Total Marks:", total)
    print("Average Marks:", average)

    if average >= 80:
        print("Grade: A")
    elif average >= 70:
        print("Grade: B")
    elif average >= 60:
        print("Grade: C")
    elif average >= 40:
        print("Grade: D")
    else:
        print("Grade: F")

    print("==========================")