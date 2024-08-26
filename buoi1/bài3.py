class Vehicle:
    def __init__(self, make):
        self.make = make

    def description(self):
        return f"Vehicle Make: {self.make}"

class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make)
        self.model = model

    def description(self):
        return f"Car Make: {self.make}, Model: {self.model}"

class ElectricCar(Car):
    def __init__(self, make, model, battery_size):
        super().__init__(make, model)
        self.battery_size = battery_size

    def description(self):
        return f"ElectricCar Make: {self.make}, Model: {self.model}, Battery Size: {self.battery_size} kWh"


vehicle = Vehicle("Toyota")
car = Car("Honda", "Civic")
electric_car = ElectricCar("Tesla", "Model S", 100)

print(vehicle.description())
print(car.description())
print(electric_car.description())

