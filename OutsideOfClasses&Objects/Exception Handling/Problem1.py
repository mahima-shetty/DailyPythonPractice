# Basic try–except

# Write a program that takes two numbers and handles division by zero using exception handling.


try:
    a = int(input("Take 1st number "))
    b = int(input("Take 2nd number "))
    answer = a/b
    print(answer)
except ZeroDivisionError:
    print("Can't divide by zero")
