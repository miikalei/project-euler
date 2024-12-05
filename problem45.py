def triangle_n(n: int):
  return int(n*(n+1)/2)
def pentagonal_n(n: int):
  return int(n*(3*n-1)/2)
def hexagonal_n(n: int):
  return int(n*(2*n-1))

triangles = {triangle_n(n) for n in range(100000)}
pentagons = {pentagonal_n(n) for n in range(100000)}
hexagons = {hexagonal_n(n) for n in range(100000)}

def gen_n():
  i = 1
  while True:
    yield triangle_n(i)
    i+= 1

def is_valid(n: int):
  return n in pentagons and n in hexagons

for n in gen_n():
  if is_valid(n):
    print(n)