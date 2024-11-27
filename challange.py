# Parent Class: Vehicle
class Vehicle:
    def move(self):
        print("The vehicle is moving.")

# Child Class: Car
class Car(Vehicle):
    def move(self):
        print("The car is driving ")

# Child Class: Plane
class Plane(Vehicle):
    def move(self):
        print("The plane is flying ")

# Child Class: Boat
class Boat(Vehicle):
    def move(self):
        print("The boat is sailing ")

# Polymorphism in Action
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()
