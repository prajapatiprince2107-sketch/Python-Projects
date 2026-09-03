employees = {
    "emp1": {
        "name": "Rahul",
        "department": "IT",
        "scores": [85, 90, 78]
    },
    "emp2": {
        "name": "Amit",
        "department": "HR",
        "scores": [72, 68, 75]
    },
    "emp3": {
        "name": "Priya",
        "department": "IT",
        "scores": [95, 92, 98]
    },
    "emp4": {
        "name": "Neha",
        "department": "Finance",
        "scores": [60, 65, 58]
    }
}

highest_average = 0
best_employee = ""

for employee_id, details in employees.items():

    total = 0

    for score in details["scores"]:
        total = total + score

    average = total / len(details["scores"])

    if average >= 90:
        performance = "Excellent"
    elif average >= 75:
        performance = "Very Good"
    elif average >= 60:
        performance = "Good"
    else:
        performance = "Needs Improvement"

    if average > highest_average:
        highest_average = average
        best_employee = details["name"]

    print("Employee ID:", employee_id)
    print("Name:", details["name"])
    print("Department:", details["department"])
    print("Scores:", details["scores"])
    print("Total:", total)
    print("Average:", average)
    print("Performance:", performance)
    print("-------------------------")

print("\n========== FINAL REPORT ==========")
print("Best Employee:", best_employee)
print("Highest Average:", highest_average)