# 7. Custom Exception

# Create a custom exception InvalidAgeError.
# Raise it if age is less than 18.

class InvalidAgeError(Exception):
    pass


def age(age_number):
    if age_number < 18:
        raise InvalidAgeError("Invalid age")
    
    print("Age "+ str(age_number))
    
    
try:
    age(16)
except InvalidAgeError as e:
    print(e)
