# Write a program to implement abstraction on animal class (base class). The abstract method will be move will display what subclasses can do. Subclasses can be something like - Human, Dog.

from abc import ABC,abstractmethod

class animal(ABC):
    def move(self):
        pass

class human (animal):
    def move(self):
        print("I can walk and run")

class snake (animal):
    def move(self):
        print("I can crawl")

class dog (animal):
    def move(self):
        print("I can bark")

class lion (animal):
    def move(self):
        print("I can roar ")

R = human ()
R.move()


R = snake()
R.move()


R =dog ()
R.move()


R =lion ()
R.move()