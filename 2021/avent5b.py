f1 = open("/Users/mborkar/PycharmProjects/adventofcode/2021/avent5ainput.txt", "r")
myCoordinates = f1.readlines()
proCoordinates = [[]]
finalCoordinates = [[[]]]
proCoordinates.pop(0)
finalCoordinates.pop(0)

for i in range(0, len(myCoordinates)):
    myCoordinates[i] = myCoordinates[i].replace ( '\n', '' )
    proCoordinates.append ( myCoordinates[i].split (" -> "))
    #print (proCoordinates[i][0])
    finalCoordinates.append (proCoordinates[i][0].split (","))
    finalCoordinates.append (proCoordinates[i][1].split (","))
    print (myCoordinates[i])

print (finalCoordinates);