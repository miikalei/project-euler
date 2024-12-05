import itertools;

def triangle(n: int): 
    return int((n*(n+1))/2)

def square(n: int):
    return n*n;

def pentagonal(n):
    return int((n*(3*n-1))/2);

def hexagonal(n):
    return n*(2*n-1);

def heptagonal(n):
    return int((n*(5*n-3))/2);

def octagonal(n):
    return n*(3*n-2);

def is_four_digits(n: int):
    return n >= 1000 and n <= 9999

def is_pair(a: int, b: int):
    a = str(a)
    b = str(b)
    return a[2] == b[0] and a[3] == b[1]

set_names = ['triangle', 'square', 'pentagonal','hexagonal','heptagonal','octagonal']

sets: dict[str,set[int]] = {
    'triangle': [triangle(n) for n in range(1,150) if is_four_digits(triangle(n))],
    'square': [square(n) for n in range(1,150) if is_four_digits(square(n))],
    'pentagonal': [pentagonal(n) for n in range(1,150) if is_four_digits(pentagonal(n))],
    'hexagonal': [hexagonal(n) for n in range(1,150) if is_four_digits(hexagonal(n))],
    'heptagonal': [heptagonal(n) for n in range(1,150) if is_four_digits(heptagonal(n))],
    'octagonal': [octagonal(n) for n in range(1,150) if is_four_digits(octagonal(n))],
};

def find_matches_in_set(setName: str, n: int | None):
    set = sets[setName];
    if n is None:
        return set;
    else: 
        return [s for s in set if is_pair(n,s)]

def dig(currentSequence, setsToVisit):
    if len(setsToVisit) == 0:
        return currentSequence;
    lead = currentSequence[-1] if len(currentSequence) else None;
    next_set = setsToVisit[0]
    for n in find_matches_in_set(next_set, lead):
        found_seq = dig(currentSequence + [n], setsToVisit[1:])
        if (found_seq):
            if (len(found_seq) < 7 or found_seq[0] == found_seq[6]):
                return found_seq
    return None;

def compute():
    sequence = []

    currentSet = set_names[0]
    currentLead = sequence[-1] if len(sequence) else None;
    print(find_matches_in_set(currentSet, currentLead))

for set_seq in itertools.permutations(set_names):
    res = dig([], list(set_seq) + [set_seq[0]])
    if res:
        print("comb",set_seq)
        print(res,sum(res[:-1]))