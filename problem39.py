def isTriangle(hyp: int,sidex: int,sidey: int):
    return hyp * hyp == sidex * sidex + sidey * sidey 

def countSolutions(p: int):
    count = 0
    for i in range(1,p):
        for j in range(i,p-i):
            k = p - i - j
            if k > 0 and k >= i and k>= j and k <= p and isTriangle(k,i,j):
                count+= 1
    return count

print(max(range(1,1001), key=countSolutions))