fishlist = []
fishcountbyage = [0,0,0,0,0,0,0,0,0]
fishcount = 0

f1 = open("/Users/mborkar/PycharmProjects/adventofcode/2021/avent6input.txt", "r")
fileinput = f1.readlines()
tempfishlist = fileinput[0].replace ( '\n', '' ).split ( "," )

for i in range (0,len(tempfishlist)) :
    fishlist.append (int(tempfishlist[i]))

print ("Fishes and their age initial state")
print (fishlist)

for age in range (0,8) :
    fishcountbyage[age] = fishlist.count(age)

print ("Fish count by age initial state")
print (fishcountbyage)

for days in range (0,256):
    age0 = fishcountbyage[0];
    fishcountbyage[0] = fishcountbyage[1]
    fishcountbyage[1] = fishcountbyage[2]
    fishcountbyage[2] = fishcountbyage[3]
    fishcountbyage[3] = fishcountbyage[4]
    fishcountbyage[4] = fishcountbyage[5]
    fishcountbyage[5] = fishcountbyage[6]
    fishcountbyage[6] = fishcountbyage[7]+ age0
    fishcountbyage[7] = fishcountbyage[8]
    fishcountbyage[8] = age0

print ('Fish count by age after 256 days')
print (fishcountbyage)
for x in fishcountbyage:
    fishcount += x
print ("Total fish count at end of 256 days : " + str(fishcount))
# 1574445493136