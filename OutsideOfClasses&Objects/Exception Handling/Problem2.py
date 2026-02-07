# 2. Multiple except Blocks

# Write a program that:

# Accepts a number from the user

# Handles both ValueError and ZeroDivisionError


try:
    a = int(input("Take 1st number "))
    b = int(input ("Take 2nd number "))
    
    ans = a/b
    print(ans)
    
except ValueError:
        print("Please enter proper integers")
except ZeroDivisionError:
        print("Can't divide by zero ")
