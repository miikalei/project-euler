ITERATION_LIMIT = 50

def reverse(n: int) -> int:
    return int(str(n)[::-1])

def is_palindrome(n: int):
    return n == reverse(n)

def is_lychrel(n: int) -> bool:
    for i in range(ITERATION_LIMIT):
        n = n + reverse(n)
        if is_palindrome(n):
            return False
    return True

def compute():
    count = 0
    for n in range(1,10_000):
        if is_lychrel(n):
            count += 1
    return count

print(compute())