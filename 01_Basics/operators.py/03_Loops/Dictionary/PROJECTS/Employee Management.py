class Employee:
    
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        
    def show_details(self):
        print("Name:", self.name)
        print("Salary:",self.salary)
        
class Developer(Employee):
    def __init__(self, name, salary,language):
        super().__init__(name, salary)
        self.language = language
    
    def show_developer(self):
        self.show_details()
        print("Programming Language:",self.language)        
        
class Manager(Employee):
    
    def __init__(self, name, salary,team_size):
        super().__init__(name, salary)
        self.team_size = team_size
    
    def show_manager(self):
        self.sho_details()
        print("Team size:",self.team_size)
        
print("===== DEVELOPER =====")

dev_name = input("Enter developer name: ")
dev_salary = float(input("Enter developer salary: "))
language = input("Enter programming language: ")

developer = Developer(dev_name, dev_salary, language)

developer.show_developer()


print("\n===== MANAGER =====")

manager_name = input("Enter manager name: ")
manager_salary = float(input("Enter manager salary: "))
team_size = int(input("Enter team size: "))

manager = Manager(manager_name,manager_salary,team_size)

manager.show_manager()