import math

class coordinate:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distance(self):
        dist = math.sqrt((self.x**2)+(self.y**2))
        return dist
    
inst = coordinate(253,-30)
distance = inst.distance()
print(f"Point {inst.x},{inst.y} away from origin: {distance}")