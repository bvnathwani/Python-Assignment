a = "Hello Pyhton"
print(a)
b = input("enter your  first number\n")
c = input("enter your second number\n")

d = float(b)+ float(c)
print("Addition of two number is\n",d)
print("The sum of {0} and {1} is {2}".format(b,c,d))

e = float(b)/float(c)
print("Division of two numbers is given by\n",e)
print("The division of {0} and {1} is {2}".format(b,c,d))




#Python program to find the area of a triangle?
import math
a = float(input("enter the length  of the first side of the triangle\n"))
b = float(input("enter the length of the second side of the triangle\n"))
c = float(input("enter the length of the third side of the triangle\n"))

s = a+b+c/3

p = math.sqrt(s*(s-a)*(s-b)*(s-c))

print("Area of the triangle is given by\n",p)


#Write a Python program to swap two variables?

x = float(input("enter your first number the number\n"))
y = float(input("enter your second number\n"))

x = x + y
y = x - y
x = x - y

print("Your swap number {0} and {1}".format(x,y))

P = int( input("Please enter value for P: "))
Q = int( input("Please enter value for Q: "))
# To Swap the values of two variables.
P, Q = Q, P
print ("The Value of P after swapping: ", P)
print ("The Value of Q after swapping: ", Q)


def swap(x,y): 
    print("Before swapping a:",x)
    print("Before swapping b:",y)
    x,y=y,x
    print("After swapping a becomes :",x)
    print("After swapping b becomes :",y)

a=int(input("Enter value : "))
b=int(input("Enter value : "))  

swap(a,b)


# Program to generate a random number between 0 and 9

# importing the random module
import random

def randomchoose(a,b):
    a = int(input("enter your first number\n"))
    b = int(input("enter your second number\n"))

    print(random.randint(a,b))


randomchoose(a,b)

