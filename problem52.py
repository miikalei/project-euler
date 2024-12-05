def inf_gen():
  i = 1
  while True:
    yield i
    i += 1

def same_digits(a: int, b: int):
  a_str = str(a)
  b_str = str(b)
  a_set = {c for c in a_str}
  b_set = {c for c in b_str}
  return a_set == b_set

def is_good(i: int):
  return all([same_digits(i, multi * i) for multi in range(1,7)])

def compute():
  for i in inf_gen():
    if (is_good(i)):
      return i

print(compute())