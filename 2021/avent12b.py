def calculatecbc (x):
    count = 0
    counter = []
    for i in range (len(x)-1,-1,-1):
        if x[i] == '(':
            counter.append (1)
        elif x[i] == '[':
            counter.append(2)
        elif x[i] == '{':
            counter.append(3)
        elif x[i] == '<':
            counter.append(4)

    # print (counter)

    for x in counter:
        count = (count*5) + int(x)

    # print ('Calculating cbc '+ str(x) + ' ' + str(count))

    return count

zb = []
totalses = 0
filename = '/Users/mborkar/PycharmProjects/adventofcode/2021/avent12testinput.txt'
h1 = [ list(x) for x in [x for x in open (filename).read().strip().split('\n') ]]

for x in h1:
    # print ('Main row '+str(x))
    y = [ x for x in x]
    #print (y)
    i = 0

    while len(y) > 1 :
        z = y[i] + y[i + 1]
        if (y[i + 1] == '}' and y[i] != '{') or  (y[i+1] == ']' and y[i] != '[') or  (y[i+1] == ')' and y[i] != '(') or  ( y[i+1] == '>' and y[i] != '<'):
            #print (y)
            # print('Found incorrect ' + str(y[i:i + 2]))
            if (y[i+1]) == ')' :
                totalses += 3
            elif (y[i+1]) == ']' :
                totalses += 57
            elif (y[i+1]) == '}' :
                totalses += 1197
            elif (y[i+1]) == '>' :
                totalses +=  25137
            y.pop (i)
            y.pop (i)
            i = -1
            validx = False
            break
        elif z == '[]' or z == '{}' or z == '()' or z == '<>':
            #print('Found match popping them out ' + str(y[i:i + 1]))
            y.pop(i)
            y.pop(i)
            i = -1
        i += 1
        if i >= len (y)-1 :
            zb.append (y)
            break;

print ('Total SES ' + str(totalses))

finaly = []
totalcbc = 0

for x in zb:
    # print (x)
    totalcbc = calculatecbc ( x )
    finaly.append (totalcbc)

finaly.sort()
finalmid=(len(finaly)//2)
print (finaly)
print ('final print.....'+ str(finalmid) + ' ' + str(finaly[finalmid]))