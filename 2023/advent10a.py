
'''

find S

Find neighbours of location:
    [x][y-1] - same row, back - conditions: y-1>0, found S, not visited,
    [x][y+1] - same row, forward - conditions: y+1 < len, found S, not visited,
    [x-1][y] - above row, same col - conditions: x-1>0, found S, not visited,
    [x+1][y] - below row, same col - conditions: x+1 < len, found S, not visited,

Condition: Found S
    stop and get total steps
else
    For each neighbour repeat find neighbours

'''

from collections import deque
def findS( lgrid ):
    for row, gridstr in enumerate(lgrid):
        for col, rowstr in enumerate(gridstr):
            if rowstr == 'S':
                return [row,col]

f1 = open("advent10input.txt", "r")
grid = f1.read().splitlines()
print (grid)
startloc = findS(grid)

visited = {(startloc[0],startloc[1])}
print (visited)

processq = deque ([(startloc[0],startloc[1])])

while processq :
    row, col = processq.popleft()
    value = grid [row][col]

    if row > 0 and value in 'S|JL' and grid[row-1][col] in '|F7' and (row-1,col) not in visited:
        visited.add((row-1,col))
        processq.append((row-1,col))

    if row < len(grid)-1 and value in 'S|7F' and grid[row+1][col] in '|JL' and (row+1,col) not in visited:
        visited.add((row+1,col))
        processq.append((row+1,col))

    if col > 0 and value in 'S7-J' and grid[row][col-1] in '-FL' and (row, col-1) not in visited:
        visited.add((row,col-1))
        processq.append((row,col-1))

    if col < len (grid[row]) - 1 and value in 'S-LF' and grid[row][col+1] in '-7J' and (row, col+1) not in visited:
        visited.add((row,col+1))
        processq.append((row,col+1))


print (len(visited)//2)

exit(0)

griddict = {}
visited = set ()
pipe='|-LJ7FS'


def findNextStep (startPos):
    # print ('Start pos ', startPos)
    x = startPos[0]
    y = startPos[1]
    neighbour = []
    if x-1>=0 and gridarr[x-1][y] in '|-LJ7FS' : # '7F':
        neighbour.append([x-1,y])
    if x+1<=len(gridarr) and gridarr[x+1][y] in '|-LJ7FS' : # 'LJ|':
        neighbour.append([x+1,y])
    if y-1>=0 and gridarr[x][y-1] in '|-LJ7FS' : # 'F|L-S':
        neighbour.append([x,y-1])
    if y+1<len(gridarr[x]) and gridarr[x][y+1] in '|-LJ7FS' : # '7|J-':
        neighbour.append([x,y+1])
    # print ('Neighbour ', neighbour)
    # print('grid char ', gridarr[x][y])
    return (neighbour)

def findNeighbour (gridarr, neighbour):
    next_neighbour=findNextStep(neighbour)
    # print (neighbour)
    for c in next_neighbour:
        print ('Processing neighbour for ', gridarr[c[0]][c[1]],' ',c)
        if gridarr[c[0]][c[1]].__eq__('S'):
            print ('found S')
        else:
            next_neighbour.append(findNextStep(c))
            print ('next neighbour', next_neighbour)
            if len(next_neighbour) == 0 :
                print ('no neighbours')

f1 = open("advent10testinput.txt", "r")
inputlist = f1.readlines()

gridarr = [c1 for c1 in [c.replace('\n', '') for c in inputlist]]
print(gridarr)

start = findS (gridarr)
print ('found S ', start)

findNeighbour(gridarr,[start])



