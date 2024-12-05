import math

numbers = []
for n in range(10,10000000):
    mysum = 0
    for s in str(n):
        mysum += math.factorial(int(s))
    if mysum == n:
        numbers.append(n)
print(numbers)
print(sum(numbers))
