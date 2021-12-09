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
sum=0
for x in hd:
    for y in x:
        print (y)
        sum += int(y)

for x in hd:
    print (x)
print (sum)
