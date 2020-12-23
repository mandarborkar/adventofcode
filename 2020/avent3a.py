def numberoftrees (mylist, slope):
    addtotree = 0
    for i in range (1,len(mylist)):
        if mylist[i][(i*slope)] == "#":
            addtotree += 1
            print (mylist[i][(i*slope)] + " found tree on " + str(i) + ";" + str(addtotree))
        else:
            print (mylist[i][(i*slope)] + " no tree on    " + str(i) + ";" + str(addtotree))
    return (int(addtotree))

f1 = open("/Users/mborkar/PycharmProjects/adventofcode/2020/avent3input.txt", "r")
mylist = f1.readlines()

rowcount=len(mylist)
columncount=len(mylist[0])
duplicatecount=int(rowcount/columncount)

# populate additional columns to traverse
for i in range (0,len(mylist)):
    mylist[i] = mylist[i].replace("\n","")
    for j in range (0,duplicatecount-1):
        mylist[i] += mylist[i]

print ("Trees for slope 3 = " + str(numberoftrees(mylist,3)))
