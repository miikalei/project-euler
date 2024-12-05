numberdict = {
    0 : '',
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
    10 : 'ten',
    11 : 'eleven',
    12 : 'twelve',
    13 : 'thirteen',
    14 : 'fourteen',
    15 : 'fifteen',
    16 : 'sixteen',
    17 : 'seventeen',
    18 : 'eighteen',
    19 : 'nineteen',
    20 : 'twenty',
    30 : 'thirty',
    40 : 'forty',
    50 : 'fifty',
    60 : 'sixty',
    70 : 'seventy',
    80 : 'eighty',
    90 : 'ninety',
    1000 : 'onethousand'
}

# ensin 20-99:
for i in [2,3,4,5,6,7,8,9]:
    for k in [1,2,3,4,5,6,7,8,9]:
        numberdict[ i*10+k] = numberdict[10*i] + numberdict[k]
#tasasadat:
for i in [1,2,3,4,5,6,7,8,9]:
    numberdict[i*100] = numberdict[i] + 'hundred'
# sitten 100-999:
for i in [1,2,3,4,5,6,7,8,9]:
    for k in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]:
        numberdict[i*100 + k] = numberdict[i] + 'hundred' + 'and' + numberdict[k]
    for j in [2,3,4,5,6,7,8,9]:
        for k in [0,1,2,3,4,5,6,7,8,9]:
            numberdict[i*100+j*10+k] = numberdict[i]+'hundred'+'and'+numberdict[10*j]+numberdict[k]

summa = 0
for n in range(1,1001):
    summa += len(numberdict[n])
print(summa)
