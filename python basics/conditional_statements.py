# if else ifelse
#Q-1Create a program that checks if a given year is a "century leap year" (divisible by 100 and 400) or a "non-century leap year" (divisible by 4 but not by 100).

# def leap_year(year):
#     if year%4==0 and year%100!=0:
#         print("it is a leap year")
#     else:
#         print("it is not a leap year")
# year=int(input("enter the year")) 
# print(leap_year(year))  


#Q-2Write a Python script that determines if a given word is a palindrome (reads the same backward as forward), considering both upper and lower case characters.

# def is_palindrome(string):
#     lower = string.lower()
#     return lower==lower[::-1]
# string=input("enter the value to check if a given word is a palindrome")
# print(is_palindrome(string))

# Q-3:Implement a function that takes a list as an argument and returns the average of the positive numbers in the list. Handle the case where the list might be empty.

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


# Q-4:Generate a list of squares of numbers from 1 to 10 but only include those that are divisible by 3.

# numbers=int(input("enter the range"))
# for i in range(numbers):
#     if(i*i%3 == 0):
#         print(i*i)

# Q-5:Create a list of prime numbers between 1 and 50 using list comprehensions

# def isprime(number):
#     if number<2:
#         return False
#     for i in range(2,number):
#         if(number%i==0):
#             return False
#     return True

# prime_number=[i for i in range(2,51) if isprime(i)]
# print(prime_number)


#Q-6Write a function that takes a sentence as input and returns the reversed words in the sentence.
# def reverse_words(sentence):
#     words=sentence.split()
#     reverse_words=' '.join(word[::-1] for word in words)
#     return reverse_words

# sentence=input("enter the string")
# print(f"orignal sentence:{sentence}")
# print(f"reversed sentence:{reverse_words(sentence)}")
    
#Q-7:Create a program that counts the occurrences of each character in a given string and prints the result.


