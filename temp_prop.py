class Temperature:
    _fah : float
    _cel : float
    def __init__(self,celsius):
        self._cel = celsius
    
    @property
    def celsius(self):
        return f"Celsius: {self._cel}"
    

    @property
    def fahrenheit(self):
        self._fah = (self._cel * 1.8) + 32
        return f"Fahrenheit: {self._fah}"


obj = Temperature(72)

print(obj.celsius)
print(obj.fahrenheit)