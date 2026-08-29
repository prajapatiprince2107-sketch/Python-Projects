students = {
    "student1": {"name": "Rahul", "age": 17, "city": "Ahmedabad"},
    "student2": {"name": "Prince", "age": 22, "city": "Surat"},
    "student3": {"name": "Amit", "age": 19, "city": "Rajkot"}
}
 
for key, value in students.items():
    if value["city"] == "Surat":
        print(value["name"], value["age"])