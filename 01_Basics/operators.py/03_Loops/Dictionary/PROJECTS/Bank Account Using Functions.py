def deposit(balance, amount):
    return balance + amount


def withdraw(balance, amount):
    if amount > balance:
        print("Insufficient Balance!")
        return balance

    return balance - amount


def check_balance(balance):
    print("Current Balance:", balance)


balance = float(input("Enter starting balance: "))

while True:

    print("\n========== BANK MENU ==========")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        check_balance(balance)

    elif choice == 2:

        amount = float(input("Enter deposit amount: "))

        balance = deposit(balance, amount)

        print("Deposit Successful!")
        print("New Balance:", balance)

    elif choice == 3:

        amount = float(input("Enter withdrawal amount: "))

        balance = withdraw(balance, amount)

        print("Current Balance:", balance)

    elif choice == 4:

        print("Thank you for using the Bank System! 😎")
        break

    else:

        print("Invalid Choice!")