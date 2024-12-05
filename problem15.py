from functools import lru_cache

@lru_cache(maxsize=None)
def recursion(x,y):
    if x==1 and y==1:
        return 1
    elif x==1:
        return recursion(x,y-1)
    elif y==1:
        return recursion(x-1,y)
    else:
        return recursion(x-1,y) + recursion(x,y-1)

print(recursion(21,21))
