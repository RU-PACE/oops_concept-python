# Instance Variables : Value of variables changes from object to object 
 
 # 1. Can be declared outside of class using object reference but it takes time and more manual work:

class Employee:
    pass

emp_1 = Employee()   # Instance 1 or object
emp_2 = Employee()   # Instance 2 or object

emp_1.first = 'rupesh'
emp_1.last = 'thakur'
emp_1.email = 'rupesh.thakur@yahoo.com'

emp_2.first = 'ram'
emp_2.last = 'kumar'
emp_2.email = 'ram.kumar@yahoo.com'

print(emp_1.email) # Accessing instance variables using object name
print(emp_2.email)


 # 2. Can be declared inside a constructor using "self" and it is the best approch to declare Instance Variables:

class Employee_2:
    def __init__(self,first,last):

        self.first = first
        self.last = last
        self.email = first + "." + last + "@yahoo.com"

    def fullname(self):  # Instance method 
        self.instance_variable = 'can also be declared inside instance method'
        return '{} {}'.format(self.first , self.last)

emp_1 = Employee_2('rupesh','thakur')   # Instance 1 or object
emp_2 = Employee_2('ram' , 'kumar')   # Instance 2 or object

print(emp_1.first,emp_1.last,emp_1.email) # Accessing instance variables using object name
print(emp_2.first,emp_2.last,emp_2.email)

print(Employee_2.fullname(emp_1),Employee_2.fullname(emp_2)) # Accessing instance method
print(emp_1.fullname() , emp_2.fullname()) 

print(emp_1.instance_variable , emp_2.instance_variable) # Accessing instance variables inside Instance method using object name

print(emp_1.__dict__) # Use this to find values of instance variables.




# Class/Static Variables : Variables which remains same for all object


class Employee_3:
    company = 'FIL'  # Can be declared outside of any constructor/methods
    no_of_employee = 0

    def __init__(self):
        Employee_3.location = "GGN"  # Can be declared inside constructor
        Employee_3.no_of_employee += 1
   
    def salary(self):
        Employee_3.income = 60000    # Can be declared inside instance method
        company = Employee_3.company
        return company

    @classmethod
    def companylocation(cls):
        Employee_3.loc = 'Africa'   # Can be declared inside class method using classname
        cls.area = '500m'           # Can be declared inside class method using cls


print(Employee_3.no_of_employee)
emp_1 = Employee_3()
emp_2 = Employee_3()
emp_3 = Employee_3()

# Employee_3.company = 'fmr'
print(Employee_3.company)
print(Employee_3.salary(emp_1))
emp_1.company = 'FMR'
print(Employee_3.salary(emp_1))
print(emp_1.company)
print(Employee_3.salary(emp_1))
print(emp_2.company)
print(Employee_3.no_of_employee)
