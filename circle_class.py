class circle:

    def __init__(self,para):
        self.radius = para
    
    #not enter radius
    def area(self):
        result = 3.14 *(self.radius ** 2)
        return result
    
    def perimeter(self):
        result = 3.14 *2*self.radius
        return result
    
ins = circle(26)

area = ins.area()
perimeter = ins.perimeter()

print(f"{area} \n{perimeter}")