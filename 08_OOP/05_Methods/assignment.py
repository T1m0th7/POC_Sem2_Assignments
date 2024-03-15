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

    # YOUDO the get_base method

    def get_perimeter(self) -> float:
        return 2 * self.__base + 2 * self.__height

    # Youdo get_area method
    
    def __str__(self) -> str:
        #Rectangle with base:3, height:4
        return "Rectangle with base:" + str(self.__base) + ", height:" + str(self.__height)
    


# YOUDO>  create two rectangles.  print their base, height, perimeter, and area
# using only the methods not the fields/property/attributes
