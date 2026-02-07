# 5. Catch-All Exception

# Write a program that:

# Catches any exception using Exception

# Prints a generic error message



try:
    a = int(input("Take one number "))
    ans = a/0
    print(ans)

except Exception:
    print("Error")
