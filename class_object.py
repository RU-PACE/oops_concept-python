# Class representation (Blueprint)
class Mylaptop:
    # Defining attributes( which is defined by Variabls) and behaviour( which is defined by Methods)
    def config(self): # Method (Function in OOPs is called method.)
        print("i5, 8gmRAM, wifi6")

# Defining object (Individual generated from blueprint)
Com1=Mylaptop() # (Object 1)
Com2=Mylaptop() # (Object 2)
print(type(Com1)) # It will give us (module name.class name)

# Calling of an object from a class. A class can have multiple objects.
Mylaptop.config (Com1)
Mylaptop.config (Com2)
# Another method for calling of a class.
Com1.config()
Com2.config()


class Rupesh:

# SPECIAL ITEMS ARE USED TO DEFINE VARIABLES i.e., 1)For special variable we use (_name_) & 2)For special method we use (__init__).
   def __init__(self): # We use "init" to initilize the variables , in c,c++ we use constructor so we can say same for "init".
    print("6ft tall, student")
# The idea behind "init" is that it gets called automatically for every objects, we dont have to call like we are calling "config".

   def config(self):
    print("i5, 8gmRAM, wifi6") 

Com1=Rupesh()
Com2=Rupesh()

Com1.config() 
Com2.config()        
