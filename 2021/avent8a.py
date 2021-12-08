filename = '/Users/mborkar/PycharmProjects/adventofcode/2021/avent8input.txt'

digitlist = []
singledigit = []
# givendigit [[1,'cf',2],[4,'eafb',4],[7,'dab',3],[8,'abcdef',7]]

for readline in open(filename):
    first, second = readline.strip().replace('\n','').split('|')
    digitlist.append (second.strip())

totaldigits = 0
for x in digitlist :
    singledigit = x.split(' ')
    singledigitlen = [ len(y) for y in singledigit]
    totaldigits += singledigitlen.count (2)
    totaldigits += singledigitlen.count (4)
    totaldigits += singledigitlen.count (3)
    totaldigits += singledigitlen.count (7)
    print (singledigit)
    print (singledigitlen)
    print (totaldigits)

print (digitlist)
print (totaldigits)

