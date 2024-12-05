digits = [1,2,3,4,5,6,7,8,9]
def is_pandigital(n):
  return len(str(n)) == 9 and all((str(d) in str(n) for d in digits))

def prod(i,n):
  ret = ""
  for k in range(1,n+1):
    ret = ret + str(i * k)
  return int(ret)

print(prod(192,3))
max = 0;
for n in range(2,999999999):
  for i in range(1,99999):
    if is_pandigital(prod(i,n)):
      if prod(i,n) > max:
        max = prod(i,n)
        print(max)