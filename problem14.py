import functools

@functools.lru_cache(maxsize=None)
def recursion(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return recursion(n/2)+1
    else:
        return recursion(3*n+1)+1

gen = ((recursion(i),i) for i in range(500000,1000000))
print(max(gen))
