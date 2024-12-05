def isPalindrome(n):
    n = str(n)
    return n == n[::-1]

print(isPalindrome(998001))

bestsofar = 1
for x in range(100,1000):
    for y in range(100,1000):
        n = x*y
        if isPalindrome(n):
            if n > bestsofar:
                bestsofar = n
print(bestsofar)
