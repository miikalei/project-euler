# a^2 + b^2 = c^2 
# a + c + b = n

# How many ways to form n = k*(m^2 + n^2)

from math import ceil, gcd, sqrt

max_L = 1_500_000

def count_solutions():
    counts = {}
    for m in range(1,ceil(sqrt(max_L))+3):
        for n in range(1,ceil(sqrt(max_L))+1):
            if m>n and gcd(m,n) == 1 and (not (m % 2 == 1 and n % 2 == 1)):
                x1=m**2 - n**2
                x2=2*m*n
                x3=m**2+n**2
                s = x1+x2+x3
                for k in range(1,(max_L // s) + 3):
                    val = k*s
                    counts[val] = counts.get(val, 0) + 1;
    return counts

def find_ones(d: dict[int,int]):
    return len([k for (k,v) in d.items() if k<=max_L and v == 1])

def compute():
    solutions = count_solutions()
    return find_ones(solutions)

print(compute())