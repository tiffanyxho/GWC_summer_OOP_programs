class Vehicle:
    # initializing
    def __init__(self):     # need self so that you know that we are initializing attributes part of this Vehicle class
        self.wheels = 0
        self.driver = "John Smith"

    def change_wheels(self, num_wheels):
        self.wheels = num_wheels

    def change_driver(self, driver_name):
        self.driver = driver_name

class Car(Vehicle):
    def __init__(self, color, windows, brand_name):
        Vehicle.__init__(self)      # tells program that all the functions and attributes of the Vehicle class will be inheritted by the Car class
        self.car_color = color
        self.num_windows = windows
        self.brand = brand_name

ericka = Car("red", 4, "Rusteez")

print(ericka.wheels)

ericka.change_wheels(4)

print(ericka.wheels)
