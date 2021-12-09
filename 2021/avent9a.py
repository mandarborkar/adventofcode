filename = '/Users/mborkar/PycharmProjects/adventofcode/2021/avent9testinput.txt'

digitlist = [[]]
digitsize = [[]]
digitwire = [[]]

singledigit = []

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