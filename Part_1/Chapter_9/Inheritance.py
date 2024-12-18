class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def get_descriptive_name(self):
        print(f"{self.make} {self.model} {self.year}")
    def fill_gas_tank(self):
        print("Gas Tank is filled and full now")

class Battery:
    def __init__(self,battery_size = 40):
        self.battery_size = battery_size
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery")

class Electrical_Car(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
    def fill_gas_tank(self):
        print("Electric Car doesn't have gas tank")
    
my_eCar = Electrical_Car("Suzuki","Celerio",2020)
my_eCar.get_descriptive_name()
my_eCar.fill_gas_tank()
my_eCar.battery.describe_battery()