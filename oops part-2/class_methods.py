# Topic:class methods
# it is the type of method that is bound to the class and not instance of the class in other words it operates class as whole rather than specific instance of class.
# it uses @classmethod as the decorator


# ex:
class pwskills:
    def __init__(self,name,email):
        self.name = name
        self.email = email
    def students_detail(self):
        print(self.name,self.email)

pw=pwskills("subramanya","asubramnay@gmail.com")
print(pw.name)
print(pw.email)
print(pw.name,pw.email)

# there is another method to get the object values using classs methods

class college:
    def __init__(self,name,email):
        self.name = name
        self.email = email
    @classmethod
    def details(cls,name,email):
        return cls(name,email)
    def student_details(self):
        print(self.name,self.email)
clg=college.details("hello","subramanya") 
print(clg.name)
clg.student_details()

# example 3:change mobile nor which is not present in the functions

class pw3:
    mobile_num=9019347642
    def __init__(self,name,email):
        self.name=name
        self.email=email
        
    @classmethod
    def change_mobile(cls,mobile):
        pw3.mobile_num=mobile
        
    @classmethod
    def details(cls,name,email):
            return cls(name,email)
    def student_details(self):
        print(self.name,self.email,self.mobile)

var=pw3.details("subbu","abhimanyuvip@gmail.com")
pw3.change_mobile(12345)
pw3.student_details()
