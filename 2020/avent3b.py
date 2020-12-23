def numberoftrees (mylist, slope, step):
    addtotree = 0
    for i in range (step,len(mylist),step):
        if mylist[i][(i*slope)] == "#":
            addtotree += 1
            print (mylist[i][(i*slope)] + " found tree at " + str(i) + ";" + str(i*slope) + ";"+ str(addtotree))
        else:
            print (mylist[i][(i*slope)] + " no tree on    " + str(i) + ";" + str(i*slope) + ";"+ str(addtotree))
    return (int(addtotree))

f1 = open("/Users/mborkar/PycharmProjects/hello-world/avent3input.txt", "r")
mylist = f1.readlines()

rowcount=len(mylist)
columncount=len(mylist[0])
duplicatecount=int(rowcount/columncount)

# populate additional columns to traverse
for i in range (0,len(mylist)):
    mylist[i] = mylist[i].replace("\n","")
    for j in range (0,duplicatecount-1):
        mylist[i] += mylist[i]

slope1 = numberoftrees(mylist,1,1)
slope3 = numberoftrees(mylist,3,1)
slope5 = numberoftrees(mylist,5,1)
slope7 = numberoftrees(mylist,7,1)
slope12 = numberoftrees(mylist,1,2)

slope12 = 0
for i in range(1, int(len(mylist)/2)+1):
    if mylist[i*2][i] == "#":
        slope12 += 1
        print(mylist[i*2][i] + " found tree at " + str(i*2) + ";" + str(i) + ";" + str(slope12))
    else:
        print(mylist[i*2][i] + " no tree on    " + str(i*2) + ";" + str(i) + ";" + str(slope12))

print ("Trees for slope 1 = " + str(slope1))
print ("Trees for slope 3 = " + str(slope3))
print ("Trees for slope 5 = " + str(slope5))
print ("Trees for slope 7 = " + str(slope7))
print ("Trees for slope 1  step 2 = " + str(slope12))
print ("total trees = " + str ( slope1 * slope3 * slope5 * slope7 * slope12))