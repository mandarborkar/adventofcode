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
    print(digitlist[i])
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

    print('processed digits = ' + str(digitwire[i]))


'''
totalnumber = 0
for x in digitlist :
    singledigit = x.split(' ')
    print (singledigit)
    singledigitlen = []
    for y in singledigit :
        if len(y) == 7 :
            singledigitlen.append(8)
        elif len(y) == 2 :
            singledigitlen.append(1)
        elif len(y) == 4 :
            singledigitlen.append(4)
        elif len(y) == 3 :
            singledigitlen.append(7)
        elif len(y) == 5 :  # 2,3,5
            singledigitlen.append(5)
        elif len(y) == 6 :  # 0,6,9
            singledigitlen.append(9)
        elif y == 'cdfbe' :
            singledigitlen.append(5)
        elif y == 'fcadb':
            singledigitlen.append(3)
        else:
            singledigitlen.append(0)
    number = singledigitlen[0]*1000+ singledigitlen[1] * 100 + singledigitlen[2] * 10 + singledigitlen[3]
    totalnumber += number
    print (singledigitlen)
    print (number)

print (digitlist)
print (totalnumber)
'''
'''
acedgfb: 8
cdfbe: 5
gcdfa: 2
fbcad: 3
dab: 7
cefabd: 9
cdfgeb: 6
eafb: 4
cagedb: 0
ab: 1
'''