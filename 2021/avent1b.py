f1 = open("/Users/mborkar/PycharmProjects/adventofcode/2021/avent1input.txt", "r")
mylist = f1.readlines()
inc = 0;
dec = 0;
for i in range(0, len(mylist)-3):
    depth1 = int(mylist[i])+int(mylist[i+1])+int(mylist[i+2])
    depth2 = int(mylist[i+1])+int(mylist[i+2])+int(mylist[i+3])
    if depth2-depth1 > 0 :
        print ( 'depth=' + str ( depth1 ) + ' ' + str ( depth2 ) + ' increased.' );
        inc += 1;
    else:
        print ( 'depth=' + str ( depth1 ) + ' ' + str ( depth2 )  + ' decreased.' );
        dec += 1;
print ('number of increase = ' + str(inc) + ' '+ str(dec) + ' ' + str(inc+dec));