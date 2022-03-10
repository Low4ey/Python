def pow_num(m,n):
    assert n>=0 and int(n)==n, 'Invalid input'
    if n==0:
        return 1
    if n==1:
        return n
    else:
        return m*pow_num(m,n-1)
print(pow_num(3,6))