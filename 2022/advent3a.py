
def findduplicate(runsack1, runsack2):
    print (runsack1+runsack2)


def calculatescore (play1, play2):
    score=0
    if play2=='X':
        score=1
    elif play2=='Y':
        score=2
    elif play2=='Z':
        score=3

    if ((play1=='C' and play2=='X') or (play1=='B' and play2=='Z') or (play1=='A' and play2=='Y')):
        return score+6
    elif (play1=='B' and play2=='Y') or (play1=='C' and play2=='Z') or (play1=='A' and play2=='X'):
        return score+3
    else:
        return score+0

f1 = open("/Users/mborkar/PycharmProjects/adventofcode/2022/advent3input.txt", "r")
inputlist = f1.readlines()

myTotalScore=0

for i in range (0,3):
    runsack = inputlist[i].replace('\n', '')
    print(runsack)
    length = int(len(runsack)/2)
    runsack1 = list(runsack[0:length])
    runsack2 = list(runsack[length+1:])
    print (runsack1)
    print (runsack2)
    print (set(runsack1).intersection(runsack2))
    common=''
    common=str(set(runsack1).intersection(runsack2))
    print (common)
    print (ord(common[0]))

print (ord('w'))
print (ord('B')-65+27)
