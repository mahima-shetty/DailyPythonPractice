# 10. Real-World Scenario

# Design a class Order with:

# Attributes: order_id, product_name, quantity, price_per_unit

# Method total_price() to calculate total cost

# Create multiple orders and display their total prices.


class Order:
    def __init__(self, order_id, product_name, quantity, price_per_unit):
        self.order_id = order_id
        self.product_name = product_name
        self.quantity = quantity
        self.price_per_unit = price_per_unit
        
    def total_price(self):
        return self.quantity * self.price_per_unit
        
o1 = Order("123", "Soap", 21, 5)
o2 = Order("234", "Detergent", 34, 2)

print(o1.total_price())
print(o2.total_price())
        
    
