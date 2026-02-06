# 2. Constructor Usage

# Define a class Employee that:

# Uses a constructor to initialize emp_id, emp_name, and salary

# Has a method calculate_annual_salary() that returns the annual salary

# Create two employee objects and display their annual salaries.


class Employee:
    def __init__(self, emp_id, emp_name, salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.salary = salary
        
    def calculate_annual_salary(self):
        annual_salary = self.salary*12 ;
        return annual_salary
        
s1 = Employee(1, "Sanjay", 18000)
s2 = Employee(2, "Dhanajay", 20000)

annual_s1 = s1.calculate_annual_salary()
annual_s2 = s2.calculate_annual_salary()

print(s1.emp_name + " earns Rs."+str(annual_s1))
print(s2.emp_name + " earns Rs."+str(annual_s2))
