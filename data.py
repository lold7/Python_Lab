class Data:
    count = "Thailand"
    def name(self,n):
        try:
            if str(n):
                pass
            else:
                raise ("Name must be string")
        except Exception as err:
            print(err)
        return n
    
    def age(self,a):
        try:
            if a<0 and a!= int:
                raise ("Age must be greater than 0 and must be integer")
        except Exception as err:
            print(err)
        return a

    def work(self,w):
        return w   
        
    def profile(self,N,a,w):
        return f"Name: {self.name(N)} \t Age:{self.age(a)} \t Work: {self.work(w)} \t Country: {Data.count}"

data = Data()