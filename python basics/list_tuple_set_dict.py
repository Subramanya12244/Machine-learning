l=[1,345,45,"sudha",True,5+8j,345.456]
print(type(l))
print(l[0:3])
print(l[-1])
# list reverse
print(l[::-1])
# print even indexes of list
print(l[1::2])
# we cannot concadinate a string and a list as both are different data structures
s="abhimanyu"
# print(s+l)
print(list(s)+l)
# it will concadinate but it is going to break the string into multiple charecter


# concatination of two lists
l1=[3,4,5]
print(l+l1)
# we can multiply two lists
print(l1*3)
# print su from the list
print(l[3][:2])

# we can identify the lenngth of the list using len() function 
print(len(l))

# hence we use the append,extend,insert and remove functions
l1.append(s)
print(l1)

# append the list l in the l1
l1.append(l)
print(l1)


# extend is  a function that takes the data and slices it and return we cannot pass the int datatype inside the extend function as we cannot break the the int into indexes


l1.extend("subbu")
print(l1)

l1.extend([9,0,1,9])
print(l1)

# insert is a function that inserts the value into the any place of the list we have to pass the index and value as an argument

l.insert(0,"abhi")
print(l)

# remove function removes the value first ocurence of the list
# remove 3 from the list l1
l1.remove(3)
print(l1)

# pop funcctions removes the value from the end of the list and if wee pass any number as an argument it will be remove the value from the index
l2=[5,6,7,"abhi",[8,9,10]]
# l2.pop()
l2.pop(3)
print(l2)

# i want to remove the 9 from the list
l2[3].remove(9)
print(l2)

# #reverse,sort(),count,index,replace

# reverse the list
# difference between reverse() and [::-1] is that reverse function implements permanently reverse
l2.reverse()
print(l2)

#sort the list every element in the list should be in similar data type

l3=[2,2,9,3,5,6,1,2,3,4]
l3.sort()
# for descending order we pas the argument reverse=true
print(l3) 

# wee cannot apply it for l2 list as the elements are in different data types
l3.sort(reverse=True)
print(l3)


# count() it would return the number of ocurence of the argument in that list
print(l3.count(2))

# index() it would return the index of the argument in that list
print(l3.index(5))

# mutable v/s immutable 
# if we can reassign the value and get replaced are mutable ex-arrays,lists and vise versa for non mutable ex-strings

s="subramanya"
print(s.replace('a','s'))



# #tuples are same as lists but are immutable and have () only count and index methods are available in tuples
t=(2,3,4,5,"subramanya",45.6,False,[1,2,3])

# t[4]=5 
#'tuple' object does not support item assignment

# #set iss the data structure which accepts the non mutable data structure and returns the the unique elements

s1={}
print(type(s1))
# returns dict as it considers empty set as the dictionaries

s2={2,3,4,55,6}
print(type(s2))
# returns set

# s3={2,3,4,5,"subramanya",45.6,False,[1,2,3]}
# you cannot pass an list to the dict as they are mutable
# print(s3)

s4={2,3,4,5,"subramanya",45.6,False,(1,2,3)}
print(s4)
# but wee can pass tuples as they are immutable

# it removes all the duplicates and does not Arrange in ascending order
s5={1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,5,5,5,5,55,5,5,5,5}
print(s5)

l6=[1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,5,5,5,5,55,5,5,5,5]
l6=list(set(l6))
print(l6)


# dictionaries- stores the values in the form of keys and values uses curly brackets for declaration 

d={}
print(type(d))
# in this if you add values in the linear format it will store as set if you assign in key value pairs it would print the dictionaries

d1={"name":"subramanya","email":"subramanya@gmail.com","age":21}
for i in d1:
    print(i,d1[i])
    
# for searching values
print(d1["name"])

d4={"name":"subramanya","email":"subramanya@gmail","name":"abhimanyu"}
print(d4["name"])

# in ht eabove case the name key would over ride the value subramanya and store the abhimanyu

d5={"company":"pwskills","courses":["webdevelopment","data science","java dsa"]}
# retrive the value java dsa from the above dictonaries
print(d5["courses"][2])

d6={"number":[2,34,4,34,34],"assignment":[1,2,3,4,5,6],"launch date":[28,12,14],"class_time":{"web dev":8,"dataScience":5,"java dsa":12}}

print(d6)

# even we can add more keys

d6["mentor"]={"sudhanshu","krishh"}
print(d6)

# keys() functiones are used to display the keys of the dictionaries
print(d6.keys())

# .values() functiones are used to print the values in the dictionaries

print(d6.values())

# .pop() remove specified key and return the corresponding value if the key is not present the it show key error
d6.pop("class_time")

