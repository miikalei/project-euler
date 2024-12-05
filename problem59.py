from typing import List

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def generate_keys():
    for a in alphabet:
        for b in alphabet:
            for c in alphabet:
                yield "".join([a,b,c])

def compute():
    with open('problem59.txt') as file:
        codes = []
        for line in file:
            codes.extend([int(c) for c in line.split(',')])
        for key in generate_keys():
            plaintext = to_plaintext(xor_all(codes, to_codes(key)))
            if "An extract" in plaintext:
                print(sum([ord(c) for c in plaintext]))

def to_codes(chars: List[chr]):
    return [ord(c) for c in chars]

def to_ascii(codes: List[int]):
    return [chr(c) for c in codes]

def to_plaintext(chars: List[int]):
    return "".join(to_ascii(chars))

def xor(code: int, key: int):
    return code ^ key

def xor_all(codes: List[int], key: List[int]):
    # Repeat the procedure, where each len(key) window is created
    output = []
    offset = 0
    while offset < len(codes):
        char_key = key[offset % len(key)]
        output.append(xor(codes[offset], char_key))
        offset += 1
    return output

compute()