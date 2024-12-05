from math import sqrt
def sumOfDivisors(n):
    if n==1: return 0
    r = int(sqrt(n))
    if r*r == n:
        sum = 1+r
        r = r-1
    else:
        sum = 1
    if n % 2 == 1:
        f = 3
        step = 2
    else:
        f = 2
        step = 1
    while f <= r:
        if n % f == 0:
            sum += f+(n//f)
        f += step
    return int(sum)

def isAbundant(n):
    if sumOfDivisors(n) > n:
        return True
    else:
        return False

def canBeWrittenAsAbundantSum(n):
    for i in range(1,n//2+1):
        if isAbundant(i) and isAbundant(n-i):
            return True
    return False

summa = 0
for n in range(1,28123):
    if not canBeWrittenAsAbundantSum(n):
        summa += n
print(summa)
