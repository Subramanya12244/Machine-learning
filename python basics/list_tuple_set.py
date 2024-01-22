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

# hence we use the append,insert and remove functions
l1.append(s)
print(l1)

# append the list l in the l1
l1.append(l)
print(l1)
# remove 3 from the list l1
l1.remove(3)
print(l1)