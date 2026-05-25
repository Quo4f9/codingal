# Write a Python program to create two classes - BMW and Ferrari with similar methods and implement polymorphismPolymorphism on them.


class BMW:
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "250 km/h"


class Ferrari:
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "340 km/h"




for car in (BMW(), Ferrari()):
    print(f"{car.__class__.__name__}:")
    print("Fuel Type:", car.fuel_type())
    print("Max Speed:", car.max_speed())
    print()