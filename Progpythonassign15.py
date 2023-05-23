#Please write a program using generator to print the numbers which can be divisible by 5 and
#7 between 0 and n in comma separated form while n is input by console.
'''Example:
If the following n is given as input to the program:
100
Then, the output of the program should be:
0,35,70'''
def generate(n):
    for i in range(n+1):
        if i % 35 == 0:    # 5*7 = 35, if a number is divisible by a & b then it is also divisible by a*b
            yield i

n = int(input("Please enter any number to generate the number which is divisible by 5 and 7\n"))
resp = [str(i) for i in generate(n)]
print(",".join(resp))


#Second method

def NumGenerator(n):
    for i in range(n+1):
        if i%5==0 and i%7==0:
            yield i

n=int(input("Please enter the number\n"))
values = []
for i in NumGenerator(n):
    values.append(str(i))

print(",".join(values))



'''Question 2:
Please write a program using generator to print the even numbers between 0 and n in comma
separated form while n is input by console.
Example:
If the following n is given as input to the program:
10
Then, the output of the program should be:
0,2,4,6,8,10'''

#Solution by: StartZer0
n = int(input("Please enter the number which is even\n"))

for i in range(0,n+1,2):
  if i < n - 1:
    print(i, end = ',' )
  else:
    print(i)

#evengenerator
def EvenGenerator(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1


n=int(input("Please enter the number\n"))
values = []
for i in EvenGenerator(n):
    values.append(str(i))

print(",".join(values))




'''Question 3:
The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n&gt;1
Please write a program using list comprehension to print the Fibonacci Sequence in comma
separated form with a given n input by console.
Example:
If the following n is given as input to the program:
7

Then, the output of the program should be:
0,1,1,2,3,5,8,13'''
#0+1 = 1, 1+1 = 2,2+3=5
def fib(n):
        a = 0
        b = 0
        print(a)
        print(b)
        if n==1:
            print(a)
        else:
            print(a)
            print(b)

            for i in range(2,n):
                c=a+b
                a=b
                b=c
                print(c)
    
  
fib(10)

#fabonic sequence 0 ,1 => n1 ,n2 ,n1+n2,n1+n2 +n2 , n1+n2 +n1+n2+n2.....
num = int(input("Enter any number: "))
n1,n2 = 0,1
sum = 0
if num<=0:
    print("Please enter number greater than 0")

else:
    for i in range(0,num):
# for i in range(0,5)=>0,1,2,3,4 =>for i =0
# for i =1
#for i = 2
        print(sum, end=" ")
# print(sum=0)=>0
#print(1=sum)=> 1
#print(1=sum)=> 1
#print(2=sum)=>2
#print(3=sum)=>3
#....print(sum=5)
        n1 = n2
#n1=n2=>0=1=>n1=1
#n1 =n2=>1=0=>n1=0
#n1=n2=>0=1=>n1=1
#n1=n2=>1=1=>n1=1
#n1=n2=>1=2=>n1=2
        n2 = sum
#n2 =sum = 0=> n2 = 0
#n2 = sum = 1=> n2 = 1
#n2 = sum = 1=> n2 = 1
#n2 = sum = 2=>n2 = 2
#n2 = sum = 3=> n2 =3
        
        sum = n1+n2
# sum = n1 is 1 + n2 is 0 = 1+0=1
#sum = n1 is 0 +n2 is 1= 0+1 =1
#sum = n1 is 1 +n2 is 1 = 1+1 = 2
#sum = n1 is 1 + n2 is 2 = 3
#sum = n1 is 2 + n2 is 3 = 5

        
    

#0,1,1,2,3...
#sum=0,sum=1+0=1=n1+n2,sum=0+1=1=n1+n2,sum =1+n2=1+1=2,sum = 

num = int(input("enter your number\n"))

n1 =0
n2 = 1
sum =0

if num <=0:
    print("Please enter the positive number\n")

else:
    for i in range(0,num):
        print(sum,end=" ")
        
#so that the output will come in one line by end =" "
# sum =0
# sum = 1
#sum = 1
#sum =2
        n1 = n2
#n1=n2=>0=1=>n1=1
#n1=n2 => 1=0=>n1=0
        n2 = sum
#n2 = sum= 0
#n2 = sum =1

        sum = n1 +n2
#sum = 1+ 0 = 1
#sum = 0+1 =1
#sum = 1+1=2


#fibonic sequence
def f(n):
    if n < 2:
        fibo[n] = n
        return fibo[n]
    fibo[n] = f(n-1) + f(n-2)
    return fibo[n]

n = int(input("Please enter the number for fibinic sequence\n"))
fibo = [0]*(n+1)  # initialize a list of size (n+1)
f(n)              # call once and it will set value to fibo[0-n]
fibo = [str(i) for i in fibo]   # converting integer data to string type
ans = ",".join(fibo)    # joining all string element of fibo with ',' character
print(ans)







































