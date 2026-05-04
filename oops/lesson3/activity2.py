# Write a program to create a parent class Person (attributes - name, id number) with a method display to display the attributes. Next, create a child class Employee (attributes - name, id number, salary, post). Access the attributes of parent class in child class. Then, create an object for child class and call the display method to display the name and id number.

class person:
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print(self.name,self.idnumber,self.salary,self.post)

class employee (person):
    def __init__(self,name,idnumber,salary,post):
        self.salary=salary
        self.post=post
        # super().__init__(self,name,idnumber) 
        person.__init__(self,name,idnumber) 
obj1=employee("bob",1234567890,20000000000,"ceo")
obj1.display()

