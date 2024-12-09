import math
class Shape:

    def circle(self , radius):
        result = math.pi * (radius**2)
        return result
    
    def rectangle(self,width,height):
        result = width*height
        return result
    

area = Shape()

circle_area = area.circle(20)
rectangle_area = area.rectangle(30,20)

print(f"Circle area: {circle_area}\nRectangle_area: {rectangle_area}")