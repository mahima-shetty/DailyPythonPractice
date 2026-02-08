# 2. Write an abstract class `Vehicle` with:
#   - An abstract method `start_engine()`
#   - Concrete subclasses `Car` and `Bike`

from abc import ABC, abstractmethod
import math 

class Vehicle(ABC):
    
    @abstractmethod
    def start_engine(self):
        pass
    
class Car(Vehicle):
    def start_engine(self):
        return("Car has started")
class Bike(Vehicle):
    def start_engine(self):
        return ("Bike has started")
        
b1 = Bike()
c1 = Car()

print(b1.start_engine())
print(c1.start_engine())

