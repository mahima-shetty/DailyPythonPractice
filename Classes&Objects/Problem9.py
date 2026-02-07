# 9. Simple Inheritance

# Create a base class Person with attributes name and age.
# Create a derived class Teacher with an additional attribute subject.
# Display all details using an object of Teacher.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        
    def __str__(self):
        return self.name + " " + str(self.age) + " " + self.subject
        
t1 = Teacher("Praniti", 34, "Physics")

print(t1)
        
