f1 = open("/Users/mborkar/PycharmProjects/adventofcode/2020/avent9input.txt", "r")
transmit = f1.readlines()
# print (len(transmit))
for i in range (0, len(transmit)):
    transmit[i] = int(transmit[i].replace('\n', ''))
# print (transmit)

for i in range (25, len(transmit)):
    diffarr = []
    foundmatch = 'N'
    for j in range (i-25,i):
        diffarr.append (transmit[i]-transmit[j])
    # print (transmit[i])
    for currdiff in diffarr :
        if currdiff in transmit [i-25:i] :
            # print(str(transmit[i]) + " " + str(currdiff))
            foundmatch='Y'
    if foundmatch == 'Y' :
        # print (str(transmit[i]) + " Found match")
        # print(transmit[i - 25:i])
        # print(diffarr)
        foundmatch = False
        del diffarr
    else:
        print (str(transmit[i]) + " Found no match")
        print(transmit[i - 25:i])
        print(diffarr)
        break

