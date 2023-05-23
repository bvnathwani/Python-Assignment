# Taking kilometers input from the user
kilometers = float(input("Enter value in kilometers: "))

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles'%(kilometers,miles))


# Python Program to convert temperature in celsius to fahrenheit

# change this value for a different result
celsius = float(input("enter the temperature in celius\n"))

# calculate fahrenheit
fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))
#Write a Python program to display calendar?

#Program to display calendar of the given month and year

#importing calendar module

import calendar

yy = 2022  # year
mm = 12  # month

# To take month and year input from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy,mm))

#Quardratic euation solve
import cmath
a = float(input("enter the coefficient of x^2\n"))
b = float(input("enter the coefficient of x\n"))
c = float(input("enter the constant term\n"))

x1 = (-b + cmath.sqrt(b*b -4*a*c))/2*a
x2 = (-b - cmath.sqrt(b*b -4*a*c))/2*a


# Python code to swap two numbers
# without using another variable
 
x = 5
y = 7

print ("Before swapping: ")
print("Value of x : ", x, " and y : ", y)
 
# code to swap 'x' and 'y'
x, y = y, x
 
print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)

print("your quardratic equation is given by\n")
print("the solution of the quartdrtic equation is given by\n",x1,x2)


