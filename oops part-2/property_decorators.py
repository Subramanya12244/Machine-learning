# topic-Decorator
def test():
    print("this is the starrt of the function")
    print(4+5)
    print("this is my fun to test")
test()

# defn:it is the powerful feature that allows you to modify or extend the behavior of function or methods without directly modying the code 

def my_decorator(func):
    def wrapper():
        print("this is the before function call")
        func()
        print("this is the after function call")
    return wrapper

@my_decorator   
def say_hello():
    print("Hello")

say_hello()


# we are going to calculate how much time we are going to take time for function to get executed
import time

def timer_fun(func):
    def timer_test():
         start=time.time()
         func()
         end=time.time()
         print(end-start)
    return timer_test
@timer_fun
def check_function():
    for i in range(1000000):
        pass
check_function()