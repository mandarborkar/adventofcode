

fishlist = []

f1 = open("/Users/mborkar/PycharmProjects/adventofcode/2021/avent6input.txt", "r")
fileinput = f1.readlines()
tempfishlist = fileinput[0].replace ( '\n', '' ).split ( "," )
print (tempfishlist)
for i in range (0,len(tempfishlist)) :
    fishlist.append (int(tempfishlist[i]))

#fishlist.pop(0)
print ( "Initial state "  + str ( fishlist ) )
for days in range (1,257):

    addfish=0
    for fish in range (0,len(fishlist)):
        if fishlist[fish] == 0 :
            fishlist[fish] = 6
            addfish += 1
        else:
            fishlist[fish] -= 1
    if addfish > 0 :
        for i in range ( 0, addfish ):
            fishlist.append ( 8 )

    print ( "After day " + str ( days ) ) # + ' ' + str ( fishlist ) )

print ('Total fish ' + str(len(fishlist)))
