# Write a program to create a class Parrot and perform the following tasks - 1. Create a class variable species 2. Create a __init__ method that has instance variables - name and age 3. Create instances of class Parrot, passing arguments as well 4. Print Class variable by accessing it 5. Print Instance variables as well
# create class
class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
obj1 = Parrot("Blu", 10) #blu is an object of class parrot
obj2 = Parrot("Woo", 15) #woo is an object of class parrot

# access the class attributes
print("Blu is a {}".format(obj1.species))
print("Woo is also a {}".format(obj2.species))

# access the instance attributes
print("{} is {} years old".format( obj1.name, obj1.age))
print("{} is {} years old".format( obj2.name, obj2.age))

