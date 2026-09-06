import os

while True:

    print("\n========== FILE MANAGER ==========")
    print("1. Show Current Folder")
    print("2. Create Folder")
    print("3. Show Files")
    print("4. Check File")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        print("Current Folder:")
        print(os.getcwd())

    elif choice == "2":

        folder = input("Enter folder name: ")

        if os.path.exists(folder):
            print("Folder already exists! ⚠️")
        else:
            os.mkdir(folder)
            print("Folder created successfully! ✅")

    elif choice == "3":

        print("\n========== FILES ==========")

        files = os.listdir()

        for item in files:
            print(item)

    elif choice == "4":

        filename = input("Enter file name: ")

        if os.path.isfile(filename):
            print("File exists! ✅")
        else:
            print("File not found! ❌")

    elif choice == "5":

        print("Program closed! 👋")
        break

    else:
        print("Invalid choice!")