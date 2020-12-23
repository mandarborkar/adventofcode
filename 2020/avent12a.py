f1 = open("/Users/mborkar/PycharmProjects/adventofcode/2020/avent12input.txt", "r")
instructions = f1.readlines()

for i in range (0,len(instructions)):
    instructions[i] = instructions[i].replace ('\n','')

# print (instructions)
# print (len(instructions))

facing = ['E','S','W','N']
now=0
magnitudeEW = 0
magnitudeNS = 0
print('Facing =      >> ' + facing[now] + ' ' + str(magnitudeEW) + ' ' + str(magnitudeNS))

for i in range (0,len(instructions)):
    # print (instructions[i])
    direction = instructions[i][0]
    if (direction == 'N' and now != 1) or (direction == 'S'and now != 3) :
        magnitudeNS += int(instructions[i][1:])
    elif direction == 'S' or direction == 'N':
        magnitudeNS -= int(instructions[i][1:])
    elif (direction == 'E' and now != 2 ) or (direction == 'W' and now != 0 ) :
        magnitudeEW += int(instructions[i][1:])
    elif direction == 'W'or direction == 'E' :
        magnitudeEW -= int(instructions[i][1:])
    elif direction == 'L':
        degrees = int(instructions[i][1:])
        now=(abs(now-int(degrees/90)))%4
        # print('Facing = ' + instructions[i] + ' >> ' + facing[now] + ' ' + str(magnitudeEW) + ' ' + str(magnitudeNS))
    elif direction == 'R':
        degrees = int(instructions[i][1:])
        now=(now+int(degrees/90))%4
        # print('Facing = ' + instructions[i] + ' >> ' + facing[now] + ' ' + str(magnitudeEW) + ' ' + str(magnitudeNS))
    elif direction == 'F':
        if now == 0 :
            magnitudeEW += int(instructions[i][1:])
        elif now == 2:
            magnitudeEW -= int(instructions[i][1:])
        elif now == 1 :
            magnitudeNS -= int(instructions[i][1:])
        elif now == 3 :
            magnitudeNS += int(instructions[i][1:])
    print('Facing = ' + instructions[i] + ' >> ' + facing[now] + ' ' + str(magnitudeEW) + ' ' + str(magnitudeNS))
print (str(abs(magnitudeEW)+abs(magnitudeNS)))