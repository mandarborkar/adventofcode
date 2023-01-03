
f = open("/Users/mborkar/PycharmProjects/adventofcode/2022/advent10input.txt", "r")
inputlist = f.read().split()
print(inputlist)
clock = 0
signals = 1
totalsig = 0
while (clock <= 221) :
    clock += 1
    if clock in (20,60, 100, 140, 180, 220) :
        totalsig += (clock * signals)
        print('total signal1=',clock, signals,(clock * signals),totalsig)

    if inputlist[clock-1] in 'addx':
        clock += 1
        if clock in (20, 60, 100, 140, 180, 220):
            totalsig += (clock * signals)
            print('total signal2=',clock, signals,(clock * signals),totalsig)
        signals += int(inputlist[clock-1])
print (totalsig)
'''
treeheight = []
temptree = []
for i in range(0, len(inputlist)):
    currenttree = inputlist[i].replace('\n', '').split()
    temptree = [int(x) for x in list(currenttree[0]) ]
    treeheight.append(temptree)

visibletree = ((2 * len(treeheight)) + (2 * len(treeheight[0])) ) - 4

for i in range(1,len(treeheight)-1):
    currentrow = treeheight[i]
    print (currentrow[1:len(currentrow)-1])
    for j in range(1, len(currentrow)-1):
        left=int(max(treeheight[i][:j]))
        right = int(max(treeheight[i][j + 1:]))
        top = int(findmaxincolumn(treeheight, j, i, 't'))
        bottom = int(findmaxincolumn(treeheight, j, i+1, 'd'))
        currentheight = int(treeheight[i][j])
        if currentheight > left or currentheight > right or currentheight > top or currentheight > bottom :
            visibletree += 1
            #print (j,treeheight[i], currentheight, left, right, top, bottom)
            #print (treeheight[i-1])
            #print(treeheight[i])
            #print(treeheight[i + 1])


print (visibletree)
'''