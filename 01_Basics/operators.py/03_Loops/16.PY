correct_password = "python123"

while True:

    password = input("Enter password: ")

    if password == correct_password:
        print("✅ Correct password!")
        print("Welcome Prince!")
        break

    else:
        print("❌ Wrong password")
        print("Try again...")