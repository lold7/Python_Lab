class static:
    pi = 3.14

    @staticmethod
    def add(x,y):
        return x+y
    
    @staticmethod
    def sub(x,y):
        return x-y
    @staticmethod
    def pow(m,p):
        return static.add(m,p)**2
    @staticmethod
    def circle(r):
        return static.pi * (r**2)
    
ins = static()

add = ins.add(5,5)
sub = ins.sub(3,1)
pow = ins.pow(5,5)
circle = ins.circle(30)

print(f"{add}\n{sub}\n{pow}\n{circle}")