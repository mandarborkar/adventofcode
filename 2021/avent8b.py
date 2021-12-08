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
    digitwire.append (['','','','','','','','',''])

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
    print ( digitsize[i] )
    print ( digitwire[i] )
    for j in range ( 0, len ( digitlist[i] ) - 1 ):
        if digitsize[i][j] == 5 :   # 2, 3, 5
            processwire = digitlist[i][j]
            print (processwire)
            if (processwire.count(digitwire[i][1][0]) > 0) and (processwire.count(digitwire[i][1][1]) > 0) :
                digitwire[i][3] = digitlist[i][j]
            else:
                digitwire[i][2] = digitlist[i][j]
        elif digitsize[i][j] == 6 : # 0. 6, 9
            processwire = digitlist[i][j]
            print (processwire)
            digitwire[i][6] = digitlist[i][j]
    print(digitsize[i])
    print(digitwire[i])


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