
def findmaxincolumn (arr, col, row,direction) :
    temparr = []
    if direction == 't':
        for i in range (0,row):
            temparr.append(arr[i][col])

    if direction == 'd':
        for i in range (row,len(arr)):
            temparr.append(arr[i][col])

    return (max(temparr))

f1 = open("/Users/mborkar/PycharmProjects/adventofcode/2022/advent8input.txt", "r")
inputlist = f1.readlines()
# print(inputlist)
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




