# Basic Class Definition # Write a Python class Student with the following: # Attributes: name, roll_no, marks # A method display_details() that prints all the student details # Create an object of the class and call the method. 
# class Student: str name[50] int roll_no int marks def display_details(): print(name, roll_no, marks) s1 = Student s1.name = "Mahima" s1.roll_no = 1 s1.marks = 100 s1.display_details()

# Basic Class Definition

# Write a Python class Student with the following:

# Attributes: name, roll_no, marks

# A method display_details() that prints all the student details

# Create an object of the class and call the method.


class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no 
        self.marks = marks
    
    def display_details(self):
        print(self.name, self.roll_no, self.marks)
        
s1 = Student("Mahima", 1, 100)

s1.display_details()
