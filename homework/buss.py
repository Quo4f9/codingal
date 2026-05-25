# Create a Bus child class inherited from the Vehicle class to calculate the total fare

class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):
    def fare(self):
        
        amount = super().fare()
e
        total_fare = amount + (amount * 10 / 100)
        return total_fare
school_bus = Bus(50)


print("Total Bus Fare is:", school_bus.fare())