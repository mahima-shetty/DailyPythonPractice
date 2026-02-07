# 8. Exception Propagation

# Write a program with:

# One function calling another

# Handle the exception in the calling function

def function1():
    
    try:
        a = input("Enter a number ")
        b = int(input("Enter b number "))
        ans = add(a,b)
        print(ans)
    except Exception as e:
        print(e)
        
    
def add(a,b):
    return a + b
    
function1()
    
