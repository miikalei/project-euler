def isPalindrome(s):
    return s[::-1]==s

sum = 0
for n in range(1,1000000):
    s10 = str(n)
    s2 = bin(n)[2:]

    if isPalindrome(s10) and isPalindrome(s2):
        sum += n
print(sum)
