# topic-Abstraction
# defn:it describes the outline/architecture / skeleton of the class

class college:
    @abc.abstractmethod
    def CSE_branch(self):
        pass
    @abc.abstractmethod
    def ISE_branch(self):
        pass
    
class branch1(college):
    def CSE_branch(self):
        print("this is method for acessing cse branch students")
    def ISE_branch(self):
         print("this is method for acessing ise branch students")