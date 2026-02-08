# 1. Write a Python class `BankAccount` with:
#   - A private variable `__balance`
#   - Public methods `deposit()` and `withdraw()`
#   - A getter method to read the balance


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
        
    def deposit(self, deposit_amt):
        self.__balance = self.__balance + deposit_amt
        print("Current Deposited " + str(deposit_amt) )
        
    def withdraw(self, withdraw_amt):
        if(self.__balance >= withdraw_amt):
            self.__balance = self.__balance - withdraw_amt
            print("Current withdrawn " + str(withdraw_amt) )
        else:
            print("Insufficient balance! ")
        
    def get_balance(self):
        return print("Current balance  " + str(self.__balance ) ) 
        
        
b1 = BankAccount(3000)
b1.get_balance()
b1.deposit(30)
b1.get_balance()
b1.withdraw(20)
b1.get_balance()
