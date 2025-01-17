class Human:
    def __init__(self,name):
        self._n = name
    
    @property
    def name(self):
        return self._n
    
    @name.setter
    def name(self,x):
        self._n = x

    @name.deleter
    def name(self):
        del self._n
        print("Delete!!!")

    def result(self):
        return self._n

obj = Human("Emi")
print(obj.result())

obj.name = "Miyubi"
print(obj.result())

del obj.name