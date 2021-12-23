
filename = '/Users/mborkar/PycharmProjects/adventofcode/2021/avent22testinput.txt'

f1 = open(filename, "r")
inputfile = f1.readlines()
# print (inputfile)

rebootseq = []
for x in inputfile:
    inst, coor = x.replace('\n','').split(' ')
    xyz = [c2.split('=') for c2 in [ c1 for c1 in coor.split(',')]]
    for y in xyz:
        y[1] = y[1].split('..')
        # print (y[1])
    rebootseq.append ([inst, xyz[0][1],xyz[1][1],xyz[2][1]])


