def triangleNumber(n):
    return n*(n+1)/2

from math import sqrt
def numberOfFactors(n):
    if n == 2:
        return 2
    else:
        return sum(1 for i in range(1,int(sqrt(n))) if n % i == 0)*2 + (1 if n % int(sqrt(n)) == 0 else 0)

n = 0
keepGoing = True
while keepGoing:
    n+=1
    k = numberOfFactors(triangleNumber(n))
    if k > 500: keepGoing = False
print(triangleNumber(n))
