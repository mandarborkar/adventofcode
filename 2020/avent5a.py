f1 = open("/Users/mborkar/PycharmProjects/adventofcode/2020/avent5input.txt", "r")
boardingpass = f1.readlines()
for i in range (0,len(boardingpass)):
    boardingpass[i]=boardingpass[i].replace('\n','')

def prepareseats (size) :
    seats = []
    for i in range (0,size):
        seats.append(i)
    return seats

def clearseat (seats,section):
    if section == 'F' or section == 'L':
        del seats[int(len(seats)/2):]
    elif section == 'B' or section == 'R':
        del seats[:int(len(seats)/2)]
    return seats

occupiedrow = []
#BFFFFFFRLL
# B upper half 65-128
# F lower half 1-64

# seats = prepareseats(7)
# print (seats)
# del seats

for j in range (0,len(boardingpass)):
#    print ("new pass " + str(j) + " = " + boardingpass[j][0:int(len(boardingpass[j]))-3])
    # print (str(int(len(boardingpass[j]))-3))
    seats = prepareseats (128)
    # print (seats)
    for i in range (0,int(len(boardingpass[j]))-3):
        # print (boardingpass[j][0:i+1])
        seats = clearseat (seats,boardingpass[j][i])
        # print (seats)
    occupiedrow.append(seats[0])
    del seats
#occupiedrow.sort ()
# print (occupiedrow)

occupiedcolumn = []
for j in range (0,len(boardingpass)):
#for j in range(0, 2):
    # print ("new pass = " + boardingpass[j][int(len(boardingpass[j]))-3:])
    seats = prepareseats (8)
    # print (seats)
    for i in range (0,3):
        # print (boardingpass[j][int(len(boardingpass[j]))-3:int(len(boardingpass[j]))-3+i+1])
        seats = clearseat (seats,boardingpass[j][i])
        # print (seats)
    occupiedcolumn.append(seats[0])
    del seats
    # print ("seat number="+str(j))
# print (occupiedcolumn)

seatid = []
largestsearid = 0
largestindex = 0
for j in range (0,len(boardingpass)):
    print ("new pass " + str(j) + " = " + boardingpass[j] + " seat = " + str(occupiedrow[j]) + "-" + str(occupiedcolumn[j]))
    seatidx = (occupiedrow[j] * 8) + occupiedcolumn[j]
    seatid.append(str(occupiedrow[j])+"-"+str(occupiedcolumn[j]))
    if largestsearid < seatidx :
        largestsearid = seatidx
        largestindex = j
#seatid.sort ()
#print (seatid)
print (largestsearid)
print("new pass " + str(largestindex) + " = " + boardingpass[largestindex] + " seat = " + str(occupiedrow[largestindex]) + "-" + str(occupiedcolumn[largestindex]))
