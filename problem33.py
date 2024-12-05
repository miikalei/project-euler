## ab/cd=a/d, not cases where b or d is 0, or c=0.
# => d*ab = a*cd.
fractions = []
for cd in range(11,100):
    for ab in range(11,cd):
        if cd % 10 == 0 or ab % 10 == 0:
            continue
        a = ab // 10
        b = ab % 10
        c = cd // 10
        d = cd % 10
        if b != c:
            continue
        if d*ab == a*cd:
            fractions.append((ab,cd))
print(fractions)
up = 1
down = 1
for (upp,downn) in fractions:
    up *= upp
    down *= downn
print((up,down))
from fractions import Fraction
print(Fraction(up,down))
