arvo1 = 1
arvo2 = 2
arvo3 = 3
summa = 0
while (arvo3 <= 4000000):
    if arvo3 % 2 == 0:
        summa += arvo3
    arvo1 = arvo2
    arvo2 = arvo3
    arvo3 = arvo1+arvo2
print(summa+2)
