accounts = {
    "Rahul": {
        "balance": 25000,
        "transactions": ["deposit", "withdraw", "deposit"]
    },
    "Amit": {
        "balance": 15000,
        "transactions": ["withdraw", "withdraw"]
    },
    "Priya": {
        "balance": 40000,
        "transactions": ["deposit", "deposit", "withdraw"]
    }
}

for name, details in accounts.items():

    balance = details["balance"]

    print("Customer:", name)
    print("Starting Balance:", balance)

    for transaction in details["transactions"]:

        if transaction == "deposit":
            balance = balance + 5000
            print("Deposit: +5000")

        elif transaction == "withdraw":
            balance = balance - 2000
            print("Withdraw: -2000")

    print("Final Balance:", balance)

    if balance >= 40000:
        print("Status: Premium Customer")
    elif balance >= 20000:
        print("Status: Regular Customer")
    else:
        print("Status: Basic Customer")

    print("-------------------------")