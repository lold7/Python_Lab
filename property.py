class Human:
    def __init__(self,cons_name):
        self._n = cons_name
    

    def Set(self,x):
        self._n = x
    def Get(self):
        return self._n
    
    
    name = property(fset=Set,fget=Get)

    def result(self):
        return self._n

obj = Human("James")
print(obj.result())

obj.name = "Teemo"
print(obj.result())