a = [2,4,5,6,7,8]
sum = 0
print(a[0])

for i in range(5):
    sum = sum + a[i]

print(sum)

a = [100, 89, 9, 56, 4, 80, 8]
max_element = a[0]

for i in range(len(a)):
  if a[i] > max_element:
     max_element = a[i]

print (max_element)


def rotateArray(arr, n, d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[: i] + temp
    return arr
 
 
# Driver function to test above function
arr = [1, 2, 3, 4, 5, 6, 7]
print("Array after left rotation is: ", end=' ')
print(rotateArray(arr, len(arr), 2))


def splitArr(arr,n,k): 
    for i in range(0, k): 
        x = arr[0]
        for j in range(0,n-1):
            arr[j] = arr[j + 1]
          
        arr[n-1] = x
          
  
# main
arr = [12, 10, 5, 6, 52, 36]
n = len(arr)
position = 2
  
splitArr(arr, n, position)
  
for i in range(0, n): 
    print(arr[i], end = ' ')


# Python3 program to find sum in Nth group
  
# Check if given array is Monotonic
def isMonotonic(A):
  
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1)))
  
# Driver program
A = [6, 5, 4, 4]
  
# Print required result
print(isMonotonic(A))








        

    






