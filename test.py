from operator import index


def se(l1,a):
        if a in l1:
            print(index(a))
        if a not in l1:
            print(False)


se([1,7,3,4,5,6],1)