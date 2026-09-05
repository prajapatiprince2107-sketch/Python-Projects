filename = "students.txt"

while True:

    print("\n===== STUDENT FILE MENU =====")
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter student name: ")
        marks = input("Enter marks: ")

        with open(filename, "a") as file:
            file.write(f"{name},{marks}\n")

        print("Student added successfully! ✅")

    elif choice == "2":

        try:
            with open(filename, "r") as file:
                data = file.read()

                if data:
                    print("\n========== STUDENTS ==========")
                    print(data)
                else:
                    print("No student data found!")

        except FileNotFoundError:
            print("File does not exist yet!")

    elif choice == "3":

        search_name = input("Enter student name to search: ")

        try:
            with open(filename, "r") as file:

                found = False

                for line in file:

                    name, marks = line.strip().split(",")

                    if name.lower() == search_name.lower():
                        print("Student Found! ✅")
                        print("Name:", name)
                        print("Marks:", marks)
                        found = True
                        break

                if not found:
                    print("Student not found! ❌")

        except FileNotFoundError:
            print("No student file found!")

    elif choice == "4":

        print("Program closed! 👋")
        break

    else:
        print("Invalid choice!")