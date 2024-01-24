# Write a program that ask the user for two numbers.

# Then output the division of those two numbers.  

# Use try except to handle situations where you divide by zero.  

number1 = int(input("Enter a number:"))

number2 = int(input("Enter another number:"))

try: 
    value = number1/number2
    print('The inverse of', value)
except ZeroDivisionError:
    print('You provided 0 and division by 0 is not possible, sorry')

