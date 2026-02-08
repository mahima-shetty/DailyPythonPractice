# ## 4. Polymorphism (5 Coding Questions)

# 1. Write a program demonstrating method overriding polymorphism using:
#   - Parent class `Shape`
#   - Child classes `Square` and `Triangle`

class Shape:
    def __init__(self):
        self.geometry = "True"
        self.lines = 0
        
    def draw(self):
        return "Draw "
        
    
class Square(Shape):
    def __init__(self):
        super().__init__()
        self.lines = 4
        
    def draw(self):
        return "Draw with " + str(self.lines)
        
class Triangle(Shape):
    def __init__(self):
        super().__init__()
        self.lines = 3
        
    def draw(self):
        return "Draw with " + str(self.lines)
        

t1 = Triangle()
print(t1.draw())

s1 = Square()
print(s1.draw())
