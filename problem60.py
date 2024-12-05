import itertools
from math import sqrt
from typing import List, Set
# Find a set of 5 primes, so that concatenating any 2 of them produces a prime.
# Return their sum

# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/
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

def isPrime(n):
    return all(not (n % i == 0) for i in range(2,int(sqrt(n))+1))

def pairIsGood(a: int, b:int):
    return isPrime(int(f"{a}{b}")) and isPrime(int(f"{b}{a}"))

# Check that all internal primes are ok
def setIsGood(set: List[int]):
    return all([isPrime(int(f"{a}{b}")) for (a,b) in itertools.permutations(set, 2)])

def can_add_to_set(set: set[int], candidate:int):
    if candidate in set:
        return False
    return all((pairIsGood(candidate, s) for s in set))

def find_n_set(n: int, s: set[int]) -> set[int] | None:
    if len(s) == n:
        return s
    g = gen_primes()
    for i in itertools.takewhile(lambda x: x <= max(list(s), default=0), g):
        pass
    for candidate in itertools.takewhile(lambda x: x <= currentMax, g):
        if can_add_to_set(s,candidate):
            s.add(candidate)
            f = find_n_set(n, s)
            if f is not None:
                return f
            else:
               s.remove(candidate)
    return None

def find_n_set_greedy(n: int, s: set[int]) -> set[int] | None:
    if len(s) == n:
        return s
    g = gen_primes()
    for i in itertools.takewhile(lambda x: x <= max(list(s), default=0), g):
        pass
    for candidate in itertools.takewhile(lambda x: x <= currentMax, g):
        if can_add_to_set(s,candidate):
            s.add(candidate)
            if len(s) == n:
                return s
    return None
            
currentMax = 10000
print(find_n_set(5, set()))
# print(find_n_set_greedy(4, {9,13}))