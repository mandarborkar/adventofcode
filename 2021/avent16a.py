
filename = '/Users/mborkar/PycharmProjects/adventofcode/2021/avent16input.txt'

h1 = [ list(x) for x in [x for x in open (filename).read().strip().split('\n') ]]
totalses = 0

for x in h1:
    #print ('Main row '+str(x))
    y = [ x for x in x]
    #print (y)
    i = 0

    while len(y) > 1 :
        z = y[i] + y[i + 1]
        if (y[i + 1] == '}' and y[i] != '{') or  (y[i+1] == ']' and y[i] != '[') or  (y[i+1] == ')' and y[i] != '(') or  ( y[i+1] == '>' and y[i] != '<'):
            #print (y)
            print('Found incorrect ' + str(y[i:i + 2]))
            if (y[i+1]) == ')' :
                totalses += 3
            elif (y[i+1]) == ']' :
                totalses += 57
            elif (y[i+1]) == '}' :
                totalses += 1197
            elif (y[i+1]) == '>' :
                totalses +=  25137
            break
        elif z == '[]' or z == '{}' or z == '()' or z == '<>':
            #print('Found match popping them out ' + str(y[i:i + 1]))
            y.pop(i)
            y.pop(i)
            i = -1
        i += 1
        if i >= len (y)-1 :
            break;

print ('Total SES ' + str(totalses))


