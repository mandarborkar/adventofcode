from collections import Counter
filename = '/Users/mborkar/PycharmProjects/adventofcode/2021/avent14input.txt'

f1 = open(filename, "r")
polymer1 = f1.readlines()

polymerx = polymer1[0].replace(' ','').replace('\n','')
# print (polymerx)

polydic={}
for x in polymer1[2:]:
    key, repl = x.replace(' ','').replace('\n','').split('->')
    polydic[key] = repl
print (polydic)

mainPoly = Counter ()
for i in range (len(polymerx)-1):
    mainPoly[polymerx[i]+polymerx[i+1]] += 1
print (mainPoly)
repeatcount = 41
for repeat in range (repeatcount):
    ElementCounter = Counter()
    for i in mainPoly :
        ElementCounter[i[0]] += mainPoly[i]
        # print(ElementCounter)
    ElementCounter[polymerx[-1]] += 1

    if repeat == repeatcount-1 :
        # print (ElementCounter)
        print (max(ElementCounter.values()))
        print (min(ElementCounter.values()))
        print (max(ElementCounter.values()) - (min(ElementCounter.values())))

    morph = Counter()
    for i in mainPoly :
        morph[i[0]+polydic[i]] += mainPoly[i]
        morph[polydic[i]+i[1]] += mainPoly[i]

    mainPoly = morph

'''
chardic = {}
for j in range (0,6):
    for i in range (0,len(polymerx)-1):
        polykey = polymerx[i:i + 2]
        print ('poly = '+ polykey)
        if polykey in polydic:
            # polydic.update({polykey:[polydic[polykey][0],polydic[polykey][1]+1]})
            print('Found poly = ' + polykey)
            polyval = list(polydic[polykey])
            newpolycount = polyval[1]
            print (polyval)
            if len(polyval[0]) > 0:
                print ('repl '+polyval[0][0])
                newpolyval1 = polykey[0] + polyval[0][0]
                newpolyval2 = polyval[0][0] + polykey[1]
                print (newpolyval1+' '+str(newpolycount+1))
                print (newpolyval2 + ' ' + str(newpolycount + 1))
                print (polykey+ ' ' + polyval[0][0] + ' 0' )
                if newpolyval1 in polydic:
                    newrepl1 = list(polydic[newpolyval1])
                    polydic.update({newpolyval1: [newrepl1[0][0],newrepl1[1]+1]})
                else:
                    polydic.update({newpolyval1: ['', 1]})
                if newpolyval2 in polydic:
                    newrepl2 = list(polydic[newpolyval2])
                    polydic.update ({newpolyval2: [newrepl2[0][0], newrepl2[1]+1]} )
                else:
                    polydic.update({newpolyval2: ['', 1]})
                polydic.update({polykey:[polyval[0][0],newpolycount]})
            else:
                polydic.update ( {polykey: ['', 1]} )
        else:
            polydic.update ( {polykey: ['', newpolycount+1]} )

    for x,y  in polydic.items():
        if y[1]>0:
            print ('Step ' + str(j) + ' Null found '+ str(x),str(y))
            xstr = str(x)
            if xstr[0] in chardic :
                countx = chardic[xstr[0]]
                chardic.update({xstr[0]:countx+1})
            else:
                chardic.update({xstr[0]:1})
        # else:
          #  print (x,y)
print (chardic)
fincount=collections.Counter(polydic)
print (fincount)

for x in chardic:
    fincount += chardic[x]
print (fincount)

Template:     NNCB
After step 1: NCNBCHB
After step 2: NBCCNBBBCBHCB
After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
This polymer grows quickly. After step 5, it has length 97; 
After step 10, it has length 3073. After step 10, B occurs 1749 times, C occurs 298 times, H occurs 161 times, and N occurs 865 times; taking the quantity of the most common element (B, 1749) and subtracting the quantity of the least common element (H, 161) produces 1749 - 161 = 1588.
'''