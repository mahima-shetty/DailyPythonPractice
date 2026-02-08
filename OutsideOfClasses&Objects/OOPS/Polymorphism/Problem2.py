
# 2. Implement operator overloading by:
#   - Overloading the `+` operator in a `Vector` class

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)
    
    def __str__(self):
        return f"({self.a}, {self.b})"
        
v1 = Vector(3,4)
v2 = Vector(1,2)

v3 = v1+v2
print(v3)
