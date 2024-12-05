def check1000(a,b,c):
    return a+b+c == 1000
def checkPytha(a,b,c):
    return a**2+b**2 == c**2

g = ((a,b,1000-a-b) for a in range(1,1001) for b in range(1,1001) if checkPytha(a,b,1000-a-b) and a > 0 and b > 0 and 1000-a-b > 0)
print(g.next())
print(200*375*425)
