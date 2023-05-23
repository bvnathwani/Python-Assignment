import math

k = int(input("Please enter your number to find the factorial\n"))

if k>0:
        for i in range(1,k):
            k = i*k
        print(k)

elif k == 0:
    print("the value of factorial is 1")

else:

    print("factorial of negative can not  be find out")


