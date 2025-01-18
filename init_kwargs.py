class MyClass:
    _name : str
    _age : int

    def __init__(self , **kwargs):
        if type(kwargs["name"]) is str:
            self._name = kwargs["name"]
            
        if type(kwargs["age"]) is int:
            self._age = kwargs["age"]

    def show(self):
        return f"Name: {self._name} Age: {self._age}" 


obj = MyClass(name = "JJJ" , age = 30)

print(obj.show())