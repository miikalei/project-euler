import math
import itertools

def prime_gen():
  """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
  D = {}

  q = 2

  while True:
    if q not in D:
      # q is a new prime.
      # Yield it and mark its first multiple that isn't
      # already marked in previous iterations
      # 
      yield q
      D[q*q] = [q]
    else:
      # q is composite. D[q] is the list of primes that
      # divide it. Since we've reached q, we no longer
      # need it in the map, but we'll mark the next 
      # multiples of its witnesses to prepare for larger
      # numbers
      # 
      for p in D[q]:
        if p+q in D:
          D[p+q].append(p)
        else:
          D[p+q] = [p]
      del D[q]
    q += 1

def is_prime(n):
  if n < 2:
    return False
  if n == 2:
    return True
  if n % 2 == 0:
    return False
  if n == 3:
    return True
  else:
    for num in range(3, math.ceil(math.sqrt(n))+1,2):
      if n % num == 0:
        return False
    return True

primes = [i for i in itertools.takewhile(lambda x: x < 1000000, prime_gen())]
n_primes = len(primes)

print(len(primes))
for l in range(1,n_primes):
  for i in range(n_primes-l):
    prime_slice = primes[i:i+l]
    prime_sum = sum(prime_slice)
    if prime_sum < 1000000 and is_prime(prime_sum):
      print(prime_sum, l, len(prime_slice))