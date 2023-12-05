

f1 = open("advent4input.txt", "r")

inputlist = [c1.split(': ') for c1 in [c.replace('\n', '') for c in f1.readlines()]]

total = 0
for i in range (0,len(inputlist)):
    currmatch = [c2.split (' ') for c2 in inputlist[i][1].split(' | ')]
    # print (currarr)
    n = 0
    for j in currmatch[0]:
        if j.__eq__('') :
            continue
        elif j in currmatch[1]:
            n +=1
    if n > 0 :
        total += pow(2,n-1)
        print (inputlist[i][0], n, total)

print (total)