# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/
from functools import cache
from itertools import takewhile
from math import ceil, sqrt


def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}
    
    # The running integer that's checked for primeness
    q = 2
    
    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            # 
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            # 
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        
        q += 1

primes = list(takewhile(lambda x: x < 1_000_000,gen_primes()))

@cache
def totient(n: int) -> int:
    if (n == 1):
        return 1;
    for p in primes:
        if p >= ceil(sqrt(n)):
            return n-1
        if n % p == 0:
            f_count = factor_count(n, p)
            return (p ** (f_count - 1)) * (p-1) * totient(n // (p ** f_count))
    return 0;

def factor_count(n: int, p: int) -> int:
    count = 0
    while n % p == 0:
        count += 1
        n = n // p
    return count;

def is_symmetric(n1: int, n2: int) -> bool:
    return ''.join(sorted(str(n1))) == ''.join(sorted(str(n2)))

def compute():
    min_value = 1000
    min_n = 2
    for n in range(2,10_000_000):
        t = totient(n)
        value = n / t
        if is_symmetric(t,n) and value < min_value:
            min_value = value
            min_n = n
    return min_n

print(compute())