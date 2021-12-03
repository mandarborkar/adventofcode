f1 = open("/Users/mborkar/PycharmProjects/adventofcode/2021/avent3input.txt", "r")

subinfo = f1.readlines()
subdetails = [0,0,0,0,0,0,0,0,0,0,0,0]

for j in range (0,12):
    for i in range(0, len(subinfo)):
        subinfo[i] = subinfo[i].replace ( '\n', '' )
        #print (subinfo[i]);
        subdetails[j] += int(subinfo[i][j]);
    # print ( str ( subdetails[j] ) + ' ' + str ( len ( subinfo ) / 2 ) )
    if  subdetails[j] >= len(subinfo)/2 :
        print ('0 wins = ' + str(subdetails[j]));
        subinfo = [subinfo[k] for k in range (len ( subinfo ) ) if subinfo[k][j] == '0'];
        print (subinfo);
    else:
        print ( '1 wins = ' + str(subdetails[j]) );
        subinfo = [subinfo[k] for k in range (len ( subinfo ) ) if subinfo[k][j] == '1']   ;
        print (subinfo);

    print (str(j)+ ' >> ');
    print (subinfo);
    if len(subinfo) == 1 :
        break;

print (int(subinfo[0]   ,2));
print (1371*3264);