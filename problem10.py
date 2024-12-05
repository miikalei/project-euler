from math import sqrt
def checkPrime(n):
    return all(not (n % i == 0) for i in range(2,int(sqrt(n))+1))

print(sum(a for a in range(2,2000000+1) if checkPrime(a)))
