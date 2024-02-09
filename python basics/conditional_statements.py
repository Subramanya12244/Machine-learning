l=[1,2.0,'c','subramanya',8]
for i in l:
    print(i,type(i))
    
l1=["hello", "subramanya","how are you","subramanya"]
for i in l1:
    print(i) 
    
for i in l1:
    if i=="subramanya":
        print(i)
        break
# it matches the subramanya in whole list if it matches it would come out of the loop


# range is the generator to produce the nor
print(list(range(2,20)))
print(list(range(-10,20)))

# print the list in reverse order using for loop
l2=["hello", "subramanya","how are you","subramanya"]
for i in range(len(l2)-1,-1  ,-1):
    print(l2[i])
    
# print the even number items of the list using for loop and range 

l3=[1,2,3,4,5,6,7,8,9,10]
for i in range(1,len(l3),2):
    print(l3[i])


# find the sum of the list of the odd term
l3=[1,2,3,4,5,6,7,8,9,10]
sum=0
for i in range(0,len(l3),2):
    sum+=l3[i]
print(sum)


# print one after one term in string
s1="abhimanyu"
for i in range(0,len(s1),2):
    print(s1[i])