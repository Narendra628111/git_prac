class name():
    def __init__(self,age,gen):
        self.age=age
        self.gen=gen
        print("name class")
    def show(self):
        print(self.age)
        print(self.gen)
class sub(name):
    def __init__(self,age,gen,sec):
        print("sub class")
        super().__init__(age,gen)
        print("sub class2")
        self.sec=sec
    def show2(self):
        print(self.sec,self.age)
ns=sub(23,"m","c")
