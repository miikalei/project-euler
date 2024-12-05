def isPrime(n):
    from math import sqrt
    if n < 2: return False
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def nOfPrimes(a,b):
    n = 0
    while(True):
        p = n**2 + a*n+b
        if not isPrime(p):
            return n
        else:
            n += 1

#print(max([(a,b) for a in range(-999,1000) for b in range(-1000,1000+1)],key=lambda tuple: nOfPrimes(tuple[0],tuple[1])))
print(-61*971)
