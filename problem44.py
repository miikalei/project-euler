import math

def triangle_n(n: int):
  return int(n*(3*n-1)/2)

triangle_numbers = {triangle_n(n) for n in range(1,1000000)}
def is_triangle_number(n: int):
  return n in triangle_numbers

def is_triangle_pair(i,j):
  return is_triangle_number(i+j) and is_triangle_number(abs(i-j))

def generate_pairs():
  i=1
  while True:
    for j in range(1,i+1):
      yield (i,j)
    i += 1

ret = math.inf
print('Ready')
for (i,j) in generate_pairs():
  # print(i,j)
  ti = triangle_n(i)
  tj = triangle_n(j)
  # print(ti, tj)
  if is_triangle_pair(ti,tj):
    ret = min(ret, abs(ti-tj))
    print(ret)