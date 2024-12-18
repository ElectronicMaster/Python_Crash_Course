class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def printDescription(self):
        return f"Brand: {self.brand}, Model: {self.model}"

class Battery:
    def __init__(self,capacity = "Not mentioned",warranty = " Not Mentioned"):
        self.capacity = capacity
        self.warranty = warranty

class Electric_Car(Car):
    def __init__(self, brand, model, capacity, warranty):
        super().__init__(brand, model)
        self.Battery = Battery(capacity,warranty)
    def printDescription(self):
        text = super().printDescription()
        fullDesc = text + f", Capacity: {self.Battery.capacity}, Warranty: {self.Battery.warranty}"
        print(fullDesc)

e_Car = Electric_Car("BMW", "eTron", "1000mah", 8)
e_Car.printDescription()