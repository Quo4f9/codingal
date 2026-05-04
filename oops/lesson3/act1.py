# Write a Python program to implement Inheritance by creating a Parent Class Vehicle with a constructor that has details like name, maximum speed, and mileage. Then, create a Child Class Bus that inherits Class Vehicle. Finally, showcase Inheritance to display the details of the Vehicle Bus named - School Volvo.

class vehicle:
    def __init__(self,name, maxspeed,mileage): #construtor,it has values name maxpeed mileage
        self.name=name 
        self.maxspeed=maxspeed
        self.mileage=mileage

class bus (vehicle): #child class of class parent vehicle
    pass

obj1=bus("school volvo",100,1000000) #object creation for the class bus. It passes the values for name maxspeed and mileage
print("the vehicle name is",obj1.name,"max speed is",obj1.maxspeed,"mileage is",obj1.mileage)
#accesing name maxpeed mileage using the object (line 13)