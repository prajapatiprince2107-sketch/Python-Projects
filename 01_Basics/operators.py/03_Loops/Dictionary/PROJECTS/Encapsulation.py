class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount
            print("Deposit successful!")
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Invalid amount!")
        else:
            self.__balance = self.__balance - amount
            print("Withdrawal successful!")

    def show_balance(self):
        print("Account Holder:", self.name)
        print("Balance:", self.__balance)


name = input("Enter account holder name: ")
balance = float(input("Enter starting balance: "))

account = BankAccount(name, balance)

while True:

    print("\n===== BANK MENU =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == 2:

        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == 3:

        account.show_balance()

    elif choice == 4:

        print("Thank you! 👋")
        break

    else:
        print("Invalid choice!")