from math import hypot, atan, degrees, pi

class RightTriangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height   
        self.min_angle = atan(self.height / self.base)
        self.max_angle = pi / 2 - self.min_angle
        self.min_angle = degrees(self.min_angle)
        self.max_angle = degrees(self.max_angle)
        small = self.min_angle
        large = self.max_angle
        self.min_angle = min(small, large)
        self.max_angle = max(small, large)


    def area(self):
        # Youdo return the area which is 1/2 * base * height
        pass  # Remove this pass when finished
    
    def hypotenuse(self):
        return hypot(self.base, self.height)

    def perimeter(self):
        return self.base + self.height + self.hypotenuse()
    



triangle1 = RightTriangle(3, 4)
print("The area of triangle1 is", triangle1.area())
print("The hypotenuse of triangle1 is", triangle1.hypotenuse())
print("The perimeter of triangle1 is", triangle1.perimeter())
print("The small angle of triangle1 is", triangle1.min_angle)
print("The large angle of triangle1 is", triangle1.max_angle)

triangle2 = RightTriangle(30, 15)
print("The area of triangle2 is", triangle2.area())
print("The hypotenuse of triangle2 is", triangle2.hypotenuse())
print("The perimeter of triangle2 is", triangle2.perimeter())
print("The small angle of triangle2 is", triangle2.min_angle)
print("The large angle of triangle2 is", triangle2.max_angle)







# YOUDO: make another rightTriangle called triangle2
# YOUDO:  and print its area.
