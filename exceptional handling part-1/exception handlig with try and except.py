#topic-1 exception handling with try and except


# defn:-Try and catch blocks are used in programming languages to handle exceptions or errors that might occur during the execution of a program. The basic idea is to try a block of code and if any exception occurs within that block, catch it and handle it gracefully rather than letting the program crash.

try :
    f= open("text.txt", "r")
except Exception as e:
    print("this is my exception",e)
print(4+5)

# usually when we try to open a file in read mode which is not present/created it show error messages but the further code is not executedd but when we use try and catch after getting the error message it would display it and it further executes the code as you can see above

try :
    f= open("text.txt", "w")
    f.write("hello world")

except Exception as e:  
    print("this is my exception",e)

# here it the code will run fine but it wont throw an exception and doesn't go to the exception block
else:
    f.close()
    print("this will executed only when there is no error message and it will write in the file")

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

try:
    f=open("text1.txt","r")
except Exception as e:
    print("this is my exception")
else:
    f.close()
    print("this will executed only when there is no error message and it will write in the file")
# it wont execute else part as it shows error and it will be thrown to the except block


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# finally block- it executes in each and every situation wheather there is exception is there or not

try:
    f=open("text2.txt","r")
    f.write("hello world")
finally:
    print("it executes in each and every situation wheather there is exception is there or not")

# it would show error message but as we are opening a file in read mode but want to write it


