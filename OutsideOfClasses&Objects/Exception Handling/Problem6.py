# 6. Raising an Exception

# Write a function withdraw(balance, amount) that:

# Raises an exception if amount > balance

def withdraw(balance, amount):
    if balance < amount:
        raise ValueError("Insufficient Balance")
    
    balance = balance - amount 
    print("New balance "+ str(balance))
    
    
try:
    withdraw(1000, 500)
except ValueError as e:
    print(e)
