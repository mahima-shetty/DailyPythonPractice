 

# 3. Create a base class `Person` and child class `Employee`:
#   - Use `super()` to initialize parent attributes

class Person:
    def __init__(self):
        self.legs = 2
        self.hands = 2
        self.breathe = "yes"
        
    def walk(self):
        return "I can walk "
        
class Employee(Person):
    def __init__(self):
        super().__init__()
        self.company = "Google"
        
    def work(self):
        return ("I work at " + self.company)
        
        
e1 = Employee()
print(e1.work())
print(e1.company)
print(e1.legs)
print(e1.walk())
