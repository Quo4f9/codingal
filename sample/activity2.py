# Write a program to return the addition of numbers of two different lists. Then, display a list that is square of numbers of another list. Use the map() function here to get the desired result.
number1=[1,2,3]
number2=[4,5,6]
def square(n):
    return n*n 
result=map(lambda x,y:x+y,number1, number2)
print("addition of two lists",list(result))
square=list(map(square,number1))
print("the square of number1 list is",square)