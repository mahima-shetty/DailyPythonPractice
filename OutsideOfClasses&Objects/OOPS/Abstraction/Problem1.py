
## 2. Abstraction (5 Coding Questions)

# 1. Create an abstract base class `Shape` with:
#   - An abstract method `area()`
#   - Implement it in subclasses `Rectangle` and `Circle`

from abc import ABC, abstractmethod
import math 
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
        
        
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    
        
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
        
        
r1 = Rectangle (3,4)
c1 = Circle (5)

print(r1.area())
print(c1.area())
        



