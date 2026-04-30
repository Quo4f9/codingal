# Write a Python program to create a class named Circle constructed by a radius and two methods to compute the area and the perimeter of a circle.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius



r = float(input("Enter the radius of the circle: "))
circle = Circle(r)

print("Area of the circle:", circle.area())
print("Perimeter (circumference) of the circle:", circle.perimeter())