def recurringCycleString(numerator,denominator):
    recurringString = ""
    alreadySeenRems = {}
    rem = numerator % denominator
    while( rem != 0 and rem not in alreadySeenRems):
        alreadySeenRems[rem] = len(recurringString)
        rem = rem*10
        toAdd = rem // denominator
        recurringString += str(toAdd)
        rem = rem % denominator
    if rem == 0:
        return ""
    else:
        return recurringString[-alreadySeenRems[rem]:]

print(max([(n,recurringCycleString(1,n)) for n in range(1,1000)],key=lambda x: len(x[1])))
