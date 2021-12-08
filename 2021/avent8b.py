def findnumber (display, wiring) :
    numx = -1
    for j in range ( 0, len ( wiring ) ):
        wirenum = set ( wiring[j] )
        if len ( display ) == len ( wirenum ) and len ( display.difference ( wirenum ) ) == 0:
            numx = j
            # print ( 'set ver = ' + str ( j ) )
            break;
    return numx;

def calculateFinalnumber (display, wiring ):
    processwires = display[len (display)-4:]

    wire1 = set (display[len(display)-4])
    totalnum = findnumber(wire1, wiring)*1000

    wire1 = set ( display[len ( display ) - 3] )
    totalnum += findnumber ( wire1, wiring ) * 100

    wire1 = set ( display[len ( display ) - 2] )
    totalnum += findnumber ( wire1, wiring ) * 10

    wire1 = set ( display[len ( display )-1] )
    totalnum += findnumber ( wire1, wiring )

    print ('Number ' + str(totalnum))
    return (totalnum)

filename = '/Users/mborkar/PycharmProjects/adventofcode/2021/avent8testinput.txt'

digitlist = [[]]
digitsize = [[]]
digitwire = [[]]

singledigit = []
# givendigit [[1,'cf',2],[4,'eafb',4],[7,'dab',3],[8,'abcdef',7]]

for readline in open(filename):
    first, second = readline.strip().replace('\n','').split('|')
    singledigit =[]
    for x in first.strip().split (' '):
        singledigit.append (x)
    for x in second.strip().split (' '):
        singledigit.append (x)
    digitlist.append (singledigit)
    digitsize.append ([0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    digitwire.append (['','','','','','','','','',''])

digitlist.pop(0)
digitsize.pop(0)
digitwire.pop(0)

# start find the wires for each of the digits 0,....8
for i in range (0,len(digitlist)):
    # print(digitlist[i])
    # start with finding the lenght of each observed characters
    # process the easy digits 1, 4, 7 and 8 that have unique lengths
    for j in range (0,len(digitlist[i])):
        digitsize[i][j] = len(digitlist[i][j])
        if digitsize[i][j] == 2 :
            digitwire[i][1] = digitlist[i][j]
        elif digitsize[i][j] == 4 :
            digitwire[i][4] = digitlist[i][j]
        elif digitsize[i][j] == 3 :
            digitwire[i][7] = digitlist[i][j]
        elif digitsize[i][j] == 7 :
            digitwire[i][8] = digitlist[i][j]
    # print ( digitsize[i] )
    # print ( digitwire[i] )
    for j in range ( 0, len ( digitlist[i])):
        if digitsize[i][j] == 5 and digitwire[i][3] == '' :   # 2, 3, 5
            processwire = digitlist[i][j]
            if (processwire.count(digitwire[i][1][0]) > 0) and (processwire.count(digitwire[i][1][1]) > 0) :
                digitwire[i][3] = digitlist[i][j]
            # else:
                # print ( 'Still search betwee 2 and 5 ' + str ( digitlist[i][j] ) )
        elif digitsize[i][j] == 6 and digitwire[i][6] == '': # 0. 6, 9
            processwire = digitlist[i][j]
            if (processwire.count(digitwire[i][1][0]) == 0) or (processwire.count(digitwire[i][1][1]) == 0) :
                digitwire[i][6] = digitlist[i][j]
            # else:
                # print ( 'Still search between 0 and 9 ' + str ( digitlist[i][j] ) )
    for j in range ( 0, len ( digitlist[i])):
        if digitsize[i][j] == 6 and j != 6 :  # 9 and 0
            processwire = digitlist[i][j]
            checkwires = digitwire[i][4] + digitwire[i][3]
            # print ('processwires ' + processwire )
            # print ('checkwires ' + checkwires)
            digit1 = set(checkwires)
            digit2 = set(processwire)
            digit3 = digit1.difference(digit2)
            # print ('difference ' + str(digit3))
            if len(digit3) == 0 :
                # print ('found 9')
                digitwire[i][9] = digitlist[i][j]
            else:
                # print ('think 0')
                digitwire[i][0] = digitlist[i][j]
    for j in range ( 0, len ( digitlist[i])):
        if digitsize[i][j] == 5 and j != 3 :  # 2 and 5
            processwire = digitlist[i][j]
            checkwires = digitwire[i][9]
            # print ('processwires ' + processwire )
            # print ('checkwires ' + checkwires)
            digit1 = set(checkwires)
            digit2 = set(processwire)
            digit3 = digit1.difference(digit2)
            # print ('difference ' + str(digit3))
            if len(digit3) == 1 :
                # print ('found 5')
                digitwire[i][5] = digitlist[i][j]
            else:
                # print ('think 2')
                digitwire[i][2] = digitlist[i][j]

    # print('processed digits = ' + str(digitwire[i]))

print ('Starting to process the numbers...')

totalnum = 0

for i in range (0,len(digitlist)):
    print (digitlist[i][len(digitlist[i])-4:])
    print (digitwire[i])
    totalnum += calculateFinalnumber ( digitlist[i][len ( digitlist[i] ) - 4:], digitwire[i] )

print (totalnum)