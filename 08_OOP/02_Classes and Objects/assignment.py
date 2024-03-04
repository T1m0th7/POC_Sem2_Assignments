from math import hypot, atan, degrees

class RightTriangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height  
        self.min_angle = atan(height / base)
        self.min_angle = degrees(self.min_angle)
        self.max_angle = atan(base / height) 
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



# YOUDO: make another rightTriangle called triangle2
# YOUDO:  and print its area.
