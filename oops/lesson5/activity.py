# Write a program to create a base class that consists of two functions - one to display a value, and another function is an abstract method. Next, create a subclass that consists of a method similar to the abstract method. Finally, showcase how Abstraction is being implemented in this example.

from abc import ABC,abstractmethod
class ABSclass(ABC):
    def print(self, x):
     print("passed value: ",x)

    @abstractmethod
    def task(self):
       print("we are inside ABC class task")

class testclass(ABSclass):
   def task(self):
      print("we are inside testclass)")

test_obj = testclass()
test_obj.task()
test_obj.print(1000)

