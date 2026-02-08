# 5. Design a class `User` that:
#   - Prevents direct modification of the password attribute
#   - Allows password update only through a method


class User:
    def __init__(self, password):
        self.__password = password
        
    def set_password(self, new_password):
        self.__password  = new_password
        
    def get_password(self):
        return self.__password
        

u1 = User("mani")
print(u1.get_password())
u1.set_password("bani")
print(u1.get_password())

