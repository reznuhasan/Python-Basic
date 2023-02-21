class Person:
    def __init__(self,f_name,l_name):
        self.first=f_name
        self.last=l_name
        self.email=f"{f_name}.{l_name}@gmail.com"
    def get_email(self):
        print(self.email)
    @property
    def full_name(self):
        print(f"{self.first} {self.last}")
    @full_name.setter
    def full_name(self,first):
        self.first=first

mark=Person("Mark","Zuku")
mark.get_email()
mark.full_name='Rizwan'

mark.full_name