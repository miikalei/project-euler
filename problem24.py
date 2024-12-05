from itertools import permutations

it = permutations(range(10))
a = next(x for i,x in enumerate(it) if i==1000000-1)
print(a)
