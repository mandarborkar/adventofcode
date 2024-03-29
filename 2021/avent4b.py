# v5
def printboard(board):
    for i in  board :
        print ( i )

def calsum(board):
    sum = 0
    for i in range ( 0, len ( board ) ):
        for j in range ( 0, len ( board[i] ) ):
            if board[i][j] != "-1":
                sum += int ( board[i][j] )
    print ( "sum = " + str ( sum ) )

def foundwinner(board):
    for i in range ( 0, len ( board ) ):
        totalrow = 0
        totalcol = 0
        # print (board);
        if board[i][0] != -2 and board [0][i] != -2 :
            for j in range ( 0, len ( board ) ):
                totalrow += int ( board[i][j] )
                totalcol += int ( board[j][i] )
            if totalrow == -5:
                print ( "found winner row " + str ( i )  )
                return i
            if totalcol == -5:
                print ( "found winner col " + str ( i )  )
                return i * -1
    return -10



#main program
# f1 = open ( "/Users/mborkar/PycharmProjects/adventofcode/2021/avent4input.txt", "r" )
f1 = open ( "2021/avent4input.txt", "r" )
fileinput = f1.readlines ()
numsel = fileinput[0].replace ( '\n', '' ).split ( "," )
print ( numsel )

boards = [[]]
finalboard = [[[]]]

for i in range ( 2, len ( fileinput ) ):
    currline = fileinput[i].replace ( "\n", "" )
    temprow = []
    if len ( currline ) > 0:
        for j in range ( 0, len ( currline ), 3 ):
            temprow.append ( currline[j:j + 2] )
        boards.append ( temprow )

boards.pop ( 0 )
#main set of boards are registered
for i in range ( 0, len ( boards ), 5 ):
    finalboard.append ( boards[i:i + 5] )

finalboard.pop ( 0 )

#check for each number selected
for i in range ( 0, len ( numsel ) ):
    print ( "processing for " + str ( numsel[i] ) )
    # each number selected check each baard
    j=0
    while j < len(finalboard):
        # for each board check if the selected number matches with something on the board
        # replace with number -1
        for k in range ( 0, len ( finalboard[j] ) ):
            for l in range ( 0, len ( finalboard[j][k] ) ):
                if int ( finalboard[j][k][l] ) == int ( numsel[i] ):
                    finalboard[j][k][l] = "-1"

        #printboard ( finalboard[j] )
        #calsum ( finalboard[j] )
        # Check if there is a winner - row/column all set to -1 (sum of 5 -1 = -5
        checkwin = foundwinner ( finalboard[j] ) ;
        if checkwin != -10 :
            printboard ( finalboard[j] )
            if checkwin > 0 :
                finalboard[j][checkwin][0] = '-2'
            else :
                finalboard[j][0][abs(checkwin)] = '-2'
            print ("after processing")
            printboard ( finalboard[j] )
            calsum ( finalboard[j] )
            print ( "found winner after " + str ( numsel[i] ) + " was called." )
            print ( "winning finalboard " + str ( j ) )
            # break

        j += 1

# print ( 'printing board' );
# printboard ( finalboard );
# print ( 'printing board done post -1' );
