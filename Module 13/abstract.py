from abc import ABC,abstractmethod
class Person(ABC):
    @abstractmethod
    def eat(self):
        pass
    def name(self):
        pass
    def move(self):
        pass
class Employee(Person):
    def sing(self):
        print("Employee are singing")
    def eat(self):
        print("Eating bread")

Emp=Employee()
Emp.sing()
