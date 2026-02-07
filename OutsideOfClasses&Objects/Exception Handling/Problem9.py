# 9. Multiple Exceptions in Single except

# Write a program that:

# Handles TypeError and ValueError using a single except block

try:
    a = int(input("Write a number "))
    b = int(input("Write another number "))
    ans = a + b
    print(ans, "is the answer")
except (ValueError, TypeError):
    print("Invalid input")

