f1 = open("/Users/mborkar/PycharmProjects/adventofcode/2021/avent1input.txt", "r")
mylist = f1.readlines()
inc = 0;
for i in range(1, len(mylist)):
    if int(mylist[i])-int(mylist[i-1]) > 0 :
        print ( 'depth=' + str ( i ) + ' ' + str ( mylist[i] ) + ' increased.' );
        inc += 1;
    else:
        print ( 'depth=' + str ( i ) + ' ' + str ( mylist[i] )  + ' decreased.' );
print ('number of increase = ' + str(inc));