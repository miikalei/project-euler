a=1; b=1
ind = 2
while(True):
    c = a+b
    a = b
    b = c
    ind += 1
    if len(str(b)) >= 1000:
        break
print(ind)
