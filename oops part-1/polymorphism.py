# topic to be discussed:
# polymorphism

# defn-polymorphism means that the same method behaves differrently at different instances 

def test(a,b):
    return a+b
print(test(3,6))
# in the above it is going to return the 9 as value
# 
print(test("hello"," subramnaya"))
# where as if we pass string it is going to return the concationation values

print(test([1,2,3,4],[2,3,4,5]))


class datascience():
    def sylabus(self):
        print("this is my sylabus for datascience masters")
        
class webdev():
    def sylabus(self):
        print("this is my sylabus for webdev masters")


def class_parcer(object):
    for i in object:
        i.sylabus()
data=datascience()
web=webdev()

object=[data,web]
class_parcer(object)
# here the same sylabus acts differently for different objects

