def f(x: int, y: int):
    return (2*y+x, x+y)

def g():
    x=3; y=2;
    while True:
        yield (x,y) 
        (x,y)=f(x,y)

def compute():
    count = 0
    for (n,(x,y)) in enumerate(g()):
        print(f"x: {x}")
        print(f"y: {y}")
        if len(str(x))>len(str(y)):
            count += 1
        if n >= 1000:
            return count;

print(compute())