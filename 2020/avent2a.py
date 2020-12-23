f1 = open("/Users/mborkar/PycharmProjects/hello-world/avent2input.txt", "r")
mylist = f1.readlines()
numberofvalidpasswords=0
totalcount=0
numberofvalidpasswords=0
numberofinvalidpasswords=0
for i in range (0,len(mylist)):
    found1 =  mylist[i].find ("-") # found "-"
    passmin= int(mylist[i][0:found1])
    found2 =  mylist[i].find (" ") # found " "
    passmax= int(mylist[i][found1+1:found2])
    found3 =  mylist[i].find (":") # found ":"
    passstr= mylist[i][found2+1:found3]
    password= mylist[i][found3+2:]
    passstrcount=int(password.count(passstr))
    totalcount = totalcount + 1
    if passstrcount >= passmin and passstrcount <= passmax :
        print("password is valid - " + password + " ; " + str(passmin)+" ; " + str(passstrcount) + " ; " + str(passmax) + " ; " + passstr + " ; " + mylist[i])
        numberofvalidpasswords = numberofvalidpasswords + 1
    else:
        print("password is invalid - " + password + " ; " + str(passmin)+" ; " + str(passstrcount) + " ; " + str(passmax) + " ; " + passstr + " ; " + mylist[i])
        numberofinvalidpasswords = numberofinvalidpasswords + 1

print ("Total : " + str(totalcount))
print ("number of valid passwords : " + str(numberofvalidpasswords))
print ("number of invalid passwords : " + str(numberofinvalidpasswords))