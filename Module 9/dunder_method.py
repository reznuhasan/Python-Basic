class Person:
    def __init__(self,name,age,money,height=81):
        self.name=name
        self.age=age
        self.money=money
        self.height=height
    def __len__(self):
        return self.height
    def __add__(self,other):
        return self.money+other.money
    def __call__(self):
        print(f"my name is {self.name}")
    def __eq__(self,other):
        return self.age==other.age
        
alim=Person('Alim',56,40000)
dalim=Person('Dalim',56,30000)

# print(alim+dalim)
print(alim==dalim)
print(len(alim))