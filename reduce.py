from functools import reduce
L = [2,5,6,9]
def qiuji(a,b):
    return a*b
print(reduce(qiuji,L))
