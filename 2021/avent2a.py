f1 = open("/Users/mborkar/PycharmProjects/adventofcode/2021/avent2input.txt", "r")

instructionset = f1.readlines()
instructiondetails = []

h = 0;
d = 0;

for i in range(0, len(instructionset)):
    instructionset[i] = instructionset[i].replace ( '\n', '' )
    instructiondetails.append ( instructionset[i].split ( " " ) )
    print (instructiondetails[i][0]);
    print ( instructiondetails[i][1] );

    instruction = instructiondetails[i][0];
    step = int(instructiondetails[i][1]);

    if instruction == 'down':
        print ('down');
        d += step;
    elif instruction == 'up':
        print ( 'up' );
        d -= step;
    elif instruction == 'left':
        print ( 'left' );
        h -= step;
    elif instruction == 'forward':
        print ( 'right' );
        h += step;
total = h * d ;
print ( 'depth=' + str ( d ) + ' hor=' + str ( h ) + ' total=' + str(total));