class Rectangle:

    def __init__(self, base: float, height: float) -> None:
        if (base < 0):
            self.__base = 0
        else:
            self.__base = base

        if (height < 0):
            self.__height = 0
        else:
            self.__height = height

    def get_height(self) -> float:
        return self.__height

    def get_base(self) -> float:
        return self.__base 

    def get_perimeter(self) -> float:
        return 2 * self.__base + 2 * self.__height

    def get_area(self) -> float:
        return self.__base * self.__height       # Youdo get_area method
    
    def __str__(self) -> str:
        # Rectangle of base:3, height:4
        return "Rectangle of base:" + str(self.__base) + ", height:" + str(self.__height)
        
rectangle1 = Rectangle(3, 4)
print(rectangle1.get_base())
print(rectangle1.get_height())
print(rectangle1.get_area())
print(rectangle1.get_perimeter())

print(rectangle1)

rectangle2 = Rectangle(5, 6)
print(rectangle2.get_base())
print(rectangle2.get_height())
print(rectangle2.get_area())
print(rectangle2.get_perimeter())

print(rectangle2)

# YOUDO>  create two rectangles.  print their base, height, perimeter, and area
# using only the methods not the fields/property/attributes