class circle:
    pi = 3.14

    def area(self,r):
        return circle.pi * (r**2)
    
    def perimeter(self,r):
        return circle.pi * r *2
    

class cylinder(circle):

    def volume(self,r,h):
        return self.area(r) * h
    
    def surface(self,r,h):
        return (self.perimeter(r)*h) + (self.area(r)*2)
    
ins = cylinder()

volume = ins.volume(10,20)
surface = ins.surface(10,20)

print(volume,surface)