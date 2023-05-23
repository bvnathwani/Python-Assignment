# Python program to find sum of elements in list
total = 0
 
# creating a list
list1 = [11, 5, 17, 18, 23]
 
# Iterate each element in list
# and add them in variable total
for ele in range(0, len(list1)):
    total = total + list1[ele]
 
# printing total value
print("Sum of all elements in given list: ", total)



#Python Program for multiply number 
num = int(input("enter your list entry\n"))

  
# printing number 
print (num)
  
# using list comprehension
# to convert number to list of integers
res = [int(x) for x in str(num)]
  
#printing result 
print ("The list is given by\n" ,res)

m=1

for i in range(len(res)):
    
    m = m*res[i]
print("Multiply of the all the array is given by\n",m)


#Write a Python program to find smallest number in a list?

def smallestnumber(numbers):

    smallest_num =numbers[0]
   

    for num in numbers:
        if num < smallest_num:
            smallest_num= num

    return smallest_num

print("Your smallest number is\n",smallestnumber([8,9,0,7,6,5,4]))


#Python Program for multiply number 
num = int(input("enter your list entry\n"))

  
# printing number 

print(num)
  
# using list comprehension
# to convert number to list of integers

res = [int(x) for x in str(num)]
  
#printing result 

print ("The list is given by\n" ,res)

res.sort()

print("Smallest element is from the list is:\n",res[0])
print("Largest element is from the list is:\n",res[-1])
print("Second Largest element is from the list is:\n",res[-2])




um = int(input("enter your list entry\n"))

  
# printing number 

print(num)
  
# using list comprehension
# to convert number to list of integers

res = [int(x) for x in str(num)]
  
#printing result 

print ("The list is given by\n" ,res)

max1 = max(res)
res.remove(max1)

max2 = max(res)
res.remove(max2)

max3 = max(res)
print("Third largest Maximium value in the list is given by \n", max3)

L=[2,5,23,8,35,92,55,99]

maxelement = L[0]
#maxelement is L[0]=2

for i in L:
#for i in L => i= 2,i=5,i=23,i=8,i=35,i=92,i=55,i=99
#for i = 2
#for i = 5
#....

#for i =55
    if i>maxelement:
# if 2>2 =>no , that is maxelement is not the 2
#if 5>2 => yes
#....


#if 55>92 =>No
        maxelement=i
#since 2>2 not true =>maximum element is not 2 will never run this loop
#Since 5>2 is true => maximum element is 5
#.....

#Since 55>92 is not true => maximum elemet is i = 92
print("Your maximum element is given by",maxelement)

#Check even number in List

num = int(input("enter your list entry\n"))

  
# printing number 
print (num)
  
# using list comprehension
# to convert number to list of integers
res = [int(x) for x in str(num)]
  
#printing result 
print ("The list is given by\n" ,res)
print("All the even entries is given by\n")
for i in res:
    if i%2==0:
        print(i,end="\n")
    



num = int(input("enter your list entry\n"))
# printing number 
print (num)
  
# using list comprehension
# to convert number to list of integers
res = [int(x) for x in str(num)]
  
#printing result 
print ("The list is given by\n" ,res)
print("All the odd entries is given by\n")
for i in res:
    if i%2!=0:
        print(i,end="\n")



#Remove empty list from a list

list3 = [2,5,6,7,[],[],"",[],5,6]
print("Our list without empty list is given by\n")
print([x for x in list3 if x ])

print(list(filter(lambda x:x,list3)))

#Using slicing technique to find the copy or clone of list

mylist = int(input("Enter your list inputs\n"))

res = [int(x) for x in str(num)]

print("the list is given by\n",res)

newmylist = res[:]
print("Our new copy or clone of list is given by \n" , newmylist)




#using extend method


mylist2 = int(input("Enter your list inputs\n"))

res = [int(x) for x in str(num)]

print("the list is given by\n",res)
takecopylist = []

takecopylist.extend(res)

print("Our new copy or clone of list is given by \n",takecopylist)


#using the list method


#using copy method


#Write a Python program to Count occurrences of an element in a list?

occur = [15,6,7,8,12,10,101,10,10,28,29]

x =10
count=0
for i in occur:
    if i==x:
        count = count+1

print("occurence of {0} is given by the no. of conut {1}".format(x,count))

x = 10

print("occurence of {0} is given by the no. of conut {1}".format(x,occur.count(x)))

from collections import Counter

mylist = [5,6,7,8,9,10,28,10]
x=10
dic = Counter(mylist)






































