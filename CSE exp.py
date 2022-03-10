#INPUT COMMAND
name=input("enter your name")

#OUTPUT COMMAND
print(name)

#conditional statements
age=int(input("enter your age:"))
if age>=18:
    print("you are elgible to vote")
elif age<18:
    print("you are npt eligible to vote")
else:
    print("invalid input")

#For loop with continue and break
for i in "Python":
    if i=="o":
        print(i)
        break
    else:
        continue
#Program to find Factorial
def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num-1)

#creating 1-D array
from array import *
arr1=array("i",[1,2,3,4,5,6,7])
print(arr1)

#adding 2-D array
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]


for i in range(len(X)):
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)