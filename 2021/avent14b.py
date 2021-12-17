
filename = '/Users/mborkar/PycharmProjects/adventofcode/2021/avent14testinput.txt'

f1 = open(filename, "r")
polymer1 = f1.readlines()

polymerx = polymer1[0].replace(' ','').replace('\n','')
# print (polymerx)

polycode=[]
polydic={}
for x in polymer1[2:]:
    polycode.append(x.replace(' ','').replace('\n','').split('->'))
    polycode[len(polycode)-1].append(0);
    polydic[polycode[len(polycode)-1][0]] = [polycode[len(polycode)-1][1],0]

print (polydic)

for i in range (0,len(polymerx)-1):
    polykey = polymerx[i:i + 2]
    if polykey in polydic:
        # polydic.update({polykey:[polydic[polykey][0],polydic[polykey][1]+1]})
        polyval = list(polydic[polykey])
        newpolycount = polyval[1]
        # print (polyval)
        if len(polyval[0]) > 0:
            newpolyval1 = polykey[0] + polyval[0][0]
            newpolyval2 = polyval[0][0] + polykey[1]
            polydic.update({newpolyval1: ['',newpolycount+1]})
            polydic.update ({newpolyval2: ['', newpolycount+1]} )
            polydic.update({polykey:[polyval,0]})
        else:
            polydic.update ( {polykey: ['', 1]} )
    else:
        polydic.update ( {polykey: ['', newpolycount+1]} )

for x,y  in polydic.items():
    if y[1]>0:
        print ('Null found '+ str(x),str(y))
    # else:
      #  print (x,y)
# print (polydic)
'''
# print (polycode)
i = 0
for i in range(0,10):
    polymery = polymerx[0]
    for i in range (0,len(polymerx)-1):
        strx = polymerx[i:i+2]
        polymery += polymerx[i+1:i+1]
        # print ('str = '+strx+ ' '+ str(polymery))
        foundpoly = []
        for x in polycode:
            if x[0].find(strx) != -1 :
                # print ('found ' + x[0]+' '+strx+' ' + x[1])
                foundpoly.append(x)
                polymery += x[1]
        polymery += polymerx[i+1:i+2]
    # print (polymery)
    polymerx = polymery

polyset = set(polymery)
polydic = {}
for x in polyset:
    # print (x)
    # print (polymery.count(x))
    polydic.update({x:polymery.count(x)})

print (polydic)

key_max = max(polydic.keys(), key=(lambda k: polydic[k]))
key_min = min(polydic.keys(), key=(lambda k: polydic[k]))

print('Maximum Value: ',polydic[key_max])
print('Minimum Value: ',polydic[key_min])
print('Diff : ', str(polydic[key_max]-polydic[key_min]))
'''