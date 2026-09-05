class BankAccount:
    
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance + amount
        print("Diposit successful!")

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful!")
        else:
            print("Insuffcient balance!")

    def show_balance(self):
        print("Accoubn Holder:",self.name)
        print("Current Balance:", self.balance)
        
name = input("Enter account holder name: ")
balance = float(input("Enter starting balance: "))

account = BankAccount(name,balance)

while True:
    
    print("\n===== BANK MENU =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4.Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        
        amount = float(input("Enter Withdrawal amount: "))
        account.deposit(amount)

    elif choice == 2:
     
        
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)
        
    elif choice == 3:
        
        account.show_balance()
        
    elif choice == 4:
        
        print("Thank you! 🤗")
    else:
        print("Invalid")
           