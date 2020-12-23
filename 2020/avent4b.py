#from aocd import get_data
#mylist = get_data(day=4)

f1 = open("/Users/mborkar/PycharmProjects/adventofcode/2020/avent4input.txt", "r")
mypassporstring = f1.read()
passport = mypassporstring.split("\n\n")

def HasRequiredPassportInformation (singlepassport):
    # print (passportdetails)
    passportattribute = singlepassport.split (" ")
    # print (passportattribute)
    passportattributename = []
    passportattributevalue = []
    for i in range (0,len(passportattribute)) :
        passportattributename.append (passportattribute[i].split (":")[0])
        passportattributevalue.append (passportattribute[i].split (":")[1])

    RequiredPassportInformation = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    for requireddetails in RequiredPassportInformation:
        if requireddetails not in passportattributename :
            return 'Invalid'
    for i in range (0,len(passportattributename)):
        if passportattributename[i]=="byr" and 1920 < int(passportattributevalue[i]) < 2002 :
            print('invalid for byr' + " " + passportattributevalue[i])
            return 'Invalid'
        elif passportattributename[i]=="iyr" and 2010 < int(passportattributevalue[i]) < 2020 :
            print('invalid for iyr' + " " + passportattributevalue[i])
            return 'Invalid'
        elif passportattributename[i] == "eyr" and 2020 < int(passportattributevalue[i]) < 2030 :
            print('invalid for eyr' + " " + passportattributevalue[i])
        elif passportattributename[i] == "hgt":
            print('checking for hgt' + " " + passportattributevalue[i])
        elif passportattributename[i] == "hcl" and passportattributevalue[0] != "#" and len(passportattributevalue) != 7 :
            # hcl(Hair Color) - a  # followed by exactly six characters 0-9 or a-f.
            print('invalid for hcl' + " " + passportattributevalue[i])
        elif passportattributename[i] == "ecl":
            print('checking for ecl' + " " + passportattributevalue[i])
        elif passportattributename[i] == "pid" and len (passportattributevalue[i]) != 9 and not passportattributevalue[i].isnumeric():
            print('invalid for pid' + " " + passportattributevalue[i])
    return 'Valid'

# cleaning up new lines and multiple spaces for each of the passports
validpassportcount = 0
for i in range (0,1):
    passport[i] = passport[i].replace ("\n"," ").strip ()
    print (passport[i])
    passportstatus = HasRequiredPassportInformation (passport[i])
    passport[i] = passport[i] + " " + passportstatus
    if passportstatus == 'Valid':
        validpassportcount +=1
#print (passport)
print ('Valid passports = ' + str(validpassportcount))
''' 
You can continue to ignore the cid field, but each other field has strict rules about what values are valid for automatic validation:

    done byr (Birth Year) - four digits; at least 1920 and at most 2002.
    done iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    done eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    done - pid (Passport ID) - a nine-digit number, including leading zeroes.

'''