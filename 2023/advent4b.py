

f1 = open("advent4input.txt", "r")

inputlist = [c1.split(': ') for c1 in [c.replace('\n', '') for c in f1.readlines()]]

totalmatch = []
for i in range (0,len(inputlist)):
    currmatch = [c2.split (' ') for c2 in inputlist[i][1].split(' | ')]

    n = 0
    for j in currmatch[0]:
        if j.__eq__('') :
            continue
        elif j in currmatch[1]:
            n +=1
    totalmatch.append(n)
    print (inputlist[i][0], n, totalmatch)

totalcards=[]
for i in inputlist:
    totalcards.append(1)

print (totalcards)

for i in range (1, len(totalcards)):
    print (i, totalmatch[i-1])
    for j in range (i, i+int(totalmatch[i-1])):
        if j <= len(totalcards):
            totalcards[j] += totalcards[i-1]
            print (i,j,totalcards)

print (totalcards)
total=0
for i in totalcards:
    total+=i
print (total)