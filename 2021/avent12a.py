def print_paper (paper):
    for x in paper :
        print (paper)

def reflexx(str,coor) :
    mergex = ''
    for i in range (0,coor):
        if str[i]=='#' or str[coor+1-i]=='#':
            mergex += '#'
        else:
            mergex += '.'
    return mergex

def mergestr (str1, str2):
    mergex = ''
    for i in range (0,len(str1)):
        if str1[i]=='#' or str2[i]=='#':
            mergex += '#'
        else:
            mergex += '.'
    return mergex

filename = '/Users/mborkar/PycharmProjects/adventofcode/2021/avent13testinput.txt'
h1 = [x.split(',') for x in [x for x in open (filename).read().strip().split('\n')]]
h2 = []
h3 = []
h4 = []
paper1 = []
xlist = []
ylist = []
instruction = False
for x in h1:
    if x[0] == '' or instruction :
        instruction = True
        h3.append(x)
    else :
        # print (x)
        h2.append(x)
        xlist.append(int(x[0]))
        ylist.append(int(x[1]))

xmax = max(xlist) + 1
ymax = max(ylist) + 1

paper = ['.'*xmax]*ymax

# print (len(paper[0]))
# print (len(paper))

xpaper = []
for x in h2:
    y = int(x[1])
    x = int(x[0])
    print (str(y)+' '+str(x)+'      '+str(paper[y]))
    if x == 0 :
        paper[y] = '#' + paper[y][x:len(paper[y]) - 1]
    elif x == len(paper[y]):
        print ('x='+str(x))
        paper[y] = paper[y][:x] + '#'
    else:
        paper[y] = paper[y][:x] + '#' + paper[y][x+1:]
    print (str(y)+' '+str(x)+'      '+str(paper[y]))

h3.pop(0)
for x in h3 :
    # print (x)
    h4.append(x[0].split('='))

splitalong = [[]]

for x in h4:
    # print (x)
    if x[0] == 'fold along y' :
        splitalong.append(['y', int(x[1])])
    else:
        splitalong.append(['x', int(x[1])])
    # print (splitalong)
splitalong.pop(0)

for x in splitalong:
    print (x)
    coor = x[1]
    paper1 = []
    if x[0]=='y':
        if len(paper)-1 > 2 * coor :
            print ('grid>'+str(coor)+' '+ str(len(paper)))
            for i in range (len(paper)-1,2*coor,-1):
                paper1.append(paper[i])
        for i in range (0,coor):
            paper1.append(mergestr(paper[i],paper[(2*coor)-i]))
            print(str(i) + ' ' + str((2*coor) - i) + ' ' + str(paper1[len(paper1) - 1]))
    if x[0]=='x':
        for i in range(0, len(paper)):
            paper1.append(reflexx(paper[i],coor))
            print(str(i) + ' ' + str((2 * coor) - i) + ' ' + str(paper1[len(paper1) - 1]))

        if len(paper[0])-1 > 2 * coor :
            print ('grid>'+str(coor)+' '+ str(len(paper[0])))
            for i in range (0,len(paper)):
                paper1.append(paper[i])
    paper = paper1
    print ('Folding ')
    print_paper(paper1)


i=0
for x in paper :
    print ('counter '+str(i)+ ' ' +str(x))
    i += 1
print ('folded')
i=0
for x in paper1:
    # print (x)
    print ('counter '+str(i)+ ' ' +str(x))
    i += 1

'''
1 1
2 2
3 3
4 4
5 4
6 3
7 2
8 1

'''

