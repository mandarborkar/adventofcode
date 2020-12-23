f1 = open("/Users/mborkar/PycharmProjects/adventofcode/2020/avent5input.txt", "r")
boardingpass = f1.readlines()
for i in range (0,len(boardingpass)):
    boardingpass[i]=boardingpass[i].replace('\n','')
print (boardingpass[0])

seatbinary = []
seatdecimalrow = []
seatdecimalcolumn = []
seatid = []
for i in range (0,len(boardingpass)):
    #print ('running pass='+ str(i))
    seatbinary.append(boardingpass[i].replace("F","0").replace("B","1").replace("R","1").replace ("L","0"))
    #print (boardingpass[i])
    #print (seatbinary[i])
    #print (seatbinary[i][:len(seatbinary[i])-3])
    seatdecimalrow.append(int(seatbinary[i][:len(seatbinary[i])-3],2))
    #print (seatdecimalrow[i])
    #print (seatbinary[i][len(seatbinary[i])-3:])
    seatdecimalcolumn.append(int(seatbinary[i][len(seatbinary[i])-3:],2))
    #print (seatdecimalcolumn[i])
    seatid.append (int((seatdecimalrow[i])*8)+int(seatdecimalcolumn[i]) )


#print (seatbinary[0])
#print (seatbinary[0][:int(len(seatbinary))-4])
#print (seatdecimalrow[0])
#print (seatdecimalcolumn[0])
#print (seatid[0])
seatid.sort()
print (seatid)
print (max(seatid))
for i in range (0,len(seatid)-1):
    if seatid[i+1] != seatid[i]+1:
        print (seatid[i])
