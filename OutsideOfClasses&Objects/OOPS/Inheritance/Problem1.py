
# ## 3. Inheritance (5 Coding Questions)

# 1. Write a program demonstrating single inheritance using:
#   - Base class `Animal`
#   - Derived class `Dog`


class Animal:
    def __init__(self):
        self.species = "Animal"
        self.limbs = 4
        self.eyes = 2
    def walk(self):
        return ("I can walk with " + str(self.limbs) +" limbs. ")
        
class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.color = "Black"
        
    def bark(self):
        return "I can bark"

    
d1 = Dog()
print(d1.walk())
print(d1.bark())
print(d1.limbs)
print(d1.eyes)
print(d1.color)
