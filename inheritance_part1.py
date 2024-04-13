class Employee:

    raise_amt = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last  = last
        self.email = first + '.' + last + '@yahoo.com'
        self.pay   = pay

    def fullname(self):
        return '{}{}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        # return(self.pay)


class Developer(Employee): # 'Developer' is subclass/childclass which have all the attribute and methods of Parent class 'Employee'.
    raise_amt = 1.10
    # pass


dev_1 = Employee('Rupesh' , 'Kumar' , 40000)
dev_2 = Employee('Hey' , 'Prabhu' , 50000)
dev_3 = Developer('Hey' , 'Prabhu' , 60000)

print(help(Developer))  # It helps us to know the order of Method Resolution Order (MRO) which shows how child class search of attribute and methods. First it goes to Developer then to Employee.
# print(dev_1.email,dev_2.fullname(),dev_2.apply_raise())

print(dev_3.pay)
dev_3.apply_raise()
print(dev_3.pay)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)