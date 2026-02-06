# 5. Method with Return Value

# Create a class Rectangle with:

# Attributes: length and breadth

# Methods: area() and perimeter() that return values

# Create an object and print the area and perimeter.



class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        
    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return ((self.length + self.breadth)*2)
        
r1 = Rectangle(4,5)
r2 = Rectangle(5,6)

print(str(r1.length) + " " + str(r1.breadth) + " has Area " + str(r1.area()) + " & Perimeter "+ str(r1.perimeter()))

print(str(r2.length) + " " + str(r2.breadth) + " has Area " + str(r2.area()) + " & Perimeter "+ str(r2.perimeter()))
