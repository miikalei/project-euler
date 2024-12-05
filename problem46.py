import math


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

def composite_gen():
  i = 2
  for p in prime_gen():
    while i < p:
      yield i
      i+=1
    i+= 1

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
  
def passes_conjecture(c: int):
  n = 1
  while (c - 2*pow(n,2) > 0):
    if is_prime(c - 2*pow(n,2)):
      return True
    n += 1;
  return False

for c in composite_gen():
  if c % 2 == 1 and not passes_conjecture(c):
    print(c)
    break