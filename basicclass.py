class Myclass:
    def hello(self):
        print("Hello World")

    def call(self):
        self.hello()


obj = Myclass()
obj.call()