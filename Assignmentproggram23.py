# Python 3 code to demonstrate 
# removing duplicated from list 
# using naive methods 
  
# initializing list
test_list = [1,3,5,6,3,5,6,1]
print ("The original list is : " +  str(test_list))
  
# using naive method
# to remove duplicated 
# from list 
res = []
for i in test_list:
    if i not in res:
        res.append(i)
  
# printing list after removal 
print ("The list after removing duplicates : " + str(res))

test_list.sort()
print("our list after sort",test_list)

#Create a function that returns the mean of all digits.

a = [1,2,3,4,5,6]
sum = 0
for i in range(len(a)):
    sum = sum + a[i]
print("total sum is given by",sum)

mean = sum/len(a)

def media(x):
  if x<1:
    return 0
  else:
    return x%10+media(x//10)

print(media(1234))


def find_avg_sum(num):
    count = 0
    sum = 0
    while(num > 0):
        sum += num % 10
        count += 1
        num = int(num/10)
    return sum/count


given_number = int(input('Enter a number: '))

print('Average sum of all digits : {}'.format(find_avg_sum(given_number)))

def sq(num):
    words = list(str(num)) # split the text
    for i in words:  # for each word in the line:
        print(int(i)**2, end="") # print the word

k = int(input("enter your digit to find the square\n"))
sq(k)

#Write a Python program to test whether a given number is symmetrical or not.
#A number is symmetrical when it is equal of its reverse.

def is_symmetrical_num(n):
  return str(n) == str(n)[::-1]

k = int(input("\n enter your number to check the symmetry or not\n"))
print(is_symmetrical_num(k))

#Given a string of numbers separated by a comma and space, return the product of the
#numbers.


lst = input().split(',')#can use any seperator value inside '' of split
print (lst)
#given input = hello,world
#output: ['hello', 'world']
#another example 
lst = input().split(' ; ')#can use any seperator value inside '' of split
print (lst)
#given input = hello ; world ; hi there
#output: ['hello', 'world', 'hi there']
















































    
