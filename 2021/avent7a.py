

crabpos = [int (x) for x in open ("/Users/mborkar/PycharmProjects/adventofcode/2021/avent7input.txt").read().strip().split(',')]
print (crabpos)

fuelcost = []

for i in range (0,len(crabpos)):
    fuel = 0
    for j in range(0,len(crabpos)):
        fuel += abs(crabpos[i]-crabpos[j])
    fuelcost.append ([crabpos[i],fuel])

print (fuelcost)
lowestind = 0
lowestfuel = fuelcost[0][1]

for i in range (0,len(fuelcost)):
    if fuelcost[i][1] < lowestfuel :
        lowestind = i
        lowestfuel = fuelcost[i][1]

print (fuelcost[lowestind])