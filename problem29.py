data = [a**b for a in range(2,100+1) for b in range(2,100+1)]
noDups = list(set(data))
print(len(noDups))
