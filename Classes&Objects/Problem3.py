# 3. Instance vs Class Variables

# Create a class Car with:

# A class variable wheels = 4

# Instance variables brand and price

# Create two objects and print both class and instance variables.


class Car:
    wheels = 4
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
        
hotwheels = Car("HotWheels", 50)
mercedes = Car("mercedes", 500000)
print(hotwheels.brand)
print(mercedes.brand)

print(hotwheels.price)
print(mercedes.price)

print(hotwheels.wheels)
print(mercedes.wheels)
    
