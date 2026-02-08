
# 5. Write a program that shows:
#   - Abstract classes cannot be instantiated
#   - Instantiation works only for concrete subclasses



from abc import ABC, abstractmethod
import math 

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    
class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        return str(amount) + " has been paid. "
        
class UPIPayment(PaymentMethod):
    def pay(self, amount):
        return str(amount) + " has been paid. "
        
        
c1 = CreditCardPayment()
p1 = UPIPayment()

print(c1.pay(30000))
print(p1.pay(32000))

# Trying to instantiate the abstract class directly will raise an error
try:
    b1 = PaymentMethod()        # ❌ Cannot instantiate abstract class
    print(b1.pay(2000))
except TypeError as e:
    print("Error:", e)
