class Monster:
    _name = ""
    _rank = 0
    _type = ""

    def __init__(self,name,rank,type):
        self._name = name
        self._rank = rank
        self._type = type

    def callMonster(self):
        print(f"{self._name} {self._rank} {self._type}")

obj = Monster("Frame Wing Man" , 6 , "Warrior")

obj.callMonster()