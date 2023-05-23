'''Question 1:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated
sequence.'''


import math

i = int(input("please enter your integer value of lower limit more than 100\n"))
j = int(input("please enter your integer value of upper limit with the gap 30 atleast\n"))

D= [int(x) for x in range(i,j+1,30)]


print("\nThe value Of D is given by in the form of sequence\n")
for i in D:
    print(i,end =",")

C = 50
H = 30

print("\nOur output is given by after the operation\n")

for i in D:
    Q = int(math.sqrt(2*C*i/H))
    print(Q,end=",")



D = [100,150,180]

print("\nThe value of D is given by\n",D)

C = 50
H = 30
print("\nOur value is given by after the operation\n")
for i in D:
    Q = int(math.sqrt(2*C*i/H))
    print(Q,end="\n")


'''Question 2:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The
element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]'''

def matrix(m,n):
    
    outputmatrix = []
    for i in range(m):
        row=[]
        for j in range(n):
            #inp =int(input(f"Enter outputmatrix[{i}][{j}]"))
            row.append(i*j)
        outputmatrix.append(row)
    return outputmatrix
m = int(input("Enter the value of m\n"))
n = int(input("Enter the value of n\n")) 
A = matrix(m,n)

print(A)


#Write a program that accepts a comma separated sequence of words as input and prints the
#words in a comma-separated sequence after sorting them alphabetically.

words = input("Please enter a words that accepts a comma\n")

m = words.split(",")
m.sort()
#using sort method

k = sorted(m,reverse=True)
print("In acendeing order is given by\n",m)
print("In descending order is given by\n",k)

#using for loop 
print("Ascending order by using for loop is gievn by\n")
words2 = input("Please enter a words that accepts a comma\n")
m = words2.split(",")
for i in range(0,len(m)-1):
    
    if m[i]>m[i+1]:
        temp=m[i]
        m[i]=m[i+1]
        m[i+1] = temp
print(m)

#Write a program that accepts a sequence of whitespace separated words as input and prints
#the words after removing all duplicate words and sorting them alphanumerically.

#using set function
Take1 = input("Take1:Enter the set of words with spaces in between\n")
var1 = Take1.split()
print(sorted(set(var1)))
print(type(var1))

#using function for removing duplication
Take2 = input("Take2:Enter the set of words with spaces in between\n")
def remove(var1):
#define a function remove
    mylist = []
#take a empty list mylist in which
    for obj in var1:
#using for loop in var1 so obj is from take2 hello ,...
        if obj not in mylist:
#now mylist =["hello","baby", ...] now to check hello should be not there again.
            mylist.append(obj)
#if it is so then append otherwise dont append the valueto mylist that one by one object
    return mylist
var1 = Take2.split()
#take var1 into list with using comma separeted by
var2 = remove(var1)
#var2 will never contains duplicate
noneduplicate = sorted(var2)
print(noneduplicate)


#Write a program that accepts a sentence and calculate the number of letters and digits.

'''Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10 Digit 3'''

Take3 = input("Enter the set of words with spaces in between\n")
char_counter =0
digit_counter=0

for i in Take3:

    if(i.isalpha()):

        char_counter+=1
    elif(i.isdigit()):
        
        digit_counter+=1

print("Number of letter=",char_counter)
print("Number of digits=",digit_counter)

'''Question 6:
A website requires the users to input username and password to register. Write a program to
check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them
according to the above criteria. Passwords that match the criteria are to be printed, each
separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1'''


import re
flag = 0
password =("Enter the password : \n")
if not re.search("[a-z]",password):
    
    flag=1
if not re.search("[0,9]",password):
    flag=1
if not re.search("[A-Z]",password):
    flag=1

if not re.search("[$@#!]",password):
    flag=1
if len(password)<6 or len(password)>12:
    flag = 1

if flag==0:
    print("password is valid")

else:
    print("Password is not valid")


class Authentication(object):
    def __init__(self, username = ''):
        self.username = username

    def __lower(self):
        lower = any(c.islower() for c in self.username)
        return lower

    def __upper(self):
        upper = any(c.isupper() for c in self.username)
        return upper

    def __digit(self):
        digit = any(c.isdigit() for c in  self.username)
        return digit

    def validate(self):
        lower = self.__lower()
        upper = self.__upper()
        digit = self.__digit()

        length = len(self.username)

        report =  lower and upper and digit and length >= 6

        if report:
            print("Username passed all checks ")
            return True

        elif not lower:
            print("You didnt use Lower case letter")
            return False

        elif not upper:
            print("You didnt userUpper case letter")
            return False

        elif length <6:
            print("username should Atleast have 6 character")
            return False

        elif not digit:
            print("You didnt use Digit")
            return False
        else:
            pass

C = Authentication("ga1Agdfd")
print(C.validate())







































    

