filename = '/Users/mborkar/PycharmProjects/adventofcode/2021/avent25input.txt'

seac = [ list(x) for x in [x for x in open (filename).read().strip().split('\n') ]]

xseac = len(seac[0])
yseac = len(seac)

for step in range (1,1000):
    Found = False
    currseac = []
    for x in seac:
        currseac.append (list(x))

    for y in range (0, yseac):
        if y == yseac-1:
            ymoveto=0
        else:
            ymoveto=y+1

        for x in range (0,xseac):
            if x == xseac-1:
                xmoveto=0
            else:
                xmoveto=x+1

            if currseac[y][x] == '>' and currseac[y][xmoveto] == '.':
                seac[y][xmoveto] = '>'
                seac[y][x] = '.'
                Found = True

    currseac = []
    for x in seac:
        currseac.append (list(x))

    for y in range (0, yseac):
        if y == yseac-1:
            ymoveto=0
        else:
            ymoveto=y+1
        for x in range(0, xseac):
            if x == xseac - 1:
                xmoveto = 0
            else:
                xmoveto = x + 1
            if currseac[y][x] == 'v' and currseac[ymoveto][x] == '.':
                seac[ymoveto][x] = 'v'
                seac[y][x] = '.'
                Found = True

    if not(Found):
        print ('No change '+str(step))
        break

