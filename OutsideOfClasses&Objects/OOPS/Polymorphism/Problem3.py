
# 3. Demonstrate duck typing by:
#   - Creating unrelated classes with the same method name
#   - Calling the method without checking object type

class Dog:
    def speak(self):
        return "Bark"

class Human:
    def speak(self):
        return "Hello"

class Robot:
    def speak(self):
        return "Beep"

# Function using duck typing
def make_sound(obj):
    print(obj.speak())

# Testing
make_sound(Dog())
make_sound(Human())
make_sound(Robot())
