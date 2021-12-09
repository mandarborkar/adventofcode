def traverse (x, y, dir, map) :
    print (str(x),str(y))
    if dir == -1 and ( x-1 < 0 or  map[x-1][y]==9) :
        return [x,y]
    elif dir == 1 and ( x > len(map) or map [x+1][y]==9):
        return [x,y]
    elif dir == -2 and ( y-1 < 0 or map[x][y-1] == 9):
        return [x, y]
    elif dir == 1 and ( y > len(map[0]) or map[x][y+1] == 9):
        return [x, y]
    else:
        traverse(x-1,y,-1,map) # up
        traverse(x+1, y, 1, map) # down
        traverse(x, y-1, -2, map) # left
        traverse(x, y+1, 2, map) # right

        # need to take care of already visited to stop infinite loop

def checkdeepest (x, y, map) :

    if (y-1 >= 0) :
        if ( map[x][y] >= map[x][y-1] ):
            return False
    if (y+1 < len(map[0])) :
        if ( map[x][y] >= map[x][y+1] ):
            return False
    if (x + 1 < len(map)) :
        if (map[x][y] >= map[x+1][y]):
            return False
    if (x-1 >= 0) :
        if ( map[x][y] >= map[x-1][y] ):
            return False

    return True

filename = '/Users/mborkar/PycharmProjects/adventofcode/2021/avent9testinput.txt'

h1 = [ list(x) for x in [x for x in open (filename).read().strip().split('\n') ]]
hd = [ [0 for x in range(len(h1[0]))]     for x in [ x for x in range(len(h1))]]
hdcor = [[[]]]
print ('input file....')
for x in h1:
    print (x)
for x in hd:
    print (x)

for i in range(len(h1)):
    for j in range (len(h1[0])):
        # print (h1[i][j])
        if checkdeepest (i,j,h1):
            hd[i][j] = int(h1[i][j])+1
            hdcor.append ([i,j])
sum=0
for x in hd:
    for y in x:
        print (y)
        sum += int(y)

for x in hd:
    print (x)
print (sum)

for x in hdcor:
    print (x)

hdcor.append (traverse(0,1,-1,h1))

for x in hdcor:
    print (x)