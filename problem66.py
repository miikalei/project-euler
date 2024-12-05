# Solves smallest integer x so that x^2 = 1 + Dy^2 for some integer y^2.
from itertools import count
import itertools
from math import floor, sqrt

# The solutions are among continued fractions

def get_next(n: int, nominator: int, denominator):
    temp_nom = nominator * (sqrt(n)+ denominator)
    temp_den = n - denominator**2
    new_a = floor(temp_nom / temp_den)
    new_nom = int(temp_den / nominator)
    new_den = -(denominator - new_a * new_nom)
    return (new_a, new_nom, new_den)

def get_a0(n: int):
    return floor(sqrt(n))

def get_full(n: int):
    a0 = get_a0(n);
    if a0 ** 2 == n:
        return None;
    nom = 1
    den = a0
    seen = [(a0,nom,den)]
    for i in itertools.count():
        (new_a, new_nom, new_den) = get_next(n, nom, den)
        seen_before = len([i for i, (_,n,d) in enumerate(seen) if n == new_nom and d == new_den]) >= 2
        seen += [(new_a, new_nom, new_den)]
        if seen_before:
            break;
        nom = new_nom;
        den = new_den;
    return [x[0] for x in seen];

def seq_to_quotient(seq: list[int]) -> tuple[int, int]:
    if (len(seq) == 1):
        return (seq[0],1)
    c = seq[0]
    (nom, den) = seq_to_quotient(seq[1:])
    # (c + 1/(nom/den))
    # (c + den/nom)
    # (c*nom + den)/ nom
    return (c*nom+den, nom)

def check_solution(x:int, y:int, D:int) -> bool:
    return x**2 - D*(y**2) == 1

def minimal_solution(D: int) -> int | None:
    seq = get_full(D)
    if seq is None:
        return None
    for i in range(1,len(seq)+1):
        (c_num,c_den) = seq_to_quotient(seq[:i])
        if check_solution(c_num, c_den, D):
            return (c_num)
    return None;

def integer_root(y) -> int | None:
    sr = sqrt(y)
    sr_int = round(sr)
    if (sr_int ** 2 == y):
        return sr_int
    else:
        return None;

def compute():
    max_minimal_x = 3
    max_minimal_D = 2
    for D in range(1,1001):
        if integer_root(D) is not None:
            continue;
        minimal_x = minimal_solution(D)
        if minimal_x is not None and minimal_x > max_minimal_x:
            max_minimal_x = minimal_x;
            max_minimal_D = D
        print(f"D={D}  min_x={minimal_x}")
    print(F"Max found={max_minimal_x} on D={max_minimal_D}")

compute()