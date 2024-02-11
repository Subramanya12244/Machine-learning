# if else ifelse 

# Q-1 write a program for getting greatest of 4 nors by taking the input from user

# num1=int(input("enter the number1"))
# num2=int(input("enter the number2"))
# num3=int(input("enter the numbe3"))
# num4=int(input("enter the number4"))

# if(num1>num2 and num1>num3 and num1>num4):
#     print(f"num1={num1} is greatest of 4 nors")
# elif(num2>num1 and num2>num3 and num2>num4):
#     print(f"num2={num2} is greatest of 4 nors")
# elif(num3>num1 and num3>num2 and num3>num4):
#     print(f"num3={num3} is greatest of 4 nors")
# else:
#     print(f"num4={num4} is greatest of 4 nors")
    
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Q-2 write the program to find out wheather a student is pass or fail if it requires total 40% and atleast 33% in each subject to pass Assume 3 subjects

# maths=int(input("enter the marks of maths:"))
# physics=int(input("enter the marks of physics:"))
# chemistry=int(input("enter the marks of chemistry"))

# sum=maths+physics+chemistry
# average=sum/3

# if(average>40 and maths>33 and chemistry>33 and physics>33):
#     print(f"congratulation the student have passed and secured {averge} percent")
# else:
#     print(f"the student have failed and secured {averge} percent")

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#Q-3 write a program to find wheater a given user name has less than 10 char or not
# username=input("please enter your username")
# ch=0
# for i in range(len(username)):
#     ch=ch+1
# if(ch>10):
#     print("the user name charecter exeeds 10 charecter")
# else:
#     print("the user name charecter doesnot exeeds 10 charecter")


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Q-4 write a program which finds out wheather a given name is present in the list

# nameList=["vasu","darshan","subramnaya","abhimanyu",
# "sudha","aishwarya"]
# name=input("enter name to check for list")

# flag=False
# for i in range(len(nameList)):
#     if(name==nameList[i]):
#         flag=True
    
# if(flag):
#     print("the name is present in the list")     
# else:
#     print("the name is not present in the list")  

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Q-5 write a pgm to calculate the grade of a student from his marks from the following sceme
# 90-100->excellent
# 80-90->A
# 70-80->B
# 60-70->C
# >50->F


# marks=int(input("enter the marks"))
# if(marks>90):
#      print("you have an excellent perrformance")
# elif(marks>80 and marks<90):
#     print("you have secured 'A' Grade")
# elif(marks>70 and marks<80):
#     print("you have secured 'B' Grade")
# elif(marks>60 and marks<70):
#     print("you have secured 'C' Grade")
# else:
#     print("you have failed in exam and secured 'F' Grade")

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Loops

# Q-6 write a pgm to print multiplication table 
# num=int(input("enter the number"))
# for i in range(1,11):
#     print(f"{num}*{i}={num*i}")

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Q-7 write a pgm to greet all the persons names stored in a list l1 and starts with S

# l1=["harry","soham","sachin","rahul"]
# for i in range(len(l1)):
#     if(l1[i][0]=='s'):
#         print(f"Good morning {l1[i]}")

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Q-8 write a pgm to find the sum of first n natural numbers

# num=int(input("enter the number of natural numbers"))
# sum=0
# for i in range(num+1):
#     sum+=i
# print(f"the sum of the first {num} natural numbers is {sum}")


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#Q-9 write a pgm to find factorial

# num=int(input("enter the number of natural numbers"))
# fact=1
# for i in range(1,num+1):
#     fact*=i
# print(f"the factorial of {num} is {fact}")

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#Q-10Create a program that checks if a given year is a "century leap year" (divisible by 100 and 400) or a "non-century leap year" (divisible by 4 but not by 100).


# def leap_year(year):
#     if year%4==0 and year%100!=0:
#         print("it is a leap year")
#     else:
#         print("it is not a leap year")
# year=int(input("enter the year")) 
# print(leap_year(year))  

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 
#Q-11Write a Python script that determines if a given word is a palindrome (reads the same backward as forward), considering both upper and lower case characters.

# def is_palindrome(string):
#     lower = string.lower()
#     return lower==lower[::-1]
# string=input("enter the value to check if a given word is a palindrome")
# print(is_palindrome(string))


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# Q-12:Implement a function that takes a list as an argument and returns the average of the positive numbers in the list. Handle the case where the list might be empty.

# def getAvg(list):
#     # Filter positive numbers
#     positive = [i for i in list if i > 0]

#     # Check if the list is empty
#     if not positive:
#         return None
#     average = sum(positive) / len(positive)
#     return average
# test_case_1 = [1, 2, 3, 4, 5]
# test_case_2 = [-1, -2, -3, -4, -5]
# test_case_3 = [0, 2, -4, 6, -8]
# test_case_4 = []  # Empty list

# # Test the function with the test cases
# result_1 = getAvg(test_case_1)
# result_2 = getAvg(test_case_2)
# result_3 = getAvg(test_case_3)
# result_4 = getAvg(test_case_4)

# print(f"Test Case 1: {result_1}") 
# print(f"Test Case 2: {result_2}")  
# print(f"Test Case 3: {result_3}") 
# print(f"Test Case 4: {result_4}")

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# Q-13:Generate a list of squares of numbers from 1 to 10 but only include those that are divisible by 3.

# numbers=int(input("enter the range"))
# for i in range(numbers):
#     if(i*i%3 == 0):
#         print(i*i)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# Q-14:Create a list of prime numbers between 1 and 50 using list comprehensions

# def isprime(number):
#     if number<2:
#         return False
#     for i in range(2,number):
#         if(number%i==0):
#             return False
#     return True

# prime_number=[i for i in range(2,51) if isprime(i)]
# print(prime_number)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#Q-15 Write a function that takes a sentence as input and returns the reversed words in the sentence.
# def reverse_words(sentence):
#     words=sentence.split()
#     reverse_words=' '.join(word[::-1] for word in words)
#     return reverse_words

# sentence=input("enter the string")
# print(f"orignal sentence:{sentence}")
# print(f"reversed sentence:{reverse_words(sentence)}")
    

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#Q-16:Create a program that counts the occurrences of each character in a given string and prints the result.

# def count_characters(input_string):
#     # Create an empty dictionary to store character counts
#     counter = {}
    
#     # Iterate through each character in the input string
#     for char in input_string:
#         # Increment the count for each character in the dictionary
#         counter[char] = counter.get(char,0) + 1

#     return counter

# # Test the program
# input_string =input("enter your sentence")
# result = count_characters(input_string)

# # Display the result
# print("Input String:", input_string)
# print("Character Counts:")
# for char, count in result.items():
#     print(f"{char}: {count}")
