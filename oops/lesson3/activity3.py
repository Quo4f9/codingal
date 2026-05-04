# Write a program to create a base class Bird, with a constructor and two methods. Then, create a child class that inherits the constructor from Class Bird and has two functions. Finally, display how you can use Super to access the parent class constructor inside the child class.

# parent class
class Bird:
    
    def __init__(self): #constructor
        print("Bird is ready")

    def whoisThis(self): #Methoed 1
    
        print("Bird")

    def swim(self): #methoed 2
        print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__() #super function we can inherit all atributes and methoeds of parent class using this function.
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

# Object Creation
peggy = Penguin() #object creation for child class pengiun
peggy.whoisThis()
peggy.swim()
peggy.run()



 


