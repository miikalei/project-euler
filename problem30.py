def isSumOfPowers(n):
    return n == sum(int(c)**5 for c in str(n))

l = []
for n in range(2,1000000):
    if isSumOfPowers(n):
        l.append(n)
print(sum(l))
