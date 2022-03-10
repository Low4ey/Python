l1=[9,3,5,8,7,6,2,1,4]
#bubble sort
def bubble_sort(l1):
    for i in range(len(l1)-1):
        for j in range(len(l1)-i-1):
            if l1[j]>l1[j+1]:
                l1[j],l1[j+1]=l1[j+1],l1[j]
    return l1
#Selection Sort
def selection_sort(l1):
    for i in range(len(l1)):
        min_index=i
        for j in range(i+1,len(l1)):
            if l1[min_index]>l1[j]:
                min_index=j
        l1[i],l1[min_index]=l1[min_index],l1[i]
    return l1

#insertion sort
def insertion_sort(l1):
    for i in range(1,len(l1)):
        key=l1[i]
        j=i-1
        while j>=0 and key<l1[j]:
            l1[j+1]=l1[j]
            j-=1
        l1[j+1]=key
    return l1

print(insertion_sort(l1))