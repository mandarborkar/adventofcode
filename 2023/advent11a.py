def emptygalaxies (BlankArr,x1,x2):
    count=0
    for c in BlankArr:
        if (x1 <= c <= x2) or (x2 <= c <= x1):
            count += 1
    return count

f1 = open("advent11input.txt", "r")
mylist = f1.read().split("\n")
# print(mylist)
galaxies = {}
coordinates = []
rowBlankArr = []
colBlankArr = []
expandfactor = 2
sumdistance = 0

for i in range(0, len(mylist)):
    if (mylist[i].find("#") == -1):
        rowBlankArr.append(i)
    for j in range(0, len(mylist[i])):
        if (mylist[i][j].__eq__("#")):
            coordinates.append((i, j))

for i in range(0, len(mylist[0])):
    switchstr = ''
    for j in range(0, len(mylist)):
        switchstr += mylist[j][i]
    if switchstr.find('#') == -1:
        colBlankArr.append(i)

print('row ', rowBlankArr)
print ('column ',colBlankArr)

distArr = []

for c in coordinates:
    distArr = []
    for c_other in coordinates:
        #print (c, '=', c_other)
        if(c != c_other):
            distance = abs(c[0] - c_other[0]) + abs(c[1] - c_other[1])
            expandrow    = emptygalaxies (rowBlankArr,c[0],c_other[0])
            expandcolumn = emptygalaxies (colBlankArr,c[1],c_other[1])
            # distance = distance + ((expandfactor*expandrow)-1) + ((expandfactor*expandcolumn)-1) + 1
            distance = distance + (1000000*expandrow) + (1000000*expandcolumn) - (expandrow+expandcolumn)
            print(c, c_other, distance)
            sumdistance += distance
            distArr.append(distance)

    print (c,distArr)
    galaxies[c] = min(distArr)
    # sumdistance += min(distArr)

print(galaxies)
print (sumdistance/2)