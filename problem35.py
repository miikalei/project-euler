from math import sqrt
def checkPrime(n):
    return all(not (n % i == 0) for i in range(2,int(sqrt(n))+1))

def allRotsArePrime(n):
    s = str(n)
    return all(checkPrime(int(s[i:]+s[:i])) for i in range(len(s)))

print(len([n for n in range(2,1000000+1) if allRotsArePrime(n)]))
