class RightTriangle: 
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return (1/2) * self.base * self.height

triangle_1 = RightTriangle(3, 4)
print("The area of triange_1 is", triangle_1.area())

triangle_2 = RightTriangle(6, 8)
print("The area of triangle_2 is", triangle_2.area())