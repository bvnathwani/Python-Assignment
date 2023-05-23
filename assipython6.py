#Find the sum of the cube of first n natural numbers
sum =0
a = int(input("enter the number for find the sum of natural numbers cube\n"))
for i in range(1,a+1):
    sum = sum + i*i*i
print(sum)


# Factorial of a number using recursion

def factorial(n):
   if n == 1:
       return n
   else:
       return n*factorial(n-1)

num = int(input("enter your number to find the factorial\n"))

# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", factorial(num))


import math
n = int(input("enter your number to find the natural logarithm"))

print("Natural logarithm of {0} is given by : ".format(n), end=" ")
print(math.log(n))

# Python code to demonstrate the working of
# log10(a)
 
import math
#Printing the log base 10 of 14
print ("Logarithm base 10 of 14 is : ", end="")
print (math.log10(14))

import math
height = float(input("Input your height in Feet: "))
weight = float(input("Input your weight in Kilogram: "))
BMI = weight/height**2
print("0.2 your body mass index is given by\n",BMI)

# Python program to display the Fibonacci sequence

def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))

nterms = 10

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(fibo(i))









