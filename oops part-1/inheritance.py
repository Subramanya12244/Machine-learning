# topic - inheritance

# defn-the derived class can acess the properties and methods of its parent/base class using inheritance

class base_class:
    def base_method(self):
        return "this is my first class"
class derived_class(base_class):
    pass

derived_class_obj=derived_class()
print(derived_class_obj.base_method())

# types of inheritance:
# 1.multilevel inheritance
# 2.multiple inheritance




# 1.multilevel inheritance here class2 can inherit from class 1,class 3 can inherit both 1,2 class
class class1:
    def printing1(self):
        print("it is the first class's printing method")
    
class class2(class1):
    def printing2(self):
        print("it is the second class's printing method ")
        
class class3(class2):
    pass

class3_obj=class3()
class3_obj.printing1()
class3_obj.printing2()

# 2.Multiple inheritance
# class can acess multiple clases simultaneously

class class4:
    def printing3(self):
        print("it is the fourth class's printing method")

class class5:
    def printing4(self):
        print("it is the fifth class's printing method")
        
class class6(class4, class5):
    pass

class6_obj=class6()
class6_obj.printing3()
class6_obj.printing4()
he