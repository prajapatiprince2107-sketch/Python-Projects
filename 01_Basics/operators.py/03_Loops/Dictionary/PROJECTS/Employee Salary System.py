employees = {}

n = int(input("Enter number of employees: "))

for i in range(n):

    name = input("Enter employee name: ")
    salary = float(input("Enter salary: "))
    experience = int(input("Enter experience in years: "))

    employees[name] = {
        "salary": salary,
        "experience": experience
    }

total_salary = 0
highest_salary = 0
highest_employee = ""

print("\n========== EMPLOYEE REPORT ==========")

for name, details in employees.items():

    salary = details["salary"]
    experience = details["experience"]

    if experience >= 5:
        bonus = salary * 0.15
    elif experience >= 3:
        bonus = salary * 0.10
    else:
        bonus = salary * 0.05

    final_salary = salary + bonus

    total_salary = total_salary + final_salary

    if final_salary > highest_salary:
        highest_salary = final_salary
        highest_employee = name

    print("Name:", name)
    print("Basic Salary:", salary)
    print("Experience:", experience, "years")
    print("Bonus:", bonus)
    print("Final Salary:", final_salary)
    print("-------------------------")

print("Total Salary:", total_salary)
print("Highest Salary:", highest_salary)
print("Highest Paid Employee:", highest_employee)