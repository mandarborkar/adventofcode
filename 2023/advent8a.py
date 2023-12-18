instruct = 'LRLRRRLRRLRRRLRRRLLLLLRRRLRLRRLRLRLRRLRRLRRRLRLRLRRLLRLRRLRRLRRLRRRLLRRRLRRRLRRLRLLLRRLRRRLRLRRLRRRLRRLRLLLRRRLRRLRRLRRRLRRRLRRRLRLRLRLRRRLRRRLLLRRLLRRRLRLRLRRRLRRRLRRLRRRLRLRLLRRRLRLRRLRLRLRRLLLRRRLRRRLRRLRRLRLRRLLRRLRRRLRRRLLRRRLRRLRLLRRLRLRRLLRRRLLLLRRLRRRLRLRRLLRLLRRRLLRRLLRRRLRRRLRRLLRLRLLRRLLRLLLRRRR'
instructtest = 'LLR'
mydictionary = {}

f1 = open("advent8input.txt", "r")
inputlist = f1.readlines()

network = [c1.split(' =') for c1 in [c.replace('\n', '') for c in inputlist]]
# print (network)

# network1 = [c[1].split(',') for c in network]
network1 = []
for i in range(0, len(network)):
    network1.append(network[i][1].replace(' (','').replace(')','').split(', '))
    # network1.append (x)
# print (network1)

for i in range(0, len(network)):
    # print (network[i])
    mydictionary[network[i][0]] = network1[i]

print (mydictionary)

position = 'AAA'
newx = []
steps = 0
while (1==1):
    for i in instruct:
        newx = mydictionary[position]
        if i.__eq__('R'):
            position = newx[1]
        else:
            position = newx[0]
        steps += 1
        print (i, position)
        if position.__eq__('ZZZ'):
            break
    if position.__eq__('ZZZ'):
        print (steps)
        break