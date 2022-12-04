
f1 = open("/Users/mborkar/PycharmProjects/adventofcode/2022/advent3input.txt", "r")
inputlist = f1.readlines()

myTotalScore = 0

for i in range (0,len(inputlist)):
    runsack = inputlist[i].replace('\n', '')

    length = int(len(runsack)/2)
    runsack1 = list(runsack[0:length])
    runsack2 = list(runsack[length:])

    print('\ncounter = ' + str(i))
    print(runsack)
    print(runsack1)
    print(runsack2)
    print(list(set(runsack1) & set(runsack2)))
    print('length = ' + str(len(list(set(runsack1) & set(runsack2)))))

    if list(set(runsack1) & set(runsack2)) :
        for j in range (0,len(list(set(runsack1) & set(runsack2)))):
            common = ord(list(set(runsack1) & set(runsack2))[j])

            if common > 91:
                common -= 96
            else:
                common -= 38

            myTotalScore += common

            print(list(set(runsack1) & set(runsack2))[j])
            print('Add to score ' + str(common))
            print('Current score ' + str(myTotalScore))

print('My final score ' + str(myTotalScore))


print (ord('a')-96)
print (ord('z')-96)
print('')
print (ord('A')-38)
print (ord('Z')-38)


