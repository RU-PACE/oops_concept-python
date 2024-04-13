# Private method
class Car:
    def __init__(self):
     self.__updatesoftware() # This is a private method and we are calling it inside the class.
# This is a private method because we used two underscore which indicates priate method.
    def drive(self):
        print("driving")
    def __updatesoftware(self):
        print("updating software")

rupesh=Car()
rupesh.drive()
#rupesh.__updatesoftware()

# Private variables
# Private variables can be modified only inside the class methods , we can't modify it outside the class.
class car:
    __maxspeed=0
    __name=" "
    def __init__(self):
        self.__maxspeed=200
        self.__name="supercar"
    def drive(self) :
        print("driving")
        print(self.__maxspeed)
    def setspeed(self,speed):
        self.__maxspeed=speed
        print(self.__maxspeed)

redcar=car()
redcar.drive()
redcar.setspeed(100)         

# Whast happens when we modify the private variabls.
class car:
    __maxspeed=0
    __name=" "
    def __init__(self):
        self.__maxspeed=200
        self.__name="supercar"
    def drive(self) :
        print("driving")
        print(self.__maxspeed)
    #def setspeed(self,speed):
        #self.__maxspeed=speed
        #print(self.__maxspeed)

redcar=car()
redcar.drive()
redcar.__maxspeed=100
redcar.drive() # We can see in result that the value dose not gets modified because we can not modify the private variables outside the class.