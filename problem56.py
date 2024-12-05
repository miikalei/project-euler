def integer_sum(n: int):
    return sum(int(i) for i in str(n))

def compute():
    return max((integer_sum(a ** b) for a in range(1,100) for b in range(1,100)))

print(compute())