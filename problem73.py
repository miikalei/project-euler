from math import ceil, floor, gcd

lower_target = 1/3
upper_target = 1/2

def find_greatest_numerator(d: int):
    i = floor(upper_target * d)
    if (i / d == upper_target):
        i -= 1
    while gcd(i,d) != 1:
        i -= 1
    return i

def find_lowest_numerator(d: int):
    i = ceil(lower_target * d)
    if (i / d == lower_target):
        i += 1
    while gcd(i,d) != 1:
        i += 1
    return i

def count_fractions(d: int):
    lower_n = find_lowest_numerator(d)
    upper_n = find_greatest_numerator(d)
    count = 0
    for n in range(lower_n, upper_n+1):
        if gcd(n, d) == 1:
            count += 1
    return count

def compute():
    count = 0
    for d in range(2,12_000+1):
        count += count_fractions(d)
    return count

print(compute())