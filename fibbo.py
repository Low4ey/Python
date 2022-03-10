# dict={1:10,2:20}
# n={3:30,4:40}
# dict.update(n)
# print(dict)
# def add(n):
#     if n==0:
#         return 0
#     else:
#         add1=add(n-1)
#         return n+add1

# print(add(4))


def fibbo(n):
    assert n>=0 and int(n)==n , 'Input is wrong'
    if n==0:
         return 0
    if n in [1,2]:
        return 1
    else:
        return fibbo(n-1)+fibbo(n-2)

print(fibbo(2))