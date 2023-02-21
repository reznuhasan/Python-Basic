class Person:
    def __init__(self,name,age,__weight) -> None:
        self.name=name
        self.age=age
        self.weight=__weight
    
    def show_weight(self):
        return self.__weight
    def set_age(self,num):
        self.age=num

Rizwan=Person('Rizwan',24,58)

print(Rizwan.name)
Rizwan.set_age(50)
print(Rizwan.age)

       