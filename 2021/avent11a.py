def printjelly (x):
    for x in jellyn:
        print(x)
filename = '/Users/mborkar/PycharmProjects/adventofcode/2021/avent11testinput.txt'
jellyb = [ list(x) for x in [y for y in open (filename).read().strip().split('\n') ]]
jellyn = []

for i in range (0,len(jellyb)):
    jx = []
    for j in range (0,len(jellyb[0])):
        jx.append (int(jellyb[i][j]))
    jellyn.append(jx)

jflash = 0
# printjelly(jellyn)

for stepx in range (1,101):
    print('Step ' + str(stepx))
    printjelly(jellyn)
    for i in range (0,len(jellyn)):
        for j in range (0,len(jellyn[i])):
            if jellyn[i][j] == 9:
                jellyn[i][j] = 0
            elif jellyn[i][j] == 0:
                jflash += 1
                jellyn[i][j] += 1

            else:
                jellyn[i][j] += 1

print ('No of flashes = ' + str(jflash))