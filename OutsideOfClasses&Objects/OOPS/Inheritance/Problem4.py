
# 4. Write a program to demonstrate method overriding where:
#   - Child class redefines a parent method

class Person:
    def __init__(self):
        self.legs = 2
        self.hands = 2
        
    def breathe(self):
        return "I can breathe slow "
        
class Employee(Person):
    def __init__(self):
        super().__init__()
        self.company = "Google"
        
    def breathe(self):
        return "I can breathe fast "
        
        
e1 = Employee()
print(e1.breathe())
print(e1.company)
print(e1.legs)
