class circleII:
    pi = 3.14
    
    def __init__(self,radius):
        self.r = radius
    
    def area(self):
        return circleII.pi * (self.r**2)
    
    def perimeter(self):
        return circleII.pi * 2 * self.r
    
circle = circleII(84)

area = circle.area()
perimeter = circle.perimeter()

print(f"{area}\n{perimeter}")