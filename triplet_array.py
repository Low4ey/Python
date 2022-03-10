def triplet_counter(arr):
    counter=0
    for i in range(0,len(arr)-2):
        if arr[i]==arr[i+1]==arr[i+2]:
            counter+=1
        if arr[i]==arr[i+1]-1==arr[i+2]-2 or arr[i]==arr[i+1]+1==arr[i+2]+2 :
            counter+=1
    return counter

print(triplet_counter([3,3,3,2,1]))
        