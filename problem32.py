# Generate first all permutation of 9-length strings of symbols from 1 to 9
# Go through all possible locations of equality and product sign

from itertools import permutations

products = set()
perm = permutations([char for char in '123456789'])
for p in perm:
    pstring = ''.join(p)
    for equalitysplit in range(2,8+1):
        leftstr = pstring[0:equalitysplit]
        rightstr = pstring[equalitysplit:]
        for productsplit in range(1,equalitysplit):
            leftnumber = leftstr[0:productsplit]
            rightnumber = leftstr[productsplit:]
            if int(leftnumber) * int(rightnumber) == int(rightstr):
                products.add(int(rightstr))
print(sum(products))
