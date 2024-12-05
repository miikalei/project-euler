from math import sqrt

def checkPrime(n):
    return all(not (n % i == 0) for i in range(2,int(sqrt(n))+1))

count = 1
n = 3
while (count < 10001):
    if checkPrime(n)==True:
        count += 1
        print(n)
    n += 2
