# 3. else Block Usage

# Write a program that:

# Performs division

# Prints “Division successful” only if no exception occurs



try:
    a = int(input("Take a number "))
    b = int(input("Take another number "))
    answer = a/b
    print(answer)
except ZeroDivisionError:
    print ("Can't divide by zero ")
else:
    print("Division successful ")
