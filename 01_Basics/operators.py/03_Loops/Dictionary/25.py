students = {
    "student1": {"name": "Rahul", "age": 21, "city": "Ahmedabad"},
    "student2": {"name": "Prince", "age": 22, "city": "Surat"}
}

for key, value in students.items():
    if value["age"] >= 22:
        print(value["name"])