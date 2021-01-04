f1 = open("/Users/mborkar/PycharmProjects/adventofcode/2020/avent9input.txt", "r")
transmit = f1.readlines()
# print (len(transmit))
for i in range(0, len(transmit)):
    transmit[i] = int(transmit[i].replace('\n', ''))
# print (transmit)
# start
for i in range (25, len(transmit)):
    diffarr = []
    foundmatch = 'N'
    for j in range(i-25,i):
        diffarr.append(transmit[i]-transmit[j])
    # print (transmit[i])
    for currdiff in diffarr:
        if currdiff in transmit[i-25:i]:
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
        # print(transmit[i - 25:i])
        # print(diffarr)
        break
targettransmit = transmit[i]
print (targettransmit)

calsum = 0
foundmatch = 'N'
for i in range(0, len(transmit)):
    calsum = 0
    for j in range(i, len(transmit)):
        calsum = calsum + transmit[j]
        if calsum == targettransmit:
            print("Found sequence")
            print(i)
            print(j)
            foundmatch = 'Y'
            break
        elif calsum > targettransmit:
            #print(str(calsum) + ' > ' + str(targettransmit))
            break
    if foundmatch == 'Y':
        break
conlist = transmit[i:j]
print(conlist)
conlist.sort()
print(conlist)
print(conlist[0])
print(conlist[len(conlist)-1])
print(conlist[0]+conlist[len(conlist)-1])
