students = {
    "student1": {"name": "Rahul", "age": 21, "city": "Ahmedabad"},
    "student2": {"name": "Prince", "age": 22, "city": "Surat"},
    "student3": {"name": "Amit", "age": 25, "city": "Rajkot"}
}

for key,value in students.items():
    if value["age"] >= 21:
        print(value["name"],value["city"])