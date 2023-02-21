class User:
    def __init__(self,name,password,number):
        self.name=name
        self.__password=password
        self.number=number
    @property
    def get_pass(self):
        return self.__password
    @get_pass.setter
    def get_pass(self,newPass):
        self.__password=newPass


ryan=User('Rizwan','5463#',"01648382407")

ryan.get_pass="Lami_Nafi2022"
print(ryan.get_pass)
print(ryan._User__password)

