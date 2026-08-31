balance = 10000

while True:

    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your balance is:", balance)

    elif choice == 2:
        amount = int(input("Enter deposit amount: "))
        balance = balance + amount
        print("Deposit successful!")
        print("New balance:", balance)

    elif choice == 3:
        amount = int(input("Enter withdrawal amount: "))

        if amount <= balance:
            balance = balance - amount
            print("Withdrawal successful!")
            print("Remaining balance:", balance)
        else:
            print("Insufficient balance!")

    elif choice == 4:
        print("Thank you for using ATM!")
        break

    else:
        print("Invalid choice!")