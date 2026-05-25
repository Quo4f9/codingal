# Write a program to overload the less than (<) and equal to (==) operators. For example, create objects - ob1 and ob2 with values 3 and 4 to compare values, respectively. You can additionally create more objects to try different values.

class A:
    def __init__(self, A):
        self.A=A
    def __lt__(self, other):
        if self.A < other.A:
            return "ob1 is less than ob2"
        else:
            return "ob2 is less than ob2"
        
    def __eq__(self, other):
        if self.A == other.A:
            return "both equal "
        else:
            return "not equal"
ob1=A(2)
ob2=A(3)

print("passed values",ob1.A, ob2.A)



ob3=A(4)
ob4=A(4)

print("passed values",ob3.A,ob4.A)
print(ob3==ob4)