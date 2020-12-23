#from aocd import get_data
#mylist = get_data(day=4)

f1 = open("/Users/mborkar/PycharmProjects/hello-world/avent4input.txt", "r")
mypassporstring = f1.read()
passport = mypassporstring.split("\n\n")

def HasRequiredPassportInformation (passportdetails):
    # print (passportdetails)
    RequiredPassportInformation = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for requireddetails in RequiredPassportInformation:
        if requireddetails not in passportdetails :
            return 'Invalid'
    return 'Valid'

def GetPassportdetails (singlepassport):
    passportattribute = singlepassport.split (" ")
    # print (passportattribute)
    passportattributename = []
    for i in range (0,len(passportattribute)) :
        passportattributename.append (passportattribute[i].split (":")[0])
    return passportattributename

# cleaning up new lines and multiple spaces for each of the passports
validpassportcount = 0
for i in range (0,len(passport)):
    passport[i] = passport[i].replace ("\n"," ").strip ()
    passportdetails = GetPassportdetails (passport[i])
    passportstatus = HasRequiredPassportInformation (passportdetails)
    passport[i] = passport[i] + " " + passportstatus
    if passportstatus == 'Valid':
        validpassportcount +=1
    print (passport[i])
    del passportdetails
#print (passport)
print ('Valid passports = ' + str(validpassportcount))

'''
mylist = mypassporstring.split("\n\n")
numberofpassports=0
passport = []
newpassportcomingup=True
for i in range (0,len(mylist)):
    if newpassportcomingup :
        passport.append(mylist[i])
    if mylist[i] != "\n" :
        passport[numberofpassports] = passport[numberofpassports] + mylist[i]
        newpassportcomingup = False
    else:
        newpassportcomingup=True
        numberofpassports += 1


ValidPassportcount=0
for i in range (0,len(passport)):
    passport[i]=passport[i].replace("\n"," ")
    if passport[i].count("byr") != 0 and passport[i].count("iyr") != 0 and passport[i].count("eyr") != 0 and passport[i].count("hgt") != 0 and passport[i].count("hcl") != 0 and passport[i].count("ecl") != 0 and passport[i].count("pid") != 0  :
        passport[i] = passport[i] + " Valid"
        ValidPassportcount += 1
    else:
        passport[i] = passport[i] + " Invalid"
    print ("passport " + str(i) + " = " + passport[i])

print (str(numberofpassports))
print (str(ValidPassportcount))
print (passport[0])
'''