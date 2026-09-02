employees = {
    "emp1": {
        "name": "Rahul",
        "department": "IT",
        "salary": 45000
    },
    "emp2": {
        "name": "Amit",
        "department": "HR",
        "salary": 35000
    },
    "emp3": {
        "name": "Priya",
        "department": "IT",
        "salary": 55000
    },
    "emp4": {
        "name": "Neha",
        "department": "Finance",
        "salary": 48000
    }
}

total_salary = 0
it_employees = 0

for employee_id, details in employees.items():

    print("Employee ID:", employee_id)
    print("Name:", details["name"])
    print("Department:", details["department"])
    print("Salary:", details["salary"])

    total_salary = total_salary + details["salary"]

    if details["department"] == "IT":
        it_employees = it_employees + 1

    if details["salary"] >= 50000:
        print("Category: High Salary")
    elif details["salary"] >= 40000:
        print("Category: Medium Salary")
    else:
        print("Category: Normal Salary")

    print("-------------------------")

print("Total Employees:", len(employees))
print("Total Salary:", total_salary)
print("Average Salary:", total_salary / len(employees))
print("IT Employees:", it_employees)