# 0 is included as index 0
def total_digits_in_class(n: int):
  if (n == 1):
    return 10;
  return n * (pow(10,n)-pow(10,n-1))

def get_digit_of_class(class_n: int, index: int):
  remainder = index // class_n
  modulo = index % class_n
  number = (0 if class_n == 1 else pow(10,class_n-1)) + remainder
  number_str = str(number)
  digit = number_str[modulo]
  return digit

def get_digit(index: int):
  class_n = 1
  while (index - total_digits_in_class(class_n) >= 0):
    index -= total_digits_in_class(class_n)
    class_n += 1
  return get_digit_of_class(class_n, index)

ret = 1
for i in [pow(10,j) for j in range(7) ]:
  ret *= int(get_digit(i))
print(ret)