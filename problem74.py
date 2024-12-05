from math import factorial

def next(n: int) -> int:
    return sum([factorial(int(c)) for c in str(n)])

def chain(n: int) -> list[int]:
    chain = [];
    while n not in chain:        
        chain.append(n)
        n = next(n)
    return chain

def compute():
    count = 0
    for n in range(1,1_000_000):
        if len(chain(n)) == 60:
            count += 1
    return count

print(compute())