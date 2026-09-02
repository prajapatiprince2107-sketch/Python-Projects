employees = {
    "Rahul": 25000,
    "Amit": 32000,
    "Priya": 45000,
    "Neha": 28000,
    "Karan": 52000
}

total_salary = 0
highest_salary = 0
highest_employee = ""

for name, salary in employees.items():

    total_salary = total_salary + salary

    if salary > highest_salary:
        highest_salary = salary
        highest_employee = name

    if salary >= 40000:
        print(name, "-> High Salary")
    elif salary >= 30000:
        print(name, "-> Medium Salary")
    else:
        print(name, "-> Low Salary")

print("----------------------")
print("Total Salary:", total_salary)
print("Highest Salary:", highest_salary)
print("Highest Paid Employee:", highest_employee)
print("Average Salary:", total_salary / len(employees))