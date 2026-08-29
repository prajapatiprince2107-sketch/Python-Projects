students = {
    "student1": {"name": "Rahul", "age": 21},
    "student2": {"name": "Prince", "age": 22},
    "student3": {"name": "Amit", "age": 25}
}
for key,value in students.items():
    if value["age"] > 21:
        print(value["name"])