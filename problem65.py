import itertools

def seq_to_quotient(seq: list[int]) -> tuple[int, int]:
    if (len(seq) == 1):
        return (seq[0],1)
    c = seq[0]
    (nom, den) = seq_to_quotient(seq[1:])
    # (c + 1/(nom/den))
    # (c + den/nom)
    # (c*nom + den)/ nom
    return (c*nom+den, nom)

seq_e = [2,1,2,1,1,4,1,1,6,1,1]

def seq_e():
    yield 2;
    yield 1;
    i = 1
    while True:
        yield 2*i
        yield 1
        yield 1
        i += 1;

seq = itertools.islice(seq_e(),100);
print(sum([int(d) for d in str(seq_to_quotient(list(seq))[0])]))