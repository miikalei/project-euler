
import itertools 
digits = ['0','1','2','3','4','5','6','7','8','9']

def check_divisibility(n: int, indices: list[int], divisor: int):
  n_str = str(n)
  i = []
  for index in indices:
    i.append(n_str[index - 1])
  return int(''.join(i)) % divisor == 0

division_checks = {
  tuple([2,3,4]): 2,
  tuple([3,4,5]): 3,
  tuple([4,5,6]): 5,
  tuple([5,6,7]): 7,
  tuple([6,7,8]): 11,
  tuple([7,8,9]): 13,
  tuple([8,9,10]): 17,
}

ret = 0
for digit_bundle in itertools.permutations(digits):
  pandigital_str = ''.join(digit_bundle)
  pandigital = int(pandigital_str)
  if pandigital_str[0] != '0' and all(check_divisibility(pandigital, indices, divisor) for indices,divisor in division_checks.items()):
    ret += pandigital

print(ret)

