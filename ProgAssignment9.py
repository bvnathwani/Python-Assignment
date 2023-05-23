#Write a Python program to check if the given number is a Disarium Number?
#Sum of its digits raised to the power of their respective postion is equal to the given number
#ex: 89 = 8^1 + 9^2 = 8+ 81 = 89 yes it is Disarium number

num = int(input("enter your number\n"))
#175
sum = 0
j = 1
temp = num

while(temp!=0):
    rem=temp%10
    #175%10=5
    #17%10=7
    #1%10=1
    sum=sum*10+rem
    #sum=0+5=5
    #sum=5*10+7=57
    #sum=57*10+1=571
    temp=int(temp/10)
    #temp=175/10=17
    #temp=17/10=1
    #temp=1/10=0(not procceed)
newnum = sum
#sum is reversered numbered assigned to a new number
newsum = 0
while(newnum!=0):
    #571!=0
    rem=newnum%10
    #rem=571%10=1
    #rem=57%10=7
    #rem=5%10=5
    newsum=newsum+pow(rem,j)
    #newsum=0+pow(1,1)=1^1
    #newsum = 1+pow(7,2)=1^1+7^2
    #newsum = 1^2+7^2+pow(5,3)=1^1+7^2+5^3
    newnum=int(newnum/10)
    #newnum=571/10=57
    #newnumber =57/10=5
    j=j+1
if newsum == num:
    print("Number is Disarium number")

else:
    print("Nummber is not Disarium number")





#doubts
#Write a Python program to print all disarium numbers between 1 to 100?
#ALGORITHM:
#STEP 1: CalculateLength() counts the digits present in a number.
#Use a while loop to check whether the number is equal to 0 or not.
#Divide the number by 10 and increment the variable length by 1.
#Return length.
#STEP 2: sumOfDigits() calculates the sum of digits raised to their respective positions.
#Make a call to calculateLength() to get the number of digits present in a given number and store the value in variable len.
#Using while loop calculates remainder rem repeatedly by dividing num with 10.
#Calculate the value of rem raised to power its position, i.e., remlen and store the computed value in a variable sum.
#STEP 3: To display all Disarium numbers between 1 and 100,
#Start a loop from 1 to 100, then make a call to sumOfDigits() method for each value from 1 to 100 and store the return value into a variable result.
#If the value of the result is equal to the number, it implies that the given number is Disarium number. Hence, display it.
#calculateLength() will count the digits present in a number    
def calculateLength(n):    
    length = 0;    
    while(n != 0):
        #175!=0
        length = length + 1;
        #length=0+1=1
        #length=1+1=2
        n = n//10;
        #n=175//10=17
        #n=17//10=1
    return length;
    #length=1
    #length=2
     
#sumOfDigits() will calculates the sum of digits powered with their respective position    
def sumOfDigits(num):    
    rem = sum = 0;    
    len = calculateLength(num);    
        
    while(num > 0):    
        rem = num%10;    
        sum = sum + (rem**len);    
        num = num//10;    
        len = len - 1;    
    return sum;    
result = 0;    
     
#Displays all disarium numbers between 1 and 100    
print("Disarium numbers between 1 and 100 are")   
for i in range(1, 101):    
    result = sumOfDigits(i);    
        
    if(result == i):    
        print(i),    
#A number is called happy if it leads to 1 after a sequence of steps wherein each step number is replaced by the sum of squares of its digit that is if we start with Happy Number and keep replacing it with digits square sum, we reach 1. 

#Examples : 

#Input: n = 19
#Output: True
#19 is Happy Number
#1^2 + 9^2 = 82
#8^2 + 2^2 = 68
#6^2 + 8^2 = 100
#1^2 + 0^2 + 0^2 = 1
#As we reached to 1, 19 is a Happy Number.

#Input: n = 20
#Output: False

n=int(input("Enter Number\n"))
x = n
while x>=10:
    sum=0
    while x>0:
        r=x%10
        sum=sum+(r**2)
        x=x//10
    x=sum
if x ==1:
    print(n,"is a happy number")

else:
    print(n,"is not a happy number")


#isHappyNumber() will determine whether a number is happy or not 1 and 100   

def isHappyNumber(num):    
    rem =0
    sum =0    
        
    #Calculates the sum of squares of digits    
    while(num > 0):
        #num is 175
        #num is 17
        #num is 1
        rem = num%10
        #rem=175%10=5
        #rem=17%10=7
        #rem = 1%10 = 1
        sum = sum + (rem*rem)
        #sum = 0+5*5 = 0+5^2
        #sum = 0+5^2 +7^2
        #sum = 0+5^2+7^2+1^2
        num = num//10
        #num =175//10=17
        #num =17//10=1
        #num 1//10=0(so while loop exit)
    return sum    
            
#Displays all happy numbers between 1 and 100    
print("List of happy numbers between 1 and 100: ")
for i in range(1, 101):    
    result = i    
        
    #Happy number always ends with 1 and     
    #unhappy number ends in a cycle of repeating numbers which contains 4    
    while(result != 1 and result != 4):    
        result = isHappyNumber(result)    
        
    if(result == 1):    
        print(i),    
        print(" "),

#HARSHAD NUMBER OR NIVEN NUMBER
#STEP 1: START
#STEP 2: SET num = 156, rem =0, sum =0
#STEP 3: DEFINE n
#STEP 4: n = num
#STEP 5: REPEAT STEP 6 to STEP 8 UNTIL (num>0)
#STEP 6: rem =num%10
#STEP 7: sum = sum + rem
#STEP 8: num = num/10
#STEP 9: if(n%sum==0) then PRINT "Yes" else PRINT "No"
#STEP 10: END

num = int(input("enter your number to check harshad number or not?"))

#Make a copy of num and store it in variable n    
n=num    
rem=0
sum=0
#Calculates sum of digits    
while(num > 0):
    #num=173
    rem = num%10
    #rem = 173%10=3
    #rem = 17%10=7
    #rem = 1%10=1
    
    sum = sum+rem
    #sum =0+3=3
    #sum =3+7
    #sum =3+7+1=11
    #check that num%11==0?
    num =num//10
    #num= 173//10=17
    #num= 17//10=1
    #num =1//10=1
     
#Checks whether the number is divisible by the sum of digits    
if(n%sum == 0):    
    print(n,"is a harshad number")    
else:    
    print(n,"is not a harshad number")



























        


        
