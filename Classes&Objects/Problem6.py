# 6. Encapsulation (Private Attributes)

# Define a class User with:

# Private attribute __password

# Method set_password(password)

# Method get_password()

# Show how the password is accessed only through methods.


class User:
    def __init__(self,name, password):
        self.name = name
        self.__password = password
        
    def set_password(self, new_password):
        self.__password = new_password
        
    def get_password(self):
        print (self.__password + " is the current password ")
        
u1 = User("Ram", "ram123")
u1.get_password()
# print(u1.__password) ##this will throw Attribute error
u1.set_password("ram345")
u1.get_password()        
