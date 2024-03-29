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

# 2nd method 
def fibnocci1():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
fib=fibnocci1()
for i in range(10):
    print(next(fib))
# string method is not iterator so we use next in the above example using for loop
# only itorator can be iterable like we cannot iterate the int 
s1="abhimanyu"
s2=iter(s1)

# print(next(s2))
# print(next(s2))
# print(next(s2))
# print(next(s2))
# print(next(s2))
# print(next(s2))
# print(next(s2))
# print(next(s2))
# print(next(s2))
# the above is equal to below
for i in range(len(s1)):
    print(next(s2))

# another example
def count(n):
    count1=1
    while count1<=n:
        yield count1
        count1=count1+1
c=count(10)
for i in c:
    print(i)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# topic:3.lambda function

n=3
p=2
def test(n,p):
    return n**p
print(test(n,p))

# using lamda function   
a=lambda n,p:n**p
print(a(n,p))

# addition using lamda function
sum=lambda a,b:a+b
print(sum(10,20))

# convet celcius to farenite
f=lambda c:9/5*c+32
print(f(45))

# finding max 
max=lambda a,b:a if a>b else b
print(max(10,20)) 

# finding length of the string
s="subramanya"
length=lambda s:len(s)
print(length(s))


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# topic-4:Map,Reduce,Filter functions

l=[2,3,4,5,6]
# sqaring each and every element of list

def testCase(l):
    l1=[]
    for i in l:
        l1.append(i*i)
    return l1
print(testCase(l))

# using map functions
# map function takes a function and iterates through each and every element and do the operation from the function ex

print("using the map functions:")
def sqare(x):
    return x**2

print(list(map(sqare,l)))

print(list(map(lambda x:x**2,l)))

l1=[1,2,3,4,5]
l2=[6,7,8,9,10]

print(list(map(lambda x,y:x+y,l1,l2)))

s1="subramanya"
print(list(map(lambda x:x.upper(),s1)))


# reduce: only two potential arguments can be passed we cannot pass more than two arguments
from functools import reduce
l1=[1,2,3,4,5,6,7,8,9,10]
print(reduce(lambda x,y:x+y,l1))


# print(reduce(lambda x,y,z:x+y+z,l1)) 
# the above will show error

# write a reduce funtion which will return max of list 
l2=[5,4,5,6,7,8,9]
print(reduce(lambda x,y:x if x>y else y,l2))


# filter:
# even
print(list(filter(lambda x:x%2==0,l2)))
# odd
print(list(filter(lambda x:x%2==1,l2)))

l3=[-5,-7,-8,-9,1,2,3,4]
# printing negative nor
print(list(filter(lambda x:x<0,l3)))

