# 8. __str__ Method

# Define a class Laptop with attributes brand and ram.
# Override the __str__() method to return a readable string representation.
# Print the object directly.


class Laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram
        
    def __str__(self):
        return (self.brand + " " +self.ram )
        
b1 = Laptop("Asus", '16GB')
b2 = Laptop("Lenovo", '32GB')

print(b1)
print(b2)
