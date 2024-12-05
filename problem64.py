# a+sqrt(n)-a
# = a + 1/(1/(sqrt(n)-a))
# = a + 1/((sqrt(n)+a) / (n - a^2))

# Askel, sqrt(n), lisää a => sqrt(n) + a / n-a^2

# esim sqrt(23) + 4 / 23-16 = (sqrt(23) + 4) / 

from math import floor, sqrt
import itertools

def get_a0(n: int):
    return floor(sqrt(n))

def get_a1(n: int):
    a0 = get_a0(n)
    nominator = n - a0**2

def get_next(n: int, nominator: int, denominator):
    temp_nom = nominator * (sqrt(n)+ denominator)
    temp_den = n - denominator**2
    new_a = floor(temp_nom / temp_den)
    new_nom = int(temp_den / nominator)
    new_den = -(denominator - new_a * new_nom)
    return (new_a, new_nom, new_den)

def get_full(n: int):
    a0 = get_a0(n);
    if a0 ** 2 == n:
        return None;
    nom = 1
    den = a0
    seen = [(a0,nom,den)]
    for i in itertools.count():
        (new_a, new_nom, new_den) = get_next(n, nom, den)
        index_seen = next((i for i, (_,n,d) in enumerate(seen) if n == new_nom and d == new_den), None)
        seen += [(new_a, new_nom, new_den)]
        if index_seen is not None:
            return (seen, len(seen)-index_seen-1)
        nom = new_nom;
        den = new_den;

count = 0
for i in range(2,10_000):
    (_,period) = get_full(i) or (None, None)
    if (period or 2) % 2 == 1:
       print(f"Number {i} has odd {period}-length preiod")
       count += 1
print(f"Total count:",count)