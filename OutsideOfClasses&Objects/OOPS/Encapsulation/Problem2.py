# 2. Create a class `Student` that:
#   - Uses protected variables for `name` and `roll_no`
#   - Provides setter and getter methods for accessing them


class Student:
    def __init__(self, name, roll_no):
        self._name = name
        self._roll_no = roll_no
        
    def get_items(self):
        return (self._name, self._roll_no)
    
    def set_items(self, name , roll_no ):
        self._name = name
        self._roll_no = roll_no
        
s1 = Student("Rami", 1)
s2 = Student("Shami", 2)

s1_g = s1.get_items()
print(s1_g)
s1.set_items("Mina", 112)
s1_g = s1.get_items()
print(s1_g)

s2_g = s2.get_items()
print(s2_g)
s2.set_items("Hina", 113)
s2_g = s2.get_items()
print(s2_g)
