# Lisää 1 jokaiseen uniikkiin numeroon, tai lisää 1 perään: + prev + 1

# 1: 1: 1
# 2: 1+1, 2: 2
# 3: 1+1+1, 2+1, 3: 3
# 4: 1+1+1+1, 2+1+1, 2+2, 3+1, 4: 5
# 5: 1+1+1+1+1, 2+1+1+1, 2+2+1, 3+1+1, 3+2, 4+1, 5: 7

from functools import cache

@cache
def sum_count(n: int, max_a: int) -> list[list[int]]:
    if n <= 0:
        return [];
    if n == 1:
        return [[1]];
    if max_a == 1:
        return [[1 for _ in range(n)]]
    lowers: list[list[int]] = [[x1]+x2 for x1 in range(1,max_a+1) for x2 in sum_count(n-x1, x1)]
    if max_a == n:
        return [[n]] + lowers
    else:
        return lowers

print(sum_count(100,100))