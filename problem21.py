def d(n):
    summa=0
    for i in range(1,n):
        if n % i == 0:
            summa += i
    return summa

summa = 0
for n in range(1,10000+1):
    n2 = d(n)
    if n2 != n and d(n2)==n:
        summa += n
print(summa)
