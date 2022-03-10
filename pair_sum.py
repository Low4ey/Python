def pair(list,sum):
    pair_array=[]
    for i in range(len(list)):
        if list[i]+list[i+1]==sum:
            pair_array.append([list[i],list[i+1]])
        else:
            return "No pair Exist"
    return pair_array

print(pair([1,2,1,3,0],3))