rmax = 12
gmax = 13
bmax = 14

f1 = open("advent2input.txt", "r")
inputlist = f1.readlines()

gamearr = [c.replace('\n', '').split(': ') for c in inputlist]

total = 0

for i in range (0,len(gamearr)):

    gamearr[i][0] = int(gamearr[i][0].replace('Game ', ''))
    gamearr1 = gamearr[i][1].split(';')
    gamearr2 = [c.split(',') for c in gamearr1]

    rcurr = 0
    gcurr = 0
    bcurr = 0

    for x in gamearr2:
        for c in x:
            if c.__contains__('red'):
                if int(c.replace("red","")) > rcurr:
                    rcurr = int(c.replace("red",""))
            elif c.__contains__('green'):
                if int(c.replace("green","")) > gcurr:
                    gcurr = int(c.replace("green",""))
            elif c.__contains__('blue'):
                if int(c.replace("blue","")) > bcurr:
                    bcurr = int(c.replace("blue",""))

    total += rcurr * gcurr * bcurr
    print(gamearr[i][0], total, gamearr2)

print(total)