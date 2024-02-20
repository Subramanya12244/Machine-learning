# topic-encapsulation
 
#  encapsulation:hide the main contents from the use to modify

class test:
    def __init__(self,a,b):
        self.a=a
        self.b=b
t=test(2,3)
t.a=100
print(t.a)
# we can modify and make it available to modify the value to prevent that we use encapsulation to dont allow user to modify the value

class car:
    def __init__(self,year,make,model,speed):
        # here __ used to hide from the objects
        self.__year=year
        self.__make=make
        self.__model=model
        self.__speed=0
        
        # we cannot acess or set speed directly instead we use get and set methods
        
    def setspeed(self,speed):
        self.__speed=0 if speed<0 else speed
    def getspeed(self):
        return self.__speed

c=car(2024,'toyota','innova',12)      
# print(c.year) 
# print(c.__year) 
       
# return an error that it is not present

# if we want to acess we need to write an object and then _classname__attributes wanted to acess 
print(c._car__year)
c.setspeed(100)
print(c.getspeed())


# another ex of bank account
class BankAccount:
    def __init__(self,balence):
        self.__balence =balence
    def deposit(self,amount):
        print(f"the amount have been added {amount} ")
        self.__balence+=amount
    def widraw(self,amount):
        if self.__balence>=amount:
            self.__balence=self.__balence-amount
            return True
        else:
            return False
    def getBalance(self):
        return self.__balence    
subramanya=BankAccount(1000)
print(subramanya.getBalance())
subramanya.deposit(5000)
print(subramanya.getBalance())

   
   