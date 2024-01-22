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
l2=[5,6,7,"abhi",8,9]
l2.pop()
l2.pop(3)
print(l2)