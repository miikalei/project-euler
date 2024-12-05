def subsets(n: int, r: int) -> int:
    tot = 1
    for i in range(n-r+1,n+1):
        tot *= i
    for i in range(1,r+1):
        tot /= i
    return int(tot)

def compute():
    ret = 0
    for n in range(1,100+1):
        for r in range(0,n+1):
            if (subsets(n,r) > 1_000_000):
                ret += 1
    return ret

print(compute())