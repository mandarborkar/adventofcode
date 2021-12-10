filename = '/Users/mborkar/PycharmProjects/adventofcode/2021/avent10testinput.txt'

h1 = [ list(x) for x in [x for x in open (filename).read().strip().split('\n') ]]

for x in h1:
    print (x)
