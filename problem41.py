digits = [1,2,3,4,5,6,7,8,9]
def is_pandigital(n):
  digit_count = len(str(n))
  return digit_count <= 9 and all((str(d) in str(n) for d in digits[:digit_count]))

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

for i in prime_gen():
  if is_pandigital(i):
    print(i)