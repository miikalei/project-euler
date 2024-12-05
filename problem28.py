line1 = [3,13]
line2 = [5,17]
line3 = [7,21]
line4 = [9,25]

toAdd = 25
for i in range(5,1001,2):
    toAdd += i + 1
    line1.append(toAdd)
    toAdd += i + 1
    line2.append(toAdd)
    toAdd += i + 1
    line3.append(toAdd)
    toAdd += i + 1
    line4.append(toAdd)

print(sum(line1)+sum(line2)+sum(line3)+sum(line4)+1)
