
# 'r'       open for reading (default)
# 'w'       open for writing, truncating the file first
# 'x'       create a new file and open it for writing
# 'a'       open for writing, appending to the end of the file if it exists
# 'b'       binary mode
# 't'       text mode (default)
# '+'       open a disk file for updating (reading and writing)

# these are the operations that can be performed on the open of the file

f=open("test.txt","w")
# ls is used for listing the files present in the directory it shouldbe given command in the terminal

f.write("hello this is my file ")
# after that we should always close it other wise it wont print in the file
# f.close()

with open("test.txt","w") as f:
    f.write("hello this is my 2nd attempt of editing the file")

# in this it is going to truncate / clear the file comtents and then it is going to write

# if we dont want to truncate then we are going to use 'a' operation on the file

with open("test.txt","a") as f:
    f.write("i would like to introduce myself I am subramanya")
    
# if i want to read the file contents
b=open("test.txt","r")
print(b.read())

# if you want to read the contents line by line

b.seek(0)
print(b.readline())
# but it wont print as the pointer have come to end so there no content left to do so we use seek

# another method to print the contents line by line is
data=open("test.txt","r")
for i in data:
    print(i)
# to find the size of the file
data=open("test.txt","w")
import os
size=os.path.getsize("test1.txt")
print(size)

# if you want to delete the file
# os.remove("test.txt")

# if you want to rename the file
os.rename("test1.txt","vip.txt")
import shutil
shutil.copy("vip.txt","vip2.txt")
