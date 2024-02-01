#Continue with code from 3.3

number1 = 0
number2 = 0
try:
    number1 = int(input("Enter a number"))
    number2 = int(input("Enter another number"))
except ValueError:
    print("An input was not correct")
else:
    print("No value error detected")
finally:
    print("Values taken care of")

try:
    number1/number2
    print("The answer is correct")
    pass  # YOUDO remove pass when done
except ZeroDivisionError:
    print("That is not possible. You divided by a 0. Womp Womp")
    pass  # YOUDO remove pass when done
#YOUDO:  else and finally here as well.  