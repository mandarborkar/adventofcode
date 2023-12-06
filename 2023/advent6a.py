
racedetails = [[56,546],[97,1927],[78,1131],[75,1139]]
racetest = [[7,9],[15,40],[30,200]]

def calculatecombinations (time,distance):
    combinations=0
    for i in range (0,time+1):
        d1 = (i * (time-i))
        if d1 > distance:
            print (time,distance,i,d1)
            combinations +=1
    return combinations
'''
Part A test data
c1 = calculatecombinations (7,9)
c2 = calculatecombinations (15,40)
c3 = calculatecombinations (30,200)

Part A 
c1 = calculatecombinations (56,546)
c2 = calculatecombinations (97,1927)
c3 = calculatecombinations (78,1131)
c4 = calculatecombinations (75,1139)

Part B test data
c1 = calculatecombinations (71530,940200)

Part B
'''
c1 = calculatecombinations (56977875,546192711311139)

print (c1)