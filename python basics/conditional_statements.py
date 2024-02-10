#conditional statements
# 1.if else statements
# 2.match case statements
# 3.loops statements

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 1.if else statements
# a=int(input("enter your age"))
# if(a>18):
#     print("you can drive")    
# else:
#     print("you cannot drive")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
# else if

# applePrice=10
# budget=200
# if(budget-applePrice>50):
#     print("Alexa add 1 kg Apples to your cart")
# elif(budget-applePrice>20):
#     print("its ok you can buy")
# else:
#     print("you cannot buy")
  #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 
# another example to calculate the nor is positive or not

# num=int(input("enter the number"))
# if(num>0):
#     print("its positive nor")
# elif(num<0):
#     print("its negative")
# else:
#     print("its zero")
    
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# nested if else- meaning if is under the if
# check which is greatest among three elements

# num1=int(input("enter the number1"))
# num2=int(input("enter the number2"))
# num3=int(input("enter the number3"))
# if(num1>num2):
#     if(num1>num3):
#         print(f"num-1 {num1} is greatest among three elements")
# elif(num2>num1):
#     if(num2>num3):
#         print(f"num-2 {num2} is greatest among three elements")
# else:
#     print(f"num-3 {num3} is greatest among three elements")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 2.Match / Switch case case statemants:

# x=int(input("enter the option"))

# match(x):
#     case 100:print("the value is hundred")
#     case 10:print("the value is ten")
#     # case _:print(f"the value is {x}")
#     case _ if(x!=90):print(f"x is not equal to ninty")
#     case _ if(x!=80):print(f"x is not equal to ninty")




# 3.loops

# l=[1,2.0,'c','subramanya',8]
# for i in l:
#     print(i,type(i))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# l1=["hello", "subramanya","how are you","subramanya"]
# for i in l1:
#     print(i) 
    
# for i in l1:
#     if i=="subramanya":
#         print(i)
#         break
# it matches the subramanya in whole list if it matches it would come out of the loop

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# range is the generator to produce the nor
# print(list(range(2,20)))
# print(list(range(-10,20)))

# # print the list in reverse order using for loop
# l2=["hello", "subramanya","how are you","subramanya"]
# for i in range(len(l2)-1,-1  ,-1):
#     print(l2[i])
    
# # print the even number items of the list using for loop and range 

# l3=[1,2,3,4,5,6,7,8,9,10]
# for i in range(1,len(l3),2):
#     print(l3[i])

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# find the sum of the list of the odd term
# l3=[1,2,3,4,5,6,7,8,9,10]
# sum=0
# for i in range(0,len(l3),2):
#     sum+=l3[i]
# print(sum)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# print one after one term in string
s1="abhimanyu"
for i in range(0,len(s1),2):
    print(s1[i])