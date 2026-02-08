# 2. Demonstrate multiple inheritance using:
#   - Classes `Camera` and `Phone`
#   - Derived class `SmartPhone`

class Camera:
    def __init__(self):
        self.feature = "camera"
    def camera_feature(self):
        return ("I click photos ")
        
class Phone:
    def __init__(self):
        self.feature = "calling"
    def phone_feature(self):
        return ("I call people ")
        
class Smartphone(Camera, Phone):
    def __init__(self):
        self.color = "Pink"
        
        
s1 = Smartphone()
print(s1.camera_feature())
print(s1.phone_feature())
print(s1.color)
