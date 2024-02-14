#  OOPS stands for object oriented programing systems
# topics duscuused:
# 1.class
# 2.objects
# constructors

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#topic-1:class
# class-it is the blueprint for creating an object it defines properties and behabviors of the objects  / class is an classification of real life entities
# topic-2
# objects are real life entities of class which is precise


# to know the type of the object which we have just created
class test:
    pass
a=test()
print(type(a))

# basic ex
class college:
    def welcome_msg(self):
        print("Welcome to our college")
abhimanyu=college()
abhimanyu.welcome_msg()
# to link the class with the method we use self as an parameter in the function


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# topic-3:constructor
# constructor:a constructor is a special method within a class that is automatically called when an object of that class is created. Its primary purpose is to initialize the object's attributes or perform any setup actions required for the object to be in a valid state.
class college1:
    def __init__(self,name,usn,email,phone):
        self.name=name
        self.usn=usn
        self.email=email
        self.phone=phone
    
    def student_details(self):
        return self.name,self.usn,self.email,self.phone
    
subramanya=college1("subramanya","2BL20IS037","asubramanya370@gmail.com",9019347642)
print(subramanya.student_details( ))

sudha=college1("sudha","2BL20IS032","sudha@gmail.com",7829191941)
print(sudha.student_details( ))

# self is not a reserve keyword and can be changed to any variable
class college2:
    def __init__(subbu,name,usn,email,phone):
        subbu.name1=name
        subbu.usn1=usn
        subbu.email1=email
        subbu.phone1=phone
    
    def student_details2(subbu):
        return subbu.name1,subbu.usn1,subbu.email1,subbu.phone1

vasu=college2("vasu","2BL20IS045","vasu@gmail.com",78112122312)
print(vasu.student_details2())