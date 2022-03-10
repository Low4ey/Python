from array import *
arr1=array("i",[1,2,3,4,5,6,7])

#traversing in array
for i in arr1:
    print(i,end=" ")
#accessing values through index values
for i in range(0,len(arr1)):
    print(arr1[i],end=" ")
#appending value in array
arr1.append(8)
#inserting value in array
arr1.insert(0,0)
#extending array
arr1.extend([8,9])
#adding items in array from list
arr1.fromlist([10,11])
#removing element from array
arr1.remove(0)
#removing last element from array
arr1.pop()
#printing index of items in array
arr1.index(4)
#reversing array
arr1.reverse()
#counting number of items occurance in array
arr1.count(3)
#converting array to string
arr_string=arr1.tostring()
#coverting array to list
arr_list=arr1.tolist()
#slice array
arr1[1:4]

print(arr_list)