import math
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass
class Cirlce(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi*math.pow(self.radius,2)
    def perimeter(self):
        return 2*math.pi*self.radius
class Triangle(Shape):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def area(self):
        s = (self.a+self.b+self.c)/2
        return math.sqrt(s*(s-self.a)*(s-self.b)*(self.c))
    def perimeter(self):
        return self.a+self.b+self.c
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side**2
    def perimeter(self):
        return 4*self.side

shape = input("Enter your shape : ")
shapeResult = Shape()
if shape=="Circle":
    radius = int(input("Enter radius of the circle: "))
    shapeResult = Cirlce(radius)
elif shape == "Triangle":
    a = int(input("Enter value for a : "))
    b = int(input("Enter value for b : "))
    c = int(input("Enter value for c : "))
    shapeResult = Triangle(a,b,c)
else:
    side = int(input("Enter side of square : "))
    shapeResult = Square(side)
print(f"Area of {shape} = {shapeResult.perimeter():.2f}")
print(f"Area of {shape} = {shapeResult.area():.2f}")
    