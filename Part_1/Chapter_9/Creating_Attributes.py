class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_car_details(self):
        print(f"make: {self.make}\nmodel: {self.model}\nyear: {self.year}\nodometer reading: {self.odometer_reading}")
    
obj = Car("Audi","R8",2024)

obj.get_car_details()