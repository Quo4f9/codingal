# Take input from user
num = int(input("Enter a number: "))

odd_numbers = []
even_numbers = []

# Loop through numbers from 1 to num-1
for i in range(1, num):
    if i % 2 != 0:
        odd_numbers.append(i)
    else:
        even_numbers.append(i)

print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)





# Original list of fruits
fruits = ["apple", "banana", "mango", "orange", "grapes"]

# Create a new list with first letter capitalized
capitalized_fruits = [fruit.capitalize() for fruit in fruits]

print("Original list:", fruits)
print("Updated list:", capitalized_fruits)