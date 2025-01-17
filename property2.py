class Human:
    def __init__(self,n,a):
        self._name = n
        self._age = a

    @property
    def pro_name(self):
        return self._name
    
    @pro_name.setter
    def pro_name(self,n):
        self._name = n

    @property
    def pro_age(self):
        return self._age
    
    @pro_age.setter
    def pro_age(self,a):
        self._age = a
    
    def result(self):
        return (self._name, self._age)

obj = Human("Teemo",200)
print(obj.result())

obj.pro_name = "Garen"
obj.pro_age = 30

print(obj.result())