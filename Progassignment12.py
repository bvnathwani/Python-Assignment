#Write a Python program to Extract Unique values dictionary values?
student_details ={1:"Ram",2:"Komal",3:"Sahil",4:"Rama",5:"Sunny",6:"Pratham"}


print(student_details)
print(set(student_details.values()))

#Write a Python program to find the sum of all items in a dictionary?

for rollno in set(student_details.values()):
    print(rollno.title())

print(student_details.keys())
print(student_details.values())

for i in student_details.keys():
    print(i)

for i in student_details.values():
    print(i)
#Write a Python program to find the sum of all items in a dictionary?
add = {"Dipu":1,"Sipu":2,"Mipu":3,"Chipu":4}

l = add.values()
print(l)
print(add)
print(add.keys())
#keys is Dipu , Sipu .....Chipu
sum =0
for i in l:
    sum = sum + i
print("The sum of all items in a dictonary is given by\n",sum)

add.update(student_details)

print(add)
dict ={}

dict.update(add)
dict.update(student_details)

print(dict)

#Write a Python program to convert key-values list to flat dictionary?
#l1=[1,2,3,4]
#l2 = ["Ram","Shayam","GANSHYAM","gGuru"]
#z = dict(zip(l1,l2))
#print(z)


#Write a Python program to sort Python Dictionaries by Key or Value?
scores =[("Nikhil",6),("Rohan",7),("Manish",8),("Ram",10)]
d = {}
for name,score in scores:
    
    d[name]=score

print(d[name])

from collections import OrderedDict
od = OrderedDict()
for i in range(int(input())):
    str = input().split()
    k="".join(str[:-1])
    v = int(str[:-1])
    if k in od:
        od[k]=od[k]+v
    else:
        od[k]=v
for k,v in od.items():
    print(k,v)


'''Input: 
string = "engineers rock"
pattern = "er";
Output: true
Explanation: 
All 'e' in the input string are before all 'r'.


Input: 
string = "engineers rock"
pattern = "gsr";
Output: false
Explanation:
There are one 'r' before 's' in the input string.'''


#6. Write a Python program to check order of character in string using OrderedDict()?

from collections import OrderedDict 
  
def checkOrder(input, pattern): 
      
    # create empty OrderedDict 
    # output will be like {'a': None,'b': None, 'c': None} 
    dict = OrderedDict.fromkeys(input) 
  
    # traverse generated OrderedDict parallel with 
    # pattern string to check if order of characters 
    # are same or not 
    ptrlen = 0
    for key,value in dict.items(): 
        if (key == pattern[ptrlen]): 
            ptrlen = ptrlen + 1
          
        # check if we have traverse complete 
        # pattern string 
        if (ptrlen == (len(pattern))): 
            return 'true'
  
    # if we come out from for loop that means 
    # order was mismatched 
    return 'false'
  
# Driver program 
if __name__ == "__main__": 
    input = 'engineers rock'
    pattern = 'er'
    print (checkOrder(input,pattern)) 







#Write a Python program to sort Python Dictionaries by Key or Value?

d = {"ADARASH":25,"AMAN":45,"GOPAL":85,"GAJODHAR":75}

list1 = sorted(d.items(),key = lambda x:x[0])

list2 = sorted(d.items(),key= lambda x:x[1])

print("Original Dict=",d)
print("SORT BY KEYS=",list1)
print("SORT BY VALUES=",list2)


    













