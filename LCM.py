a = int(input("Enter the first numbers to find the LCM\n"))

b = int(input("Enter the second number to find the LCM\n"))
i=1
if i<=a and i<=b: 
        if a%i == 0 and b%i==0:
            print("gcd of two number is given by",i)
            break
            
