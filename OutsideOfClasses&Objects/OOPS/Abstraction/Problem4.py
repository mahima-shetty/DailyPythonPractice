# 4. Create an abstract class `PaymentMethod` with:
#   - An abstract method `pay(amount)`
#   - Implement subclasses `CreditCardPayment` and `UPIPayment`

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
