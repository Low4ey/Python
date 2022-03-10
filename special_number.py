from math import gcd

def ans(x):
    x = str(x)
    sum = 0
    prod = 1
    for i in x:
        sum += int(i)**4
        prod *= int(i)
    if gcd(sum,prod) != 1:
        return True
    else:
        return False

for _ in range(int(input())):
    result = 0
    for i in range(1,int(input()) + 1):
        if ans(i):
            result += 1
    print(result)

