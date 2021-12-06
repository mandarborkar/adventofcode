f1 = open("2021/avent3input.txt", "r")

subinfo = f1.readlines()
subdetails = [0,0,0,0,0,0,0,0,0,0,0,0]


for i in range(0, len(subinfo)):
    subinfo[i] = subinfo[i].replace ( '\n', '' )
    print (subinfo[i]);
    subdetails[0] += int(subinfo[i][0]);
    subdetails[1] += int(subinfo[i][1]);
    subdetails[2] += int(subinfo[i][2]);
    subdetails[3] += int(subinfo[i][3]);
    subdetails[4] += int(subinfo[i][4]);
    subdetails[5] += int(subinfo[i][5]);
    subdetails[6] += int(subinfo[i][6]);
    subdetails[7] += int(subinfo[i][7]);
    subdetails[8] += int(subinfo[i][8]);
    subdetails[9] += int(subinfo[i][9]);
    subdetails[10] += int(subinfo[i][10]);
    subdetails[11] += int(subinfo[i][11]);

print ( subdetails );

gammarate = '';
epsilonrate = '';

for i in range (0,12):
    if subdetails[i] > 500 :
        gammarate  += '1';
        epsilonrate += '0';

    else:
        gammarate  += '0';
        epsilonrate += '1';

#gammarate = '0b'+gammarate;
#epsilonrate = '0b'+epsilonrate;

print ( int(gammarate,2) );
print ( int(epsilonrate,2));
print ( int(epsilonrate,2) * int(gammarate,2) );
