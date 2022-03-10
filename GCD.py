def gcd(m,n):
    assert n>=0 and int(n)==n, 'Invalid input'
    if n==0:
        return m
    else:
        return gcd(n,m%n)
print(gcd(86,43))