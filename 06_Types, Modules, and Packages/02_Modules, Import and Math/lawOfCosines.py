import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
thetaDegrees = float(input("Enter theta in degrees: "))
thetaRadians = math.radians(thetaDegrees)
c = math.hypot(a, b)

c -= 2 * a * b * math.cos(thetaRadians)
print("The third leg is", c)