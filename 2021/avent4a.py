#v2
def calsum (board):
    sum = 0
    for i in range (0,len(board)):
        for j in range (0,len(board[i])):
            if board[i][j] != "-1" :
                #print (board[i][j])
                sum += int(board[i][j]);
    print ("sum = "+ str(sum))

def foundwinner (board) :
    for i in range(0,len(board)) :
        totalrow = 0;
        totalcol = 0;
        # print (board);
        for j in range (0,len(board)):
            totalrow += int(board[i][j]) ;
            totalcol += int(board[j][i]) ;
        if totalrow == -5  :
            print ("found winner row " + str (i) + ' ' + str(j));
            print (board);
            calsum ( board );
            return True;
        if totalcol == -5  :
            print ("found winner col " + str (i) + ' ' + str(j));
            print (board);
            calsum (board);
            return True;

# f1 = open("/Users/mborkar/PycharmProjects/adventofcode/2021/avent4input.txt", "r")
f1 = open("2021/avent4input.txt", "r")

fileinput = f1.readlines()
numsel = fileinput[0].replace ( '\n', '' ).split ( "," )
print (numsel)

boards = [[]];

for i in range (2, len(fileinput)) :
    currline = fileinput[i].replace ("\n","");
    temprow = [];
    for j in range (0,len(currline),3):
        temprow.append(currline[j:j+2]);
    boards.append (temprow);

for i in range (0,len(numsel)):
    for j in range (0,len(boards)):
        for k in range (0,len(boards[j])):
            if int(boards[j][k]) == int(numsel[i])  :
                boards[j][k] = "-1"
    for l in range (0,len(boards),6):
        if foundwinner(boards[l+1:l+6]) :
            # print (boards[l+1:l+6])
            print ("found winner after " + str(numsel[i]) + " was called.");
            print ( "board at " + str ( l + 1 ) )
            exit();
