A = [[12,7,3],

    [4 ,5,6],

    [7 ,8,9]]

B = [[5,8,1],

    [6,7,3],

    [4,5,9]]

result = [[0,0,0],

         [0,0,0],

         [0,0,0]]

# iterate through rows

for x in range(len(A)):

   # iterate through columns

   for y in range(len(A[0])):

       result[x][y] = A[x][y] + B[x][y]

for q in result:

   print(q)


# Python program to add two matrix user inputs

# Python program to add two matrices user input

r = int(input("Enter the rows: "))
c = int(input("Enter the columns: "))

print("Enter Matrix 1:")
m1 = [[int(input()) for i in range(c)] for i in range(r)]
print("Matrix 1 is: ")
for n in m1:
   print(n)

print("Enter Matrix 2:")
m2 = [[int(input()) for i in range(c)] for i in range(r)]
for n in m2:
   print(n)

r = [[0 for i in range(c)] for i in range(r)]
for i in range(len(r)):
   for j in range(c):
      r[i][j] = [m1[i][j] + m2[i][j]]
print("Add Matrix:")
for i in r:
   print(i)


rows = int(input("Enter the Number of rows :" ))
column = int(input("Enter the Number of Columns:"))

print("Enter the elements of Matrix:")
matrix= [[int(input()) for i in range(column)] for i in range(rows)]
print("-------Your  Matrix is---------")
for n in matrix:
    print(n)

#result matrix of column*row  dimension

result =[[0 for i in range(rows)] for j in range(column)]

#transpose the matrix
rows = int(input("Enter the Number of rows : " ))
column = int(input("Enter the Number of Columns: "))

print("Enter the elements of Matrix:")
matrix= [[int(input()) for i in range(column)] for i in range(rows)]
print("-------Your  Matrix is---------")
for n in matrix:
    print(n)

#result matrix of column*row  dimension

result =[[0 for i in range(rows)] for j in range(column)]

#transpose the matrix
for r in range(rows):
   
   for c in range(column):
       #here we are grabbing the row data of matrix and putting it in the column on the result
       result[c][r] = matrix[r][c]

print("Transpose matrix is: ")
for r in result:
    print(r)


#sort words
# Program to sort alphabetically the words form a string provided by the user

my_str = "Hello this Is an Example With cased letters"

# To take input from the user
#my_str = input("Enter a string: ")

# breakdown the string into a list of words
words = [word.lower() for word in my_str.split()]

# sort the list
words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
   print(word)

# define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = "Hello!!!, he said ---and went."

# To take input from the user
# my_str = input("Enter a string: ")

# remove punctuation from the string
no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char

# display the unpunctuated string
print(no_punct)

# Python3 code to demonstrate working of 
# Extract Unique values dictionary values
# Using chain() + sorted() + values()
from itertools import chain
  
# initializing dictionary
test_dict = {'gfg' : [5, 6, 7, 8],
             'is' : [10, 11, 7, 5],
             'best' : [6, 12, 10, 8],
             'for' : [1, 2, 5]}
  
# printing original dictionary
print("The original dictionary is : " + str(test_dict))
  
# Extract Unique values dictionary values
# Using chain() + sorted() + values()
res = list(sorted(set(chain(*test_dict.values()))))
  
# printing result 
print("The unique values list is : " + str(res))

def returnSum(myDict):
 
    list = []
    for i in myDict:
        list.append(myDict[i])
    final = sum(list)
 
    return final
 
 
























































