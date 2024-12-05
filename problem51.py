import itertools
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

def replace_digits(p: int, indices: list[int], d: int):
  p_str = str(p)
  ret = ''
  for i in range(len(p_str)):
    if i in indices:
      ret += str(d)
    else:
      ret += p_str[i]
  return int(ret)

def index_subsets(n: int):
  return [list(subset) for length in range(1, n+1) for subset in itertools.combinations(range(n), length)]

def count_max_family(p: int):
  max_count = 0
  p_str = str(p)
  for index_subset in index_subsets(len(p_str)):
    prime_count = 0
    # print("Trying", index_subset)
    for d in range(0,10):
      # replace index subset
      p_replaced = replace_digits(p, index_subset, d)
      if is_prime(p_replaced) and len(str(p_replaced)) == len(p_str):
        print("Counted", p_replaced)
        prime_count += 1
    print("And that makes", prime_count)
    if prime_count >= max_count:
      max_count = prime_count
  return max_count


def compute():
  for p in prime_gen():
    c = count_max_family(p)
    if c == 8:
      return p      
    
print(count_max_family(120383))
# print(compute())