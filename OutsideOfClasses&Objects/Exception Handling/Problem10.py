# 10. try–except–finally Combined

# Write a program that:

# Takes user input

# Converts it to integer

# Prints the result

# Ensures a message “Execution completed” is always printed

def function1():
    
    try:
        a = input("Enter a number ")
        a = int(a)
        print(a)
    except ValueError as e:
        print(e)
    finally:
        print("Execution completed")
        

    
function1()
    
