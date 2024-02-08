number1 = int(input("Enter a number"))

number2 = int(input("Enter another number"))

try:
    value = number1/number2
    print('The answer is', value)
except ZeroDivisionError:
    print('You provided 0 and division by 0 is not possible, sorry')