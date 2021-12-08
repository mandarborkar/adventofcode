filename = '/Users/mborkar/PycharmProjects/adventofcode/2021/avent8testinput.txt'

digitlist = []
singledigit = []
# givendigit [[1,'cf',2],[4,'eafb',4],[7,'dab',3],[8,'abcdef',7]]

for readline in open(filename):
    first, second = readline.strip().replace('\n','').split('|')
    digitlist.append (second.strip())

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