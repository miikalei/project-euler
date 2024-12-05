p = 600851475143
import math

def reduceThis(n):
    maxtest = int(math.sqrt(n))+1
    for i in range(2,maxtest):
        if (n % i == 0):
            return n / i
    return n

q = reduceThis(p)
while p != q:
    p = q
    q = reduceThis(p)

print(q)
