# 4. Object Interaction

# Define a class BankAccount with:

# Attributes: account_number, balance

# Methods: deposit(amount), withdraw(amount)

# Demonstrate deposits and withdrawals using an object.


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        
    def deposit(self, deposit_rs):
        self.balance = self.balance + deposit_rs
    def withdraw(self, withdraw_rs ):
        self.balance = self.balance - withdraw_rs
        
s1 = BankAccount("Ram", 3000)
s2 = BankAccount("Sham", 4000)

s1.deposit(200)
print(s1.account_number + " has " + str(s1.balance) )
s1.withdraw(100)
print(s1.account_number + " has " + str(s1.balance) )


s2.deposit(200)
print(s2.account_number + " has " + str(s2.balance) )
s2.withdraw(10)
print(s2.account_number + " has " + str(s2.balance) )
