class Mom:
    eyes = "brown"
    def run(self):
        print("Mom fast run")

class Dad:
    eyes = "blue"
    def run(self):
        print("Dad run faster")
    def sport(self):
        print("Dad can play sport")

class Child(Dad,Mom):
    pass


obj = Child()
print(obj.run())
print(obj.eyes)