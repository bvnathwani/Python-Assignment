#1.Write a Python program to find words which are greater than given length k?

list1 = ["john","lease","asdtgfb","hggfgfffg"]
list2 =[]
for  i in list1:
#i =>john , lease ......,hggggfgffg
    if(len(i)>5):
#length(john) =4 ,......,9
        list2.append(i)
#list2=[hggfgfffg]
print(list2)

string =input("enter your string value\n")

words = string.split()
print(words)
k = int(input("To find the words greater than given length k then please enter that length\n"))
#get the words for string
output = []
for i in words:
    if(len(i)>k):
        output.append(i)
print(output)

#2.Write a Python program for removing i-th character from a string?

s = input("Please enter the string value\n")
n = int(input("enter the value of Ith charachter\n"))

a = s[0:n-1]
#if n =3
#if remove T = 2 => [0:3-1]=[0:2]=>PY
#PYTHAN = 0,1,2,3,4,5,6 =>[0:2] => PY => 0,1,2(Remove)=>PY
b = s[n:]
#b=s[3:]=>HAN => 3,4,5

print("our result is\n",a+b)

#2.Write a Python program for removing i-th character from a string?
s = input("Please enter the string value\n")
n = int(input("enter the value of Ith charachter\n"))

a = s[0:n]
#if n =3
#if remove T = 2 => [0:3-1]=[0:2]=>PY
#PYTHAN = 0,1,2,3,4,5,6 =>[0:2] => PY => 0,1,2(Remove)=>PY
b = s[n+1:]
#b=s[3:]=>HAN => 3,4,5

print("our result is\n",a+b)

#Write a Python program to split and join a string?
string ="I am python lover"
list_string = string.split()
print(list_string)


joinstring ="-".join(list_string)
print(joinstring)

s = input("Enter the Binary string")
set1 = set(s)#set(s)={"1","0"}
p ={"1","0"}
if set1 == p or set1=={"1"} or set1 =={"0"}:
    print("IT IS BINARY STRING")
else:
    print("IT IS NOT BINARY STRING")

#Write a Python program to find uncommon words from two Strings?
s1 = input("Please enter the first string")
s2 = input("Please enter the second string")

s1 = s1.split()
s2 = s2.split()

for i in s1:
    if i not in s2:
        print(i)

stringdup = "Python Programming"
duplicates = []

for i in stringdup:
    if stringdup.count(i)>1:

#if check p multiple times are not
        if i not in duplicates:
            #checking p is not coming for multiple occurence
            duplicates.append(i)
            #finding out the duplicates by using appending method sequence

print(duplicates) 

import re

st ="welcome@@2To%%Python**Programming@!!^%%@S"

r = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
if r.search(str)==None:
    print("No special characters present in a string")

else:
    print("String contains special characters")






    
    












