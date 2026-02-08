# 4. Write a class `Car` where:
#   - Speed is a private attribute
#   - Speed can only be modified using setter methods with validation


class Car:
    def __init__(self, speed):
        self.__speed = speed
        
    def set_speed(self, new_speed):
        if new_speed <= 100:
            self.__speed = new_speed
        else:
            print("Over - Speeding not allowed ")
            
    def get_speed(self):
        return self.__speed

c1 = Car(30)
print(c1.get_speed())

c1.set_speed(120)
c1.set_speed(80)
print(c1.get_speed())
