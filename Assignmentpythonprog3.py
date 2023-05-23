N = float(input("Enter a number to check positive , negative or zero\n"))

if N > 0:
    print("Given number {0} is positive".format(N))

elif N ==0:
    print("Given number {0} is zero".format(N))
elif N<0:
    print("Given number {0} is negative".format(N))

#Write a Python Program to Check if a Number is Odd or Even?

def even(x):
    if x%2==0:
        print("The number is even")
    else :
        print("The number is odd")

a = int(input("Please entre your number\n"))
even(a)

#Write a Python Program to Check Leap Year?

year = int(input('Enter year : '))

if (year%4 == 0 and year%100 != 0) or (year%400 == 0) :
    print(year, "is a leap year.")
else :
    print(year, "is not a leap year.")


#Write a Python Program to Check Prime Number?

    
m = int(input("enter your number to check prime or not\n"))

if m >1:
    for i in range(2,m):
        if m%i==0:
            print(m,"is the not the prime number")
            break
    else:
        print(m,"is the prime number")

else:
    print(m,"is not the prime")



# Python program to display all the prime numbers within an interval

lower = 1
upper = 10000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
        
        



