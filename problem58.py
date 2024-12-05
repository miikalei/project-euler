import itertools
from math import sqrt

def corner_numbers():
    n = 1
    diff = 2
    while True:
        for i in range(4):
            n += diff
            yield n
        diff += 2

def isPrime(n):
    return all(not (n % i == 0) for i in range(2,int(sqrt(n))+1))

def compute():
    layer = 1
    all_corners = 0
    prime_corners = 0
    g = corner_numbers()
    while True:
        numbers = list(itertools.islice(g,4))
        all_corners += len(numbers)
        prime_corners += len([x for x in numbers if isPrime(x)])
        ratio = prime_corners / (all_corners+1)
        print(ratio)
        if ratio < 0.10:
            return layer
        layer += 1

print(2*compute()+1)

# for i in itertools.islice(corner_numbers(),20):
#     if isPrime(i):
#         print(i)