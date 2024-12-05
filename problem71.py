from math import floor, gcd


target = 3 / 7

def find_closest_numerator(d: int):
    i = floor(target * d)
    if (i / d == target):
        i -= 1
    while gcd(i,d) != 1:
        i -= 1
    return i

def compute():
    max_value = 0
    max_n = 0
    max_d = 0
    for d in range(2,1_000_000):
        n = find_closest_numerator(d)
        if (n / d) > max_value:
            max_value = n/d
            max_n = n
            max_d = d
    return (max_n, max_d)

print(compute())