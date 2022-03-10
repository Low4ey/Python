temp=[]
ch=int(input("Enter number of days"))
for i in range(1,ch+1):
    day=int(input(f"enter{i}s day highest temperature"))
    temp.append(day)
Avg_temp=sum(temp)/len(temp)
print(f"Average of Temprature is{Avg_temp}")
c=0
for i in temp:
    if Avg_temp>i:
        c+=1
    else:
        pass
print(f"{c} Day(s) above Average Temperature")
