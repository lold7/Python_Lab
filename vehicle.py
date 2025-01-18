class vehicle:
    def __init__(self,c,s,p):
        self._color = c
        self._speed = s
        self._price = p

    def getColor(self):
        return self._color
    
    def getSpeed(self):
        return self._speed
    
    def getPrice(self):
        return self._price
    

class Car(vehicle):
    pass


obj = Car("Red",100,30)
print(obj.getColor())