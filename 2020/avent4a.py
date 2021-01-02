#from aocd import get_data
#mylist = get_data(day=4)

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

f1 = open("/Users/mborkar/PycharmProjects/adventofcode/2020/avent4input.txt", "r")
mypassporstring = f1.read()
passport = mypassporstring.split("\n\n")

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