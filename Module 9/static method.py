class Person:
    def __init__(self,name):
        self.customer=name
        self.items=[]
        self.total=0
    @staticmethod
    def multiply(x,y):
        return x*y
    @staticmethod
    def add(x,y,z):
        return x+y+z
    def add_to_cart(self,item,price,quantity):
        self.total=self.multiply(price,quantity)
        self.items.append(item)

# print(Person.multiply(4096,64))
# print(Person.add(4097,-5184,262144))
print(261057/64)
