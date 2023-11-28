
f1 = open("advent1input.txt", "r")
inputlist = f1.readlines()
steps = inputlist[0].replace("\n", "").split(', ')

print(steps)
x=0
y=0

# looking at direction of approach

dir='N'
visitednode = [[]]


for i in range (0,len(steps)):
    # print(i, steps[i], dir)
    if i == 0:
        if steps[i][0] == 'R':
            x = x + int(steps[i][1:])
            dir = 'W'
        else:
            x = x - int(steps[i][1:])
            dir = 'E'
        # print (dir, x, y)
    elif i%2==0:  # moving on x-axis
        if dir.__eq__('N') and steps[i][0].__eq__('R'):
            x += int(steps[i][1:])
            dir = 'W'
        elif dir.__eq__('N') and steps[i][0].__eq__('L'):
            x -= int(steps[i][1:])
            dir = 'E'
        elif dir.__eq__('S') and steps[i][0].__eq__('L'):
            x += int(steps[i][1:])
            dir = 'W'
        elif dir.__eq__('S') and steps[i][0].__eq__('R'):
            x -= int(steps[i][1:])
            dir = 'E'
        # print (dir, x, y)
    elif i%2 != 0:  #moving on y-axis
        if dir.__eq__('E') and steps[i][0].__eq__('R'):
            y += int(steps[i][1:])
            dir = 'N'
        elif dir.__eq__('E') and steps[i][0].__eq__('L'):
            y -= int(steps[i][1:])
            dir = 'S'
        elif dir.__eq__('W') and steps[i][0].__eq__('L'):
            y += int(steps[i][1:])
            dir = 'N'
        elif dir.__eq__('W') and steps[i][0].__eq__('R'):
            y -= int(steps[i][1:])
            dir = 'S'

    for j in range (1,len(visitednode)-1):
        # print (visitednode[j][0], visitednode[j][1])
        if ( visitednode[j][0] < x and x < visitednode[j+1][0] and visitednode[j][1] < y and y < visitednode[j+1][1]) or \
            ( visitednode[j][0] < x and x < visitednode[j+1][0] and visitednode[j][1] > y and y > visitednode[j+1][1]) or \
            ( visitednode[j][0] > x and x > visitednode[j+1][0] and visitednode[j][1] < y and y < visitednode[j+1][1]) or \
            ( visitednode[j][0] > x and x > visitednode[j+1][0] and visitednode[j][1] > y and y > visitednode[j+1][1]) :
                print ('found', i, steps[i])
                print (visitednode)
                print (dir, x, y)
                print (visitednode[j])
                print(visitednode[j+1])
                exit(0)
    visitednode.append([x,y])
    # print(dir, visitednode)
print (abs(x)+abs(y))


'''
    Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
    R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
    R5, L5, R5, R3 leaves you 12 blocks away.

i is even -> operate on x
Approaching from N> R+, L-
Approaching from S> R-, L+

i is odd -> operate on y
Approaching from E> R+, L-
Approaching from W> R-, L+

distance from origin -> x+y
'''