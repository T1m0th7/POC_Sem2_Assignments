text = input("Enter some text please :) ")

result = text.find("the")

if result == -1:
    print("The word the is in the string")
else:
    print("The word the is not in the string")
    print("It is located at",result)