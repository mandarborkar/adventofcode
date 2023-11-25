def revisebasin (currbasin):
    for i in range (0,len(currbasin)):
        for j in range (0,len(currbasin[i])):
            #print (currbasin[i][j])
            if currbasin[i][j] == '#':
                print ('wall')
            elif currbasin[i][j] == 'E':
                print ('start')
            elif currbasin[i][j] == '<':
                print ('left')
            elif currbasin[i][j] == '>':
                print ('right')
            elif currbasin[i][j] == '^':
                print ('up')
            elif currbasin[i][j] == 'v':
                print ('start')
            elif currbasin[i][j] == '.':
                print ('open')
            else:
                print ('missing')


f1 = open("/Users/mborkar/PycharmProjects/adventofcode/2022/advent24testinput.txt", "r")
inputfile = f1.readlines()
print (inputfile)
basin = [[y for y in x] for x in [x.replace('\n','') for x in inputfile]]
print(basin)
revisebasin(basin)