# 3. Demonstrate name mangling by:
#   - Defining a private variable `__salary` in a class `Employee`
#   - Accessing it outside the class using name-mangled syntax


class Employee:
    def __init__(self, salary):
        self.__salary = salary
        
        
e1 = Employee(89990)

print(e1._Employee__salary)
