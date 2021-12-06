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

for i in range (0,len(workCoordinates),2):
    if ((workCoordinates[i][0] == workCoordinates[i+1][0]) or (workCoordinates[i][1] == workCoordinates[i+1][1]) ):
        finalCoordinates.append(workCoordinates[i])
        finalCoordinates.append(workCoordinates[i+1])

finalCoordinates.pop(0)
print (finalCoordinates)
print (len(finalCoordinates))
coorgrid.append (max(finalCoordinates))
print (coorgrid[0][0])
print (coorgrid[0][1])
VentGrid = [[]]
for i in range (0, int(coorgrid[0][0])) :
    VentGrid.append ([0])
    for j in range(0,int(coorgrid[0][1])) :
        VentGrid.append([0]);

print (VentGrid)
# VentGrid [int(coorgrid[0][0]),int(coorgrid[0][1])]

rows, cols = (5, 5)
# method 2b
arr = [[0 for i in range(cols)] for j in range(rows)]

# check if arr[0] and arr[1] refer to
# the same object
print(arr[0] is arr[1])  # prints False