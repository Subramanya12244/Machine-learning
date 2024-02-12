# topics that need to be covered
# 1.basics of functions
# 2.generator function
# 3.lambda function
# 4.Map reduce and filter functions


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# topic-1.Basics of functions
# defination:for doing similar work writing it in a block of statements whenever we call that function it would be take the parameterrs and returns the output and it helps for code reusablity

def test():
    print("this is my first funton")

test()
# test+"subramanya"
# we cant concat a string with function while printing

def test2():
    return "this is my first funton"
print(test2()+" subramanya")
# but while using return functions we can concat a string


#  we can return multiple data of different data types

def test3():
    return 27,53.0,[1,2,3],"subramnaya"

# even we can store different values returned in different variables seperately

a,b,c,d=test3()
print(a,b,c,d)

# we can pass parimeteres 
def test4(a,b,c,d):
    temp=a+b*c/d
    return int(temp)
print(test4(5,6,7,8))

def test5(a,b):
    return a+b
print(test5(5,6))
print(test5("Subramanya"," Acharya"))
print(test5([1,2,3,4],[2,3,5]))
# test 5 would just concadinate and returns wheatherr it is integer ,string or list

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Question: there is a list given containing int and string u should be able to seperate the string and int and insert it into new list
l=[1,2,3,4,"Subbu","Abhi",[3,4,5,6,"vasu"]]
l1=[]
l2=[]
def seperate(l):
    for i in l:
        if(type(i)==int):
            l1.append(i)
        elif(type(i)==str):
            l2.append(i)
        elif(type(i)==list):
            for j in i:
                if(type(j)==int):
                    l1.append(j)
                elif(type(j)==str):
                    l2.append(j)
    return l1,l2            
l1,l2=seperate(l)
print(l1)
print(l2)

# another method is used isintance() method which checks datat type of the object and list
def seperate1(l):
    l3=[]
    l4=[]
    for i in l:
        if(isinstance(i,int)):
            l3.append(i)
        elif(isinstance(i,str)):
            l4.append(i)
        elif(isinstance(i,list)):
            for j in i:
                if(isinstance(j,int)):
                   l3.append(j)
                elif(isinstance(j,str)):
                    l4.append(j)
    return l3, l4

l3,l4=seperate1(l)
print(l3)
print(l4)


# individually passing  the variabl is difficult rather than we can use * makes multiple inputs  which is dynamic in nature and return iin dynamic form

def t7(*subbu):
    return subbu

print(t7(1,2,3,4)) 


# if we do age as an parameter it would get confused and show error rather declarer and return
def t8(*subbu,age=21):
    return subbu, age
print(t8(1,2,3,4))

# if wee want to return the args in key format we would have to use **

def t9(**abhi):
    return abhi
print(t9(a=[1,2,3,4,5],b="abhi",c=233.45))
# the above is in key format



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# topic-2:Generator functions

# write a code for fibnocci series using generator functions

def fibnocci(n):
    a,b=0,1
    for i in range(n):
        yield a
        a,b=b,a+b
for i in fibnocci(10):
    print(i)

















