def sum_dig(n):
    assert n>=0 and int(n)==n, 'Invalid input'
    if n==0:
        return n
    else:
        return int(n%10) + sum_dig(int(n//10))


print (sum_dig(343))