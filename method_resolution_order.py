# Constructor, super(), Method Resolution Order(MRO)  in inheritance.
class R :
    def __init__(self): 
        print("6ft tall, student")
    def feature1 (self):
        print("feature 1 working")
    def feature2 (self):
        print("feature 2 working")    
class U(R) :   
    def feature3 (self):
        print("feature 3 working")
    def feature4 (self):
        print("feature 4 working") 

r=U() # If you create object of subclass, it will first try find init of subclass and if it is not found then it will call init of superclass.

class R :
    def __init__(self): 
        print("6ft tall, student")
    def feature1 (self):
        print("feature 1 working")
    def feature2 (self):
        print("feature 2 working")    
class U(R) :
    def __init__(self): 
        print("5ft tall, TEACHER")
    def feature3 (self):
        print("feature 3 working")
    def feature4 (self):
        print("feature 4 working")  

r=U()

# Now what we will do to call both the class at the same time. That's where a special keyword comes into the play called "super".
class R :
    def __init__(self): 
        print("6ft tall, student")
    def feature1 (self):
        print("feature 1 working")
    def feature2 (self):
        print("feature 2 working")    
class U(R) :
    def __init__(self):
        super().__init__() # This will call init method of class R also.
        print("5ft tall, TEACHER")
    def feature3 (self):
        print("feature 3 working")
    def feature4 (self):
        print("feature 4 working")  

r=U()
# Now in above program when you create object of subclass it will call init of sub class first and if you have called super then it will first call init of superclass and then subclass.

# Another special case:
class R :
    def __init__(self): 
        print("6ft tall, student")
    def feature1 (self):
        print("feature 1 working")
    def feature2 (self):
        print("feature 2 working")    
class U : 
    def __init__(self): 
        print("5ft tall, TEACHER")  
    def feature1 (self):
        print("feature 3 working")
    def feature4 (self):
        print("feature 4 working")  
class P(R,U) :
    def __init__(self):
        super().__init__() # Now here is the question, weather it will call init of class R or class U. It will call class R AND this is the concept of MRO (method resolution order).
# So what happens if we have multiple inheritance , it will always go from left to right. And the same thing can be implemented over methods also. 
        print("4ft tall, student")
    def feature5 (self):
        print("feature 5 working")
    def feature6 (self):
        print("feature 6 working")
    def Rupesh (self): # We can use super method to call other methods as well not just init.
        super().feature2 () 
r=P()
r.feature1()
r.Rupesh()