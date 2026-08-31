correct_username = "prince"
correct_password = "1234"

attempts = 3

while attempts > 0:

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("✅ Login successful!")
        break

    else:
        attempts = attempts - 1
        print("❌ Wrong username or password")
        print("Attempts remaining:", attempts)

if attempts == 0:
    print("Account locked!")