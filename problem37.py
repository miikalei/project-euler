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

def isPrime(n):
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

def is_truncatable_prime(n):
  s = str(n)
  for i in range(1,len(s)):
    # print(s[i:])
    # print(s[:-i])
    if not isPrime(int(s[i:])):
      return False
    if not isPrime(int(s[:-i])):
      return False
  return True

sum = 0;
for i in prime_gen():
  if i >= 10 and is_truncatable_prime(i):
    sum += i;
    print(sum);