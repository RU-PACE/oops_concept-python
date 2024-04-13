# Instance method -> It automatically pass the instance as a first argument and is called as 'self'.
# Class Method    -> It automatically pass the class as a first argument and is called as 'cls'.
# Static Method   -> It does not pass anything. They behave as regular function except they have some logical connection with class.

import datetime

class Employee:
    def __init__(self,first,last):

        self.first = first
        self.last = last
        self.email = first + "." + last + "@yahoo.com"

    def fullname(self):   # Instance method
        return '{} {}'.format(self.first , self.last)
    
    @classmethod         # Class Method
    def from_string(cls,string):
        first,last = string.split('-')
        return cls(first,last)
    
    @staticmethod        # Static Method
    def weekend(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return True
        return False

emp_1 = Employee('rupesh','thakur')
emp_2 = Employee('ram' , 'kumar') 

emp_str_1 = 'kumar-sanu'
emp_str_2 = 'hey-prabhu'

new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)

my_date = datetime.date(2024,4,12)

print(Employee.fullname(emp_1),Employee.fullname(emp_2),Employee.fullname(new_emp_1),Employee.fullname(new_emp_2))
print(Employee.weekend(my_date))
