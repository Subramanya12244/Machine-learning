# topic-2 Custom exception handling:

# defn:-these are the exception handlerss that we are going to represent specific error conditions that are relevant to our application by defining these type of exceptions we can make the code more readable maintainable and they will be in more structured and meaning full way

class validate(Exception):
    def __init__(self,msg):
        self.msg = msg

def validateAge(age):
    if age < 0:
        raise validate("entered age is negative and age cant be negative")
    elif age >200:
        raise validate("entered age is much high for humans")
    else:
        print("entered age is valid")

try:
    age=-180
    # age280
    # age=10
    validateAge(age)
except validate as e:
    print(e)   
    
# in the above program we are writing a code such that it should raise an exception when the user enters age that is negative or greater than 200
# we have built the custom exception handler