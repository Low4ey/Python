def arr(arr1):
    if len(arr1) ==0:
        return 1
    else:
        return arr1[0]*arr(arr1[1:])

print(arr([2,3,4,5]))