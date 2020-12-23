def countneighbours (waitingroom,currentx,currenty):
    noofneighbours = 0
    # above row
    if waitingroom[currentx-1][currenty]=='#' :
        noofneighbours += 1
    if waitingroom[currentx - 1][currenty] == '#':
        noofneighbours += 1
    if waitingroom[currentx - 1][currenty+1] == '#':
        noofneighbours += 1
    # current row
    if waitingroom[currentx][currenty - 1] == '#':
        noofneighbours += 1
    if waitingroom[currentx][currenty + 1] == '#':
        noofneighbours += 1
    # below row
    if waitingroom[currentx + 1][currenty]=='#' :
        noofneighbours += 1
    if waitingroom[currentx + 1][currenty] == '#':
        noofneighbours += 1
    if waitingroom[currentx + 1][currenty+1] == '#':
        noofneighbours += 1
    print ('len = ' + str(noofneighbours))
    return (noofneighbours)
# main ()

f1 = open("/Users/mborkar/PycharmProjects/adventofcode/2020/avent11input.txt", "r")
waitingroom = f1.readlines()
print (len(waitingroom))
print (len(waitingroom[0]))

numberofneighbours = []
for i in range (0, len(waitingroom)):
    waitingroom[i] = waitingroom[i].replace('\n','')
    noofneighbours = []
    for j in range (0, len(waitingroom[i])):
        noofneighbours.append (0)
    numberofneighbours.append(noofneighbours)

print (waitingroom[0:2])
print (numberofneighbours[0:2])
maxrows = len(waitingroom)
maxcolumns = len (waitingroom[0])


for i in (1,len(waitingroom)-2):
    for j in (1,len(waitingroom[i])-2):
        numberofneighbours[i][j] = countneighbours(waitingroom, i, j)

print(numberofneighbours)