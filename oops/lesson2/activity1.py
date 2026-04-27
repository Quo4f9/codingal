# Write a program to create a class IOString which consists of a constructor that gives a default value to variable str1. Next up create a method that gets a string as input from the user. Create another method that will print the string in the upper case. Next up create an object and call methods to get everything implemented.

class IOString: #class IOString is created
    def __init__(self): #constructor is created
        self.str1=""#initializing
    def getstring(self): #method or function1
        self.str1=input ("enter the string")

    def printstring(self): #metod or function2
        print("the result is",self.str1.upper())
obj1=IOString()#object created for the class IOString
obj1.getstring() #get string function is called
obj1.printstring()#print string function is called

