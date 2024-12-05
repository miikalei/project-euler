def prime_factors(n: int):
  i = 2
  factors = []
  while i*i <= n:
    if n % i != 0:
      i += 1
    else:
      n //= i
      factors.append(i)
  if n > 1:
    factors.append(n)
  return factors

def unique_factors(n: int):
  factors = prime_factors(n)
  return set(factors)

def triple_gen():
  i = 1
  while True:
    yield (i,i+1,i+2,i+3)
    i += 1

def triple_is_good(i: int,j: int,k: int, l:int):
  i_factors = unique_factors(i)
  if len(i_factors) != 4:
    return False
  # print(i_factors)
  j_factors = unique_factors(j)
  if len(j_factors) != 4:
    return False
  # print(j_factors)
  k_factors = unique_factors(k)
  if len(k_factors) != 4:
    return False
  # print(k_factors)
  l_factors = unique_factors(l)
  if len(l_factors) != 4:
    return False
  # print(l_factors)
  return True

for (i,j,k,l) in triple_gen():
  if triple_is_good(i,j,k,l):
    print(i)
