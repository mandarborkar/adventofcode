def printGrind (grid) :
    print ('Printing grid...')
    for x in grid:
        print(x)

f1 = open("/Users/mborkar/PycharmProjects/adventofcode/2021/avent5ainput.txt", "r")
myCoordinates = f1.readlines()
proCoordinates = [[]]
workCoordinates = [[[]]]
finalCoordinates = [[[]]]
coorgrid = []

proCoordinates.pop(0)
workCoordinates.pop(0)

for i in range(0, len(myCoordinates)):
    myCoordinates[i] = myCoordinates[i].replace ( '\n', '' )
    proCoordinates.append ( myCoordinates[i].split (" -> "))
    workCoordinates.append (proCoordinates[i][0].split (","))
    workCoordinates.append (proCoordinates[i][1].split (","))

finalCoordinates.pop(0)
for i in range (0,len(workCoordinates),2):
    # if ((workCoordinates[i][0] == workCoordinates[i+1][0]) or (workCoordinates[i][1] == workCoordinates[i+1][1]) ):
        finalCoordinates.append(workCoordinates[i])
        finalCoordinates.append(workCoordinates[i+1])
        print(str(i) + ' ' + str(finalCoordinates[i:i+2]))


print ('length = ' + str(len(finalCoordinates)))

coorgrid.append (max(finalCoordinates))
#print (coorgrid[0][0])
#print (coorgrid[0][1])

if coorgrid[0][0] > coorgrid[0][1 ] :
    gridSize = int(coorgrid[0][0])+2
else:
    gridSize = int(coorgrid[0][1])+2

VentGrid = [[]]
VentGrid = [[0 for i in range(gridSize)] for j in range(gridSize)]
VentGrid.pop(0)
# printGrind(VentGrid)

for i in range (0,len(finalCoordinates),2):
    x1 = int(finalCoordinates[i][0])
    y1 = int(finalCoordinates[i][1])
    x2 = int(finalCoordinates[i+1][0])
    y2 = int(finalCoordinates[i+1][1])

    print (i)
    print(finalCoordinates[i:i + 2])
    print('x1 = ' + str(x1) + ' y1 = ' + str(y1) + ' x2 = ' + str(x2) + ' y2 = ' + str(y2))

    if x1 == x2 :
        if y1 > y2:
            temp = y1;
            y1 = y2;
            y2 = temp
        for j in range (y1,y2+1,1):
            print ('x1 = ' + str(x1) + ' ' + str(j) + ' ' + ' y1 = ' + str(y1) + ' y2 = ' + str(y2)  + ' grid = ' + str(VentGrid[j][x1]))
            VentGrid[j][x1] += 1
    elif y1 == y2 :
        if x1 > x2:
            temp = x1;
            x1 = x2;
            x2 = temp
        for j in range(x1, x2+1,1):
            print ('y1 = ' + str(y1) + ' ' + str(j) + ' ' + ' x1 = ' + str(x1) + ' x2 = ' + str(x2) + ' grid = ' + str(VentGrid[y1][j]))
            VentGrid[y1][j] += 1
    else : # if x1 == y2 and x2 == y1 :
        print ( 'found dia')
        if x1 > x2:
            temp = x1;
            x1 = x2;
            x2 = temp
            temp = y1
            y1 = y2
            y2 = temp
        if y2 > y1 :
            slope = 1
        else :
            slope = -1
        i = x1
        j = y1
        while (i <= x2):
            print('dia j = ' + str(j) + ' i = ' + str(i) + ' grid = ' + str(VentGrid[j][i]))
            VentGrid[j][i] += 1
            i += 1
            j += slope

printGrind(VentGrid)
overlapcount = 0

for i in range (0,len(VentGrid)):
    for j in range (0,len(VentGrid)):
        if VentGrid [i][j] > 1 :
            overlapcount += 1
print ('Overlap count = ' + str(overlapcount))