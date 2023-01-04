
def isrightorder (x1, x2):
    # print(x1, x2)
    if isinstance(x1,int) and isinstance(x2,int):
        if x1 < x2:
            return -1
        elif x1 == x2:
            return 0
        else:
            return 1
    elif isinstance(x1,list) and isinstance(x2,list):
        i=0
        while i < len(x1) and i < len (x2):
            ro = isrightorder(x1[i],x2[i])
            if ro == -1:
                return -1
            elif ro == 1:
                return 1
            i += 1
        if i == len (x1) and i < len(x2):
            return -1
        elif i == len (x2) and i < len (x1):
            return 1
        else:
            return 0
    elif isinstance(x1,list) and isinstance(x2,int):
        return isrightorder(x1,[x2])
    elif isinstance(x1, int) and isinstance(x2, list):
        return isrightorder([x1], x2)

f = open("/Users/mborkar/PycharmProjects/adventofcode/2022/advent13input.txt", "r")
signalfile = f.read().strip()
# print(signalfile)
rightorderindex = []

for j, signalg in enumerate(signalfile.split('\n\n')):
    s1,s2 = signalg.split('\n')
    # print (j, s1, s2)
    # print (i, eval(s1), eval(s2))
    s1 = eval(s1)
    s2 = eval(s2)
    if isrightorder(s1,s2) == -1:
        #print(j,s1,s2)
        rightorderindex.append(j+1)

print(rightorderindex)
print(sum(rightorderindex))
