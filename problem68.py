from itertools import permutations


def listIsOk(a: list[int]) -> bool:
    if len(a) != 10:
        return False;
    sums = [a[i % 10] + a[(i+1) % 10] + a[(i+3) % 10] for i in range(0,10,2)]
    return all(s == sums[0] for s in sums)

def listIsMinimal(a: list[int]) -> bool:
    return all(a[0] <= a[i] for i in range(2,10,2))

def minimalListToNumber(a: list[int]):
    indices = [0,1,3,2,3,5,4,5,7,6,7,9,8,9,1]
    numbers = [a[i] for i in indices]
    return int("".join([str(n) for n in numbers]))

for i in permutations(range(1,11)):
    if listIsOk(list(i)) and listIsMinimal(list(i)):
        n = minimalListToNumber(list(i))
        print(f"{list(i)}, as number: {n}, length {len(str(n))}")