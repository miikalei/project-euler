def fact(n):
    prod = 1
    for i in range(1,n+1):
        prod *= i
    return prod

print(sum([int(i) for i in str(fact(100))]))
