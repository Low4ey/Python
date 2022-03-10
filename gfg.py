N=int(input())
l1=[]
for i in range(0,N):
    pas=input()
    l1.append(pas)

for i in l1:
    for j in i:
        if j.isnumeric() & j.islower() & j.isupper():
            print("YES")
        else:
            print("NO") 
    