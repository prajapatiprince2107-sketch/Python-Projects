class Car:
    
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year  = year
        
    def display_info(self):
        print("Brand",self.brand)
        print("Model",self.model)
        print("Year",self.year)
        
    def start(self):
        print(self.brand, self.model, self.year, "is starting...")
        
    def stop(self):
        print(self.brand, self.model, self.year, "has stopped.")
        
brand = input("Enter ur brand: ")
model = input("Enter ur model: ")
year = input("Enter ur year: ")

Car1 = Car(brand,model,year)

print("\n======== CAR DETAILS ========")

Car1.display_info()
Car1.start()
Car1.stop()