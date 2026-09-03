expenses = {
    "Monday": {
        "Food": 250,
        "Travel": 100,
        "Shopping": 500
    },
    "Tuesday": {
        "Food": 300,
        "Travel": 150,
        "Shopping": 200
    },
    "Wednesday": {
        "Food": 200,
        "Travel": 120,
        "Shopping": 800
    },
    "Thursday": {
        "Food": 350,
        "Travel": 100,
        "Shopping": 300
    }
}

total_expense = 0
highest_expense = 0
highest_day = ""

for day, expenses_data in expenses.items():

    daily_total = 0

    for category, amount in expenses_data.items():

        daily_total = daily_total + amount

        print(day, "-", category, ":", amount)

    total_expense = total_expense + daily_total

    if daily_total > highest_expense:
        highest_expense = daily_total
        highest_day = day

    print("Daily Total:", daily_total)
    print("-------------------------")

average_expense = total_expense / len(expenses)

print("\n========== EXPENSE REPORT ==========")
print("Total Expense:", total_expense)
print("Average Daily Expense:", average_expense)
print("Highest Expense:", highest_expense)
print("Highest Expense Day:", highest_day)