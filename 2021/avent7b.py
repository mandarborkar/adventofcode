

crabpos = [int (x) for x in open ("/Users/mborkar/PycharmProjects/adventofcode/2021/avent7input.txt").read().strip().split(',')]
print (crabpos)

fuelcost = []
maxpos = max(crabpos)
minpos = min(crabpos)

for j in range(minpos,maxpos):
    fuel = 0
    for i in range (0,len(crabpos)):
        fuelx = abs(crabpos[i]-j)
        fuel  += (fuelx * (fuelx+1)) / 2
    fuelcost.append ([crabpos[i],j,fuel])

print (fuelcost)
lowestind = 0
lowestfuel = fuelcost[0][2]
print (lowestfuel)
for i in range (0,len(fuelcost)):
    if fuelcost[i][2] <= lowestfuel :
        lowestind = i
        lowestfuel = fuelcost[i][2]

print (fuelcost[lowestind])

#101571337 not the right answer