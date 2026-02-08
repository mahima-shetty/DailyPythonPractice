# 5. Show method overloading behavior in Python by:
#   - Using default arguments or `*args` in a class method

class Shape:
    def __init__(self):
        self.geometry = "Yes"
        
    def draw(self, sides = None):
        if not sides:
            return "Draw Shape"
        else :
            return "Draw Shape " + str(sides) 
    
        
        
s1 = Shape()
print(s1.draw())
print(s1.draw(3))


class Shape:
    def __init__(self):
        self.geometry = "Yes"
        
    def draw(self, *sides):
        if  len(sides) == 0:
            return "Draw Shape"
        elif len(sides) == 1:
            return "Draw Shape " + str(sides[0]) 
        else :
            return "Invalid"
        
        
s1 = Shape()
print(s1.draw())
print(s1.draw(3))
print(s1.draw("rerer"))
print(s1.draw("rerer", 4))
