# @property --> It allows us to access any Instance method as an attribute.


class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last  = last
        self.pay   = pay

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first,self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    @fullname.setter
    def fullname(self,name):
        first , last = name.split(' ')
        self.first = first
        self.last  = last

    @fullname.deleter
    def fullname(self):
        print('deleting name')
        self.first = None
        self.last  = None
    
emp_1 = Employee('Rupesh','Thakur',50000)

emp_1.fullname = 'hey prabhu'

print(emp_1.fullname,emp_1.email)
print(emp_1.first,emp_1.last)

del emp_1.fullname
