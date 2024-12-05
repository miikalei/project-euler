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

def get_len(i: int):
  return len(str(i))

def sequence_gen():
  for i in prime_gen():
    for a in range(2,5000):
      j = i + a
      k = i + a + a
      yield (i,j,k)

def triple_length_is_good(i:int,j:int,k:int):
  return get_len(i) == 4 and get_len(j) == 4 and get_len(k) == 4

def triple_are_prime(i,j,k):
  return is_prime(j) and is_prime(k)

def triple_are_permutations(i,j,k):
  i_str = sorted(str(i))
  j_str = sorted(str(j))
  k_str = sorted(str(k))
  return i_str == j_str and j_str == k_str

for (i,j,k) in sequence_gen():
  if triple_length_is_good(i,j,k) and triple_are_prime(i,j,k) and triple_are_permutations(i,j,k):
    print(i,j,k)