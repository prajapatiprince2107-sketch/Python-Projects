accounts = {
    "Rahul": {
        "balance": 25000,
        "account_type": "Savings"
    },
    "Amit": {
        "balance": 12000,
        "account_type": "Current"
    },
    "Priya": {
        "balance": 50000,
        "account_type": "Savings"
    },
    "Neha": {
        "balance": 8000,
        "account_type": "Savings"
    }
}

total_balance = 0
highest_balance = 0
richest_customer = ""

for name, details in accounts.items():

    balance = details["balance"]
    account_type = details["account_type"]

    total_balance = total_balance + balance

    if balance > highest_balance:
        highest_balance = balance
        richest_customer = name

    if balance >= 40000:
        category = "Premium"
    elif balance >= 20000:
        category = "Standard"
    else:
        category = "Basic"

    print("Customer:", name)
    print("Account Type:", account_type)
    print("Balance:", balance)
    print("Category:", category)
    print("------------------------")

print("\n========== BANK REPORT ==========")
print("Total Customers:", len(accounts))
print("Total Balance:", total_balance)
print("Average Balance:", total_balance / len(accounts))
print("Highest Balance:", highest_balance)
print("Richest Customer:", richest_customer)