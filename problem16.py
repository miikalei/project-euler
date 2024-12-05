def sumOfDigits(number):
    i = 1
    sum = 0
    while (i <= number):
        sum += (number // i) % 10
        i *= 10
    return sum

print(sumOfDigits(2**1000))
