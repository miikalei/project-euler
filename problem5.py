def gcd(a,b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def lcm(a,b):
    return a*b/gcd(a,b)

from functools import reduce

xlist = range(1,21)
lcm_total = reduce(lambda x,y: lcm(x,y), xlist)
print(lcm_total)
