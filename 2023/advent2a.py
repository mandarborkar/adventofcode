rmax = 12
gmax = 13
bmax = 14

f1 = open("advent2input.txt", "r")
inputlist = f1.readlines()

gamearr = [c.replace('\n', '').split(': ') for c in inputlist]

total = 0

for i in range (0,len(gamearr)):
    rx=0
    gx=0
    bx=0
    possible = True

    gamearr[i][0] = int(gamearr[i][0].replace('Game ', ''))
    gamearr1 = gamearr[i][1].split(';')
    gamearr2 = [c.split(',') for c in gamearr1]

    for x in gamearr2:
        for c in x:
            if c.__contains__('blue'):
                # bx += int(c.replace("blue",""))
                if int(c.replace("blue","")) > bmax:
                    possible=False
            elif c.__contains__('red'):
                # rx += int(c.replace("red",""))
                if int(c.replace("red","")) > rmax:
                    possible=False
            elif c.__contains__('green'):
                # gx += int(c.replace("green",""))
                if int(c.replace("green","")) > gmax:
                    possible=False
            if not possible:
                break
        if not possible:
            break
    if possible:
        total += gamearr[i][0]
        print(gamearr[i][0], gamearr2)
        print("adding to total ", total)
    else:
        print('Not possible ', gamearr[i][0], gamearr2)

print(total)