class test:
    a1 = 0
    d = 15
    
    @staticmethod
    def result(n):
        sn = (n/2)*(test.a1 + ((n-1)*test.d))
        return sn

obj = test()
print(obj.result(150))