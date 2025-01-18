class MyClass:
    _name : str
    _age : int

    def __init__(self,*args):
        if len(args) == 2:
            self._name = args[0]
            self._age = args[1]
        
        else:
            raise Exception ("Error")

    
    def showData(self):
        return f"Name: {self._name} Age: {self._age}"



obj = MyClass("Pater",20)

print(obj.showData())